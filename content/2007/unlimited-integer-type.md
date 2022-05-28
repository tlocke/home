Title: Unlimited Integer Type
Date: 2009-01-28 20:12
Author: Tony Locke
Tags: language-design
Slug: unlimited-integer-type
Status: published

In my ideal programming language, the size of the integer type would only be limited by the storage space of the machine, it wouldn't have an artificial limit. It would be like the [BigInt](http://java.sun.com/javase/6/docs/api/java/math/BigInteger.html) type in Java. This is exactly what [Clojure](http://clojure.org/data_structures) does. Brilliant!  
  
There isn't such an elegant solution for floating point numbers. The problem is that 1 / 3, for example, would take up an infinite amount of memory. Clojure uses BigDecimal and its own Ratio type to try and get round this. What's to be done?
