Title: Imprimatur 013
Date: 2008-06-18 13:20
Author: Tony Locke
Tags: imprimatur
Slug: imprimatur-013
Status: published

The [new release](http://sourceforge.net/project/showfiles.php?group_id=145016&package_id=159509) of [Imprimatur](http://imprimatur.wikispaces.com/) has the following changes:  

-   The [response-code]{style="font-style: italic;"} element was missing from the<response-code> DTD, so that's been added in.  
   </response-code>
-   Now supports the PUT method.
-   Can [set and check HTTP headers](http://imprimatur.wikispaces.com/BodyFile).
-   Added a [body-file]{style="font-style: italic;"} attribute to the [request]{style="font-style: italic;"} element which allows the request body to be retrieved from a file. There's a [new example](http://imprimatur.wikispaces.com/BodyFile) that shows this.<response-code><request></request></response-code>
-   <response-code><request>Removed 'enctype' attribute from the [request]{style="font-style: italic;"} <request> element. If there's no [body-file]{style="font-style: italic;"} attribute, the content type is inferred[]{style="font-style: italic;"}. If there is a [body-file]{style="font-style: italic;"} attribute the content type can be set explicitly using a [header]{style="font-style: italic;"} element.</request></request></response-code>

Thanks to Jesse Pelton for his suggestions for this release.

</p>

