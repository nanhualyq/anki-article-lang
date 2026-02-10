from aqt import mw
from anki.models import ModelManager

MODEL_NAME = "@ArticleLang"


def get_style():
    return """
.card {
  font-family: arial;
  font-size: 20px;
  line-height: 1.5;
  /* text-align: center; */
  color: black;
  background-color: white;
}

#popover-button {
  display: none;
}
#mark-box {
	scroll-margin-top: 40vh;
}
    """


def get_read_tmpl(mm: ModelManager):
    tmpl = mm.new_template("Read")
    tmpl["qfmt"] = '''
<div id="field-content">{{Content}}</div>
<hr />
{{Info}}

<script>
  function musk() {
    const MUSK_STRING = "!???!";
    const mark = `<mark id="mark-box" onclick="document.getElementById('popover-button')?.click()">{{Locale}}</mark>`;
    const box = document.getElementById("field-content");
    box.innerHTML = box.innerHTML.replace(MUSK_STRING, mark);
  }
  musk();
  setTimeout(() => {
    location.hash = ''
    location.hash = '#mark-box'
  }, 0);
</script>
    '''
    tmpl["afmt"] = '''
{{FrontSide}}
<button id="popover-button" popovertarget="my-popover">Toggle Popover</button>
<div id="my-popover" popover>
  {{LocaleAlt}}
  {{#LocaleTips}}<br>{{LocaleTips}}{{/LocaleTips}}
  {{#Locale}}
    <br>
    {{tts en_US :Locale}}
  {{/Locale}}
</div>

<script>
  document.getElementById('popover-button')?.click()
</script>
    '''
    return tmpl

def get_speak_tmpl(mm: ModelManager):
    tmpl = mm.new_template("Speak")
    tmpl["qfmt"] = '''
{{#Locale}}
  {{^-Speak}}
    <div id="field-content">{{Content}}</div>
    <hr />
    {{Info}}
  {{/-Speak}}
{{/Locale}}

<script>
  function musk() {
    const MUSK_STRING = "!???!";
    const mark = `<mark id="mark-box" onclick="document.getElementById('popover-button')?.click()">🎤{{Locale}}🎤</mark>`;
    const box = document.getElementById("field-content");
    box.innerHTML = box.innerHTML.replace(MUSK_STRING, mark);
  }
  musk();
  setTimeout(() => {
    location.hash = ''
    location.hash = '#mark-box'
  }, 0);
</script>
    '''
    tmpl["afmt"] = '''
{{FrontSide}}
<button id="popover-button" popovertarget="my-popover">Toggle Popover</button>
<div id="my-popover" popover>
  {{tts en_US :Locale}}
  <br>{{LocaleAlt}}
  {{#LocaleTips}}<br>{{LocaleTips}}{{/LocaleTips}}
</div>

<script>
  document.getElementById("popover-button")?.click();
</script>
    '''
    return tmpl

def get_write_tmpl(mm: ModelManager):
    tmpl = mm.new_template("Write")
    tmpl["qfmt"] = '''
{{#Locale}}
  {{^-Write}}
    <div id="field-content">{{Content}}</div>
    <hr />
    {{Info}}
  {{/-Write}}
{{/Locale}}

<script>
  function musk() {
    const MUSK_STRING = "!???!";
    const mark = `<mark id="mark-box" onclick="document.getElementById('popover-button')?.click()">{{LocaleAlt}}</mark>`;
    const box = document.getElementById("field-content");
    box.innerHTML = box.innerHTML.replace(MUSK_STRING, mark);
  }
  musk();
  setTimeout(() => {
    location.hash = ''
    location.hash = '#mark-box'
  }, 0);
</script>
    '''
    tmpl["afmt"] = '''
{{FrontSide}}
<button id="popover-button" popovertarget="my-popover">Toggle Popover</button>
<div id="my-popover" popover>
  {{Locale}}
  <br />
  {{tts en_US :Locale}}
</div>

<script>
  document.getElementById("popover-button")?.click();
</script>
    '''
    return tmpl

def get_listen_tmpl(mm: ModelManager):
    tmpl = mm.new_template("Listen")
    tmpl["qfmt"] = '''
{{#Locale}}
  {{^-Listen}}
    {{tts en_US :Locale}}
    <div id="field-content">{{Content}}</div>
    <hr />
    {{Info}}
  {{/-Listen}}
{{/Locale}}

<script>
  function musk() {
    const MUSK_STRING = "!???!";
    const mark = `<mark id="mark-box" onclick="document.getElementById('popover-button')?.click()"></mark>`;
    const box = document.getElementById("field-content");
    box.innerHTML = box.innerHTML.replace(MUSK_STRING, mark);
    document.getElementById('mark-box').appendChild(document.querySelector('.replay-button'))
  }
  musk();
  setTimeout(() => {
    location.hash = ''
    location.hash = '#mark-box'
  }, 0);
</script>
    '''
    tmpl["afmt"] = '''
{{FrontSide}}
<button id="popover-button" popovertarget="my-popover">Toggle Popover</button>
<div id="my-popover" popover>
  {{Locale}}
  {{#LocaleTips}}<br>{{LocaleTips}}{{/LocaleTips}}
</div>

<script>
  document.getElementById("popover-button")?.click();
</script>
    '''
    return tmpl


def ensure_model():
    mm = mw.col.models

    model = mm.by_name(MODEL_NAME)
    if model:
        return model

    # 新建 note type
    model = mm.new(MODEL_NAME)

    # 添加字段
    mm.add_field(model, mm.new_field("Content"))
    mm.add_field(model, mm.new_field("Info"))
    mm.add_field(model, mm.new_field("Locale"))
    mm.add_field(model, mm.new_field("LocaleAlt"))
    mm.add_field(model, mm.new_field("LocaleTips"))
    mm.add_field(model, mm.new_field("-Write"))
    mm.add_field(model, mm.new_field("-Listen"))
    mm.add_field(model, mm.new_field("-Speak"))

    model["css"] = get_style()

    mm.add_template(model, get_read_tmpl(mm))
    mm.add_template(model, get_speak_tmpl(mm))
    mm.add_template(model, get_write_tmpl(mm))
    mm.add_template(model, get_listen_tmpl(mm))

    # 保存
    mm.add(model)
    mm.save(model)

    return model


def on_collection_loaded(col):
    ensure_model()
