from sys import argv

from time import time

from tkinter import *
from tinui.TinUI import TinUI

# 调试用
debug = False

# 初始化 xaml
def init():
    init_xaml = '''<!-- start -->
<!-- 0_start -->
<!-- 0 -->
<!-- openEdit_start -->
<StackPanel Margin="25,40,23,15">
<StackPanel Orientation="Horizontal" HorizontalAlignment="Center">
<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="新建卡片" EventType="打开文件" EventData="Custom.exe|newMycard,0" />
<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="关闭编辑模式" EventType="打开文件" EventData="Custom.exe|closeEdit,0" />
<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="刷新主页" EventType="刷新主页" />
</StackPanel>
</StackPanel>
<!-- openEdit_end -->
<!-- 0_end -->
<!-- 1_start -->
<!-- 1 -->
<!-- closeEdit_start -->
<!-- <StackPanel Margin="25,40,23,15"> -->
<!-- <StackPanel Orientation="Horizontal" HorizontalAlignment="Center"> -->
<!-- <local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="打开编辑模式" EventType="打开文件" EventData="Custom.exe|openEdit,0" /> -->
<!-- <local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="刷新主页" EventType="刷新主页" /> -->
<!-- </StackPanel> -->
<!-- </StackPanel> -->
<!-- closeEdit_end -->
<!-- 1_end -->
<!-- end -->'''
    input('即将初始化 Custom.xaml ，按回车继续（若要取消请直接关闭程序）')
    write_xaml(init_xaml)

# 关闭编辑模式
def closeEdit():
    global lines

    try:
        # 文件编辑
        with open('Custom.xaml', 'r', encoding='utf-8') as xaml:
            lines = xaml.readlines()
            l = 0
            for line in lines:
                if line == f'<!-- openEdit_start -->\n':
                    l_openstart = l
                elif line == f'<!-- openEdit_end -->\n':
                    l_openend = l
                    for i in range(l_openstart + 1, l_openend):
                        lines[i] = f'<!-- {lines[i][:-1]} -->\n'
                elif line == f'<!-- closeEdit_start -->\n':
                    l_closestart = l
                elif line == f'<!-- closeEdit_end -->\n':
                    l_closeend = l
                    for i in range(l_closestart + 1, l_closeend):
                        lines[i] = lines[i][5:-5] + '\n'
                l += 1

    except Exception as e:
        print(e)
        input()

# 打开编辑模式
def openEdit():
    global lines

    try:
        # 文件编辑
        with open('Custom.xaml', 'r', encoding='utf-8') as xaml:
            lines = xaml.readlines()
            l = 0
            for line in lines:
                if line == f'<!-- closeEdit_start -->\n':
                    l_closestart = l
                elif line == f'<!-- closeEdit_end -->\n':
                    l_closeend = l
                    for i in range(l_closestart + 1, l_closeend):
                        lines[i] = f'<!-- {lines[i][:-1]} -->\n'
                elif line == f'<!-- openEdit_start -->\n':
                    l_openstart = l
                elif line == f'<!-- openEdit_end -->\n':
                    l_openend = l
                    for i in range(l_openstart + 1, l_openend):
                        lines[i] = lines[i][5:-5] + '\n'
                l += 1

    except Exception as e:
        print(e)
        input()


def 换行符转换(text):
    '''\\n ---> &#xA;'''
    text = list(text)
    for i in range(len(text)):
        if text[i] == '\n':
            text[i] = '&#xA;'
    return ''.join(text[:-1])

def new_id():
    return str(int(time()*10**6))

