## DAY 1




# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 1: Cardio (Beginner - Brisk Walking)")
# app.geometry("900x800")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 1: Cardio (Beginner - Brisk Walking) 🚶‍♂️",
#     font=("Arial", 28, "bold"),
#     text_color="#00aaff"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)

# exercise1_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="1. Brisk Walking",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("brisk_walking.jpeg")  
# exercise1_img = exercise1_img.resize((700, 300))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM BRISK WALKING",
#     """
# 1. WARM-UP

# - Start with 5 minutes of slow walking to prepare your body.



# 2. MAIN ACTIVITY

# - Walk at a pace that raises your heart rate, but still allows you to hold a conversation.
# - Maintain a brisk but sustainable pace for the entire session.



# 3. COOL-DOWN

# - Finish with 5 minutes of slow walking to bring your heart rate down.



# 4. TIPS

# - Wear comfortable shoes for support.
# - Maintain good posture with shoulders relaxed and back straight.
# - Stay hydrated before, during, and after the walk.
# """
# )

# app.mainloop()






##DAY 2


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 2: Full Body Strength Training (Beginner)")
# app.geometry("900x800")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 2: Full Body Strength Training 💪",
#     font=("Arial", 28, "bold"),
#     text_color="#00aaff"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)

# exercise1_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="1. Bodyweight Squats",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("squates.jpeg")  
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM BODYWEIGHT SQUATS",
#     """
# 1. Stand with feet shoulder-width apart.

# 2. Lower your body by bending your knees and hips, keeping your back straight.

# 3. Return to standing position.

# 4. Maintain your knees over your toes throughout the movement.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. Push-Ups",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("push_up.jpeg")  
# exercise2_img = exercise2_img.resize((700, 600))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM PUSH-UPS",
#     """
# 1. Start in a plank position with hands directly under your shoulders.

# 2. Lower your body until your chest nearly touches the floor.

# 3. Push back up to the starting position.

# 4. Keep your body in a straight line and avoid flaring your elbows.
# """
# )

# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Dumbbell Rows",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("dumbbell_rows.jpeg") 
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM DUMBBELL ROWS",
#     """
# 1. Bend at the waist, holding a dumbbell in one hand.

# 2. Pull the dumbbell towards your hip and lower it back down.

# 3. Keep your back flat and core engaged throughout the movement.
# """
# )

# exercise4_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="4. Plank",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise4_title.pack(pady=10)

# exercise4_img = Image.open("plank.jpg")  
# exercise4_img = exercise4_img.resize((700, 600))
# exercise4_photo = ImageTk.PhotoImage(exercise4_img)

# exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
# exercise4_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM PLANK",
#     """
# 1. Start in a forearm plank position.

# 2. Keep your body in a straight line from head to heels.

# 3. Engage your core and hold the position.

# 4. Avoid letting your hips sag or rise.
# """
# )

# app.mainloop()






##DAY 3


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 3: Cardio (HIIT)")
# app.geometry("900x800")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 3: Cardio (HIIT) 🏃‍♂️",
#     font=("Arial", 28, "bold"),
#     text_color="#ff9900"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)


# exercise1_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="1. Jumping Jacks",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("plank_jack.jpeg")  
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM JUMPING JACKS",
#     """
# 1. Stand with your feet together and arms at your sides.

# 2. Jump up, spreading your feet to shoulder-width apart while raising your arms overhead.

# 3. Jump again to return to the starting position.

# 4. Keep your movements controlled and rhythmic.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. High Knees",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("high_knees.jpeg") 
# exercise2_img = exercise2_img.resize((700, 600))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM HIGH KNEES",
#     """
# 1. Stand with your feet hip-width apart.

# 2. Lift your right knee towards your chest.

# 3. Quickly switch to lift your left knee towards your chest while lowering your right leg.

# 4. Keep your back straight and core engaged.
# """
# )


# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Mountain Climbers",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("mountain_climbers.jpeg")  
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM MOUNTAIN CLIMBERS",
#     """
# 1. Start in a high plank position with your hands directly under your shoulders.

# 2. Bring your right knee towards your chest.

# 3. Quickly switch legs, bringing your left knee towards your chest while extending your right leg back.

