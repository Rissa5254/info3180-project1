from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, DecimalField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    
    bedrooms = IntegerField('No. of Rooms', validators=[InputRequired(), NumberRange(min=0)])
    bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired(), NumberRange(min=0)])
    
    price = DecimalField('Price', places=2, validators=[InputRequired()])
    
    type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    
    location = StringField('Location', validators=[InputRequired()])
    
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    
