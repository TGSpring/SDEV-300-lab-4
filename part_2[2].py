import hashlib
message = input("Enter message")
message = message.encode()

print(hashlib.md5(message).hexdigest())
print(hashlib.sha256(message).hexdigest())
print(hashlib.blake2b(message).hexdigest())
print(hashlib.blake2s(message).hexdigest())
print(hashlib.sha3_256(message).hexdigest())
print(hashlib.sha3_512(message).hexdigest())

