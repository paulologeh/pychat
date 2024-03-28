import os
from src import create_app
from dotenv import load_dotenv

if os.getenv("DEVELOPMENT"):
    load_dotenv()

app = create_app(os.getenv("ENVIRONMENT"))