# 新建卡片
def newMycard(id, title, swap, win):
    global lines

    newid = new_id()

    try:
        title = 换行符转换(title)
        
        # 文件编辑
        lines = read_xaml()
        l = 0
        for line in lines:
            if line == f'<!-- {id} -->\n':
                lines[l:l+1] = [
                    f'<!-- {newid}_start -->\n',
                    f'<local:MyCard Title="{title}" IsSwaped="{IsSwaped(swap)}" Margin="0,0,0,15" CanSwap="{CanSwap(swap)}">\n',
                        '<StackPanel Margin="25,40,23,15">\n',
                            f'<!-- {newid} -->\n',
                            '<!-- openEdit_start -->\n',
                            '<StackPanel Margin="25,40,23,15">\n',
                                '<StackPanel Orientation="Horizontal" HorizontalAlignment="Center">\n',
                                    f'<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="新建文本" EventType="打开文件" EventData="Custom.exe|newTextBlock,{newid}" />\n',
                                    '<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="刷新主页" EventType="刷新主页" />\n',
                                '</StackPanel>\n',
                            '</StackPanel>\n',
                            '<StackPanel Margin="25,40,23,15">\n',
                                '<StackPanel Orientation="Horizontal" HorizontalAlignment="Center">\n',
                                    f'<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="新建卡片" EventType="打开文件" EventData="Custom.exe|newMycard,{newid}" />\n',
                                    f'<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Red" Text="删除卡片" EventType="打开文件" EventData="Custom.exe|delMycard,{newid}" />\n'
                                    '<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="刷新主页" EventType="刷新主页" />\n',
                                '</StackPanel>\n',
                            '</StackPanel>\n',
                            '<!-- openEdit_end -->\n',
                        '</StackPanel>\n',
                    '</local:MyCard>\n',
                    f'<!-- {newid}_end -->\n',
                    f'<!-- {id} -->\n']
                break
            l += 1
        
    except Exception as e:
        print(e)
        input()

    finally:
        win.destroy()

def win_newMycard(data):
    try:
        win = Tk()

        # 获取屏幕尺寸
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        # 设置窗口的相对大小，设为屏幕尺寸的 30%
        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.3)
        # 设置窗口的位置，使其在屏幕中央
        position_right = int((screen_width - window_width) / 2)
        position_down = int((screen_height - window_height) / 2)
        # 应用设置
        win.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        win.title("卡片属性")

        title_label = Label(win,text="标题：",font=("宋体",20),fg="black")
        title_label.place(relx = 0, rely = 0, relwidth = 0.2, relheight = 0.2)

        title_entry = Text(win,width=50, height=10, font=("宋体",10),fg="black")
        title_entry.place(relx = 0.2, rely = 0, relwidth = 1, relheight = 0.4)

        global swap_list, swap
        swap_list = ['不可折叠', '可折叠，初始折叠', '可折叠，初始展开']
        swap = 0
        swap_label = Label(win, text=swap_list[0], font=("宋体",15), fg="black")
        swap_label.place(relx = 0, rely = 0.4, relwidth = 0.5, relheight = 0.3)

        swap_button = Button(win, text='切换', font=("宋体",20),fg="black", command=lambda:updata_swap(swap_label))
        swap_button.place(relx= 0.51, rely= 0.41, relwidth= 0.48, relheight= 0.28)

        button = Button(win,text="确定",font=("宋体",20),fg="black",command=lambda:newMycard(data.rsplit(',')[1], title_entry.get(1.0,END), swap, win))
        button.place(relx = 0.01, rely = 0.71, relwidth = 0.98, relheight = 0.28)
        
        win.mainloop()
        
    except Exception as e:
        print(e)
        input()

def updata_swap(swap_label):
    global swap
    swap = (swap + 1)%3
    swap_label.config(text=swap_list[swap])

def IsSwaped(swap):
    return [False, True, False][swap]

def CanSwap(swap):
    return [False, True, True][swap]


# 删除卡片
def delMycard(id, win):
    global lines

    try:
        lines = read_xaml()
        l = 0
        for line in lines:
            if line == f'<!-- {id}_start -->\n':
                l_start = l
            elif line == f'<!-- {id}_end -->\n':
                l_end = l
                break
            l += 1
        lines[l_start:l_end+1] = []

    except Exception as e:
        print(e)
        input()

    finally:
        win.destroy()

def win_delMycard(data):
    try:
        win = Tk()

        # 获取屏幕尺寸
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        # 设置窗口的相对大小，设为屏幕尺寸的 30%
        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.3)
        # 设置窗口的位置，使其在屏幕中央
        position_right = int((screen_width - window_width) / 2)
        position_down = int((screen_height - window_height) / 2)
        # 应用设置
        win.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        win.title("删除卡片")

        title_label = Label(win,text="确定删除卡片？",font=("宋体",20),fg="black")
        title_label.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.48)

        title_button = Button(win,text="否",font=("宋体",20),fg="black",command=win.destroy)
        title_button.place(relx = 0.01, rely = 0.51, relwidth = 0.48, relheight = 0.48)

        title_button = Button(win,text="是",font=("宋体",20),fg="red",command=lambda:delMycard(data.rsplit(',')[1], win))
        title_button.place(relx = 0.51, rely = 0.51, relwidth = 0.48, relheight = 0.48)

        win.mainloop()
    except Exception as e:
        print(e)
        input()


