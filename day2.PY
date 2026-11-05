# Find  outputs (Home  work)
a = 0O6247
print(a) #006247
print(type(a))#class int
print(id(a)) #address of object a
b = 0o6247#6x8power3+2x8power2+4x8power1+7x8power 0
print(id(b))# address of object a
print(b) #006247
c = 3239
print(c)#3239
print(id(c))#adress of object c
print(0o9248)#9x8power3+2x8power2+4x8power1+8x8power0

  # Find  outputs  (Home  work)
a = 0XA7B9
print(a) 10x16power3+7x16power2+11x16power1+9x16power0
print(type(a))#class int
b = 0xBEEF
print(b) #11x16power3+14x16power2+14x16power1+15x16power0
print(0xA7B9)#10x16powr3+7x16power2+11x16power1+9x16power0 
print('A7B9')#A7B9
print(0XBEEF)
print(0XHYD)
print(0xA7G9B)

  # Find outputs (Home  work)
a = 9248
print(a)#9248
print(type(a))#CLASS INT

  #  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) #Rama Raop
print(type(a)) #string
print(id(a))#address of the object string
b = 'Hyd'
print(b)#Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)#Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.

  # Index   demo  program  (Home  work)
a = 'Hyd'
print(How  to  print  'H'  of  object  'a') #print(a[0])
print(How  to  print  'y'  of  object  'a')#print(a[1])
print(How  to  print  'd'  of  object  'a')#print)a[2])
print(a[3])#error
print(How  to  print  'd'  of  object  'a')#print(a[-1])
print(How  to  print  'y'  of  object  'a')#print(a[-2])
print(How  to  print  'H'  of  object  'a')#print(a[-3])
print(a[-4])#error
print(a[0] ==  a[-3])#True
a[2] = 'c'#False
print(25[0])
print('25'[0])
print(True[1])
print('True'[1])

  #  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3)#HydHydHyd
print(a * 2) HydHyd
print(a * 1)Hyd
print(a * 0)#error
print(a * -1)#error
print(25 * 3)#75
print('25' * 3)#252525
print('25' * 4.0)#error
print(3 * 'Hyd')HydHydHyd
print('25' * True)#25


  '''
Tricky  program

Find  outputs  (Home work)
'''
a = 'Hyd'
print(a , id(a))#Hyd ,address of object a
a = a * 3  #  Is  it  valid/Yes
print(a , id(a)) #HydHydHyd ,address of the object a

  # len()  function  (Home  work)
print(len('Hyd'))#3
print(len('Rama Rao')) #8
print(len('9247'))#4
print(len(''))#0
print(len(' ')#1
print(len(689))#Error

  # Find  outputs  (Home  work)
a = """"Hyd"""
print(a) #"Hyd
print(len(a))#4
print(a[0])#"
print("""Hyd"""")#Hyd"
b = """""Hyd"""
print(b)#Hyd""
print(len(b))#5

# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12])#Dayal
print(a[7 : ])#Dayal Sarma
print(a[ : 6])#Sankar
print(a[ : ])  #  a[0 : 18 : 1]  --->  String  from  indexes  0  to  17  in  steps  of  1  i.e. Sankar Dayal Sarma
print(a[:  : ])
print(a[1 : 10 : 2])#akrDy
print(a[0 : : 2])#Sna aa ar
print(a[1 : : 2])
print(a[-5 : -1])#Sarm
print(a[::-1])#amraS layaD raknaS
print(a[-1:-5:-1])a
print(a[ : : -2]) #  a[-1 : -19 : -2]  --->  String  from  indexes  -1  to   -18  in  steps  of  -2   i.e. arSlyDrka
print(a[3 : -3])
print(a[2 : -5])#nasraS
print(a[-1:-5])#ras 
print(a[3 : 3])


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1



      #  Find  outputs  (Home  work)
a =  'A'
print(a[1])
print(a[1:])


      # int()  function  demo  program
print(int(10.8))  #   10
print(int(True))  #  1
print(int(False))#0
print(int('25'))#25
print(int('0075'))#75
print(int(0B11010))#26
print(0B11010)#26
print(int(0O6247))#6x8power3+2x8power2+4x8power1+7x8power0
print(0O6247)
print(int(0XA7B9))#10x16power3+7x16power2+11x16power1+9x16power0
print(0XA7B9)#10x16power3+7x16power2+11x16power1+9x16power0
print(int(3 + 4j))#error
print(int('25.4'))#error
print(int('Ten'))#error


'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer


  # float()  function  demo  program
print(float(25))  #  25.0
print(float(True))#1.0
print(float(False))#0.0
print(float('92'))#92.0
print(float('36.4'))#36.4
print(float('0075'))  #  75.0
print(float(0B1010101))#85.0
print(float(0O6247))6x8power3+2x8power2+4x8power1+7x8power0
print(float(0XA7B9))10x16power3+7x16power2+11x16power1+9x16power0.0
print(float(3 + 4j))#error
print(float('Ten'))#error



'''
float()   function
--------------------
1) What  does  float(x)  do  ?  ---> Converts  object  'x'  to  float



  # complex()  function  demo  program
print(complex(3 , 4))#3+4j
print(complex(0 , 4))#0+4j
print(complex(3))#3+0j
print(complex(3.8 , 4.6))#3.8+4.6j
print(complex(3.8))#3.8+0j
print(complex(3 , 4.5))#3+4.5j
print(complex(True , False))#1+0j
print(complex(True))#1+0j
print(complex(False))#0j
print(complex(True , 4))#1+4j
print(complex('3'))#3+4j
print(complex('3.8'))#3.8+0j
print(complex(3 , '4'))#error
print(complex('3' , 4)) #error 
print(complex('3' , '4')) #error
print(complex('Ten'))#error


  #  bool()  function  demo  program
print(bool(0)) #False
print(bool(10))#True 
print(bool(-25))#True 
print(bool(0.0))#False
print(bool(0.1))  #  True
print(bool(0 + 0j))#false
print(bool(10 + 20j))#True
print(bool(-15j))#True
print(bool('False'))  #  True
print(bool(''))#False
print(bool('Hyd'))#True
print(bool(' '))#False
print(bool('True'))#True



'''
bool()  function
------------------
1) What  does  bool(x)  do  ?  ---> Converts  object  'x'  to  True / False

2) Is  0  True  (or)  False ? ---> False
    What  about  non-zero ?  ---> True

