from aqt import mw
from aqt.editor import Editor, EditorMode

config = mw.addonManager.getConfig(__name__)


def revert_content(editor: Editor):
    # 只在首次打开时执行
    if getattr(editor, "_my_addon_inited", False):
        return

    editor._my_addon_inited = True

    if editor.editorMode != EditorMode.ADD_CARDS:
        return
    if editor.note.note_type()["name"] != config["notetype_name"]:
        return
    if not editor.note["Locale"]:
        return
    field_content = config["field_content"]
    editor.note[field_content] = editor.note[field_content].replace(
        config["locale_placeholder"], editor.note[config["field_locale"]]
    )
    editor.note[config["field_locale_alt"]] = ""
    editor.note[config["field_locale_tips"]] = ""
    editor.loadNoteKeepingFocus()
