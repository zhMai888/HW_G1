import tkinter as tk
import all


# 更改按钮用处与文本的页面
class cur(object):
    def __init__(self):
        all._init()
        self.root = tk.Toplevel()
        self.root.title("更改")
        self.root.geometry('400x200+600+350')

        # choose the open way(web/local)
        self.val = tk.IntVar()
        self.val.set(1)

        self.rad1 = tk.Radiobutton(self.root, text='网站url', variable=self.val, value=1)
        self.rad1.place(x=290, y=20)

        self.rad2 = tk.Radiobutton(self.root, text='本地地址', variable=self.val, value=2)
        self.rad2.place(x=290, y=50)

        tk.Label(self.root, text="名字：").grid(row=0)
        tk.Label(self.root, text="Add：").grid(row=1)
        self.e1 = tk.Entry(self.root)
        self.e2 = tk.Entry(self.root)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.e2.grid(row=1, column=1, padx=10, pady=5)
        self.b1 = tk.Button(self.root, text="更改", width=10, command=self.JieShu)
        self.b1.grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.root.bind("<Return>", lambda event: self.b1.invoke())
        tk.Button(self.root, text="取消", width=10, command=self.root.destroy).grid(row=3, column=1, sticky="e", padx=10,
                                                                                  pady=5)
        self.shan1 = tk.Button(self.root, text='删除按钮', width=10, height=3, command=self.shan0)
        self.shan1.grid(row=4, column=3, padx=20, pady=10)

        # 直接销毁当前界面，防止bug
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.root.attributes("-topmost", True)
        self.root.mainloop()

    # 获得名字，存入全局列表中
    def ge(self):
        self.a = self.e1.get()
        all.set_value(self.a)
        self.ge2()

    # 销毁窗口，分开防止gai1函数读取不到列表内容
    def JieShu(self):
        self.ge()
        self.ge2()
        self.over()

    # 更改按钮
    def over(self):
        all.set_over1(100)
        all.set_url_loc(str(self.val.get()))
        self.root.destroy()
        self.root.quit()

    # url获取
    def ge2(self):
        self.b = self.e2.get()
        all.set_value2(self.b)
        if all.len1() > 1:
            all.shan2()

    # 删除按钮程序
    def shan0(self):
        all.set_shan01(200)
        self.root.destroy()
        self.root.quit()


if __name__ == "__main__":
    cur()
