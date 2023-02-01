
#DESCRIPTION:
#Complete the solution so that it splits the string into pairs 
# of two characters. If the string contains an odd number of 
# characters then it should replace the missing second character 
# of the final pair with an underscore ('_').

#Examples:

#* 'abc' =>  ['ab', 'c_']
#* 'abcdef' => ['ab', 'cd', 'ef']
def solution(s):
    s2=''
    l=[]
    if len(s)%2!=0:
        s=s+'_'
    for x in range(len(s)):
        s2=s2+s[x]
        if x%2!=0:
            l.append(s2)
            s2=''
    return l
solution('abcdef')    

######## Mejor Forma #####

#import re
#def solution(s):
    #return re.findall(".{2}", s + "_")

#def solution(s):
    #return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]   