3) Is  ''(i.e.  Empty  string)  True  (or) False ?  ---> False
    What  about  non-empty  string ?  --->	 True

4) When  is  x + yj  treated  as  False ?  ---> When  both  'x'  and  'y'  are  zeroes
     When  is  x + yj  treated  as  True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non-zero
'''

  # str()  function  demo  program
print(str(25))    #  '25'
print(str(10.8))#'10.8'
print(str(3 + 4j))#'3+4j'
print(str(True))"True"
print(str(False))"False"
print(str(None))'None'


'''
str()  function
-----------------
What  does  str(x)  do ?  ---> Converts  object  'x'  to  string
'''
  # oct()  function  demo  program
print(oct(195))  
print(oct(0B10101110010))  1 × 2¹⁰ + 0 × 2⁹ + 1 × 2⁸+ 0 × 2⁷ + 1 × 2⁶ + 1 × 2⁵+ 1 × 2⁴ + 0 × 2³ + 0 × 2²+ 1 × 2¹ + 0 × 2⁰
print(oct(0xA7B9)) #10 × 16³ + 7 × 16² + 11 × 16¹ + 9 × 16⁰







'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number







  # hex()  function  demo  program
print(hex(25))  
print(hex(0B10101111010111)) #2^14 +2^12 + 2^10 +2^9 + 2^8 +2^7 + 2^5 + 2^3 + 2^2 + 2^1
print(hex(0O6247))#6 × 8³ = 3072 +2 × 8² = 128+4 × 8¹ = 32+7 × 8⁰ = 7 








'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number


  # Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))#range
print(a)#10,15,20,25,30,35,40,45
print(*a)#10,15,20,25,30,35,40,45
print(id(a))#address of object a range
print(len(a))#8
print(*a[2 : 7] , sep = ' , ') #20,25,30,35,40
print(*a[ : : -1])#40,35,30,25,20
a[4] = 32
print(a * 2)#error


  #  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')#10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)#0,1,2,3,4
c = range(10 , 1 , -1)
print(*c , sep = '...')#'10''9''8''7''6'5''4''3''2'
d = range(-10 , 0)
print(*d)#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)#
f = range(2 , 2)
print(*f)
g = range(10 , 11 , 0.1)#error
h = range('A' , 'F')#error



  #  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)#10,13,16
a , b , c = r  
print(a , b , c) #10,13,16
r = range(3)   
x , y = r   
p , q  , r , s = r 
a , b , c = *r  
m = r  
print(id(r)) 
print(id(m))