# 新建文本
def newTextBlock(id, text, win):
    global lines

    newid = new_id()

    try:
        text = 换行符转换(text)

        # 文件编辑
        lines = read_xaml()
        l = 0
        for line in lines:
            if line == f'<!-- {id} -->\n':
                lines[l:l+1] = [
                    f'<!-- {newid} -->\n',
                    f'<!-- {newid}_start -->\n',
                    '<!-- openEdit_start -->\n',
                    '<StackPanel Margin="25,40,23,15">\n',
                        '<StackPanel Orientation="Horizontal" HorizontalAlignment="Center">\n',
                            f'<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="新建文本" EventType="打开文件" EventData="Custom.exe|newTextBlock,{newid}" />\n',
                            f'<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="新建提示/警告条" EventType="打开文件" EventData="Custom.exe|newMyHint,{newid}" />\n',
                        '</StackPanel>\n',
                        '<StackPanel Orientation="Horizontal" HorizontalAlignment="Center">\n',
                            f'<local:MyButton Margin="0,0,10,15" Width="280" Height="35" Padding="13,0,13,0" ColorType="Red" Text="删除下方文本/提示条/警告条" EventType="打开文件" EventData="Custom.exe|delTextBlockorMyHint,{newid}" />\n'
                            '<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="刷新主页" EventType="刷新主页" />\n',
                        '</StackPanel>\n',
                    '</StackPanel>\n',
                    '<!-- openEdit_end -->\n'
                    f'<TextBlock Margin="0,0,0,4" TextWrapping="Wrap" Text="{text}" />\n',
                    f'<!-- {newid}_end -->\n',
                    f'<!-- {id} -->\n']
                break
            l += 1

    except Exception as e:
        print(e)
        input()
    
    finally:
        win.destroy()

def win_newTextBlock(data):
    try:
        win = Tk()

        # 获取屏幕尺寸
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        # 设置窗口的相对大小，设为屏幕尺寸的 30%
        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.3)
        # 设置窗口的位置，使其在屏幕中央
        position_right = int((screen_width - window_width) / 2)
        position_down = int((screen_height - window_height) / 2)
        # 应用设置
        win.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        win.title("文本属性")

        text_label = Label(win,text="文本内容：",font=("宋体",20),fg="black")
        text_label.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.18)

        text_entry = Text(win,width=50, height=10, font=("宋体",10),fg="black")
        text_entry.place(relx = 0.01, rely = 0.21, relwidth = 0.58, relheight = 0.58)

        text_button = Button(win,text="确定",font=("宋体",20),fg="black",command=lambda:newTextBlock(data.rsplit(',')[1], text_entry.get(1.0,END), win))
        text_button.place(relx = 0.01, rely = 0.81, relwidth = 0.98, relheight = 0.18)

        win.mainloop()
    except Exception as e:
        print(e)
        input()

# 删除文本
def delTextBlock(id, win):
    global lines

    try:
        lines = read_xaml()
        l = 0
        for line in lines:
            if line == f'<!-- {id}_start -->\n':
                l_start = l
            elif line == f'<!-- {id}_end -->\n':
                l_end = l
                break
            l += 1
        lines[l_start:l_end+1] = []

    except Exception as e:
        print(e)
        input()

    finally:
        win.destroy()

def win_delTextBlock(data):
    try:
        win = Tk()

        # 获取屏幕尺寸
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        # 设置窗口的相对大小，设为屏幕尺寸的 30%
        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.3)
        # 设置窗口的位置，使其在屏幕中央
        position_right = int((screen_width - window_width) / 2)
        position_down = int((screen_height - window_height) / 2)
        # 应用设置
        win.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        win.title("删除文本")

        text_label = Label(win,text="确定删除文本？",font=("宋体",20),fg="black")
        text_label.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.48)

        text_button = Button(win,text="否",font=("宋体",20),fg="black",command=win.destroy)
        text_button.place(relx = 0.01, rely = 0.51, relwidth = 0.48, relheight = 0.48)

        text_button = Button(win,text="是",font=("宋体",20),fg="red",command=lambda:delMycard(data.rsplit(',')[1], win))
        text_button.place(relx = 0.51, rely = 0.51, relwidth = 0.48, relheight = 0.48)

        win.mainloop()
    except Exception as e:
        print(e)
        input()


