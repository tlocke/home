Title: Directed Identity
Date: 2009-08-01 14:17
Author: Tony Locke
Slug: directed-identity
Status: published

I read Glyn Moody's writings with interest, but with his post [Why Single Sign On Systems Are Bad](http://opendotdotdot.blogspot.com/2009/07/why-single-sign-on-systems-are-bad.html) I think he's made a rare slip. Here's a note to Glyn on why I think he's wrong on this occasion:  
  
You conflate single sign-on (SSO) and single identity. OpenId lets you have SSO [and]{style="font-style: italic;"}lets you have a separate identity for each web site you visit. It's called Directed Identity, and Peter Williams [gives a good explanation](http://barelyenough.org/blog/2007/12/openid-20s-killer-feature/) of it.  
  
[![OpenId](http://openid.net/logo-graphics/openid-icon-250x250.png)](http://openid.net/logo-graphics/openid-icon-250x250.png)  
  
~~Yahoo! implement directed identity. Anyone with a Yahoo! account that signs in to websites using OpenId automatically has a different ID for each web site. When you sign in to the web site you just type yahoo.com in the OpenId box, and Yahoo! magically works it all out.~~  
  
<ins>I got that last paragraph wrong. As [Will Norris explains](http://willnorris.com/2009/07/openid-directed-identity-identifier-select), Yahoo! implements *identifier select* and can give an *opaque URL*, Yahoo! does not support *directed identity*. Google does support directed identity.</ins>
