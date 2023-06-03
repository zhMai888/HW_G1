import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import random


class ver_vip():
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("获取VIP")
        width = 400  # 设定窗口宽度
        height = 200  # 设定窗口高度
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
        self.left = (screenWidth - width) / 2
        self.top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, self.left, self.top))
        self.a = tk.Label(self.root, text="QQ邮箱:")
        self.a.place(x=40, y=30)
        self.b = tk.Entry(self.root, width=25)
        self.b.place(x=100, y=30)
        self.c = tk.Label(self.root, text="验证码:")
        self.c.place(x=40, y=80)
        self.d = tk.Entry(self.root, width=25)
        self.d.place(x=100, y=80)
        self.get = tk.Button(self.root, text="获取验证码", command=self.get1)
        self.get.place(x=300, y=25)
        self.que = tk.Button(self.root, width=10, text="确定", command=self.que2)
        self.que.place(x=40, y=140)
        self.root.bind("<Return>", lambda event: self.que.invoke())
        self.xiao = tk.Button(self.root, width=10, text='取消', command=self.xiao2)
        self.xiao.place(x=240, y=140)

        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def countdown(self, seconds):
        if seconds > 0:
            # 更新按钮文本显示剩余秒数
            self.get.config(text=f"    {seconds} 秒    ")
            # 每过一秒递归调用countdown函数
            self.get.after(1000, self.countdown, seconds - 1)
        else:
            # 倒计时结束，启用按钮
            self.enable_button()

    def enable_button(self):
        # 启用按钮，允许点击
        self.get.config(state=tk.NORMAL, text="获取验证码")

    def get1(self):

        # 向邮箱发送验证码
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "user"  # 用户名
        mail_pass = "password"  # 密码、授权码

        sender = 'sender'  # 发送邮箱
        emailadd=self.b.get()
        receivers = [str(emailadd)]  # 接收邮箱

        if emailadd!='':
            if len(emailadd)>=12 and  emailadd[-7:]=='@qq.com':
                try:
                    self.idcode=str(random.randint(10000,100000))

                    sender_name = "name"
                    sender_email = 'email'
                    sender2 = formataddr((Header(sender_name, 'utf-8').encode(), sender_email))

                    # 邮件主题，邮件内容
                    def send_mail(title, message):
                        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
                        message = MIMEText(message, 'plain', 'utf-8')
                        message['From'] = sender2  # 发送者
                        message['To'] = Header('My Dear User', 'utf-8')  # 接收者
                        message['Subject'] = Header(title, 'utf-8')

                        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
                        smtpObj.login(mail_user, mail_pass)
                        smtpObj.sendmail(sender, receivers, message.as_string())

                    send_mail('A Good News For You',
                              "Hello:"+"\n"
                              +"Welcome to zhMak's Favorite!!!"+"\n"
                              +"😊😊😊😊😊😊😊😊"+"\n"
                              +'Your Verification Code Is:'+self.idcode+'\n'+
                              "Thank you for being our valued VIP"+'\n'
                              +'\n'
                              +"Yours,"+"\n"
                              +" zhMak")
                    self.root.grab_set()
                    tk.messagebox.showinfo("提示","已发送邮件")
                    self.root.grab_release()

                    # 禁用按钮，避免重复点击
                    self.get.config(state=tk.DISABLED)

                    # 开始倒计时
                    self.countdown(60)
                except:
                    self.root.grab_set()
                    tk.messagebox.showwarning("警告", "网络中断"+"\n"+"请检测网络")
                    self.root.grab_release()
            else:
                self.root.grab_set()
                tk.messagebox.showwarning("警告","邮箱格式错误")
                self.root.grab_release()
        else:
            self.root.grab_set()
            tk.messagebox.showwarning("警告","邮箱不能为空")
            self.root.grab_release()


    def que2(self):
        if "idcode" in dir(self):
            m = self.d.get()
            if m == self.idcode:
                import all
                all.vvvip1(1)
                self.xiao2()
            else:
                self.root.grab_set()
                tk.messagebox.showinfo("提示", "验证码错误,请重新输入")
                self.root.grab_release()
        else:
            self.root.grab_set()
            tk.messagebox.showwarning("警告","请输入邮箱")
            self.root.grab_release()

    def xiao2(self):
        self.root.destroy()
        self.root.quit()


if __name__ == "__main__":
    ver_vip()
