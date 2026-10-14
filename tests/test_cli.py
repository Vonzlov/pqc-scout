"""Проверки командной строки: команды на месте, заглушки честно сообщают о себе."""

from typer.testing import CliRunner

from pqc_scout.cli import app

runner = CliRunner()


def test_help_lists_all_commands():
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    for command in ("scan", "analyze", "eval"):
        assert command in result.output


def test_scan_stub_exits_with_error():
    result = runner.invoke(app, ["scan", "."])

    assert result.exit_code == 1
    assert "not implemented yet" in result.output
