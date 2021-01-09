import random
from pwn import *


FLAG = "magpie{T74t'5_a_F31StY_C19HeR}"
HOST = 'enter address'
PORT = 20000


# finds half of the key assuming the messages are a slid pair
# ensure right half of p1 = left half of p2
def find_half_key(p1, p2):
	return bytes([(((p2[i + 2] ^ p1[i]) - p1[i + 2]) % 256) for i in range(2)])


# calculates one round
def f(plaintext, key):
	return plaintext[2:4] + bytes([(((plaintext[i + 2] + key[i]) % 256) ^ plaintext[i]) for i in range(2)])


def solve():
	# generate random plaintexts and ciphertexts, leaving the half that is unchanged the same
	plaintexts = set()

	for i in range(2**8):
		x = random.randrange(0, 2**16)
		x = hex(x)[2:]
		p = b'\x00\x00' + bytes.fromhex('0'*(4-len(x)) + x)

		plaintexts.add(p)

	ciphertexts = set()

	for i in range(2**8):
			x = random.randrange(0, 2**16)
			x = hex(x)[2:]
			c = bytes.fromhex('0'*(4-len(x)) + x) + b'\x00\x00'

			ciphertexts.add(c)

	conn = remote(HOST, PORT)
	pairs = []

	for p in plaintexts:
		discard = conn.recvline()
		conn.sendline('1')

		discard = conn.recvline()
		conn.sendline(p.hex())
		c = str(conn.recvline())[2:10]
		pairs.append([p, bytes.fromhex(c[4:8] + c[0:4])])

	for c in ciphertexts:
		discard = conn.recvline()
		conn.sendline('2')

		discard = conn.recvline()
		conn.sendline(c.hex())
		p = str(conn.recvline())[2:10]
		pairs.append([c, bytes.fromhex(p[4:8] + p[0:4])])

	# search for slid pairs to calculate half the key
	key0, key1 = b'\x00\x00', b'\x00\x00'
	for i in range(len(plaintexts)):
		for j in range(len(plaintexts), len(pairs)):
			k = find_half_key(pairs[j][0], pairs[i][0])

			if f(pairs[j][1], k) == pairs[i][1]:
				key1 = k

	# repeat the above, reversing the offset to find the other half of the key
	plaintexts = set()

	for i in range(2**8):
		x = random.randrange(0, 2**16)
		x = hex(x)[2:]
		p = bytes.fromhex('0'*(4-len(x)) + x) + b'\x00\x00'

		plaintexts.add(p)

	ciphertexts = set()

	for i in range(2**8-1):
			x = random.randrange(0, 2**16)
			x = hex(x)[2:]
			c = b'\x00\x00' + bytes.fromhex('0'*(4-len(x)) + x)

			ciphertexts.add(c)

	pairs = []

	for p in plaintexts:
		discard = conn.recvline()
		conn.sendline('1')

		discard = conn.recvline()
		conn.sendline(p.hex())
		c = str(conn.recvline())[2:10]
		pairs.append([p, bytes.fromhex(c[4:8] + c[0:4])])

	for c in ciphertexts:
		discard = conn.recvline()
		conn.sendline('2')

		discard = conn.recvline()
		conn.sendline(c.hex())
		p = str(conn.recvline())[2:10]
		pairs.append([c, bytes.fromhex(p[4:8] + p[0:4])])

	for i in range(len(plaintexts)):
		for j in range(len(plaintexts), len(pairs)):
			k = find_half_key(pairs[i][0], pairs[j][0])

			if f(pairs[i][1], k) == pairs[j][1]:
				key0 = k

	if key0 != b'\x00\x00' and key1 != b'\x00\x00':
		discard = conn.recvline()
		conn.sendline('3')

		discard = conn.recvline()
		conn.sendline((key0 + key1).hex())

		if "flag" in conn.recvline():
			flag = str(conn.recvline())
			conn.close()
			return FLAG in flag
		else:
			conn.close()
			return False
	else:
		conn.close()
		return False
