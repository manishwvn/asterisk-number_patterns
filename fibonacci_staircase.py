# print the following pattern of fibonacci sequence in staircase pattern
'''   
0 
1 1 
2 3 5 
8 13 21 34 
'''

n = 4
a, b = 0, 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(a, end=' ')
        c = a + b
        a = b
        b = c
    print()
