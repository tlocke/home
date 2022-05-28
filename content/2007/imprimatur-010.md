Title: Imprimatur 010
Date: 2007-08-31 11:28
Author: Tony Locke
Tags: imprimatur
Slug: imprimatur-010
Status: published

This [new release](http://sourceforge.net/project/showfiles.php?group_id=145016) removes the <parameter> element, and replaces it with a <control> element. The <control> element is the same as the <parameter> element, but the value of the control can be put in the 'value' attribute or the element content.  
  
The reason for the change is to deal with whitespace better. It's hard to put a script as an attribute, but if you use element content for everything, then whitespace gets changed by editors formatting the XML to make it more readable.
