import os
dir=os.path.dirname(__file__)
print(dir)


write_dir=os.path.join(dir+"/","test/","test.txt")

print(write_dir)
a=os.path.exists(write_dir)
print("是否存在->"+str(a))
if not a:
    print(os.getcwd())
    os.mkdir(os.path.join(dir,"test"))
    pass