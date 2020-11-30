import os
import math

size_of_og = os.path.getsize('NEO_SYNTAGMA_AB.txt') *8
print('Size of NEO_SYNTAGMA_AB in bits = ', size_of_og)

size_of_SF = os.path.getsize('S_F_2019070_2019235.txt')
print('Size of Shannon Fano coded message in bits = ',size_of_SF)

size_of_Huff = os.path.getsize('Huff_2019070_2019235.txt')
print('Size of Huffman coded message in bits = ',size_of_Huff)

SF_ratio = (size_of_SF/size_of_og) *100
Huff_ratio = (size_of_Huff/size_of_og) *100

print('The compression ratio is \nShannon-Fano:',SF_ratio,'%\nHuffman:',Huff_ratio,'%')