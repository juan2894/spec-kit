"""Regression guard: console symbols must remain importable from specify_cli."""
from specify_cli import (
    console,
    StepTracker,
    get_key,
    select_with_arrows,
    BannerGroup,
    show_banner,
    BANNER,
    TAGLINE,
)


def test_console_symbols_importable():
    from rich.console import Console
    assert isinstance(console, Console)


def test_console_symbols_available_from_star_import():
    namespace = {}
    exec("from specify_cli import *", namespace)

    for symbol in (
        "console",
        "StepTracker",
        "get_key",
        "select_with_arrows",
        "BannerGroup",
        "show_banner",
        "BANNER",
        "TAGLINE",
    ):
        assert symbol in namespace


def test_step_tracker_instantiable():
    tracker = StepTracker("test")
    tracker.add("step1", "Step One")
    tracker.complete("step1", "done")
    assert tracker.steps[0]["status"] == "done"


def test_step_tracker_add_duplicate_key():
    tracker = StepTracker("test")
    tracker.add("step1", "Step One")
    tracker.add("step1", "Step One Duplicate")
    assert len(tracker.steps) == 1
    assert tracker.steps[0]["label"] == "Step One"


def test_step_tracker_transitions_existing_step():
    tracker = StepTracker("test")
    tracker.add("s1", "Step 1")

    tracker.start("s1", detail="starting")
    assert tracker.steps[0]["status"] == "running"
    assert tracker.steps[0]["detail"] == "starting"

    tracker.complete("s1", detail="finished")
    assert tracker.steps[0]["status"] == "done"
    assert tracker.steps[0]["detail"] == "finished"

    tracker.error("s1", detail="failed")
    assert tracker.steps[0]["status"] == "error"
    assert tracker.steps[0]["detail"] == "failed"

    tracker.skip("s1", detail="bypassed")
    assert tracker.steps[0]["status"] == "skipped"
    assert tracker.steps[0]["detail"] == "bypassed"


def test_step_tracker_transitions_unknown_key_creates_step():
    tracker = StepTracker("test")

    tracker.start("unknown_start", detail="in progress")
    assert len(tracker.steps) == 1
    assert tracker.steps[0] == {
        "key": "unknown_start",
        "label": "unknown_start",
        "status": "running",
        "detail": "in progress",
    }

    tracker.complete("unknown_complete", detail="finished")
    assert len(tracker.steps) == 2
    assert tracker.steps[1] == {
        "key": "unknown_complete",
        "label": "unknown_complete",
        "status": "done",
        "detail": "finished",
    }

    tracker.error("unknown_error", detail="something went wrong")
    assert len(tracker.steps) == 3
    assert tracker.steps[2] == {
        "key": "unknown_error",
        "label": "unknown_error",
        "status": "error",
        "detail": "something went wrong",
    }

    tracker.skip("unknown_skip", detail="not needed")
    assert len(tracker.steps) == 4
    assert tracker.steps[3] == {
        "key": "unknown_skip",
        "label": "unknown_skip",
        "status": "skipped",
        "detail": "not needed",
    }


def test_step_tracker_refresh_callback():
    tracker = StepTracker("test")
    calls = []

    def callback():
        calls.append(True)

    tracker.attach_refresh(callback)
    tracker.add("s1", "Step 1")
    assert len(calls) == 1

    tracker.start("s1")
    assert len(calls) == 2


def test_step_tracker_refresh_callback_exception_suppression():
    tracker = StepTracker("test")

    def failing_callback():
        raise RuntimeError("refresh failed")

    tracker.attach_refresh(failing_callback)
    # Adding a step should invoke callback and swallow exception without crashing
    tracker.add("s1", "Step 1")
    assert len(tracker.steps) == 1


def test_step_tracker_render():
    from rich.tree import Tree

    tracker = StepTracker("Test Title")
    tracker.add("s1", "Pending Step")
    tracker.add("s2", "Running Step")
    tracker.start("s2", detail="in progress")
    tracker.add("s3", "Done Step")
    tracker.complete("s3")
    tracker.add("s4", "Error Step")
    tracker.error("s4", detail="failed")
    tracker.add("s5", "Skipped Step")
    tracker.skip("s5")
    tracker._update("s6", status="unknown_status", detail="custom")

    tree = tracker.render()
    assert isinstance(tree, Tree)
    assert tree.label == "[cyan]Test Title[/cyan]"
    children_text = [str(child.label) for child in tree.children]

    assert children_text[0] == "[green dim]○[/green dim] [bright_black]Pending Step[/bright_black]"
    assert children_text[1] == "[cyan]○[/cyan] [white]Running Step[/white] [bright_black](in progress)[/bright_black]"
    assert children_text[2] == "[green]●[/green] [white]Done Step[/white]"
    assert children_text[3] == "[red]●[/red] [white]Error Step[/white] [bright_black](failed)[/bright_black]"
    assert children_text[4] == "[yellow]○[/yellow] [white]Skipped Step[/white]"
    assert children_text[5] == "  [white]s6[/white] [bright_black](custom)[/bright_black]"


def test_select_with_arrows_raises_on_empty_options():
    import pytest
    with pytest.raises(ValueError, match="at least one option"):
        select_with_arrows({})
