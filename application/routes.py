from application import app, db
from application.models import Tasks

@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all()
    output=""
    if not all_tasks:
        return "No tasks have been created"
    else:
        for task in all_tasks:
            output += task.description + " - Completed? "+ str(task.completed) + "<br>"
        return output

@app.route("/create")
def create():
    new_todo= Tasks(description="New task")
    db.session.add(new_todo)
    db.session.commit()
    return "New task added"

@app.route("/complete/<int:id>")
def complete(id):
    task=Tasks.query.filter_by(id=id).first()
    task.completed =True
    db.session.commit()
    return f"Task {id} is now completed"

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task= Tasks.query.filter_by(id=id).first()
    task.completed =False
    db.session.commit()
    return f"Task {id} is now incomplete "

@app.route("/update/<new_description>")
def update(new_description):
    task=Tasks.query.order_by(Tasks.id.desc()).first()
    task.description = new_description 
    db.session.commit()
    return f"Most recent task was updated with the description: {new_description}"

@app.route("/delete/<int:id>")
def delete(id):
    task=Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} was deleted"