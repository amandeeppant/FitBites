from customtkinter import *
import tkinter.messagebox as MessageBox

settings_page = CTk()
settings_page.title("Settings Page")
settings_page.geometry("400x400")
settings_page.resizable(False, False)

set_appearance_mode("Dark")
set_default_color_theme("dark-blue")

def toggle_theme():
    if settings_page._get_appearance_mode() == "Light":
        settings_page._set_appearance_mode("Dark")
    elif settings_page._get_appearance_mode()=="Dark":
        settings_page._set_appearance_mode("light")

def edit_profile():
    MessageBox.showinfo("Edit Profile", "Edit Profile functionality coming soon!")

def logout():
    MessageBox.showinfo("Logout", "Logged out successfully!")
    settings_page.destroy() 

settings_frame = CTkFrame(settings_page, fg_color="#2B2B2B", corner_radius=20) 
settings_frame.pack(pady=40, padx=20, fill="both", expand=True)

settings_title = CTkLabel(settings_frame, text="Settings", text_color="white", font=("Arial", 30, "bold"))
settings_title.pack(pady=20)

theme_btn = CTkButton(
    settings_frame, 
    text="Toggle Theme", 
    font=("Arial", 15, "bold"), 
    command=toggle_theme, 
    height=45, 
    width=200, 
    fg_color="#007BFF", 
    hover_color="#0056B3",  
    text_color="white"
)
theme_btn.pack(pady=15)

edit_profile_btn = CTkButton(
    settings_frame, 
    text="Edit Profile", 
    font=("Arial", 15, "bold"), 
    command=edit_profile, 
    height=45, 
    width=200, 
    fg_color="#007BFF",  
    hover_color="#0056B3",  
    text_color="white"
)
edit_profile_btn.pack(pady=15)

logout_btn = CTkButton(
    settings_frame, 
    text="Logout", 
    font=("Arial", 15, "bold"), 
    command=logout, 
    height=45, 
    width=200, 
    fg_color="#FF4C4C",  
    hover_color="#CC0000",  
    text_color="white"
)
logout_btn.pack(pady=15)

settings_page.mainloop()