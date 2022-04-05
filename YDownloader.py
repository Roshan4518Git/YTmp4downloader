from pytube import YouTube
from pytube.cli import on_progress
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from threading import *
from tkinter.filedialog import askdirectory
#total size container
file_size = 0

# #this function is call for updating percentage...
def progress(stream=None,chunk=None,file_handle=None,remaining=None):
    # get the percentage of file that has been downloaded
    file_downloaded=(file_size-remaining)
    per=(file_downloaded/file_size)*100
    dBtn.config(text="{} % downloaded".format(per))
    

def startDownload():
    global file_size
    try:
        url= urlField.get()
        print(url)
        #change Buton text
        dBtn.config(text='Please wait...')
        dBtn.config(state = DISABLED)
        PATH_SAVE = askdirectory()
        print(PATH_SAVE)
        if PATH_SAVE is None:
            return 
        # creating youtube object with url
        ob = YouTube(url,on_progress_callback=on_progress) #add after url

        strm = ob.streams.first()
        file_size=strm.filesize
        print(file_size)

        strm.download(PATH_SAVE)

        print("Downloaded")
        
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Downloading Finish","Downloaded Successfully")
        # urlField.delete(0,END)

    except Exception as e:
        print(e)
        print("ERROR !")

def startDownloadThread():
#create thread
    thread=Thread(target=startDownload)
    thread.start()

#strarting GUI Building
main = Tk()
main.title("My Youtube Downloader")

# set the icon
main.iconbitmap('icon.ico')

main.geometry("500x600")

#heading icon
file=PhotoImage(file='ydown.png')
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP)

#url textField
urlField = Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=10)

#download Button
dBtn=Button(main,text="Start Download",font=("verdana",18),relief='ridge',command=startDownloadThread)
dBtn.pack(side=TOP,pady=10)


main.mainloop()
