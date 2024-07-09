
def func(string):
 file=open('Story.txt' , 'r')
 v=file.read()
 lst=v.split(" ")
 a=0
 for i in lst:
    a=a+1
 print(a)

string=input("Enter the file name")
func(string)