
# Moving Pictures
### Category: Forensics
### Author: Braydon Willms

## Description
I've been trying to figure out where Neil's car is - I wonder if he hid it in one of his albums?

We're also given Moving\_Pictures.pdf.

## Hint
Where could things be hidden in a pdf?

## Solution
1. We can start by looking around the pdf. We can find that it has multiple layers, and there's a steganography password hidden underneath the top layer when we remove it.

2. Figuring out where to use this password takes a bit more work. We might try to use it on the album pictures, but this doesn't seem to work. When we look closer at the pdf data (using something like a hex editor, or strings or binwalk), we find an object that has been partially corrupted which prevents it from rendering correctly.

3. We can extract the picture in this object using binwalk to locate it and dd to extract the data.

4. Once the picture is extracted, we can use steghide along with the password we found to pull a binary out of the image, which gives us the flag when we run or look through it.

## Flag
magpie{B4rc73774\_8UR1eD\_!n\_7H3\_B4RN}
