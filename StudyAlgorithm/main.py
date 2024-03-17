# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Screen():
    def init(self):
        import tkinter as tk
        Screen_root = tk.Tk()
        Screen_root.title("StudyAlgorithm")
        Screen_root.geometry("4000x3000")
        label = tk.Label(Screen_root, text="Hello, Learner!")
        label.pack()  # 将标签添加到主窗口
        # 创建菜单
        menu_bar = tk.Menu(Screen_root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="新建", command=lambda: print("新建文件"))
        file_menu.add_command(label="退出", command=Screen_root.quit)
        menu_bar.add_cascade(label="文件", menu=file_menu)
        Screen_root.config(menu=menu_bar)
        Screen_root.mainloop()
def main():
    # Use a breakpoint in the code line below to debug your script.
    User_Screen = Screen()
    User_Screen.init()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
