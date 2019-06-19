Title: MOSM
Date: 2011-01-17 16:07
Author: Tony Locke
Slug: mosm
Status: published

I've done some work on [MOSM](http://mobosm.appspot.com/), the mobile web site for seeing a map of where you are. For fun I thought I'd use HTML5. It worked out okay on the browser you get with Android 2.2.  
  
One thing I had to learn to get a web page working in a mobile was to use the [meta viewport element](http://www.w3.org/TR/mwabp/#bp-viewport):  
  
`<meta name="viewport" content="width=device-width, initial-scale=1.0">`  
  
If you try out MOSM, you'll notice that it has two flaws:  

-   The downloading of the tiles is really slow. I've turned off the tile buffer, where it downloads tiles off the edge of the screen, but it's still slow.
-   To get the current position, it doesn't trigger the retrieval of GPS coordinates. An app does, but a browser app doesn't.

If you know how to solve these problems, please let me know.
