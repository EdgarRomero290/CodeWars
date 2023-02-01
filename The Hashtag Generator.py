#DESCRIPTION:
#The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!

#Here's the deal:

#It must start with a hashtag (#).
#All words must have their first letter capitalized.
#If the final result is longer than 140 chars it must return false.
#If the input or the result is an empty string it must return false.
from re import sub
def generate_hashtag(s):
    return False if s=='' or len(s)>140 else ''.join('#'+sub(r"(_|-)+", "", s).title().replace(" ",""))

generate_hashtag('sadk sdasd dfgdfg dd')



