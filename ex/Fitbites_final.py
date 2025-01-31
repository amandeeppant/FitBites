import PIL.Image
import customtkinter as ctk
from customtkinter import *
from PIL import Image, ImageTk
import PIL
from datetime import datetime
from plyer import notification
import time
import tkinter.messagebox as MessageBox
import os
from tkinter import font
tracker_data=[]
def login():   #data check krna h and page change
    f= open("data","r")
    L=f.read().split()

    x=country_code.get()+'_'+phone_entry.get() + '^' + passwd_entry.get()
    f.close()
    for i in L:
        if x==i:
            after_login()
            break
        else:
            continue
    else:
        wrong_login_credentials()
    
    #pass

def agree_and_continue(): #data store krna h and page change krna h
    if (phone_entry.get()=='' or passwd_entry.get()==''):
        return fill_login()
    else:
        x=phone_entry.get()+ '^' + passwd_entry.get()
        f=open(f"{country_code.get() + '_'+ x}",'w')
        f.write(f"Account created at {datetime.now()}/")
        f.close()
        if len(x[0:10])!=10:
            os.remove(country_code.get()+'_'+ x)
            return invalid_credentials()
        else:
            f=open("data","a")
            f.write(f"{country_code.get()}_{x} ")
            f.close()
            start_page()

def fill_login():
    a=ctk.CTk()
    a.title("fill username and pass")
    a.geometry("500x600")
    a.maxsize(500,600)
    lbl=ctk.CTkLabel(a,text='Please fill username and \nand password both',font=("Arial",30,'bold'),fg_color='red',text_color='white')
    lbl.pack(pady=200)
    a.mainloop()
    pass

def invalid_credentials():
    a=ctk.CTk()
    a.title("Invalid_creds")
    a.geometry("500x600")
    a.maxsize(500,600)
    lbl=ctk.CTkLabel(a,text='The phone number entered\n by you is invalid',font=("Arial",30,'bold'),fg_color='red',text_color='white')
    lbl.pack(pady=200)
    a.mainloop()


def wrong_login_credentials():
    a=ctk.CTk()
    a.geometry("500x600")
    a.title("wrong_login_credentials")
    lbl=ctk.CTkLabel(a,text="Wrong Login Credentials",font=("Arial",30,'bold'),text_color='white')
    lbl.pack(pady=200)
    a.maxsize(500,600)
    a.mainloop()

    pass

def start_page(): #start page m hi details 1 and then  details 2 aayega

    def save():
        f=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'a')
        f.write(nam_entry.get() + '/' + gender_var.get()+'/'+ age_entry.get() + '/' + height_entry.get() + '/' + weight_entry.get()+'/'+ quote_entry.get()+'/')
        f.close()
        main.destroy()
        after_login()
    

    ctk.set_appearance_mode("dark") 
    ctk.set_default_color_theme("blue")  


    main = ctk.CTk()
    main.title("User Information")
    main.geometry("800x400")
    

    input_frame = ctk.CTkFrame(main, fg_color="#373737", bg_color="#373737", corner_radius=20)
    input_frame.pack(pady=20, padx=20, fill="both", expand=True)

    gender_var = ctk.StringVar(value="Select Gender")  
    gender_label = ctk.CTkLabel(input_frame, text="Gender:", font=("", 14))
    gender_label.grid(row=0, column=0, pady=10, padx=10)

    gender_option_menu = ctk.CTkOptionMenu(input_frame, variable=gender_var, values=["Male", "Female", "Other"])
    gender_option_menu.grid(row=0, column=1, pady=10, padx=10)

    age_label = ctk.CTkLabel(input_frame, text="Age:", font=("", 14))
    age_label.grid(row=1, column=0, pady=10, padx=10)

    age_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter Age")
    age_entry.grid(row=1, column=1, pady=10, padx=10)

    nam_label = ctk.CTkLabel(input_frame, text="Enter Name:", font=("", 14))
    nam_label.grid(row=2, column=0, pady=10, padx=10)

    nam_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter Name:")
    nam_entry.grid(row=2, column=1, pady=10, padx=10)

    height_label = ctk.CTkLabel(input_frame, text="Height (cm):", font=("", 14))
    height_label.grid(row=3, column=0, pady=10, padx=10)

    height_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter Height")
    height_entry.grid(row=3, column=1, pady=10, padx=10)

    weight_label = ctk.CTkLabel(input_frame, text="Weight (kg):", font=("", 14))
    weight_label.grid(row=4, column=0, pady=10, padx=10)

    weight_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter Weight")
    weight_entry.grid(row=4, column=1, pady=10, padx=10)

    #submit_btn = ctk.CTkButton(input_frame, text="Submit", command=save)
    #submit_btn.grid(row=5, column=1, columnspan=2, pady=20)

    quote_lbl=CTkLabel(input_frame, text='Write A Quote for\nYourself',font=('Georgia',28))
    quote_lbl.grid(row=2,column=15,padx=200)

    quote_entry=ctk.CTkEntry(input_frame, placeholder_text="Enter the quote here",font=('Arial',16),corner_radius=20)
    quote_entry.grid(row=4, column=15,padx=200)

    submit_btn = ctk.CTkButton(input_frame, text="Submit", command=save)
    submit_btn.grid(row=5, column=1, columnspan=2, pady=20)

    main.mainloop()

    

def greetings(x):
    #a=datetime.now().strftime('%H:%M:%S')
    f=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'r')
    a=(f.read().split('/'))[1]
    x=int(x)
    if 4<=x<12:
        return f"Good morning {a}!"
    elif 12<=x<16:
        return f"Good afternoon {a}!"
    elif 16<=x<24:
        return f"Good evening {a}!"
    elif 0<=x<4:
        return f"Good evening {a}!"
    
def after_login():
    global app
    
    app = ctk.CTk()

    app.title("Homepage")
    app.geometry("1100x500")  


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    global main_frame
    main_frame = ctk.CTkFrame(app, corner_radius=20)
    main_frame.pack(pady=30, padx=20, fill="both", expand=True)

    #bg=PhotoImage(file="Homepage1.png")
    #bg_lbl=ctk.CTkLabel(main_frame ,image=bg)
    #bg_lbl.place(x=0,y=0)
    greetings_lbl=ctk.CTkLabel(main_frame, text=greetings((datetime.now().strftime('%H:%M:%S'))[:2]), font=('Georgia',30),bg_color="#2B2B2B")
    greetings_lbl.place(x=10,y=10)
    print(greetings)


    time_label = ctk.CTkLabel(main_frame, text=datetime.now().strftime("%H:%M"), font=("cosmic sans ms", 40), bg_color="#2B2B2B")
    time_label.pack(pady=(30, 5))


    date_label = ctk.CTkLabel(main_frame, text=datetime.now().strftime("%A, %d %B"), font=("Arial", 16), bg_color="#2B2B2B")
    date_label.pack()


    def update_time():
        time_label.configure(text=datetime.now().strftime("%H:%M"))
        date_label.configure(text=datetime.now().strftime("%A, %d %B"))
        app.after(1000, update_time)


    icons_frame = ctk.CTkFrame(main_frame, fg_color="transparent",bg_color="#2B2B2B")
    icons_frame.pack(pady=30)
    
    #bg_lbl=ctk.CTkLabel(icons_frame ,image=bg)
    #bg_lbl.place(x=0,y=0)


    icons = ["🕒\nReminder", "👽\nTracker", "🏋‍♂\nExercises", "🍉\nDiet planner","📈\nYour Progress",'🧠\nMental Health', "⚙️\nSettings"]  
    commands=[reminder,tracker,exercises,diet_planner,see_your_progress,mental_health,settings]

    for i, icon_text in enumerate(icons):
        icon_button = ctk.CTkButton(
            icons_frame, 
            text=icon_text,
            width=60, height=60,
            corner_radius=15,
            font=("Arial", 20),
            fg_color="white",
            text_color="black",
            hover_color="lightgray",
            border_color="#FFFFFF",
            border_width=1,
            bg_color="#2B2B2B",
            command=commands[i]
        )
        icon_button.grid(row=0, column=i, padx=10)
    fi=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'r')
    b=fi.read().split('/')
    fi.close()
    #custom_font = font.Font(family='Arial', size=14, weight="bold", slant="italic")
    quote_show=ctk.CTkLabel(main_frame, text=b[6], font=('Arial',22,"italic"))
    quote_show.pack(pady=30)

    update_time()
    app.mainloop()
    
    

