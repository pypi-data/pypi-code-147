"""Tests for libtmux Pane object."""
import logging
import shutil

from libtmux.session import Session

logger = logging.getLogger(__name__)


def test_resize_pane(session: Session) -> None:
    """Test Pane.resize_pane()."""

    window = session.attached_window
    window.rename_window("test_resize_pane")

    pane1 = window.attached_pane
    assert pane1 is not None
    pane1_height = pane1.pane_height
    window.split_window()

    pane1.resize_pane(height=4)
    assert pane1.pane_height != pane1_height
    assert pane1.pane_height is not None
    assert int(pane1.pane_height) == 4

    pane1.resize_pane(height=3)
    assert pane1.pane_height is not None
    assert int(pane1.pane_height) == 3


def test_send_keys(session: Session) -> None:
    pane = session.attached_window.attached_pane
    assert pane is not None
    pane.send_keys("c-c", literal=True)

    pane_contents = "\n".join(pane.cmd("capture-pane", "-p").stdout)
    assert "c-c" in pane_contents

    pane.send_keys("c-a", literal=False)
    assert "c-a" not in pane_contents, "should not print to pane"


def test_set_height(session: Session) -> None:
    window = session.new_window(window_name="test_set_height")
    window.split_window()
    pane1 = window.attached_pane
    assert pane1 is not None
    pane1_height = pane1.pane_height

    pane1.set_height(4)
    assert pane1.pane_height != pane1_height
    assert pane1.pane_height is not None
    assert int(pane1.pane_height) == 4


def test_set_width(session: Session) -> None:
    window = session.new_window(window_name="test_set_width")
    window.split_window()

    window.select_layout("main-vertical")
    pane1 = window.attached_pane
    assert pane1 is not None
    pane1_width = pane1.pane_width

    pane1.set_width(10)
    assert pane1.pane_width != pane1_width
    assert pane1.pane_width is not None
    assert int(pane1.pane_width) == 10

    pane1.reset()


def test_capture_pane(session: Session) -> None:
    env = shutil.which("env")
    assert env is not None, "Cannot find usable `env` in PATH."

    session.new_window(
        attach=True,
        window_name="capture_pane",
        window_shell=f"{env} PS1='$ ' sh",
    )
    pane = session.attached_window.attached_pane
    assert pane is not None
    pane_contents = "\n".join(pane.capture_pane())
    assert pane_contents == "$"
    pane.send_keys(
        r'printf "\n%s\n" "Hello World !"', literal=True, suppress_history=False
    )
    pane_contents = "\n".join(pane.capture_pane())
    assert pane_contents == r'$ printf "\n%s\n" "Hello World !"{}'.format(
        "\n\nHello World !\n$"
    )


def test_capture_pane_start(session: Session) -> None:
    env = shutil.which("env")
    assert env is not None, "Cannot find usable `env` in PATH."

    session.new_window(
        attach=True,
        window_name="capture_pane_start",
        window_shell=f"{env} PS1='$ ' sh",
    )
    pane = session.attached_window.attached_pane
    assert pane is not None
    pane_contents = "\n".join(pane.capture_pane())
    assert pane_contents == "$"
    pane.send_keys(r'printf "%s"', literal=True, suppress_history=False)
    pane_contents = "\n".join(pane.capture_pane())
    assert pane_contents == '$ printf "%s"\n$'
    pane.send_keys("clear -x", literal=True, suppress_history=False)
    pane_contents = "\n".join(pane.capture_pane())
    assert pane_contents == "$"
    pane_contents_start = pane.capture_pane(start=-2)
    assert pane_contents_start[0] == '$ printf "%s"'
    assert pane_contents_start[1] == "$ clear -x"
    assert pane_contents_start[-1] == "$"
    pane_contents_start = pane.capture_pane(start="-")
    assert pane_contents == "$"


def test_capture_pane_end(session: Session) -> None:
    env = shutil.which("env")
    assert env is not None, "Cannot find usable `env` in PATH."

    session.new_window(
        attach=True,
        window_name="capture_pane_end",
        window_shell=f"{env} PS1='$ ' sh",
    )
    pane = session.attached_window.attached_pane
    assert pane is not None
    pane_contents = "\n".join(pane.capture_pane())
    assert pane_contents == "$"
    pane.send_keys(r'printf "%s"', literal=True, suppress_history=False)
    pane_contents = "\n".join(pane.capture_pane())
    assert pane_contents == '$ printf "%s"\n$'
    pane_contents = "\n".join(pane.capture_pane(end=0))
    assert pane_contents == '$ printf "%s"'
    pane_contents = "\n".join(pane.capture_pane(end="-"))
    assert pane_contents == '$ printf "%s"\n$'
