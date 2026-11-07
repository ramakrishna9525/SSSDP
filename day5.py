SSDP DAY 3

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)# = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)# 25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25
print(type(a))#List
print(id(a))# address of the elements a
print(len(a))#8
a[2] = 'Sec'
print(a)# [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])# ['Sec' , True , 3 + 4j , None]



# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)#Empty list
a . append(25)#[25]
a . append(10.8)#[25,10.8]
a . append('Hyd')#[25,10.8,’Hyd’]
a . append(True) )#[25,10.8,’Hyd’,True]
print(a)#[25,10.8,’Hyd’,True]

a . remove('Hyd')#[25,10.8,True]
print(a)# #[25,10.8,True]
a . remove('25')#error because it is a string
print(a)# #[25,10.8,True]


#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a)#  [25 , 10.8 , 'Hyd']
print(id(a))#address of the elements a
print(a * 3)#  [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2) #[25 , 10.8 , 'Hyd'  ,25 , 10.8 , 'Hyd']
print(a * 1)# [25 , 10.8 , 'Hyd']
print(a * 0)#[]
print(a * -1)#[]
print(a * 4.0)#error
a = a * 3 
print(a)# [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(id(a))#address of the elements a
a = [25]
print(a , id(a))#[25] address of the element or object a
print(a * a)#[2525]



# list()  function  demo  program
a = list('Hyd')
print(a)#(‘H’,’y’,’d’)
print(type(a))# class list
print(len(a))#3
b = (10 , 20 , 15 , 18)
print(list(b))#[10,20,25,18]
print(list(range(5)))#[0,1,2,3,4]
print(list(25))#Error


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  ---> Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  ---> No  becoz  list()  function  expects  sequence  only

3) What  does  list(No-args)  do ?  ---> Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''



# Find  outputs
a = [ ]
print(type(a))#Empty list
print(a)#[]
print(len(a))#0
b = list()
print(b)#Empty tuple
print(len(b))#0


# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7])
print(list[ : : ])
print(list[:])  #  list[0 : 8 : 1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])
print(list[ : : 2])
print(list[1 : : 2])
print(list[ : : -2]) #  list[-1 : -9 : -2]  --->  List  from  indexes  -1   to  -8   in  steps  of  -2  i.e. ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])
print(list[1 : 4])
print(list[-4 : -1])
print(list[3 : -3])
print(list[2 : -5])
print(list[-1:-5])
THIS PROBLEM ALREADY SOLVED IN NOTES

#  Find  outputs  (Home  work)
a =  [25]
print(a[1])#eRROR,There is no index 
print(a[1:])#Error

#  Tricky  program
#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a))#  [10 , 20 , 30 , 40 , 50] address of elements a
a[1 : 4] = [60 , 70]
print(a , id(a)) #[10 , 20 , 60, 70 , 50]
a[2: 4] = [100 , 200 ,  300] address of the elements a
print(a , id(a))# #[10 , 20 , 100, 200 , 300]




# List  packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d] 
print(e) #[25,10.8,’Hyd’,True]
print(type(e))#List

# List  unpacking
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d = list
print('a : ' , a)  #a :25
print('b : ' , b) #b:10.8
print('c : ' , c) #c:Hyd
print('d : ' , d) #d:True
x , y , z = *list  #error
x , y , z = list  #error
a , b , c , d , e = list#error

#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x)#x:Hyd
print('y : ' , y)#y:True
for  x  in  list[2 : 7]:
	print(x)#3+4j
                                Hyd
                                 True
                                   None
                                   10.8

#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a)# (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a)# 25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25
print(type(a))#class tuple
print(len(a))#8
print(a[2 : 5])#( ’Hyd' True  3+4j)
print(*a[2 : 5])# Hyd  True  3+4j
a[2] = 'Sec'#Error
a . append('Sec')#error bcoz it is immutable
a . remove('Hyd')#Error it is immutable
a =  10 , 20 , 30
print(a)#(10,20,30,)
print(a * 2)#( 10,20,30,10,20,30)
a = 40 , 50 , 60,
print(a)#(40,50,60,)
print(type(a))#class tuple
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a))#class int
print(type(b))#class tuple
print(type(c))#class int
print(type(d))#class tuple
print(a * 4)#100
print(b * 4)#(25 ,25, 25, 25,)
print(c * 4)#100
print(d * 4)#(25,25,25,25) 



# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a)# H ,y,d
print(type(a))#class tuple
print(len(a))#3
b = [10 , 20 , 15 , 18] 
print(tuple(b))#(10,20,15,18,)
print(tuple(range(5)))#(0,1,2,3,4)
print(tuple(25))#Error


'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  --->  No  becoz  tuple()  function  expects  sequence

