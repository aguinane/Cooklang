import pytest
from typer.testing import CliRunner

from cooklang.cli import app


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(app, ["--help"])
    assert "cooklang" in result.stdout
    assert result.exit_code == 0


def test_cli_from_nyum(runner):
    result = runner.invoke(app, ["from-nyum", "examples/", "test-output"])
    assert "Converted" in result.stdout
    assert result.exit_code == 0


def test_cli_to_nyum(runner):
    result = runner.invoke(app, ["to-nyum", "examples/", "test-output"])
    assert "Converted" in result.stdout
    assert result.exit_code == 0


def test_cli_to_chowdown(runner):
    result = runner.invoke(app, ["to-chowdown", "examples/", "test-output"])
    assert "Converted" in result.stdout
    assert result.exit_code == 0
