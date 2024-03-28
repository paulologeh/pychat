import os
import logging.config
import logging.handlers
import pathlib
import json
import atexit
from src import create_app
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def setup_logging():
    config_file = pathlib.Path("logConfig.json")
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


if os.getenv("DEVELOPMENT"):
    load_dotenv()
    setup_logging()

app = create_app(os.getenv("ENVIRONMENT"))
