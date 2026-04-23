import hashlib
import base64

def hash_string(text):
    #return the sha256 hash of the input string
    return hashlib.sha256(text.encode()).hexdigest()

def hash_file(file_path):
    #return the sha256 hash of the file
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()
    
def encode_base64(text):
    #return the base64 encoding of the input string
    return base64.b64encode(text.encode()).decode()

def decode_base64(encoded_text):
    #return the original string from the base64 encoded input
    return base64.b64decode(encoded_text.encode()).decode()