import os 
import sys
current_path=__file__
#当前路径
current_dir=os.path.dirname(__file__)
to_trans_file_name_list=[]
#要处理的文件列表
files=[]
#只翻译一次
luan_ma="幚峴僼傽僀儖"
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
    print("请输入模式,\n 0为退出程序\n 1为单行日文文本乱码翻译模式,\n 2为批量文件名乱码翻译模式 \n 3是一些说明 \n 4是批量文件夹翻译模式")
    print("5是批量翻译文件内容模式")
    print("6是使用帮助")
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
    if(usr=="4"):
        print("进入批量乱码文件夹解码模式")
        translate_dir()
    if usr=="5":
        if(not os.path.exists(os.path.join(current_dir,"jp"))):
            os.mkdir(os.path.join(current_dir,"jp"))
        translate_contents_in_files()
    if usr=="6":
        while True:
            os.system("cls")
            print("输入0退出")
            print("帮助 我把每个功能分开写了")
            print("注意如果本身是utf-8的文件,不需要转换,只能转换非utf-8编码文件的内容 不然会报错")
            a=input()
            if a=="0":
                break
        init()
#翻译乱码的文件内容
def translate_contents_in_files():
    for file in os.listdir(current_dir):
        #print(file)
        current_tmp_file_path=os.path.join(current_dir,file)
        print("当前路径->"+current_tmp_file_path)
        if(os.path.isfile(current_tmp_file_path)):
            #排除自身脚本文件
            if(current_tmp_file_path.endswith("jp_to_zh_cn.py")):
                print("---------")
                pass
            else:
                print("-------------排除自身脚本后的代码--------------")
                current_tmp_file=open(current_tmp_file_path,"r",1024,"utf-8")
                tmp_text=current_tmp_file.read()
                #print("文件内容->"+tmp_text)
                gbk=tmp_text.encode("gbk","ignore")
                #print("gbk->"+str(gbk))
                jp=gbk.decode("shift-jis","ignore")
                print("jp->"+jp)
                current_tmp_file.close()
                #注意少了/会路径出错
                new_path=os.path.join(current_dir+"/","jp/",file)
                print("新路径"+new_path)
                new_file=open(new_path,"w+")
                new_file.write(jp)
                new_file.close()
                
    pass
#翻译乱码文件夹
def translate_dir():
    print("如果出现权限问题的报错 那么应该就是网吧系统的问题了")
    #-------以下是批量翻译乱码文件夹代码--正式开始编写-------------------
    for file in os.listdir(current_dir):
        if(os.path.isdir(os.path.join(current_dir,file))):
            #通过判断 现在的file变量应该为文件夹 不然就是我写错了
            print("file变量的值"+str(file))
            gbk=file.encode("gbk")
            jp=gbk.decode("shift-jis")
            print("解码结果"+str(jp))
            old_path=os.path.join(current_dir,file)
            new_path=os.path.join(current_dir,jp)
            os.rename(old_path,new_path)
            print("脚本运行完毕 快去查看解码结果吧-------")
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


