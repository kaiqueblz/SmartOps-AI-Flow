import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data.db")
REDIS_BROKER = os.getenv("REDIS_BROKER", "redis://localhost:6379/0")