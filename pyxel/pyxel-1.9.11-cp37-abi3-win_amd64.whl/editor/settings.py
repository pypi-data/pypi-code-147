import os

import pyxel

EDITOR_IMAGE_FILE = "assets/editor_220x160.png"
EDITOR_IMAGE = pyxel.Image.from_image(
    os.path.join(os.path.dirname(__file__), EDITOR_IMAGE_FILE)
)

APP_WIDTH = 240
APP_HEIGHT = 180

TOOL_SELECT = 0
TOOL_PENCIL = 1
TOOL_RECTB = 2
TOOL_RECT = 3
TOOL_CIRCB = 4
TOOL_CIRC = 5
TOOL_BUCKET = 6

MAX_SOUND_LENGTH = 48
MAX_MUSIC_LENGTH = 32

TEXT_LABEL_COLOR = 7
HELP_MESSAGE_COLOR = 5

PANEL_FOCUS_COLOR = 7
PANEL_FOCUS_BORDER_COLOR = 0
PANEL_SELECT_FRAME_COLOR = 15
PANEL_SELECT_BORDER_COLOR = 0

PIANO_KEYBOARD_REST_COLOR = 12
PIANO_KEYBOARD_PLAY_COLOR = 14

PIANO_ROLL_CURSOR_PLAY_COLOR = 14
PIANO_ROLL_CURSOR_EDIT_COLOR = 6
PIANO_ROLL_CURSOR_SELECT_COLOR = 15
PIANO_ROLL_BACKGROUND_COLOR = 7
PIANO_ROLL_NOTE_COLOR = 8
PIANO_ROLL_REST_COLOR = 5

OCTAVE_BAR_BACKGROUND_COLOR = 7
OCTAVE_BAR_COLOR = 13

SOUND_FIELD_DATA_NORMAL_COLOR = 1
SOUND_FIELD_DATA_SELECT_COLOR = 7
SOUND_FIELD_CURSOR_EDIT_COLOR = 1
SOUND_FIELD_CURSOR_SELECT_COLOR = 2

MUSIC_FIELD_BACKGROUND_COLOR = 6
MUSIC_FIELD_SOUND_NORMAL_COLOR = 1
MUSIC_FIELD_SOUND_SELECT_COLOR = 7
MUSIC_FIELD_CURSOR_PLAY_COLOR = 8
MUSIC_FIELD_CURSOR_EDIT_COLOR = 1
MUSIC_FIELD_CURSOR_SELECT_COLOR = 2
