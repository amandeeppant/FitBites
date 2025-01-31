# #DAY 1



# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 1: Full Body Strength Training + Cardio")
# app.geometry("900x700")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 1: Full Body Strength Training + Cardio 🏋️‍♂️",
#     font=("Arial", 28, "bold"),
#     text_color="#00aaff"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
# scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

# def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
#     title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
#     title_label.pack(anchor="w", padx=20, pady=(10, 5))

#     content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
#     content_label.pack(anchor="w", padx=20, pady=5)

# exercise1_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="1. Squats",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("squats.jpg")  
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "WHAT ARE SQUATS?",
#     """
# Squats are a compound exercise that primarily targets the quadriceps, hamstrings, and glutes, while also engaging the core. Squats are foundational for building lower body strength and improving functional movement.
# """
# )

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM SQUATS",
#     """
# 1. SET UP

# - Stand with your feet shoulder-width apart and your toes slightly pointed outwards.
# - Keep your chest up and core braced.



# 2. EXECUTING THE MOVEMENT

# - Lower your hips back and down as if sitting into a chair, keeping your knees in line with your toes.
# - Descend until your thighs are parallel to the ground or lower, if comfortable.
# - Push through your heels to return to the standing position.



# 3. TIPS FOR BETTER SQUATS

# - Keep your weight evenly distributed across your feet.
# - Avoid letting your knees cave inward or your chest collapse forward.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. Push-Ups",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("pushups.jpeg")  
# exercise2_img = exercise2_img.resize((700, 300))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "WHAT ARE PUSH-UPS?",
#     """
# Push-ups are a bodyweight exercise targeting the chest, shoulders, triceps, and core. They are a versatile exercise that can be scaled for different difficulty levels.
# """
# )

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM PUSH-UPS",
#     """
# 1. SET UP

# - Place your hands slightly wider than shoulder-width apart on the floor, and extend your legs back into a plank position.
# - Keep your body straight from head to heels and engage your core.



# 2. EXECUTING THE MOVEMENT

# - Lower your chest towards the ground by bending your elbows, keeping them at about a 45-degree angle.
# - Push through your hands to return to the starting position.
# """
# )

# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Deadlifts",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("deadlift.jpg")  
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "WHAT ARE DEADLIFTS?",
#     """
# Deadlifts are a compound movement targeting the posterior chain, including the hamstrings, glutes, and lower back. They are excellent for building total body strength and improving posture.
# """
# )

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM DEADLIFTS",
#     """
# 1. SET UP

# - Stand with your feet hip-width apart and the barbell close to your shins.
# - Bend your hips and knees to grip the bar with both hands just outside your legs.



# 2. EXECUTING THE MOVEMENT

# - Lift the bar by driving through your heels, extending your hips and knees simultaneously.
# - Keep your back flat and your core braced throughout.
# """
# )

# exercise4_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="4. 10-Minute Cardio Session",
#     font=("Arial", 22, "bold"),
#     text_color="#ffaa00"
# )
# exercise4_title.pack(pady=10)

# exercise4_img = Image.open("cardio.jpeg")  # Replace with the actual cardio image filename
# exercise4_img = exercise4_img.resize((700, 500))
# exercise4_photo = ImageTk.PhotoImage(exercise4_img)

# exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
# exercise4_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "CARDIO ROUTINE",
#     """
# - Jumping Jacks: 1 minute
# - High Knees: 1 minute
# - Burpees: 30 seconds
# - Rest: 30 seconds
# (Repeat 3 rounds)
# """
# )

# app.mainloop()





##DAY 2

# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 2: Full Body Strength Training")
# app.geometry("900x700")
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

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
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

# exercise1_img = Image.open("squats.jpg")  
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM BODYWEIGHT SQUATS",
#     """
# 1. SET UP

# - Stand with your feet shoulder-width apart.
# - Keep your chest up, and your arms can be extended forward for balance.



# 2. EXECUTING THE MOVEMENT

# - Lower your body by bending your knees and hips.
# - Continue lowering until your thighs are parallel to the ground, keeping your knees in line with your toes.
# - Push through your heels to return to the standing position.



# 3. TIPS

