Title: HTML discovery in OpenId 2.0
Date: 2007-10-27 12:15
Author: Tony Locke
Slug: html-discovery-in-openid-20-is-broken
Status: published

The [OpenId 2.0 specification](http://openid.net/specs/openid-authentication-2_0-12.html) is intended to be backwards compatible. However in the latest draft (12), the recommended [markup for HTML discovery](http://openid.net/specs/openid-authentication-2_0-12.html#anchor50) gives the 'rel' attribute in the 'link' element the values 'openid2.provider openid.server' and 'openid2.local\_id openid.delegate'. In OpenId 1.x the values for 'rel' were simply 'openid.server' and 'openid.delegate'.  
  
So to really be compatible with previous versions, the markup should be the same as in OpenId 1.x. I urge the authors of the specification to change it back. In my experience with [OwnId](http://www.own-id.com/) if you stick to the specification on this, you break compatibility with previous versions.  
  
Come to think of it, I don't see why a link to the server is needed at all. Can someone explain this to me?
