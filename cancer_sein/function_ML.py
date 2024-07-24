import pandas as pd
import joblib 


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
    # link_diabete = 
    # link'

    match id_maladie:
        case 1:
            # definition de la variable target
            target = 'Outcome'

            #chargement du model
            model = joblib.load(r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\MPLclassifier_diabete.plk')

            # preparation des données
            X = df.drop(columns=target, axis=1)
            #prediction
            maladie_pred = False if model.predict(X)[0] == 0 else True

        case 2:
            # definition de la variable target
            target = 'diagnosis'

            #chargement du model
            model = joblib.load(r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\best_model_breast_cancer.pkl')

            # preparation des données
            X = df.drop(target, axis=1)

            #prediction
            maladie_pred = False if str(model.predict(X)[0]) == 'B' else True
            
        case 3:
            # definition de la variable target
            target = 'target'

            #chargement du model
            model = joblib.load(r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\Cardiaque_KNN.pkl')

            # preparation des données
            X = df.drop(target, axis=1)

            #prediction
            maladie_pred = False if model.predict(X)[0] == 0 else True

        case 4:
            # definition de la variable target
            target = 'classification_str'

            #chargement du model
            model = joblib.load(r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\random_forest_model_mrc.pkl')

            # preparation des données
            X = df.drop(target, axis=1)

            #prediction
            maladie_pred = False if str(model.predict(X)[0]) == 'notckd' else True

        case 5:
            # definition de la variable target
            target = 'Dataset'

            #chargement du model
            model = joblib.load(r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\best_model_foie.pkl')

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


