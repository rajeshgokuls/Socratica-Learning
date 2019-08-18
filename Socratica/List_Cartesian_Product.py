

A = [1 ,3, 5, 7]

B = [2 , 4, 6, 8]

C = [11, 12, 13, 14]

cartesian_product = [(a,b,c) for a in A for b in B for c in C]


print(cartesian_product)