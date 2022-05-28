Title: Polifesto 17
Date: 2009-10-02 10:49
Author: Tony Locke
Tags: polifesto
Slug: polifesto-17
Status: published

I've been doing some work on [Polifesto](http://www.polifesto.com/), both the functionality of the site, and the content. Polifesto is a wiki of political manifestos. You can rate the manifestos and write your own. You can include policies from other manifestos. I've fleshed out a manifesto call [La Licorne Manifesto](http://www.polifesto.com/policies/1/).  
  
The technical changes are:  

-   Now uses the excellent [GAE Utilities](http://gaeutilities.appspot.com/) to handle sessions.
-   Fixed bug where the wrong radio button was checked that said what your policy rating was.
-   Corrected problem with logging out by using `cgi.FieldStorage()`.
-   Fixed bug where rating radio button didn't stay checked when it had been checked.
-   I'm using [Selenium](http://seleniumhq.org/) for testing. This probably means an end to my own [Imprimatur](http://imprimatur.wikispaces.com/).
-   Fixed loads of other bugs.  