def settings():   #logout, change theme to dark or light
    settings_page = CTk()
    settings_page.title("Settings Page")
    settings_page.geometry("600x600")
    settings_page.resizable(False, False)

    set_appearance_mode("Dark")
    set_default_color_theme("dark-blue")

    def toggle_theme():
        if app._get_appearance_mode() == "Light":
            main_frame._set_appearance_mode("Dark")
            app._set_appearance_mode("Dark")
        else:
            main_frame._set_appearance_mode('Light')
            app._set_appearance_mode("light")

    def edit_profile():
        def save():
            f=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'r')
            l=f.read().split('/')
            f.close()
            l[1]=name_edit.get()
            l[2]=gender_edit.get()
            l[3]=age_edit.get()
            l[4]=ht_edit.get()
            l[5]=wt_edit.get()
            l[6]=Tht_edit.get()
            s=''
            for i in l:
                s=s+i+"/"


            f=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'w')
            f.write(s)
            f.close()
            b.destroy()
            MessageBox.showinfo("Edit Profile", "Profile Updated")
            
        b=ctk.CTk()
        b.geometry('900x500')
        b.title("Edit Profile")
        name_edit=ctk.CTkEntry(b,placeholder_text="Enter Name")
        name_edit.pack(pady=15)

        age_edit=ctk.CTkEntry(b,placeholder_text="Enter age")
        age_edit.pack(pady=15)

        gender_edit=ctk.CTkEntry(b,placeholder_text="Enter Gender")
        gender_edit.pack(pady=15)

        ht_edit=ctk.CTkEntry(b,placeholder_text="Enter Height")
        ht_edit.pack(pady=15)

        wt_edit=ctk.CTkEntry(b,placeholder_text="Enter Weight")
        wt_edit.pack(pady=15)

        Tht_edit=ctk.CTkEntry(b,placeholder_text="Enter Quote")
        Tht_edit.pack(pady=15)

        submit=ctk.CTkButton(b, text="Submit",corner_radius=20,command=save)
        submit.pack(pady=15)

    
        b.mainloop()

    def logout():
        MessageBox.showinfo("Logout", "Logged out successfully!")
        settings_page.destroy() 
        app.destroy()

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
    pass

def see_your_progress():
    f=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'r')
    l=f.read().split('&')
    f.close()
    b=''
    for i in range(1,len(l)):
        b=b+l[i]+'\n'


    a=ctk.CTk()
    a.geometry("1200x1200")
    a.title("Your Progress Report")
    

    #pr_lbl=CTkLabel(a,text=f"Title: {l[1]}\nActivity: {l[2]}\nStart Time: {l[3]}\nDuration: {l[4]}")
    tp_label=CTkLabel(a,text='YOUR PROGRESS REPORT',font=("Georgia",30))
    tp_label.pack(pady=40)
    pr_lbl=CTkLabel(a,text=b, font=('cosmic sans ms',18))
    pr_lbl.pack()
    a.mainloop()
    pass

    
def tracker():    #track food intake, water intake, nutrients intake, vitamins, carbohyfrates, protein record for workout
    f=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'a')
    f.close()
    def save_track():
        f=open(country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(),'a')
        #f.write("\n&Date     Title     Activity     Start      Duration")
        f.write(f"\n&    Title:  {title_entry.get()}&      Activity:  {act_entry.get()}&      Start:  {start_time.get()}&      Duration:  {dur.get()}")
        f.close()
        MessageBox.showinfo('Fitbites',"Progress Saved")
        app.destroy()
    
    app=ctk.CTk()
    app.geometry("900x600")
    app.title("Tracker")

    main_lbl=ctk.CTkLabel(app, text="Track Your Progress",font=("Georgia",30))
    main_lbl.pack(pady=50)

    date_entry=CTkEntry(app, placeholder_text="Date", text_color="grey")
    date_entry.pack(pady=20)

    title_entry=ctk.CTkEntry(app, placeholder_text="Title", text_color="grey")
    title_entry.pack(pady=20)

    act_entry=ctk.CTkEntry(app, placeholder_text="Activity")
    act_entry.pack(pady=20)

    start_time=ctk.CTkEntry(app, placeholder_text="Start time",text_color="grey")
    start_time.pack(pady=20)

    dur=ctk.CTkEntry(app, placeholder_text="Duration",text_color="grey")
    dur.pack(pady=20)

    save_button=ctk.CTkButton(app, text="Save Your Progress", font=('Arial',14),command=save_track)
    save_button.pack(pady=30)

    app.mainloop()

