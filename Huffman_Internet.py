# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 23:20:02 2022

@author: juans
"""

# Huffman Coding in python
import math

string= 'aaaaaabbbbbbbbccccd'
#string = 'aaaabbcd' #con este huffman llega al limite
#string = '       aaaaeeeefffhhiimmnnssttloprux'
#string='aaaaaaaabbbbbbbbccccddddeeff'


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq={'A':5000,'B':2500,'C':1250,'D':625,'E':375,'F':250}
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)


nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))

#Calcular la cantida de simbolos para saber el total que hay 
total=0
for symbol in freq:
    total+=symbol[1]


#Calcula la entropia de la fuente
Entropy = 0
L_av = 0
for symbol in freq:
    P=symbol[1]/total #Calcula la probabilidad de cada simbolo
    #print("Para",symbol[0],"probabilidad es",P)
    Entropy+=P*math.log2(1/P)
    L_av+=len(huffmanCode[symbol[0]])*P
print("Longitud promedio huffman: ",L_av)
print("Source Entropy: ",Entropy)
