import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = os.path.join(os.getcwd(), "logs")  # sirf folder ka path
os.makedirs(logs_dir, exist_ok=True)          # folder banega agar nahi hai

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)  # ab file ka path alag

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.info("Logging setup complete.")
