# Jaya kumar - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(";")
  if (len(datalist) == 9) : 
    Username, Identifier, password, Recovery_code, First_name, Last_name, Department,Location,Salary = datalist

    # print intermediate key-value pairs to standard output
    print(Username,"\t",1)
