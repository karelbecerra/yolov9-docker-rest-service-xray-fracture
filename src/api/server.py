import io
import base64

import logging
logger = logging.getLogger("uvicorn")
from fastapi import FastAPI

def start():
  logger.info("AI Server - starting")
  return FastAPI()