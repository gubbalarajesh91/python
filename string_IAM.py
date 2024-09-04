arn = "arn:aws:iam::123456789012:user/johndoe"
print(arn.split("/")[1])

#UpperCase & LowerCase
name = "rajesh"
uppercase = name.upper()
lowercase = name.lower()
print(name.upper())
print(name.lower())
print("UpperCase:", uppercase)
print("LowerCase:", lowercase)

#String club(String Concatination)
str1 = "Hello"
str2 = "Rajesh"
result = str1 + " " + str2
print(str1 + " " + str2)
print(result[6])
print(result)

#Length count
text = "Python is awesome"
length = len(text)
print("Length of the String:", length)