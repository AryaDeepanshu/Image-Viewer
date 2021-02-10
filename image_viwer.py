from tkinter import *
from PIL import ImageTk,Image
import os,pygame

root = Tk()
root.title("Image viewer")

images = os.listdir("img/")
for i in images[:]:
    if not(i.endswith(".png") or i.endswith(".jpg") or i.endswith(".JPG")):
        images.remove(i)
for i in range(len(images)):
    images[i] = ImageTk.PhotoImage(Image.open("img/"+images[i]).resize((400,400), Image.ANTIALIAS))

def nxt_img(image_number):
    global my_label
    global btn_nxt_img
    global btn_prv_img
    if image_number == 0:
        my_label = Canvas(root,width=500,height=500)
        my_label.create_image(20, 20, anchor=NW, image=images[image_number])
        my_label.grid_forget()
        btn_lr = Button(root,text="",image=lr,command=lambda: lr_img(image_number+1))
        btn_rr = Button(root,text="",image=rr,command=lambda: rr_img(image_number+1))
        btn_prv_img = Button(root,text="<=",state=DISABLED)
        btn_nxt_img = Button(root,text="=>",command= lambda: nxt_img(image_number+1))
    else:
        my_label.grid_forget()
        my_label = Canvas(root,width=500,height=500)
        my_label.create_image(20, 20, anchor=NW, image=images[image_number])
        btn_lr = Button(root,text="",image=lr,command=lambda: lr_img(image_number+1))
        btn_rr = Button(root,text="",image=rr,command=lambda: rr_img(image_number+1))
        btn_nxt_img = Button(root,text="=>",command= lambda: nxt_img(image_number+1))
        btn_prv_img = Button(root,text="<=",command= lambda: prv_img(image_number-1))
        if image_number == len(images)-1:
            btn_nxt_img = Button(root,text="=>",state=DISABLED)
    my_label.grid(row=0,column=0,columnspan=5)
    btn_nxt_img.grid(row=1,column=4)
    btn_prv_img.grid(row=1,column=0)
    btn_lr.grid(row=1,column=1)
    btn_rr.grid(row=1,column=3)
def prv_img(image_number):
    global my_label
    global btn_nxt_img
    global btn_prv_img
    if image_number ==0:
       my_label.grid_forget()
       my_label = Canvas(root,width=500,height=500)
       my_label.create_image(20, 20, anchor=NW, image=images[image_number])
       btn_prv_img = Button(root,text="<=",state=DISABLED)
       btn_nxt_img = Button(root,text="=>",command= lambda: nxt_img(image_number+1))
       btn_lr = Button(root,text="",image=lr,command=lambda: lr_img(image_number))
       btn_rr = Button(root,text="",image=rr,command=lambda: rr_img(image_number))
    else:
        my_label.grid_forget()
        my_label = Canvas(root,width=500,height=500)
        my_label.create_image(20, 20, anchor=NW, image=images[image_number])
        btn_nxt_img = Button(root,text="=>",command= lambda: nxt_img(image_number+1))
        btn_prv_img = Button(root,text="<=",command= lambda: prv_img(image_number-1))
        btn_lr = Button(root,text="",image=lr,command=lambda: lr_img(image_number-1))
        btn_rr = Button(root,text="",image=rr,command=lambda: rr_img(image_number-1))
    my_label.grid(row=0,column=0,columnspan=5)
    btn_nxt_img.grid(row=1,column=4)
    btn_prv_img.grid(row=1,column=0)
    btn_lr.grid(row=1,column=1)
    btn_rr.grid(row=1,column=3)
def lr_img(image_number):
    
    surface = pygame.transform.rotate(pygame.image.load("img/Capture.JPG"),90)
    my_label = Canvas(root,width=500,height=500)
    my_label.create_image(20, 20, anchor=NW, image=surface)
    my_label.grid(row=0,column=0,columnspan=5)

def rr_img(image_number):
    pass

lr = PhotoImage(file = r"E:\programs\lr.png")
rr = PhotoImage(file = r"E:\programs\rr.png")
my_label = Canvas(root,width=500,height=500)
my_label.create_image(20, 20, anchor=NW, image=images[0])
btn_prv_img = Button(root,text="<=",state=DISABLED)
btn_lr = Button(root,text="",image=lr,command=lambda: lr_img(0))
btn_exit = Button(root,text="Exit",command=root.quit)
btn_rr = Button(root,text="",image=rr,command=lambda: rr_img(0))
btn_nxt_img = Button(root,text="=>",command=lambda: nxt_img(1))

my_label.grid(row=0,column=0,columnspan=5)
btn_prv_img.grid(row=1,column=0)
btn_lr.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)
btn_rr.grid(row=1,column=3)
btn_nxt_img.grid(row=1,column=4)

root.mainloop()
