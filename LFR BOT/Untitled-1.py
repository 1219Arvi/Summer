file=open("Story.txt" , "r")
cont=file.read()
stri=""
for i in cont:
    if i.islower==True:
        a=i.capitalize()
        stri=stri+a
     
    else:
        stri+stri+i
        
file2=open("New.txt" , "w+")
file2.write(stri)
print(stri)

