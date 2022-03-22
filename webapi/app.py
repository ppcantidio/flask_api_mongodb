from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
from webapi.config import DevelopmentConfig


load_dotenv(str(Path(__file__).parent.absolute()) +'/.env')

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
