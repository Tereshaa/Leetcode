class Solution:
    def myPow(self, x: float, n: int) -> float:
        sol=1
        number=n
        if number<0:
            number=-1*number
        while number:
            if number%2==1:
                sol=sol*x
                number=number-1
            elif number%2==0:
                x=x*x
                number=number//2
        if n<0:
            sol=1/sol
        return sol
                
     
 
                
                
        
        