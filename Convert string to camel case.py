#DESCRIPTION:
#Complete the method/function so that it converts dash/underscore 
# delimited words into camel casing. The first word within the output 
# should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).
#  The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

from re import sub
def to_camel_case(s):
    if s!='':
        s1 = sub(r"(_|-)+", "", s).title().replace(" ","")
        if s[0].islower()==True:
            s1 =''.join([s1[0].lower(), s1[1:]])
    else:
        s1=''
    return s1
to_camel_case('easdafad-sdf')

######## Mejor Forma #####

#def to_camel_case(text):
#    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

#def to_camel_case(text):
#    removed = text.replace('-', ' ').replace('_', ' ').split()
#    if len(removed) == 0:
#        return ''
#   return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])