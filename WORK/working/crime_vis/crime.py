# import dependencies
from flask import Flask, jsonify, render_template, request, redirect
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect 

import pandas as pd
import numpy as np 
import datetime as dt    

# database setup using automap
engine = create_engine("sqlite:///chi_db.sqlite")

Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
AllCrime = Base.classes.all_crime

# Create our session (link) from Python to the DB
session = Session(engine)


# initialize Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///chi_db.sqlite"

@app.route("/crimehistory")
def crime_dict(crime):
    results = session.query.(AllCrime.id, AllCrime.crimeGroup, AllCrime.year,AllCrime.nunCrimes).filter(AllCrimes.id)

    dict=[]
    for result in results:
        crime_dict= {}
        crime_dict["year"] = result.year
        crime_dict["id"] = result.id
        crime_dict["crimeGroup"] = result.crimeGroup
        crime_dict["nunCrimes"] = result.nunCrimes
        dict.append(crime_dict)
    return jsonify(dict)

if __name__ == "__main__":
    app.run(debug=True)