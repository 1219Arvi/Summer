def is_Vowel(a):
 for i in ['a' , 'e' , 'i ','o' ,'u']:
   if  a==i :
      print("True")
   else :
      print("False")

def Main(b):

 count=0
 for i in b:
   if i in ['a','e',"i" ,"o" , "u"]:
      count=count+1
 print(count)



a=input("Enter the charector")
b=input("Enter the string")
is_Vowel(a)
Main(b)