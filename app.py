import secrets
import pandas as pd
import joblib 
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm, CSRFProtect
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import SubmitField, HiddenField, FileField
from wtforms.validators import DataRequired, Length
from werkzeug.utils import secure_filename
import imblearn
from imblearn.over_sampling import SMOTE


# Create a Flask app
app = Flask(__name__)
# Generate a random secret key
foo = secrets.token_urlsafe(16)
# Set the secret key of the app
app.secret_key = foo
# Create a CSRFProtect object
csrf = CSRFProtect(app)

# Set the dictionary of diseases
diseaseDict = {'1'  :  'Diabetes',
               '2'  : 'Cancer',
               '3'  :  'Heart Disease',
               '4'  : 'MRC',
               '5' : 'Liver'
               }



class UploadForm(FlaskForm):
    disease = HiddenField('Disease', id='diseaseId' ,validators=[DataRequired()])
    csv_file = FileField('CSV File', id='fileId', validators=[FileRequired(), FileAllowed(['csv'], 'CSV only!')])
    submit = SubmitField('Upload')

def prediction(id_maladie: int, df:pd.DataFrame)->dict[str:int, str:bool]:

    '''
    Prediction des maladie en fonction des différents model cahr

    diseaseDict = { 1  : 'Diabetes',
                    2  : 'Cancer',
                    3  : 'Heart Disease',
                    4  : 'MRC',
                    5  : 'Liver'
                }

    '''
    link_diabete = r'C:\Users\Work\Desktop\projects\semiology_AI\model\MPLclassifier_diabete.pkl'
    link_cancer = r'C:\Users\Work\Desktop\projects\semiology_AI\model\best_model_breast_cancer.pkl'
    link_heart = r'C:\Users\Work\Desktop\projects\semiology_AI\model\Cardiaque_KNN.pkl'
    link_mrc = r'C:\Users\Work\Desktop\projects\semiology_AI\model\random_forest_model_mrc.pkl'
    link_liver = r'C:\Users\Work\Desktop\projects\semiology_AI\model\best_model_foie.pkl'



    match id_maladie:
        case 1:
            # definition de la variable target
            target = 'Outcome'

            #chargement du model
            model = joblib.load(link_diabete)

            # preparation des données
            X = df.drop(columns=target, axis=1)
            #prediction
            maladie_pred = False if model.predict(X)[0] == 0 else True

        case 2:
            # definition de la variable target
            target = 'diagnosis'

            #chargement du model
            model = joblib.load(link_cancer)

            # preparation des données
            X = df.drop(target, axis=1)

            #prediction
            maladie_pred = False if str(model.predict(X)[0]) == 'B' else True
            
        case 3:
            # definition de la variable target
            target = 'target'

            #chargement du model
            model = joblib.load(link_heart)

            # preparation des données
            X = df.drop(target, axis=1)

            #prediction
            maladie_pred = False if model.predict(X)[0] == 0 else True

        case 4:
            # definition de la variable target
            target = 'classification_str'

            #chargement du model
            model = joblib.load(link_mrc)

            # preparation des données
            X = df.drop(target, axis=1)
            

            #prediction
            maladie_pred = False if str(model.predict(X)[0]) == 'notckd' else True

        case 5:
            # definition de la variable target
            target = 'Dataset'

            #chargement du model
            model = joblib.load(link_liver)

            # preparation des données
            X = df.drop(target, axis=1)

            #prediction
            maladie_pred = False if model.predict(X)[0] == 0 else True
        
        case _:
            pass
    
    try:


        return {"id_maladie": id_maladie, "prediction": maladie_pred}
    
    except:
        print('erreur de chargement maladie')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        disease = form.disease.data
        csv_file = form.csv_file.data
        filename =  secure_filename(csv_file.filename)
        df = pd.read_csv(csv_file)
        print((df.head()))
        reponse_dict = prediction(int(disease), df )
        #{"id_maladie": id_maladie, "prediction": maladie_pred}
        message = f"You have selected {diseaseDict[str(reponse_dict["id_maladie"])]} and you're {reponse_dict['prediction']}"
    else:
        message = "Vous n'avez pas encore choisie une maladie"
    return render_template('form.html', form=form, message=message)


if __name__ == '__main__':
    app.run(debug=True)