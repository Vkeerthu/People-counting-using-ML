import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True
import os
import mainGUI_support
import os.path
import cv2
from PeopleCounter import count_people
from threading import Thread




def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1(root)
    mainGUI_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    mainGUI_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):



        def extractFrame(path):

            total_frames = 0
            toal_people = 0

            # Set up camera
            cap = cv2.VideoCapture(path)

            # Create folder to store frames
            if not os.path.exists('frames'):
                os.makedirs('frames')


            file_names = os.listdir('frames')

            # Loop over file names and remove each file
            for file_name in file_names:
                file_path = os.path.join('frames', file_name)
                os.remove(file_path)

            # Start capturing frames
            frame_num = 0
            counter=0

            file = open('frames/total.txt','w+')
            file.write(str(0))
            file.close()

            while True:
                # Capture frame-by-frame
                counter+=1
                ret, frame = cap.read()

                # If frame is successfully captured
                if ret:
                    if counter==5:
                        # Save frame to folder
                        cv2.imwrite('frames/frame_{}.jpg'.format(frame_num), frame)

                        # Count people in frame
                        Thread(target=count_people,args=(str(frame_num),)).start()
                        # num_people = count_people(frame)

                        # Increment frame number
                        frame_num += 1
                        counter =0      
                        total_frames +=1              

                # If there is an error capturing the frame
                else:
                    print('Error capturing frame')
                    file = open('frames/total_frame.txt','w+')
                    file.write(str(frame_num))
                    file.close()
                    break


            top.destroy()
            import DisplayFrame


        def VideoModule(event):
            VideoFileName = filedialog.askopenfilename(initialdir="/", title="Select Video file", filetypes=(
            ("MP4 files", "*.mp4"), ("avi files", "*.avi"), ("all files", "*.*")))
            try:
                extractFrame(VideoFileName)
            except Exception as e:
                print(e)
                messagebox.showinfo('Error','Please Select Valid file '+str(e))

        def btnExit(event):
            import os
            os._exit(0)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font16 = "-family Constantia -size 40 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font18 = "-family {Sitka Small} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        w = 1000
        h = 650
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # top.geometry("1016x635")
        top.title("Sickness Detection (CNN)")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.3, rely=0.01, height=250, width=350)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "Images/yologo_2.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=self._img0)
        self.Label1.configure(text='''Label''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=0.4, height=88, width=1000)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font16)
        self.Label2.configure(foreground="#2365e8")
        self.Label2.configure(text='''People Counting''')
        self.Label2.configure(width=659)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.03, rely=0.535, relheight=0.402, relwidth=0.94)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="7")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(width=955)


        self.btnVideo = tk.Label(self.Frame1)
        self.btnVideo.place(relx=0.19, rely=0.090, height=186, width=162)
        self.btnVideo.configure(activebackground="#f9f9f9")
        self.btnVideo.configure(activeforeground="black")
        self.btnVideo.configure(background="#ffffff")
        self.btnVideo.configure(disabledforeground="#a3a3a3")
        self.btnVideo.configure(foreground="#000000")
        self.btnVideo.configure(highlightbackground="#d9d9d9")
        self.btnVideo.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "Images/video-camera-png-icon-5.png")
        self._img3 = tk.PhotoImage(file=photo_location)
        self.btnVideo.configure(image=self._img3)
        self.btnVideo.configure(text='''Label''')
        self.btnVideo.configure(width=162)
        self.btnVideo.bind('<Button-1>', VideoModule)


        self.Label3_6 = tk.Label(self.Frame1)
        self.Label3_6.place(relx=0.2, rely=0.784, height=36, width=142)
        self.Label3_6.configure(activebackground="#f9f9f9")
        self.Label3_6.configure(activeforeground="black")
        self.Label3_6.configure(background="#ffffff")
        self.Label3_6.configure(disabledforeground="#a3a3a3")
        self.Label3_6.configure(font=font18)
        self.Label3_6.configure(foreground="#061104")
        self.Label3_6.configure(highlightbackground="#d9d9d9")
        self.Label3_6.configure(highlightcolor="#000000")
        self.Label3_6.configure(text='''Video''')
        self.Label3_6.configure(width=142)

        self.btnExit = tk.Label(self.Frame1)
        self.btnExit.place(relx=0.6, rely=0.100, height=186, width=150)
        self.btnExit.configure(activebackground="#f9f9f9")
        self.btnExit.configure(activeforeground="black")
        self.btnExit.configure(background="#ffffff")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "Images/ExitIcon.png")
        self._img4 = tk.PhotoImage(file=photo_location)
        self.btnExit.configure(image=self._img4)
        self.btnExit.configure(text='''Label''')
        self.btnExit.configure(width=162)
        self.btnExit.bind('<Button-1>', btnExit)

        self.Label3_6 = tk.Label(self.Frame1)
        self.Label3_6.place(relx=0.61, rely=0.784, height=26, width=130)
        self.Label3_6.configure(activebackground="#f9f9f9")
        self.Label3_6.configure(activeforeground="black")
        self.Label3_6.configure(background="#ffffff")
        self.Label3_6.configure(disabledforeground="#a3a3a3")
        self.Label3_6.configure(font=font18)
        self.Label3_6.configure(foreground="#061104")
        self.Label3_6.configure(highlightbackground="#d9d9d9")
        self.Label3_6.configure(highlightcolor="#000000")
        self.Label3_6.configure(text='''Exit''')
        self.Label3_6.configure(width=142)




vp_start_gui()