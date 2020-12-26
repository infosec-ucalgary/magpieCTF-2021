import os, sys, requests

def solve() -> bool:
    flag = "magpie{l0053_c0mp4r150n_l34d5_t0_tr0ub13}"
    challenge_host = "http://web01.magpiectf.ca:8594"

    key = open(os.path.join(os.path.dirname(__file__), "assets/smurfs-solve-key"), "rb")
    r = requests.post(challenge_host + "/decrypt.php", files={"key": key})

    key.close()

    return flag in r.text