from PIL import ImageTk
import tkinter as tk
import qrcode


class QRCodeViewer:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("QRcode")
        width = 300  # 设定窗口宽度
        height = 300  # 设定窗口高度
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
        self.left = (screenWidth - width) / 2
        self.top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, self.left, self.top))
        self.photo = None  # 添加一个实例变量，用于保存PhotoImage对象
        self.generate_qr_code()

        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def generate_qr_code(self):
        # 生成二维码图像
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data('https://zhmak4.wordpress.com')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # 将Pillow Image对象转换为Tkinter PhotoImage对象
        image = ImageTk.PhotoImage(img)

        # 保存PhotoImage对象的引用
        self.photo = image

        # 创建画布并显示二维码图像
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.canvas.create_image(150, 150, image=image)






if __name__ == "__main__":
    QRCodeViewer()
