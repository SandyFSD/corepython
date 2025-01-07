# def name():
#     print("Sandy")
# name()

# def sum():
#     a=10
#     b=20
#     c=a+b
#     return c  #it is used for return the value otherwise use print function
# print("the sum is:",sum())

# def sum():
#     a=10
#     b=20
#     c=a+b #without return it show the value none
# print("the sum is:",sum())

#With parameter
# def name(sandy):
#     print("SP",sandy)
# name("Selva")

# def sam(purpose):
#     if purpose=="Economy":print("You have money")
#     elif purpose=="Health":print("You have health")
#     elif purpose=="Relief":print("You have relief")
#     else:print("Nothing found")
# sam("Health")
# sam("Relief")
# sam("Safty first")
    
#without parameter and runtime output

# def ram():
#     ans=input("tell ur name:")
#     if ans=="chennai":
#         print("Welcome to chennai.")
#     elif ans=="salem":
#         print("Welcome to salem")
#     else:
#         print("Welcome to TN")
# ram()

#with 2parameter 

# def prompt(qual,ref):
#     if qual=="ug" and ref=="ug":
#         print("you are in the team")
#     elif qual=="diploma" and ref=="tested":
#         print("Test assosiate")
#     else:
#         print("May be nexttime")
# prompt("ug","ug")
# prompt("manager","Hr")
# prompt(qual="diploma",ref="tested")

#funtion with default arguments

# def register(name,location,prefix="Mr/Miss/Mrs"):
#     if location=="salem":
#         print(prefix,name,"has approved in",location)
#     elif location=="chennai":
#         print(prefix,name,"has gone under waiting state since its",location)
#     else:
#         print("Business not approved")
# register("Sandy automobiles","chennai","Mr.")
# register("has been completed","sss")
# register("Zeoleus tech corp","salem")