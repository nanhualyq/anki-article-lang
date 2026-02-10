import json
from aqt.editor import Editor, EditorMode
from aqt.utils import tooltip, showInfo


def on_replace_and_return(editor: Editor):
    def got_selection(original_text: str):
        if not original_text:
            tooltip("没有选中文本", period=1500)
            return

        new_content = "!???!"

        editor.web.eval(
            f"""
            document.execCommand("insertText", false, {new_content!r});
            """
        )

        def on_saved():
            if "Locale" in editor.note:
                editor.note["Locale"] = original_text
                editor.loadNoteKeepingFocus()

        editor.call_after_note_saved(on_saved, keepFocus=True)

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
        cmd="extract_en_text_to_cn",
        func=on_replace_and_return,
        tip="Extract En Text",
        label="En",
        keys="Ctrl+Alt+E",
    )
    buttons.append(btn)
    return buttons
