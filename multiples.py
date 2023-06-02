#assign value to total

sum = 0;

#run loop ,the index  starts from 0 ends 999

for i in range(1000):
    #use modular to check if there is no remainder
    if i%3==0 or i%5==0 :
        
        #add everything and increment
        sum+=i

    #exit loop aand print
print(sum)

    

    