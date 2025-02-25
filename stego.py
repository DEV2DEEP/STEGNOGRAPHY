import string
import tkinter as tk
from tkinter import *
import PIL.Image
from PIL import ImageTk,Image
import cv2
from tkinter import messagebox,ttk,filedialog,simpledialog
import os

global filename
global img
global sample
filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                               title="Select Image File", filetypes=(("All files","*.*"),("jpeg files", "*.jpg"), ("gif files", "*.gif*"), ("png files", "*.png")))
print(filename)
img1 = (Image.open(filename))
img = cv2.imread(filename) # Replace with the correct image path

msg = input("Enter a secret message:")
password = input("Enter the passcode:")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHENTIC ")
