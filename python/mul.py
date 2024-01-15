print("        Table de Multiplication")
i = 1
while i<=9 :
    for j in range(1,10):
        for k in range(i,i+3):
            print (k, " x ",j," = ",k*j,end="\t| ")
        print()
    print("--------------------------------------------------------------------------------------------------")
    i =k+1
            