def mental_health():
    def journal():

        def write_journal():
            def save_journal():
                content = journal_entry.get("1.0", "end").strip()
                if content:
                    with open("journal"+country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get(), "a") as file:
                        file.write((datetime.now().strftime("%D:%M:%Y")[0:8:]+' '+content) + "\n" + "-"*50 + "\n")
                    MessageBox.showinfo("Saved", "Your journal entry has been saved!")
                    journal_entry.delete("1.0", "end")
                else:
                    MessageBox.showwarning("Empty Entry", "Journal entry cannot be empty.")

            app = ctk.CTk()
            app.title("Journal")
            app.geometry("800x600")
            app.configure(fg_color="#1e1e2f")  

            header = ctk.CTkLabel(
                app, 
                text="Your Daily Journal", 
                font=ctk.CTkFont(size=24, weight="bold"), 
                text_color="#5ac0ff"
            )
            header.pack(pady=20)

            journal_entry = ctk.CTkTextbox(
                app, 
                font=ctk.CTkFont(size=14), 
                fg_color="#121212", 
                text_color="#ffffff", 
                border_width=2,
                border_color="#5ac0ff",
                corner_radius=10
            )
            journal_entry.pack(expand=True, fill="both", padx=20, pady=10)

            save_button = ctk.CTkButton(
                app, 
                text="Save", 
                font=ctk.CTkFont(size=14, weight="bold"), 
                fg_color="#5ac0ff", 
                hover_color="#3f8dbd", 
                text_color="#ffffff", 
                command=save_journal
            )
            save_button.pack(pady=20)

            app.mainloop()



        def create_journal_entry_widget(parent, entry):
            lines = entry.split("\n")
            #date = lines[-1] if lines else "Unknown Date"
            preview_text = lines[0][:15] + "..." if len(lines) > 0 else "No Content"

        
            entry_button = ctk.CTkButton(
                parent, 
                text=f"{preview_text}\n",
                font=ctk.CTkFont(size=14), 
                fg_color="#121212", 
                text_color="#5ac0ff", 
                hover_color="#3f8dbd", 
                command=lambda: view_full_entry(entry)
            )
            entry_button.pack(fill="x", pady=5, padx=5)


        def view_full_entry(entry):
            c=ctk.CTk()
            c.geometry("900x600")
            c.title("Your Journal")
            heading_lbl=ctk.CTkLabel(c,text=entry[0:8:],font=("Georgia",30))
            heading_lbl.pack(pady=50)

            body=CTkLabel(c,text=entry,font=("Arial",13))
            body.pack(pady=10)
            c.mainloop()
            

        journal_page = ctk.CTkToplevel()
        journal_page.title("Journal Entries")
        journal_page.geometry("800x600")
        journal_page.configure(fg_color="#1e1e2f")

            
        header_frame = ctk.CTkFrame(journal_page, fg_color="#1e1e2f")
        header_frame.pack(fill="x", pady=10, padx=10)

            
        header_label = ctk.CTkLabel(
            header_frame, 
            text="Your Journals", 
            font=ctk.CTkFont(size=24, weight="bold"), 
            text_color="#5ac0ff"
            )
        header_label.pack(side="left", padx=10)

        
        write_button = ctk.CTkButton(
            header_frame, 
            text="+ Write", 
            font=ctk.CTkFont(size=14, weight="bold"), 
            fg_color="#5ac0ff", 
            hover_color="#3f8dbd", 
            text_color="#ffffff", 
            command=write_journal 
        )
        write_button.pack(side="right", padx=10)

            
        scrollable_frame = ctk.CTkScrollableFrame(
            journal_page, 
            fg_color="#121212", 
            corner_radius=10, 
            width=760, 
            height=480
        )
        scrollable_frame.pack(pady=10, padx=20, expand=True, fill="both")


        journal_file = "journal"+country_code.get()+ '_' + phone_entry.get()+'^'+passwd_entry.get()
        if os.path.exists(journal_file):
            with open(journal_file, "r") as f:
                entries = f.read().strip().split("\n" + "-" * 50 + "\n")
                for entry in entries:
                    if entry.strip():
                        create_journal_entry_widget(scrollable_frame, entry)
        else:
                
            no_entry_label = ctk.CTkLabel(
                scrollable_frame, 
                text="No journal entries found.", 
                font=ctk.CTkFont(size=16), 
                text_color="#5ac0ff"
                )
            no_entry_label.pack(pady=20)

        journal_page.mainloop()
        



    app = ctk.CTk()
    app.title("Mental Health Support")
    app.geometry("800x600")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    bg_frame = ctk.CTkFrame(app, fg_color="#2e2e2e", corner_radius=0)
    bg_frame.pack(fill="both", expand=True)

    header = ctk.CTkLabel(
        bg_frame,
        text="Your Mental Health Matters 🧠",
        font=("Arial", 28, "bold"),
        text_color="#4a90e2"
    )
    header.pack(pady=20)

    subheading = ctk.CTkLabel(
        bg_frame,
        text="We're here to provide resources, support, and care for your mental well-being.",
        font=("Arial", 16),
        text_color="#b0b0b0"
    )
    subheading.pack(pady=10)

    info_frame = ctk.CTkFrame(bg_frame, fg_color="#3a3a3a", corner_radius=15)
    info_frame.pack(pady=20, padx=30, fill="x")

    info_text = ctk.CTkLabel(
        info_frame,
        text=(
            "Mental health is just as important as physical health. Taking care of your mind helps you "
            "stay focused, positive, and balanced. Explore ways to manage stress, improve your mindset, "
            "and seek help when needed."
        ),
        font=("Arial", 14),
        text_color="#d1d1d1",
        wraplength=700,
        anchor="w",
        justify="left"
    )
    info_text.pack(padx=20, pady=20)

    button_frame = ctk.CTkFrame(bg_frame, fg_color="#2e2e2e")
    button_frame.pack(pady=20)

    resource_button1 = ctk.CTkButton(
        button_frame,
        text="Journalism and Gratitude ",
        font=("Arial", 16),
        fg_color="#4a90e2",
        hover_color="#357ABD",
        command=journal
    )
    resource_button1.pack(pady=10, padx=20)

    resource_button2 = ctk.CTkButton(
        button_frame,
        text="Motivational Quotes",
        font=("Arial", 16),
        fg_color="#4a90e2",
        hover_color="#357ABD",
        command=motivation_quotes
    )
    resource_button2.pack(pady=10, padx=20)

    resource_button3 = ctk.CTkButton(
        button_frame,
        text=" Meditation and Breathing Exercises ",
        font=("Arial", 16),
        fg_color="#4a90e2",
        hover_color="#357ABD",
        command=lambda: print("Navigating to Daily Affirmations...")
    )
    resource_button3.pack(pady=10, padx=20)

    footer = ctk.CTkLabel(
        bg_frame,
        text="Remember: Seeking help is a sign of strength, not weakness.",
        font=("Arial", 12, "italic"),
        text_color="#888"
    )
    footer.pack(side="bottom", pady=20)

    app.mainloop()
    pass
def motivation_quotes():
    quotes = ["Believe you can, and you're halfway there. – Theodore Roosevelt",
        "You are braver than you believe, stronger than you seem, and smarter than you think. – A.A. Milne",
        "Dream big, start small, act now. – Robin Sharma",
        "Every day is a second chance.",
        "Doubt kills more dreams than failure ever will. – Suzy Kassem",
        "Don’t be pushed by your problems; be led by your dreams. – Ralph Waldo Emerson",
        "Your potential is endless. Go do what you were created to do.",
        "Small steps in the right direction can turn out to be the biggest steps of your life.",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
        "The way to get started is to quit talking and begin doing. – Walt Disney"
        "Gratitude turns what we have into enough. – Anonymous",
        "Start each day with a grateful heart.",
        "Happiness is not by chance, but by choice. – Jim Rohn",
        "The more you praise and celebrate your life, the more there is in life to celebrate. – Oprah Winfrey",
        "Take time to do what makes your soul happy.",
        "A grateful heart is a magnet for miracles.",
        "Joy is what happens to us when we allow ourselves to recognize how good things really are. – Marianne Williamson",
        "Every sunset brings the promise of a new dawn. – Ralph Waldo Emerson",
        "Enjoy the little things, for one day you may look back and realize they were the big things. – Robert Brault",
        "Keep your face to the sunshine, and you cannot see a shadow. – Helen Keller"
        "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
        "The struggle you’re in today is developing the strength you need for tomorrow.",
        "Rise above the storm, and you will find the sunshine. – Mario Fernandez",
        "Fall seven times, stand up eight. – Japanese Proverb",
        "Turn your wounds into wisdom. – Oprah Winfrey",
        "Don’t limit your challenges; challenge your limits.",
        "Even the darkest night will end, and the sun will rise. – Victor Hugo",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "It always seems impossible until it’s done. – Nelson Mandela",
        "When you feel like quitting, think about why you started."
        "Believe in yourself and all that you are.",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Don’t watch the clock; do what it does. Keep going.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "Dream big and dare to fail.",
        "Act as if what you do makes a difference. It does.",
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "Perseverance is not a long race; it is many short races one after the other.",
        "Opportunities don't happen, you create them.",
        "Hardships often prepare ordinary people for an extraordinary destiny.",
        "Success usually comes to those who are too busy to be looking for it.",
        "Don’t stop when you’re tired. Stop when you’re done.",
        "If you can dream it, you can do it.",
        "Success is not how high you have climbed, but how you make a positive difference to the world.",
        "Motivation is what gets you started. Habit is what keeps you going.",
        "The best way to get started is to quit talking and begin doing.",
        "The road to success and the road to failure are almost exactly the same.",
        "Don't be afraid to give up the good to go for the great.",
        "I find that the harder I work, the more luck I seem to have.",
        "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
        "Your limitation—it’s only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn’t just find you. You have to go out and get it.",
        "The harder you work, the luckier you get.",
        "It’s not whether you get knocked down. It’s whether you get up.",
        "You learn more from failure than from success. Don’t let it stop you.",
        "Do something today that your future self will thank you for.",
        "Little things make big days.",
        "Go as far as you can see; when you get there, you’ll be able to see further.",
        "Your only limit is your mind.",
        "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
        "The key to success is to focus on goals, not obstacles.",
        "Dream bigger. Do bigger.",
        "You don’t have to be great to start, but you have to start to be great.",
        "Do what you can with all you have, wherever you are.",
        "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.",
        "I never dreamed about success. I worked for it.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Don’t let yesterday take up too much of today.",
        "People who are crazy enough to think they can change the world are the ones who do.",
        "Knowing is not enough; we must apply. Wishing is not enough; we must do.",
        "Imagine your life is perfect in every respect; what would it look like?",
        "We generate fears while we sit. We overcome them by action.",
        "Whether you think you can or think you can’t, you’re right.",
        "Security is mostly a superstition. Life is either a daring adventure or nothing.",
        "Innovation distinguishes between a leader and a follower.",
        "Happiness is not something ready-made. It comes from your own actions.",
        "Don’t wait for opportunity. Create it.",
        "Success seems to be connected with action. Successful people keep moving.",
        "Don’t be afraid to fail. Be afraid not to try.",
        "The best way to predict the future is to create it."
    ]


    quotes_page = ctk.CTk()
    quotes_page.title("Motivational Quotes")
    quotes_page.geometry("1150x600")
    quotes_page.configure(fg_color="#1e1e2f")  # Dark background

        # Header
    header = ctk.CTkLabel(
        quotes_page, 
        text="Motivational Quotes", 
        font=ctk.CTkFont(size=24, weight="bold"), 
        text_color="#5ac0ff"
    )
    header.pack(pady=20)

    # Scrollable Frame for Quotes
    scrollable_frame = ctk.CTkScrollableFrame(
        quotes_page, 
        fg_color="#121212", 
        corner_radius=10, 
        width=1150, 
        height=480
    )
    scrollable_frame.pack(pady=10, padx=20, expand=True, fill="both")

        # Display Quotes in the Scrollable Frame
    for i, quote in enumerate(quotes, start=1):
        quote_label = ctk.CTkLabel(
            scrollable_frame, 
            text=f"{i}. {quote}", 
            font=ctk.CTkFont(size=14), 
            text_color="#ffffff", 
            anchor="w",  # Align text to the left
            wraplength=1150  # Wrap text to fit frame width
        )
        quote_label.pack(fill="x", pady=5, padx=10)

    quotes_page.mainloop()



