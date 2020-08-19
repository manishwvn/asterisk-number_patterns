# to print the following pattern
'''
'''

n = 5  # number of lines to print in output

for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j == n + 1:
            print('*\t', end = ' ')
        else:
            print('\t', end = ' ')

    print()
