import sys
import base64

encode = sys.argv[1]
file = sys.argv[2]

decode = base64.b64decode(encode). decode()

with open(file, 'w') as f:
    f.write(decode)
