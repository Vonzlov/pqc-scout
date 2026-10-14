"""Сборка графа: узлы, рёбра и компиляция."""


def build_graph():
    """Собирает и компилирует граф этапа 1.

    TODO(этап 1, задание 1). Схема графа:

        START → scan → pick ──→ assess
                        │ ↑        │
                        │ └────────┘
                        └──→ report → END

    1. Создай StateGraph(ScoutState).
    2. Добавь четыре узла: scan, pick, assess, report.
    3. Обычные рёбра: START → scan, scan → pick, assess → pick, report → END.
    4. Из pick — условное ребро через route_after_pick.
    5. Верни скомпилированный граф: builder.compile().

    Понадобятся импорты:
        from langgraph.graph import END, START, StateGraph
        from pqc_scout.graph.nodes import assess, pick, report, route_after_pick, scan
        from pqc_scout.graph.state import ScoutState
    """
    raise NotImplementedError("TODO(этап 1, задание 1)")
