import logging
import os


def configurar_logger():
    # Crear carpeta logs si no existe
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.ERROR)

    # Evita duplicar handlers si se importa varias veces
    if not logger.handlers:
        handler = logging.FileHandler("logs/app.log", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
