import tkinter as tk
from verify_vip import ver_vip


class vvip:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("升级成为尊贵的vip用户")
        self.root.geometry('300x200+600+350')

        self.a = tk.Label(self.root, text="成为尊贵的vip用户,\n你可以无限创建按钮，\n不再因为只能生成15个按钮而难受,\n心动不如行动,赶快升级吧！")
        self.a.place(x=55, y=0)
        self.b = tk.Button(self.root, text="升级", command=self.good, width=10)
        self.b.place(x=38, y=100)
        self.c = tk.Button(self.root, text="下次一定", command=self.sad, width=10)
        self.c.place(x=170, y=100)

        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def good(self):
        self.root.destroy()
        self.root.quit()
        ver_vip()

    def sad(self):
        self.root.destroy()
        self.root.quit()

if __name__ == '__main__':
    vvip()
