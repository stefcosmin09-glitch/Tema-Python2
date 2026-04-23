import sha256

text = "Hello, World!"
encoded_text = sha256.encode_base64(text)
print(f"Encoded: {encoded_text}")

decoded_text = sha256.decode_base64(encoded_text)
print(f"Decoded: {decoded_text}")