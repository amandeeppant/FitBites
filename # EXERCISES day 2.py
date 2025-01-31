# EXERCISES  DAY1
import customtkinter as ctk
from PIL import Image, ImageTk
import os


def run():

    # Initialize the app
    app = ctk.CTkToplevel()
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

    exercise3_img = Image.open("incline.jpg")  
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

    # Run the app
    app.mainloop()

a=ctk.CTk()
a.geometry("400x400")
a.title("ferf")
b=ctk.CTkButton(a,text="hello",command=run)
b.pack()
a.mainloop()



