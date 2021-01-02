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
    session = requests.Session()
    ids = get_ids()

    for id_str in ids:
        dl_link = f"https://drive.google.com/u/0/uc?id={id_str}&export=download" 
        confirm_key = ""
        prev_key = ""

        print(dl_link)
        # Essential code is below
        resp = session.get(dl_link)

        while(True):
            for key, value in session.cookies.get_dict().items():
                if "download" not in key: continue
                confirm_key = value
                break

                if not confirm_key: 
                    print("Confirmation key not found :(")
                    break

            if prev_key != confirm_key: break
        resp.close()

        prev_key = confirm_key
        print(confirm_key)
        confirm_link = f"https://drive.google.com/u/0/uc?export=download&id={id_str}&confirm={confirm_key}"

        print(f"requesting {confirm_link}")
        resp = session.get(confirm_link)
        print(f"downloading {confirm_link} to temp.bin")
        with open("./temp.bin", "wb+") as dump: dump.write(resp.content)
        resp.close()

        print(f"content from {confirm_link} has been written to temp")
        grep = subp.Popen(f"strings temp.bin | grep magpie >> flag.txt", shell=True)

    return

if __name__ == "__main__": main()