# - Keep your back straight and engage your core.
# - Avoid letting your knees cave inward during the squat.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. Push-Ups",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("pushups.jpeg")  
# exercise2_img = exercise2_img.resize((700, 300))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM PUSH-UPS",
#     """
# 1. SET UP

# - Start in a plank position with your hands slightly wider than shoulder-width apart.
# - Engage your core and keep your body in a straight line from head to heels.



# 2. EXECUTING THE MOVEMENT

# - Lower your body towards the ground by bending your elbows.
# - Once your chest is nearly touching the floor, push back up to the starting position.
# - Avoid flaring your elbows out.



# 3. TIPS

# - Keep your body in a straight line throughout the movement.
# - Engage your core and avoid letting your hips sag.
# """
# )

# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Dumbbell Rows",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("rows.jpg")  
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM DUMBBELL ROWS",
#     """
# 1. SET UP

# - Hold a dumbbell in one hand and bend at the waist with your opposite hand supported on a bench.
# - Keep your back flat and your core engaged.



# 2. EXECUTING THE MOVEMENT

# - Pull the dumbbell towards your hip, keeping your elbow close to your body.
# - Lower the dumbbell back down to the starting position.
# - Repeat for the other arm.



# 3. TIPS

# - Avoid twisting your torso; keep your back flat.
# - Engage your core to maintain stability throughout the movement.
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
# 1. SET UP

# - Start in a forearm plank position, with your elbows directly beneath your shoulders.
# - Engage your core and keep your body in a straight line from head to heels.



# 2. EXECUTING THE MOVEMENT

# - Hold the plank position for the designated time (30 seconds).
# - Keep your hips aligned with your body to avoid sagging.



# 3. TIPS

# - Keep your core tight and avoid letting your back arch or your hips drop.
# """
# )

# app.mainloop()





## DAY 3


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 3: Cardio (HIIT)")
# app.geometry("900x700")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 3: Cardio (HIIT) 🏃‍♂️",
#     font=("Arial", 28, "bold"),
#     text_color="#00aaff"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
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

# exercise1_img = Image.open("jacks.jpeg")  
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM JUMPING JACKS",
#     """
# 1. SET UP

# - Stand with your feet together and arms at your sides.
# - Keep your core engaged and your posture upright.



# 2. EXECUTING THE MOVEMENT

# - Jump up, spreading your feet to shoulder-width apart while raising your arms overhead.
# - Jump again to return to the starting position.



# 3. TIPS

# - Move rhythmically and land softly to reduce impact.
# - Maintain control over your movements and avoid excessive bouncing.
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
# 1. SET UP

# - Stand with your feet hip-width apart.
# - Keep your arms at your sides, ready to pump with your movement.



# 2. EXECUTING THE MOVEMENT

# - Lift your right knee towards your chest and quickly switch to lift your left knee.
# - Continue alternating at a fast pace.



# 3. TIPS

# - Engage your core and keep your back straight.
# - Pump your arms in sync with your legs for balance and momentum.
# - Aim to lift your knees to hip level or higher.
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
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM MOUNTAIN CLIMBERS",
#     """
# 1. SET UP

# - Start in a high plank position, with your hands directly under your shoulders.
# - Engage your core and keep your body in a straight line.



# 2. EXECUTING THE MOVEMENT

# - Bring your right knee towards your chest, then quickly switch legs.
# - Continue alternating legs at a steady pace.



# 3. TIPS

# - Maintain a controlled and steady rhythm.
# - Avoid letting your hips sag or lifting them too high.
# - Keep your core tight for stability.
# """
# )

# hiit_circuit_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="HIIT Circuit Instructions",
#     font=("Arial", 22, "bold"),
#     text_color="#ffaa00"
# )
# hiit_circuit_title.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "CIRCUIT DETAILS",
#     """
# - Perform each exercise for 30 seconds.
# - Rest for 30 seconds between exercises.
# - Complete 4-5 rounds of the circuit.

# TIPS:
# - Warm up before starting to prepare your muscles and joints.
# - Cool down after completing the circuit to gradually lower your heart rate.
# - Stay hydrated and listen to your body throughout.
# """
# )

# app.mainloop()






