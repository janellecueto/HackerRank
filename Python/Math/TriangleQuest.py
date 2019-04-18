for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)*i)     # this is just plain math. '//' is floor division:
                            # ex. (i=2)  (10**2//9)*2 = (100//9)*2 = 11*2 = 22
                            #     (i=5)  (10**5//9)*5 = (100000//9)*5 = 11111*5 = 55555
                            # NOTE: remove these comments as more the 2 lines results in 0 score 
