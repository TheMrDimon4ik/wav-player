from tkinter import *
import simpleaudio as sa

root = Tk()

def but():
    ms = music.get()
    wave_obj = sa.WaveObject.from_wave_file(ms)
    play_obj = wave_obj.play()
    play_obj.wait_done()

root['bg'] = '#fafafa'
root.title("Wav Player")
root.geometry('205x280')
textsh = Label(root, text="после начала проигрывания\nпрограма не будет отвечать\nдо завершение музыки", bg="gray", font=40)
textsh.pack()

frame = Frame(root, bg='green')
frame.place(relx=0.20, rely=0.20, relwidth=0.7, relheight=0.7)

but = Button(frame, text='проигрывать', bg='gray', command=but)
but.pack()

music = Entry(frame, bg='white')
music.pack()

text = Label(frame, text='писать с расширением\nпример: music.wav', bg='gray')
text.pack()

root.mainloop()