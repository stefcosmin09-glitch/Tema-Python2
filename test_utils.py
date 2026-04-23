import sha256 

rezult = sha256.hash_string("Hello, World!")
print(f"Hash of 'Hello, World!': {rezult}")

rezult = sha256.hash_file("test_file.txt")
print(f"Hash of 'test_file.txt': {rezult}")