# # Q1
# def get_age():
#     try:
#         age = int(input("Enter your age: "))
#         if age <= 0:
#             raise ValueError("Age must be a positive integer.")
#         print("Your age is:", age)
#     except ValueError as e:
#         print("Invalid input:", e)

# get_age()

# # Q2
# import math

# try:
#     number = float(input("Enter a number: "))
    
#     # Check if the number is negative
#     if number < 0:
#         raise ValueError("Cannot calculate square root of a negative number.")
    
#     square_root = math.sqrt(number)
#     print("The square root of", number, "is:", square_root)

# except ValueError as e:
#     print("Error:", e)


# # Q3
# try:
#     with open("data.txt", "r") as file:
#         content = file.read()
#         print("File content:")
#         print(content)
# except FileNotFoundError:
#     print("Error: The file 'data.txt' was not found.")


#  # Q4
# x = 50

# print("Initial Global x:", x)

# def outer_function():
#     y = 30
    
#     def inner_function():
#         x = 10
#         print("Inside inner_function - Local x:", x)
#         print("Inside inner_function - Enclosing y:", y)
        
#     inner_function()
#     print("Inside outer_function - Enclosing y:", y)

# outer_function()
# print("Outside functions - Global x:", x)


# # Q5
# from math import pow, sqrt

# a = 5
# b = 3

# result_pow = pow(a, b)
# result_sqrt = sqrt(a)

# print("The result of a^b is:", result_pow)
# print("The square root of a is:", result_sqrt)


# # Q6
# x = 10

# def outer_function():
#     x = 20
#     def inner_function():
#         global x
#         x = 30
#         print("Inside inner_function:", x)
#     inner_function()
#     print("Inside outer_function:", x)

# outer_function()
# print("Outside all functions:", x)


# # Q7
# def find_longest_line(filename):
#     with open(filename, "r") as file:
#         longest_line = ""
#         for line in file:
#             if len(line) > len(longest_line):
#                 longest_line = line
#     return longest_line.strip(), len(longest_line.strip())

# filename = "data.txt"
# longest_line, length = find_longest_line(filename)

# print("The longest line is:", longest_line)
# print("Length of the longest line:", length)


# Q8
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive.")
#         else:
#             self.balance += amount
#             print(f"Deposited: ${amount}. New balance: ${self.balance}")

#     def withdraw(self, amount):
#         try:
#             if amount > self.balance:
#                 raise ValueError("Insufficient balance for withdrawal.")
#             elif amount <= 0:
#                 print("Withdrawal amount must be positive.")
#             else:
#                 self.balance -= amount
#                 print(f"Withdrew: ${amount}. New balance: ${self.balance}")
#         except ValueError as e:
#             print(e)

#     def check_balance(self):
#         print(f"Current balance: ${self.balance}")

# account = BankAccount("John Doe", 100)  

# account.deposit(50)       
# account.withdraw(30)      
# account.withdraw(200)      
# account.check_balance()     


from customtkinter import *
from tkinter import Menu
from PIL import Image, ImageTk
import tkinter.messagebox as MessageBox

settings_page = CTk()
settings_page.title("Settings Page")
settings_page.geometry("500x500")
settings_page.resizable(False, False)

set_appearance_mode("Dark")
set_default_color_theme("dark-blue") 

username = "abcd"


def toggle_theme():
    if CTk.get_appearance_mode() == "Dark":        
        set_appearance_mode("Light")  
        bulb_label.configure(image=bulb_light)  
    else:
        set_appearance_mode("Dark")  
        bulb_label.configure(image=bulb_dark) 

def edit_profile():
    MessageBox.showinfo("Edit Profile", "Edit Profile functionality coming soon!")

def logout():
    MessageBox.showinfo("Logout", "You have been logged out.")
    settings_page.destroy()

def show_profile_menu(event):
    profile_menu.tk_popup(event.x_root, event.y_root)

settings_frame = CTkFrame(settings_page, fg_color="#2B2B2B", corner_radius=20)
settings_frame.pack(pady=20, padx=20, fill="both", expand=True)

profile_frame = CTkFrame(settings_frame, fg_color="#2B2B2B", corner_radius=10)
profile_frame.pack(pady=20, padx=20, fill="x")

profile_icon = Image.open("profile_icon.png").resize((50, 50))  
profile_icon = CTkImage(dark_image=profile_icon, size=(50, 50))  

profile_label = CTkLabel(profile_frame, text=f"{username}", text_color="white", font=("Arial", 18, "bold"))
profile_label.pack(side="left", padx=10)

profile_button = CTkLabel(profile_frame, image=profile_icon, text="")
profile_button.pack(side="right", padx=10)
profile_button.bind("<Button-1>", show_profile_menu) 

profile_menu = Menu(settings_page, tearoff=0, bg="#2B2B2B", fg="white", font=("Arial", 12))
profile_menu.add_command(label="Edit Profile", command=edit_profile)
profile_menu.add_separator()
profile_menu.add_command(label="Logout", command=logout)

settings_title = CTkLabel(settings_frame, text="Settings", text_color="white", font=("Arial", 30, "bold"))
settings_title.pack(pady=10)

bulb_frame = CTkFrame(settings_frame, fg_color="#2B2B2B", corner_radius=10)
bulb_frame.pack(pady=20, padx=20, fill="x")

bulb_light = Image.open("bulb_light.png").resize((50, 50)) 
bulb_light = CTkImage(dark_image=bulb_light, size=(50, 50))  

bulb_dark = Image.open("bulb_dark.png").resize((50, 50))  
bulb_dark = CTkImage(dark_image=bulb_dark, size=(50, 50))  

bulb_label = CTkLabel(bulb_frame, image=bulb_dark, text="")
bulb_label.pack(pady=10)
bulb_label.bind("<Button-1>", lambda event: toggle_theme()) 

logout_btn = CTkButton(
    settings_frame, 
    text="Logout", 
    font=("Arial", 15, "bold"), 
    command=logout, 
    height=45, 
    width=200, 
    fg_color="#FF4C4C", 
    hover_color="#CC0000"
)
logout_btn.pack(pady=30)

settings_page.mainloop()
