import json
import pickle
import math
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional, List, Dict, Any
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import (
    FlaskUser, FlaskConversation, FlaskMessage, StateSnapshot,
    get_async_session, get_async_engine
)

DEFAULT_UNIVERSE_STATE = {
    "tau_0": 41.9,
    "alpha": 0.333333,
    "n_g": 1.1547,
    "R_max": "Lambda_Limit"
}


def compute_retarded_kernel(t: float, tau_0: float, alpha: float) -> float:
    return (alpha / tau_0) * math.exp(-t / tau_0)


def compute_chi_squared_bullet_cluster(tau_0: float, alpha: float, n_g: float) -> float:
    t_collision = 150.0
    observed_offset = 720.0
    kernel_weight = compute_retarded_kernel(t_collision, tau_0, alpha)
    predicted_offset = 4500.0 * t_collision * kernel_weight * n_g / 1000.0
    residual = (observed_offset - predicted_offset) / observed_offset
    return residual ** 2


def compute_chi_squared_cmb(tau_0: float) -> float:
    tau_target = 41.9
    residual = (tau_0 - tau_target) / tau_target
    return residual ** 2


class PersistenceService:
    def __init__(self):
        self.SessionLocal = get_async_session()
    
    async def get_session(self) -> AsyncSession:
        return self.SessionLocal()
    
    async def get_user_by_id(self, user_id: str) -> Optional[FlaskUser]:
        async with self.SessionLocal() as session:
            result = await session.execute(
                select(FlaskUser).where(FlaskUser.id == UUID(user_id))
            )
            return result.scalar_one_or_none()
    
    async def create_conversation(
        self,
        user_id: str,
        title: str = "GRUT Chat",
        constants: Optional[Dict] = None
    ) -> FlaskConversation:
        async with self.SessionLocal() as session:
            conv = FlaskConversation(
                user_id=UUID(user_id),
                title=title,
                constants=constants or DEFAULT_UNIVERSE_STATE.copy()
            )
            session.add(conv)
            await session.commit()
            await session.refresh(conv)
            return conv
    
    async def get_user_conversations(self, user_id: str) -> List[FlaskConversation]:
        async with self.SessionLocal() as session:
            result = await session.execute(
                select(FlaskConversation)
                .where(FlaskConversation.user_id == UUID(user_id))
                .options(selectinload(FlaskConversation.messages))
                .order_by(FlaskConversation.updated_at.desc())
            )
            return list(result.scalars().all())
    
    async def get_conversation(self, conversation_id: str, user_id: str) -> Optional[FlaskConversation]:
        async with self.SessionLocal() as session:
            result = await session.execute(
                select(FlaskConversation)
                .where(
                    FlaskConversation.id == UUID(conversation_id),
                    FlaskConversation.user_id == UUID(user_id)
                )
                .options(selectinload(FlaskConversation.messages))
            )
            return result.scalar_one_or_none()
    
    async def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
        chi_squared: Optional[float] = None,
        kernel_weight: Optional[float] = None
    ) -> FlaskMessage:
        async with self.SessionLocal() as session:
            message = FlaskMessage(
                conversation_id=UUID(conversation_id),
                role=role,
                content=content,
                chi_squared=chi_squared,
                kernel_weight=kernel_weight
            )
            session.add(message)
            
            await session.execute(
                update(FlaskConversation)
                .where(FlaskConversation.id == UUID(conversation_id))
                .values(updated_at=datetime.utcnow())
            )
            
            await session.commit()
            await session.refresh(message)
            return message
    
    async def save_universe_state_atomic(
        self,
        user_id: str,
        conversation_id: Optional[str] = None,
        description: Optional[str] = None,
        snapshot_type: str = "manual"
    ) -> StateSnapshot:
        async with self.SessionLocal() as session:
            async with session.begin():
                user_result = await session.execute(
                    select(FlaskUser).where(FlaskUser.id == UUID(user_id))
                )
                user = user_result.scalar_one_or_none()
                if user is None:
                    raise ValueError("User not found")
                
                universe_state: Dict[str, Any] = dict(user.universe_state) if user.universe_state else DEFAULT_UNIVERSE_STATE.copy()  # type: ignore
                tau_0: float = universe_state.get('tau_0', 41.9)  # type: ignore
                alpha: float = universe_state.get('alpha', 0.333333)  # type: ignore
                n_g: float = universe_state.get('n_g', 1.1547)  # type: ignore
                
                bullet_chi2 = compute_chi_squared_bullet_cluster(tau_0, alpha, n_g)
                cmb_chi2 = compute_chi_squared_cmb(tau_0)
                
                kernel_weights = {}
                t_values = [0, 10, 20, 30, 41.9, 50, 83.8, 100, 150]
                for t in t_values:
                    kernel_weights[f"K({t})"] = compute_retarded_kernel(t, tau_0, alpha)
                
                chi_squared_metrics = {
                    "bullet_cluster": bullet_chi2,
                    "cmb": cmb_chi2,
                    "total": bullet_chi2 + cmb_chi2,
                    "timestamp": datetime.utcnow().isoformat()
                }
                
                serialized_data = {
                    "universe_state": universe_state,
                    "chi_squared_metrics": chi_squared_metrics,
                    "kernel_weights": kernel_weights,
                    "kernel_formula": "K(t) = (alpha/tau_0) * exp(-t/tau_0)"
                }
                serialized_blob = pickle.dumps(serialized_data)
                
                snapshot = StateSnapshot(
                    user_id=UUID(user_id),
                    conversation_id=UUID(conversation_id) if conversation_id else None,
                    snapshot_type=snapshot_type,
                    universe_state=universe_state,
                    chi_squared_metrics=chi_squared_metrics,
                    kernel_weights=kernel_weights,
                    serialized_state=serialized_blob,
                    bullet_cluster_chi2=bullet_chi2,
                    cmb_chi2=cmb_chi2,
                    description=description or f"State snapshot at {datetime.utcnow().isoformat()}"
                )
                
                session.add(snapshot)
            
            await session.refresh(snapshot)
            return snapshot
    
    async def get_user_snapshots(self, user_id: str, limit: int = 10) -> List[StateSnapshot]:
        async with self.SessionLocal() as session:
            result = await session.execute(
                select(StateSnapshot)
                .where(StateSnapshot.user_id == UUID(user_id))
                .order_by(StateSnapshot.created_at.desc())
                .limit(limit)
            )
            return list(result.scalars().all())
    
    async def restore_snapshot(self, snapshot_id: str, user_id: str) -> Optional[Dict]:
        async with self.SessionLocal() as session:
            result = await session.execute(
                select(StateSnapshot).where(
                    StateSnapshot.id == UUID(snapshot_id),
                    StateSnapshot.user_id == UUID(user_id)
                )
            )
            snapshot = result.scalar_one_or_none()
            
            if not snapshot:
                return None
            
            if snapshot.serialized_state is not None:
                restored_data = pickle.loads(snapshot.serialized_state)  # type: ignore
                
                await session.execute(
                    update(FlaskUser)
                    .where(FlaskUser.id == UUID(user_id))
                    .values(universe_state=restored_data.get('universe_state', {}))
                )
                await session.commit()
                
                return restored_data
            
            return {
                "universe_state": snapshot.universe_state,
                "chi_squared_metrics": snapshot.chi_squared_metrics,
                "kernel_weights": snapshot.kernel_weights
            }
    
    async def delete_conversation(self, conversation_id: str, user_id: str) -> bool:
        async with self.SessionLocal() as session:
            await session.execute(
                delete(FlaskConversation).where(
                    FlaskConversation.id == UUID(conversation_id),
                    FlaskConversation.user_id == UUID(user_id)
                )
            )
            await session.commit()
            return True


persistence_service = PersistenceService()
