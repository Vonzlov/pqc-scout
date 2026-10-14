"""Состояние графа: общие данные одного прогона, которые видят все узлы."""

from typing import TypedDict


class ScoutState(TypedDict, total=False):
    """Состояние прогона pqc-scout.

    TODO(этап 1, задание 1): опиши четыре поля.

    queue        — находки, которые ещё не разобраны: list[dict].
    current      — находка, которую разбираем сейчас: dict | None.
                   None означает, что очередь кончилась.
    assessments  — оценки уже разобранных находок: list[dict].
                   Узел assess каждый раз возвращает одну оценку, и они должны
                   копиться, а не затирать друг друга. Для этого полю нужен редьюсер:
                   Annotated[list[dict], operator.add] (понадобятся
                   `import operator` и `from typing import Annotated`).
    report       — итоговый текст отчёта: str.
    """