## DAY 4


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 4: Active Recovery (Yoga/Stretching)")
# app.geometry("900x700")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 4: Active Recovery (Yoga/Stretching) 🧘‍♂️",
#     font=("Arial", 28, "bold"),
#     text_color="#00aaff"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
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
# exercise1_img = exercise1_img.resize((700, 300))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM CHILD'S POSE",
#     """
# 1. SET UP

# - Kneel on the floor with your big toes touching and knees apart.
# - Sit back on your heels and stretch your arms forward.



# 2. EXECUTING THE MOVEMENT

# - Lower your torso between your thighs and rest your forehead on the floor.
# - Hold the position for 1-2 minutes while breathing deeply.



# 3. TIPS

# - Relax your shoulders and neck.
# - Breathe deeply and evenly.
# - Use a cushion under your forehead for comfort.
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
# exercise2_img = exercise2_img.resize((700, 300))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM DOWNWARD DOG",
#     """
# 1. SET UP

# - Start on your hands and knees.
# - Lift your hips up and back, straightening your legs.



# 2. EXECUTING THE MOVEMENT

# - Press your heels towards the floor and extend your arms forward.
# - Hold the position for 1-2 minutes while breathing deeply.



# 3. TIPS

# - Keep your spine long and straight.
# - Avoid locking your knees.
# - Engage your core and breathe deeply.
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
# exercise3_img = exercise3_img.resize((700, 300))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM CAT-COW STRETCH",
#     """
# 1. SET UP

# - Start on your hands and knees with your wrists directly under your shoulders.
# - Keep your knees under your hips.



# 2. EXECUTING THE MOVEMENT

# - Inhale and arch your back, lifting your head and tailbone (Cow Pose).
# - Exhale and round your back, tucking your chin and tailbone (Cat Pose).
# - Continue to alternate between Cat and Cow poses for 1-2 minutes.



# 3. TIPS

# - Move smoothly between poses.
# - Keep your shoulders relaxed.
# - Breathe deeply and evenly.
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
# exercise4_img = exercise4_img.resize((700, 300))
# exercise4_photo = ImageTk.PhotoImage(exercise4_img)

# exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
# exercise4_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM SEATED FORWARD BEND",
#     """
# 1. SET UP

# - Sit on the floor with your legs extended straight in front of you.
# - Inhale and lengthen your spine.



# 2. EXECUTING THE MOVEMENT

# - Exhale and hinge at your hips to reach for your toes.
# - Hold the position for 1-2 minutes while breathing deeply.



# 3. TIPS

# - Keep your back straight and avoid rounding your spine.
# - Reach as far as comfortable without forcing the stretch.
# - Use a strap around your feet if you can't reach your toes.
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
# exercise5_img = exercise5_img.resize((700, 300))
# exercise5_photo = ImageTk.PhotoImage(exercise5_img)

# exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
# exercise5_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM PIGEON POSE",
#     """
# 1. SET UP

# - Start in a plank position.
# - Bring your right knee forward and place it behind your right wrist.
# - Extend your left leg back, keeping your hips square.



# 2. EXECUTING THE MOVEMENT

# - Lower your torso over your right leg and rest on your forearms or forehead.
# - Hold the position for 1-2 minutes, then switch sides.



# 3. TIPS

# - Keep your hips square to the floor.
# - Avoid forcing the stretch, go as deep as comfortable.
# - Use a cushion under your hip for support if needed.
# """
# )

# tips_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="Tips for Active Recovery",
#     font=("Arial", 22, "bold"),
#     text_color="#ffaa00"
# )
# tips_title.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "ACTIVE RECOVERY TIPS",
#     """
# - Focus on Breathing: Deep, steady breathing helps relax your muscles and improve the effectiveness of the stretches.
# - Stay Hydrated: Drink plenty of water to help flush out toxins and aid in muscle recovery.
# - Listen to Your Body: Stretch gently and avoid any movements that cause pain or discomfort.
# """
# )

# app.mainloop()





##DAY 5


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 5: Lower Body Strength Training")
# app.geometry("900x700")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 5: Lower Body Strength Training 🦵",
#     font=("Arial", 28, "bold"),
#     text_color="#00aaff"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
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
# 1. SET UP

# - Step forward with one leg, keeping your body upright.
# - Lower your hips until both knees are bent at 90 degrees.



