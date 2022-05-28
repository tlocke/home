Title: Imprimatur 017
Date: 2010-08-11 22:03
Author: Tony Locke
Tags: imprimatur
Slug: imprimatur-017
Status: published

Someone requested that Imprimatur support HTTPS requests. It did seem an oversight, so I've remedied that with the newly released [Imprimatur 017](http://sourceforge.net/projects/imprimatur/).

HTTPS requests are supported with the `scheme` attribute, which has a default of `http`, but can also be set to `https`. The `scheme` attribute can be used in the same elements as the `port` and `hostname` attributes can be used, eg. `imprimatur`, `test`, `test-group`, `request`. I've updated the documentation to give [an example](http://imprimatur.wikispaces.com/HttpsRequest).

Let me know how you get on with it.
