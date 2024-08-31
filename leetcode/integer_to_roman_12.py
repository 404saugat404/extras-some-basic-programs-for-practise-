def int_to_roman(number):
    dict={
            "M":1000,
            "CM":900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1,
            
        }
    
    result=''

    for roman, value in dict.items():
        count=number//value
        result=result+count*roman
        number=number%value

    return result


number=3749
print(int_to_roman(number=number))

