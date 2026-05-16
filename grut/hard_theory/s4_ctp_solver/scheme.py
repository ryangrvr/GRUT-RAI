"""Scheme tracking for the S4 CTP scaffold."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Scheme:
    name: str
    description: str


def ms_bar_scheme() -> Scheme:
    return Scheme(
        name="MS-bar",
        description="Minimal subtraction scheme placeholder.",
    )


def on_shell_scheme() -> Scheme:
    return Scheme(
        name="on-shell",
        description="On-shell renormalization scheme placeholder.",
    )