# 2. EXECUTING THE MOVEMENT

# - Push off your front leg to return to standing position.



# 3. TIPS

# - Keep your front knee over your ankle.
# - Engage your core and keep your back straight.
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
# 1. SET UP

# - Lie on your back with your knees bent and feet flat on the floor.
# - Place your arms at your sides for stability.



# 2. EXECUTING THE MOVEMENT

# - Press through your heels to lift your hips toward the ceiling.
# - Lower your hips back down to the starting position.



# 3. TIPS

# - Squeeze your glutes and engage your core as you lift.
# - Avoid arching your back excessively.
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
# 1. SET UP

# - Stand with your feet hip-width apart.
# - Keep your legs straight, engage your core.



# 2. EXECUTING THE MOVEMENT

# - Raise your heels off the ground as high as possible.
# - Slowly lower your heels back to the floor.



# 3. TIPS

# - Keep your movements controlled and avoid bouncing.
# - Focus on the contraction in your calves.
# """
# )

# app.mainloop()





##DAY 6


# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 6: Upper Body Strength Training")
# app.geometry("900x700")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 6: Upper Body Strength Training 💪",
#     font=("Arial", 28, "bold"),
#     text_color="#00aaff"
# )
# header.pack(pady=10)

# scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
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
# 1. SET UP

# - Stand with a dumbbell in each hand, palms facing forward.
# - Keep your elbows close to your body.



# 2. EXECUTING THE MOVEMENT

# - Curl the weights towards your shoulders.
# - Lower the dumbbells back down with control.



# 3. TIPS

# - Focus on squeezing your biceps at the top of the curl.
# - Avoid swinging your arms, keep the movement slow and controlled.
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
# 1. SET UP

# - Sit on the edge of a bench or chair with your hands next to your hips.
# - Slide your hips off the edge, keeping your feet flat on the ground.



# 2. EXECUTING THE MOVEMENT

# - Lower your body by bending your elbows at a 90-degree angle.
# - Push back up to return to the starting position.



# 3. TIPS

# - Keep your elbows pointing straight back, not flaring out.
# - Engage your core to prevent your body from sinking.
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
# 1. SET UP

# - Stand with a dumbbell in each hand at shoulder height.
# - Keep your elbows bent at a 90-degree angle.



# 2. EXECUTING THE MOVEMENT



# - Press the dumbbells overhead until your arms are fully extended.
# - Lower the dumbbells back down to shoulder height.



# 3. TIPS

# - Keep your core tight and avoid arching your back.
# - Perform the movement slowly and with control.
# """
# )

# app.mainloop()





##DAY 7

# import customtkinter as ctk
# from PIL import Image, ImageTk

# app = ctk.CTk()
# app.title("Day 7: Cardio (Steady-State) + Mobility Work")
# app.geometry("900x800")
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("dark-blue")

# main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
# main_frame.pack(fill="both", expand=True)

# header = ctk.CTkLabel(
#     main_frame,
#     text="Day 7: Cardio (Steady-State) + Mobility Work 🏃‍♂️",
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
#     text="1. Steady-State Cardio (Jogging/Cycling)",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise1_title.pack(pady=10)

# exercise1_img = Image.open("steady_state_cardio.jpeg")  
# exercise1_img = exercise1_img.resize((700, 600))
# exercise1_photo = ImageTk.PhotoImage(exercise1_img)

# exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
# exercise1_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM STEADY-STATE CARDIO",
#     """
# 1. WARM-UP

# - Start with 5-10 minutes of light jogging or brisk walking.
# - Gradually prepare your muscles and joints for the main activity.



# 2. MAIN ACTIVITY

# - Maintain a steady, moderate pace where you can hold a conversation.
# - If jogging, aim for a pace that feels sustainable for the entire duration.
# - If cycling, adjust the resistance to a moderate level.



# 3. COOL-DOWN

# - Finish with 5-10 minutes of light jogging or walking to bring your heart rate down.



# 4. TIPS

# - Keep your form upright and relaxed.
# - Breathe steadily and rhythmically.
# - Hydrate before, during, and after your session.
# """
# )

# exercise2_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="2. Hip Circles",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise2_title.pack(pady=10)

