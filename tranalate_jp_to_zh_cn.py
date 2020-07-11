import os 
import sys
current_path=__file__
#当前路径
current_dir=""
to_trans_file_name_list=[]
#要处理的文件列表
files=[]
#只翻译一次
luan_ma="幚峴僼傽僀儖乛DLL"
def one_trans():
    while(True):
        print("欢迎使用,输入0退出循环")
        print("请输入乱码")
        usr_in=input()
        if usr_in=="0":
            break
            print("已经退出单行模式")
        else:
            print("继续运算")
            result_gbk=usr_in.encode("gbk")
            result_jp=result_gbk.decode("shift-jis","strict")
            print("解码结果->"+result_jp)
    init()
        
    
def init():
    global current_dir
    current_dir=os.path.dirname(__file__)
    print("当前路径->"+current_dir)
    print("欢迎使用这个日文乱码工具,目前只支持单行文本翻译模式和批量翻译(批量翻译文件目录不能有乱码文件夹,不然无法解码")
    print("遇到不会使用的问题欢迎联系作者微信13023335265")
    print("请输入模式,\n 0为退出程序\n 1为单行日文文本乱码翻译模式,\n 2为批量文件翻译模式 \n 3是一些说明")
    usr=input()
    if(usr=="1"):
        one_trans()
    if(usr=="2"):
        translate()
    if(usr=="0"):
        print("已经退出程序")
    if(usr=="3"):
        print("此程序原理是先把乱码文件用gbk编码一下,再用shift-jis日语编码来解码")
        print("如果出现报错,证明你文件已经被翻译过了,对于不是乱码的文件 使用编码转换会出错")
        print("输入0来回到上一个菜单")
        a=input()
        if a=="0":
            init()

#翻译乱码文件夹
def translate_dir():
    for file in os.listdir():
        
    pass
#这个不能翻译乱码文件夹
def translate():

    #这个方法不能解码文件夹
    for file in os.listdir(current_dir):
        #print("解码结果->"+str(jp))
        if(os.path.isfile(os.path.join(current_dir,file))):
            gbk=file.encode("gbk")
            jp=gbk.decode("shift-jis")
            #旧目录名 #新目录名 新旧完整文件路径名称
            old_path=os.path.join(current_dir,file)
            new_path=os.path.join(current_dir,jp)
            print("旧路径->"+old_path)
            print("新路径->"+new_path)
            
            os.rename(old_path,new_path)
    print("翻译完成->"+":D")
init()


