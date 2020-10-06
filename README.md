# Highlighter

An api backend used to **highlight** code snippet of any programming language.

## Features

* **Code highlighter**.  
Used in highlighting programming languages used in blogs, chat apps and any project requiring code samples.  

 ### Formats Available
    * BBCode [Bulletin Board Code](https://en.wikipedia.org/wiki/BBCode).
    * HTML [Hypertext Markup Language](https://www.w3schools.com/html/html_intro.asp).
    * RTF [Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format).
    * SVG [Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG).
    * Terminal.
    * Terminal256.
    * Text.
    * IRC.

 ### Styles Available
    * default
    * emacs
    * friendly
    * colorful
    * autumn
    * murphy
    * manni
    * monokai
    * perldoc
    * pastie
    * borland
    * trac
    * native
    * fruity
    * bw
    * vim
    * vs
    * tango
    * rrt
    * xcode
    * igor
    * paraiso-light
    * paraiso-dark
    * lovelace
    * algol
    * algol_nu
    * arduino
    * rainbow_dash
    * abap
    * solarized-dark
    * solarized-light
    * sas
    * stata
    * stata-light
    * stata-dark
    * inkpot

## Request Config

Here are the config options for highlighting code snippets.  
>NOTE: this should be a **POST** request at all times as **GET** request is not supported.

```javascript
{
    // Code snippet to be highlighted. Required.
    code: '',

    // Programming language of the code snippet to be highlighted. Required. 
    language: 'python', // default

    // Syntax highlighting style.
    style: 'default', // default

    // What format would you like to retrieve your code snippet. Required.
    getFormat: 'html', // default

    // linenos is used to request if the result should have line numbers
    // or not, this can be one of ['inline', 'table', False], defaults to
    // False, no line numbers.
    lineNos: false, // default
    
    // noclasses is used to define if the user requires inline css
    // styling or classes, this can be one of ['inline', 'class']
    styling: 'inline', // default
    
    // class name giving to the div tag wrapping the whole code block
    // defaults to highlighter,
    // NOTE: if linenos is set to table this will append a 'table' making 
    // to it making it 'highlightertable'.
    divClass: 'highlighter', // default

    // Specify a list of line numbers to be highlighted in your code snippet
    // this should be an array of numbers. Defaults to an empty array.
    hlLines: [], 
    
    // If set to 'true', the syntax highlighting style won't output the
    // background color of the code block, leaving this to you to style
    // the background color of the code block when returned in the
    // response data.
    noBackground: false, // default
    
    // prefix the css classes used when 'noclasses' is set 'class'
    classPrefix: '', // default is an empty string
}