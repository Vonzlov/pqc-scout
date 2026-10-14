"""Этап 1, задание 1: скелет графа на заглушках.

Эти тесты — условие задания. Пока узлы и граф не написаны, тесты падают.
Задание выполнено, когда `uv run pytest` проходит целиком.
"""

from pqc_scout.graph.build import build_graph
from pqc_scout.graph.nodes import FAKE_FINDINGS, assess, pick, report, route_after_pick, scan


def test_scan_puts_all_fake_findings_into_queue():
    update = scan({})

    assert update["queue"] == list(FAKE_FINDINGS)


def test_pick_takes_first_finding_from_queue():
    first, second = FAKE_FINDINGS[0], FAKE_FINDINGS[1]

    update = pick({"queue": [first, second]})

    assert update["current"] == first
    assert update["queue"] == [second]


def test_pick_does_not_change_queue_in_place():
    queue = list(FAKE_FINDINGS)

    pick({"queue": queue})

    # Состояние меняется только через возвращённое обновление
    assert queue == list(FAKE_FINDINGS)


def test_pick_sets_current_to_none_when_queue_is_empty():
    update = pick({"queue": []})

    assert update["current"] is None


def test_route_after_pick():
    assert route_after_pick({"current": FAKE_FINDINGS[0]}) == "assess"
    assert route_after_pick({"current": None}) == "report"


def test_assess_returns_one_assessment_in_a_list():
    update = assess({"current": FAKE_FINDINGS[0]})

    # Список из одного элемента: накапливать оценки будет редьюсер из состояния
    assert update == {"assessments": [{"id": "F1", "priority": "P1"}]}


def test_report_has_a_line_per_assessment():
    state = {"assessments": [{"id": "F1", "priority": "P1"}, {"id": "F3", "priority": "P4"}]}

    text = report(state)["report"]

    assert text.splitlines() == ["F1: P1", "F3: P4"]


def test_graph_assesses_every_finding_exactly_once():
    final_state = build_graph().invoke({})

    assert [a["id"] for a in final_state["assessments"]] == ["F1", "F2", "F3"]
    assert final_state["report"].splitlines() == ["F1: P1", "F2: P2", "F3: P4"]


def test_graph_visits_nodes_in_expected_order():
    graph = build_graph()

    # stream отдаёт обновления по шагам: {имя_узла: что этот узел вернул}
    visited = [node for update in graph.stream({}, stream_mode="updates") for node in update]

    assert visited == [
        "scan",
        "pick",
        "assess",
        "pick",
        "assess",
        "pick",
        "assess",
        "pick",
        "report",
    ]
