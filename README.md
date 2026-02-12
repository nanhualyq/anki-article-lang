# Introduction

This is a tool to help you learn languages on Anki. The `@ArticleLang.apkg` note type preserves original context, enabling progressive learning of any details you desire. The addon supports quick card creation, allowing one-click extraction of partial text into corresponding fields to reduce repetitive work.

<!-- gif -->
![notetype](https://github.com/user-attachments/assets/f2c8cdeb-ae21-46cd-99dc-e190cee88cab)

![addon](https://github.com/user-attachments/assets/6f2a97a9-eff7-426d-a828-0cf1810f3214)

# 介绍
这是一个帮助你在anki上学习语言的工具，`@ArticleLang.apkg` 笔记类型支持保留原文上下文，渐进式的学习任何你想要的细节。插件支持快捷的做卡，可以一键提取局部文本到对应字段，减少重复劳动。

## Usage
- Download and import note types

https://github.com/nanhualyq/anki-article-lang/releases/download/apkg/@ArticleLang.apkg

- Add the addon

Copy the repository code to your Anki addons directory, e.g., `~/.local/share/Anki2/addons21/article_lang`

## 使用
- 下载并导入笔记类型

https://github.com/nanhualyq/anki-article-lang/releases/download/apkg/@ArticleLang.apkg

- 添加插件

复制本仓库代码到anki addons目录下，比如 `~/.local/share/Anki2/addons21/article_lang`

## for dev
```bash
ln -s $PWD ~/.local/share/Anki2/addons21/article_lang

DEBUG=1 anki -p manong

zip -r article_lang.ankiaddon *
```