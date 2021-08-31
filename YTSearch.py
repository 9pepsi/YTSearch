import tkinter as tk
import googleapiclient.discovery
import googleapiclient.errors
import webbrowser
import tkinter.font as font

#Functionality#
def getSearch(title):
    yt = googleapiclient.discovery.build('youtube', 'v3', developerKey='AIzaSyCmZG4N4i91tQM5jLcuvAcQZ2K08c2hc6U')
    request=yt.search().list(
    part="snippet",
    maxResults=5,
    q=title,
    type="video"
    )
    response = request.execute()
    Query = []
    global vID
    vID = []
    for title in response['items']:
     list = title['snippet']['title']
     watch = title['id']['videoId']
     Query.append(list)
     vID.append(watch)
    Label1['text']=Query[0]
    Label2['text']=Query[1]
    Label3['text']=Query[2]
    Label4['text']=Query[3]
    Label5['text']=Query[4]
#GUI_Object_Declration#

Root = tk.Tk()
Root.title("Simple Youtube Search")
Root.iconbitmap('C:/Users/mj/Desktop/YTSAPI/logo.ico')
Canvas = tk.Canvas(Root, height=600,width=600)
BgImg= tk.PhotoImage(file="C:/Users/mj/Desktop/YTSAPI/bg_img.png")
BgLabel= tk.Label(Root, image=BgImg)
Frame1 =tk.Frame(Root, bg='#2e2e2e',bd=5)
myFont = font.Font(family='Fira Code')
SButton = tk.Button(Frame1, text="Search YT",font=myFont ,bg='#b32e2e',fg='black',command= lambda: getSearch(SBar.get()))
SBar= tk.Entry(Frame1, bg='grey', font=500)
Frame2=tk.Frame(Root, bg='#2e2e2e', bd=10)
Label1= tk.Button(Frame2, command= lambda: webbrowser.open("https://www.youtube.com/watch?v="+vID[0]))
Label2= tk.Button(Frame2, command= lambda: webbrowser.open("https://www.youtube.com/watch?v="+vID[1]))
Label3= tk.Button(Frame2, command= lambda: webbrowser.open("https://www.youtube.com/watch?v="+vID[2]))
Label4= tk.Button(Frame2, command= lambda: webbrowser.open("https://www.youtube.com/watch?v="+vID[3]))
Label5= tk.Button(Frame2, command= lambda: webbrowser.open("https://www.youtube.com/watch?v="+vID[4]))

#GUI_Objects_Placement#

Canvas.pack()
BgLabel.place(relheight=1,relwidth=1)
Frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
SButton.place(relx=0.7,relheight=1,relwidth=0.3)
SBar.place(relwidth=0.65, relheight=1)
Frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
Label1.place(relwidth=1, relheight=0.17)
Label2.place(relwidth=1, relheight=0.17,relx=0,rely=.21)
Label3.place(relwidth=1, relheight=0.17,relx=0,rely=.42)
Label4.place(relwidth=1, relheight=0.17,relx=0,rely=.63)
Label5.place(relwidth=1, relheight=0.17,relx=0,rely=.84)

###Main###
Root.mainloop()