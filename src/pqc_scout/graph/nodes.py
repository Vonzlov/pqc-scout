"""Узлы графа. На этапе 1 все они — заглушки с фиксированными данными.

Узел — обычная функция: получает состояние и возвращает словарь только с теми полями,
которые нужно обновить. Менять состояние на месте нельзя: LangGraph узнаёт
об изменениях только из возвращённого словаря.
"""

from typing import Literal

from pqc_scout.graph.state import ScoutState

# Фиксированные находки вместо настоящего детектора (он появится на этапе 3)
FAKE_FINDINGS = [
    {
        "id": "F1",
        "file": "app/crypto.py",
        "line": 12,
        "algorithm": "RSA-2048",
        "operation": "keygen",
    },
    {
        "id": "F2",
        "file": "app/tokens.py",
        "line": 40,
        "algorithm": "ECDSA-P256",
        "operation": "sign",
    },
    {
        "id": "F3",
        "file": "tests/test_keys.py",
        "line": 7,
        "algorithm": "X25519",
        "operation": "key_exchange",
    },
]

# Фиксированные приоритеты вместо оценки моделью (она появится на этапе 6)
FAKE_PRIORITIES = {"F1": "P1", "F2": "P2", "F3": "P4"}


def scan(state: ScoutState) -> dict:
    """Кладёт копию FAKE_FINDINGS в очередь, в поле queue."""
    raise NotImplementedError("TODO(этап 1, задание 1)")


def pick(state: ScoutState) -> dict:
    """Берёт первую находку из очереди.

    Возвращает её в поле current, а в поле queue — новый список без неё.
    Если очередь пуста, возвращает current = None.
    """
    raise NotImplementedError("TODO(этап 1, задание 1)")


def route_after_pick(state: ScoutState) -> Literal["assess", "report"]:
    """Решает, куда идти после pick: есть текущая находка — в assess, нет — в report."""
    raise NotImplementedError("TODO(этап 1, задание 1)")


def assess(state: ScoutState) -> dict:
    """Оценивает текущую находку: приоритет берёт из FAKE_PRIORITIES по id.

    Возвращает {"assessments": [{"id": ..., "priority": ...}]}, то есть список
    из одного элемента. Копить оценки будет редьюсер, описанный в состоянии.
    """
    raise NotImplementedError("TODO(этап 1, задание 1)")


def report(state: ScoutState) -> dict:
    """Собирает текст отчёта в поле report: по строке на оценку, вида «F1: P1»."""
    raise NotImplementedError("TODO(этап 1, задание 1)")
