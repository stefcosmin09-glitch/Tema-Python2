from utils.utilities import sha256_text, sha256_file
text = "Salut!"

text_hash = sha256_text(text)
print(f"Hash text: {text_hash}")

file_hash = sha256_file("README.md")
print(f"Hash fișier: {file_hash}")