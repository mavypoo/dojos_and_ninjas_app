from flask_app import app
from flask import render_template, redirect, request, session 

# Import your models
from flask_app.models import ninja, dojo  # Create Flights by doing flight.Flight()


@app.route('/ninjas')
def all_ninjas():
    return render_template("all_ninjas.html", dojos=dojo.Dojo.get_all())


@app.route('/add/ninja', methods=['POST'])
def create():
    ninja.Ninja.save(request.form)
    return redirect('/')

