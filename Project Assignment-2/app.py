#!/usr/bin/env python3
import logging
from app import app

if __name__ == '__main__':
    app_path = '/'.join(__file__.split('/')[:-1])
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", filename=app_path + "/logs/app.log", level=logging.DEBUG)
    logging.info("Starting app")
    app.run(debug=True)
    logging.info("Ending app")