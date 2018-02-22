class CalculateCreditWorth

    def CreditCalculation():


        
        result = 0
        if (result >= 60 and result <= 80):
            print ("You will be granted the loan.\nCongratulations!")
        elif (result >=45 and result < 60):
            print ("Your request for loan is still under consideration")
        elif (result < 45):
            print ("We are indeed sorry, the loan you request cannot be granted")
        else:
            print ("We are indeed sorry, the loan you request cannot be granted")
        return result;


Total_result = CalculateCreditWorth
Total_result.CreditCalculation
    
    
