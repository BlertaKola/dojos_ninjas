from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/addNinja')
def addNinja():

    dojos = Dojo.getAllDojos()

    return render_template("addNinja.html", dojos=dojos)

@app.route('/createNinja', methods = ['POST'])
def createNinja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.createNinja(data)
    return redirect('/addNinja')

