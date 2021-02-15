# Magpie2021 - Cylons!
### Category: Reverse Engineering
### Author: Jeremy Stuart (Mr.Wizard) 

## Description
The Cylons have invaded Magpie Electronic Machines Inc and stolen a flag!  They have the ability to look like humans now too.  See if you find where they're hiding in the Magpie website and get the flag back from them.

## Hints

1.  Where do robots hide in a website?

## Solution:
1. First, figure out that Cylons are robots from the TV show Battlestar Galactica (originally aired in 1978-1979, but ran again for 10 episodes after fans wrote thousands of letters demanding it be put back on).  The hint tells you that you need to figure our where robots hide in a website, and if you're not familiar then a quick Google search should reveal the robots.txt file that most websites have.  Knowing this, you can navigate to this file.

2. Go to magpiemachines.com/robots.txt to find a page with a message that reads "Attention Attention!  Greetings fellow human being.  There are no robots here.  Only genuine human beings.  Cease the search for robots.  There are only humans, not robots."  You should also notice that the page is disallowing web crawlers access to humans.txt.  This means that this website also has a humans.txt file.  Navigate there.

3. Go to magpiemachines.com/humans.txt to find a message from the Cyclons and the flag.


## Flag: 
magpie{@||_y0uR_f1@G5_aR3_b3|0nG_t0_u5}