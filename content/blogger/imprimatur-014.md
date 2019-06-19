Title: Imprimatur 014
Date: 2008-06-19 19:32
Author: Tony Locke
Tags: imprimatur
Slug: imprimatur-014
Status: published

A bug-fix [release](http://sourceforge.net/project/showfiles.php?group_id=145016&package_id=159509) of [Imprimatur](http://imprimatur.wikispaces.com/). Fixed a problem that has been there for ages. If you started Imprimatur with a file name only (no path) for the script file, and then referred to another file in the script file, there would be a problem. I fixed it using:  
  
`File file = new File(fileName).getAbsoluteFile();`  
  
instead of:  
  
`File file = new File(fileName);`  
  
Thanks to Jesse Pelton for reporting this bug.
