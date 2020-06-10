# sqlalchemy-challenge
Before treating myself to a trip to Hawaii, I need to do the necessary research on the climate!  

![Surfing in Hawaii](https://github.com/RutgersCodingBootcamp/RU-JER-DATA-PT-01-2020/blob/master/02-Homework/10-Advanced-Data-Storage-and-Retrieval/Instructions/Images/surfs-up.png?raw=true)  


Using SQLAlchemy ORM Queries, Pandas, and Matplotlib, I did some basic climate analysis and data exploration on the SQLite file, connecting to it using the "create_engine" command. Tables were reflected into classes using "automap_base()". A query was designed to retrieve precipitation data; this was loaded into a DF, plotted, and summarized statistically. Three more queries were used to find the total number of stations, the most active stations, and get the last 12 months of temperature observation data (TOBS).  
Below, you may find both of the plots:  

![



Next, I created a Flask API based on my queries. The routes are as follows: a home page; a JSON (JavaScript Object Notation) representation of the queries (transformed into a dictionary w/ key-value pairs); a JSON list of stations; a JSON list of TOBS; and a JSON list of min., max. and avg. temperature from the start date to the end date.  
```
Objectives for the Advanced Data Storage and Retrieval Unit:
- Connect to a SQL database using SQLAlchemy.
- Perform basic SQL queries using engine.execute().
- Create Python classes and objects.
- Create, read, update, and delete data from a SQL database using SQLAlchemy's ORM.
- Reflect existing databases.
- Use the SQLAlchemy ORM to create classes that model tables.
- Use the ORM define relationships and foreign key constraints.
- Use joins to query related data.
- Use Flask to create and run a server.
- Define endpoints using Flask's @app.route decorator.
- Extract query variable path values from GET requests.
- Use variable paths to execute database queries on behalf of the client.
- Return JSONified query results from API endpoints.
```
