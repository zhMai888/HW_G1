import tkinter as tk
from tkinter import messagebox

import all


class exe1(object):
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("网站地址修改")
        width = 450  # 设定窗口宽度
        height = 200  # 设定窗口高度
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
        self.left = (screenWidth - width) / 2
        self.top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, self.left, self.top))
        self.now = tk.Label(self.root, text="当前路径为:\n%s\n" % (all.get_urlexe()))
        self.now.pack()
        self.a = tk.Label(self.root, text="更改的浏览器exe(要绝对路径):")
        self.a.pack()
        self.b = tk.Entry(self.root, width=60)
        self.b.pack()
        self.que = tk.Button(self.root, width=10, text="确定", command=self.que1)
        self.que.place(x=100, y=120)
        self.root.bind("<Return>", lambda event: self.que.invoke())
        self.xiao = tk.Button(self.root, width=10, text='取消', command=self.xiao1)
        self.xiao.place(x=265, y=120)

        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def que1(self):
        a = self.b.get()
        if a != '':
            import all
            all.urlget(a)
            self.xiao1()
        else:
            messagebox.showwarning("警告", "地址不能为空")
            exe1()

    def xiao1(self):
        self.root.destroy()
        self.root.quit()


if __name__ == "__main__":
    exe1()
