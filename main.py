import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import filedialog as fdl
import easygui as eg
import time
import random as rd

def get_h_w():
    try: #input data ,if user want to exit, it will make an error isn't ValueError
        weight,high = eg.multenterbox("Enter Data","Enter the basic data of your form",["Width","Height"])
        print(weight,high)
        weight = int(weight)
        high = int(high)
        return high,weight
    except ValueError:
        return -1,-1
    except:
        return "e","e" #when user want to exit instead of type a correct number


def startbutton():
    with open("./start.txt","rt") as f:
        txt = "My form "+version+"\n"+"\n".join(list(f.readlines())[0:12]) + "\n...\nSee more information in \"start.txt\"\n\nHappy using!"

    msgbox.showinfo(title = "Start",message=txt)

def caress_creator():
    saylst = ["Thank you for caressing me !! My cute user!",
              "Emm...My fur is really soft,right?",
              "As you know, software building is a kind of art...",
              "How beautiful the world is!",
              "When you are sad, think about the people who love you...",
              "Remember, Nothing is impossible if you try it hard."]
    msgbox.showinfo(title="Creator's Psychological Virtual Machine",message=rd.choice(saylst))

def form_to_str():
    global mainlist
    res = ""
    res += "{"

    for j in mainlist:
        res += "{"
        for i in j:
            #print(i.get())
            if ("{" not in i.get() ) and ("}" not in i.get() ) and ("," not in i.get() ) and ("/" not in i.get() ) and (i.get() != ""):
                res += i.get()
                print(3)
            elif(i.get() == "" or i.get() == None):
                res += "/n"
                print(2)
            else:
                tmp = ""
                for a in i.get():
                    if (a == "{" or a == "}" or a == "," or a == "/"):
                        tmp += "/" + a
                    else:
                        tmp += a
                res += tmp
                print(1)

            if(i != j[-1]):
                res+=','
        res += "}"

        if j != mainlist[-1]:
            res += ","
    res += "}"

    print(res)

    return res

def str_to_list(s):
    s = s[2:-2]

    rs = s.split('},{')
    '''
    not_add = False
    bki = 0
    i = 0
    while i < len(s):
        if s[i] == "{":
            not_add = True
            bki = i+1-1
        elif s[i] == "}":
            not_add = False
        elif s[i] == "/":
            i += 1
        if s[i] == "," and not_add == False :
            rs.append(s[bki+1:i-1])
        i += 1
    print(rs)
    '''
    s = []
    print(rs)
    '''
    for i in range(len(rs)):
        s.append([])
        for j in rs[i].split(","):
            if ("/," not in j and "//" not in j and "/{" not in j and "/}" not in j and j != "/n"):
                s[i].append(j)
            elif(j == '/n'):
                s[i].append("")
            else:
                tmp = ""
                #for a in range(len(j)):
                a = 0
                while a < len(j):
                    if(j[a] == "/"):
                        tmp += j[a+1]
                        a+=1
                    else:
                        tmp += a
                    a+=1
                s[i].append(tmp)
    '''
    
    for i in range(len(rs)):
        s.append([''])
        count = 0
        splt = 0    #Split into how many parts
        while count < len(rs[i]):
            if rs[i][count] == '/' and rs[i][count+1] != "n":
                count += 1
                s[i][splt] += rs[i][count]
            elif rs[i][count] == '/' and rs[i][count+1] == "n":
                count += 1
            elif rs[i][count] == ',':
                s[i].append('')
                splt += 1
            else:
                s[i][splt] += rs[i][count]
            count += 1
    
    print(s)
    return s




#GRASS GRASS GRASS GRASS GRASS GRASS
#It's an area full of growing grass between 2 parts.

def openform():
    global path,mainlist,wd
    if path == "No Name" :
        if msgbox.askyesno(title="Save?",message="Do you want to save your form?"):
            save()
    else:
        save()

    path = fdl.askopenfilename(title="Open form...",filetypes=[("My From","*.myfm"),("All files", "*.*")])
    with open(path,"rt") as f:
        txt = f.read()
        frm = str_to_list(txt)
    wd.destroy()
    setup(high = len(frm),weight = len(frm[0]),putin=frm)

    """for i in range(len(mainlist)):
        for j in range(len(mainlist[0])):
            mainlist[i][j].insert(0,frm[i][j])
            print("What's up")"""

    

