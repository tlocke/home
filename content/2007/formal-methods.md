Title: Formal Methods
Date: 2009-08-18 22:34
Author: Tony Locke
Slug: formal-methods
Status: published

I don't understand [formal methods](http://en.wikipedia.org/wiki/Formal_methods). A group has [claimed to have formally verified](http://ertos.nicta.com.au/research/l4.verified/) the [L4 kernel](http://en.wikipedia.org/wiki/L4_microkernel_family). What does this mean? I suppose that this means that specification of the kernel has been written as a mathematical proof. Then it must have been demonstrated that the C code exactly matched the proof.  
  
But if it's easier to write the specification than the code, that must mean that the programming language isn't very good. And yes! This is borne out by the sort of [programming errors that are found](http://ertos.nicta.com.au/research/l4.verified/proof.pml) when comparing the specification to the implementation:  

> -   Buffer overflows
> -   Null pointer dereferences
> -   Pointer errors in general
> -   Memory leaks
> -   Arithmetic overflows and exceptions

These are mostly solved by using a decent programming language such as Python.  
  
Ben Laurie talks about this in his [post on formal methods](http://www.links.org/?p=689).
