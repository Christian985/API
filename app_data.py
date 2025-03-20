from flask import Flask
from flask_pydantic_spec import FlaskPydanticSpec

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0',)

app2 = Flask(__name__)