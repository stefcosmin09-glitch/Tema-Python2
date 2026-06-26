import utils

text = "Salut lume"

encoded = utils.encode_base64(text)
decoded = utils.decode_base64(encoded)

print("Original:", text)
print("Encoded:", encoded)
print("Decoded:", decoded)