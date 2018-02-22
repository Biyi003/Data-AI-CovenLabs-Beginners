class creditWorthy:

    def attributes():   
        firstName = input ("Enter your first name: ");
        lastName = input ("Enter your last name: ");
        return firstName + " " + lastName;
    
    print ("Please, follow the instructions given for each question carefully")

    def detectIntent():
        print ("\nFor the following question, the options are Personal, Business or Project")
        print ("Example: If I would be using the loan for a personal purpose, my reply would be 'Personal'") 
        intentVar = input ("What will you use the loan for if offered?\n");
        intentVar = intentVar.lower()
        if (intentVar == "personal"):
            ans_intent = 1
        elif (intentVar == "business"):
            ans_intent = 2
        elif (intentVar == "project"):
            ans_intent = 3
        else:
            print ("Unacceptable")
            ans_intent = 0
        return ans_intent;
        
    def detectNetworth():
        print ("\nFor the next question, note that your Net worth should be in numbers only, no characters or alphabets please E.G 207900")
        networthVar = int(input("What is your networth?\n"));
        if (networthVar<200000 and networthVar>=100000):
            ans_networth = 1
        elif (networthVar<300000 and networthVar>=200000):
            ans_networth = 2
        elif (networthVar>=300000):
            ans_networth = 3
        else:
            print ("Unacceptable")
            ans_networth = 0
        return ans_networth;

    def detectExpression():
        print ("\nFor the next question, note that you are to choose from Depressed, Happy, Sad or Bored")
        print ("Example: If I will be sad after getting this loan, my reply would be 'sad'")
        expressionVar = (input ("How do you feel currently?\n"));
        expressionVar = expressionVar.lower()
        if (expressionVar == "depressed"):
            ans_expression = 1
        elif (expressionVar == "happy"):
            ans_expression = 2
        elif (expressionVar == "sad"):
            ans_expression = 3
        elif (expressionVar == "bored"):
            ans_expression = 4
        else:
            print ("Unacceptable")
            ans_expression = 0
        return ans_expression;

    def detectLoan():
        print ("\nFor the next question, note that the loan you want to get should be inputed in numbers only, no characters or alphabets please E.G 301400")
        loanVar = int(input("How much would you like to be loaned?\n"));
        if (loanVar <200000 and loanVar >= 100000):
            ans_loan = 1
        elif (loanVar < 300000 and loanVar >= 200000):
            ans_loan = 2
        elif (loanVar < 400000 and loanVar >= 3000000):
            ans_loan = 3
        elif (loanVar > 500000):
            ans_loan = 4
        else:
            print ("Unacceptable")
            ans_loan = 0
        return ans_loan;

    def detectAge():
        ageVar = int(input("\nWhat is your age?\n"));
        if (ageVar <= 29 and ageVar > 17):
            ans_age = 1
        elif (ageVar <= 45 and ageVar > 29):
            ans_age = 2
        elif (ageVar <= 60 and ageVar > 45):
            ans_age = 3
        else:
            print ("Unacceptable")
            ans_age = 0
        return ans_age;

    def detectMaritalstatus():
        print ("\nFor the next question, note that you are to choose from Single, Married or Divorced")
        print ("Example: If I am married, my reply would be 'married'")
        maritalstatusVar = (input("What is your marital status?\n"));
        maritalstatusVar = maritalstatusVar.lower()
        if (maritalstatusVar == "single"):
            ans_maritalstatus = 1
        elif (maritalstatusVar == "married"):
            ans_maritalstatus = 2
        elif (maritalstatusVar == "divorced"):
            ans_maritalstatus = 3
        else:
            print ("Unacceptable")
            ans_maritalstatus = 0
        return ans_maritalstatus;

applicant = creditWorthy
Name = applicant.attributes()
intent = applicant.detectIntent()
netWorth = applicant.detectNetworth()
expression = applicant.detectExpression()
loan = applicant.detectLoan()
age = applicant.detectAge()
maritalStatus= applicant.detectMaritalstatus()

final_input = []
# final_input = str(expression+netWorth+intent+loan+age+maritalStatus)

final_input.append(expression)
final_input.append(netWorth)
final_input.append(intent)
final_input.append(loan)
final_input.append(age)
final_input.append(maritalStatus)

print (final_input)
    
         
        
                      
            
