#!/usr/bin/python
#-*- coding:utf-8 -*-

import tkinter as tk
from PIL import Image,ImageTk,ImageSequence
import time
import datetime
import threading

root=tk.Tk()
root.title('clock')
root.geometry('213x88')
root.resizable(False,False)

timcanvas=tk.Canvas(root,width=213,height=88,bg='white')
timcanvas.place(x=0,y=0)
timimg=tk.PhotoImage(file='time.png')
timcanvas.create_image(1,1,anchor='nw',image=timimg)
                
t0=tk.PhotoImage(file='time0.png')
t1=tk.PhotoImage(file='time1.png')
t2=tk.PhotoImage(file='time2.png')
t3=tk.PhotoImage(file='time3.png')
t4=tk.PhotoImage(file='time4.png')
t5=tk.PhotoImage(file='time5.png')
t6=tk.PhotoImage(file='time6.png')
t7=tk.PhotoImage(file='time7.png')
t8=tk.PhotoImage(file='time8.png')
t9=tk.PhotoImage(file='time9.png')

def tim():
    while True:
        timy=list(str(datetime.datetime.now().year))
        timm=list(str(datetime.datetime.now().month))
        timd=list(str(datetime.datetime.now().day))
        timh=list(str(datetime.datetime.now().hour))
        timmin=list(str(datetime.datetime.now().minute))
        tims=list(str(datetime.datetime.now().second))
                    
        dic={'0':t0,'1':t1,'2':t2,'3':t3,'4':t4,'5':t5,'6':t6,'7':t7,'8':t8,'9':t9}

        def show(a,b,c=0,d=0,e=0):
            wt1=dic[str(a)]
            wt2=dic[str(b)]
            wt3=dic[str(c)]
            wt4=dic[str(d)]
            if e==0:
                timcanvas.create_image(1,4,anchor='nw',image=wt1)
                timcanvas.create_image(22,4,anchor='nw',image=wt2)
                timcanvas.create_image(43,4,anchor='nw',image=wt3)
                timcanvas.create_image(64,4,anchor='nw',image=wt4)
            elif e==1:
                timcanvas.create_image(106,4,anchor='nw',image=wt1)
                timcanvas.create_image(127,4,anchor='nw',image=wt2)
            elif e==2:
                timcanvas.create_image(169,4,anchor='nw',image=wt1)
                timcanvas.create_image(190,4,anchor='nw',image=wt2)
            elif e==3:
                timcanvas.create_image(1,46,anchor='nw',image=wt1)
                timcanvas.create_image(22,46,anchor='nw',image=wt2)
            elif e==4:
                timcanvas.create_image(64,46,anchor='nw',image=wt1)
                timcanvas.create_image(85,46,anchor='nw',image=wt2)
            elif e==5:
                timcanvas.create_image(127,46,anchor='nw',image=wt1)
                timcanvas.create_image(148,46,anchor='nw',image=wt2)
        time.sleep(0.97)
                            
        timy1=timy[0]
        timy2=timy[1]
        timy3=timy[2]
        timy4=timy[3]
        show(a=timy1,b=timy2,c=timy3,d=timy4,e=0)
            
        if len(timm)==1:
            timm1=timm[0]
            show(a=0,b=timm1,e=1)
        else:
            timm1=timm[0]
            timm2=timm[1]
            show(a=timm1,b=timm2,e=1)

        if len(timd)==1:
            timd1=timd[0]
            show(a=0,b=timd1,e=2)
        else:
            timd1=timd[0]
            timd2=timd[1]
            show(a=timd1,b=timd2,e=2)
            
        if len(timh)==1:
            timh1=timh[0]
            show(a=0,b=timh1,e=3)
        else:
            timh1=timh[0]
            timh2=timh[1]
            show(a=timh1,b=timh2,e=3)

        if len(timmin)==1:
            timmin1=timmin[0]
            show(a=0,b=timmin1,e=4)
        else:
            timmin1=timmin[0]
            timmin2=timmin[1]
            show(a=timmin1,b=timmin2,e=4)
        
        if len(tims)==1:
            tims1=tims[0]
            show(a=0,b=tims1,e=5)
        else:
            tims1=tims[0]
            tims2=tims[1]
            show(a=tims1,b=tims2,e=5)

t=threading.Thread(target=tim)
t.start()
root.mainloop()

