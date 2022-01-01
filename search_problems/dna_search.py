from enum import IntEnum
from typing import List, Tuple


#Nucleotide bases represented using IntEnum
nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
print(repr(nucleotide.A))