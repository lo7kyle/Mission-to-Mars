from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Setting up Flask
app = Flask(__name__)
# Connect Python with Mongo. This tells Python that our app is going to connect to Mongo using a URI
# Similar to connecting to a URL
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set up Flask routes: One for the Main HTML page and the other to our scrape data
# index is the default HTML file that we'll use to display the content we've scraped
@app.route("/")
def index():
    # this assigns a variable that points to the mars MongoDB (mongo.db.mars)
    mars = mongo.db.mars.find_one()
    # mars=mars tells Python to use the "mars" collection in MongoDB
    return render_template("index.html", mars=mars)
# Create the scraping route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape.all() # Referencing the scrape_all function in scraping.py 
    # Updates our mars database. Syntax: .update(query_parameter, data, options)
    mars.update({}, mars_data, upsert = True) # use {} as empty JSON object, upsert creates a new document if one doesn't already exist
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()