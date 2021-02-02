import os
import sys
import socket
import platform
import requests
import subprocess

def solve() -> bool:
    flag = "magpie{1t5_4lw4y5_DNS}"

    # Since this challenge won't be hosted on the CTFd site
    # these are two external IP's that are used instead
    dns_ip = "167.71.58.123" # IP of the 'DNS' server
    goal_ip = "34.219.182.220" # IP of the web server

    if check_ip(dns_ip):
        resp = requests.get("http://" + goal_ip)
        return resp.content.decode('utf-8').strip() == flag
    else:
        print("Cannot connect to either challenge DNS or challenge Web server")
        return False

# Check if a given IP is reachable
def check_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    cmd = ['ping', param, '3', ip]
    result = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    return result

