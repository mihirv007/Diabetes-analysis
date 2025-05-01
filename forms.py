from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField
from wtforms.validators import DataRequired,NumberRange
import secrets

class diabetes_form(FlaskForm):
    Pregnancies=IntegerField('Pregnancies',validators=[DataRequired(message="Glucose level is required."),NumberRange(min=0,max=20)]
                        ,render_kw={"min":0,"max":20,"inputmode":"numeric","step":"1","maxlength":"2"})
    
   
    Glucose=IntegerField('Glucose',validators=[DataRequired(),NumberRange(min=50,max=400)]
                         ,render_kw={"min":50,"max":400,"inputmode":"numeric","step":"1","maxlength":"3"})
    
    BloodPressure=IntegerField('BloodPressure',validators=[DataRequired(),NumberRange(min=50,max=200)]
                        ,render_kw={"min":50,"max":200,"inputmode":"numeric","step":"1","maxlength":"3"})
    
    SkinThickness=IntegerField('SkinThickness',validators=[DataRequired(),NumberRange(min=5,max=100)]
                        ,render_kw={"min":5,"max":100,"inputmode":"numeric","step":"1","maxlength":"3"})
    
    Insulin=IntegerField('Insulin',validators=[DataRequired(),NumberRange(min=10,max=1000)]
                         ,render_kw={"min":10,"max":999,"inputmode":"numeric","step":"1","maxlength":"3"})
    
    BMI=IntegerField('BMI',validators=[DataRequired(),NumberRange(min=5,max=100)]
                        ,render_kw={"min":5,"max":100,"inputmode":"numeric","step":"1","maxlength":"3"})
    
    DiabetesPedigreeFunction=IntegerField('DiabetesPedigreeFunction',validators=[DataRequired(),NumberRange(min=1,max=2)]
                        ,render_kw={"min":1,"max":2,"inputmode":"numeric","step":"1","maxlength":"1"})
    
    Age=IntegerField('Age',validators=[DataRequired(),NumberRange(min=5,max=120)]
                    ,render_kw={"min":5,"max":120,"inputmode":"numeric","step":"1","maxlength":"3"})

    submit=SubmitField('submit')






