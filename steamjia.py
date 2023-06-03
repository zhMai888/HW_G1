import tkinter
import tkinter.messagebox
from github import Github
import sys
import os
import re
from churl import cur
import all


# 主程序页面
class steamjia(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('收藏夹')
        self.root.minsize(1000, 650)
        self.root.maxsize(1000, 650)
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
        width = 1000  # 设定窗口宽度
        height = 650  # 设定窗口高度
        self.left = (screenWidth - width) / 2
        self.top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, self.left, self.top))

        self.canvas = tkinter.Canvas(self.root)
        self.canvas.pack(side='left', fill='both', expand=True)
        self.scrollbar = tkinter.Scrollbar(self.root, command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<MouseWheel>', self.on_mousewheel)

        # create a frame to hold the buttons
        self.button_frame = tkinter.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.button_frame, anchor='nw')

        # create the "add" button
        button_plus = tkinter.Button(self.root, cursor='arrow', text='增添按钮', command=self.plus, width=10)
        button_plus.pack(side='top', pady=10)

        # creat open web
        self.button_web = tkinter.Button(self.root, text='更改网站exe', command=self.web1, width=10)
        self.button_web.pack(side='top', pady=10)

        # creat the "vip" button
        self.button_vip = tkinter.Button(self.root, text='升级vip', command=self.ver_VIP, width=10)
        self.button_vip.pack(side='top', pady=10)

        # creat a button to check out the account
        self.button_check_out = tkinter.Button(self.root, text='退出账户', command=self.check_out1, width=10)
        self.button_check_out.pack(side='top', pady=10)

        # 多按钮创建
        self.row1 = 0
        self.column1 = 0
        self.padx1 = 5
        self.pada1 = 5
        self.column_per_row = 2

        # 封面
        self.cover()

        # 按钮
        self.layout()

        # 改变X按钮的用法，将结束进程强制改为结束运行
        self.root.protocol("WM_DELETE_WINDOW", self.JieShu)

        # 存放button
        self.frames = []

        # 存放网站还是本地指令
        self.ur_lo = []

        # 网站地址
        self.exeur = []

        # 存放用户信息
        self.Kname1 = all.know1()  # 存放是哪个账户

        self.button_name = []  # 存放按钮名称
        self.u_name = []  # 存放网站或本地地址名称
        self.u_type = []  # 存放检测是网站地址还是本地地址

        # 存放url
        self.url_dict = {}

        # 确认是否成为vip
        self.vip = 0

        self.shezhi = 0

        try:
            # 初始化账户框架,从GitHub上下载之前的存档
            token = 'token'

            # 设置仓库信息
            repo_owner = 'owner'
            repo_name = 'name'
            file_path = f'{self.Kname1}.txt'

            # 创建 Github 对象
            g = Github(token, verify=False)

            # 获取仓库对象
            repo = g.get_repo(f'{repo_owner}/{repo_name}')

            # 获取文件对象
            file = repo.get_contents(file_path)

            # 读取文件内容并将其转换为列表
            content = file.decoded_content.decode()
            content_list = re.split('[,|\n]', content)

            # 初始化界面

            # 检测是否是vip
            if len(content_list) > 1:
                if content_list[0] == "1":
                    all.vvvip1("1")
                    self.check_value()

                # 放入exe站点
                all.urlget(content_list[1])

                # 初始化按钮个数
                button_num = int((len(content_list) - 2) / 3)  # name & web & select are the same
                self.button_name.extend(content_list[2:button_num + 2])  # name
                self.u_name.extend(content_list[button_num + 2:2 * button_num + 2])  # web
                self.u_type.extend(content_list[2 * button_num + 2:])  # select

                # 初始化所有在云端保存的按钮
                if len(self.button_name)>0:
                    for i in range(button_num):
                        frame = tkinter.Frame(self.button_frame)
                        frame.grid(row=self.row1, column=self.column1, padx=self.padx1, pady=self.pada1)
                        self.frames.append(frame)
                        if self.button_name[i] == "bhdqw2312￥#bdh23123@WE12dqwdqwer234":
                            self.button = tkinter.Button(frame, text="", width=50, height=6,
                                                         command=lambda z=len(self.frames) - 1: self.open_web(z))
                        else:
                            self.button = tkinter.Button(frame, text=self.button_name[i], width=50, height=6,
                                                         command=lambda z=len(self.frames) - 1: self.open_web(z))
                        self.button.grid(row=0, column=0, sticky="w")

                        self.button2 = tkinter.Button(frame, text='更改按钮设置', width=10, height=5,
                                                      command=lambda i=len(self.frames) - 1: self.gai1(i))
                        self.button2.grid(row=0, column=1, sticky='w')

                        sor2 = []
                        for i in self.frames:
                            if i != 0:
                                sor2.append(i)
                        for i, frame in enumerate(sor2):
                            row = self.row1 + i // self.column_per_row
                            column = self.column1 + i % self.column_per_row
                            frame.grid(row=row, column=column, padx=self.padx1, pady=self.pada1)

                        if self.u_type[i] == "Gdasdq12312^234@#1+":
                            self.ur_lo.append(0)
                        else:
                            self.ur_lo.append(self.u_type[i])
                        # update the scroll region of the canvas
                        self.button = frame.grid_slaves()[1]
                        self.url_dict[self.button] = self.u_name[i]
                self.layout()

            self.check2()

            self.check3()

            self.check4()

            self.check5()

            self.root.attributes("-topmost", True)
            self.root.mainloop()
        except:
            tkinter.messagebox.showerror("报错","您似乎断开网络"+"\n"+"请检查好网络后重新登录")
            sys.exit(0)

    # 鼠标滚轮
    def on_mousewheel(self, event):
        # 向上滚动
        if event.delta < 0:
            self.canvas.yview_scroll(1, 'units')
        # 向下滚动
        elif event.delta > 0:
            self.canvas.yview_scroll(-1, 'units')

    # 结束进程
    def JieShu(self):
        try:
            # 隐藏窗口, 为了好看
            self.root.withdraw()
            # 保存账户里的所有信息，并发送到GitHub
            token = 'token'

            # 设置仓库信息
            repo_owner = 'owner'
            repo_name = 'name'
            file_path = f'{self.Kname1}.txt'

            # 设置要上传的字符串列表
            content_list = self.button_name
            content_list2 = self.u_name
            content_list3 = self.u_type

            # 将字符串列表连接成一个字符串
            # 第一个用于上传是否是vip，第二个是网络exe地址，第三个是按钮名字，第四个是按钮索引地址, 第五个是地址是本地还是网站
            if len(self.exeur) > 0:
                if all.vvvip2() >= 1:
                    content = "1" + "\n" + str(self.exeur[0]) + "\n" + ','.join(content_list) + "\n" + ','.join(
                        content_list2) + "\n" + ','.join(content_list3)
                else:
                    content = "0" + "\n" + str(self.exeur[0]) + "\n" + ','.join(content_list) + "\n" + ','.join(
                        content_list2) + "\n" + ','.join(content_list3)
            else:
                if all.vvvip2() >= 1:
                    content = "1" + "\n" + "None" + "\n" + ','.join(content_list) + "\n" + ','.join(
                        content_list2) + "\n" + ','.join(content_list3)
                else:
                    content = "0" + "\n" + "None" + "\n" + ' '.join(content_list) + "\n" + ' '.join(
                        content_list2) + "\n" + ' '.join(content_list3)
            # 创建 Github 对象
            g = Github(token, verify=False)

            # 获取仓库对象
            repo = g.get_repo(f'{repo_owner}/{repo_name}')

            # 读取文件内容
            file = repo.get_contents(file_path)
            file_content = file.decoded_content.decode()

            # 更新文件内容
            repo.update_file(file_path, message='Update file via PyGithub', content=content, sha=file.sha)

            # 停止after,防止因为窗口被销毁还运行after产生的报错
            self.root.after_cancel(self.check2_id)
            self.root.after_cancel(self.check3_id)
            self.root.after_cancel(self.check4_id)
            self.root.after_cancel(self.check5_id)

            # 结束进程
            self.root.destroy()
            self.root.quit()
            os._exit(0)
        except:
            self.root.deiconify()
            tkinter.messagebox.showerror("报错","网络中断"+"\n"+"无法保存此次进度")
            from WiFi_lin import WI_LI
            WI_LI()
    # 一个小小的自我称述
    def cover(self):
        allmenu = tkinter.Menu(self.root)
        allmenu.add_command(label='关于我', command=self.aboutme)
        self.root.config(menu=allmenu)

    # 添加按钮的创建
    def layout(self):
        self.button_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    # 当添加按钮被单击时，创建两个按钮，一个是执行按钮，一个是更改执行按钮用处的按钮
    def plus(self):
        import all
        vip2 = all.vvvip2()
        m = self.frames.count(0)
        if len(self.frames) - m < 15 and vip2 == 0:
            frame = tkinter.Frame(self.button_frame)
            frame.grid(row=self.row1, column=self.column1, padx=self.padx1, pady=self.pada1)
            self.frames.append(frame)

            self.button = tkinter.Button(frame, text="", width=50, height=6,
                                         command=lambda z=len(self.frames) - 1: self.open_web(z))
            self.button.grid(row=0, column=0, sticky="w")

            self.button2 = tkinter.Button(frame, text='更改按钮设置', width=10, height=5,
                                          command=lambda i=len(self.frames) - 1: self.gai1(i))
            self.button2.grid(row=0, column=1, sticky='w')

            sor2 = []
            for i in self.frames:
                if i != 0:
                    sor2.append(i)
            for i, frame in enumerate(sor2):
                row = self.row1 + i // self.column_per_row
                column = self.column1 + i % self.column_per_row
                frame.grid(row=row, column=column, padx=self.padx1, pady=self.pada1)

            self.ur_lo.append("0")
            # update the scroll region of the canvas
            self.layout()
            self.button_name.append("bhdqw2312￥#bdh23123@WE12dqwdqwer234")  # 存入乱码，用于记录存在此按钮但未定义
            self.u_name.append("heru234c83423467123&*^c4ADs")
            self.u_type.append("0")
        elif len(self.frames) - m >= 15 and vip2 == 0:
            tkinter.messagebox.showinfo('提示', '没money,只能创建15个了')
            self.ver_VIP()
        elif vip2 >= 1:
            frame = tkinter.Frame(self.button_frame)
            frame.grid(row=self.row1, column=self.column1, padx=self.padx1, pady=self.pada1)
            self.frames.append(frame)

            self.button = tkinter.Button(frame, text="", width=50, height=6,
                                         command=lambda z=len(self.frames) - 1: self.open_web(z))
            self.button.grid(row=0, column=0, sticky="w")

            self.button2 = tkinter.Button(frame, text='更改按钮设置', width=10, height=5,
                                          command=lambda i=len(self.frames) - 1: self.gai1(i))
            self.button2.grid(row=0, column=1, sticky='w')

            sor2 = []
            for i in self.frames:
                if i != 0:
                    sor2.append(i)
            for i, frame in enumerate(sor2):
                row = self.row1 + i // self.column_per_row
                column = self.column1 + i % self.column_per_row
                frame.grid(row=row, column=column, padx=self.padx1, pady=self.pada1)
            self.ur_lo.append("0")
            # 更新面板&存入空数据
            self.layout()
            self.button_name.append("bhdqw2312￥#bdh23123@WE12dqwdqwer234")
            self.u_name.append("heru234c83423467123&*^c4ADs")
            self.u_type.append("0")

    # 当单击更改按钮时，运行更改界面，并判断是否更改，以及更改执行按钮
    def gai1(self, index):
        frame = self.frames[index]
        self.button = frame.grid_slaves()[1]
        cur()
        # 更改按钮设定
        if all.get_over1() == 100:
            # name
            b = all.get_value()
            self.button.configure(text=str(b))
            self.button_name[index] = str(b)
            all.shan1()
            # add
            url1 = all.get_value2()
            self.url_dict[self.button] = url1

            # 云端保存
            self.ur_lo[index] = all.get_url_loc()
            self.u_name[index] = url1
            self.u_type[index] = self.ur_lo[index]
        self.layout()

        # 删除按钮
        if all.get_shan01() == 200:
            if index <= len(self.frames):
                frame.destroy()
                self.frames[index] = 0
                del self.button_name[index]
                del self.u_name[index]
                del self.u_type[index]

                self.row1 = 0
                self.column1 = 0
                sor2 = []
                for i in self.frames:
                    if i != 0:
                        sor2.append(i)
                for i, frame in enumerate(sor2):
                    row = self.row1 + i // self.column_per_row
                    column = self.column1 + i % self.column_per_row
                    frame.grid(row=row, column=column, padx=self.padx1, pady=self.pada1)

                # 更新canvas的scrollregion
                self.layout()

    def web1(self):
        from edge_exe import exe1
        exe1()

    def open_web(self, index):
        frame = self.frames[index]
        self.button = frame.grid_slaves()[1]
        if self.button in self.url_dict.keys():
            q = self.url_dict[self.button]  # 地址
            m = self.ur_lo[index]
            if m == "1":  # 网站地址存档
                if self.exeur[0] != "None":
                    if os.path.exists(self.exeur[0]):
                        os.system('start "" "' + self.exeur[0] + '" "' + q + '"')
                    else:
                        tkinter.messagebox.showwarning("警告", "该exe地址错误,请重新录入地址")
                else:
                    tkinter.messagebox.showwarning("警告", "没有检测到你的网站exe")
            if m == "2":  # 本地地址存档
                if os.path.exists(q):
                    os.startfile(q)
                else:
                    tkinter.messagebox.showwarning("提示", "该exe地址错误,请重新录入地址")

    def ver_VIP(self):
        from vip import vvip
        vvip()

    def bigvip(self):
        tkinter.messagebox.showinfo('提示', '您已经时尊贵的vip用户,\n不用再升级了')

    def aboutme(self):
        from QRcode import QRCodeViewer
        QRCodeViewer()

    ## vip检查值是否发生了变化
    def check_value(self):
        if all.vvvip2() >= 1:
            # 如果变化了，更新标签的文本
            self.button_vip.destroy()
            self.button_check_out.destroy()
            self.button_vip2 = tkinter.Button(self.root, text='vip', command=self.bigvip, width=10)
            self.button_vip2.pack(side='top', pady=10)

            self.button_check_out = tkinter.Button(self.root, text='退出账户', command=self.check_out1, width=10)
            self.button_check_out.pack(side='top', pady=10)

            self.shezhi = 1

            # 刷新窗口
            self.root.update()

    # vip变化后的更新
    def check2(self):
        if self.shezhi == 0:
            self.check_value()

        # 继续循环
        self.check2_id = self.root.after(100, self.check2)

    # 网站exe变化后的更新
    def check3(self):
        if all.check_urlexe() > 0:
            adr = all.get_urlexe()
            edge_path = str(adr)  # Edge浏览器的路径
            self.exeur.clear()
            self.exeur.append(edge_path)

        # 继续循环
        self.check3_id = self.root.after(100, self.check3)

    # 退出检测
    def check4(self):
        if all.check_home2() > 0:
            all.check_home3()
            try:
                # 保存内容
                token = 'token'

                # 设置仓库信息
                repo_owner = 'owner'
                repo_name = 'name'
                file_path = f'{self.Kname1}.txt'

                # 设置要上传的字符串列表
                content_list = self.button_name
                content_list2 = self.u_name
                content_list3 = self.u_type

                # 将字符串列表连接成一个字符串
                # 第一个用于上传是否是vip，第二个是网络exe地址，第三个是按钮名字，第四个是按钮索引地址, 第五个是地址是本地还是网站
                if len(self.exeur) > 0:
                    if all.vvvip2() >= 1:
                        content = "1" + "\n" + str(self.exeur[0]) + "\n" + ','.join(content_list) + "\n" + ','.join(
                            content_list2) + "\n" + ','.join(content_list3)
                    else:
                        content = "0" + "\n" + str(self.exeur[0]) + "\n" + ','.join(content_list) + "\n" + ','.join(
                            content_list2) + "\n" + ','.join(content_list3)
                else:
                    if all.vvvip2() >= 1:
                        content = "1" + "\n" + "None" + "\n" + ','.join(content_list) + "\n" + ','.join(
                            content_list2) + "\n" + ','.join(content_list3)
                    else:
                        content = "0" + "\n" + "None" + "\n" + ' '.join(content_list) + "\n" + ' '.join(
                            content_list2) + "\n" + ' '.join(content_list3)
                # 创建 Github 对象
                g = Github(token, verify=False)

                # 获取仓库对象
                repo = g.get_repo(f'{repo_owner}/{repo_name}')

                # 读取文件内容
                file = repo.get_contents(file_path)
                file_content = file.decoded_content.decode()

                # 更新文件内容
                repo.update_file(file_path, message='Update file via PyGithub', content=content, sha=file.sha)

                # 停止after,防止因为窗口被销毁还运行after产生的报错
                self.root.after_cancel(self.check2_id)
                self.root.after_cancel(self.check3_id)
                self.root.after_cancel(self.check5_id)

                # 销毁窗口,创建登录窗口
                self.root.destroy()
                self.root.quit()
                from action import act
                act()
            except:
                tkinter.messagebox.showerror("报错","网络中断"+"\n"+"无法保存此次进度")
                from WiFi_lin import WI_LI2
                WI_LI2()

        self.check4_id=self.root.after(100, self.check4)

    # 退出账户
    def check_out1(self):
        from check_back import che_ba
        che_ba()


    def check5(self):
        if all.check_out2()==2:
            all.check_out3()
            self.root.after_cancel(self.check2_id)
            self.root.after_cancel(self.check3_id)
            self.root.after_cancel(self.check4_id)
            self.root.destroy()
            self.root.quit()
            os._exit(0)
        if all.check_out2()==99:
            all.check_out3()
            self.root.after_cancel(self.check2_id)
            self.root.after_cancel(self.check3_id)
            self.root.after_cancel(self.check4_id)
            self.root.destroy()
            # self.root.quit()
            from action import act
            act()

        # 继续循环
        self.check5_id = self.root.after(100, self.check5)


if __name__ == "__main__":
    steamjia()
