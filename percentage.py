#percentage = input('What is the percentage?')
#print('The percentage is ', percentage,%)

def get_percentage():
    while True:
        try:
            return float(input('What is the percentage? '))
        except:
            print('That isn\'t a number, please try again!')

percentage = get_percentage()

def get_value():
    while True:
        try:
            return float(input('What is the value? '))
        except:
            print('That isn\'t a number, please try again!')

value = get_value()

result = value * percentage/100

print(percentage,"%", "of", value, "=", result,)