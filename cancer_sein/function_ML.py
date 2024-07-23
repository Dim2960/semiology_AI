import pandas as pd
import joblib 


def prediction(id_maladie: int, df:pd.DataFrame)->dict[str:int, str:bool]:

    '''
    Prediction des maladie en fonction des différents model cahr

    diseaseDict = {1  :  'Diabetes',
                    2  : 'Cancer',
                    3  :  'Heart Disease',
                    4  : 'MRC',
                    5 : 'Liver'
                }

    '''

    match id_maladie:
        case 1:
            pass

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
            pass
        
        case 4:
            pass

        case 5:
            pass
        
        case _:
            pass
    
    try:


        return {"maladie": id_maladie, "prediction": maladie_pred}
    
    except:
        print('erreur de chargement maladie')




df_cancer = pd.read_csv(r'C:\Users\dimle\Documents\clone_repo\semiology_AI\cancer_sein\data_clean_cancer_test.csv')

df_cancer = df_cancer.head(1)

print(df_cancer)

pred = prediction(2, df_cancer)

print(pred)
