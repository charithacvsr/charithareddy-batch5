### day 6####

'''
# python program a capitalize the first and last character of each
s1=input("enter string")
fst=s1[0].upper()
lst=s1[1].upper()
print(fst+s1[1:len(s1)-1]+lst)

'''
'''

n=128
i = 0
while n!=0:
    rem=n%10
    check+temp % rem
    if check!=0:
        f1=1
     n = n//10
if f1==0:
    print("yes")
else:
    print("no")

'''

'''
 l1=[8,9,0,7]
 l2=[7,6,5,4]
print(l1[0]+l2[0],l1[1]+l2[1])



for val in range(len(l1)):
    print(l1[val]+l2[val]
          13.appened(ans)
print(13)
'''
'''
 -----> set
# characteristics of set
1.) set can be created using{}
2.) The element inside set are not indexed
3.) Does not allow duplicate values
4.) it unordered
5.) heterogenous
6.) mutable or changable

'''
'''

# eg:1
s1={9,9,89,7.76,8+7],(8,7,5),"truck",'e'}
print(s1)

'''

'''
# eg:2
s2={5,8,98,[9,0]}
print(s2) ----> error
'''
'''
#eg:3
min(),max(),len()
'''
'''
# eg
# to add elements inside set

s1={8,78,67,'u'}
s1.add(43)
print(s1)
update()
s1.update([9,0])
print(s1)
#? to delete element inside set
s1={8,78,67,'u'}
pop() # to delete one element randomly
s1.pop()
print(s1)
remove()
s1.remove(78)
print(s1)
discard()
s1.discard(67)
print(s1)
'''
'''
#---> join the sets
s1={9,0,8}
s2={9.90,"card",'t',56}
union() --> to combine 2 sets
s3=s1.union(s2)
print(s3)

'''

'''
#* intersection () ---> to get elements inside set
s1={4,5,6}
s2={5,6,7,8}
print(s1.intersection(s2))
#* difference()
s1={4,5,6}
s2={5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symetric_difference(s2))

'''
'''
# isdisjoint(),issubject(),issuperset
s1={1,2,3,4,5}
s2={3,2,7,8,9}
#! ---> problem1
s1={1,2,3,4,5}
s2={3,2,7,8,9}
for val in s1:
    if val in s2:
        str1="its joint set"
print(str1)
'''
'''
# ----> dictionary

eg:1
d1={1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))
mech_name=["name1","name2","name3"]
mech_age=[23,22,24]
mech_mark=[89,78,60]
mech_email

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7.) key does not allow datatypes,values allow mutable datatypes

'''
'''

d1={1:100,2:200,3:300,4:400}
print(d1[1]) # o/p --->100

#? some common functions
#len(),min,max()
print(min(d1))
print(max(d1))
'''
'''
#? to find min,max based values

print(min(d1.values())
print(max(d1.values())


'''
'''
# to replace a value in dictionary
 d1[2]="mango"
 print(d1)

# get()
 d1 = (d1[90])
 print(type(d1.keys()))
      
      
# to print all the values
print(d1.values())
      
# interating dictionary
for val in d1 :
      print(val)

#! for val in d1.values():# to iterate values alone
      print(val)

to get both key and values
      for key,val in.items():
            print(key,val)
  '''    
'''    
# ! problem:1

n= input()
!** swap elements in string list
 # the original list is:['gfg','is','best','for','geeks']
 # list after performing character swaps:['efg','is','bgst','for','eggks']

 '''
'''
  n=int(input("enter a num of times:"))
  integer=[]
  float_value=[]
  string=[]
   for val in range(n):
       value=eval(input("enter the values:"))
       if type(value)==int:
           integer.appened(value)
        elif type(value)==float:
            float_value.appened(value)
          elif type(value)==string:   
                 string.appened(value)
           else:
               print("pls provide data in int,float,string")
           print(integer)
           print(float_value)
           print(string)
'''

'''
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

 for val in set1:
     if val not in set2:
         set3.add(val)
  for val in set2:
      if val not in set1:
         set3.add(val)


print(set3)
# ! or
c = 0
for val in set1,set2:
    c=c+1
    if c==1:
        for element in val:
            

'''



'''
#!------>  problem3
l1=[1,2,3,4,]# key
l2=["a","b","c","d"] # value

l1=[1,2,3,4,]
l2=["a","b","c","d"] 
d1={}
d1[l1[0]]=l2[0]
print(d1)



'''



























