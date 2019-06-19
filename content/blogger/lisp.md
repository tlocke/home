Title: Lisp
Date: 2009-08-09 20:11
Author: Tony Locke
Slug: lisp
Status: published

Like many others, I read Paul Graham's [Lisp](http://www.paulgraham.com/avg.html) [essays](http://www.paulgraham.com/power.html) and thought I should give Lisp a go. I installed [Clojure](http://clojure.org/) and wrote my first Lisp program:  
  

    (defn num_books
     ([dist]
       (num_books dist 0 0))
     ([dist achieved nbooks]
     (if
       (>= achieved dist)
       nbooks
       (num_books dist
           (+ achieved
               (/ 1
                   (+ nbooks 2)))
           (+ nbooks 1)))))

    (println (num_books 1.5))

  
  
If you put a book on the edge of a table you can balance it so that it sticks out half a book length. Place another judiciously on top and it'll stick out 1/2 + 1/3 book lengths. You give the function above a number of book lengths you want the stack to stick out, and it'll return the number of books you need.  
  
Coming from a Python background, wouldn't it make sense to use whitespace instead of parentheses?  
  

    defn num_books
    [dist]
    num_books dist 0 0
    [dist achieved nbooks]
    if
       >= achieved dist
       nbooks
       num_books dist
           + achieved
               / 1
                   + nbooks 2
           + nbooks 1

    println
    num_books desired_distance

  
  
Also, I'm interested to compare this function with its Python equivalent:  
  

    def num_books(desired):
    achieved = 0
    nbooks = 0
    while achieved < desired:
     achieved = achieved + 1 / (nbooks + 2)
     nbooks = nbooks + 1
    return nbooks

The Python one is shorter, how can this be? Okay a re-write of the Lisp version:  

    (defn num_books
        ([dist]
            (loop [nbooks 0 achieved 0]
              (if
                  (< achieved dist)
                (recur
                    (inc nbooks)
                    (+ achieved
                        (/ 1
                            (+ nbooks 2))))
                    nbooks))))

  
  
Python 166 chars, Lisp 186 characters. What am I doing wrong?
