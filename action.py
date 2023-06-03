import tkinter as tk
from tkinter import messagebox
import sys
import os
import threading
from github import Github
from steamjia import steamjia
from creat import crea
from get import gett
import all


#      , verify=False  别忘了关掉 (跳过SSH访问)

# act类创建登录菜单
class act(object):
    def __init__(self):
        all._init()
        self.win = tk.Tk()
        self.win.title("登录")
        self.win.geometry('400x200+600+350')
        self.win.protocol("WM_DELETE_WINDOW", self.JieShu)

        # 创建两个列表用于账号和密码的比对
        self.z = []
        self.m = []

        # 将俩个标签分别布置在第一行、第二行
        tk.Label(self.win, text="账号：").grid(row=0)
        tk.Label(self.win, text="密码：").grid(row=1)
        chaung = tk.Button(self.win, text='创建账户', command=self.happy)
        chaung.place(x=340, y=140, width=50, height=50)
        zhaohui = tk.Button(self.win, text='找回账号或密码', command=self.zhaohui1)
        zhaohui.place(x=10, y=140, width=100, height=50)

        # 创建输入框控件
        self.e1 = tk.Entry(self.win)
        self.e2 = tk.Entry(self.win, show='*')
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.e2.grid(row=1, column=1, padx=10, pady=5)

        self.password = tk.StringVar()
        self.toggle_btn = tk.Button(self.win, text='显示密码', command=self.Buvis)
        self.toggle_btn.grid(row=2, column=1, padx=10, pady=5)

        # 使用 grid()的函数来布局，并控制按钮的显示位置
        self.a1=tk.Button(self.win, text="登录", width=10, command=self.login)
        self.a1.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        tk.Button(self.win, text="退出", width=10, command=self.JieShu).grid(row=3, column=1, sticky="e", padx=10, pady=5)

        #绑定回车盲操
        self.win.bind("<Return>", lambda event: self.a1.invoke())

        # 启用多线程,让读取数据比生成窗口慢，防止由于读取数据导致线程阻塞
        t = threading.Timer(1, self.tok)
        t.start()

        self.win.mainloop()

    # 将云端的所有数据放入本地
    def tok(self):
        # 初始化，如果没有网络则提示
        try:
            token = 'token'

            # 设置仓库信息
            repo_owner = 'owner'
            repo_name = 'name'
            file_path = 'zhanghao.txt'
            file_path2 = 'mima.txt'

            # 创建 Github 对象
            g = Github(token, verify=False)

            # 获取仓库对象
            repo = g.get_repo(f'{repo_owner}/{repo_name}')

            # 获取文件内容
            file = repo.get_contents(file_path)
            file_content = file.decoded_content.decode()

            self.z.extend(file_content.split())  # 存储账号

            # 获取文件内容
            file = repo.get_contents(file_path2)
            file_content = file.decoded_content.decode()

            self.m.extend(file_content.split())  # 存储密码
        except:
            def l():
                python = sys.executable
                os.execl(python, python, *sys.argv)  # 重启程序

            def lm():
                self.JieShu()

            m = tk.Toplevel()
            m.title("连接异常")
            m.geometry('250x120+700+400')
            check_web = tk.Label(m, text="请检测当前网络是否可用", font=10)
            check_web.pack()
            check_ok = tk.Button(m, text="重启程序", command=l)
            check_no = tk.Button(m, text="结束程序", command=lm)
            check_ok.place(x=40, y=65)
            check_no.place(x=140, y=65)

    # 将界面转换成创建账号界面(chuang按钮)
    def happy(self):
        all.zh_cre_qu(self.z)
        self.win.destroy()
        crea()

    # 将界面转为找回账号密码界面(zhaohui按钮)
    def zhaohui1(self):
        all.zh_cre_qu(self.z)
        all.mim_cre_qu(self.m)
        self.win.destroy()
        gett()

    # 账号密码比对
    def login(self):
        a = self.e1.get()  # 得到输入框中账号的数字
        if a in self.z:
            z1 = self.z.index(a)
            b = self.e2.get()
            if b == self.m[z1]:
                all.Know4(a)
                messagebox.showinfo('提示', '欢迎您到来')
                self.win.destroy()
                self.win.quit()
                steamjia()
            else:
                self.e2.delete(0, 'end')
                messagebox.showwarning('警告', '账号或密码错误')
        else:
            self.e2.delete(0, 'end')
            messagebox.showwarning('警告', '账号或密码错误')

    # 在点X时，防止bug，直接结束程序
    def JieShu(self):
        os._exit(0)

    # 显示密码与隐藏密码
    def Buvis(self):
        if self.e2['show'] == '':
            self.e2.config(show='*')
            self.toggle_btn.configure(text='显示密码')
        else:
            self.e2.config(show='')
            self.toggle_btn.configure(text='隐藏密码')


act()
