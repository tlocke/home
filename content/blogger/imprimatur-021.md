Title: Imprimatur-021
Date: 2011-05-02 18:21
Author: Tony Locke
Tags: imprimatur
Slug: imprimatur-021
Status: published

I've just released [Imprimatur-021](https://sourceforge.net/projects/imprimatur/). The main change is that the &lt;session&gt; element has been removed. There's now just one session for the whole test script. The reason is that I felt that session information didn't fit with the hierarchy of XML. At the moment there isn't a way to start a new session part way through the script. It would probably be done with a 'new-session' attribute of the &lt;request&gt; element. Let me know if that would be useful to you.  
  
With this release I've changed from CVS to Git, simply because Git is more fashionable :-) I used [cvs2git](http://cvs2svn.tigris.org/cvs2git.html) and it worked really well.  
</request></session>