def exercises():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def show_feature_page(feature_name):
        feature_window = ctk.CTkToplevel(main)
        feature_window.title(feature_name)
        feature_window.geometry("400x600")  # Adjusted height to accommodate the image
        feature_window.configure(bg_color="#3E3E3E")

        if feature_name == "Weight Gain":
            show_workout_level_selector(feature_window)

    def show_workout_level_selector(feature_window):
        workout_level_label = ctk.CTkLabel(feature_window, text="Select your workout level:", font=("Arial", 14), text_color="white")
        workout_level_label.pack(pady=10)

        workout_level = ctk.StringVar(value="")

        beginner_radio = ctk.CTkRadioButton(feature_window, text="Beginner", variable=workout_level, value="Beginner", font=("Arial", 12), text_color="white")
        beginner_radio.pack(pady=5)

        advanced_radio = ctk.CTkRadioButton(feature_window, text="Advanced", variable=workout_level, value="Advanced", font=("Arial", 12), text_color="white")
        advanced_radio.pack(pady=5)

        submit_btn = ctk.CTkButton(feature_window, text="Submit", font=("Arial", 15), height=40, width=250, 
                                fg_color="black", text_color="white", command=days)
        submit_btn.pack(pady=20)

        try:
            img = Image.open("workout.jpg")  # Make sure the image is in the same directory
            img = img.resize((300, 400))  # Resize the image to fit
            img = ImageTk.PhotoImage(img)
            img_label = ctk.CTkLabel(feature_window, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack(pady=20)  # Add padding to keep it below the submit button
        except Exception as e:
            print(f"Error loading image: {e}")

        feature_window.lift()
        feature_window.attributes('-topmost', True)


    main = ctk.CTk()
    main.title("Exercises")
    main.geometry("500x600")
    main.configure(bg_color="#3E3E3E")

    menu_frame = ctk.CTkFrame(main, fg_color="#3E3E3E", bg_color="#3E3E3E", corner_radius=20)
    menu_frame.pack(pady=20, padx=20, fill="both", expand=True)

    title_label = ctk.CTkLabel(menu_frame, text="Exercises", font=("Georgia", 24, "bold"), text_color="white")
    title_label.pack(pady=40)

    features = ["Weight Gain", "Weight Loss", "Flexibility", "Basic Exercises"]

    for feature in features:
        button = ctk.CTkButton(menu_frame, text=feature, font=("Arial", 15), height=40, width=250,
                            fg_color="black", text_color="white", cursor="hand2", 
                            command=lambda f=feature: show_feature_page(f))
        button.pack(pady=10)

    main.mainloop()

def reminder():   #water reminder, mealreminder, any other reminder if set by the user   *DONE*
    


    def sleep_reminder(alarm_time='22:00:00',n='Sleep reminder'):
        while True:
            # abhi ka time
            current_time = datetime.now().strftime("%H:%M:%S")
            #print("Current time:", current_time)

            # Check if current time matches the alarm time
            if current_time == alarm_time:
                notification.notify(
                    title=n,
                    message="Time for bed",
                    timeout=15  #notif k jane ka time in seconds
                )
                break
            time.sleep(1)

    def water_reminder(alarm_time=['22:00:00','21:00:00','20:00:00','19:00:00','18:00:00',
                                '17:00:00','16:00:00','15:00:00','14:00:00','13:00:00',
                                '12:00:00','11:00:00','10:00:00','09:00:00','08:00:00'],n='Water reminder'):
        while True:
            # abhi ka time
            current_time = datetime.now().strftime("%H:%M:%S")
           # print("Current time:", current_time)

            # Check if current time matches the alarm time
            if current_time in alarm_time:
                notification.notify(
                    title=n,
                    message="Time for a glass of water💧💧💧",
                    timeout=15  #notif k jane ka time in seconds
                )
                break
            time.sleep(1)

    def set_alarm():
        MessageBox.showinfo("FITBITES", f'Reminder for {custom_reminder_entry.get()} has been set.')
        while True:
            # abhi ka time
            current_time = datetime.now().strftime("%H:%M:%S")
           # print("Current time:", current_time)

            # Check if current time matches the alarm time
            if current_time == cust_time.get():
                notification.notify(
                    title='FITBITES',
                    message=f"{custom_reminder_entry.get()}",
                    timeout=15  #notif k jane ka time in seconds
                )
                break
            time.sleep(1)


    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("blue") 

    
    root = ctk.CTk()
    root.title("Reminder Page")
    root.geometry("900x400")

    title_label = ctk.CTkLabel(root, text="REMINDER FOR YOURSELF", font=("Arial", 24))
    title_label.pack(pady=15)

    default_reminder1 = ctk.CTkButton(root, text="Set sleep reminder",command=sleep_reminder)
    default_reminder1.pack(pady=15)

    default_reminder2 = ctk.CTkButton(root, text="Set water reminder",command=water_reminder)
    default_reminder2.pack(pady=15)


    title_label2 = ctk.CTkLabel(root, text="SET CUSTOM REMINDER", font=("Arial", 19))
    title_label2.pack(pady=15)

    custom_reminder_entry = ctk.CTkEntry(root, placeholder_text="Custom Reminder Name")
    custom_reminder_entry.pack(pady=10)

    cust_time=ctk.CTkEntry(root, placeholder_text="Enter time in HH:MM:SS format")
    cust_time.pack(pady=5)
    set_rem_button=ctk.CTkButton(root, text="Set Reminder",command=set_alarm)
    set_rem_button.pack()


    root.mainloop()
    pass

def diet_planner():  #all vitamins, nutrients, calories, protien, etc planner according to user's workout and meal that one should take before and after workout
    pass

def workout_planner():   #exercises, and details about it
    pass

def days():


    app=ctk.CTk()
    app.geometry('900x600')
    app.title("Days")

    hedding_lbl=ctk.CTkLabel(app, text="Your workout Plans for 7 days",font=("Georgia", 30))
    hedding_lbl.pack(pady=40)

    day1_but=ctk.CTkButton(app, text="Day 1", command=day1)
    day1_but.pack(pady=20)

    day2_but=ctk.CTkButton(app, text="Day 2", command=day2)
    day2_but.pack(pady=20)

    day3_but=ctk.CTkButton(app, text="Day 3", command=day3)
    day3_but.pack(pady=20)

    day4_but=ctk.CTkButton(app, text="Day 4", command=day4)
    day4_but.pack(pady=20)

    day5_but=ctk.CTkButton(app, text="Day 5", command='')
    day5_but.pack(pady=20)

    day6_but=ctk.CTkButton(app, text="Day 6", command='')
    day6_but.pack(pady=20)

    day7_but=ctk.CTkButton(app, text="Day 7", command='')
    day7_but.pack(pady=20)


    app.mainloop()
    pass

def day1():
    app = ctk.CTk()
    app.title("Weight Gain - Day 1: Upper Body")
    app.geometry("900x700")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Main Frame
    main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
    main_frame.pack(fill="both", expand=True)

    # Header
    header = ctk.CTkLabel(
        main_frame,
        text="Day 1: Upper Body (Push Focus) 🏋️‍♂️",
        font=("Arial", 28, "bold"),
        text_color="#00aaff"
    )
    header.pack(pady=10)

    # Scrollable Frame
    scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
    scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

    def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
        # Title for the section
        title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
        title_label.pack(anchor="w", padx=20, pady=(10, 5))

        # Content for the section
        content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
        content_label.pack(anchor="w", padx=20, pady=5)

    # Exercise 1: Barbell Bench Press
    exercise1_title = ctk.CTkLabel(
        scrollable_frame,
        text="1. Barbell Bench Press",
        font=("Arial", 22, "bold"),
        text_color="#00aaff"  
    )
    exercise1_title.pack(pady=10)

    exercise1_img = Image.open("barbell.jpg")  
    exercise1_img = exercise1_img.resize((700, 300))
    exercise1_photo = ImageTk.PhotoImage(exercise1_img)

    exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
    exercise1_image_label.pack(pady=10)

    create_section(
        scrollable_frame,
        "WHAT IS THE BARBELL BENCH PRESS?",
        """
    The Barbell Bench Press is a classic strength training exercise that primarily targets the chest (pectoralis major), while also engaging the shoulders (deltoids) and triceps. It’s a compound movement involving multiple joints and muscle groups, making it ideal for building upper body strength and muscle mass. The exercise is commonly used by athletes and bodybuilders alike to develop pressing strength and power.
    """
    )

    create_section(
        scrollable_frame,
        "HOW TO PERFORM THE BARBELL BENCH PRESS",
        """
    1. SET UP THE BENCH AND BARBELL

    - Position the Bench: Place the bench in the middle of the rack with the barbell directly above your chest when lying down. Ensure your head, shoulders, and hips remain flat on the bench.
    - Adjust the Barbell: Set the barbell at chest height. Check that it’s evenly loaded with weights on both sides and secured with collars.



    2. PROPER FORM

    - Grip: Place your hands on the barbell slightly wider than shoulder-width apart. Keep your grip firm but not excessively tight.
    - Elbow Position: Keep your elbows at a 45-degree angle to your torso. Do not let them flare out too much to avoid shoulder strain.
    - Pressing the Barbell: Push the barbell upward, extending your arms fully, but do not lock your elbows.



    3. EXECUTING THE LIFT

    - Lowering the Barbell: Slowly lower the barbell to your chest, keeping your elbows at a 45-degree angle.
    - Push Through the Chest: Push the barbell back to the starting position, focusing on using your chest muscles rather than your shoulders or triceps.
    """
    )

    create_section(
        scrollable_frame,
        "IMPORTANT TIPS FOR THE BARBELL BENCH PRESS",
        """
    - Keep your core tight throughout the exercise to protect your lower back.
    - Make sure your feet are flat on the ground for stability.
    - Control the weight and avoid bouncing the bar off your chest.
    """
    )

    # Exercise 2: Dumbbell Shoulder Press
    exercise2_title = ctk.CTkLabel(
        scrollable_frame,
        text="2. Dumbbell Shoulder Press",
        font=("Arial", 22, "bold"),
        text_color="#00aaff"  
    )
    exercise2_title.pack(pady=10)

    exercise2_img = Image.open("dumbell.jpg")  
    exercise2_img = exercise2_img.resize((700, 500))
    exercise2_photo = ImageTk.PhotoImage(exercise2_img)

    exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
    exercise2_image_label.pack(pady=10)

    create_section(
        scrollable_frame,
        "WHAT IS THE DUMBBELL SHOULDER PRESS?",
        """
    The Dumbbell Shoulder Press (also known as the Overhead Dumbbell Press) is an upper body exercise that primarily targets the deltoid muscles (shoulders). It also works the triceps and upper chest. This exercise is highly effective for building shoulder strength and muscle mass. By performing this exercise with dumbbells, you get the added benefit of working each shoulder independently, ensuring balanced development.
    """
    )

    create_section(
        scrollable_frame,
        "HOW TO PERFORM THE DUMBBELL SHOULDER PRESS CORRECTLY",
        """
    1. SET UP THE POSITION

    - Start Position: Sit on a bench with back support (or stand if you prefer). Keep your feet flat on the ground for stability.
    - Grab the Dumbbells: Hold a dumbbell in each hand and position them at shoulder height, with your palms facing forward and elbows bent at about 90 degrees. Ensure your elbows are slightly in front of your body, not flared out to the sides.



    2. PRESS THE DUMBBELLS UP

    - Engage Your Core: Tighten your core and keep your back straight throughout the movement to prevent arching your lower back.
    - Press the Dumbbells: Push both dumbbells upward, extending your arms fully but not locking your elbows. The dumbbells should travel in a straight line overhead, and your palms should remain facing forward.



    3. LOWER THE DUMBBELLS

    - Controlled Descent: Slowly lower the dumbbells back to shoulder height, maintaining control over the weights. Your elbows should bend to about 90 degrees again.
    - Keep the Elbows Close: Avoid letting your elbows flare out excessively to the sides. Keep them slightly in front of your body.
    """
    )

    create_section(
        scrollable_frame,
        "FORM AND TECHNIQUE TIPS:",
        """
    - Core Engagement: Keep your core tight to avoid arching your lower back.
    - Head Position: Keep your head in a neutral position (don’t tilt it back too much as you press the weights up).
    - Avoid Excessive Weight: Use a weight that you can control with good form. Pressing too heavy can cause poor technique, which could lead to injury.
    - Breathing: Inhale as you lower the dumbbells and exhale as you press them up.
    """
    )

    # Exercise 3: Incline Dumbbell Press
    exercise3_title = ctk.CTkLabel(
        scrollable_frame,
        text="3. Incline Dumbbell Press",
        font=("Arial", 22, "bold"),
        text_color="#00aaff"  
    )
    exercise3_title.pack(pady=10)

    exercise3_img = Image.open("face.jpg")  
    exercise3_img = exercise3_img.resize((700, 300))
    exercise3_photo = ImageTk.PhotoImage(exercise3_img)

    exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
    exercise3_image_label.pack(pady=10)

    create_section(
        scrollable_frame,
        "WHAT IS THE INCLINE DUMBBELL PRESS?",
        """
    The Incline Dumbbell Press is a variation of the traditional chest press that targets the upper part of the chest (clavicular head of the pectorals). It also works the shoulders and triceps. This exercise is great for building upper chest strength and definition. The incline angle places less strain on the shoulder joints and focuses more on the upper chest muscles.
    """
    )

    create_section(
        scrollable_frame,
        "HOW TO PERFORM THE INCLINE DUMBBEL PRESS CORRECTLY",
        """
    1. SET UP THE INCLINE BENCH AND DUMBBELLS

    - Set the bench to an incline angle of about 30-45 degrees. Sit down and hold a dumbbell in each hand.
    - Rest the dumbbells on your thighs before lying back on the bench.



    2. STARTING POSITION

    - Hold the Dumbbells: Start with the dumbbells resting at shoulder height, palms facing forward, elbows bent at about 90 degrees.



    3. LIFTING AND LOWERING THE DUMBBELLS

    - Press the Dumbbells: Push the dumbbells up, extending your arms fully. Keep your elbows slightly bent at the top of the movement.
    - Lower the Dumbbells: Slowly lower the dumbbells back to the starting position, maintaining control.
    """
    )

    create_section(
        scrollable_frame,
        "TIPS FOR THE INCLINE DUMBBELL PRESS",
        """
    - Maintain Control: Always lower the dumbbells with control. Avoid using momentum to press the weights up.
    - Elbow Angle: Keep your elbows slightly in front of your body, not flared out at a 90-degree angle.
    - Feet Placement: Keep your feet flat on the ground to ensure stability.
    """
    )

    # Exercise 4: Dumbbell Lateral Raise
    exercise4_title = ctk.CTkLabel(
        scrollable_frame,
        text="4. Dumbbell Lateral Raise",
        font=("Arial", 22, "bold"),
        text_color="#00aaff"  
    )
    exercise4_title.pack(pady=10)

    exercise4_img = Image.open("lateral.jpg")  
    exercise4_img = exercise4_img.resize((700, 300))
    exercise4_photo = ImageTk.PhotoImage(exercise4_img)

    exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
    exercise4_image_label.pack(pady=10)

    create_section(
        scrollable_frame,
        "WHAT IS THE DUMBBELL LATERAL RAISE?",
        """
    The Dumbbell Lateral Raise is an isolation exercise that primarily targets the lateral (middle) head of the deltoid muscles in the shoulders. This exercise helps to increase shoulder width and improve the overall appearance of the upper body. It's an effective movement to sculpt and strengthen the shoulders for better performance in overhead pressing exercises.
    """
    )

    create_section(
        scrollable_frame,
        "HOW TO PERFORM THE DUMBBELL LATERAL RAISE",
        """
    1. SET UP THE POSITION

    - Stand tall with your feet hip-width apart, holding a dumbbell in each hand by your sides, palms facing inward.
    - Keep your knees slightly bent and your core engaged to maintain balance.



    2. LATERAL RAISE MOTION

    - Lift the Dumbbells: Raise both dumbbells out to the sides, keeping a slight bend in your elbows. Your arms should be parallel to the floor at the top of the movement. 
    - Don't Swing: Avoid swinging the dumbbells using momentum. Control the movement both on the way up and down.



    3. LOWER THE DUMBBELLS

    - Lower the dumbbells slowly back to the starting position, maintaining control and not letting them drop quickly.
    """
    )

    create_section(
        scrollable_frame,
        "TIPS FOR THE DUMBBELL LATERAL RAISE",
        """
    - Elbow Position: Keep your elbows slightly bent throughout the movement.
    - Don't Use Momentum: Focus on using the shoulder muscles to lift the dumbbells instead of relying on momentum or swinging.
    - Control the Descent: Lower the dumbbells slowly to maximize muscle engagement.
    """
    )

    # Exercise 5: Triceps Dips

    exercise5_title = ctk.CTkLabel(
        scrollable_frame,
        text="5. Triceps Dips",
        font=("Arial", 22, "bold"),
        text_color="#00aaff")
    exercise5_title.pack(pady=10)

    # Parallel Bar Triceps Dips
    parallel_bar_image = Image.open("tricep.jpg")  
    parallel_bar_image = parallel_bar_image.resize((700, 500))
    parallel_bar_photo = ImageTk.PhotoImage(parallel_bar_image)

    parallel_bar_image_label = ctk.CTkLabel(scrollable_frame, image=parallel_bar_photo, text="")
    parallel_bar_image_label.pack(pady=10)

    create_section(
        scrollable_frame,
        "WHAT IS THE PARALLEL BAR TRICEPS DIP?",
        """
    The Parallel Bar Triceps Dip is a bodyweight exercise that targets the triceps, shoulders, and chest. By using parallel bars to dip your body, this movement isolates the triceps while also engaging the shoulders and lower chest. It is an effective exercise for building upper body strength and defining the triceps.
    """
    )

    create_section(
        scrollable_frame,
        "HOW TO PERFORM THE PARALLEL BAR TRICEPS DIP",
        """
    1. SET UP THE PARALLEL BARS

    - Position the parallel bars so that you can easily grip them with your hands. They should be at a height where you can bend your knees when your arms are fully extended.



    2. STARTING POSITION

    - Grab the Bars: Grab both parallel bars firmly with your palms facing inward, arms fully extended. Keep your body upright and your legs slightly bent, feet off the ground.



    3. PERFORMING THE DIP

    - Lower Your Body: Slowly lower your body by bending your elbows. Keep your body vertical and avoid leaning forward. Continue lowering until your upper arms are parallel to the ground, or as deep as your flexibility allows.



    4. PUSH UP

    - Push Your Body Back Up: Press through your palms and extend your elbows to push your body back up to the starting position. Keep your core engaged to maintain stability.
    """
    )

    create_section(
        scrollable_frame,
        "TIPS FOR THE PARALLEL BAR TRICEPS DIP",
        """
    - Keep your elbows close to your body during the descent to better target the triceps.
    - Avoid locking your elbows at the top of the movement to keep tension on the muscles.
    - Keep your core tight to prevent swinging your legs.
    """
    )

    # Cable Tricep Pushdowns
    cable_pushdown_image = Image.open("pushdown.jpg")  # Replace with the correct image path
    cable_pushdown_image = cable_pushdown_image.resize((700, 300))
    cable_pushdown_photo = ImageTk.PhotoImage(cable_pushdown_image)

    cable_pushdown_image_label = ctk.CTkLabel(scrollable_frame, image=cable_pushdown_photo, text="")
    cable_pushdown_image_label.pack(pady=10)

    create_section(
        scrollable_frame,
        "WHAT IS THE CABLE TRICEP PUSHDOWN?",
        """
    The Cable Tricep Pushdown is an isolation exercise that primarily targets the triceps. Using a cable machine with a rope or bar attachment, this exercise allows for a controlled range of motion, effectively working the triceps without the involvement of other muscle groups. It's great for building tricep strength and mass.
    """
    )

    create_section(
        scrollable_frame,
        "HOW TO PERFORM THE CABLE TRICEP PUSHDOWN CORRECTLY",
        """
    1. SET UP THE CABLE MACHINE

    - Attach a rope or straight bar to the high pulley on a cable machine. Adjust the weight so it’s challenging but allows you to maintain control.



    2. STARTING POSITION

    - Grab the Attachment: Stand tall and grip the rope or bar with both hands. Pull the attachment towards you and position your elbows by your sides, bent at about 90 degrees.



    3. PUSH THE ATTACHMENT DOWN

    - Push Down: Keeping your elbows stationary, push the attachment downward, fully extending your arms at the bottom of the movement. Focus on squeezing your triceps at the bottom.



    4. RETURN TO STARTING POSITION

    - Slowly return the rope or bar to the starting position, maintaining control and not allowing the weight to pull your arms back too quickly.
    """
    )

    create_section(
        scrollable_frame,
        "TIPS FOR THE CABLE TRICEP PUSHDOWN",
        """
    - Elbow Position: Keep your elbows fixed at your sides and avoid letting them flare out during the movement.
    - Control the Weight: Perform the movement in a controlled manner, avoiding any jerking or swinging.
    - Don't Overextend: Avoid overextending your arms at the bottom of the movement to maintain tension on the triceps.
    """
    )


    app.mainloop()


    

    

def day2():
    root1 =ctk.CTkToplevel()
    root1.title('FitBites')
    root1.geometry('900x600')
    my_label=ctk.CTkLabel(root1,text="""WELCOME TO DAY 1 EXERCISES \n  
                                        \n Lower Body (Legs & Core)""",font=("Helvetica",24))
    my_label.pack(pady=50)
    
    ip="d2.jpg"
    i=Image.open(ip)
    ctk_i=ctk.CTkImage(light_image=i, size=(200,150))
    lbl= ctk.CTkLabel(root1, text="Barbell Squats     ", image= ctk_i,compound="right")
    lbl.pack(pady=20)

    ip2="d22.jpg"
    i2=Image.open(ip2)
    ctk_i2=ctk.CTkImage(light_image=i2, size=(200,150))
    lbl2= ctk.CTkLabel(root1, text="     Dumbbell Lunges", image= ctk_i2,compound="left")
    lbl2.pack(pady=20)

    ip3="d222.jpg"
    i3=Image.open(ip3)
    ctk_i3=ctk.CTkImage(light_image=i3, size=(200,150))
    lbl3= ctk.CTkLabel(root1, text="Leg Curls      ", image= ctk_i3,compound="right")
    lbl3.pack(pady=20)


    my_button=ctk.CTkButton(root1,text="Tap for more details of this exercise",command=more2)
    my_button.pack(pady=20)


    root1.mainloop()

def more2():
    m=ctk.CTk()
    m.geometry('900x500')
    lbl_2=ctk.CTkLabel(m, text='''1. Set Up the Barbell:
Rack the Bar: Position the barbell on a squat rack at about chest height. The bar should be even across the rack so you can lift it off without it hitting your body.
Choose the Right Weight: Begin with a manageable weight to focus on proper form. Gradually increase the weight as you get stronger.
2. Position Yourself Under the Bar:
Stand under the Bar: Place your body directly under the bar with your feet shoulder-width apart. The bar should sit high on your traps (the upper back muscles, just below the neck), not directly on your neck.
Grip the Bar: Grab the bar with both hands just wider than shoulder-width apart. Your palms should be facing forward (pronated grip), and your elbows should be pointing down or slightly back. This will help you keep the bar stable on your upper back.
Head Position: Look straight ahead to maintain a neutral spine throughout the movement. Don’t look up or down excessively.
3. Lift the Bar off the Rack:
Stand Tall: Push through your legs and lift the bar off the squat rack by standing upright. Take a step or two back to create space and ensure you're stable before starting the squat.
Feet Position: Position your feet about shoulder-width apart or slightly wider, with your toes pointed slightly outward (10–15 degrees).
Core Activation: Engage your core (brace your abs as if you're about to get punched in the stomach) to provide support for your spine.
4. Start the Descent:
Initiate the Squat: Begin the squat by pushing your hips back (like you're sitting into a chair) and simultaneously bending your knees. Your hips and knees should move together.
Keep Chest Up: Throughout the squat, keep your chest tall and your back neutral. Avoid rounding your lower back or letting your chest collapse forward.
Knee Position: Your knees should track over your toes. Do not let them cave inward. Push your knees out to the side to ensure proper alignment.
Depth: Lower yourself as deep as your mobility allows. Ideally, you want your thighs to be parallel to the ground or even lower (below parallel), but don't force depth if you don’t have the flexibility yet.
5. Bottom of the Squat:
Pause (Optional): You can briefly pause at the bottom position for 1-2 seconds, maintaining tension in your legs and core.
Maintain Control: Make sure your weight is distributed evenly across your feet, with your heels firmly planted. Do not let your heels come off the ground.
\n6. Drive Up:
Push Through Your Heels: To rise from the squat, press through your heels and the middle of your feet. Focus on pushing the floor away to stand up.
Keep the Chest Up: Keep your chest lifted, your back neutral, and don’t lean forward as you rise.
Fully Extend Legs: As you reach the top, fully extend your hips and knees, standing upright. Do not lock your knees out fully at the top.
7. Repeat:
Perform the desired number of reps, typically 3-5 sets of 5-12 reps, depending on your strength or hypertrophy goals.
8. Rack the Bar Safely:
Once you’ve completed your set, step forward into the squat rack, ensuring the bar is securely placed back on the rack before you let go.
\nHow to Do Dumbbell Lunges Correctly:
Start Position:

Hold a dumbbell in each hand, with your arms fully extended at your sides.
Stand tall with your feet hip-width apart, chest up, and core engaged.
Step Forward:

Take a large step forward with your right foot, ensuring your knee is directly above your ankle.
Lower your hips by bending both knees. Your left knee should almost touch the ground, but don't let it touch.
Achieve Proper Lunge Depth:

Aim for a 90-degree angle in both knees. The front knee should track over the toes but not go past them.
Push Back Up:

Push through the heel of your front foot to stand back up and return to the starting position.
Keep your torso upright and core engaged throughout the movement.
Repeat on Other Side:

After completing the movement with your right leg, repeat the lunge with your left leg.
Continue alternating legs for the desired number of reps.\n1. Adjust the Machine:
Seat Adjustment: Lie face down on the machine with your knees aligned with the machine's pivot point. Adjust the seat so that your legs are fully extended, and your knees are at the edge of the bench.
Ankle Rollers: Place your ankles under the padded rollers. The pads should rest just above your ankles, with your feet pointing down.
2. Starting Position:
Ensure your body is aligned on the machine. Keep your hips flat on the bench, and grip the handles (if available) to stabilize your torso.
3. Perform the Leg Curl:
Curl the Legs: Engage your hamstrings to curl your lower legs upward toward your glutes. Exhale as you lift your feet, ensuring the motion is controlled.
Full Range of Motion: Continue the movement until your knees are fully flexed and your heels are near your glutes.
4. Lower the Weight:
Controlled Descent: Slowly lower your legs back to the starting position while inhaling. Avoid letting the weights drop too quickly to maintain tension on the hamstrings.
5. Repeat:
Perform the desired number of repetitions, typically 8-12 reps for 3-4 sets.
 ''')
    lbl_2.pack()
    m.mainloop()

def day3():
    root1 =ctk.CTkToplevel()
    root1.title('FitBites')
    root1.geometry('900x600')
    my_label=ctk.CTkLabel(root1,text="""WELCOME TO DAY 3 EXERCISES \n  
                                        \n Rest or Active Recovery""",font=("Helvetica",24))
    my_label.pack(pady=50)
    
    ip="d3.jpg"
    i=Image.open(ip)
    ctk_i=ctk.CTkImage(light_image=i, size=(200,150))
    lbl= ctk.CTkLabel(root1, text="Pullups     ", image= ctk_i,compound="right")
    lbl.pack(pady=20)

    ip2="d33.jpg"
    i2=Image.open(ip2)
    ctk_i2=ctk.CTkImage(light_image=i2, size=(200,150))
    lbl2= ctk.CTkLabel(root1, text="     V bar seated row", image= ctk_i2,compound="left")
    lbl2.pack(pady=20)

    my_button=ctk.CTkButton(root1,text="Tap for more details of this exercise",command=more3)
    my_button.pack(pady=20)


    root1.mainloop()

def more3():
    m=ctk.CTk()
    m.geometry('900x500')
    lbl_3=ctk.CTkLabel(m, text='''1. Find a Pull-Up Bar:
Look for a sturdy pull-up bar that can support your body weight. It should be at a height where you can hang with your arms fully extended and feet off the ground.
2. Grip the Bar:
Overhand Grip (Pronated): Place your hands shoulder-width apart with palms facing away from you (this is the standard grip for pull-ups).
Underhand Grip (Supinated): For chin-ups, the palms face toward you with hands shoulder-width apart or closer.
Your fingers should wrap around the bar, and your thumb should lock around the bar to secure the grip.
3. Hang with Fully Extended Arms:
Let your body hang from the bar with your arms fully extended, legs straight or slightly bent.
Engage your core to avoid swinging. Keep your body still and in control.
4. Pull Yourself Up:
Initiate the Pull: Begin by pulling your shoulder blades back and down. This will activate your lats and engage the upper back muscles.
Use Your Back: As you pull, think about bringing your chest toward the bar rather than pulling with your arms alone. This emphasizes your lats and back muscles.
Elbows and Biceps: As you continue the pull, bring your elbows down toward your sides. Your biceps will engage as your elbows bend.
Chin Above the Bar: Aim to pull your chin above the bar. At the top of the movement, your chest should be close to the bar.
5. Lower Back Down:
Slowly lower your body back to the starting position with control. Do not let your arms lock out completely, but extend them almost fully at the bottom.
Keep your core engaged to avoid swinging and maintain stability.
6. Repeat:
Perform 3-4 sets of 5-12 reps depending on your strength level.
 \n1. Set Up the Cable Machine:
Attach a V-bar, wide-grip handle, or single handle to the low pulley on a cable machine.
Adjust the seat and knee pad so that your feet can comfortably rest flat on the platform, and your knees are slightly bent when you sit.
Select the appropriate weight to start with.
2. Position Yourself:
Sit on the bench with your feet flat on the footrest or platform.
Grip the handle with both hands (palms facing each other for V-bar or pronated for wide-grip).
Sit Tall: Keep your chest lifted, shoulders down, and back straight. Avoid rounding your lower back.
Engage Your Core: Tighten your core muscles to keep your torso stable during the movement.
3. Start the Movement:
Begin with your arms fully extended, holding the handle with your hands at arm’s length.
Keep your elbows slightly bent and your shoulders relaxed. Make sure your back is straight and your chest is slightly up.
4. Pull the Handle Toward You:
Initiate the Pull: Pull the handle toward your torso by retracting your shoulder blades (pulling them back and down). This engages your back muscles, particularly the lats and rhomboids.
Elbows Close: As you row, keep your elbows close to your sides, not flaring out.
Drive With Your Elbows: Focus on driving the movement with your elbows, not your hands, to better target your back muscles.
Pause at the Top: At the peak of the movement, your hands should be around the area of your lower ribs or waist, and you should feel a contraction in your back.
5. Return Slowly to the Starting Position:
Slowly extend your arms back to the starting position, resisting the pull of the weight. This eccentric phase (lowering the weight) is where a lot of muscle growth occurs.
Allow your shoulders to protract (move forward) and feel a stretch in your back.
6. Repeat:
Perform 8-12 reps for 3-4 sets, depending on your strength level.''')
    lbl_3.pack()
    m.mainloop()

def day4():
    root1 =ctk.CTkToplevel()
    root1.title('FitBites')
    root1.geometry('900x600')
    my_label=ctk.CTkLabel(root1,text="""WELCOME TO DAY 4 EXERCISES \n  
                                        \n Strength""",font=("Helvetica",24))
    my_label.pack(pady=50)
    
    ip="d4.jpg"
    i=Image.open(ip)
    ctk_i=ctk.CTkImage(light_image=i, size=(200,150))
    lbl= ctk.CTkLabel(root1, text="Dumbbell Row     ", image= ctk_i,compound="right")
    lbl.pack(pady=20)

    ip2="d44.jpg"
    i2=Image.open(ip2)
    ctk_i2=ctk.CTkImage(light_image=i2, size=(200,150))
    lbl2= ctk.CTkLabel(root1, text="     Hammer Curls", image= ctk_i2,compound="left")
    lbl2.pack(pady=20)

    my_button=ctk.CTkButton(root1,text="Tap for more details of this exercise",command=more3)
    my_button.pack(pady=20)

    root1.mainloop()
def more4():
    m=ctk.CTk()
    m.geometry('900x500')
    lbl_4=ctk.CTkLabel(m, text='''1. Set Up:
Equipment Needed: A flat bench and a dumbbell.
Start Position: Place one knee and one hand on the bench for support, creating a stable position. Your other foot should be flat on the floor, and the opposite hand should be holding the dumbbell.
Grip: With your free hand, grasp the dumbbell with a neutral grip (palm facing inward) or pronated grip (palm facing down), depending on your preference.
2. Position Your Body:
Keep your torso parallel to the floor. Avoid rounding your lower back.
Engage your core to stabilize your body.
Your supporting arm (the one on the bench) should be straight, and the dumbbell should be hanging straight down towards the floor.
3. Perform the Row:
Pull the Dumbbell: Initiate the movement by pulling the dumbbell toward your hip, leading with your elbow (not your hand). This will engage the lats and upper back muscles.
Retract Your Shoulder Blade: As you row the dumbbell, focus on squeezing your shoulder blade back and down. This is important for activating the rhomboids and middle traps.
Full Range of Motion: Pull the dumbbell as high as possible (without rotating your torso), aiming to bring your elbow just past your ribcage or toward your hip.
4. Lower the Dumbbell:
Slowly lower the dumbbell back to the starting position with control, fully extending your arm at the bottom.
Avoid letting the dumbbell just "drop" back down; control the descent to maximize muscle engagement.
5. Repeat:
Perform 8-12 reps per side for 3-4 sets.
\n1. Set Up:
Position: Stand with your feet shoulder-width apart and knees slightly bent to maintain a stable base.
Grip: Hold a dumbbell in each hand with a neutral grip (palms facing each other, thumbs wrapped around the handles).
Posture: Keep your chest up, shoulders back, and core engaged. Let your arms hang fully extended by your sides.
2. Curl the Dumbbells:
Lift: Exhale and curl both dumbbells upward by flexing your elbows. Keep your elbows close to your torso and avoid swinging.
Contract the Muscles: Focus on squeezing the muscles of the forearm and biceps as the dumbbells move upward. The palms remain facing each other throughout the movement.
Full Contraction: Curl the dumbbells until your forearms are roughly parallel to the floor or when you reach full bicep contraction (dumbbells near shoulder level).
3. Lower the Weights:
Controlled Descent: Slowly lower the dumbbells back to the starting position, fully extending your arms.
Tension on the Muscles: Resist gravity during the lowering phase to maximize muscle activation.
4. Repeat:
Perform 3-4 sets of 8-12 reps, depending on your goals (strength or hypertrophy).
 ''')
    lbl_4.pack()
    m.mainloop()


#bg_img=PIL.Image.open('homepage1.png')
#bg=ctk.CTkImage(bg_img,size=(600,500))

ctk.set_appearance_mode('dark')


main = ctk.CTk()
main.title("Login Page")
main.config(bg="white")
main.resizable(False, False)

bg_img = CTkImage(dark_image=Image.open("OIP.jpeg"), size=(500, 500))

bg_lab = CTkLabel(main, image=bg_img, text="", corner_radius=5, height=10, width=10)
bg_lab.grid(row=0, column=0)

frame1 = CTkFrame(main,fg_color="#D9D9D9", bg_color="white", height=350, width=300,corner_radius=20)
frame1.grid(row=0, column=1,padx=40)

title = CTkLabel(frame1,text="Welcome Back! \nLogin to Account",text_color="black",font=("",35,"bold"))
title.grid(row=0,column=0,sticky="nw",pady=30,padx=10)

phone_entry = CTkEntry(frame1,text_color="white", placeholder_text="Mobile no.", fg_color="black", placeholder_text_color="white",
                         font=("",16,"bold"), width=200, corner_radius=15, height=45)
phone_entry.grid(row=1,column=0,sticky="nwe",padx=30)

passwd_entry = CTkEntry(frame1,text_color="white",placeholder_text="Password",fg_color="black",placeholder_text_color="white",
                         font=("",16,"bold"), width=200,corner_radius=15, height=45, show="*")
passwd_entry.grid(row=2,column=0,sticky="nwe",padx=30,pady=20)

country_code = ctk.CTkOptionMenu(frame1, values=["+91", "+1", "+44", "+61", "+81"],fg_color="black",dropdown_fg_color="white",dropdown_text_color="black")
country_code.grid(row=1, column=3, padx=6, pady=10)
country_code.set("+91")

cr_acc = CTkButton(frame1,text="Create Account!",text_color="black",cursor="hand2",font=("",15),fg_color="#FFFFFF",command=agree_and_continue)
cr_acc.grid(row=3,column=0,sticky="w",pady=20,padx=40)

l_btn = CTkButton(frame1,text="Login",font=("",15,"bold"),height=40,width=60,fg_color="#0085FF",cursor="hand2",
                  corner_radius=15,command=login)
l_btn.grid(row=3,column=0,sticky="ne",pady=20, padx=35)

main.mainloop()

