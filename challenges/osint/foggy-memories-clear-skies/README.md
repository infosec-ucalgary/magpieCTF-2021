# Foggy Memories, Clear Skies
### Category: OSINT
### Author: Emily Baird (analytical engine)

## Description
I don’t remember much about my first trip where I got to take an airplane. I must’ve been eight or nine, because it was definitely in 1988. And I definitely remember the drive to the Ottawa airport. As for the rest of the trip, it’s all a bit foggy. I do know that while we were there, we visited the grave of the first famous American daredevil, who jumped off Niagara Falls in the 1800s.

What airline did I fly with?

Flag format: magpie{airline_name}

## Hints
1. Some things can be done as well as others. Such as finding the flight destination.

2. I’m sure governments keep information about old flights somewhere… right?

## Solution
The first step here is to determine where the flight's destination was. With some googling, we can find that a man named [Sam Patch](https://en.wikipedia.org/wiki/Sam_Patch) jumped off Niagra Falls in the 1800s, and that he died and was buried in Rochester New York.

From here, we need to figure out what airlines were flying between Ottawa and Rochester in 1988. A preliminary google doesn't reveal much initially. However, this sounds like the kind of data that government archives might keep track of, so we'll try searching the American National Archives. By searching for keywords such as 'transportation' and 'aviation' and narrowing down our search for the correct timeline, we start to get results for things like "Service Segment Domestic and International Data File," which looks like we're on the right track. Eventually, we find [this](https://catalog.archives.gov/id/20899009) databank, and reading the [technical documentation](https://catalog.archives.gov/OpaAPI/media/20899009/content/electronic-records/rg-467/DB27T/250.1DP.pdf?download=false) for the bank gives us the following:

    "In general, these files contain totals of passenger enplaned and transported for each pair of points served or scheduled to be served by a single stage of at least one flight within the reported time period. Each record contains information regarding the reporting carrier, aircraft type flown, revenue class of service flown."

This data bank definitely looks as though it will contain the information we need. Now to go about extracting that information. The technical documentation also gives a detailed byte-by-byte breakdown of how an individual record is structured. It says that "Airport (1) Alpha Code" is at position 11 in the record, and "Airport (2) Alpha Code" is at position 21. Knowing that we are looking for a flight between Ottawa and Rochester, we can look for records where Airport (1) is alpha code 'YOW' and Airport (2) is alpha code 'ROC'. We can also see that the carrier code is the next two bytes after the Airport (2) alpha code.

Another file, the [Technical Specifications Summary](https://catalog.archives.gov/OpaAPI/media/20899009/content/electronic-records/rg-467/DB27T/DB27T_TSS250.pdf?download=false), gives a high level overview of the databank's encoding scheme:

    "Format: EBCDIC, variable-length records with packed decimal data (EBCPAK)"

Some more googling reveals that [EBCDIC](https://en.wikipedia.org/wiki/EBCDIC) was a popular character encoding scheme used on IBM mainframe computers. 

Now we can get down to business: we'll write a basic python script to scan the databank looking for the records we're after:

```python
import ebcdic
import codecs


with open("RG467.DBNK27T.Y88", "rb") as f:
    c = f.read(1)
    while c!=b'':
        if 'Y' in c.decode('cp1047'):
            c=f.read(1)
            if 'O' in c.decode('cp1047'):
                c=f.read(1)
                if 'W' in c.decode('cp1047'):
                    f.read(7)
                    c=f.read(3)
                    if 'ROC' in c.decode('cp1047'):
                        c=f.read(2)
                        print(c.decode('cp1047'))
        c = f.read(1)     
print('End')
```

We run the script, to find that the only airline travelling between Ottawa and Rochester in '88 was an airline called "Piedmont Aviation." Submit the flag `magpie{piedmont_aviation}` and get those points!

## Flag
magpie{piedmont_aviation}