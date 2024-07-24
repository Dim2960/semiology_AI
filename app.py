import secrets
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField, HiddenField, FileField,IntegerField
from wtforms.validators import DataRequired, Length



# Create a Flask app
app = Flask(__name__)
# Generate a random secret key
foo = secrets.token_urlsafe(16)
# Set the secret key of the app
app.secret_key = foo
# Create a CSRFProtect object
csrf = CSRFProtect(app)

# Set the dictionary of diseases
diseaseDict = {1  :  'Diabetes',
               2  : 'Cancer',
               3  :  'Heart Disease',
               4  : 'MRC',
               5 : 'Liver'
               }



class UploadForm(FlaskForm):
    disease = HiddenField('Disease', validators=[DataRequired()])
    csv_file = FileField('CSV File', validators=[DataRequired()])
    submit = SubmitField('Upload')



@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        disease = form.disease.data
        csv_file = form.csv_file.data
        message = f'You have selected {diseaseDict[disease]} and uploaded {csv_file.filename}'
    else:
        message = 'Wasted'
    return render_template('form.html', form=form, message=message)


if __name__ == '__main__':
    app.run(debug=True)