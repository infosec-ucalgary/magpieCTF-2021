def mod_inv(p, q):
	# calculate inverse of p mod q
	if p < q:
		return mod_inv(q, p)
	else:
		x0, y0, x1, y1 = 1, 0, 0, 1
		x0, y0, x1, y1 = x1, y1, x0 - (p // q) * x1, y0-( p // q) * y1
		p, q = q, p%q
		while q != 0:
			x0, y0, x1, y1 = x1, y1, x0 - (p // q) * x1, y0 - (p // q) * y1
			p, q = q, p % q
		return y0


def find_encryption_matrix(data):
	# set up a system of equations using the magic number for a png and encrypted file bytes to find the encryption matrix
	equations = [[0x89,0x50,0,0,data[0]], [0x4E,0x47,0,0,data[2]], [0,0,0x89,0x50,data[1]], [0,0,0x4E,0x47,data[3]]]

	# reduce to RREF
	for i in range(4):
		inverse = mod_inv(equations[i][i], 256)
		for j in range(5):
			equations[i][j] = (equations[i][j] * inverse) % 256

		for j in range(4):
			if j != i:
				multiple = equations[j][i]
				for k in range(5):
					equations[j][k] = (equations[j][k] - multiple * equations[i][k]) % 256

	return [[equations[0][4], equations[1][4]],[equations[2][4], equations[3][4]]]


def find_decryption_matrix(enc_matrix):
	# find inverse of encryption matrix
	determinant = enc_matrix[0][0]*enc_matrix[1][1]-enc_matrix[0][1]*enc_matrix[1][0]
	det_inv = mod_inv(determinant%256, 256)

	dec_matrix=[[(enc_matrix[1][1]*det_inv)%256,(-enc_matrix[0][1]*det_inv)%256],[(-enc_matrix[1][0]*det_inv)%256, (enc_matrix[0][0]*det_inv)%256]]

	return dec_matrix


def decrypt(data, dec_matrix):
	# decrypt file
	decrypted = []
	for i in range(0, len(data), 2):
		decrypted.append(round(data[i]*dec_matrix[0][0]+data[i+1]*dec_matrix[0][1]) % 256)
		decrypted.append(round(data[i]*dec_matrix[1][0]+data[i+1]*dec_matrix[1][1]) % 256)

	return decrypted


f = open("flag.png", "rb")
data = f.read()
f.close()

enc_matrix = find_encryption_matrix(data)

dec_matrix = find_decryption_matrix(enc_matrix)

data = decrypt(data, dec_matrix)

f = open("flag.png", "wb")
f.write(bytes(data))
f.close()
