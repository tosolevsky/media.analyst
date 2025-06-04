import logging
from logging.handlers import RotatingFileHandler
import os

# Log klasörü oluştur
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Ana logger nesnesi
logger = logging.getLogger("media.analyst")
logger.setLevel(logging.INFO)

# Konsola log
console_handler = logging.StreamHandler()
console_format = logging.Formatter("[%(levelname)s] %(message)s")
console_handler.setFormatter(console_format)

# Dosyaya log (maksimum 1MB, 3 yedek)
file_handler = RotatingFileHandler(
    f"{log_dir}/app.log", maxBytes=1_000_000, backupCount=3
)
file_format = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
file_handler.setFormatter(file_format)

# Handler'ları ekle
logger.addHandler(console_handler)
logger.addHandler(file_handler)
