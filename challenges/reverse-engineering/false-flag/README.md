# Magpie2021 - False-Flag
### Category: Forensics
### Author: Jeremy Stuart (Mr.Wizard) 

## Description
The United States didn't land on the moon, that flag is completely fake!  Dig in and
see if you can figure out the REAL flag!

## Hints

1. Despite the lack of gravity, it's still pretty easy to binwalk on the Moon.

## Solution:
This is meant to be a simple binwalk challenge, whereby you use binwalk (or some other
tool) to find that there is more than one file in the image data.  If you run binwalk
on the image you're given you'll find that there's a file called "RealImage.zip" appended
to the end of moonman.jpeg and you can either use binwalk to automatically extract it or
use the `dd` tool to remove the bytes of the zip to a new file.  Once you do that, unzip
`RealImage.zip` to find a file called `mtv.txt`.  If you open it in a text editor it
shouldn't make any sense.  This is because it's actually a jpg file.  You can check this by
 running `file` on `mtv.txt` and finding out that it's a jpg.  Opening it as an image
you get the same picture, but the flag is changed to the MTV flag.  This image is a frame
from the opening braodcast of MTV on August 1, 1981.  If you run binwalk again, you'll find
 a tar file attached.  Again use `binwalk` or `dd` to pull the tar file off and untar the 
 file to find flag.txt.

## Flag: 
magpie{V1d30_ki113d_Th3_R4D10_St4R}
