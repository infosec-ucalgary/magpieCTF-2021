import os
import time


def encrypt(message, key):
	left = message.hex()[0:5]
	right = message.hex()[5:10]

	subkeys = gen_subkeys(key)

	for i in range(32):
		left, right = right, xor_hex_strings(f(right, subkeys[i]), left)
	
	return bytes.fromhex(right + left)


def decrypt(ciphertext, key):
	left = ciphertext.hex()[0:5]
	right = ciphertext.hex()[5:10]

	subkeys = gen_subkeys(key)[::-1]

	for i in range(32):
		left, right = right, xor_hex_strings(f(right, subkeys[i]), left)
	
	return bytes.fromhex(right + left)


def f(r, key):
	sub = [hex( (int(r[i], 16) + int(key[i], 16)) % 16 )[2] for i in range(5)]

	return ''.join(sub[1:5] + [sub[0]])


def gen_subkeys(key):
	subkeys = [key[0:5], key[5:10]]

	for i in range(30):
		subkeys.append(subkeys[i])
	
	return subkeys


def xor_hex_strings(a, b):
	return ''.join([hex( int(a[i], 16) ^ int(b[i], 16) )[2] for i in range(len(a))])


def main():
	FLAG = "magpie{}"
	key = os.urandom(5).hex()

	print("Hello! The encryption service will start momentarily...")
	time.sleep(5)
	start = time.time()

	for i in range(2**12):
		print("Choose an option: 1 to encrypt a message, 2 to decrypt, 3 to guess the key, or 4 to exit")
		choice = int(input())

		if choice == 1:
			message = bytes.fromhex(input())
			
			print(encrypt(message, key).hex())
		elif choice == 2:
			message = bytes.fromhex(input())
			
			print(decrypt(message, key).hex())
		elif choice == 3:
			print("Enter your guess in hex")

			guess = input().lower()

			if(guess == key and time.time() - start <= 1800):
				print("You figured it out... I guess I owe you a flag")
				print(FLAG)
				exit()
			else:
				print("Better luck next time")
				exit()
		else:
			exit()
	
	print("I think that's enough")

main()

