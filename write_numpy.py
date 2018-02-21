import numpy as np
from sklearn import linear_model


sn,expression,net_worth,intent,Loan,Y = np.genfromtxt('./Model1.csv', delimiter=',', dtype=int, unpack=True)
#  = the_csv
new_Y= np.delete(Y, 0)
print (new_Y)
print (expression)
print (net_worth)
# TODO Convert intent and expression to ordinal data
X =  np.column_stack((net_worth, Loan))

print (X)
reg = linear_model.LinearRegression()
print (reg.fit (X, Y))
print (reg.coef_)
print(reg.predict([[0, 0]]))