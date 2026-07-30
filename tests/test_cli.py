import subprocess
import sys


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "promptforge", *args],
        capture_output=True,
        text=True,
    )


def test_help():
    result = run_cli("--help")

    assert result.returncode == 0
    assert "PromptForge CLI" in result.stdout
    assert "validate" in result.stdout


def test_version():
    result = run_cli("--version")

    assert result.returncode == 0
    assert "PromptForge" in result.stdout


def test_no_arguments():
    result = run_cli()

    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()


def test_unknown_command():
    result = run_cli("does-not-exist")

    assert result.returncode != 0