# exercise2_img = Image.open("hip_curls.jpeg")  
# exercise2_img = exercise2_img.resize((700, 600))
# exercise2_photo = ImageTk.PhotoImage(exercise2_img)

# exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
# exercise2_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM HIP CIRCLES",
#     """
# 1. SET UP

# - Stand with your feet shoulder-width apart.
# - Place your hands on your hips.



# 2. EXECUTING THE MOVEMENT

# - Rotate your hips in large circular motions.
# - Perform 10-15 circles in one direction, then switch to the other direction.



# 3. TIPS

# - Keep your upper body still.
# - Gradually increase the size of your circles.
# - Maintain control and avoid jerky movements.
# """
# )

# exercise3_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="3. Arm Circles",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise3_title.pack(pady=10)

# exercise3_img = Image.open("arm_circles.jpeg")  
# exercise3_img = exercise3_img.resize((700, 600))
# exercise3_photo = ImageTk.PhotoImage(exercise3_img)

# exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
# exercise3_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM ARM CIRCLES",
#     """
# 1. SET UP

# - Stand with your feet shoulder-width apart.
# - Extend your arms out to the sides, parallel to the ground.



# 2. EXECUTING THE MOVEMENT

# - Make small circles with your arms, gradually increasing the size.
# - Perform 10-15 circles in one direction, then switch to the other direction.



# 3. TIPS

# - Keep your back straight and core engaged.
# - Move your arms smoothly without straining your shoulders.
# - Focus on breathing steadily throughout.
# """
# )

# exercise4_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="4. Thoracic Rotations",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise4_title.pack(pady=10)

# exercise4_img = Image.open("thoracic_rotations.jpeg")  
# exercise4_img = exercise4_img.resize((700, 600))
# exercise4_photo = ImageTk.PhotoImage(exercise4_img)

# exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
# exercise4_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM THORACIC ROTATIONS",
#     """
# 1. SET UP

# - Start on your hands and knees, wrists under shoulders and knees under hips.
# - Place one hand behind your head.



# 2. EXECUTING THE MOVEMENT

# - Rotate your upper body to bring your elbow towards the ceiling.
# - Return to starting position and repeat on the other side.



# 3. TIPS

# - Engage your core and avoid arching your back.
# - Focus on rotating your thoracic spine slowly and with control.
# """
# )

# exercise5_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="5. Ankle Circles",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise5_title.pack(pady=10)

# exercise5_img = Image.open("ankle_circles.jpeg")  
# exercise5_img = exercise5_img.resize((700, 600))
# exercise5_photo = ImageTk.PhotoImage(exercise5_img)

# exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
# exercise5_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM ANKLE CIRCLES",
#     """
# 1. SET UP

# - Sit or stand with one leg lifted off the ground.



# 2. EXECUTING THE MOVEMENT

# - Rotate your ankle in a circular motion.
# - Perform 10-15 circles in one direction, then switch to the other.



# 3. TIPS

# - Keep your leg still and focus on the ankle movement.
# - Gradually increase the size of the circles for a better range of motion.
# """
# )

# exercise6_title = ctk.CTkLabel(
#     scrollable_frame,
#     text="6. Deep Squat Hold",
#     font=("Arial", 22, "bold"),
#     text_color="#00aaff"
# )
# exercise6_title.pack(pady=10)

# exercise6_img = Image.open("deep_squat_hold.jpeg")  
# exercise6_img = exercise6_img.resize((700, 600))
# exercise6_photo = ImageTk.PhotoImage(exercise6_img)

# exercise6_image_label = ctk.CTkLabel(scrollable_frame, image=exercise6_photo, text="")
# exercise6_image_label.pack(pady=10)

# create_section(
#     scrollable_frame,
#     "HOW TO PERFORM DEEP SQUAT HOLD",
#     """
# 1. SET UP

# - Stand with your feet shoulder-width apart.



# 2. EXECUTING THE MOVEMENT

# - Lower your body into a deep squat position, with hips below your knees.
# - Hold the position for 1-2 minutes, keeping your heels on the ground.



# 3. TIPS

# - Keep your back straight and chest lifted.
# - Use your arms for balance if needed.
# - Adjust your position or reduce the duration if uncomfortable.
# """
# )

# app.mainloop()
