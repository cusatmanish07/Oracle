#set start with the curly bracess

set1= {"apple", "banana", "mango"}
print(set1)

#print the member of the set using for loop. 
for x in set1:
 print(x)

set2={1, 2, 3, 4, 5}
for x in set2:
 print(x)  

#check if the member is present in the set or not

print("banana" in set1)
print("apple" in set1)
print("mango" in set1)
print("papya" in set1)
print(6 in set2)
print("6" in set2)
print(5 in set2)
print("5" in set2)
print(1 in set2)

#Add Items
#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.

set1.add("papaya")
print(set1)
set1.add("guava")
for x in set1:
 print(x)


set1.update(["dog", "cat", "rat"])
for x in set1:
 print(x)


#Print the length of the  set 

print(len(set1))

print(len(set2))


#remove Item from set

set1.remove("banana")
for x in set1:
 print(x)

set2.discard(5)

for x in set2:
 print(x)

set2.discard(4)
for x in set2:
 print(x)

#Union create a new set from set 1 and set 2

set3={"sun", "mon", "tue"}
set4={"wed", "thurs", "fri", "sat"}
set5=set3.union(set4)
print(set5)

for x in set5:
 print(x)

#update function to merge to set 

set1.update(set2)
print(set1)
print(set2)

#Clear the all element from set
set1.clear()
print(set1)

#set() as constructor to create a set

set6 = set(("a", "b", "c", "d", "e"))
for x in set6:
 print(x)



