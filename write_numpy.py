import numpy as np
from sklearn import linear_model


#  Getting the values from the_csv
expression,net_worth,intent,loan,age,marital_stat,Y = np.genfromtxt('./Model1.csv', delimiter=',', dtype=int, unpack=True)
# Removing the Header of the 
column
Y= np.delete(Y, 0)
expression = np.delete(expression, 0)
net_worth = np.delete(net_worth, 0)
intent = np.delete(intent, 0)
loan = np.delete(loan, 0)
age = np.delete(age,0)
marital_stat = np.delete(marital_stat, 0)

# Combining the X values
# TODO Convert intent and expression to ordinal data
X =  np.column_stack((expression,net_worth,intent,loan,age,marital_stat))

# Training the Model
reg = linear_model.LinearRegression()
print (reg.fit (X, Y))
print (reg.coef_)

print(reg.predict([[0,0,0,0,0,0]]))