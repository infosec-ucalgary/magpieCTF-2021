import sys, os, requests

def solve() -> bool:
    flag = "magpie{build_automation_genius}"
    challenge_host = "http://web.magpiectf.ca:4325"

    r = requests.get(challenge_host + "/api.php", headers={"Authorization": "token f4e53e561c6580d6d304f3f31e3102f5"})

    return flag in r.text
