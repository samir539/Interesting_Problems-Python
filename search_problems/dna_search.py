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
example_Gene: str = 'ACCCGGC'
# print(example_Gene)

def to_gene(input_gene:str) -> Gene:
    '''
    Take input gene in string format and outputs the gene as a variable of the 'Gene' type
    
    Args:
        input_gene (str): the input gene in a string representation
    
    Returns:
        gene (Gene): A list of codons which make up the gene represented in the string 
    '''
for i in example_Gene:
    gene: Gene = []
