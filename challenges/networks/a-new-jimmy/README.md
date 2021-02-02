# A New Jimmy
### Category: Networks
### Author: Joshua Novak (rm -rf /#0797)

## Description
It seems like Jimmy got the flag illegitimately as he got it directly from our server.  
Luckily for us, we were able to capture the traffic from that transaction. See if you  
can figure out what he did and find the flag!  

## Hints
1. I can't TELl you  how he conNEcTed, it was pure magic.

## Solution
1. Open pcap file in wireshark
2. Two ways to do this
  - Follow the TCP stream and find cat flag.txt response
  - Scan through each packet and find the packet where the server sends the encoded flag (packet 110)
3. Decode base64 data string for the flag

## Flag
magpie{t3ln3t_1s_b@d}
