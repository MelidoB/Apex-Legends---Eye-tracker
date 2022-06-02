import tkinter, win32api, win32con, pywintypes
from tkinter import Tk,PhotoImage,Label

root = Tk()
root.configure(background='white')
# Create a photoimage object of the image in the path
img1 = PhotoImage(file="cursor.png")

label = Label(image=img1,fg='black', bg='white')
label.image = img1

# Position image
label.master.overrideredirect(True)
label.master.geometry("+250+250")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

label.pack(padx=490,pady=153)
label.mainloop()
