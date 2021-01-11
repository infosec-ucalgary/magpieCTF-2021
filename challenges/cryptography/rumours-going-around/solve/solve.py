from Crypto.PublicKey import RSA

def egcd(p, q):
    if p < q:
        return egcd(q, p)
    else:
        x0, y0, x1, y1 = 1, 0, 0, 1
        x0, y0, x1, y1 = x1, y1, x0 - (p // q) * x1, y0-( p // q) * y1
        p, q = q, p%q
        while q != 0:
            x0, y0, x1, y1 = x1, y1, x0 - (p // q) * x1, y0 - (p // q) * y1
            p, q = q, p % q
        return p, x0, y0

f = open('public1.pem', 'r')
key1 = RSA.importKey(f.read())
f.close()

f = open('public2.pem', 'r')
key2 = RSA.importKey(f.read())
f.close()

f = open('c1.txt', 'r')
c1 = int(f.read(), 16)
f.close()

f = open('c2.txt', 'r')
c2 = int(f.read(), 16)
f.close()

gcd, x, y = egcd(key1.e, key2.e)

c1_inverse = egcd(c1, key1.n)[2]

p = (pow(c1_inverse, -y, key1.n) * pow(c2, x, key2.n)) % key1.n

print(bytes.fromhex(('0' * (len(hex(p)) % 2)) + hex(p)[2:]))
