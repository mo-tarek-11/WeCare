import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import  RandomizedSearchCV, train_test_split , GridSearchCV
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
#To turn off warning messages.
import warnings
warnings.filterwarnings('ignore')


# Importing the dataset 
data = pd.read_csv("HepatitisCdata.csv")  

data = data.drop(["Unnamed: 0"], axis = 1)  

#Convert categorical to binary in Category & Sex
data['Category'] = data['Category'].map({'0=Blood Donor': 0, 
                                         '0s=suspect Blood Donor': 0, 
                                         "1=Hepatitis" : 1, 
                                         "2=Fibrosis" : 1, 
                                         "3=Cirrhosis" : 1})

data['Sex'] = data['Sex'].map({'m': 1, 'f': 0})

data.fillna(data.median() ,inplace=True)

n_cols = {'ALB':'Albumin Blood Test (ALB) g/L ',
            'ALP':  'Alkaline Phosphatase Test (ALP) IU/L',
            'ALT': 'Alanine Transaminase Test (ALT) U/L',
            'AST' : 'Aspartate Transaminase Test (AST) U/L',
            'BIL': 'Bilirubin Blood Test (BIL) µmol/L',
            'CHE' : 'Cholinesterase (CHE) kU/L' ,
            'CHOL' : 'Cholesterol (CHOL) mmol/L',
            'CREA' : 'Creatinine Blod Test (CREA) µmol/L',
            'GGT' : 'Gamma-Glutamyl Transpeptidase Test (GGT) U/L',
            'PROT' : 'Protein Blood Test (PROT) g/L'}

data.rename(columns=n_cols ,inplace=True)

print(f'Good People : {data.Category.value_counts()[0]}')
print(f'Infected People : {data.Category.value_counts()[1]}')

# Splitting the data  
X = data.drop(["Category"], axis = 1)  
y = data["Category"]  
X = X.drop(["Albumin Blood Test (ALB) g/L "], axis = 1)  
#Splitting the data into the training and testing set  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) 

clf_rnf=RandomForestClassifier(random_state =46)
parametrs_rnf={ 
    'n_estimators': [200, 500],
    'max_features': [ 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}
grid_forest=GridSearchCV(clf_rnf, parametrs_rnf, cv=6, n_jobs=-1)
grid_forest.fit(X_train,y_train)

best_model_rnf=grid_forest.best_estimator_
y_pred_rnf=best_model_rnf.predict(X_test)

cm_rnf = confusion_matrix(y_test, y_pred_rnf)
print("Confution matrix for model " f'{best_model_rnf} : \n',cm_rnf)
ac_rnf = accuracy_score(y_test, y_pred_rnf)
print("Accuracy score for model " f'{best_model_rnf} : ',ac_rnf)
cr_rnf = classification_report(y_test, y_pred_rnf)
print("classification_report for model " f'{best_model_rnf} : \n',cr_rnf)

print(best_model_rnf.score(X_train,y_train))
print(best_model_rnf.score(X_test,y_test))

pickle.dump(best_model_rnf, open('Cmodel.pkl' , 'wb'))

model = pickle.load(open('Cmodel.pkl' , 'rb'))

print(model.predict([[32,1,52.5,7.7,22.1,7.5,6.9,3.2,106,12,70]]))
print(model.predict([[50,1,230,200,300,220,15,9,320,600,80]]))

