import tkinter as tk

import AttendanceProjects

root = tk.Tk()

Canvas = tk.Canvas(root, height=700,width=700,bg="#392ed9")
Canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8,relheight=0.8, relx=0.1,rely=0.1)

openFile = tk.Button(frame, text="Track Attendance", 
            padx=100, pady=100, fg="white", bg="#392ed9",command=AttendanceProjects.loopfunction)
openFile.pack()

escape = tk.Button(frame, text="NOTE: Press 'q' to escape", 
            padx=100, pady=100, fg="white", bg="#392ed9",)
escape.pack()



root.mainloop()