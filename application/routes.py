from application.forms import TaskForm
from application import app, db
from application.models import Tasks
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for


@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all()
    output=""
    return render_template("index.html", title="Home", all_tasks = all_tasks)

@app.route("/create", methods=["GET", "POST"]) #allow get & post request 
def create():
    form=TaskForm()
    if request.method == "POST": #post request: send  the filled/complete info to the route
        if form.validate_on_submit():
            new_task = Tasks(description = form.description.data) #check if new task has been added with the data
            db.session.add(new_task) # add the new task to the route 
            db.session.commit() # commit to the data base itself
            return redirect(url_for("home"))  #back to the home page
    return render_template("add.html", title = "Create a Task", form=form)

@app.route("/complete/<int:id>") #button will only do post request  
def complete(id):
    task=Tasks.query.filter_by(id=id).first()
    task.completed =True
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/incomplete/<int:id>") #button will only do post request 
def incomplete(id):
    task= Tasks.query.filter_by(id=id).first()
    task.completed =False
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:id>", methods=["GET","POST"]) #buton will get the id & post request 
def update(id):
    form= TaskForm()
    task= Tasks.query.filter_by(id=id).first()
    if request.method =="POST": # id the form has been posted 
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home")) 
    return render_template("update.html", form=form, title="Update Task", task=task)
   
@app.route("/delete/<int:id>")
def delete(id):
    task=Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))