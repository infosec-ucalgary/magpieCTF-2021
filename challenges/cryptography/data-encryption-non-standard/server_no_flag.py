import os
import time


def encrypt(message, key):
	left = message[0:2]
	right = message[2:4]

	subkeys = gen_subkeys(key)

	for i in range(32):
		left, right = right, xor_bytes(f(right, subkeys[i]), left)
	
	return right + left


def decrypt(ciphertext, key):
	left = ciphertext[0:2]
	right = ciphertext[2:4]

	subkeys = gen_subkeys(key)[::-1]

	for i in range(32):
		left, right = right, xor_bytes(f(right, subkeys[i]), left)
	
	return right + left


def f(r, key):
	return bytes([(r[i] + key[i]) % 256 for i in range(2)])


def gen_subkeys(key):
	subkeys = [key[0:2], key[2:4]]

	for i in range(30):
		subkeys.append(subkeys[i])
	
	return subkeys


def xor_bytes(a, b):
	return bytes(a[i] ^ b[i] for i in range(len(a)))


def main():
	FLAG = "magpie{}"
	key = os.urandom(4)

	for i in range(2**10):
		print("Choose an option: 1 to encrypt a message, 2 to decrypt, 3 to guess the key, or 4 to exit")
		choice = int(input())

		if choice == 1:
			print("Enter your message in hex")

			message = bytes.fromhex(input())
			
			print(encrypt(message, key).hex())
		elif choice == 2:
			print("Enter your ciphertext in hex")

			message = bytes.fromhex(input())
			
			print(decrypt(message, key).hex())
		elif choice == 3:
			print("Enter your guess in hex")

			guess = input().lower()

			time.sleep(5)

			if(guess == key.hex()):
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

