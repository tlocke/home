Title: BrowserId Better Than OpenId
Date: 2013-05-08 21:47
Author: Tony
Slug: browserid-better-than-openid
Status: published

I've been a long-time fan of [OpenId](http://en.wikipedia.org/wiki/OpenID), but I now think [BrowserId](http://en.wikipedia.org/wiki/BrowserID) is better. Here are the two main reasons why:  

-   With BrowserId the user enters an email address, whereas with OpenId the user enters a URL. Most users already have an email address that they remember, and can type easily. With OpenId and its URLs, it's more complicated.
-   With OpenId, you had to work out whether you had an OpenId or not. If not then you had to go and obtain one at a separate web site. With Mozilla Persona (an implementation of BrowserId) any email address you have will work.

So I've put my money where my mouth is and replaced OpenId with Persona on [Polifesto](http://www.polifesto.com/). Let me know what you think.
