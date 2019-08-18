# # doing without list comprehension
#
# squares = []
#
# for i in range(1, 101):
#
#     squares.append(i**2) #exponent, squares is done using double squares in python
# #print(squares)
#
#
# #Print remainders when dividing first 100 numbers by 5
#
# remainders5 = [x**2 % 5 for x in range(1,101)]
#
# #print(remainders5)
#
# remainders11 = [x**2 % 11 for x in range(1,101)]
#
# print(remainders11)



v = [2, -3, 1]

w = [ 4*x for x in v]

print(w)