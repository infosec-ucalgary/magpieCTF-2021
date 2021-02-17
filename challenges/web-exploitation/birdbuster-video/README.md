# Birdbuster Video
### Category: Web Exploitation
### Author: James Lowther (Articuler)

## Description
Weren't video rental stores the best?! See if you can break into this one!

## Hints
1. 80s action movies really inject you full of adrenaline!

## Solution
This challenge gives provides you a website with the ability to upload a barcode. The website will "scan" this barcode and will return information about the movie title that was encoded.

1. To solve this challenge, generate a barcode with a SQL injection that returns all rows using an online barcode generator.
    * For example, `' OR 1=1;  --  `
2. Upload the barcode to the website.
3. The flag can be found at the bottom of the returned results.

## Flag
magpie{80s_m0v135_4r3_th3_b35t}