from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def dashboard():
    dojos = Dojo.getAllDojos()

    return render_template("dashboard.html", dojos=dojos)

@app.route('/addDojo', methods = ['POST'])
def createNewDojo():
    data = {
        'name': request.form['name']
    }
    Dojo.createDojo(data)
    return redirect('/')
#/dojos/{{dojo.id}}

@app.route('/dojos/<int:id>')
def showDojosInfo(id):
    data = {
        'id': id
    }
    dojos = Dojo.getDojosInfoById(data)
    return render_template("showNinja.html",dojos = dojos, ninjas= Ninja.getDojosNinjas(data))