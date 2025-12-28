import os
from datetime import datetime
from uuid import uuid4
from sqlalchemy import (
    Column, String, Text, Integer, Float, DateTime, ForeignKey, JSON, LargeBinary,
    create_engine, MetaData
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, relationship

DATABASE_URL = os.environ.get('DATABASE_URL', '')
ASYNC_DATABASE_URL = DATABASE_URL.replace('postgresql://', 'postgresql+asyncpg://').replace('postgres://', 'postgresql+asyncpg://')

Base = declarative_base()
metadata = MetaData()

class FlaskUser(Base):
    __tablename__ = 'flask_users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    universe_state = Column(JSONB, default={
        "tau_0": 41.9,
        "alpha": 0.333333,
        "n_g": 1.1547,
        "R_max": "Lambda_Limit"
    })
    global_sync_version = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    conversations = relationship("FlaskConversation", back_populates="user", cascade="all, delete-orphan")
    snapshots = relationship("StateSnapshot", back_populates="user", cascade="all, delete-orphan")


class FlaskConversation(Base):
    __tablename__ = 'flask_conversations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('flask_users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(255), default='GRUT Chat')
    constants = Column(JSONB, default={
        "tau_0": 41.9,
        "alpha": 0.333333,
        "n_g": 1.1547,
        "R_max": "Lambda_Limit"
    })
    parent_conversation_id = Column(UUID(as_uuid=True), ForeignKey('flask_conversations.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("FlaskUser", back_populates="conversations")
    messages = relationship("FlaskMessage", back_populates="conversation", cascade="all, delete-orphan", order_by="FlaskMessage.created_at")
    parent = relationship("FlaskConversation", remote_side=[id], backref="forks")


class FlaskMessage(Base):
    __tablename__ = 'flask_messages'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey('flask_conversations.id', ondelete='CASCADE'), nullable=False)
    role = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    chi_squared = Column(Float, nullable=True)
    kernel_weight = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    conversation = relationship("FlaskConversation", back_populates="messages")


class StateSnapshot(Base):
    __tablename__ = 'state_snapshots'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('flask_users.id', ondelete='CASCADE'), nullable=False)
    conversation_id = Column(UUID(as_uuid=True), ForeignKey('flask_conversations.id', ondelete='SET NULL'), nullable=True)
    
    snapshot_type = Column(String(50), default='manual')
    
    chi_squared_metrics = Column(JSONB, default={})
    kernel_weights = Column(JSONB, default={})
    universe_state = Column(JSONB, default={})
    
    serialized_state = Column(LargeBinary, nullable=True)
    
    bullet_cluster_chi2 = Column(Float, nullable=True)
    cmb_chi2 = Column(Float, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    description = Column(Text, nullable=True)
    
    user = relationship("FlaskUser", back_populates="snapshots")
    conversation = relationship("FlaskConversation")


async_engine = None
AsyncSessionLocal = None

def get_async_engine():
    global async_engine
    if async_engine is None:
        async_engine = create_async_engine(
            ASYNC_DATABASE_URL,
            echo=False,
            pool_pre_ping=True
        )
    return async_engine

def get_async_session():
    global AsyncSessionLocal
    if AsyncSessionLocal is None:
        AsyncSessionLocal = async_sessionmaker(
            bind=get_async_engine(),
            class_=AsyncSession,
            expire_on_commit=False
        )
    return AsyncSessionLocal


async def init_async_db():
    engine = get_async_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("[SQLAlchemy] Async database tables initialized")
