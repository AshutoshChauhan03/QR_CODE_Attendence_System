# Opening file where data should be stored
file = open('inputData.txt', "w")
# Taking input for operations
print("Elements to convert into QR CODE : ", end="")
n = int(input())

# Writing on file
for i in range(n):
    ele = input()
    file.write(ele+"\n")

# Executing python file on updated input file
exec(open('generatingQR.py').read())

