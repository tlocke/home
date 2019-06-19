Title: Own-Id 004
Date: 2008-05-05 13:02
Author: Tony Locke
Tags: own-id
Slug: own-id-004
Status: published

Just released a new version of [Own-Id](http://www.own-id.com/). Now gives [more detail in error messages](http://code.google.com/p/openid-delegator/issues/detail?id=14&can=1).  
  
Incidentally, we now have 188 ids now on Own-Id. As ever, I'm always keen to hear about your experiences with Own-Id.  
  
For testing Own-Id on my local machine, I use the [MyId](http://siege.org/projects/phpMyID/) OpenId server which is great because it's so simple to set up, and it uses [Digest Authentication](http://en.wikipedia.org/wiki/Digest_access_authentication) which is a [RESTful](http://en.wikipedia.org/wiki/Representational_State_Transfer) method that makes testing easy. For me, the one problem with MyID is that is uses a META tag to redirect the browser, but I find it easier for testing to have a HTTP 302 redirect, so I modified the source (just a simple change) to achieve this.
