file = open('attendance.txt', 'r')
lines = file.read().split('\n')
print(lines)
if lines[0] == '':
    exit(0)
for l in lines:
    print("H")