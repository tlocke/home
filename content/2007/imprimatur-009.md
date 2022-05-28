Title: Imprimatur 009
Date: 2007-08-12 15:58
Author: Tony Locke
Tags: imprimatur
Slug: imprimatur-009
Status: published

A new version of [Imprimatur](http://imprimatur.wikispaces.com/) has been released. The only change is with &lt;parameter&gt; elements. They used to look like:  
  
&lt;parameter name="emailAddress" value="adam.smith@localhost"/&gt;  
  
but now they look like:  
  
&lt;parameter name="emailAddress"&gt;adam.smith@localhost&lt;/parameter&gt;  
  
This is so that you can conveniently have parameter values with line breaks.
