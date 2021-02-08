:

# WarGames
### Category: Forensics
### Author: Alexandra Tenney (alexxxii)

## Description
Joshua doesn't only like playing games, he also likes messing with the windows registry. I heard he was messing around at Software\Magpie.

## Hints
1. "Software\Magpie" might be the key...

## Solution
Volatlity is a great program to parse through volatile memory, like that found in a vmem file. An `apt install` isnt the best installation choice because it doesn't download the newest version, so directly cloning the github and running the program from there should be our course of action.

```bash
1. git clone https://github.com/volatilityfoundation/volatility.git
2. cd volatility
3. chmod 755 setup.py
4. ./setup.py install
```

Then we need to find the profile of the machine that the vmem was taken from, this can be done using the command: `python vol.py -f wopr.vmem imageinfo`. This should give you the profile of `Win10x64_18362`

The description and hint refer to a Windows Registry Key of Software\Magpie, which we can look through using volatility.

`vol.py -f ~/alex/windows.vmem --profile=Win10x64_18362 printkey -K "Software\Magpie"`

The string `bWFncGlle3RoM19yM2cxc3RyeV8xNV9uMHRfc2M0cnl9` is a base 64 ecoded string of the flag.

## Flag
magpie{th3_r3g1stry_15_n0t_sc4ry}

