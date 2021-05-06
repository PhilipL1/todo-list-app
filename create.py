from application.models import db, Tasks

db.drop_all()
db.create_all()

test = Tasks(description = "finally works kmt")
db.session.add(test)
db.session.commit()