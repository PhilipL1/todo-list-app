from flask_wtf import FlaskForm #class that the forms clasess are going to inherit from so they need to be type form 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

class TaskForm(FlaskForm):
    description= StringField('Description of the Task', validators=[DataRequired()])
    submit=SubmitField('Add Task') # the botton
