import tkinter as tk
from tkinter import messagebox

import all


class gett(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("找回账号或密码")
        self.root.geometry('350x170+600+350')
        self.root.protocol("WM_DELETE_WINDOW", self.gohome)
        self.z1 = []  # 存放账号
        self.m1 = []  # 存放密码

        label1 = tk.Label(self.root)  # 占位，为了好看
        label1.pack()
        self.rad1 = tk.Label(self.root, text='用账号找回')
        self.rad1.pack()
        tk.Label(self.root, text="账号")
        self.e1 = tk.Entry(self.root, width=30)
        self.e1.pack()

        self.ma = tk.Button(self.root, text="找回", width=10, command=self.zh1)
        self.ma.place(x=50, y=90)
        self.root.bind("<Return>", lambda event: self.ma.invoke())
        self.mi = tk.Button(self.root, text="取消", width=10, command=self.gohome)
        self.mi.place(x=210, y=90)
        self.root.mainloop()

    def gohome(self):
        self.root.destroy()
        from action import act
        act()

    def zh1(self):
        b = self.e1.get()  # 得到输入账号
        self.z1.extend(all.zh_cre_verify())
        self.m1.extend(all.mim_cre_verify())
        if b in self.z1:
            messagebox.showinfo('找回成功', '密码是:%s' % (self.m1[self.z1.index(b)]))
            self.root.destroy()
            from action import act
            act()
        else:
            messagebox.showwarning('警告', '账号不存在')
            self.e1.delete(0, 'end')


if __name__ == "__main__":
    gett()
