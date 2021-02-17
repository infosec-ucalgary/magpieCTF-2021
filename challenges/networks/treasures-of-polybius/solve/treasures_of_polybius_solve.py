import requests

def solve() -> bool:
    flag = "magpie{g00gl3_dr1v3_|)1v3}"
    link_id = "11CqxPS4fpnYA799rhCw3SdjYoGFUwXdD"

    session = requests.Session()
    resp = session.get(f"https://drive.google.com/u/0/uc?id={link_id}&export=download")

    confirm_key = get_confirm_key(session)

    # attempt to recieve download cookie 10 more times if the key was not found
    retry = 10
    while(not confirm_key and retry):
        session.close()
        confirm_key = get_confirm_key(session)
        retry -= 1

    if(not confirm_key):
        return False

    resp = session.get(f"https://drive.google.com/u/0/uc?id={link_id}&export=download&confirm={confirm_key}")
    resp_text = str(resp.content)

    return flag in resp_text

def get_confirm_key(session) -> str:
    for key, value in session.cookies.get_dict().items():
        if "download" not in key: continue
        return value

    return ""
