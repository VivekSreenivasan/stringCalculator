from stringCalculator import StringCalculator

stringCalculator = StringCalculator()
print(stringCalculator.parse("+,6,A"))
stringCalculator.tokens=[]
print(stringCalculator.parse("%,A,1"))