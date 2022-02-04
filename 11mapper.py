# Jaya Kumar Saga 1 - Mapper using Files
# Easy to test
# Not quite Hadoop-ready

# open returns a file object
with open("sample.csv", "r") as input:
  with open("output11mapped.txt", "w") as output:

    # iterate through each line in the file object
    for line in input:
      datalist = line.strip().split(";")
      
      if (len(datalist) == 9) : 
        Username, Identifier, password, Recovery_code, First_name, Last_name, Department,Location,Salary = datalist
        
        # output intermediate key-value pairs
        output.write(Username + "\t" + Salary + "\n")

        # display to console (not required - just for the user)
        print(Username + "\t" + Salary + "\n")

