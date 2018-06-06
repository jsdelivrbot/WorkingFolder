# libraries
import sqlite3
import pandas as pd
import numpy as np

from flask import Flask, render_template,request,redirect,url_for, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



# Databses setup using automap
engine = create_engine("sqlite:///chi_db")

Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Data = Base.classes.samples_metadata
population = Base.classes.population
crime = Base.classes.crime

# Create our session (link) from Python to the DB
session = Session(engine)

#Save reference to the table

#################################################
# Flask Setup
app = Flask(__name__)

#Home route 
    #Route renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

    # Route renders crime.html template
@app.route("/crime")
def crimepage():
    return render_template("crime.html")


