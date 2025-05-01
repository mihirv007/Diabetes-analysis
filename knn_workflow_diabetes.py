import pandas as pd 
import numpy as np
import math
import time
import joblib

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score 

#how to see datasets in vs code
dataset=pd.read_csv(r"//Users//mihirverma//knn_workflow_diabetes//diabetes.csv")

print(dataset.head())
print(len(dataset))

zero_not_accepted=['Glucose','BloodPressure','SkinThickness','BMI','Insulin']

for names in dataset:
    print(f'{names} max:{dataset[names].max()}')
    print(f'{names} min:{dataset[names].min()}')
    

#clean and manipulate dataset
for column in zero_not_accepted:
    dataset[column]=dataset[column].replace(0,np.NaN)# what np.NaN does in numpy 
    mean=int(dataset[column].mean(skipna=True))
    dataset[column]=dataset[column].replace(np.NaN,mean)

#split the dataset
    
X=dataset.iloc[:,0:8]
y=dataset.iloc[:,8]

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.2)

#feature scaling or making dataset uniform

sc_X=StandardScaler() 
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.fit_transform(X_test)

# Save the scaler
#joblib.dump(sc_X, 'scaler.pkl')
print("Scaler saved successfully!")

#define the model: init knn

classifier=KNeighborsClassifier(n_neighbors=11,p=1,metric='manhattan')

#fit model
start_time = time.time()
classifier.fit(X_train,y_train)
KNeighborsClassifier(algorithm='auto',leaf_size=30,metric='',metric_params=None,
                     n_jobs=1,n_neighbors=11,p=1,weights='distance')
print(f"Training time: {time.time() - start_time:.2f} seconds")

print(f'y:{len(y)}')
print(f'y_train:{len(y_train)}')
print(f'y_test:{len(y_test)}')
print(f'X_train:{len(X_train)}')
print(f'X_test:{len(X_test)}')


#predict the test set result

y_pred=classifier.predict(X_test)
print(y_pred)

#evaluate model

cm=confusion_matrix(y_test,y_pred)
print(cm)

# Plot the confusion matrix
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=[0, 1], yticklabels=[0, 1])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()

#accuracy

print(f1_score(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

# Save the trained model to a file
joblib.dump(classifier, 'knn_model.pkl')
print("Model saved successfully!")


# Plot F1 Score and Accuracy
f1 = f1_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
metrics = [f1, accuracy]
metrics_names = ['F1 Score', 'Accuracy']

plt.bar(metrics_names, metrics, color=['blue', 'green'])
plt.title("KNN Model Performance Metrics")
plt.ylabel("Score")
plt.show()

# Plot feature distributions
dataset[zero_not_accepted].hist(bins=10, figsize=(10, 8))
plt.suptitle('Feature Distributions')
plt.show()

# Pair Plot for feature relationships
sns.pairplot(dataset[zero_not_accepted])
plt.show()





      
