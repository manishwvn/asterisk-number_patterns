# to print the following pattern
'''
*                *   
     *       *       
         *           
     *       *       
*                *   
'''

#hint: if we observe, we print '*' when i == j or i + j = n + 1, where n is number of lines

n = 5

for i in range(1, n + 1):
  for j in range(1, n + 1):
    
    if (i == j) or (i + j == n + 1):
      print('*\t', end = ' ')
    else:
      print('\t', end = ' ')

  print()



