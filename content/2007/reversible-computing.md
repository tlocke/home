Title: Reversible computing
Date: 2008-07-12 13:37
Author: Tony Locke
Slug: reversible-computing
Status: published

I'm trying to understand [reversible computing](http://en.wikipedia.org/wiki/Reversible_computing). My friend Bill made the comment that it may well be of interest to academics, but it has no appreciable effect in the real world. So here's a rough calculation for the power an irreversible computer needs that's operating right at the Landauer limit. For each bit the energy used per switch is T \* k \* ln 2. Assume a 2 GHz processor, 5 GB of RAM, and room temperature:  
  
power = 293 \* 1.38 \* 10\^-23 \* ln 2 \* 2 \* 10\^9 \* 5 \* 10\^9  
  
\~ 0.01 W  
  
we can times this by 100 because k\*ln 2 is just the theoretical minimum that can never be reached.  
  
\~ 1 W  
  
So with Moore's law, this limit will become increasingly significant.  
  
I've no idea if this calculation is correct, I just made it up to prove my own point! Can someone correct me please?
