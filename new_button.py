from aqt import mw
from aqt.editor import Editor
from aqt.utils import tooltip

config = mw.addonManager.getConfig(__name__)


def on_replace_and_return(editor: Editor):
    def got_selection(original_text: str):
        if not original_text:
            tooltip("No text selected", period=1500)
            return

        editor.web.eval(
            f"""
            document.execCommand("insertText", false, {config["locale_placeholder"]!r});
            """
        )

        def on_saved():
            field_locale = config["field_locale"]
            locale_idx = editor.note.keys().index(field_locale)
            if locale_idx == -1:
                tooltip(f"Field {field_locale} not found in note", period=1500)
                return
            editor.note[field_locale] = original_text
            editor.loadNote(focusTo=locale_idx)

        editor.call_after_note_saved(on_saved, keepFocus=True)

    if editor.note.note_type()["name"] != config["notetype_name"]:
        tooltip(f"Not a {config['notetype_name']} note", period=1500)
        return

    # 先异步获取选中文本（最准的方式）
    js_get_sel = """
        (function() {
            var sel = window.getSelection();
            if (sel.rangeCount) {
                return sel.toString();
            }
            return "";
        })();
    """
    editor.web.evalWithCallback(js_get_sel, got_selection)


def add_my_replace_button(buttons, editor):
    btn = editor.addButton(
        icon=None,
        cmd="extract_locale_text",
        func=on_replace_and_return,
        tip=f"Extract Locale ({config['extract_shortcut']})",
        label="✂️",
        keys=config["extract_shortcut"],
    )
    buttons.append(btn)
    return buttons
