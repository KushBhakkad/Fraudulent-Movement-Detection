import cv2                            #importing OpenCV
from datetime import datetime         #importing Datetime
import winsound                       #inporting soundlibrabry
from tkinter import *
from PIL import Image
from PIL import ImageTk
import subprocess
import os
from twilio.rest import Client
import pywhatkit

# import pywhatkit

def openfolder():
    subprocess.Popen(r'explorer /select,"D:\Practice\recordings\"')


def strat():
    # client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    cap = cv2.VideoCapture(0)   
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  #For Recording Video
    out = cv2.VideoWriter(f'recordings/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc,20,(640,480))  #Store record
    # img_out = f"/{datetime.today()}.png"
    # img_out = "2.png"
    count = 0
    time_now = datetime.now()

    while True:
        _, frame1 = cap.read()         
        _, frame2 = cap.read()
        diff = cv2.absdiff(frame2, frame1)                                                           
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv2.blur(diff, (5,5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY) 

        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(max_cnt)                                                     #display a box
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)                                 #display a box
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)       #Motion display
            cv2.putText(frame1, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,255,255), 2)   #Date-time stamp
            out.write(frame1)
            count += 1
            if count == 30:
                winsound.PlaySound('alert.wav', winsound.SND_FILENAME)

                pywhatkit.sendwhatmsg('+918668831058', 'Alert! Suspicious behavior detected!', time_now.hour, time_now.minute + 2)
                
                count=0
                

        else:
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)

        # cv2.imshow("esc. to exit", frame1)   #display Color Camera
        cv2.imshow("esc. to exit", diff)   #display B&W Camera

        if cv2.waitKey(1) == 27:       #Stop the program
            cap.release()
            cv2.destroyAllWindows()
            break

root = Tk()
root.geometry("400x400")
root.maxsize(400,400)

root.title("Motion Detection System")
photo=PhotoImage(file="download.png")
label1 = Label( root, image = photo)
label1.place(x = 0, y = 0)

frame=Frame(root, relief=SUNKEN, bg = "#88cffa")
frame.pack(side=TOP,pady=100)

b1=Button(frame,text="Start",command=strat,padx=95,pady=10,font="comicsansms 12 bold")
b1.pack(pady=5)
b2=Button(frame,text="Open recordings",command=openfolder,padx=50,pady=10,font="comicsansms 12 bold")
b2.pack(pady=5)
label=Label(text="Developed By:\nB11 group, VIT Pune ",justify=LEFT,font="comicsansms 12 bold")
label.pack(side=BOTTOM)

root.mainloop()