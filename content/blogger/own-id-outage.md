Title: Own-Id outage
Date: 2008-01-22 21:40
Author: Tony Locke
Tags: own-id
Slug: own-id-outage
Status: published

[Own-Id](http://www.own-id.com/) was down from 2008-01-18 15:16 GMT to 2008-01-19 12:47 GMT. Sorry to everyone for this outage. The reason was that the Java VM ran out of memory. This means that Own-Id probably has a memory leak.  
  
One of the problems was that it took a long time for me to find out that the server was down. I've now set up [Montastic](http://www.montastic.com/) to send me an email if the server goes down again, they also provide a web feed of server status. This should mean that if there's another outage, I should know much sooner.  
  
There remains the problem of finding the memory leak. I'll let you know how I get on!
