def generatePermutation(s,i):  
    j = 0;  
    if(i == len(s)-1):  
        print(s);  
    else:   
        for j in range(i,len(s)):
            x = list(s);  
            x[i],x[j]=x[j],x[i]     
            generatePermutation("".join(x),i+1);  
                #Swapping the string by fixing a character  
            x[i],x[j]=x[j],x[i]     
str = "ABC"   
print("All the permutations of the string are: ");  
generatePermutation(str,0);  