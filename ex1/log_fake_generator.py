import logging
import random
import uuid
import sys

# lista 1 - 10 request ID-uri
request_ids = [uuid.uuid4() for i in range(10)]

# lista 2 - mesaje de log

messages = [
    "Conection established",
    "User authenticated",
    "Data retrieved successfully",
    "Error: Invalid input",
    "File not found",
]

# lista 3 - niveluri de log
level = ["INFO", "WARNING", "ERROR"]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",

)
nr_linii = int(sys.argv[1])

for i in range(nr_linii):
    level = random.choice(level)
    message = random.choice(messages)
    request_id = random.choice(request_ids)
    log_message = f"{request_id} - {message}"

    if level == "INFO":
        logging.info(log_message)
    elif level == "WARNING":
        logging.warning(log_message)
    elif level == "ERROR":
        logging.error(log_message)