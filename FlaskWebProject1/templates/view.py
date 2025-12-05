"""
Routes and views for the flask application.
"""

from datetime import datetime
from sre_parse import State
from unittest import result
from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from FlaskWebProject1 import app
from flask_googlemaps import Map, GoogleMaps


import pyodbc



def connection():
    s = 'DESKTOP-VL6AIUJ\SQLEXPRESS' #Your server name 
    d = 'DemoDB' 
    u = 'reportuser' #Your login
    p = 'service-01' #Your login password
    #cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';Trusted_Connection=yes;'
    conn = pyodbc.connect(cstr)
    return conn

@app.route('/')
@app.route('/bookslot')
def bookslot():
    """Renders the home page."""
    return render_template(
        'bookslot.html',
        title='bookslot ',
        year=datetime.now().year,
    )


    

@app.route('/bookslot', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template(
        'bookslot.html',
        title='bookslot',
        year=datetime.now().year,
        message='User bookslot sample page.'
        )
    if request.method == 'POST':
        #id = int(request.form["id"])
        Vehicle_Type = request.form["vehicle_type"]
        Charging_Station = request.form["charging_station"]
        Rate_Plans = request.form["rate_plans"]
        Date = request.form["date"]
        Start = request.form["start"]
        Endd = request.form["endd"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO [dbo].[Bookings] ( [Vehicle_Type], [Charging_Station] , [Rate_Plans], [Date], [Start], [Endd]) VALUES ( ?, ?, ?, ?, ?, ?)",  Vehicle_Type, Charging_Station, Rate_Plans, Date, Start, Endd)
        conn.commit()
        conn.close()
        return render_template(
        'bookslot.html',
        title='bookslot',
        year=datetime.now().year,
        message='User Registration successfully.'
        )

    
@app.route('/map', methods=["GET", "POST"])
def map():
    #id = int(request.form["id"])
    mymap = Map(
    identifier="view-side",
    lat=37.4419,
    lng=-122.1419,
    markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
    identifier="sndmap",
    lat=37.4419,
    lng=-122.1419,
    markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png':[(37.4419, -122.1419)],
    'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(37.4300, -122.1400)]}
    )
    return render_template('map.html', mymap=mymap, sndmap=sndmap)
    # conn = connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT  Country, State, City, Lattitude and Longitude  FROM  AdminRegistration")
    # for row in cursor:    
    #        s = s + "<tr>"    
    #        for x in row:    
    #                s = s + "<td>" + str(x) + "</td>"    
    #        s = s + "</tr>"
    # conn.commit()
    # conn.close()
    # return render_template(
    # 'map.html',
    # title='map',
    # year=datetime.now().year,
    # message='User Registration successfully.'
    # )

    
@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'GET':
        return render_template(
        'signin.html',
        title='signin',
        year=datetime.now().year,
        message='User signup sample page.'
        )
    if request.method == 'POST':
        #id = int(request.form["id"])
        username = request.form["Username"]
        password= request.form["Password"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("Select * from [dbo].[UsersRegistration] where Username = ? And PassCode = ?",  username, password)
        for row in cursor.fetchall():
            return render_template(
            'index.html',
            title='User Logged-In successfully.',
            year=datetime.now().year,
            message='User Logged-In successfully.'
            )
        conn.commit()
        conn.close()
        return render_template(
        'signin.html',
        title='signin',
        year=datetime.now().year,
        message='User Logged-In successfully.'
        )



@app.route('/users', methods=["GET", "POST"])
def users():
    if request.method == 'GET':
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("Select Name from [dbo].[UsersRegistration]")
        s = "<table style='border:1px solid red'>"    
        for row in cursor:    
            s = s + "<tr>"    
            for x in row:    
                    s = s + "<td>" + str(x) + "</td>"    
            s = s + "</tr>"
        conn.commit()
        conn.close()
        return render_template(
        'users.html',
        title='users',
        year=datetime.now().year,
        message='Users available',
        result=s
        )
    
    if request.method == 'POST':
        #id = int(request.form["id"])
        name = request.form["name"]
        #email = request.form["email"]
        #passcode = request.form["passcode"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("Select Name from [dbo].[UsersRegistration]")
        s = "<table style='border:1px solid red'>"    
        for row in cursor:    
            s = s + "<tr>"    
            for x in row:    
                    s = s + "<td>" + str(x) + "</td>"    
            s = s + "</tr>"
        conn.commit()
        conn.close()
        return render_template(
        'users.html',
        title='users',
        year=datetime.now().year,
        message='User Registration successfully.',
        result=s
        )
    

@app.route('/partners', methods=["GET", "POST"])
def partners():
    if request.method == 'GET':
        return render_template(
        'partners.html',
        title='partners',
        year=datetime.now().year,
        message='User Partners sample page.'
        )
    if request.method == 'POST':
        #id = int(request.form["id"])
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        country = request.form["country"]
        State = request.form["state"]
        city = request.form["city"]
        lattitude = request.form["lattitude"]
        longitude = request.form["longitude"]
        address = request.form["address"]
        numberofstation = request.form["numberofstation"]
        rateperhour = request.form["rateperhour"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO [dbo].[AdminRegistration] ( [Name], [Email] , [Phone], [Country], [State], [City], [Lattitude], [Longitude], [Address], [NumberofStations], [RatePerHour]) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",  name, email, phone, country, State, city, lattitude, longitude, address, numberofstation, rateperhour)
        conn.commit()
        conn.close()
        return render_template(
        'partners.html',
        title='partners',
        year=datetime.now().year,
        message='User Registration successfully.'
        )
   
    
    

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/chargeafter')
def chargeafter():
    """Renders the chargeafter page."""
    return render_template(
        'chargeafter.html',
        title='chargeafter',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/products')
def products():
    """Renders the products page."""
    return render_template(
        'products.html',
        title='products',
        year=datetime.now().year,
        message='Your application description page.'
    )




@app.route('/rap')
def rap():
    """Renders the rap page."""
    return render_template(
        'rap.html',
        title='rap',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/bookslot')
def bookslot():
    """Renders the bookslot page."""
    return render_template(
        'bookslot.html',
        title='bookslot',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/service')
def service():
    """Renders the service page."""
    return render_template(
        'service.html',
        title='service',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/benefits')
def benefits():
    """Renders the benefits page."""
    return render_template(
        'benefits.html',
        title='benefits',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/index')
def index():
    """Renders the benefits page."""
    return render_template(
        'index.html',
        title='index',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/')
@app.route('/payment')
def bookslot():
    """Renders the home page."""
    return render_template(
        'payment.html',
        title='payment ',
        year=datetime.now().year,
    )


@app.route('/map')
def map():
    mymap = [{'lat': 22.719568, 'lng': 75.857727, 'zoom': 8, 'title': 'My Branch'},
    {'lat': 23.259933, 'lng': 77.412613, 'zoom': 8, 'title': 'My Branch'},
     {'lat': 23.334169, 'lng': 75.037636, 'zoom': 8, 'title': 'My Branch'}]
    return render_template('map.html', mymap=mymap)

    # mymap = Map(
    #     identifier="view-side",
    #     lat=37.4419,
    #     lng=-122.1419,
    #     zoom= 8,
    #     title = "My Demo"
    # )
    # sndmap = Map(
    #     identifier="sndmap",
    #     lat=37.4419,
    #     lng=-122.1419,
    #     markers=[
    #       {
    #          'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
    #          'lat': 37.4419,
    #          'lng': -122.1419,
    #          'infobox': "<b>Hello World</b>"
    #       },
    #       {
    #          'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
    #          'lat': 37.4300,
    #          'lng': -122.1400,
    #          'infobox': "<b>Hello World from other place</b>"
    #       }
    #     ]
    # )
    #return render_template('map.html', mymap=mymap, sndmap=sndmap)
app = Flask(__name__, template_folder="map")

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDPQ9Ktgzo53QTPQbg2tRY_4Txdd84bWbQ"

GoogleMaps(app)


if __name__ == "__main__":
    app.run(debug=True)