# 4. Keep your hips level and engage your core.
# """
# )


# exercise4_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="4. Rest",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise4_title.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO REST",
#     """
# 1. Take a 30-second rest between each exercise.

# 2. Use this time to catch your breath and prepare for the next exercise.

# 3. Stay hydrated and keep moving lightly to prevent muscles from cooling down.

# 4. Focus on deep, steady breathing.
# """
# )


# create_section(
#     scrollable_frame,
#     "HIIT CIRCUIT",
#     """
# 1. Perform each exercise for 30 seconds.

# 2. Rest for 30 seconds between exercises.

# 3. Repeat the circuit 4-5 times.

# 4. Warm-up before and cool down after the HIIT circuit.

# 5. Modify the intensity if needed and listen to your body.
# """
# )

# app.mainloop()






##DAY 4


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 4: Active Recovery (Yoga/Stretching)")
# app.geometry("900x800")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 4: Active Recovery (Yoga/Stretching) 🧘‍♂️",
#     font=("Arial", 28, "bold"),
#     text_color="#ff9900"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)

# exercise1_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="1. Child's Pose",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("child_pose.jpeg")
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM CHILD'S POSE",
#     """
# 1. Kneel on the floor with your big toes touching and knees apart.

# 2. Sit back on your heels and stretch your arms forward.

# 3. Lower your torso between your thighs and rest your forehead on the floor.

# 4. Hold for 1-2 minutes, breathing deeply.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. Downward Dog",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("downward_dog.jpeg")
# exercise2_img = exercise2_img.resize((700, 600))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM DOWNWARD DOG",
#     """
# 1. Start on your hands and knees.

# 2. Lift your hips up and back, straightening your legs.

# 3. Press your heels towards the floor and extend your arms.

# 4. Hold for 1-2 minutes, breathing deeply.
# """
# )

# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Cat-Cow Stretch",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("cat.jpg")
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM CAT-COW STRETCH",
#     """
# 1. Start on your hands and knees with wrists under shoulders and knees under hips.

# 2. Inhale, arch your back, lifting your head and tailbone (Cow Pose).

# 3. Exhale, round your back, tucking chin and tailbone (Cat Pose).

# 4. Alternate between Cat and Cow poses for 1-2 minutes.
# """
# )

# exercise4_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="4. Seated Forward Bend",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise4_title.pack(pady=10)

# exercise4_img = Image.open("seated_forward_bend.jpeg")
# exercise4_img = exercise4_img.resize((700, 600))
# exercise4_photo = ImageTk.PhotoImage(exercise4_img)

# exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
# exercise4_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM SEATED FORWARD BEND",
#     """
# 1. Sit on the floor with legs extended in front of you.

# 2. Inhale and lengthen your spine.

# 3. Exhale and hinge at your hips to reach for your toes.

# 4. Hold for 1-2 minutes, breathing deeply.
# """
# )

# exercise5_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="5. Pigeon Pose",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise5_title.pack(pady=10)

# exercise5_img = Image.open("pigeon_pose.jpeg")
# exercise5_img = exercise5_img.resize((700, 600))
# exercise5_photo = ImageTk.PhotoImage(exercise5_img)

# exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
# exercise5_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM PIGEON POSE",
#     """
# 1. Start in a plank position.

# 2. Bring your right knee forward and place it behind your right wrist.

# 3. Extend your left leg back, keeping your hips square.

# 4. Lower your torso over your right leg and rest on forearms or forehead.

# 5. Hold for 1-2 minutes, then switch sides.
# """
# )

# create_section(
#     scrollable_frame,
#     "TIPS FOR ACTIVE RECOVERY",
#     """
# 1. Focus on breathing: Deep, steady breathing helps relax your muscles.

# 2. Stay hydrated: Drink plenty of water to aid muscle recovery.

# 3. Listen to your body: Stretch gently and avoid discomfort.
# """
# )

# app.mainloop()





##DAY 5


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 5: Lower Body Strength Training")
# app.geometry("900x800")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 5: Lower Body Strength Training 💪",
#     font=("Arial", 28, "bold"),
#     text_color="#ff9900"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)

