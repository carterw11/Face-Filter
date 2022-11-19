from tkinter import *
from PIL import *
from PIL import Image, ImageTk
import cv2
import time

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        self.running = True

        self.canv = Canvas(master, height=5, width=5)
        self.canv.pack() 

        self.mode = 0

        self.leftButton = Button(self.canv, height = 1, width = 8, text="Prev Filter", command=self.subtractMode)
        self.rightButton = Button(self.canv, height = 1, width = 8, text="Next Filter", command=self.addMode)
        self.quitButton = Button(self.canv, height = 1, width = 4, text="Exit", command=self.exitApp)

        self.leftButton.place(x=0,y=0)
        self.rightButton.place(x=0,y=0)
        self.quitButton.place(anchor=NW,x=0,y=0)

    def subtractMode(self):
        self.mode -= 1
        if self.mode < 0:
            self.mode = 5

    def addMode(self):
        self.mode += 1
        if self.mode > 5:
            self.mode = 0

    def updateCanvas(self, frame):
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

        colourframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faceimg = Image.fromarray(colourframe)
        faceimage = ImageTk.PhotoImage(faceimg)
        self.canv.config(width=faceimg.width,height=faceimg.height)
        self.canv.create_image(0,0, anchor=NW, image=faceimage)
        
        for (xpos, ypos, w, h) in face_coordinates:
            if self.mode == 1:
                cv2.rectangle(frame, (xpos, ypos), (xpos+w, ypos+h), (0, 0, 255), 2)
                colourframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faceimg = Image.fromarray(colourframe)
                faceimage = ImageTk.PhotoImage(faceimg)
                self.canv.config(width=faceimg.width,height=faceimg.height)
                self.canv.create_image(0,0, anchor=NW, image=faceimage)
            elif self.mode == 2:
                resizedPhoto = happyImage.resize((int(w*1.3),int(h*1.3)))
                adjustedPhoto = ImageTk.PhotoImage(resizedPhoto)
                self.canv.create_image(xpos+(w/2),ypos+(h/2),image=adjustedPhoto)
            elif self.mode == 3:
                resizedPhoto = sadImage.resize((int(w*1.3),int(h*1.3)))
                adjustedPhoto = ImageTk.PhotoImage(resizedPhoto)
                self.canv.create_image(xpos+(w/2),ypos+(h/2),image=adjustedPhoto)
            elif self.mode == 4:
                resizedPhoto = sunglassesImage.resize((int(w*1.3),int(h*1.3)))
                adjustedPhoto = ImageTk.PhotoImage(resizedPhoto)
                self.canv.create_image(xpos+(w/2),ypos+(h/2),image=adjustedPhoto)
            elif self.mode == 5:
                resizedPhoto = angryImage.resize((int(w*1.3),int(h*1.3)))
                adjustedPhoto = ImageTk.PhotoImage(resizedPhoto)
                self.canv.create_image(xpos+(w/2),ypos+(h/2),image=adjustedPhoto)
                

        
        self.leftButton.place(x=0, y=self.canv.winfo_height()-self.leftButton.winfo_height())
        self.rightButton.place(x=self.canv.winfo_width()-self.rightButton.winfo_width(), y=self.canv.winfo_height()-self.leftButton.winfo_height())
        self.quitButton.place(anchor=NW,x=0,y=0)
        self.canv.update_idletasks()
        self.canv.update()
        time.sleep(0.01)
    
    def exitApp(self):
        self.running = False

webcam = cv2.VideoCapture(0)
top = Tk()
top.title("Face Detector")
mainWindow = Window(top)
happyImage = Image.open ("happy.png")
sadImage = Image.open("sad.png")
sunglassesImage=Image.open("sunglasses.png")
angryImage = Image.open("angry.png")

while mainWindow.running:
    successful_frame_read , frame = webcam.read()
    
    mainWindow.updateCanvas(frame)