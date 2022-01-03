from enum import IntEnum
from typing import List, Tuple


#Nucleotide bases represented using IntEnum
nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
print(repr(nucleotide.A))

#Representing a Codon and Gene TYPING ALIAS
Codon = Tuple[nucleotide, nucleotide, nucleotide]
Gene = List[Codon]

print(type(Gene))
## Input of gene is a string of letters
example_Gene: str = 'ACCCGG'
# print(example_Gene)

def to_gene(input_gene:str) -> Gene:
    '''
    Take input gene in string format and outputs the gene as a variable of the 'Gene' type
    
    Args:
        input_gene (str): the input gene in a string representation
    
    Returns:
        gene (Gene): A list of codons which make up the gene represented in the string 
    '''
    gene: Gene = []
    for i in range(0, len(input_gene),3):        
        if(i +2 >= len(input_gene)):
            return gene
        codon: Codon = [nucleotide[input_gene[i]], nucleotide[input_gene[i+1]], nucleotide[input_gene[i+2]]]
        gene.append(codon)
    return gene
        

# 
        
            
        
