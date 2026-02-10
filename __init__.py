from aqt.gui_hooks import (
    collection_did_load,
    editor_did_init_buttons,
    editor_did_load_note,
)

from .add_notetype import on_collection_loaded

from .revert_content import revert_content
from .new_button import add_my_replace_button

editor_did_init_buttons.append(add_my_replace_button)
editor_did_load_note.append(revert_content)
collection_did_load.append(on_collection_loaded)
