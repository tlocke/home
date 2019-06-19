Title: Comparing incomparable types
Date: 2008-12-07 11:00
Author: Tony Locke
Tags: language-design
Slug: comparing-incomparable-types
Status: published

The [Python 3 changes doc](http://docs.python.org/dev/3.0/whatsnew/3.0.html#ordering-comparisons) says:  

> objects of different incomparable types always compare unequal to each other.

I don't think this is the right way to go. If you try to compare incomparable types, a `TypeError` exception should be thrown. For example, at the moment if you write `9 == 'hello'` in Python it'll return false, but I think it should throw a `TypeError`.