def get_time_str():
    return "%02d%02d%d%02d%02d%02d" % (time.localtime()[1],time.localtime()[2],time.localtime()[0],time.localtime()[3],time.localtime()[4],time.localtime()[5])

def save():
    global path
    try:
        if path == "No Name":
            path = fdl.asksaveasfilename(title="Save form...",initialfile=get_time_str()+".myfm",filetypes=[("My Form", ".myfm"),("All types", "*")],defaultextension='.myfm')

        with open(path,"wt") as f:
            f.write(form_to_str())
    except Exception as e:
        path = "No Name"
        print(e)

    
def saveas():
    with open(fdl.asksaveasfilename(title="Save form...",initialfile=get_time_str()+".myfm"),"wt") as f:
        f.write(form_to_str())

def setup(high=15,weight=10,putin=None):
    global mainlist,path,wd
    #high = 15
    #weight = 10

    wd = tk.Tk() #Main window
    wd.geometry("700x500")
    wd.title("MyForm - "+path)
    wd.iconphoto(False, tk.PhotoImage(file="surface.png"))#wd.iconbitmap("./surface.ico") can be used too if the ico file(surface.ico) is there
    mainlist = [[tk.Entry(wd,width=10) for j in range(weight)] for i in range(high)]
    print(mainlist)

    menu = tk.Menu(wd)  #Menu created 
    wd.config(menu=menu) # will not creat groups of menu

    menuFile = tk.Menu(menu) #下拉菜单
    menu.add_cascade(label="File",menu=menuFile) 
    menuFile.add_command(label="Save",command = save) #项目
    menuFile.add_command(label="Save As", command=saveas )
    menuFile.add_separator() #分割线
    menuFile.add_command(label="Open", command = openform)

    


    tk.Button(wd,text="Start",cursor="hand2",command=startbutton).grid(row=0,column=0) #turn mouse into a hand while on the img
    for i in range(weight):
        tk.Label(wd,text=chr(65+i)).grid(row=0,column=i+1) #A B C ...
    for i in range(high):
        #print(i)
        tk.Label(wd,text=str(i+1)).grid(row=i+1,column=0) #1 2 3 ...
        for j in range(weight):
            mainlist[i][j].grid(row= i+1,column=j+1) #squares are here
    
    if putin != None:
        for i in range(len(mainlist)):
            for j in range(len(mainlist[0])):
                mainlist[i][j].insert(0,putin[i][j])
                print("W",end="/")

    #Scroll bar

    bar_updown = tk.Scrollbar(wd,orient = tk.VERTICAL,jump = True,width=25)
    bar_updown.grid(row=0,column = len(mainlist[0])+1 ,rowspan=10)

    bar_leftright = tk.Scrollbar(wd,orient = tk.HORIZONTAL,jump = True,width=25)
    bar_leftright.grid(row=len(mainlist)+1,column = 1 ,columnspan=10)
    
    creator_img = tk.PhotoImage(file="./creator.png")
    tk.Button(wd,text="Creator's PVM",fg="#0000ff",image=creator_img,compound="top",cursor="hand2",command=caress_creator).grid(row=high+1,column=0,columnspan=3)

    wd.protocol ("WM_DELETE_WINDOW", on_closing) 
    wd.mainloop()


def on_closing():
    global path,wd
    
    if path == "No Name" and msgbox.askyesno(title="Save?",message="Do you want to save your form?"):
        save()
    elif path != "No Name":
        save()
        
    wd.destroy()
        
            

def main():
    global path,version
    path = "No Name"
    version = "V1.0.1"
    h,w = get_h_w()
    #print(h,w)
    if h != "e":
        while (h <= 0 or w <= 0 ):
            msgbox.showerror(title="Wrong Input",message="You typed something wrong...\nPlease type again.")
            h,w = get_h_w()
            if(h == "e"):
                break
    if (h != 'e'):
        setup(h,w)

if __name__ == "__main__":
    main()