def display_multiplication_table(n1,n2):
    for j in range(1,10):
        for i in range(n1,n2+1):
            print(i,'×',j,'=',i*j,end='\t')
        print()
    print()

display_multiplication_table(2,5)
display_multiplication_table(6,9)
