import os
path = os.getcwd()+'\\new file'
try:
    os.mkdir(path)
except:
    f = open('C:\\Users\\Akash kumar\\Desktop\\python project\\assignment\\new file\\file2.txt','w')
    f = open('C:\\Users\\Akash kumar\\Desktop\\python project\\assignment\\new file\\file2.txt','a')
    f.write('my self akash')
    f.writelines(['\nthis is','\tmy new','\t second sample file'])
    f.close()
    import pyperclip
    print(pyperclip.paste())
    
    
