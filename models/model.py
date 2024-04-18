import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import  RandomizedSearchCV, train_test_split , GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import pickle

#To turn off warning messages.
import warnings
warnings.filterwarnings('ignore')

# Importing the dataset 
data = pd.read_csv("heart.csv")  

n_cols = {'cp':'Chest Pain Type (CP)',
          'trestbps':'Resting Blood Pressure (trestbps)',
          'chol':'Serum Cholestoral (chol) mg/dl',
          'fbs':  'Fasting Blood Sugar (fbs) > 120 mg/dl',
          'restecg': 'Resting Electrocardiographic Results (restecg)',
          'thalach' : 'Maximum Heart Rate Achieved (thalach)',
          'exang': 'Exercise Induced Angina (exang)',
          'oldpeak' : 'ST depression (oldpeak)' ,
          'slope' : 'Slope of the ST Segment (slope)',
          'ca' : 'Number of Major Vessels (ca)',
          'thal' : 'Thal'}

data.rename(columns=n_cols ,inplace=True)

#Scale all values for good Accuracy
#sc = StandardScaler()
#col = ['age',
 #      'Resting Blood Pressure (trestbps)', 
  #     'Serum Cholestoral (chol) mg/dl', 
   #    'Maximum Heart Rate Achieved (thalach)', 
    #   'ST depression (oldpeak)']
#data[col] = sc.fit_transform(data[col])


# Splitting the data  
X = data.drop(["target"], axis = 1)  
y = data["target"]  
  
#Splitting the data into the training and testing set  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)  


clf_knn=KNeighborsClassifier()
parametrs_knn={'n_neighbors':[1,3,5,7,9,11], 'metric':['euclidean','manhattan','chebyshev']}
grid_clf_knn=GridSearchCV(clf_knn, parametrs_knn, cv=6, n_jobs=-1)
grid_clf_knn.fit(X_train, y_train)


best_model_knn=grid_clf_knn.best_estimator_
y_pred_knn=best_model_knn.predict(X_test)



cm_knn = confusion_matrix(y_test, y_pred_knn)
print("Confution matrix for model " f'{best_model_knn} : \n',cm_knn)
ac_knn = accuracy_score(y_test, y_pred_knn)
print("Accuracy score for model " f'{best_model_knn} : ',ac_knn)
cr_knn = classification_report(y_test, y_pred_knn)
print("classification_report for model " f'{best_model_knn} : \n',cr_knn)

print(best_model_knn.score(X_test,y_test))
print(best_model_knn.score(X_train,y_train))

pickle.dump(best_model_knn, open('model.pkl' , 'wb'))

model = pickle.load(open('model.pkl' , 'rb'))
print(model.predict([[22,1,1,100,150,0,2,100,1,3,1,1,3]]))
print(model.predict([[77,1,4,200,500,3,3,202,1,6.2,3,3,7]]))





