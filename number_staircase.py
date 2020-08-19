# print numbers in the following patterns
'''
1
2 3
4 5 6
7 8 9 10
'''

n = 4  # number of lines to print
val = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(val, end = ' ')
        val += 1
    print()
    
