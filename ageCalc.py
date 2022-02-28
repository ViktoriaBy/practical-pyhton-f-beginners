# Create an Age Calculator

age = int(input('How old are you?\n')) # everything input returns is a string
decades = age//10 # // -> whole number division
years = age % 10

print('You are ' + str(decades) + ' decades and ' + str(years) + ' years old.')