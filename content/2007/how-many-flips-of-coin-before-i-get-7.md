Title: How many flips of a coin before I get 7 heads in a row?
Date: 2018-04-07 20:01
Author: Tony
Slug: how-many-flips-of-coin-before-i-get-7
Status: published

Bill asked, 'On average, how many flips of a coin do I have to do to get 7 heads in a row?'. I thought this would be really easy, but I had to think about it for ages. I think it means, how many flips to get 50% probability of getting 7 heads in a row. On Maths StackExchange there was [an answer](https://math.stackexchange.com/a/602194/195992) that I didn't fully understand, but it said to do 1 - (probability of not getting 7 in a row). It also said to think about 'atoms' which for 7 heads are:  
  
T  
HT  
HHT  
HHHT  
HHHHT  
HHHHHT  
HHHHHHT  
  
The idea is that the number of ways of not getting 7 heads in a row if you flip the coin 40 times, is the number of ways of arranging the atoms so that the total length is 41. I tried it out with smaller numbers first, so I thought about the chances of getting 2 heads in a row for 2 coin tosses. So in this case the atoms are:  
  
T  
HT  
  
and the ways of arranging them in a total length of 3 are:  
  
TTT  
THT  
HTT  
  
So there are 3 of them, and the total number of combinations are 2\^2 = 4, giving a probability of not getting two heads in a row of 3/4, and so the probability of getting two heads in a row is 1 - 3/4 = 1/4. Which we know is correct. So the problem now is, how do we work out the number of ways of arranging the atoms for 2 heads in an arbitrary length?  
  
The picture below shows how I imagine it:  

![Diagram]({static}/images/2018/2_heads.jpg)

Starting at zero, the single arrows mean an atom of length 1 (ie. a tail), and a double arrow means an atom of length 2 (ie. a head followed by a tail). The number of ways of getting to a certain length, is equal to the number of different paths to get to the number on the graph in the picture (that's what the number in brackets is). So for example, there are two ways to get to length 2, one way is to go from zero directly, and the other way is go via 1. Looking at the number of ways as the path length increases you get a [fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number):  
  
0, 1, 1, 2, 3, 5, 8, 13, ...  
  
So if there are n coin tosses the probability of getting two heads in a row is:  
  
1 - fib(n + 1) / 2\^n  
  
So there we have it for 2 heads in a row, but what about 3? I drew another diagram, but with 3 arrows coming from each length rather than 2, and the number of ways of not getting 3 heads in a row was a [tribonacci](https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Fibonacci_numbers_of_higher_order) sequence. The next term of the fibonacci sequence if found by adding up the two previous terms, but the next term in the tribonacci sequence is found by adding up the three previous terms. So it goes:  
  
0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, ...  
  
Say the nth term of a kth order fibonacci sequence is fib(k, n), then the probability of getting k heads in n flips is:  
  
1 - fib(k, n) / 2\^n  
  
There's probably some fancy way of working this out, but I wrote a Python 3.6 programme to do it:  
  

    prob = 0
    NUM_IN_A_ROW = 7

    while prob < 0.5:
        first_key, first_val = sorted(stream.items())[0]
        for v in range(NUM_IN_A_ROW):
            stream[first_key + v + 1] += first_val
        prob = 1 - stream[first_key + 1] / 2 ** first_key
        print(
            "After " + str(first_key) + " flips the probability of getting " +
            str(NUM_IN_A_ROW) + " in a row is " + str(prob))
        del stream[first_key] 

  
Running this gives: `After 178 flips the probability of getting 7 in a row is 0.5014494277755364`. So my answer is 178!  
  
Any corrections and comments welcome :-)  
  

#### Update 2018-04-08

Having thought about the maths again, I think the Python can be written in a better way, and the [deque](https://docs.python.org/3/library/collections.html#collections.deque) data structure is well suited to finding n-order fibonacci sequences. So here's my second attempt, and reassuringly it comes out with the same answer.  
  

    from collections import deque
    from itertools import count


    NUM_IN_A_ROW = 7
    fibs = deque([1], NUM_IN_A_ROW)
    tot = 1

    for n in count():
        fib = sum(fibs)
        fibs.append(fib)
        prob = 1 - fib / tot
        print(
            f"After {n} flips the probability of getting {NUM_IN_A_ROW} in a row "
            f"is {prob}")
        if prob >= 0.5:
            break
        tot *= 2