# exercise1_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="1. Lunges",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("lunges.jpg")
# exercise1_img = exercise1_img.resize((700, 300))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM LUNGES",
#     """
# 1. Step forward with one leg.

# 2. Lower your hips until both knees are bent at 90 degrees.

# 3. Return to standing.

# 4. Perform 3 sets of 12 reps per leg.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. Glute Bridges",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("glute_bridges.jpeg")
# exercise2_img = exercise2_img.resize((700, 600))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM GLUTE BRIDGES",
#     """
# 1. Lie on your back with knees bent.

# 2. Lift your hips towards the ceiling.

# 3. Lower your hips back down.

# 4. Perform 3 sets of 15 reps.
# """
# )

# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Calf Raises",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("calf_raises.jpeg")
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM CALF RAISES",
#     """
# 1. Stand with feet hip-width apart.

# 2. Raise your heels off the ground.

# 3. Lower them back down.

# 4. Perform 3 sets of 15 reps.
# """
# )

# app.mainloop()





##DAY 6


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 6: Upper Body Strength Training")
# app.geometry("900x800")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 6: Upper Body Strength Training 💪",
#     font=("Arial", 28, "bold"),
#     text_color="#ff9900"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)

# exercise1_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="1. Bicep Curls",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("bicep_curls.jpeg")
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM BICEP CURLS",
#     """
# 1. Stand with a dumbbell in each hand.

# 2. Curl the weights towards your shoulders.

# 3. Lower them back down.

# 4. Perform 3 sets of 12 reps.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. Tricep Dips",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("tricep_dips.jpeg")
# exercise2_img = exercise2_img.resize((700, 600))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM TRICEP DIPS",
#     """
# 1. Sit on the edge of a bench.

# 2. Slide your hips off and lower your body by bending your elbows.

# 3. Push back up.

# 4. Perform 3 sets of 10 reps.
# """
# )

# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Shoulder Press",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("shoulder_press.jpeg")
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM SHOULDER PRESS",
#     """
# 1. Stand with a dumbbell in each hand at shoulder height.

# 2. Press the weights overhead.

# 3. Lower them back down.

# 4. Perform 3 sets of 12 reps.
# """
# )

# app.mainloop()





##DAY7


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 7: Cardio (Steady-State) + Mobility Work")
# app.geometry("900x900")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 7: Cardio (Steady-State) + Mobility Work 🏃‍♂️🚴‍♀️",
#     font=("Arial", 28, "bold"),
#     text_color="#ff9900"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)

# # Steady-State Cardio Section
# cardio_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="Steady-State Cardio: Jogging or Cycling",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# cardio_title.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "How to Perform Steady-State Cardio",
#     """
# 1. Warm-Up: 5-10 minutes of light jogging or brisk walking.

# 2. Main Activity: Jog or cycle at a steady, moderate pace for 30-45 minutes.

# 3. Cool-Down: 5-10 minutes of light jogging or walking.
# """
# )

# # Mobility Work Section
# mobility_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="Mobility Work",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# mobility_title.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "1. Hip Circles",
#     """
# 1. Stand with your feet shoulder-width apart.

# 2. Rotate your hips in large circles, 10-15 times in each direction.
# """
# )

# create_section(
#     scrollable_frame,
#     "2. Arm Circles",
#     """
# 1. Stand with feet shoulder-width apart and extend arms to the sides.

# 2. Make small circles with your arms, gradually increasing the size.

# 3. Perform 10-15 circles in each direction.
# """
# )

# create_section(
#     scrollable_frame,
#     "3. Thoracic Rotations",
#     """
# 1. Start on your hands and knees.

# 2. Place one hand behind your head and rotate your upper body, bringing your elbow toward the ceiling.

# 3. Repeat on the other side.
# """
# )

# create_section(
#     scrollable_frame,
#     "4. Ankle Circles",
#     """
# 1. Sit or stand with one leg lifted off the ground.

# 2. Rotate your ankle in large circles, 10-15 times in each direction.
# """
# )

# create_section(
#     scrollable_frame,
#     "5. Deep Squat Hold",
#     """
# 1. Stand with your feet shoulder-width apart.

# 2. Lower your body into a deep squat position, keeping your heels on the ground.

# 3. Hold the position for 1-2 minutes.
# """
# )

# app.mainloop()
