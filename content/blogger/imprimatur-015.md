Title: imprimatur-015
Date: 2009-05-13 01:13
Author: Tony Locke
Tags: imprimatur
Slug: imprimatur-015
Status: published

[New release](http://sourceforge.net/project/showfiles.php?group_id=145016&package_id=159509) of [Imprimatur](http://imprimatur.wikispaces.com/) with the following changes:  

> \* Changed so that a regex matches if it's found anywhere within the string.

Previously you'd have to use the pattern `.*hello.*` to match 'hello' within a response. Now you can just use the pattern `hello` to do the same thing.  

> \* In regexes, a dot character now matches line terminators as well.

Imprimatur used to remove all control characters from the response, and then do the match. I thought it was better not to do this behind-the-scenes chicanery and make '.' match line terminators as well.

</p>

