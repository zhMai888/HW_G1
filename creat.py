import tkinter as tk
from tkinter import messagebox
from github import Github
import all


# 创建菜单
class crea(object):
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("创建账号")
        self.win.geometry('400x200+600+350')
        self.win.protocol("WM_DELETE_WINDOW", self.happy)

        # 将俩个标签分别布置在第一行、第二行
        tk.Label(self.win, text="账号：").grid(row=0)
        tk.Label(self.win, text="密码：").grid(row=1)

        # 创建输入框控件
        self.e1 = tk.Entry(self.win)
        self.e2 = tk.Entry(self.win)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.e2.grid(row=1, column=1, padx=10, pady=5)

        # 使用 grid()的函数来布局，并控制按钮的显示位置
        self.c12=tk.Button(self.win, text="创建", width=10, command=self.zhanghao2)
        self.c12.grid(row=3, column=0, sticky="w", padx=10,pady=5)
        self.win.bind("<Return>", lambda event: self.c12.invoke())
        tk.Button(self.win, text="取消", width=10, command=self.happy).grid(row=3, column=1, sticky="e", padx=10, pady=5)

        # 检测账号是否被注册过
        self.zh_check = []

        self.win.mainloop()

    # 得到输入的数字，并将账号和密码分别存入两个文件中
    def chunru(self):
        a = self.e1.get()
        b = self.e2.get()

        # 将账号传到github上，进行云端储存
        token = 'token'

        # 设置仓库信息
        repo_owner = 'owner'
        repo_name = 'name'
        file_path = 'zhanghao.txt'

        # 设置要添加的字符串
        content = a + '\n'  # 换行符便于日后读取数据

        # 创建 Github 对象
        g = Github(token, verify=False)

        # 获取仓库对象
        repo = g.get_repo(f'{repo_owner}/{repo_name}')

        # 读取文件内容
        file = repo.get_contents(file_path)
        file_content = file.decoded_content.decode()

        # 更新文件内容
        new_content = file_content + content
        repo.update_file(file_path, message='Update file via PyGithub', content=new_content, sha=file.sha)

        repo_owner = 'owner'
        repo_name = 'name'
        file_path = 'mima.txt'

        # 设置要添加的字符串
        content = b + '\n'  # 换行符便于日后读取数据

        # 创建 Github 对象
        g = Github(token, verify=False)

        # 获取仓库对象
        repo = g.get_repo(f'{repo_owner}/{repo_name}')

        # 读取文件内容
        file = repo.get_contents(file_path)
        file_content = file.decoded_content.decode()

        # 更新文件内容
        new_content = file_content + content
        repo.update_file(file_path, message='Update file via PyGithub', content=new_content, sha=file.sha)

        # 创建该账号的独属txt文件
        token = 'token'
        repo_owner = 'owner'
        repo_name = 'name'

        # 创建 Github 对象
        g = Github(token, verify=False)

        # 获取仓库对象
        repo = g.get_repo(f'{repo_owner}/{repo_name}')

        # 设置新文件的路径和名称
        new_file_path = f'{a}.txt'

        file_content2='0'+'\n'+"None"+'\n'+'\n'+'\n'

        # 创建新文件
        repo.create_file(new_file_path, "commit message", file_content2)

    # 创建成功后销毁窗口并回到登录界面
    def login(self):
        self.chunru()
        messagebox.showinfo('提示', '创建成功')
        self.win.destroy()
        from action import act
        act()

    # 取消创建或点X时直接销毁窗口，回到登陆界面
    def happy(self):
        self.win.destroy()
        from action import act
        act()

    # 密码的创建条件
    def mima2(self):
        qw = self.e2.get()
        if len(qw) <= 8:
            messagebox.showinfo('提示', '密码必须要有大小写和数字且位数大于8位')
            self.e2.delete(0, 'end')
        else:
            d = 0
            u = 0
            o = 0
            for i in qw:
                if i.islower():
                    o += 1
                if i.isupper():
                    u += 1
                if i.isdigit():
                    d += 1
            if o != 0 and u != 0 and d != 0:
                self.login()
            else:
                messagebox.showinfo('提示', '密码必须要有大小写和数字且位数大于8位')
                self.e2.delete(0, 'end')

    # 账号创建条件
    def zhanghao2(self):
        zh = self.e1.get()

        self.zh_check.extend(all.zh_cre_verify())

        for i in zh:
            if '\u4e00' <= i <= '\u9fff':
                messagebox.showinfo("提示", "账号不能包含中文字符")
                self.e1.delete(0, 'end')
                break
        else:
            check1 = self.zh_check.count(zh)
            if check1 == 0:
                self.mima2()
            else:
                messagebox.showinfo("提示", "账号已存在")
                self.e1.delete(0, 'end')


if __name__ == "__main__":
    crea()
