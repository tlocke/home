Title: Google's Webmaster Tools
Date: 2011-04-17 18:56
Author: Tony Locke
Slug: googles-webmaster-tools
Status: published

Call me a late adopter, but I thought I'd give [Google's Webmaster Tools](https://www.google.com/webmasters/tools/home) a go. I pointed it at [MtrHub](http://www.mtrhub.com/) and it found a bug. It found that even if you'd set a meter to be public, you still couldn't see individual reads without being logged in. It found it because if a user needs to be authorized, MtrHub returns an [HTTP 401](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2), which Webmaster Tools rightly complains about. Another advantage of using HTTP response codes conscientiously.
