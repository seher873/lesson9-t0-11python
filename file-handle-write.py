#lesson 10
#file handling 
#open a file
with open("my_file.txt","w")as file:
    file.write("mera pehla file hanling program ha!")
    print("file created successfully")
with open("my_file.txt","r")as file:
    contant=file.read()
    print(contant)