# Day 84: Logging Module
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

logging.info("Application initialized.")
logging.warning("Cache miss detected; re-fetching data.")
