#DESCRIPTION:
#Given two arrays of strings a1 and a2 return a sorted 
# array r in lexicographical order of the strings 
# of a1 which are substrings of strings of a2.

#Example 1:
#a1 = ["arp", "live", "strong"]
#a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#returns ["arp", "live", "strong"]
import  re
a1 = ['1028', '1295', 'ar']

a2 = ["liv1028ely", "ali1295ve", "harp", "sharp", "armstrong"]
result=[]
for x in a1:
    for y in a2:
        if y.count(x)==1:
            result.append(x)
            break
result=list(set(result))    
result.sort()        
print(result)
    
