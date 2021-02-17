# Jimmy Strikes Back
### Category: Networks
### Author: Joshua Novak (rm -rf /#0797)

## Description
Looks like Jimmy's at it again... I heard him mention something about a new DNS server  
he's hosting. I heard him mention that the first octet is "167". Dig around this pcap  
and see what you can find. It also seems like he hasn't bought his domain yet...

## Hints
1. Since he is still deveoping this, its not using the normal DNS port
2. There is a URL somewhere in the .pcap file

## Solution
1. Look for communication with the IP starting with 167...
2. Find the fake URL in the message sent to the DNS server
3. Dig the server with the following command (keep the port in mind)
  - `dig @<SERVER> -p <PORT> <URL>`
  - `nslookup -port=<PORT> <URL> <SERVER>`
```
dig @167.71.58.123 -p 44434 magpie.flag
```
or
```
nslookup -port=44434 magpie.flag 167.71.58.123
```
4. Find the IP of the fake URL
5. Visit IP:
  - In web browser
  - via cURL
6. Grab flag

## Flag
magpie{1t5_4lw4y5_DNS}
