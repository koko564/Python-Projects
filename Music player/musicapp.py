import os
import tkinter
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk

root = Tk()

image1 = Image.open("musicapp.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

label1.place(x=0, y=0)

class MusicPlayer:
    def __init__(self, window ):
        
        window.geometry('900x400'); window.title('GroovZ'); window.resizable(0,0)
       
        Play = Button(window,bg='#DBA2F4', text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,bg='#DBA2F4',text = 'Pause/Resume',  width = 15, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,bg='#DBA2F4',text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load_playlist= Button(window ,bg='#DBA2F4',text = 'Load Playlist',  width = 10, font = ('Times', 10), command = self.load_playlist)
        Play.place(x=140,y=250);Pause.place(x=250,y=250);Stop.place(x=200,y=300);Load_playlist.place(x=800,y=20)
        self.music_file = False
        self.playing_state = False
        
   
   
    def load_playlist(self):

        directory = filedialog.askdirectory()
        os.chdir(directory)
        songsframe = LabelFrame(root,text="Song Playlist",font=("times new roman",15,"bold"),bg="#91D6D9",fg="black",bd=5,relief=GROOVE)
        songsframe.place(x=500,y=0,width=400,height=400)
    # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="#DBA2F4",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="#41CF88",fg="black",bd=5,relief=GROOVE)
    # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        songtracks = os.listdir()
    
        for track in songtracks:
         self.playlist.insert(END,track)
    def play(self):
        self.music_file = self.playlist.get(ACTIVE)
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    
    def stop(self):
        mixer.music.fadeout(500)

app= MusicPlayer(root)
root.mainloop()