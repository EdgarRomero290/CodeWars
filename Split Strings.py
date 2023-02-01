
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



