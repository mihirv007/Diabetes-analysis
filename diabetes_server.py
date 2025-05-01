from flask import Flask,render_template,url_for,redirect
import numpy as np 
from flask_sqlalchemy import SQLAlchemy
from forms import diabetes_form
import joblib
from flask_migrate import Migrate
import pandas as pd

app=Flask(__name__)
app.config['SECRET_KEY']='b9ed95bedb6db90ba2a0e5d53fce4e3a'

#users data
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)#creating insitants of database to work with the data

#migrate data
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    Pregnancies=db.Column(db.Integer,nullable=False)
    Insulin=db.Column(db.Integer,nullable=False)
    Glucose=db.Column(db.Integer,nullable=False)
    BloodPressure=db.Column(db.Integer,nullable=False)
    SkinThickness=db.Column(db.Integer,nullable=False)
    BMI=db.Column(db.Integer,nullable=False)
    DiabetesPedigreeFunction=db.Column(db.Integer,nullable=False)
    Age=db.Column(db.Integer,nullable=False)
    #prediction=db.Column(db.Integer,nullable=False)

    def show_Users_data(self):
        return f"""data(Pregnancies:'{self.Pregnancies}', Insulin:'{self.Insulin}',Glucose:'{self.Glucose}',
               BloodPressure:'{self.BloodPressure}',SkinThickness:'{self.SkinThickness}' ,BMI:'{self.BMI}',
                DiabetesPedigreeFunction:'{self.DiabetesPedigreeFunction}', Age:'{self.Age}')"""


# Load the trained KNN model
classifier = joblib.load('knn_model.pkl')

# Load the scaler
sc_X = joblib.load('scaler.pkl')

@app.route('/')
@app.route('/knn_workflow_diabetes',methods=['POST','GET'])
def predict():
    form=diabetes_form()
    result=None
    if form.validate_on_submit():
       
        data=np.array([[
            form.Pregnancies.data,
            form.Glucose.data,
            form.BloodPressure.data,
            form.SkinThickness.data,
            form.Insulin.data,
            form.BMI.data,
            form.DiabetesPedigreeFunction.data,
            form.Age.data]])

        scaler_data = sc_X.transform(data)
        prediction_result=classifier.predict(scaler_data)

        if prediction_result[0]==1:
            result='you have diabetes'
        else:
            result='you donot have diabetes'

         # Save data to the database
        user = User(
            Pregnancies=form.Pregnancies.data,
            Insulin=form.Insulin.data,
            Glucose=form.Glucose.data,
            BloodPressure=form.BloodPressure.data,
            SkinThickness=form.SkinThickness.data,
            BMI=form.BMI.data,
            DiabetesPedigreeFunction=form.DiabetesPedigreeFunction.data,
            Age=form.Age.data
            #prediction=prediction_result[0]
            )

        db.session.add(user)
        db.session.commit()  # Save the data to the database
        
    return render_template('knn_workflow_diabetes.html',prediction_text=result,title='diabetes_analysis',form=form)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5001)