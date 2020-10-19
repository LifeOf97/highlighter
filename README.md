# Highlighter

A code **syntax highlighter** request api, which can handle most programming languages and text formats.


## Features

* **Code highlighter**.  
Used in highlighting programming languages used in blogs, chat apps and any project requiring code samples.

  * **Formats Available** (_currently_)
    * BBCode [Bulletin Board Code](https://en.wikipedia.org/wiki/BBCode).
    * HTML [Hypertext Markup Language](https://www.w3schools.com/html/html_intro.asp).
    * RTF [Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format).
    * SVG [Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG).
    * Terminal.
    * Terminal256.
    * Text.
    * IRC.

  * **Styles Available**  
    default emacs friendly colorful autumn murphy manni monokai perldoc pastie borland trac native fruity bw vim vs tango rrt xcode igor paraiso-light paraiso-dark lovelace algol algol_nu arduino rainbow_dash abap solarized-dark solarized-light sas stata stata-light stata-dark inkpot


## Usage
**CDN** only  
coming soon.


## Request Config

Here are the config options for highlighting code snippets.  
>NOTE: this should be made through a **POST** request at all times as **GET** request is not supported.

```javascript
{
    // Code snippet to be highlighted. Required.
    code: '',

    // Programming language of the code snippet to be highlighted. Required. 
    language: 'python', // default

    // Syntax highlighting style. Optional.
    // checkout the available styles at the features section of this readme.
    style: 'default', // default

    // In what format would you like to retrieve your code snippet.
    getFormat: 'html', // default

    // linenos is used to request if the result should have line numbers
    // or not, this can be one of ['inline', 'table', false], defaults to
    // false, no line numbers.
    // Optional.
    lineNos: false, // default
    
    // noclasses is used to define if the user requires inline css
    // styling or classes, this can be one of ['inline', 'class']
    styling: 'inline', // default
    
    // class name giving to the div tag wrapping the whole code block
    // defaults to highlighter,
    // NOTE: if linenos is set to table this will append a 'table' making 
    // it 'highlightertable'.
    divClass: 'highlighter', // default

    // Specify a list of line numbers to be highlighted in your code snippet
    // this should be an array of numbers. Defaults to an empty array.
    hlLines: [], 
    
    // The noBackground option is used to request the the code background should be styles by the selected syntax style of not. this should either be true/false 
    noBackground: false, // default
    
    // prefix the css classes used when 'noclasses' is set 'class'
    classPrefix: '' // default is an empty string
}
```

## Response Data

The succefull response of a valid request contains the following.

```javascript
{
    // The status of the reesponse.
    status: 'success',
    
    // The result object containing the highlighted code data
    // and style
    result: {
        data: '',
        styles: '', // only available when styling is set to class.
    }
}
```

## Examples

* **Using axios API**
* **Using fetch API**


## Credits

**Highlighter** depends fully on **Pygments** which syntax highlighter written in Python. Checkout [Pygments github repo](https://github.com/pygments/pygments) and also [Pygments documentation](https://pygments.org/) for more insight.