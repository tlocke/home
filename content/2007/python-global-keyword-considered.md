Title: Python 'global' Keyword Considered Harmful
Date: 2010-08-05 21:38
Author: Tony Locke
Tags: language-design
Slug: python-global-keyword-considered
Status: published

Looking at Python's `global` keyword led me to think how I'd like [scoping](http://en.wikipedia.org/wiki/Scope_(programming)) to work. Some languages have lexical scoping, some dynamic scoping and some a mixture of two. I think scoping should be entirely lexical. My language (let's call it Klop) is dynamically typed, and variables are declared the first time they are assigned, so if you wrote:

<div>

    x = 0

    def f():
      return x

    def g():
      x = 1
      return f()

Calling `g()` would return 1. In most languages with lexical scoping you can declare a variable with the same name, at a more local scope. With Klop you can't, and I think that this would make programs more readable.

</div>
