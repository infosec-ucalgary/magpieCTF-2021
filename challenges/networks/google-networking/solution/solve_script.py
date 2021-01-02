#!/usr/bin/env python3

import requests
import os
import subprocess as subp

def get_ids():
    ids = []

    with open("link_list.txt", 'r') as link_list:
        links = link_list.read().split('\n')
        for link in links:
            if not link: continue
            id_str = link.split('/')[-2]
            ids.append(id_str)

    return ids

def main():
    ids = get_ids()

    prev_key = ""
    for id_str in ids:
        dl_link = f"https://drive.google.com/u/0/uc?id={id_str}&export=download" 
        confirm_key = ""

        print(dl_link)

        # Essential code is below
        session = requests.Session()
        resp = session.get(dl_link)
        for key, value in session.cookies.get_dict().items():
            if "download" not in key: continue
            confirm_key = value
            break

        if not confirm_key: 
            print("Confirmation key not found :(")
            return
 

        prev_key = confirm_key
        print(confirm_key)
        confirm_link = f"https://drive.google.com/u/0/uc?export=download&id={id_str}&confirm={confirm_key}"

        print(f"requesting {confirm_link}")
        resp = session.get(confirm_link)
        print(f"downloading {confirm_link} to temp.bin")
        with open("./temp.bin", "wb+") as dump: dump.write(resp.content)
        session.close()

        print(f"content from {confirm_link} has been written to temp")
        grep = subp.Popen(f"strings temp.bin | grep magpie >> flag.txt", shell=True)
        with open("./flag.txt", "r") as flag: flag.read()

        print("")
    return

if __name__ == "__main__": main()
