# f = open("Hello") #pass name or path
# text = f.read()
# f.close()
# print(text)

#more advanced
#
# with open("Hello") as fobj:
#
#     bio = fobj.read()
#
# print(bio)

#
# try:
#     with open("BOSTON") as f:
#         text = f.read()
# except FileNotFoundError:
#        text = None
#
# print(text)

#write
# oceans = ["PACIFIC", "ATLANTIC", "INDIAN", "SOUTHERN",
#           "ARTIC"]
#
# with open("Oceans.txt", "w") as f:
#     for ocean in oceans:
#         f.write(ocean)
#         f.write("\n")
#     print(oceans)

#APPEND AT THE END


with open("Oceans.txt", "a") as f:
    print(23*"=", file =f)
    print("These are the 5 oceans", file=f)






