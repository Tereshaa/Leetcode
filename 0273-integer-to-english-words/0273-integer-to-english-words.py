class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Mapping numbers to words
        less_than_20 = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 
            8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 
            19: "Nineteen"
        }
        
        ten = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 
            7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        
        def numstr(n):
            res=[]
            hundreds=n//100
            if hundreds:
                res.append(less_than_20[hundreds] + " Hundred")
            last_2=n%100
            if last_2>=20:
                tens,ones=last_2//10,last_2%10
                res.append(ten[tens])
                if ones:
                    res.append(less_than_20[ones])
            elif last_2:
                res.append(less_than_20[last_2])
            return ' '.join(res)
        
        thousands = ["", " Thousand", " Million", " Billion"]
        i=0
        res=[]
        while num:
            digits=num%1000
            s=numstr(digits)
            if s:
                res.append(s+thousands[i])
            num=num//1000
            i+=1
        res.reverse()
        return " ".join(res)
            
                
        
       