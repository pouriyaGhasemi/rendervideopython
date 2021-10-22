import sys

# read file to check its on work or not
file1 = open("E:\\limoonad render logo\\c4\\isrun.txt","rt")
statusprogram=file1.readline(1)
print('\n'+statusprogram)
file1.close()
if statusprogram=="1":
    print('\n asd asdasdas')
    sys.exit()
else:
    print('\n asd asdasdas 22')
    file1 = open("E:\\limoonad render logo\\c4\\isrun.txt","wt")
    file1.write("1") 
    file1.close() 