# 新建提示/警告条
def newMyHint(id, text, is_warn, win):
    global lines

    newid = new_id()

    try:
        text = 换行符转换(text)

        # 文件编辑
        lines = read_xaml()
        l = 0
        for line in lines:
            if line == f'<!-- {id} -->\n':
                lines[l:l+1] = [
                    f'<!-- {newid} -->\n',
                    f'<!-- {newid}_start -->\n',
                    '<!-- openEdit_start -->\n',
                    '<StackPanel Margin="25,40,23,15">\n',
                        '<StackPanel Orientation="Horizontal" HorizontalAlignment="Center">\n',
                            f'<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="新建文本" EventType="打开文件" EventData="Custom.exe|newTextBlock,{newid}" />\n',
                            f'<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="新建提示/警告条" EventType="打开文件" EventData="Custom.exe|newMyHint,{newid}" />\n',
                        '</StackPanel>\n',
                        '<StackPanel Orientation="Horizontal" HorizontalAlignment="Center">\n',
                            f'<local:MyButton Margin="0,0,10,15" Width="280" Height="35" Padding="13,0,13,0" ColorType="Red" Text="删除下方文本/提示条/警告条" EventType="打开文件" EventData="Custom.exe|delTextBlockorMyHint,{newid}" />\n'
                            '<local:MyButton Margin="0,0,10,15" Width="140" Height="35" Padding="13,0,13,0" ColorType="Highlight" Text="刷新主页" EventType="刷新主页" />\n',
                        '</StackPanel>\n',
                    '</StackPanel>\n',
                    '<!-- openEdit_end -->\n'
                    f'<local:MyHint Margin="0,8,0,2" IsWarn="{is_warn}" Text="{text}" />\n',
                    f'<!-- {newid}_end -->\n',
                    f'<!-- {id} -->\n']
                break
            l += 1

    except Exception as e:
        print(e)
        input()
    
    finally:
        win.destroy()

def win_newM(data):
    try:
        win = Tk()

        # 获取屏幕尺寸
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        # 设置窗口的相对大小，设为屏幕尺寸的 30%
        window_width = int(screen_width * 0.3)
        window_height = int(screen_height * 0.3)
        # 设置窗口的位置，使其在屏幕中央
        position_right = int((screen_width - window_width) / 2)
        position_down = int((screen_height - window_height) / 2)
        # 应用设置
        win.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

        win.title("新建文本")

        text_label = Label(win,text="文本内容：",font=("宋体",10),fg="black")
        text_label.place(relx = 0, rely = 0, relwidth = 0.2, relheight = 0.2)

        text_entry = Text(win,width=50, height=10, font=("宋体",10),fg="black")
        text_entry.place(relx = 0.2, rely = 0, relwidth = 0.6, relheight = 0.6)

        text_button = Button(win,text="确定",font=("宋体",10),fg="black",command=lambda:newTextBlock(data.rsplit(',')[1], text_entry.get(1.0,END), win))
        text_button.place(relx = 0.8, rely = 0, relwidth = 0.2, relheight = 0.2)

        win.mainloop()
    except Exception as e:
        print(e)
        input()



# 读取 xaml 文件
def read_xaml():
    '''直接 return readlines 的值'''
    try:
        with open('Custom.xaml', 'r', encoding='utf-8') as xaml:
            return xaml.readlines()
    except Exception as e:
        print(e)
        input()
    finally:
        if xaml:
            xaml.close()


# 写入 xaml 文件
def write_xaml(text):
    try:
        with open('Custom.xaml', 'w+', encoding='utf-8') as xaml:
            xaml.write(text)
    except Exception as e:
        print(e)
        input()
    finally:
        if xaml:
            xaml.close()


if __name__ == '__main__':
    # 检查参数
    if argv[1:]:
        # 保存输入的参数
        data = argv[1:][0]

        # 关闭编辑模式
        if data.rsplit(',')[0] == 'closeEdit':
            closeEdit()

        # 打开编辑模式
        elif data.rsplit(',')[0] == 'openEdit':
            openEdit()

        # 新建卡片
        elif data.rsplit(',')[0] == 'newMycard':
            win_newMycard(data)
            
        # 删除卡片
        elif data.rsplit(',')[0] == 'delMycard':
            win_delMycard(data)

        # 新建文本
        elif data.rsplit(',')[0] == 'newTextBlock':
            win_newTextBlock(data)

        # 删除文本
        elif data.rsplit(',')[0] == 'delTextBlock':
            win_delTextBlock(data)

        # 最后写入 xaml 文件，这样用户在直接关闭属性编辑的 UI 界面后也不会丢失原有配置
        write_xaml(''.join(lines))

    # 初始化 Custom.xaml
    else:
        init()

    if debug:
        input('end')
