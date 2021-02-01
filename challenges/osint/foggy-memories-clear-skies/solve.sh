#!/bin/bash 

echo "Converting data bank to ASCII..."

if dd if=data-bank-27t-1988 of=ascii-data-bank conv=ascii | grep -q '0+0 records in'; then
   echo "Failed to convert data bank"
   exit 1
fi

echo "Finding matches to 'ROCHESTER' in converted data bank"

cat ascii-data-bank | grep -aob 'ROCHESTER' > grandrapids.txt 

if [wc -c grandrapids.txt | awk '{print $1}' == 0]; then 
    echo "Failed to write to grandrapids.txt"
    exit 1
fi 

python extract-ebcdic.py 
