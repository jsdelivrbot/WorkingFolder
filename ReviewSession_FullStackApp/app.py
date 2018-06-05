# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy


@app.route("/")
def index():
    return: 
    
@app.route("/send", methods= ["GET", "POST"])
	def send_data():
	if request.method = "POST"; 
			## HTTP verb, " hey I want to give you some data" 

