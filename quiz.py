from tkinter import *
import random
from random import shuffle
from PIL import ImageTk, Image
import time
import pygame
import winsound 


pygame.init()

score = 0
flag=0
root = Tk()  # object of main window

soundstatus=1
frame = Frame(root, width=200, height=200 )

var1=IntVar()
var2=IntVar()
var3=IntVar()

root.title("The LOGO Game ")
i0 = "gucci.png"
i1 = "nike.png"
i2 = "adidas.png"
i3 = "chanel.png"
i4 = "prada.png"
i5 = "louisvuitton.png"
i6 = "versace.png"
i7 = "dior.png"
i8 = "hermes.png"
i9 = "ralphlauren.png"
i10 = "burberry.png"
i11 = "fendi.png"
i12 = "givenchy.png"
i13 = "dolcegabbana.png"
i14 = "balenciaga.png"
i15 = "saintlaurent.png"
i16 = "tomford.png"
i17 = "valentino.png"
i18 = "offwhite.png"
i19 = "moncler.png"
i20 = "armani.png"

musicflag=1

list1 = []
list = list = [[i0, "Gucci"], [i1, "Nike"], [i2, "Adidas"], [i3, "Chanel"], [i4, "Prada"], [i5, 'Louis Vuitton'],
        [i6, 'Versace'], [i7, 'Dior'], [i8, 'Hermes'], [i9, 'Ralph Lauren'], [i10, 'Burberry'],
        [i11, 'Fendi'], [i12, 'Givenchy'], [i13, 'Dolce & Gabbana'], [i14, 'Balenciaga'],
        [i15, 'Saint Laurent'], [i16, 'Tom Ford'], [i17, 'Valentino'], [i18, 'Off-White'],
        [i19, 'Moncler'], [i20, 'Armani']]
list2 = list2 = [['Gucci', 'Prada', 'Versace', 'Dior'], ['Nike', 'Puma', 'Reebok', 'Adidas'], 
         ['Adidas', 'Nike', 'Puma', 'Reebok'], ['Chanel', 'Gucci', 'Versace', 'Dior'],
         ['Prada', 'Gucci', 'Fendi', 'Chanel'], ['Louis Vuitton', 'Gucci', 'Prada', 'Fendi'],
         ['Versace', 'Gucci', 'Armani', 'Valentino'], ['Dior', 'Gucci', 'Versace', 'Prada'],
         ['Hermes', 'Gucci', 'Prada', 'Chanel'], ['Ralph Lauren', 'Gucci', 'Versace', 'Dior'],
         ['Burberry', 'Gucci', 'Prada', 'Fendi'], ['Fendi', 'Gucci', 'Versace', 'Dior'],
         ['Givenchy', 'Gucci', 'Prada', 'Fendi'], ['Dolce & Gabbana', 'Gucci', 'Versace', 'Dior'],
         ['Balenciaga', 'Gucci', 'Prada', 'Fendi'], ['Saint Laurent', 'Gucci', 'Versace', 'Dior'],
         ['Tom Ford', 'Gucci', 'Prada', 'Fendi'], ['Valentino', 'Gucci', 'Versace', 'Dior'],
         ['Off-White', 'Gucci', 'Prada', 'Fendi'], ['Moncler', 'Gucci', 'Versace', 'Dior'],
         ['Armani', 'Gucci', 'Prada', 'Fendi']]
f_obj = open("highscore.txt", "r")
f_inst=open("instructions.txt","r")
hscore = int(f_obj.read())
instructions=f_inst.read()
#instructions=instructions.strip()

# print(hscore)
# print(score)


