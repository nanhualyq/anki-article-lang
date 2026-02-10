from aqt.editor import Editor, EditorMode

def revert_content(editor: Editor):
    print(editor.note)
    # 只在首次打开时执行
    if getattr(editor, "_my_addon_inited", False):
        return

    editor._my_addon_inited = True

    if editor.editorMode != EditorMode.ADD_CARDS:
        return
    if editor.note.note_type()["name"] != "@ArticleLang":
        return
    if not editor.note["Locale"]:
        return
    editor.note["Content"] = editor.note["Content"].replace(
        "!???!", editor.note["Locale"]
    )
    editor.note['LocaleAlt'] = ''
    editor.note['LocaleTips'] = ''
    editor.loadNoteKeepingFocus()
