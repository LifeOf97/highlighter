# Highlighter

A code **syntax highlighter** request api, which can handle most programming languages and text formats.


## Features

* **Code highlighter**.  
Used in highlighting programming languages used in blogs, chat apps and any project requiring code samples.

  * **Formats Available** (_currently_)
    * BBCode [Bulletin Board Code](https://en.wikipedia.org/wiki/BBCode).
    * HTML [Hypertext Markup Language](https://www.w3schools.com/html/html_intro.asp).
    * RTF [Rich Text Format](https://en.wikipedia.org/wiki/Rich_Text_Format).
    * SVG [Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG). (_experimental_)
    * Terminal.
    * Terminal256.
    * Text.
    * IRC.

  * **Styles Available**  
    default emacs friendly colorful autumn murphy manni monokai perldoc pastie borland trac native fruity bw vim vs tango rrt xcode igor paraiso-light paraiso-dark lovelace algol algol_nu arduino rainbow_dash abap solarized-dark solarized-light sas stata stata-light stata-dark inkpot


## Usage
#

## Request Config

Here are the config options for highlighting code snippets.  
>NOTE: this should be made through a **POST** request at all times as **GET** request is not supported.

```javascript
{
  // Code snippet to be highlighted. Required.
  code: '',

  // Programming language (sourcecode) of the code snippet to be highlighted. Required. 
  language: 'python', // default

  // Syntax highlighting style.
  // checkout the available styles at the features section of this readme.
  style: 'default', // default

  // In what format would you like to retrieve your code snippet,
  // checkout the available formats at the features section of this readme.
  getFormat: 'html', // default

  // linenos is used to request if the result should have line numbers
  // or not, this can be one of ['inline', 'table', 'none'], defaults to
  // 'none', no line numbers. Optional.
  lineNos: 'none', // default
  
  // FORMAT: HTML => what type of html styling would you prefer? inline css or
  // classes, this can be one of ['inline', 'class']
  css: 'inline', // default
  
  // FORMAT: HTML => class name giving to the div tag wrapping the whole code block
  // defaults to 'justhighlight'. NOTE: if "lineNos" is set to table this
  // will append a 'table' to the class name making it for example 'justhighlighttable'.
  divClass: 'justhighlight', // default

  // hlLines is used to specify a list of line numbers to be highlighted in your code snippet
  // this should be an array of numbers. Defaults to an empty array.
  hlLines: [], // default
  
  // FORMAT: HTML => classPrefix is used to prefix the css classes used
  // when "css" is set "class".
  classPrefix: '' // default is an empty string

  // The noBackground option is used to request that the "style" option selected should not
  // affect the code background color. this should either be true/false, where true is
  // "do not apply background color" and false is "apply background color". 
  noBackground: false, // default
}
```

## Response Data
#
The succefull response of a valid request contains the following.

```javascript
{
    // The status of the reesponse.
    status: 'success',
    
    // The result object containing the highlighted code data
    result: {
        data: '', // the highlighted code snippet.
        sourcecode: '', // the highlighted code return format. 
        formatting: '', // the programming language highlighted.
        styles: '', // only available when styling is set to class.
    }
}
```

## Examples
#
* **Using axios API**

```javascript
axios.post('https://api.justhighlight.com/highlighter/', {
    code: "const greet = 'Hello World!'",
    language: 'javascript',
    getFormat: 'html',
    style: 'paraiso-dark',
    lineNo: 'none',
    css: 'inline',
    divClass: 'player',
    hlLines: [],
    noBackground: false,
})
  .then((response) => {
      // make use of the returned response as you will.
      this.highlighted = response.data.result.data;
  })
  .catch((error) => {
      // catch any error what so ever and debug it.
      console.log(error.response);
  });

```

* **Using fetch API**
```javascript
// get all data needed.
const data = {
    code: "const greet = 'Hello World!'",
    language: 'javascript',
    getFormat: 'html',
    style: 'paraiso-dark',
    lineNo: 'none',
    css: 'inline',
    divClass: 'player',
    hlLines: [],
    noBackground: false,
};
// make a post request using fetch api.
fetch('https://api.justhighlight.com/highlighter/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data),
})
  .then((response) => response.json())
  .then((data) => {
      // make use of the returned response as you will.
      this.highlighted = data.result.data;
  })
  .catch((error) => {
      // catch any error what so ever and debug it.
      console.log(error);
  });
```

## Credits
#
**Highlighter** depends fully on **Pygments** which is a syntax highlighter written in Python. Checkout [Pygments github repo](https://github.com/pygments/pygments) and also [Pygments official website](https://pygments.org/) for more insight.