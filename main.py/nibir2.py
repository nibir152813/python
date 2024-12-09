

# for loop over list
"""
 citylist = ['Dhaka','Rangpur','Barishal']
for item in citylist:
    print(item)

 #for loop over string

name = 'antor'
for chr in name:
       print(chr)

# for loop over range

for i in range(12):
    print(i)

#brack

name = 'antor'
for chr in name:
    if chr=="o":
        break
    print(chr)

#continue

name = 'antor'
for chr in name:
    if chr=="o":
        continue
    print(chr)
"""
# while loop over list
"""
furits = ['apple' , 'mango' , 'banana']
index=0
while index < len(furits):
    print(furits [index])
    index +=1

#while loop over string

name = 'nibir'
index=0
while index < len(name):
    print(name [index])
    index +=1

# Range loop

start =0
end =10
while start<end:
    print(start)
    start+=1

furits = ['apple' , 'mango' , 'banana']
index=0
while index < len(furits):
    if(furits[index] =="banana"):
        break
    print(furits [index])
    index +=1

furits = ['apple' , 'mango' , 'banana']
index=0
while index < len(furits):

    if(furits[index] =="mango"):
        continue
    print(furits [index])
    index +=1

# while loop whit Continue

counter=0
while counter <10:
    counter+=1
    if counter % 2 == 0:
        continue
    print(counter)

citylist=['Dhaka','Rangpur','Rajshai','pabna']
print(id(citylist))
citylist.append('sylhet')
print(id(citylist))
print(citylist[0])

#append

citylist=['Dhaka','Rangpur','Rajshai','pabna']
citylist.append('123')
print(citylist)

#insert

citylist=['Dhaka','Rangpur','Rajshai','pabna']
citylist.insert(3,'123')
print(citylist)

#extend

list1 =['Dhaka','Rangpur','Rajshai','pabna']
list2= ['Newyork','londod','Mosco','Torento']
list1.extend(list2)
print(list1)

#Remove

list1 =['Dhaka','Rangpur','Rajshai','pabna']
list1.remove('Rajshai')
print(list1)

#pop

list1 =['Dhaka','Rangpur','Rajshai','pabna']
list1.pop()
print(list1)

#clear

list1 =['Dhaka','Rangpur','Rajshai','pabna']
list1.clear()
print(list1)

#index

list1 =['Dhaka','Rangpur','Rajshai','pabna']
index = list1.index('Rangpur')
print(index)

#count

list1 =['Dhaka','Rangpur','Rajshai','pabna','Rangpur','Rangpur']
countvalue = list1.count('Rangpur')
print(countvalue)

#sort / reverse

numbers = [2,6,8,7,12,9,1,0,11]
numbers.sort()
numbers.reverse()
print(numbers)

# tuples
# tuples in immutable
# Allow Duplicate data

furits = ('apple' , 'mango' , 'banana')
print(id(furits))
furits = ('apple' , 'mango')
print(id(furits))

#count

numbers = (2,3,6,45,4,5,3,4,6,8,8,2,5,6,8)
count=numbers.count(8)
print(count)

#index

city=('dhaka','rajsahi','bogora')
index=city.index('dhaka')
print(index)

# convert tuple to list

citytuple=('dhaka','rajsahi','bogora')
citylist=list(citytuple)
print(citylist)

#set
# unoderlist write by {}
# mutable data type

furits = {'apple' , 'mango' , 'banana'}
print(id(furits))
furits.add('coconat')
print(id(furits))

# not allow doplicata data

furits = {'apple' , 'mango' , 'banana','banana','banana'}
print(id(furits))
furits.add('coconat')
print(id(furits))
print(furits)

#set add

furits = {'apple' , 'mango' , 'banana'}
furits.add("charry")
print(furits)

#set update

furits = {'apple' , 'mango' , 'banana'}
furits.update("A","b","c")
print(furits)

# Remove

furits = {'apple' , 'mango' , 'banana'}
furits.remove("apple")
print(furits)

# clear

furits = {'apple' , 'mango' , 'banana'}
furits.clear()
print(furits)


# Dictionary
# key-value pair data (bf-gf)
# unordered
# bf/key can't duplicate
# gf/value can duplicate


Smuct={
    "huda":"mun",
    "antor":"fatema",
    "kainat":"lamisa ar vai",
    "imran":"shan",
    "jamil":"fatema",
    "asraful":"fatema"
}
print(Smuct)
#print(Smuct[''])


# Lets start practical example
# keys method
# value method
iphone = {
    "name":"iphone",
    "price":212000,
    "rating":2.5,
    "isStock":"true",
    "color":['red','black','white'],

}
#print(iphone.keys())
print(iphone.values())

# update gf/value
Smuct={
    "huda":"mun",
    "antor":"fatema",
    "kainat":"lamisa ar vai",
    "imran":"shan",
    "jamil":"fatema",
    "asraful":"fatema"
}
Smuct.update({ "huda":"sayma"})
print(Smuct)

#clear the smuct

Smuct={
    "huda":"mun",
    "antor":"fatema",
    "kainat":"lamisa ar vai",
    "imran":"shan",
    "jamil":"fatema",
    "asraful":"fatema"
}
Smuct.clear()
print(Smuct)
"""
# search for ""
Smuct={
    "huda":"mun",
    "antor":"fatema",
    "kainat":"lamisa ar vai",
    "imran":"shan",
    "jamil":"fatema",
    "asraful":"fatema"
}
adnan = Smuct.get("kainat",'nai')
print(adnan)