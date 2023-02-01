#DESCRIPTION:
#Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of 
# cells and carries the "instructions" for the development and 
# functioning of living organisms.

#If you want to know more: http://en.wikipedia.org/wiki/DNA#

#In DNA strings, symbols "A" and "T" are complements of each other,
#  as "C" and "G". Your function receives one side of 
# the DNA (string, except for Haskell); 
# you need to return the other complementary side. 
# DNA strand is never empty or there is no DNA at all 
# (again, except for Haskell).

#More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

#Example: (input --> output)
#"ATTGC" --> "TAACG"
#"GTAT" --> "CATA"

def DNA_strand(dna):
    result=''
    coding = {'A': 'T', 'T': 'A','G': 'C', 'C': 'G'}
    for x in dna:
        if x in coding:
            result=result+coding[x]
    return result
DNA_strand("ATTGC")

######## Mejor Forma #####

#import string
#def DNA_strand(dna):
    #return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

#pairs = {'A':'T','T':'A','C':'G','G':'C'}
#def DNA_strand(dna):
    #return ''.join([pairs[x] for x in dna])

#def DNA_strand(dna):
  #return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])    