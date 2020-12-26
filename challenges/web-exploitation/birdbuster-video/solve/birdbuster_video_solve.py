import sys, os, requests

def solve() -> bool:
    flag = "magpie{80s_m0v135_4r3_th3_b35t}"
    challenge_host = "http://web01.magpiectf.ca:7633"

    code = open(os.path.join(os.path.dirname(__file__), "assets/birdbuster-barcode.gif"), "rb")
    r = requests.post(challenge_host + "/upload", files={"uploaded_file": code})

    code.close()

    return flag in r.text