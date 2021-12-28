a = 1 << 2
b = a | 0b11
# print(a)
# print(b)
# print(4 & 0b11)
# mystr = 101011101011
# newstr = mystr >> 2
# print(newstr)
# # print(6 & 0b11)
# for i in range(0,16):
#     print(bin(i))
ym = 10101010
new = ym >> 8 & 0b11
# print(new)
# print(ym.bit_length())
# bit_string = 1001
# print(0 & 0b11)
# print(bin(0 & 0b11))
# print(bin(bit_string >> 0 & 0b11))
# print(bin(bit_string >> 0))
# print(bit_string >> 0)
# print(bit_string >> 0 & 0b11)
# print(bit_string.bit_length())
# print(bin(bit_string))

def _compress(gene: str) -> int:
        bit_string: int = 1
        for nucleotide in gene.upper():
            bit_string <<=2
            if nucleotide == "A":
                bit_string |= 0b00             
            if nucleotide == "C":
                bit_string |= 0b01
            if nucleotide == "G":
                bit_string |= 0b10
            if nucleotide == "T":
                bit_string |= 0b11
        return bit_string

a =_compress("ACAAA")
print(a)
print(a.bit_length())
print(bin(a))
print("-------------------------")
gene: str = ""
for i in range(0, a.bit_length()-1, 2):
    print (i)
    
    bits: int = a >> i & 0b11
    # print (bin(bits))
    if bits == 0b00:
        gene += "A"
    elif bits == 0b01:
        gene += "C"
    elif bits == 0b10:
        gene += "G"
    elif bits == 0b11:
        gene += "T"

print(gene)
print (gene[::-1])
# print(bit_string.bit_length())
#1010111010
# i = 2
# z = mystr >> i & 0b11
# # print (z)
# for i in range(0,16,2):
#     interst = i & 0b11
#     print (interst)

# for i in range(0,12, 2):
#     bits = mystr >> i & 0b11
#     # print (i)
#     print (bits)
# # print(8 & 0b11)