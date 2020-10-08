data = {}
stringinput = input("Enter Some String:- ")
stringinput = list(stringinput.casefold())

length = len(stringinput)

for i in stringinput:
    data[i] = stringinput.count(i)
sum =0
for individualdata in data:
   sum = sum+data[individualdata]
   print(str(individualdata)+" -> "+str(data[individualdata]))

print("Total  number of characters are ",sum)