def showimage():

	def button_event(text, x):
		if text == list[x][1]:
			global score, hscore
			score = score + 1;print("CURRENT SCORE: ", score)

			if hscore < score:
				f_obj = open("highscore.txt", "w")

				hscore = score
				print("HIGHSCORE:", hscore)
				f_obj.write(str(score))
				f_obj.close()
			else:
				print("HIGHSCORE", hscore)
			
			print("correct")
			 
			answer=1
			sound(answer)
			frame1.destroy()
			showimage()
		else:
			print("Wrong")
			frame1.destroy()
			
			answer=0
			sound(answer)
			frame3=Frame(root,width=500,height=330)
			canvas3=Canvas(frame3,width=500,height=330,bg="lightblue")
			
			canvas3.create_text(250,80,text="You Lose!!!!",fill="red",font=("Times",30))
			canvas3.create_text(245,150,text="Better Luck Next Time",fill="red",font=("Times",30))
			canvas3.create_text(240,195,text="Your Score: "+str(score),fill="darkblue",font=("Times",30))
				
			restart_but1 = Button(frame3, text="Play again", width=15, height=2, command=lambda: restart(frame3))
			restart_but1.place(x=135, y=250)
			exit_but1=Button(frame3, text="Quit", width=15, height=2, command=exit)
			exit_but1.place(x=255, y=250)
			canvas3.pack()
			frame3.pack()

	def showbuttons(n):
		if musicflag == 0:
			val=1
		else:
			val=0
		cbut_music1 = Checkbutton(frame1, text="Music",variable=var1,onvalue=val,offvalue=not val,command=music)
		cbut_music1.place(x=450,y=3)
		
		cbut_sound = Checkbutton(frame1, text="Sound",variable=var2,onvalue=0,offvalue=1,command=soundflag)
		cbut_sound.place(x=380,y=3)	
		
		shuffle(list2[n])
		x1=10
		y1=260
		option1 = Button(frame1, text=list2[n][0], width=34, height=2, command=lambda: button_event(list2[n][0], n))
		option1.place(x=x1, y=y1)

		x2=265
		y2=260
		option2 = Button(frame1, text=list2[n][1], width=34, height=2, command=lambda: button_event(list2[n][1], n))
		option2.place(x=x2, y=y2)
		
		x3=10
		y3=305
		option3 = Button(frame1, text=list2[n][2], width=34, height=2, command=lambda: button_event(list2[n][2], n))
		option3.place(x=x3, y=y3)
		
		x4=265
		y4=305
		option4 = Button(frame1, text=list2[n][3], width=34, height=2, command=lambda: button_event(list2[n][3], n))
		option4.place(x=x4, y=y4)
        
	frame.destroy()
	global frame1
	frame1 = Frame(root, width=520, height=350)
	canvas1 = Canvas(frame1, width=520, height=350,bg="lightblue")
	canvas1.place(x=0, y=0)
	
	
	canvas1.create_rectangle(380,32,500,47,fill="white")   
	canvas1.create_rectangle(380,52,500,67,fill="white")	
	canvas1.create_text(435, 40, fill="darkblue", text="CURRENT SCORE : ",font=("Times",9))
	canvas1.create_text(490, 40, fill="darkblue", text=str(score),font=("Times",9))
	canvas1.create_text(436, 60, fill="red", text="HIGH  SCORE       : ",font=("Times",9))
	canvas1.create_text(490, 60, fill="red", text=str(hscore),font=("Times",9))
	
	n = random.randrange(0, 20, 1)
    
	def restart(frame2):
		global score
		score=0
		frame2.destroy()
		showimage()
		
	if len(list1) == 20:
		list1.clear()
		frame1.destroy()
		frame2 = Frame(root)
		canvas2 = Canvas(frame2, height=330, width=500,bg="lightblue")

		canvas2.create_text(250,80, fill="green", text="You Won!!!!", font=("Times", 30))
		canvas2.create_text(250,130, fill="darkblue", text="*Congratulations*", font=("Times", 30))
		
		restart_but = Button(frame2, text="Play again", width=15, height=2, command=lambda: restart(frame2))
		restart_but.place(x=135, y=170)
		exit_but=Button(frame2, text="Quit", width=15, height=2, command=exit)
		exit_but.place(x=255, y=170)
		canvas2.pack()
		frame2.pack()

	elif n in list1:
		showimage()

	else:
		
		canvas1.create_rectangle(12,12,253,253)
		canvas1.create_rectangle(10,10,255,255,fill="gray")
		canvas1.create_rectangle(15,15,250,250,fill="lightblue")
		img = ImageTk.PhotoImage(Image.open("Images/"+list[n][0]))
		canvas1.create_image(20, 20, anchor=NW, image=img)
		canvas1.image = img
		canvas1.place(x=0, y=0)
		
		list1.append(n)
		showbuttons(n)

	frame1.pack()
	print("list1 : ",list1)
	
def soundflag():
	global soundstatus 
	if soundstatus == 0:
		print("sound on\n")
		soundstatus=1
	elif soundstatus == 1:
		print("sound off\n")
		soundstatus=0
		



def exit():

	quit()
def music():
	
	global musicflag
	if musicflag == 0:
		musicflag=1
		pygame.mixer.music.load('music.mp3')
		pygame.mixer.music.play(-1)
		print("music on")
	else:
		musicflag=0
		pygame.mixer.music.stop()
		print("music off")	

def sound(answer):
	if soundstatus == 1:
		if answer == 1 :
			winsound.Beep(4000,100)
		
		elif answer == 0:
			winsound.Beep(400,300)


def showinst():
		def closeinsrtuct():
			instwindow.destroy()
			
		instwindow=Tk()
		instwindow.title("Instructions")
		global fr2
		fr2=Frame(instwindow, width=500, height=300)
		ca2 = Canvas(fr2, height=300, width=500,bg="lightblue")
		#ca2.create_rectangle(380,32,500,47,fill="white")
		instlabel=Label(ca2,text=instructions,font="Times 14")
		close_but=Button(fr2, text="Close",width=10, height=1, command=closeinsrtuct)
		
		instlabel.place(x=25,y=50)
		close_but.place(x=200,y=260)
		ca2.pack()
		fr2.pack()
		instwindow.resizable(0,0)
		instwindow.mainloop()
		

		


canvas4 = Canvas(frame, height=800, width=800)
back_img=ImageTk.PhotoImage(Image.open("Images/final.png"))
canvas4.create_image(0, 0, anchor=NW, image=back_img)
canvas4.image = back_img
canvas4.pack()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

but = Button(frame, text="Start",width=25, height=1, command=showimage)
but1 = Button(frame, text="Quit", width=25, height=1,command=exit)
cbut_music = Checkbutton(frame, text="Music",variable=var3,onvalue=0,offvalue=1,command=music)
instbut=Button(frame,text="Help",width=25,height=1,command=showinst)

instbut.place(x=160,y=80)
but.place(x=60,y=40)
but1.place(x=280,y=40)
cbut_music.place(x=430,y=3)

frame.pack()
root.resizable(0,0)
root.mainloop()
