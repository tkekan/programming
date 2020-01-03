def divide(dividend, divisor): 
      
    # Calculate sign of divisor  
    # i.e., sign will be negative 
    # either one of them is negative 
    # only iff otherwise it will be 
    # positive 
      
    sign = (-1 if((dividend < 0) ^  
                  (divisor < 0)) else 1); 
      
    # remove sign of operands 
    dividend = abs(dividend); 
    divisor = abs(divisor); 
      
    # Initialize 
    # the quotient 
    quotient = 0; 
    temp = 0; 
      
    # test down from the highest  
    # bit and accumulate the  
    # tentative value for valid bit 
    for i in range(31, -1, -1): 
        if (temp + (divisor << i) <= dividend): 
            temp += divisor << i; 
            quotient |= 1 << i; 
    remainder = dividend - temp
    #print "Remainder: %d" % remainder    
    return sign * quotient,remainder; 
  
# Driver code 
a = 100; 
b = 30; 
ans, r = divide(a, b) 
print "Ans: %d Remainder : %d" %(ans,r)
  
a = 438; 
b = 30; 
ans, r = divide(a, b) 

print "Ans: %d Remainder : %d" %(ans,r)
