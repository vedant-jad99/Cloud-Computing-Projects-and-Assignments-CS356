#!/usr/bin/env python3
#Creating a basic app

import logging
from app import app
import os

if __name__ == '__main__':
    app_path = os.getcwd()
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s %(thread)s", filename=app_path + "/logs/app.log", level=logging.DEBUG)
    logging.info("Starting app")
    app.run(debug=True, host="0.0.0.0", port=8080)
    logging.info("Ending app")
