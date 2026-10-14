"""Командная строка pqc-scout.

Пока все команды — заглушки. Каждая заработает на своём этапе плана (docs/ROADMAP.md),
а до тех пор честно сообщает, что ещё не готова, и завершается с кодом 1.
"""

from pathlib import Path

import typer

app = typer.Typer(
    help="Find quantum-vulnerable cryptography in Python projects.",
    no_args_is_help=True,
)


def not_implemented(command: str, stage: int) -> None:
    typer.echo(f"'{command}' is not implemented yet (planned for stage {stage}).")
    raise typer.Exit(code=1)


@app.command()
def scan(path: Path) -> None:
    """Find vulnerable cryptography with the rule-based detector (no LLM)."""
    not_implemented("scan", stage=3)


@app.command()
def analyze(path: Path) -> None:
    """Assess each finding and propose a migration patch."""
    not_implemented("analyze", stage=6)


# Функция называется evaluate, чтобы не перекрывать встроенную eval,
# а команда в терминале при этом остаётся `pqc-scout eval`.
@app.command("eval")
def evaluate() -> None:
    """Measure quality on the labeled testbed."""
    not_implemented("eval", stage=3)
