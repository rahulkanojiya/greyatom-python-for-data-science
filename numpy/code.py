# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate((data , new_record))
print(census.shape)

age = census[ : , [0] ] #this takes only first column 
max_age = np.max(age)
min_age = np.min(age)
print(max_age ,min_age )
age_mean = np.mean(age)
age_std = np.std(age)
print("mean of age = {0} and standard deviation of age  = {1}".format(age_mean, age_std))


#step 3
race = census[: , [2]]
race_0 = [i for i in race if i==0 ]
race_1 = [i for i in race if i==1 ]
race_2 = [i for i in race if i==2 ]
race_3 = [i for i in race if i==3 ]
race_4 = [i for i in race if i==4 ]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
print(len_0 ,len_1,len_2,len_3,len_4)
race_len = np.array([len_0, len_1, len_2, len_3, len_4])
race_min = np.min(race_len)
x=0
for i in race_len:
    if i == race_min:
        minority_race = x
    x+=1
print(minority_race)


#Step 4


working_hours = census[ : , [6]]
matrix = np.array([age , working_hours])

i = 0
j = 0
working_hours_sum = []
senior_citizens = []
while j < len(age) :
    if matrix[0][i] > 60 :
        senior_citizens = np.append(senior_citizens , matrix[0][i])

        working_hours_sum = np.append(working_hours_sum , matrix[1][i])
    i += 1
    j += 1

avg_working_hours = working_hours_sum.sum() / len(senior_citizens)
print(avg_working_hours)

#step 5
education_num = census[ : , [1]]
income = census[ : , [7]]
income_education = np.array([education_num , income])
avg_pay_high = []
avg_pay_low = []
i , j = 0 , 0
while j < len(income):
    if income_education[0][i] > 10 :
        avg_pay_high = np.append(avg_pay_high , income_education[1][i])
    else :
        avg_pay_low = np.append(avg_pay_low , income_education[1][i])
    i += 1 
    j += 1
avg_pay_high = np.mean(avg_pay_high)
avg_pay_low = np.mean(avg_pay_low)
print(avg_pay_high)
print(avg_pay_low)










