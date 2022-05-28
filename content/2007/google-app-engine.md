Title: Google App Engine
Date: 2008-05-20 20:28
Author: Tony Locke
Slug: google-app-engine
Status: published

I set out to port [Own-Id](http://www.own-id.com/) to [Google App Engine](http://code.google.com/appengine/) but failed because Own-Id relies on people being able to point their own host name to the Own-Id app. This only works because Own-Id has its own IP address. With App Engine it seems you're not assigned an IP address. If anyone knows how I can make Own-Id work with App Engine, please let me know!  
  
While looking at App Engine, it seemed that one of its limitations is that the datastore doesn't support complex queries. It's a big constraint when one is used to SQL. Having said that, I love the fact that it supports Python and the whole thing seems really nicely done. When I come do do my next web app, I'll certainly look first at doing it with App Engine.