3) What  does  tuple(No-args)  do ?  --->  Returns  an  empty  tuple
'''

# Find  outputs (Home  work)
a = ()
print(type(a))#class tuple
print(a)#empty tuple
print(len(a))#0
b = tuple()
print(b)#() or tuple()
print(len(b))#0


# Tricky program
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)# (10 , 20 , 30,)
print(id(a))#address of the elements a
a = a * 2  #  Valid / Invalid#valid
print(a)# (10 , 20 , 30, 10 , 20 , 30,)
print(id(a))#address of the a

# Find  outputs   (Home  work)
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)#(25,10.8,’Hyd’,True,)
print(type(x))#class tuple

# Find  outputs   (Home  work)
tpl = 25 , 10.8 , 'Hyd' , True
a , b , c , d = tpl
print(a)#25,
print(b)#10.8,
print(c)#Hyd,
print(d)True,
p , q , r , s = *tpl#error
x , y , z = tpl#Error
m , n , o , p , r = tpl#error
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(type(a))#class set
print(len(a))#6
print(a[2])#Hyd
print(a[1 : 4])#{10.8,’Hyd’,True}
a[2] = 'Sec'#{25 , 10.8 , 'Sec' , True , 3+4j , None , 25 , 'Hyd'}
print(a * 2)#error
print(a * a)#error

# Tricky  program
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)# = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(len(a))#4
print(type(a))#class set


#  set()  function demo  program
a = set('Rama rAo')#
print(a)#(R,a,m, r,A,o)
print(len(a))#7 or6
print(set([10 , 20 , 15 , 20]))#{10,20,15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) {25,10.8,’Hyd’}
print(set(range(10 , 20 , 3)))#{10,13,16,19}
print(set(25))#error
print(set([25 , 10.8 , [] , 'Hyd'])) #Error


'''
set()  function
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  ---> No  becoz  set()  function  expects  sequence

3) What  does  set(No-args)  do ?  --->  Returns  an  empty  set
'''

# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   {}
d =   set()
print(type(a))#Empty List
print(type(b))#Empty tuple
print(type(c))#Empty dict
print(type(d))#Empty set
print(a)#[]  
print(b)#()
print(c)#{}
print(d)#set()

# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25)#{25}
a . add(10.8)#{25,10.8}
a . add('Hyd')#{25,10.8,’Hyd’}
a . add(True)#{25,10.8,’Hyd’,True}
a . add(None)#{25,10.8,’Hyd’,True,None}
a . add('Hyd')#error due to duplicates
a . add(1)# Error
print(a) )#{25,10.8,’Hyd’,True,None}
print(len(a))#5
a . remove(25)# {10.8,’Hyd’,True,None}
print(a)# {10.8,’Hyd’,True,None}

a . append(100)# {10.8,’Hyd’,True,None,100}
a . add(set())#Error
a . add(())#error
a . add([])#error
print(a)# {10.8,’Hyd’,True,None,100}
a . add({})

# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(a)
print('Iterate  thru  set  with  for  loop')
#for x in a:
      print(a)
#  Find  outputs
print((32 , 40.6 , [39 , 54.8] , 'Hyd')) #Valid
print({(32 , 40.6 , [39 , 54.8] , 'Hyd')})#Invalid because tuple-set--list


# Find  outputs  (Home  work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)#{Hyd  True 25 }
print(len(s))#3
print(type(s)) #class set

# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #{10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) #class dict
print(How  to  print  value  key  10)# a[10]
print(How  to  print  value  key  20)#a[20]
print(How  to  print  value  key  15)#a[15]
print(How  to  print  value  key  18)#a[18]
print(a[19])#error
print(a[0])#eror
print(a['Amar'])#Error
How  to  moify  value  of   key  15  to  'Krishna' #a[15]:’Krishna
How  to  remove  20 :  'Kiran'  from  dict  'a'#del[20] or #del[20]:’Kiran’
How  to  append  25 : 'Vamsi'  to  dict  'a' #error or # a[25] :’Vamsi’
print(a)#  {10 : 'Ramesh' , 15 : 'Krishna' , 18 : 'Sita', 25:’Vamsi}
print(len(a))#3 or 4
print(a * 2)#Error or Duplicates may occur 



# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)# {10 : 'Hyd' , 10 : 'Sec'}
print(len(a))#1 
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)#{ 'R' : 'Red', 'G' : 'Gray' , 'Y' : 'Yellow' , 'B' : 'Black'}
print(len(b))#4

#  Tricky  program
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)#{True:’NO’,Yes:’May be’}
print(len(a))#2


# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)#Error 
c = { { } : 25}#Error
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)# {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(len(d))#1
e = {set() : 10.8}#Error

# Find  outputs
a = {}
print(type(a))# class dict
print(len(a))#0
print(a)#{}
b = dict()
print(type(b))#class dict
print(len(b))#0
print(b)#()

# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
{10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
How  to  print  dictionary  with  print()  function
print('Keys  of  dictionary')
#for x in a.keys():#dict_keys([10,20,15,18]
Print(x)
How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
for x in a.values():##dict_values([‘Ramesh’,’Kiran’,’Amar’,’Sita’])
       print(x)
How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')
#for x in a.values():
  Print(x)
How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
for x ,y in a items():
  print(x,y , sep’…’)
How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
for x in a keys():
  print(x,a[x],sep=’:’
How  to  print  each  key  and  corresponding  value  in  dict  'a'
