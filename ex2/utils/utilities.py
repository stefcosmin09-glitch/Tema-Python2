import hashlib

def sha256_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

def sha256_file(file_path):
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()