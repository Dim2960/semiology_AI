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
    link_diabete = r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\MPLclassifier_diabete.plk'
    link_cancer = r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\best_model_breast_cancer.pkl'
    link_heart = r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\Cardiaque_KNN.pkl'
    link_mrc = r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\random_forest_model_mrc.pkl'
    link_liver = r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\best_model_foie.pkl'



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


