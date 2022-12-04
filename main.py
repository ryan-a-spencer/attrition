from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Age : int
    BusinessTravel : int
    DailyRate : int
    Department : varchar
    DistanceFromHome : int
    Education : int
    EducationField : varchar
    EmployeeCount : int
    EmployeeNumber : int
    EnvironmentSatisfaction : int
    Gender : varchar
    HourlyRate : int
    JobInvolvement : int
    JobLevel : int
    JobRole : varchar
    JobSatisfaction : int
    MaritalStatus : varchar
    MonthlyIncome : int
    MonthlyRate : int
    NumCompaniesWorked : int
    Over18 : Boolean
    OverTime : Boolean
    PercentSalaryHike : int
    PerformanceRating : int
    RelationshipSatisfaction : int
    StandardHours : int
    StockOptionLevel : int
    TotalWorkingYears : int
    TrainingTimesLastYear : int
    WorkLifeBalance : int
    YearsAtCompany : int
    YearsInCurrentRole : int
    YearsSinceLastPromotion : int
    YearsWithCurrManager : int
    

# loading the saved model
attrition_model = pickle.load(open('attrition_model.sav','rb'))


@app.post('/attrition_prediction')
def attition_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['Age']
    travel = input_dictionary['BusinessTravel']
    dailyrate = input_dictionary['DailyRate']
    dept = input_dictionary['Department']
    distance = input_dictionary['DistanceFromHome']
    education = input_dictionary['Education']
    field = input_dictionary['EducationField']
    count = input_dictionary['EmployeeCount']
    nr = input_dictionary['EmployeeNumber']
    envsatisfaction = input_dictionary['EnvironmentSatisfaction']
    gender = input_dictionary['Gender']
    rate = input_dictionary['HourlyRate']
    involvement = input_dictionary['JobInvolvement']
    level = input_dictionary['JobLevel']
	role = input_dictionary['JobRole']
    jobsatisfaction = input_dictionary['JobSatisfaction']
    maritalstatus = input_dictionary['MaritalStatus']
    income = input_dictionary['MonthlyIncome']
    companies = input_dictionary['NumCompaniesWorked']
    adult = input_dictionary['Over18']
    ot = input_dictionary['OverTime']
    raise = input_dictionary['PercentSalaryHike']
    pr = input_dictionary['PerformanceRating']
    relationship = input_dictionary['RelationshipSatisfaction']
    workingyears = input_dictionary['TotalWorkingYears']
    training = input_dictionary['TrainingTimesLastYear']
    wlb = input_dictionary['WorkLifeBalance']
    companyyears = input_dictionary['YearsAtCompany']
    currentrole = input_dictionary['YearsInCurrentRole']
    promo = input_dictionary['YearsSinceLastPromotion']
    manager = input_dictionary['YearsWithCurrManager']

    input_list = [age, travel, dailyrate, dept, distance, education, 
					field, count, nr, envsatisfaction, gender,
					rate, involvement, level, role, jobsatisfaction,
					maritalstatus, income, companies, adult,
					ot, raise, pr, relationship, workingyears,
					training, wlb, compnayyears, currentrole,
					promo, manager]
    
    prediction = attrition_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person is likely to leave'
    
    else:
        return 'The person is not likely to leave'


