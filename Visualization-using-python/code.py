# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#step 1
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind = 'bar', stacked = True, figsize = (2,5))

#step 2
property_and_loan = data.groupby(['Property_Area' , 'Loan_Status']).size().unstack()
#print(property_and_loan)
property_and_loan.plot(kind= 'bar' , stacked = False , figsize = (10,10))
plt.xlabel('Poperty Area')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)

#step 3
education_and_loan = data.groupby(['Education' , 'Loan_Status']).size().unstack()
#print(education_and_loan)
education_and_loan.plot(kind= 'bar' , stacked = False , figsize = (10,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation = 45)

#Step4
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
graduate.plot(kind ='density' ,label = 'Graduate')
not_graduate.plot(kind ='density' ,label = 'Not Graduate')

#Step 5
fig ,(ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize = (10,10))
data.plot.scatter(x = 'ApplicantIncome' , y = 'LoanAmount',ax = ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter(x = 'CoapplicantIncome' , y = 'LoanAmount',ax = ax_2)
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter(x = 'TotalIncome' , y = 'LoanAmount',ax = ax_3)
ax_3.set_title('Total Income')






