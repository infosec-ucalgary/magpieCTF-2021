import random
from pwn import *


FLAG = "magpie{T74t'5_a_F31StY_C19HeR}"
HOST = 'enter ip address'
PORT = 20000


# finds half of the key assuming the messages are a slid pair
# ensure right half of p1 = left half of p2
def find_half_key(p1, p2):
	sub = [(int(p2[i + 5], 16) ^ int(p1[i], 16)) for i in range(5)]
	sub = [sub[4]] + sub[0:4]

	return ''.join([hex((sub[i] - int(p1[i + 5], 16)) % 16)[2] for i in range(5)])


# calculates one round
def f(plaintext, key):
	sub = [((int(plaintext[i + 5], 16) + int(key[i], 16)) % 16) for i in range(5)]
	sub = sub[1:5] + [sub[0]]

	return plaintext[5:10] + ''.join([hex(sub[i] ^ int(plaintext[i], 16))[2] for i in range(5)])


def solve():
	# generate random plaintexts and ciphertexts, leaving the half that is unchanged the same
	plaintexts = set()

	for i in range(2**10):
		x = random.randrange(0, 2**20)
		x = hex(x)[2:]
		p = "00000" + ('0'*(5-len(x)) + x)

		plaintexts.add(p)

	ciphertexts = set()

	for i in range(2**10):
			x = random.randrange(0, 2**20)
			x = hex(x)[2:]
			c = ('0'*(5-len(x)) + x) + "00000"

			ciphertexts.add(c)

	conn = remote(HOST, PORT)
	pairs = []

	discard = conn.recvline()

	for p in plaintexts:
		discard = conn.recvline()
		conn.send("1\n" + p + '\n')

		c = str(conn.recvline())[2:12]
		pairs.append([p, c[5:10] + c[0:5]])

	for c in ciphertexts:
		discard = conn.recvline()
		conn.send("2\n" + c + '\n')

		p = str(conn.recvline())[2:12]
		pairs.append([c, p[5:10] + p[0:5]])

	# search for slid pairs to calculate half the key
	key0, key1 = "00000", "00000"
	for i in range(len(plaintexts)):
		for j in range(len(plaintexts), len(pairs)):
			k = find_half_key(pairs[j][0], pairs[i][0])

			if f(pairs[j][1], k) == pairs[i][1]:
				key1 = k

	# repeat the above, reversing the offset to find the other half of the key
	plaintexts = set()

	for i in range(2**10):
		x = random.randrange(0, 2**20)
		x = hex(x)[2:]
		p = ('0'*(5-len(x)) + x) + "00000"

		plaintexts.add(p)

	ciphertexts = set()

	for i in range(2**10-1):
			x = random.randrange(0, 2**20)
			x = hex(x)[2:]
			c = "00000" + ('0'*(5-len(x)) + x)

			ciphertexts.add(c)

	pairs = []

	for p in plaintexts:
		discard = conn.recvline()
		conn.send("1\n" + p + '\n')

		c = str(conn.recvline())[2:12]
		pairs.append([p, c[5:10] + c[0:5]])

	for c in ciphertexts:
		discard = conn.recvline()
		conn.send("2\n" + c + '\n')

		p = str(conn.recvline())[2:12]
		pairs.append([c, p[5:10] + p[0:5]])

	for i in range(len(plaintexts)):
		for j in range(len(plaintexts), len(pairs)):
			k = find_half_key(pairs[i][0], pairs[j][0])

			if f(pairs[i][1], k) == pairs[j][1]:
				key0 = k

	if key0 != "00000" and key1 != "00000":
		discard = conn.recvline()
		conn.sendline('3')

		discard = conn.recvline()
		conn.sendline(key0 + key1)

		if "flag" in str(conn.recvline()):
			flag = str(conn.recvline())
			conn.close()
			return FLAG in flag
		else:
			conn.close()
			return False
	else:
		conn.close()
		return False

