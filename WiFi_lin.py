import tkinter as tk
import all

class WI_LI(object):
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("退出账号")
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
        width = 300  # 设定窗口宽度
        height = 200  # 设定窗口高度
        self.left = (screenWidth - width) / 2
        self.top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, self.left, self.top))

        self.a = tk.Label(self.root, text="您是否确定不保存此次记录直接退出程序")
        self.a.place(x=40, y=50)
        self.b = tk.Button(self.root, text="确定", command=self.good, width=10)
        self.b.place(x=38, y=100)
        self.root.bind("<Return>", lambda event: self.b.invoke())
        self.c = tk.Button(self.root, text="取消", command=self.sad, width=10)
        self.c.place(x=170, y=100)

        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def good(self):
        self.root.destroy()
        self.root.quit()
        all.check_out3()
        all.check_out1(2)


    def sad(self):
        self.root.destroy()
        self.root.quit()

class WI_LI2(WI_LI):
    def __init__(self):
        super(WI_LI2,self).__init__()
    def good(self):
        self.root.destroy()
        self.root.quit()
        all.check_out3()
        all.check_out1(99)


if __name__ == '__main__':
    WI_LI2()