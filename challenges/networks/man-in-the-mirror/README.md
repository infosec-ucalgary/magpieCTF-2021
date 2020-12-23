# Man-in-the-Mirror
### Category: Networks
### Author: James Lowther (Articuler)

## Description
And no message could have been any clearer...

Hint 1: Where is the data getting filtered?

## Solution
This challenge provides a website and a proxy. Going to the website without going through the proxy will return an error stating that you can't get the flag this way. Connecting to the website through the proxy will indicate that the flag was returned, but was filtered out by the proxy before getting sent to you.

1. To solve this challenge, we need to intercept the response from the website that was requested by the proxy before it is sent back to the proxy and filtered out.
2. To do this, write your own proxy in something like Python3 which forwards all requests to the given website and prints out the returned HTML.
3. Then, send a request to your custom proxy while connected to the given proxy. This will allow the website to return the flag using the the proxy's authentication credentials and also allow us to read it before it gets obfuscated by the proxy.

## Flag
magpie{m4n_1n_th3_m1ddl3}