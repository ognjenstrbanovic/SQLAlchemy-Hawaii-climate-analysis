# import Flask and other dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)
# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
# Create an app, being sure to pass __name__
app = Flask(__name__)
# Define what to do when a user hits the index route
@app.route("/")
def welcome():
    # List all available api routes.
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/<start><br/>"
        f"/api/v1.0/start/<start>/end/<end>"
    )
@app.route("/api/v1.0/precipitation")
# Define what to do when a user hits the precipitation route
def precipitation():
    # Create our session (link) from Python to the DB
    session_1 = Session(engine)
    results_1 = session_1.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23").order_by(Measurement.date).all()
    session_1.close()
    # Create a dictionary from the row data and append to a list
    query_1_converted_to_dict = []
    for date, prcp in results_1:
        precipitation_dictionary = {}
        precipitation_dictionary["Date"] = date
        precipitation_dictionary["Precipitation"] = prcp
        query_1_converted_to_dict.append(precipitation_dictionary)
    return jsonify(query_1_converted_to_dict)
@app.route("/api/v1.0/stations")
# Define what to do when a user hits the stations route
def stations():
    # Create our session (link) from Python to the DB
    session_2 = Session(engine)
    results_2 = session_2.query(Station.station).all()
    session_2.close()
    # Convert list of tuples into normal list
    stations = list(np.ravel(results_2))
    return jsonify(stations)
@app.route("/api/v1.0/tobs")
# Define what to do when a user hits the tobs route
def tobs():
    # Create our session (link) from Python to the DB
    session_3 = Session(engine)
    results_3 = session_3.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-18").filter(Measurement.station == 'USC00519281').order_by(Measurement.date).all()
    session_3.close()
    # Create a dictionary from the row data and append to a list
    query_3_converted_to_dict = []
    for date, tobs in results_3:
        tobs_dictionary = {}
        tobs_dictionary["Date"] = date
        tobs_dictionary["Temperature Observed"] = tobs
        query_3_converted_to_dict.append(tobs_dictionary)
    return jsonify(query_3_converted_to_dict)
@app.route("/api/v1.0/start/<start>")
# Define what to do when a user hits the start route
def start_behavior(start_1):
    user_input_1 = start_1.replace("/", "-")
    session_4 = Session(engine)
    all_dates_1 = session_4.query(Measurement.date).all()
    session_4.close()
    list_of_all_dates_1 = list(np.ravel(all_dates_1))
    # Create our session (link) from Python to the DB
    session_5 = Session(engine)
    results_5 = session_5.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= user_input_1).all()
    session_5.close()
    # Convert list of tuples into normal list
    start_list = list(np.ravel(results_5))
    # Create a dictionary
    start_dictionary = {"TMIN": start_list[0]}, {"TMAX": start_list[1]}, {"TAVG": start_list[2]}
    if user_input_1 not in list_of_all_dates_1:
        return jsonify({"Error": "Date not found."}), 404
    else:
        return jsonify(start_dictionary)
@app.route("/api/v1.0/start/<start>/end/<end>")
# Define what to do when a user hits the start/end route
def start_end(start, end):
    user_input_2 = start.replace("/", "-")
    user_input_3 = end.replace("/", "-")
    session_6 = Session(engine)
    all_dates_2 = session_6.query(Measurement.date).all()
    session_6.close()
    list_of_all_dates_2 = list(np.ravel(all_dates_2))
    # Create our session (link) from Python to the DB
    session_7 = Session(engine)
    results_7 = session_7.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= user_input_2).filter(Measurement.date <= user_input_3).all()
    session_7.close()
    # Convert list of tuples into normal list
    start_end_list = list(np.ravel(results_7))
    # Create a dictionary
    start_end_dictionary = {"TMIN": start_end_list[0]}, {"TMAX": start_end_list[1]}, {"TAVG": start_end_list[2]}
    if (user_input_2 or user_input_3) not in list_of_all_dates_2:
        return jsonify({"Error": "Date(s) not found."}), 404
    else:
        return jsonify(start_end_dictionary)
# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)