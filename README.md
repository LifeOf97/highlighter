# Highlighter

An api backend used to **highlight** code snippet of any programming language.

## Features

* **Code highlighter**.  
Used in highlighting programming languages used in blogs, chat apps and any project requiring code samples.  
This can return the highlighted code in any of this format:-  
    * BBCode [Bulletin Board Code](https://en.wikipedia.org/wiki/BBCode).
    * HTML [Hypertext Markup Language](https://www.w3schools.com/html/html_intro.asp).
    * RTF [Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format).
    * SVG [Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG).
    * Terminal.
    * Terminal256.
    * Text.
    * IRC.

## Request Config

Here are the config options for highlighting code snippets.  
>NOTE: this should be a **POST** request at all times as **GET** request is not supported.