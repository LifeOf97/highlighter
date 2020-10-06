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

```javascript
{
    // code snippet to be highlighted. Required.
    code: '',

    // Programming language of the code snippet to be highlighted. Required. 
    language: 'python', // default

    // Syntax highlighting style.
    style: 'emacs', // default

    // What format would you like to retrieve your code snippet. Required.
    get_format: 'html', // default

    // linenos is used to request if the result should have line numbers
    // or not, this can be one of ['inline', 'table', False], defaults to
    // False, no line numbers.
    linenos: false, // default
    
    // noclasses is used to define if the user requires inline css
    // styling or classes, this can be one of ['inline', 'class']
    styling: 'inline', // default
    
    // class name giving to the div tag wrapping the whole code block
    // defaults to highlighter,
    // NOTE: if linenos is set to table this will append a 'table' making 
    // to it making it 'highlightertable'.
    cssclass: 'highlighter', // default

    // Specify a list of line numbers to be highlighted in your code snippet
    // this should be a array of numbers. Defaults to an empty array.
    hl_lines: [], 
    
    // should the syntax highlighting style selected also affect the
    // overall code background?
    nobackground: false, // default
    
    // prefix the css classes used when 'noclasses' is set 'class'
    classprefix: '', // default is an empty string
}