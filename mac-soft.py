from tkinter import *
from tkinter import ttk, messagebox, filedialog
import tkinter as tk
import platform
import psutil

# brightness
import screen_brightness_control as pct

# audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

# clock
from time import strftime

# calendar
from tkcalendar import *

# open google
import pyautogui

import subprocess
import webbrowser as wb
import random

# Create the main window
root = Tk()
root.title('mac-soft Tool')
root.geometry("850x500+300+170")
root.resizable(False, False)
root.configure(bg='#292e2e')  # Corrected color code for background

# Set the window icon
image_icon = PhotoImage(file="Images/109613.png")
root.iconphoto(False, image_icon)

# Main Body Frame
Body = Frame(root, width=900, height=600, bg="#d6d6d6")
Body.pack(pady=20, padx=20)

# Left-Hand Side Frame
LHS = Frame(Body, width=310, height=435, bg="#f4f5f5", highlightbackground="black")
LHS.place(x=10, y=10)

# Right-Hand Side Frame
RHS = Frame(Body, width=470, height=230, bg="#f4f5f5", highlightbackground="black")
RHS.place(x=330, y=10)

# Right-Hand Bottom Frame
RHB = Frame(Body, width=470, height=190, bg="#f4f5f5", highlightbackground="black")
RHB.place(x=330, y=255)

# Example Widgets (You can add your own widgets as needed)
# Left-Hand Side Widgets
Label(LHS, bg="#f4f5f5").pack(pady=10)

# Right-Hand Side Widgets
Label(RHS,bg="#f4f5f5").pack(pady=10)

# Right-Hand Bottom Widgets
Label(RHB, bg="#f4f5f5").pack(pady=10)


#logo
photo=PhotoImage(file="Images/109613.png")
myimage=Label(LHS,image=photo,background="f4f5f5")

# Main loop to run the application
root.mainloop()
