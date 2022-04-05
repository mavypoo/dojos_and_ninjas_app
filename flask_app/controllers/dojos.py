from flask_app import app
from flask import render_template, redirect, request, session 

# Import your models
from flask_app.models.dojo import Dojo
                # dojo = model file      Dojo = class Name in dojo.py

# Define our routes!
@app.route("/")
def index():
    return redirect ("/dojos")

# Reoute that shows all dojos on one page 
@app.route("/dojos")
def all_dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("all_dojos.html", all_dojos = dojos)


@app.route("/add/dojos", methods=['POST'])  #route should match html document route on the form
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect("/dojos")
    

@app.route("/dojo/<int:id>")
def show_ninja(id):
    data = {
        "id": id,
    }
    return render_template("grab_ninja.html", dojo=Dojo.get_one_ninja(data))
