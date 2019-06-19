Title: Own-Id: DNS propogation bug
Date: 2007-11-08 23:30
Author: Tony Locke
Tags: own-id
Slug: own-id-dns-propogation-bug
Status: published

I was going through the [Own-Id](http://www.own-id.com/) error log and found a
bug that affects new users only. It occurred when the DNS propagated to the
user's browser before it reached the Own-Id server. I've now changed the code
so that no DNS lookup is ever done on the domain name that the user is trying
to set up.
