import subprocess 

def searchForCities():
    positionlist = []

    # get just the bytes from the results of the grep search for 'YAKUTAT'
    with open("rochester.txt") as greplist:
        for line in greplist:
            bytePosition = line[0]

            i = 1
            while line[i] != ":":
                bytePosition = bytePosition + line[i]
                i+=1

            positionlist.append(int(bytePosition))

    with open("ascii-data-bank", "rb") as databank:
        for position in positionlist:
            # get some context at each of the positions
            databank.seek(position-50)          # set file read position slightly behind our desired string
            context = databank.read(100)         # read data before and after our string
            
            
            # based on the documentation package, we can assume that finding the full names of the airports
            # means that we are approximately 261 bytes into the record. backing up by that amount should put
            # us close to the beginning of the record, where carrier information is stored.
            if b'OTTAWA' in context:
                databank.seek(position-270)     # we'll give it a few extra bytes just in case
                
                print(context)
                print(databank.read(100))        # again, get some context knowing that we're in the right general area
                print()
            

if __name__ == "__main__":
    searchForCities()

