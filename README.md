# Markup Text Editor 
This package can be used to format the text in a way with the specified markups. The notations followed in the markup are below:\
 \*\*within double asterisk** -- Bold \
 \//within two forward slashes// -- Italics \
 \_\_within two underscores__ -- Underlined \
 $$within two dollars$$ -- Strike through \
 \* item 1\
 \* item 2 -- Unordered list with two items \
 \1. item 1\
 \2. item 2 -- Ordered list with two items \
 \[link\]\(address\) -- Link 
 
## What it does?
 The package will convert these into corresponding HTML tags html tags.

## Installation

Install the pacakge using pip (or) pip3. [For python3]

```python
pip install markup-editor
```
It has the following functions.
  
```python
import markup-editor as me
me.bold()
me.italics()
me.underline()
me.strike()
me.bullets()
me.number()
me.link()
```
Each will return the corresponding HTML tags.
