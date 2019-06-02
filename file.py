import os
path = os.getcwd()+'\\new file'
try:
    os.mkdir(path)
except:
    f = open('C:\\Users\\Akash kumar\\Desktop\\python project\\assignment\\new file\\file1.txt','w')
    f = open('C:\\Users\\Akash kumar\\Desktop\\python project\\assignment\\new file\\file1.txt','a')
    f.write('my self akash')
    f.writelines(['\nthis is','\tmy new','\tsample file'])
    f.close()
    f = open('C:\\Users\\Akash kumar\\Desktop\\python project\\assignment\\new file\\file1.txt','r')
    print(f.read())
    
    
    
