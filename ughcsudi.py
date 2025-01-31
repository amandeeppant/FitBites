import customtkinter as ctk
from PIL import Image,ImageTk

# Set the theme for the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def weight_gain_beginner():
    clear_frame()
    label = ctk.CTkLabel(app, text="Weight Gain Beginner", font=("Arial", 18, "bold"))
    label.pack(pady=10)
    def day1():
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
        pass
    def day2():
        app = ctk.CTkToplevel()
        app.title("Day 2: Lower Body 🏋️‍♀️")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 2: Lower Body (Leg Focus) 🦵",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Barbell Squats",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("squats.jpg")
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS THE BARBELL SQUAT?",
            """
        The Barbell Squat is a fundamental lower body exercise that primarily targets the quadriceps, hamstrings, and glutes. It also engages the lower back and core muscles for stability. Barbell squats are considered one of the best exercises for building strength and mass in the legs, as well as improving overall functional fitness.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM THE BARBELL SQUAT CORRECTLY",
            """
        1. SET UP THE BARBELL AND POSITION YOURSELF

        - Position the Barbell: Place the barbell across your upper back, just below the neck, with your feet shoulder-width apart.
        - Grip the Barbell: Hold the barbell with your hands at shoulder-width, ensuring your grip is firm and secure.



        2. LOWER INTO THE SQUAT

        - Hinge at the Hips: Push your hips back and bend your knees, lowering your body into a squat. Keep your chest lifted and your back straight.
        - Depth: Lower yourself until your thighs are parallel to the ground, or deeper if your flexibility allows.



        3. RETURN TO THE STARTING POSITION

        - Push Through Your Heels: Push through your heels and drive your hips forward to stand back up. Avoid letting your knees cave inward.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR THE BARBELL SQUAT",
            """
        - Keep Your Back Straight: Maintain a neutral spine throughout the movement to avoid injury.
        - Don't Let Your Knees Go Beyond Your Toes: Ensure your knees stay behind your toes during the squat.
        - Focus on Depth: Squat as deep as you can while maintaining proper form.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Leg Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )

        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("legpress.jpg")
        exercise2_img = exercise2_img.resize((700, 300))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS THE LEG PRESS?",
            """
        The Leg Press is a lower body exercise that targets the quadriceps, hamstrings, and glutes. It is performed on a machine and is considered a safer alternative to squats for beginners, as it provides more control and stability.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM THE LEG PRESS CORRECTLY",
            """
        1. SET UP THE MACHINE

        - Sit on the Leg Press Machine: Ensure your back is fully supported, and your feet are placed shoulder-width apart on the platform.



        2. PERFORM THE EXERCISE

        - Push the Platform: Push the platform away by extending your legs, ensuring you don’t lock your knees.
        - Control the Descent: Lower the platform slowly, allowing your knees to bend at a 90-degree angle or slightly deeper.



        3. RETURN TO THE STARTING POSITION

        - Press the Platform Back Up: Push through your heels and return to the starting position, keeping control of the movement.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR THE LEG PRESS",
            """
        - Maintain a Neutral Spine: Keep your lower back against the seat to prevent injury.
        - Don’t Lock Your Knees: Avoid fully extending your legs and locking your knees at the top of the movement.
        - Focus on Controlled Movement: Perform the exercise with a slow and controlled motion to maximize muscle engagement.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Dumbbell Lunges",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("lunges.jpg")
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE DUMBBELL LUNGES?",
            """
        Dumbbell Lunges are a single-leg, bodyweight exercise that targets the quadriceps, hamstrings, glutes, and calves. It also helps improve balance, coordination, and stability, making it a great addition to any leg day routine.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DUMBBELL LUNGES CORRECTLY",
            """
        1. CHOOSE THE RIGHT DUMBBELLS

        - Select a pair of dumbbells that allow you to maintain proper form throughout the movement.



        2. PERFORM THE LUNGE

        - Step Forward: With a dumbbell in each hand, step forward with one leg, lowering your body until both knees are bent at 90 degrees. The back knee should hover just above the ground.
        - Push Through the Heel: Press through the heel of your front foot to return to the starting position.



        3. ALTERNATE LEGS

        - Repeat the lunge movement with the opposite leg, alternating between legs for the desired number of repetitions.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DUMBBELL LUNGES",
            """
        - Maintain an Upright Posture: Keep your chest up and avoid leaning forward.
        - Keep Your Knees Behind Your Toes: Ensure your front knee doesn't extend past your toes as you lunge.
        - Engage Your Core: Activate your core muscles to help with balance and stability during the exercise.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Leg Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("legcurls.jpg")
        exercise4_img = exercise4_img.resize((700, 300))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS THE LEG CURL?",
            """
        The Leg Curl is an isolation exercise that primarily targets the hamstrings. It is performed on a machine where you curl a padded lever toward your glutes, working the muscles in the back of your thighs. This exercise is great for building strength and definition in the hamstrings.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM THE LEG CURL",
            """
        1. SET UP THE MACHINE

        - Adjust the seat and pad so that your knees align with the machine’s pivot point.
        - Position your feet under the padded lever, making sure the pads are placed on the lower part of your calves.



        2. CURLING THE LEVER

        - Pull your heels toward your glutes by flexing your knees.
        - Keep your hips pressed against the seat to avoid excessive movement.



        3. RETURN TO STARTING POSITION

        - Slowly lower the lever back to the starting position, fully extending your legs without locking your knees.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR THE LEG CURL",
            """
        - Keep your movements controlled, especially on the lowering phase.
        - Avoid using momentum to pull the lever; focus on engaging the hamstrings.
        - Do not arch your back or lift your hips off the seat.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Standing Calf Raises",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("calf.jpg")
        exercise5_img = exercise5_img.resize((700, 300))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE STANDING CALF RAISES?",
            """
        Standing Calf Raises primarily target the calves, specifically the gastrocnemius muscle. This exercise is done by standing with your feet flat on the floor, lifting your heels as high as possible, and then lowering them back down. It's an effective exercise for building calf strength and definition.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM STANDING CALF RAISES",
            """
        1. STARTING POSITION

        - Stand upright with your feet shoulder-width apart, either on a flat surface or on a raised step.
        - Keep your core engaged and your posture straight.



        2. RAISING YOUR HEELS

        - Slowly raise your heels off the ground as high as you can, squeezing your calves at the top of the movement.



        3. LOWERING YOUR HEELS

        - Lower your heels back to the starting position, stretching your calves as you descend.
        - Repeat the movement for the desired number of repetitions.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR STANDING CALF RAISES",
            """
        - Focus on a controlled movement, especially during the lowering phase.
        - Avoid bouncing at the top or bottom of the movement.
        - Keep your body upright throughout the exercise, avoiding excessive leaning forward.
        """
        )
        exercise6_title = ctk.CTkLabel(
            scrollable_frame,
            text="6. Plank",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise6_title.pack(pady=10)

        exercise6_img = Image.open("plank.jpg")
        exercise6_img = exercise6_img.resize((700, 300))
        exercise6_photo = ImageTk.PhotoImage(exercise6_img)

        exercise6_image_label = ctk.CTkLabel(scrollable_frame, image=exercise6_photo, text="")
        exercise6_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS THE PLANK?",
            """
        The Plank is a core-strengthening exercise that involves holding a position similar to a push-up, but with your weight on your forearms. It targets the abs, lower back, and shoulders. Planks are excellent for improving core stability and endurance.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM THE PLANK",
            """
        1. STARTING POSITION

        - Begin by getting into a push-up position, but with your forearms resting on the ground. Your elbows should be directly under your shoulders.
        - Keep your body in a straight line from head to heels, engaging your core and glutes.



        2. HOLD THE POSITION

        - Hold this position for as long as you can while maintaining proper form.
        - Keep your hips level and avoid letting your back sag.



        3. FINISH

        - When you're finished, gently lower your knees to the floor and rest.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR THE PLANK",
            """
        - Keep your core tight to prevent your lower back from sagging.
        - Avoid holding your breath; continue breathing steadily.
        - If you're unable to hold the position for long, start with shorter intervals and gradually increase your time.
        """
        )
        exercise7_title = ctk.CTkLabel(
            scrollable_frame,
            text="7. Russian Twist",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise7_title.pack(pady=10)

        exercise7_img = Image.open("russian.jpg")
        exercise7_img = exercise7_img.resize((700, 300))
        exercise7_photo = ImageTk.PhotoImage(exercise7_img)

        exercise7_image_label = ctk.CTkLabel(scrollable_frame, image=exercise7_photo, text="")
        exercise7_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS THE RUSSIAN TWIST?",
            """
        The Russian Twist is a core exercise that primarily targets the obliques. It involves twisting your torso from side to side while holding a weight, typically a medicine ball or dumbbell. This exercise helps build rotational strength and improves core stability.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM THE RUSSIAN TWIST",
            """
        1. STARTING POSITION

        - Sit on the floor with your knees bent and your feet flat on the floor. Lean back slightly to engage your core.
        - Hold a weight or medicine ball with both hands in front of your chest.



        2. TWISTING THE TORO

        - Rotate your torso to one side, bringing the weight towards the floor beside your hip.
        - Return to the center and rotate to the opposite side.



        3. REPEATING THE MOVEMENT

        - Continue alternating sides for the desired number of repetitions, maintaining a controlled movement throughout.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR THE RUSSIAN TWIST",
            """
        - Keep your back straight and your core engaged throughout the exercise.
        - Avoid slouching or arching your back.
        - Perform the movement slowly and with control to maximize effectiveness.
        """
        )
        app.mainloop()
        pass    
    def day3():
        app = ctk.CTkToplevel()
        app.title("Day 3: Rest or Active Recovery")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 3: Rest or Active Recovery (Light Cardio, Stretching) 🧘‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        create_section(
            scrollable_frame,
            "WHAT IS ACTIVE RECOVERY?",
            """
        Active recovery refers to low-intensity exercises that help maintain blood flow to muscles and promote recovery. These exercises can include light cardio, such as walking, cycling, or swimming, as well as stretching routines. The goal is to keep the body moving without putting stress on the muscles, allowing them to recover while still benefiting from movement.
        """
        )

        create_section(
            scrollable_frame,
            "BENEFITS OF ACTIVE RECOVERY",
            """
        1. IMPROVED BLOOD FLOW

        Active recovery helps improve circulation, which delivers nutrients to muscles and removes waste products, speeding up the healing process.

        2. REDUCED MUSCLE STIFFNESS

        Low-intensity activity prevents muscles from stiffening up, which can happen when resting completely after intense workouts.

        3. MENTAL RELAXATION

        Light movement can help reduce stress and improve mental clarity, making active recovery an effective method to recover both physically and mentally.
        """
        )

        create_section(
            scrollable_frame,
            "ACTIVE RECOVERY ROUTINE IDEAS",
            """
        - **Light Cardio**: 20-30 minutes of walking, cycling, or swimming at a comfortable pace. This helps maintain blood circulation without overexerting yourself.

        - **Stretching**: Focus on gentle stretches for the whole body. Include dynamic stretches like arm circles, leg swings, and neck rolls, followed by static stretches like hamstring stretches and hip openers.

        - **Yoga**: Incorporate basic yoga poses like Downward Dog, Child's Pose, and Cat-Cow to help stretch the muscles and improve flexibility while promoting relaxation.
        """
        )
        app.mainloop()


    def day4():
    # # DAY 4


        app = ctk.CTkToplevel()
        app.title("Day 3: Upper Body (Pull Focus)")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 3: Upper Body (Pull Focus) 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Pull-Ups",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("pullup.jpg")  
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A PULL-UP?",
            """
        Pull-ups are a compound exercise that primarily targets the back (latissimus dorsi), while also working the biceps, shoulders, and core. It is a bodyweight exercise that involves pulling your body up towards a bar until your chin is above it. Pull-ups are one of the best exercises for developing upper body strength and are a staple in many strength training programs.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A PULL-UP",
            """
        1. SET UP THE PULL-UP BAR

        - Grab a pull-up bar with both hands, palms facing away from you (pronated grip), and your hands slightly wider than shoulder-width apart.
        - Hang with your arms fully extended and your feet off the ground. Engage your core and maintain a straight body position.



        2. EXECUTING THE LIFT

        - Pull Up: Begin pulling your body upward by engaging your back and biceps. Focus on driving your elbows down and towards your sides.
        - Chin Over Bar: Continue pulling until your chin is above the bar. Hold briefly at the top, then lower yourself back to the starting position.



        3. LOWERING YOUR BODY

        - Control the Descent: Slowly lower your body back to the starting position with control, ensuring that your arms are fully extended before performing another rep.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR PULL-UPS",
            """
        - Keep your chest lifted and your shoulder blades pulled down and back to engage the lats properly.
        - Avoid swinging your legs or using momentum to help lift your body.
        - Perform the movement in a controlled manner to maximize muscle engagement.
        """
        )
        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Seated Cable Rows",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("seated.jpg")
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A SEATED CABLE ROW?",
            """
        The seated cable row is a compound exercise that targets the upper back, specifically the latissimus dorsi, rhomboids, and traps. It also engages the biceps and forearms. This exercise is done using a cable machine, which allows for a smooth and controlled movement while also enabling variable resistance throughout the motion.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A SEATED CABLE ROW",
            """
        1. SET UP THE SEATED CABLE MACHINE

        - Sit down on a cable machine with your feet flat on the platform and your knees slightly bent.
        - Grab the handle with both hands and sit up straight with a slight lean forward at your hips.
        - Extend your arms fully to start with the weight at the lowest point.



        2. EXECUTING THE LIFT

        - Pull Back: Initiate the movement by pulling your elbows back, keeping them close to your torso, while you squeeze your shoulder blades together.
        - Full Contraction: Continue pulling the handle until your torso is upright and your hands are near your abdomen.



        3. LOWERING THE WEIGHT

        - Slowly extend your arms back to the starting position, maintaining control throughout the descent.
        - Avoid allowing your body to swing or your arms to fully lock out.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR SEATED CABLE ROWS",
            """
        - Keep your back straight and avoid rounding your spine during the movement.
        - Focus on squeezing your shoulder blades together at the end of the row for maximum back engagement.
        - Don't use momentum; let your back muscles do the work.
        """
        )
        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Dumbbell Rows",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("rows.jpg")
        exercise3_img = exercise3_img.resize((700, 300))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A DUMBBELL ROW?",
            """
        Dumbbell rows are a unilateral compound exercise that targets the upper back, primarily the latissimus dorsi, traps, and rhomboids. It also engages the biceps, forearms, and core. Dumbbell rows are excellent for improving muscular imbalances since they work each side of the body individually.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A DUMBBELL ROW",
            """
        1. SET UP

        - Hold a dumbbell in one hand and place your opposite knee and hand on a bench for support.
        - Keep your back flat and your core engaged. The dumbbell should be hanging down with your arm fully extended.



        2. EXECUTING THE LIFT

        - Row the Dumbbell: Pull the dumbbell upwards, leading with your elbow. Keep your elbow close to your body and squeeze your shoulder blades together.
        - Reach the Top: At the top of the movement, your upper arm should be parallel to the floor. Pause briefly at the top.



        3. LOWERING THE DUMBBELL

        - Slowly lower the dumbbell back to the starting position, ensuring full range of motion and control throughout.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DUMBBELL ROWS",
            """
        - Keep your back flat and avoid rotating your torso.
        - Focus on squeezing your back muscles at the top of the movement.
        - Perform the exercise slowly and with control for maximum muscle engagement.
        """
        )
        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Dumbbell Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("dumbell_curls.jpg")
        exercise4_img = exercise4_img.resize((700, 300))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A DUMBBELL CURL?",
            """
        Dumbbell curls are a classic isolation exercise that targets the biceps. By using dumbbells, the exercise allows for a greater range of motion and the ability to work each arm independently. This makes it effective for building arm strength and size, particularly in the biceps.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A DUMBBELL CURL",
            """
        1. SET UP

        - Stand up straight with a dumbbell in each hand, arms fully extended, and palms facing forward.
        - Keep your elbows close to your torso and maintain a straight posture.



        2. EXECUTING THE LIFT

        - Curl the Dumbbells: Keeping your upper arms stationary, curl the dumbbells towards your shoulders by flexing your elbows.
        - Contract the Biceps: Squeeze your biceps at the top of the movement, then slowly lower the weights back to the starting position.



        3. LOWERING THE DUMBBELLS

        - Slowly lower the dumbbells back to the starting position, fully extending your arms before beginning the next rep.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DUMBBELL CURLS",
            """
        - Keep your elbows stationary and close to your body throughout the movement.
        - Avoid swinging your body or using momentum to lift the weights.
        - Focus on squeezing your biceps at the top of the curl.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Hammer Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("hammer.jpg")
        exercise5_img = exercise5_img.resize((700, 500))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A HAMMER CURL?",
            """
        Hammer curls are a variation of the traditional bicep curl that target the brachialis muscle, which lies underneath the biceps. This exercise also works the forearms and helps increase grip strength. By using a neutral grip (palms facing inward), hammer curls help develop more overall arm strength.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A HAMMER CURL",
            """
        1. SET UP

        - Stand straight with a dumbbell in each hand, palms facing your torso.
        - Keep your elbows close to your torso and maintain a straight posture.



        2. EXECUTING THE LIFT

        - Curl the Dumbbells: Keeping your upper arms stationary, curl the dumbbells towards your shoulders by flexing your elbows.
        - Contract the Biceps and Forearms: Squeeze your biceps and forearms at the top of the movement.



        3. LOWERING THE DUMBBELLS

        - Slowly lower the dumbbells back to the starting position, fully extending your arms before beginning the next rep.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR HAMMER CURLS",
            """
        - Keep your elbows stationary and close to your torso throughout the movement.
        - Avoid swinging your body or using momentum to lift the weights.
        - Focus on squeezing your forearms and biceps at the top of the curl.
        """
        )
        exercise6_title = ctk.CTkLabel(
            scrollable_frame,
            text="6. Face Pulls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise6_title.pack(pady=10)

        exercise6_img = Image.open("face.jpg")
        exercise6_img = exercise6_img.resize((700, 600))
        exercise6_photo = ImageTk.PhotoImage(exercise6_img)

        exercise6_image_label = ctk.CTkLabel(scrollable_frame, image=exercise6_photo, text="")
        exercise6_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A FACE PULL?",
            """
        Face pulls are a cable-based exercise that primarily targets the rear deltoids (shoulders), trapezius, and rhomboids. It also helps improve posture by strengthening the muscles of the upper back. Face pulls can improve shoulder stability and prevent injuries by strengthening the small stabilizer muscles in the rotator cuff.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A FACE PULL",
            """
        1. SET UP THE CABLE MACHINE

        - Attach a rope handle to a cable machine set at upper chest height.
        - Grab the rope with both hands, palms facing each other, and step back so that the cable is taut.



        2. EXECUTING THE LIFT

        - Pull the Rope: Pull the rope towards your face, separating the rope ends as you pull. Your elbows should be flared out to the sides.
        - Squeeze the Shoulder Blades: At the peak of the movement, squeeze your shoulder blades together and hold briefly.



        3. LOWERING THE WEIGHT

        - Slowly return to the starting position with control, keeping tension in the cable.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR FACE PULLS",
            """
        - Keep your shoulders down and back throughout the movement.
        - Focus on pulling the rope towards your face while keeping your upper arms level with your body.
        - Don't let your body sway; maintain a stable stance throughout the exercise.
        """
        )
        app.mainloop()
        pass

    def day5():
        app = ctk.CTkToplevel()
        app.title("Day 5: Lower Body Focus")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 5: Lower Body Focus 🦵",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Deadlifts",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("deadlift.jpg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A DEADLIFT?",
            """
        Deadlifts are a compound exercise that targets the entire posterior chain, including the hamstrings, glutes, and lower back. It also works the core, forearms, and traps. The deadlift is considered one of the most effective exercises for building overall strength and mass.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A DEADLIFT",
            """
        1. SET UP THE BARBELL

        - Place the barbell on the floor with your feet about hip-width apart. The bar should be directly over the middle of your feet.
        - Bend down and grip the bar with your hands slightly wider than shoulder-width apart, keeping your arms straight.
        - Lower your hips and engage your core, maintaining a straight back throughout the movement.



        2. EXECUTING THE LIFT

        - Lift the Bar: Push through your heels and extend your hips and knees simultaneously to lift the barbell. Keep the bar close to your body throughout the movement.
        - Lockout: At the top, your back should be straight, and your chest should be up, with the barbell at thigh height.



        3. LOWERING THE BARBELL

        - Control the Descent: Push your hips back and lower the barbell down in a controlled manner, keeping your back straight and bending at the hips and knees.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DEADLIFTS",
            """
        - Keep your back straight and avoid rounding your lower back during the lift.
        - Focus on pushing through your heels and maintaining a stable core.
        - Perform the lift in a controlled manner, avoiding jerky movements.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Walking Lunges",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("walking.jpg")
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE WALKING LUNGES?",
            """
        Walking lunges are a unilateral lower-body exercise that targets the quads, hamstrings, and glutes. They also engage the core for stability. The walking lunge is effective for building strength and balance while targeting the muscles of the legs.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A WALKING LUNGE",
            """
        1. SET UP

        - Stand up straight with your feet hip-width apart. Hold a dumbbell in each hand if using weights.
        - Take a step forward with your right leg and bend both knees to 90 degrees, lowering your body toward the ground.



        2. EXECUTING THE LUNGE

        - Push Back Up: Push through your right heel and return to the standing position.
        - Alternate Legs: Step forward with your left leg and repeat the process.



        3. CONTINUOUS MOTION

        - Continue alternating legs with each step, making sure to maintain a tall posture and keep your core engaged throughout the movement.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR WALKING LUNGES",
            """
        - Keep your chest lifted and avoid leaning forward during the movement.
        - Don't let your knee extend past your toes when lunging.
        - Perform the movement in a controlled manner to maintain balance and stability.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Lying Leg Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("lying.jpg")
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A LYING LEG CURL?",
            """
        The lying leg curl is an isolation exercise that targets the hamstrings. It is performed on a leg curl machine and involves bending the knees to bring the lower legs toward the glutes. This exercise helps improve hamstring strength and flexibility.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A LYING LEG CURL",
            """
        1. SET UP THE MACHINE

        - Lie face down on the leg curl machine with your knees aligned with the pivot point of the machine.
        - Place your feet under the padded lever and grip the handles to stabilize your body.



        2. EXECUTING THE CURL

        - Curl Your Legs: Bend your knees and curl your legs towards your glutes, focusing on contracting the hamstrings.
        - Full Contraction: At the top of the movement, hold for a moment to maximize the contraction.



        3. LOWERING THE WEIGHT

        - Slowly lower your legs back to the starting position, maintaining control throughout the descent.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR LYING LEG CURLS",
            """
        - Avoid using momentum to lift the weight; focus on controlling the movement with your hamstrings.
        - Keep your hips pressed against the bench throughout the movement.
        - Don't fully extend your legs at the bottom to maintain tension in the hamstrings.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Seated Calf Raises",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("calfraises.jpg")
        exercise4_img = exercise4_img.resize((700, 300))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE SEATED CALF RAISES?",
            """
        Seated calf raises are an isolation exercise that targets the calves, specifically the soleus muscle. This exercise is performed on a seated calf raise machine, which allows for a deep stretch and full range of motion in the calf muscles.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM SEATED CALF RAISES",
            """
        1. SET UP THE MACHINE

        - Sit on the calf raise machine with your feet on the footrest and your knees under the pads.
        - Position the weight on your thighs to provide resistance during the movement.



        2. EXECUTING THE RAISE

        - Push Up: Raise your heels as high as possible by extending your ankles and contracting your calves.
        - Full Contraction: Pause at the top to fully engage the calf muscles.



        3. LOWERING THE WEIGHT

        - Slowly lower your heels back to the starting position, stretching the calves at the bottom.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR SEATED CALF RAISES",
            """
        - Focus on using your calves to lift the weight, avoiding any momentum or bouncing.
        - Ensure your knees are stationary throughout the movement.
        - Perform the movement slowly and with control to maximize muscle engagement.
        """
        )
        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Leg Raises",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("legraises.jpg")  # Replace with your actual image path
        exercise5_img = exercise5_img.resize((700, 300))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE LEG RAISES?",
            """
        Leg raises are an excellent exercise for targeting the lower abs, hip flexors, and quads. They are typically performed lying on your back, either on a mat or on a bench. This exercise helps build core strength and stability.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM LEG RAISES",
            """
        1. GET INTO POSITION

        - Lie flat on your back with your legs extended and your arms by your sides for stability.
        - Keep your legs straight, and ensure your back is pressed into the floor.



        2. LIFTING THE LEGS

        - Slowly raise your legs towards the ceiling while keeping them straight, engaging your lower abdominal muscles.
        - Lift until your legs are perpendicular to your body or as high as your flexibility allows.



        3. LOWERING THE LEGS

        - Lower your legs back down slowly, stopping just before your feet touch the floor, to maintain tension in the abs.
        - Repeat for the desired number of reps.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR LEG RAISES",
            """
        - Focus on using your abdominal muscles to lift your legs, not your hip flexors.
        - Keep your lower back pressed to the floor throughout the movement to avoid straining your spine.
        - Avoid swinging your legs or using momentum to lift them.
        """
        )

        app.mainloop()
        pass
    def day6():
        app = ctk.CTkToplevel()
        app.title("Day 6: Rest or Active Recovery (Light Cardio, Walking, Yoga)")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 6: Rest or Active Recovery (Light Cardio, Walking, Yoga) 🧘‍♀️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        create_section(
            scrollable_frame,
            "WHAT IS ACTIVE RECOVERY?",
            """
        Active recovery involves performing light exercises that aid muscle recovery without overtaxing the body. This could include walking, light cycling, or practicing yoga. The primary aim is to keep moving while allowing the body to recover from intense physical activity.
        """
        )

        create_section(
            scrollable_frame,
            "BENEFITS OF ACTIVE RECOVERY",
            """
        1. ENHANCED RECOVERY

        Active recovery promotes better circulation, which helps to reduce muscle soreness and speed up recovery.

        2. IMPROVED FLEXIBILITY

        Yoga or stretching routines during active recovery can help improve flexibility and maintain joint mobility.

        3. LOW-IMPACT MOVEMENT

        Activities like walking or gentle yoga place minimal strain on the body while still providing movement and aiding in muscle relaxation.
        """
        )

        create_section(
            scrollable_frame,
            "ACTIVE RECOVERY ROUTINE IDEAS",
            """
        - **Walking**: Take a 20-30 minute walk at a brisk pace to keep your body moving without overexerting.

        - **Yoga**: Focus on restorative yoga poses like Child's Pose, Warrior II, and Seated Forward Fold to stretch and relax the muscles.

        - **Light Cardio**: If you prefer, engage in 20-30 minutes of light cycling or swimming to promote circulation and muscle relaxation.
        """
        )
        app.mainloop()
        pass
    def day7():
        app = ctk.CTkToplevel()
        app.title("Day 7: Full Rest (Muscle Recovery)")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 7: Full Rest (Muscle Recovery) 🛀",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        create_section(
            scrollable_frame,
            "WHAT IS A REST DAY?",
            """
        A full rest day means taking a break from intense physical activities to allow your muscles to recover and repair. Rest days are essential for muscle growth, reducing fatigue, and preventing overtraining.
        """
        )

        create_section(
            scrollable_frame,
            "WHY IS A REST DAY IMPORTANT?",
            """
        1. MUSCLE REPAIR

        Rest days allow muscles to repair and grow after strength training or intense cardio, preventing injury and promoting overall strength development.

        2. PREVENTING BURNOUT

        Constant training without proper rest can lead to burnout or overtraining syndrome. Taking regular rest days helps to avoid exhaustion.

        3. MENTAL RESET

        Rest days also provide mental relaxation, giving you a break from structured workouts and helping to stay motivated.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO USE A REST DAY EFFECTIVELY",
            """
        - **Complete Rest**: Simply take the day off from all forms of intense physical activity. Allow your body to recover fully.

        - **Light Movement**: If you prefer to stay active, engage in very light activities such as stretching, yoga, or walking, but keep it minimal to avoid muscle strain.

        - **Focus on Recovery**: This is a great time to focus on nutrition, hydration, and getting good quality sleep, which are all essential for recovery.
        """
        )
        app.mainloop()

        pass

    days=[day1,day2,day3,day4,day5,day6,day7]
    for i, day in enumerate(days):
        button = ctk.CTkButton(app, text=f"Day{i+1}", font=("Arial", 14), width=200,command=day)
        button.pack(pady=10)

    pass

def weight_gain_advanced():
    def day1():
        # #DAY1

        app = ctk.CTkToplevel()
        app.title("Day 1: Push Day (Chest, Shoulders, Triceps) 💪")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 1: Push Day (Chest, Shoulders, Triceps) 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Bench Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("benchpress.jpg") 
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A BENCH PRESS?",
            """
        The bench press is a classic strength training exercise that primarily targets the chest muscles (pectoralis major), but also works the shoulders (deltoids) and triceps. It is performed using a barbell or dumbbells while lying on a bench. It is essential for developing upper body strength and is a fundamental compound exercise.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A BENCH PRESS",
            """
        1. SET UP THE BENCH PRESS STATION

        - Lie flat on a bench with your feet firmly planted on the floor.
        - Grip the barbell with your hands slightly wider than shoulder-width apart. Ensure the barbell is directly above your chest when fully extended.



        2. EXECUTING THE LIFT

        - Lower the Bar: Slowly lower the barbell towards your chest while maintaining control. Keep your elbows at a 45-degree angle.
        - Push the Bar Up: Press the bar back up to the starting position by pushing through your chest and extending your arms fully.



        3. SAFETY TIPS

        - Always use a spotter when lifting heavy loads to prevent injury.
        - Keep your back flat against the bench and avoid arching it excessively.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR BENCH PRESS",
            """
        - Keep your wrist straight and avoid letting them bend backward during the press.
        - Maintain a controlled movement throughout both the descent and ascent phases.
        - Engage your core for better stability.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Incline Dumbbell Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("dumbell_incline.jpg")  
        exercise2_img = exercise2_img.resize((700, 300))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS AN INCLINE DUMBBELL PRESS?",
            """
        The incline dumbbell press is an effective exercise to target the upper portion of the chest. It also works the shoulders and triceps. By using dumbbells, you increase the range of motion compared to a barbell, which leads to better chest engagement.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM AN INCLINE DUMBBELL PRESS",
            """
        1. SET UP THE INCLINE BENCH

        - Set the bench to a 30-45 degree incline and sit down with a dumbbell in each hand.
        - Press the dumbbells overhead with your palms facing forward and arms fully extended.



        2. EXECUTING THE LIFT

        - Lower the Dumbbells: Slowly lower the dumbbells down towards your upper chest, keeping your elbows at a 45-degree angle.
        - Press the Dumbbells Up: Press the dumbbells back up to the starting position, fully extending your arms.



        3. SAFETY TIPS

        - Keep your wrists neutral and avoid letting them bend excessively.
        - Engage your core to avoid arching your back.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR INCLINE DUMBBELL PRESS",
            """
        - Avoid locking your elbows at the top of the press for continuous tension.
        - Focus on squeezing your chest at the top of the movement.
        - Keep the movement slow and controlled for maximum muscle engagement.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Shoulder Overhead Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("overhead.jpeg")  
        exercise3_img = exercise3_img.resize((700, 300))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A SHOULDER OVERHEAD PRESS?",
            """
        The shoulder overhead press, also known as the military press, is a key exercise for building shoulder strength. It targets the deltoid muscles (front, side, and rear) and works the triceps and upper chest as well. This exercise can be performed with a barbell or dumbbells.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A SHOULDER OVERHEAD PRESS",
            """
        1. SET UP THE PRESS STATION

        - Stand with your feet shoulder-width apart and hold a barbell or dumbbells at shoulder height.
        - Engage your core and maintain a neutral spine.



        2. EXECUTING THE LIFT

        - Press the Weight Up: Press the weight overhead by extending your arms, ensuring your elbows are fully extended at the top.
        - Control the Descent: Lower the weight back to shoulder height, maintaining control throughout the movement.



        3. SAFETY TIPS

        - Avoid arching your lower back excessively by keeping your core engaged.
        - Keep the barbell or dumbbells aligned with your body throughout the press.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR SHOULDER OVERHEAD PRESS",
            """
        - Avoid flaring your elbows too wide, as this can strain the shoulder joint.
        - Use a controlled pace to focus on muscle activation.
        - Engage your traps and lats to support the press.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Tricep Dips",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("tricep.jpg") 
        exercise4_img = exercise4_img.resize((700, 600))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A TRICEP DIP?",
            """
        Tricep dips are a bodyweight exercise that primarily targets the triceps, but also engages the shoulders and chest. It is an excellent exercise for developing arm strength and building muscle mass in the triceps.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A TRICEP DIP",
            """
        1. SET UP THE DIP STATION

        - Place your hands on parallel bars or a bench, ensuring your palms are facing inward.
        - Keep your feet off the ground and your legs extended.



        2. EXECUTING THE LIFT

        - Lower Your Body: Slowly lower your body by bending your elbows, keeping them close to your sides.
        - Press Back Up: Push yourself back up to the starting position by fully extending your arms.



        3. SAFETY TIPS

        - Avoid letting your shoulders round forward; keep your chest lifted.
        - Engage your core for stability during the movement.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR TRICEP DIPS",
            """
        - Keep your elbows pointed straight back to target the triceps effectively.
        - Avoid swinging your legs or body; the movement should be controlled and stable.
        - Use a spotter if you plan to add additional weight.
        """
        )
        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Dumbbell Flys",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("flys.jpeg")  
        exercise5_img = exercise5_img.resize((700, 300))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A DUMBBELL FLY?",
            """
        Dumbbell Flys are a chest exercise that focuses on isolating the pectoral muscles. They provide an excellent stretch and contraction at the peak of the movement. Unlike presses, which involve pushing weights in a linear motion, flys require the arms to open wide, effectively targeting the chest fibers for hypertrophy and definition.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A DUMBBELL FLY",
            """
        1. SET UP THE EXERCISE

        - Lie flat on a bench, holding a dumbbell in each hand with your arms extended straight up.
        - Keep a slight bend in your elbows, and make sure your feet are flat on the floor.



        2. EXECUTING THE MOVEMENT

        - Lower the Dumbbells: Slowly lower the dumbbells out to the sides, keeping your elbows slightly bent. Aim to get a good stretch in the chest at the bottom.
        - Bring the Dumbbells Back Up: Reverse the movement and bring the dumbbells back to the starting position by squeezing your chest muscles.



        3. SAFETY TIPS

        - Avoid going too heavy, as form is crucial for this movement.
        - Do not let your arms extend beyond your shoulders to prevent injury.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DUMBBELL FLYS",
            """
        - Focus on a slow, controlled descent to fully stretch the chest muscles.
        - Keep your elbows slightly bent throughout the exercise to avoid excessive strain on the shoulder joints.
        - Perform the movement with a full range of motion for maximum chest activation.
        """
        )
        app.mainloop()
        pass
    def day2():
         #DAY2

        app = ctk.CTkToplevel()
        app.title("Day 2: Leg Day (Hypertrophy Focus) 🦵")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 2: Leg Day (Hypertrophy Focus) 🦵",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Squats",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("squats.jpg")  
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A SQUAT?",
            """
        Squats are a fundamental lower-body strength exercise that primarily targets the quadriceps, hamstrings, and glutes. They also engage the core and lower back muscles for stability. Squats are essential for building overall leg strength and mass.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A SQUAT",
            """
        1. SET UP YOUR FEET



        - Stand with your feet shoulder-width apart, toes slightly turned out.
        - Keep your chest up and shoulders back.

        2. EXECUTING THE LIFT

        - Lower your hips by bending your knees and pushing your hips back, as if sitting down on a chair.
        - Go as low as you can while keeping your knees behind your toes and your back neutral.
        - Press through your heels to return to the starting position.



        3. SAFETY TIPS

        - Keep your chest lifted and avoid rounding your back.
        - Do not let your knees collapse inward as you squat.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR SQUATS",
            """
        - Keep the weight distributed across your heels and mid-foot.
        - Engage your core throughout the movement to maintain stability.
        - Consider using a squat rack if you're lifting heavy weights.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Deadlifts",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("deadlift.jpg")  
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A DEADLIFT?",
            """
        The deadlift is a compound exercise that targets the posterior chain, including the hamstrings, glutes, and lower back. It also engages the core and traps, making it a full-body exercise that builds functional strength.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A DEADLIFT",
            """
        1. SET UP YOUR FEET

        - Stand with your feet hip-width apart, barbell close to your shins.
        - Grip the barbell with both hands slightly outside your knees.



        2. EXECUTING THE LIFT

        - Hinge at the hips, keeping your back straight, and lift the barbell by extending your hips and knees simultaneously.
        - Lower the bar back down with control by hinging at the hips and bending the knees.



        3. SAFETY TIPS

        - Always keep the barbell close to your body during the lift.
        - Avoid rounding your back, and maintain a neutral spine throughout the movement.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DEADLIFTS",
            """
        - Engage your lats before starting the lift to create tension and prevent rounding your back.
        - Do not jerk the weight up; focus on a controlled, smooth movement.
        - Use a mixed grip if lifting heavy to improve grip strength.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Leg Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("legpress.jpg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A LEG PRESS?",
            """
        The leg press is a machine-based exercise that targets the quadriceps, hamstrings, and glutes. It allows you to lift heavy weights in a controlled manner and is an excellent accessory movement for building leg mass and strength.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A LEG PRESS",
            """
        1. SET UP THE MACHINE

        - Sit down on the leg press machine and place your feet shoulder-width apart on the platform.
        - Adjust the seat so your knees are at a 90-degree angle when starting.



        2. EXECUTING THE LIFT



        - Push the platform away by extending your legs but do not lock your knees.
        - Lower the platform back down by bending your knees until they are at a 90-degree angle.



        3. SAFETY TIPS

        - Avoid letting your lower back come off the seat during the lift.
        - Keep your knees aligned with your toes to prevent knee injuries.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR LEG PRESS",
            """
        - Keep your feet flat on the platform and avoid letting your heels lift.
        - Focus on pushing through your heels to fully engage your glutes and hamstrings.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Romanian Deadlifts",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("romanian.jpg") 
        exercise4_img = exercise4_img.resize((700, 600))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A ROMANIAN DEADLIFT?",
            """
        The Romanian deadlift (RDL) is a variation of the deadlift that targets the hamstrings and glutes more intensely. It is an excellent exercise for improving posterior chain strength and muscle growth.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A ROMANIAN DEADLIFT",
            """
        1. SET UP YOUR FEET

        - Stand with your feet hip-width apart and hold the barbell with an overhand grip in front of your thighs.
        - Keep your knees slightly bent and your chest up.



        2. EXECUTING THE LIFT

        - Hinge at the hips, lowering the barbell towards the ground while keeping it close to your body.
        - Go as low as you can while maintaining a neutral spine, then reverse the movement by driving your hips forward.



        3. SAFETY TIPS

        - Keep your back straight and avoid rounding your spine.
        - Focus on hinging at the hips rather than bending your knees too much.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR ROMANIAN DEADLIFTS",
            """
        - Engage your glutes and hamstrings as you reverse the movement.
        - Do not let the barbell drop too low to avoid overextending your lower back.
        - Control the descent to maximize the stretch in the hamstrings.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Standing Calf Raises",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("standing.jpg")  
        exercise5_img = exercise5_img.resize((700, 300))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE STANDING CALF RAISES?",
            """
        Standing calf raises target the calf muscles (gastrocnemius and soleus). This exercise helps improve lower leg strength, stability, and endurance.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM STANDING CALF RAISES",
            """
        1. SET UP

        - Stand tall with your feet shoulder-width apart, with the balls of your feet on a raised surface (like a calf raise machine or platform).
        - Keep your hands on a support for balance if needed.



        2. EXECUTING THE LIFT

        - Raise your heels as high as possible by pushing through the balls of your feet.
        - Lower back down with control, stretching the calves fully at the bottom.



        3. SAFETY TIPS

        - Do not bounce at the bottom of the movement; control both the ascent and descent.
        - Avoid locking your knees; keep a slight bend throughout the movement.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR CALF RAISES",
            """
        - Focus on fully extending your calves at the top and fully stretching them at the bottom.
        - Perform the movement slowly to maximize the time under tension.
        """
        )

        app.mainloop()
        pass
    def day3():
        ##DAY3


        app = ctk.CTkToplevel()
        app.title("Day 3: Pull Day (Back, Biceps, Rear Delts) - Strength and Volume Focus 💪")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 3: Pull Day (Back, Biceps, Rear Delts) - Strength and Volume Focus 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Deadlifts",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("deadlift.jpg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A DEADLIFT?",
            """
        The deadlift is one of the best compound exercises for building full-body strength. It primarily targets the posterior chain, including the hamstrings, glutes, and lower back, while also engaging the traps, core, and forearms.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A DEADLIFT",
            """
        1. SET UP YOUR FEET

        - Stand with your feet hip-width apart, barbell close to your shins.
        - Grip the barbell with both hands slightly outside your knees.



        2. EXECUTING THE LIFT

        - Engage your lats, pull your chest up, and drive through your legs and hips to lift the barbell.
        - Stand tall, keeping the barbell close to your body and maintaining a neutral spine.



        3. LOWERING THE BARBELL

        - Reverse the movement by hinging at the hips first and then bending the knees to lower the barbell with control.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DEADLIFTS",
            """
        - Always keep your back straight and your core braced.
        - Avoid jerking or rounding your back during the lift.
        - Use a mixed grip (one palm facing up, one facing down) if lifting heavy.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Pull-Ups (Weighted, If Possible)",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("pullup.jpg")  
        exercise2_img = exercise2_img.resize((700, 300))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE PULL-UPS?",
            """
        Pull-ups are a fundamental bodyweight exercise that primarily target the back muscles, specifically the lats, traps, and rear delts. Adding weight can increase the intensity, leading to greater muscle growth.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A PULL-UP",
            """
        1. SET UP

        - Grab the pull-up bar with your palms facing away from your body (overhand grip), hands slightly wider than shoulder-width apart.
        - Hang freely with your arms fully extended and your body slightly engaged.



        2. EXECUTING THE LIFT

        - Pull your body upwards by driving your elbows down towards your sides.
        - Keep your chest up and avoid swinging your body. Engage your core throughout the movement.



        3. LOWERING YOURSELF

        - Slowly lower your body back to the starting position, ensuring your arms are fully extended before starting the next rep.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR PULL-UPS",
            """
        - Engage your lats and avoid using your arms excessively.
        - Focus on controlled movements rather than rapid swings.
        - Perform the movement in a slow and deliberate manner for optimal muscle activation.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Bent-over Rows",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("bentoverrows.jpg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE BENT-OVER ROWS?",
            """
        Bent-over rows are a key exercise for developing thickness in the upper back, particularly targeting the lats, rhomboids, and traps. They also engage the lower back and core for stability.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A BENT-OVER ROW",
            """
        1. SET UP YOUR FEET

        - Stand with your feet hip-width apart and bend at the hips until your torso is almost parallel to the ground.
        - Hold a barbell or dumbbells with an overhand grip, palms facing down.



        2. EXECUTING THE LIFT

        - Pull the barbell or dumbbells towards your lower ribcage, driving your elbows back and squeezing your shoulder blades together.
        - Lower the weight back down with control.



        3. SAFETY TIPS

        - Keep your back flat and avoid rounding your lower back.
        - Do not jerk the weight up; control the movement throughout.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR BENT-OVER ROWS",
            """
        - Keep your core engaged to protect your lower back.
        - Focus on using your back muscles to pull the weight, not your arms.
        - Keep your elbows close to your body during the row.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Dumbbell Shrugs",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("shrugs.jpg")  
        exercise4_img = exercise4_img.resize((700, 300))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE DUMBBELL SHRUGS?",
            """
        Dumbbell shrugs are an excellent exercise for building the traps and improving shoulder stability. They primarily target the upper traps, which can help create a broader, more defined upper back.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DUMBBELL SHRUGS",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart, holding a dumbbell in each hand with your arms fully extended.
        - Let the dumbbells hang naturally at your sides.



        2. EXECUTING THE LIFT

        - Shrug your shoulders upward as high as possible while keeping your arms straight.
        - Hold the contraction for a second before lowering the weights back down with control.



        3. SAFETY TIPS

        - Avoid using momentum or jerking your shoulders up.
        - Focus on squeezing the traps at the top of the movement.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DUMBBELL SHRUGS",
            """
        - Perform the movement slowly and with full control.
        - Do not roll your shoulders; simply lift them straight up and down.
        - Use a weight that allows for a controlled motion without excessive swinging.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Barbell Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("barbell_curls.jpg")  
        exercise5_img = exercise5_img.resize((700, 300))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE BARBELL CURLS?",
            """
        Barbell curls are one of the most effective exercises for isolating the biceps. This exercise helps build mass in the upper arm and can be performed with various grips to target different parts of the biceps.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A BARBELL CURL",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart, gripping the barbell with an underhand (supine) grip, hands shoulder-width apart.



        2. EXECUTING THE LIFT

        - Curl the barbell upward by contracting your biceps, keeping your elbows close to your torso.
        - Focus on squeezing the biceps at the top of the movement before lowering the barbell slowly.



        3. SAFETY TIPS

        - Avoid swinging your body or using momentum to lift the barbell.
        - Keep your elbows locked in place and avoid letting them drift forward.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR BARBELL CURLS",
            """
        - Perform the movement slowly and with full control.
        - Use a grip that feels comfortable and strong.
        - Focus on squeezing the biceps at the top of the curl.
        """
        )

        app.mainloop()
        pass
    def day4():
        # ##DAY 4

        app = ctk.CTkToplevel()
        app.title("Day 4: Active Recovery (Yoga/Stretching/Light Cardio) 🌿")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 4: Active Recovery (Yoga/Stretching/Light Cardio) 🌿",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Light Yoga or Stretching Session (30 minutes)",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("yog.jpg")  # Replace with actual image path
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS ACTIVE RECOVERY?",
            """
        Active recovery is a low-intensity form of exercise that helps promote blood flow, improve flexibility, and reduce soreness in the muscles. On this day, we focus on activities that improve mobility and recovery without putting too much strain on the body.
        """
        )

        create_section(
            scrollable_frame,
            "BENEFITS OF YOGA AND STRETCHING",
            """
        - Reduces muscle tension and stiffness.
        - Improves joint mobility and flexibility.
        - Aids in muscle recovery and reduces soreness.
        - Helps improve mental focus and relaxation.
        """
        )

        create_section(
            scrollable_frame,
            "SUGGESTED YOGA POSES AND STRETCHES",
            """
        1. **Downward Dog (Adho Mukha Svanasana)**: Stretches your back, hamstrings, and calves.

        2. **Cat-Cow Stretch (Marjaryasana-Bitilasana)**: A gentle movement to mobilize the spine.

        3. **Child's Pose (Balasana)**: A resting pose that helps relax the body and mind.

        4. **Pigeon Pose (Eka Pada Rajakapotasana)**: Opens up the hips and glutes.

        5. **Standing Forward Fold (Uttanasana)**: A deep hamstring stretch.

        6. **Seated Forward Fold (Paschimottanasana)**: Targets the hamstrings and lower back.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM YOGA AND STRETCHES",
            """
        1. Start with **gentle movements** and gradually move into deeper stretches.

        2. Focus on **breathing** and hold each stretch for 20-30 seconds.

        3. For yoga poses, ensure you maintain a **neutral spine** and focus on **proper alignment** to prevent injury.

        4. Include **mindfulness and breathing techniques** to reduce stress and improve recovery.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Low-Intensity Cardio (Walking or Cycling - 20 minutes)",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("walk.jpeg")  # Replace with actual image path
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS LOW-INTENSITY CARDIO?",
            """
        Low-intensity cardio involves activities like walking, cycling, or swimming at a relaxed pace. It is designed to get your heart rate up slightly while not straining the body, promoting recovery and enhancing overall circulation.
        """
        )

        create_section(
            scrollable_frame,
            "BENEFITS OF LOW-INTENSITY CARDIO",
            """
        - Improves circulation and nutrient delivery to muscles.
        - Reduces muscle stiffness and promotes recovery.
        - Enhances overall cardiovascular health.
        - Helps clear lactic acid build-up from intense workouts.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM LOW-INTENSITY CARDIO",
            """
        1. **Walking**: Maintain a moderate pace, not too slow but not too fast. Aim to keep your heart rate at a steady, comfortable level.

        2. **Cycling**: Keep the resistance low and the pace steady. Pedal at a comfortable rate for about 20 minutes.

        3. Focus on **proper posture** while performing any cardio exercises.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Mobility Exercises or Foam Rolling (10-20 minutes)",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("foam.jpg")  # Replace with actual image path
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE MOBILITY EXERCISES AND FOAM ROLLING?",
            """
        Mobility exercises help increase joint range of motion, whereas foam rolling is a form of self-myofascial release that targets muscle tightness and helps release knots or trigger points. These exercises are crucial for preventing injuries and maintaining flexibility.
        """
        )

        create_section(
            scrollable_frame,
            "BENEFITS OF MOBILITY AND FOAM ROLLING",
            """
        - Improves range of motion in joints and muscles.
        - Helps release muscle knots and tightness.
        - Reduces soreness and prevents injury.
        - Enhances circulation and promotes quicker recovery.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM FOAM ROLLING AND MOBILITY EXERCISES",
            """
        1. **Foam Rolling**: Roll slowly over each muscle group for about 30-60 seconds. Focus on any tight or sore areas. 

        2. **Mobility Exercises**: Perform exercises that involve controlled movements of the joints, such as hip circles or shoulder rotations, to improve range of motion.

        3. Use a foam roller on **muscle groups** such as the quads, hamstrings, calves, and upper back.
        """
        )

        app.mainloop()
        pass
    def day5():
        ##DAY 5

        app = ctk.CTkToplevel()
        app.title("Day 5: Full Body Power Day (Heavy Compound Lifts)")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 5: Full Body Power Day (Heavy Compound Lifts) 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Squats",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("squats1.jpg")
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A SQUAT?",
            """
        Squats are a compound exercise that primarily targets the quadriceps, hamstrings, and glutes. It also engages the lower back, core, and calves. As a fundamental movement pattern, squats help build strength in the lower body and improve overall functional fitness.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A SQUAT",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart, toes slightly turned outward.
        - Keep your chest up, shoulders back, and core engaged.



        2. EXECUTING THE LIFT

        - Lower Down: Push your hips back as if sitting into a chair, bending at the knees while keeping your chest upright.
        - Depth: Lower until your thighs are parallel to the floor or deeper, depending on flexibility and mobility.



        3. RISING BACK UP

        - Push Up: Drive through your heels to return to the standing position, fully extending your knees and hips.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR SQUATS",
            """
        - Keep your knees tracking over your toes to avoid unnecessary stress on the joints.
        - Maintain a neutral spine throughout the movement to protect your lower back.
        - If using weights, keep the barbell balanced over your mid-foot.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Bench Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("benchpress.jpg")
        exercise2_img = exercise2_img.resize((700, 300))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A BENCH PRESS?",
            """
        The bench press is a compound upper body exercise that primarily targets the chest, shoulders, and triceps. It is performed by lying on a bench and pressing a barbell or dumbbells upward, making it one of the most effective exercises for building upper body strength.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A BENCH PRESS",
            """
        1. SET UP

        - Lie flat on a bench with your feet firmly on the ground. Grab the barbell with a grip slightly wider than shoulder-width apart.
        - Lower the bar to your chest with control, keeping your elbows at a 45-degree angle from your body.



        2. EXECUTING THE PRESS

        - Press Up: Push the barbell back up to the starting position, extending your arms fully without locking your elbows.
        - Full Extension: Keep your shoulders and core tight while pressing the weight upward.



        3. LOWERING THE BARBELL

        - Lower the barbell slowly to your chest, maintaining control throughout the movement.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR BENCH PRESS",
            """
        - Keep your wrists straight and avoid letting the bar drift too far forward or back.
        - Maintain consistent tension in your chest and arms throughout the press.
        - Avoid bouncing the bar off your chest; control the descent for better muscle engagement.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Deadlifts",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("deadlift.jpg")
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A DEADLIFT?",
            """
        Deadlifts are a compound lift that primarily targets the posterior chain, including the hamstrings, glutes, lower back, and traps. It is one of the most effective exercises for building overall strength and power in the body.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A DEADLIFT",
            """
        1. SET UP

        - Stand with your feet hip-width apart, barbell over the mid-foot. Grab the bar with a mixed or double overhand grip.
        - Keep your chest up, shoulders back, and hips slightly lower than your shoulders.



        2. EXECUTING THE LIFT

        - Lift the Bar: Push through your heels and engage your glutes and hamstrings to pull the bar up.
        - Lockout: At the top, fully extend your hips and stand tall without arching your back.



        3. LOWERING THE BAR

        - Control the Descent: Lower the bar back to the floor with control, maintaining a neutral spine and keeping the bar close to your body.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR DEADLIFTS",
            """
        - Keep your back straight and avoid rounding your lower back during the lift.
        - Focus on driving through your heels, not your toes, to activate the posterior chain properly.
        - Keep the bar as close to your body as possible throughout the lift.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Barbell Rows",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("barbellrows.jpg")
        exercise4_img = exercise4_img.resize((700, 600))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A BARBELL ROW?",
            """
        Barbell rows are a compound exercise that targets the upper and middle back, including the lats, traps, and rhomboids. It also works the biceps and forearms as secondary muscles.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A BARBELL ROW",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart and grip the barbell with your hands slightly wider than shoulder-width apart.
        - Hinge forward at the hips, keeping your back flat and your chest up.



        2. EXECUTING THE LIFT

        - Row the Barbell: Pull the bar towards your lower chest or upper stomach, keeping your elbows close to your body.
        - Full Contraction: Squeeze your shoulder blades together at the top of the movement.



        3. LOWERING THE BARBELL

        - Slowly lower the barbell back down to the starting position with control, maintaining a flat back.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR BARBELL ROWS",
            """
        - Keep your back flat and avoid rounding your spine during the lift.
        - Focus on pulling with your back muscles, not just your arms.
        - Avoid swinging your body to generate momentum; perform the movement slowly for maximum effectiveness.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Overhead Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("overhead.jpg")
        exercise5_img = exercise5_img.resize((700, 600))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS AN OVERHEAD PRESS?",
            """
        The overhead press is a compound exercise that targets the shoulders, triceps, and upper chest. It is performed by pressing a barbell or dumbbells overhead, engaging the shoulders and upper body muscles.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM AN OVERHEAD PRESS",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart, grip the barbell with a slightly wider-than-shoulder-width grip.
        - Begin with the barbell at shoulder height, elbows slightly forward, and core engaged.



        2. EXECUTING THE PRESS

        - Press Up: Drive the barbell overhead until your arms are fully extended, keeping your core tight and back straight.
        - Full Extension: Avoid arching your lower back during the press.



        3. LOWERING THE BARBELL

        - Lower the barbell back to shoulder height with control, maintaining a steady pace.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR OVERHEAD PRESS",
            """
        - Avoid leaning back excessively to prevent strain on the lower back.
        - Keep the bar close to your body and press it in a straight line upwards.
        - Keep your core engaged throughout the movement for stability.
        """
        )

        app.mainloop()

        pass
    def day6():
        ##DAY 6

        app = ctk.CTkToplevel()
        app.title("Day 6: Arms and Core (Isolation Focus)")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 6: Arms and Core (Isolation Focus) 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Barbell Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("barbell_curls1.jpg")
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A BARBELL CURL?",
            """
        Barbell curls are an isolation exercise targeting the biceps. It involves curling a barbell upwards to build strength and mass in the upper arms.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A BARBELL CURL",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart, holding a barbell with an underhand (supine) grip, hands just wider than shoulder-width apart.
        - Keep your elbows close to your torso and your back straight.



        2. CURLING THE BARBELL

        - Curl the barbell upward by flexing your elbows while keeping your upper arms stationary.
        - Squeeze your biceps at the top of the movement.



        3. LOWERING THE BARBELL

        - Lower the barbell with control back to the starting position, maintaining tension in the biceps.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR BARBELL CURLS",
            """
        - Keep your elbows stationary throughout the movement to ensure that the biceps do the work.
        - Don't use momentum to lift the weight; focus on controlled, deliberate movements.
        - Keep your core tight to avoid swinging your body.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Hammer Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("hammer_curls.jpg")
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A HAMMER CURL?",
            """
        Hammer curls are a variation of the traditional curl, targeting the brachialis and brachioradialis muscles in addition to the biceps.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A HAMMER CURL",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart and hold a dumbbell in each hand, palms facing your torso (neutral grip).
        - Keep your elbows close to your torso and your back straight.



        2. CURLING THE DUMBBELLS

        - Curl the dumbbells upward while keeping your upper arms stationary.
        - Squeeze your biceps at the top of the movement.



        3. LOWERING THE DUMBBELLS

        - Lower the dumbbells with control to the starting position, maintaining tension in the arms.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR HAMMER CURLS",
            """
        - Keep your palms facing each other throughout the movement to fully target the brachialis and brachioradialis.
        - Perform the movement slowly and with control to maximize muscle activation.
        - Avoid using momentum or swinging your arms.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Tricep Rope Pushdowns",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("rope.jpg")
        exercise3_img = exercise3_img.resize((700, 300))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A TRICEP ROPE PUSHDOWN?",
            """
        Tricep rope pushdowns are an isolation exercise targeting the triceps. Using a rope attachment on a cable machine, the triceps are engaged as the rope is pulled downward.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A TRICEP ROPE PUSHDOWN",
            """
        1. SET UP

        - Stand facing a cable machine with the rope attachment at the highest setting.
        - Grip the rope with both hands and keep your elbows close to your torso.



        2. EXECUTING THE PUSHDOWN

        - Pull the rope downward until your arms are fully extended and your triceps are engaged.
        - At the bottom, spread the rope apart to maximize tricep activation.



        3. RETURN TO STARTING POSITION

        - Slowly return the rope to the starting position, maintaining tension in the triceps.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR TRICEP ROPE PUSHDOWN",
            """
        - Keep your elbows stationary throughout the movement to isolate the triceps.
        - Focus on squeezing your triceps at the bottom of the movement.
        - Avoid letting the rope pull you back; control the weight in both directions.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Plank",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("plank.jpg")
        exercise4_img = exercise4_img.resize((700, 300))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT IS A PLANK?",
            """
        The plank is an isometric core exercise that targets the abdominals, obliques, and lower back. It improves core strength and stability.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM A PLANK",
            """
        1. SET UP

        - Begin in a push-up position, but with your forearms on the ground and your body in a straight line from head to heels.
        - Keep your elbows under your shoulders, and engage your core, glutes, and legs.



        2. HOLDING THE PLANK

        - Hold the position for as long as you can, keeping your body straight and avoiding sagging at the hips or arching the back.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR PLANK",
            """
        - Engage your core and glutes to maintain proper alignment.
        - Avoid holding your breath; continue to breathe steadily while maintaining tension in your core.
        - If needed, modify the plank by dropping to your knees for a less intense version.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Russian Twists (Weighted)",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("russian.jpg")
        exercise5_img = exercise5_img.resize((700, 600))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE RUSSIAN TWISTS?",
            """
        Russian twists are a dynamic core exercise that engages the obliques and helps improve rotational strength and stability.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM RUSSIAN TWISTS",
            """
        1. SET UP

        - Sit on the floor with your knees bent and feet flat. Lean back slightly to create an angle in your torso.
        - Hold a weight (plate, dumbbell, or medicine ball) with both hands, keeping your arms extended.



        2. TWISTING THE TORSO

        - Rotate your torso to the right, bringing the weight to your side, then twist to the left.
        - Keep your core tight and engage your obliques with each twist.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR RUSSIAN TWISTS",
            """
        - Keep your chest upright and avoid rounding your back.
        - Focus on twisting from your torso, not just your arms.
        - Use a weight that challenges you but allows for controlled movements.
        """
        )

        app.mainloop()
        pass
    def day7():
        app = ctk.CTkToplevel()
        app.title("Day 7: Rest and Recovery")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 7: Rest and Recovery 🧘‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        create_section(
            scrollable_frame,
            "Rest and Recovery Focus",
            """
        Day 7 is all about taking the time to rest and recover. It is important to allow your muscles and body to recuperate fully after intense training.
        On this day, focus on gentle movement, relaxation, and mental restoration.
        """
        )

        create_section(
            scrollable_frame,
            "Mobility and Foam Rolling (10-20 minutes)",
            """
        Spend 10-20 minutes focusing on mobility exercises and foam rolling to relieve tightness and improve flexibility. 
        Foam rolling helps increase blood flow to the muscles, aiding recovery and reducing soreness. 
        You can roll out areas such as your calves, quads, hamstrings, back, and shoulders.
        """
        )

        create_section(
            scrollable_frame,
            "Relax and Mentally Reset",
            """
        This is a time for mental recovery. Engage in relaxing activities such as deep breathing exercises, meditation, or reading.
        Taking a mental break is essential for reducing stress, improving focus, and resetting your mindset for the next training cycle.
        """
        )

        create_section(
            scrollable_frame,
            "Additional Recovery Tips",
            """
        - Ensure you are drinking plenty of water throughout the day to stay hydrated.
        - Aim for 7-9 hours of quality sleep to support muscle repair and recovery.
        - Eat nutrient-dense foods, rich in protein and healthy fats, to help your muscles rebuild.
        """
        )

        app.mainloop()

        pass
    days=[day1,day2,day3,day4,day5,day6,day7]
    for i, day in enumerate(days):
        button = ctk.CTkButton(app, text=f"Day{i+1}", font=("Arial", 14), width=200,command=day)
        button.pack(pady=10)

    pass

def weight_loss_beginner():
    def day1():
        ## DAY 1

        app = ctk.CTkToplevel()
        app.title("Day 1: Cardio (Beginner - Brisk Walking)")
        app.geometry("900x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 1: Cardio (Beginner - Brisk Walking) 🚶‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Brisk Walking",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("walk.jpeg")  
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM BRISK WALKING",
            """
        1. WARM-UP

        - Start with 5 minutes of slow walking to prepare your body.



        2. MAIN ACTIVITY

        - Walk at a pace that raises your heart rate, but still allows you to hold a conversation.
        - Maintain a brisk but sustainable pace for the entire session.



        3. COOL-DOWN

        - Finish with 5 minutes of slow walking to bring your heart rate down.



        4. TIPS

        - Wear comfortable shoes for support.
        - Maintain good posture with shoulders relaxed and back straight.
        - Stay hydrated before, during, and after the walk.
        """
        )

        app.mainloop()
        pass
    def day2():
        ##DAY 2

        app = ctk.CTkToplevel()
        app.title("Day 2: Full Body Strength Training (Beginner)")
        app.geometry("900x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 2: Full Body Strength Training 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Bodyweight Squats",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("squates.jpeg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM BODYWEIGHT SQUATS",
            """
        1. Stand with feet shoulder-width apart.

        2. Lower your body by bending your knees and hips, keeping your back straight.

        3. Return to standing position.

        4. Maintain your knees over your toes throughout the movement.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Push-Ups",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("push_up.jpeg")  
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM PUSH-UPS",
            """
        1. Start in a plank position with hands directly under your shoulders.

        2. Lower your body until your chest nearly touches the floor.

        3. Push back up to the starting position.

        4. Keep your body in a straight line and avoid flaring your elbows.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Dumbbell Rows",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("dumbbell_rows.jpeg") 
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DUMBBELL ROWS",
            """
        1. Bend at the waist, holding a dumbbell in one hand.

        2. Pull the dumbbell towards your hip and lower it back down.

        3. Keep your back flat and core engaged throughout the movement.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Plank",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("plank.jpg")  
        exercise4_img = exercise4_img.resize((700, 600))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM PLANK",
            """
        1. Start in a forearm plank position.

        2. Keep your body in a straight line from head to heels.

        3. Engage your core and hold the position.

        4. Avoid letting your hips sag or rise.
        """
        )

        app.mainloop()
        pass
    def day3():
        ##DAY 3

        app = ctk.CTkToplevel()
        app.title("Day 3: Cardio (HIIT)")
        app.geometry("900x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 3: Cardio (HIIT) 🏃‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#ff9900"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)


        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Jumping Jacks",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("plank_jack.jpeg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM JUMPING JACKS",
            """
        1. Stand with your feet together and arms at your sides.

        2. Jump up, spreading your feet to shoulder-width apart while raising your arms overhead.

        3. Jump again to return to the starting position.

        4. Keep your movements controlled and rhythmic.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. High Knees",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("high_knees.jpeg") 
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM HIGH KNEES",
            """
        1. Stand with your feet hip-width apart.

        2. Lift your right knee towards your chest.

        3. Quickly switch to lift your left knee towards your chest while lowering your right leg.

        4. Keep your back straight and core engaged.
        """
        )


        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Mountain Climbers",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("mountain_climbers.jpeg")  
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM MOUNTAIN CLIMBERS",
            """
        1. Start in a high plank position with your hands directly under your shoulders.

        2. Bring your right knee towards your chest.

        3. Quickly switch legs, bringing your left knee towards your chest while extending your right leg back.

        4. Keep your hips level and engage your core.
        """
        )


        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Rest",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO REST",
            """
        1. Take a 30-second rest between each exercise.

        2. Use this time to catch your breath and prepare for the next exercise.

        3. Stay hydrated and keep moving lightly to prevent muscles from cooling down.

        4. Focus on deep, steady breathing.
        """
        )


        create_section(
            scrollable_frame,
            "HIIT CIRCUIT",
            """
        1. Perform each exercise for 30 seconds.

        2. Rest for 30 seconds between exercises.

        3. Repeat the circuit 4-5 times.

        4. Warm-up before and cool down after the HIIT circuit.

        5. Modify the intensity if needed and listen to your body.
        """
        )

        app.mainloop()
        pass
    def day4():
        ##DAY 4

        app = ctk.CTkToplevel()
        app.title("Day 4: Active Recovery (Yoga/Stretching)")
        app.geometry("900x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 4: Active Recovery (Yoga/Stretching) 🧘‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#ff9900"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Child's Pose",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("child_pose.jpeg")
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM CHILD'S POSE",
            """
        1. Kneel on the floor with your big toes touching and knees apart.

        2. Sit back on your heels and stretch your arms forward.

        3. Lower your torso between your thighs and rest your forehead on the floor.

        4. Hold for 1-2 minutes, breathing deeply.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Downward Dog",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("downward_dog.jpeg")
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DOWNWARD DOG",
            """
        1. Start on your hands and knees.

        2. Lift your hips up and back, straightening your legs.

        3. Press your heels towards the floor and extend your arms.

        4. Hold for 1-2 minutes, breathing deeply.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Cat-Cow Stretch",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("cat.jpg")
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM CAT-COW STRETCH",
            """
        1. Start on your hands and knees with wrists under shoulders and knees under hips.

        2. Inhale, arch your back, lifting your head and tailbone (Cow Pose).

        3. Exhale, round your back, tucking chin and tailbone (Cat Pose).

        4. Alternate between Cat and Cow poses for 1-2 minutes.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Seated Forward Bend",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("seated_forward_bend.jpeg")
        exercise4_img = exercise4_img.resize((700, 600))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM SEATED FORWARD BEND",
            """
        1. Sit on the floor with legs extended in front of you.

        2. Inhale and lengthen your spine.

        3. Exhale and hinge at your hips to reach for your toes.

        4. Hold for 1-2 minutes, breathing deeply.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Pigeon Pose",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("pigeon_pose.jpeg")
        exercise5_img = exercise5_img.resize((700, 600))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM PIGEON POSE",
            """
        1. Start in a plank position.

        2. Bring your right knee forward and place it behind your right wrist.

        3. Extend your left leg back, keeping your hips square.

        4. Lower your torso over your right leg and rest on forearms or forehead.

        5. Hold for 1-2 minutes, then switch sides.
        """
        )

        create_section(
            scrollable_frame,
            "TIPS FOR ACTIVE RECOVERY",
            """
        1. Focus on breathing: Deep, steady breathing helps relax your muscles.

        2. Stay hydrated: Drink plenty of water to aid muscle recovery.

        3. Listen to your body: Stretch gently and avoid discomfort.
        """
        )

        app.mainloop()
        pass
    def day5():
        ##DAY 5

        app = ctk.CTkToplevel()
        app.title("Day 5: Lower Body Strength Training")
        app.geometry("900x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 5: Lower Body Strength Training 💪",
            font=("Arial", 28, "bold"),
            text_color="#ff9900"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Lunges",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("lunges.jpg")
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM LUNGES",
            """
        1. Step forward with one leg.

        2. Lower your hips until both knees are bent at 90 degrees.

        3. Return to standing.

        4. Perform 3 sets of 12 reps per leg.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Glute Bridges",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("glute_bridges.jpeg")
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM GLUTE BRIDGES",
            """
        1. Lie on your back with knees bent.

        2. Lift your hips towards the ceiling.

        3. Lower your hips back down.

        4. Perform 3 sets of 15 reps.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Calf Raises",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("calf_raises.jpeg")
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM CALF RAISES",
            """
        1. Stand with feet hip-width apart.

        2. Raise your heels off the ground.

        3. Lower them back down.

        4. Perform 3 sets of 15 reps.
        """
        )

        app.mainloop()
        pass
    def day6():
        ##DAY 6

        app = ctk.CTkToplevel()
        app.title("Day 6: Upper Body Strength Training")
        app.geometry("900x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 6: Upper Body Strength Training 💪",
            font=("Arial", 28, "bold"),
            text_color="#ff9900"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Bicep Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("bicep_curls.jpeg")
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM BICEP CURLS",
            """
        1. Stand with a dumbbell in each hand.

        2. Curl the weights towards your shoulders.

        3. Lower them back down.

        4. Perform 3 sets of 12 reps.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Tricep Dips",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("tricep_dips.jpeg")
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM TRICEP DIPS",
            """
        1. Sit on the edge of a bench.

        2. Slide your hips off and lower your body by bending your elbows.

        3. Push back up.

        4. Perform 3 sets of 10 reps.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Shoulder Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("shoulder_press.jpeg")
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM SHOULDER PRESS",
            """
        1. Stand with a dumbbell in each hand at shoulder height.

        2. Press the weights overhead.

        3. Lower them back down.

        4. Perform 3 sets of 12 reps.
        """
        )

        app.mainloop()
        pass
    def day7():
        ##DAY7

        app = ctk.CTkToplevel()
        app.title("Day 7: Cardio (Steady-State) + Mobility Work")
        app.geometry("900x900")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 7: Cardio (Steady-State) + Mobility Work 🏃‍♂️🚴‍♀️",
            font=("Arial", 28, "bold"),
            text_color="#ff9900"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        # Steady-State Cardio Section
        cardio_title = ctk.CTkLabel(
            scrollable_frame,
            text="Steady-State Cardio: Jogging or Cycling",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        cardio_title.pack(pady=10)

        create_section(
            scrollable_frame,
            "How to Perform Steady-State Cardio",
            """
        1. Warm-Up: 5-10 minutes of light jogging or brisk walking.

        2. Main Activity: Jog or cycle at a steady, moderate pace for 30-45 minutes.

        3. Cool-Down: 5-10 minutes of light jogging or walking.
        """
        )

        # Mobility Work Section
        mobility_title = ctk.CTkLabel(
            scrollable_frame,
            text="Mobility Work",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        mobility_title.pack(pady=10)

        create_section(
            scrollable_frame,
            "1. Hip Circles",
            """
        1. Stand with your feet shoulder-width apart.

        2. Rotate your hips in large circles, 10-15 times in each direction.
        """
        )

        create_section(
            scrollable_frame,
            "2. Arm Circles",
            """
        1. Stand with feet shoulder-width apart and extend arms to the sides.

        2. Make small circles with your arms, gradually increasing the size.

        3. Perform 10-15 circles in each direction.
        """
        )

        create_section(
            scrollable_frame,
            "3. Thoracic Rotations",
            """
        1. Start on your hands and knees.

        2. Place one hand behind your head and rotate your upper body, bringing your elbow toward the ceiling.

        3. Repeat on the other side.
        """
        )

        create_section(
            scrollable_frame,
            "4. Ankle Circles",
            """
        1. Sit or stand with one leg lifted off the ground.

        2. Rotate your ankle in large circles, 10-15 times in each direction.
        """
        )

        create_section(
            scrollable_frame,
            "5. Deep Squat Hold",
            """
        1. Stand with your feet shoulder-width apart.

        2. Lower your body into a deep squat position, keeping your heels on the ground.

        3. Hold the position for 1-2 minutes.
        """
        )

        app.mainloop()
        pass
    days=[day1,day2,day3,day4,day5,day6,day7]
    for i, day in enumerate(days):
        button = ctk.CTkButton(app, text=f"Day{i+1}", font=("Arial", 14), width=200,command=day)
        button.pack(pady=10)


    pass

def weight_loss_advanced():
    def day1():
        # #DAY 1


        app = ctk.CTkToplevel()
        app.title("Day 1: Full Body Strength Training + Cardio")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 1: Full Body Strength Training + Cardio 🏋️‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Squats",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("squats.jpg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE SQUATS?",
            """
        Squats are a compound exercise that primarily targets the quadriceps, hamstrings, and glutes, while also engaging the core. Squats are foundational for building lower body strength and improving functional movement.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM SQUATS",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart and your toes slightly pointed outwards.
        - Keep your chest up and core braced.



        2. EXECUTING THE MOVEMENT

        - Lower your hips back and down as if sitting into a chair, keeping your knees in line with your toes.
        - Descend until your thighs are parallel to the ground or lower, if comfortable.
        - Push through your heels to return to the standing position.



        3. TIPS FOR BETTER SQUATS

        - Keep your weight evenly distributed across your feet.
        - Avoid letting your knees cave inward or your chest collapse forward.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Push-Ups",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("pushups.jpeg")  
        exercise2_img = exercise2_img.resize((700, 300))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE PUSH-UPS?",
            """
        Push-ups are a bodyweight exercise targeting the chest, shoulders, triceps, and core. They are a versatile exercise that can be scaled for different difficulty levels.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM PUSH-UPS",
            """
        1. SET UP

        - Place your hands slightly wider than shoulder-width apart on the floor, and extend your legs back into a plank position.
        - Keep your body straight from head to heels and engage your core.



        2. EXECUTING THE MOVEMENT

        - Lower your chest towards the ground by bending your elbows, keeping them at about a 45-degree angle.
        - Push through your hands to return to the starting position.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Deadlifts",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("deadlift.jpg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "WHAT ARE DEADLIFTS?",
            """
        Deadlifts are a compound movement targeting the posterior chain, including the hamstrings, glutes, and lower back. They are excellent for building total body strength and improving posture.
        """
        )

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DEADLIFTS",
            """
        1. SET UP

        - Stand with your feet hip-width apart and the barbell close to your shins.
        - Bend your hips and knees to grip the bar with both hands just outside your legs.



        2. EXECUTING THE MOVEMENT

        - Lift the bar by driving through your heels, extending your hips and knees simultaneously.
        - Keep your back flat and your core braced throughout.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. 10-Minute Cardio Session",
            font=("Arial", 22, "bold"),
            text_color="#ffaa00"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("cardio.jpeg")  # Replace with the actual cardio image filename
        exercise4_img = exercise4_img.resize((700, 500))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "CARDIO ROUTINE",
            """
        - Jumping Jacks: 1 minute
        - High Knees: 1 minute
        - Burpees: 30 seconds
        - Rest: 30 seconds
        (Repeat 3 rounds)
        """
        )

        app.mainloop()
        pass
    def day2():
        ##DAY 2

        app = ctk.CTkToplevel()
        app.title("Day 2: Full Body Strength Training")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 2: Full Body Strength Training 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Bodyweight Squats",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("squats.jpg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM BODYWEIGHT SQUATS",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart.
        - Keep your chest up, and your arms can be extended forward for balance.



        2. EXECUTING THE MOVEMENT

        - Lower your body by bending your knees and hips.
        - Continue lowering until your thighs are parallel to the ground, keeping your knees in line with your toes.
        - Push through your heels to return to the standing position.



        3. TIPS

        - Keep your back straight and engage your core.
        - Avoid letting your knees cave inward during the squat.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Push-Ups",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("pushups.jpeg")  
        exercise2_img = exercise2_img.resize((700, 300))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM PUSH-UPS",
            """
        1. SET UP

        - Start in a plank position with your hands slightly wider than shoulder-width apart.
        - Engage your core and keep your body in a straight line from head to heels.



        2. EXECUTING THE MOVEMENT

        - Lower your body towards the ground by bending your elbows.
        - Once your chest is nearly touching the floor, push back up to the starting position.
        - Avoid flaring your elbows out.



        3. TIPS

        - Keep your body in a straight line throughout the movement.
        - Engage your core and avoid letting your hips sag.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Dumbbell Rows",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("rows.jpg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DUMBBELL ROWS",
            """
        1. SET UP

        - Hold a dumbbell in one hand and bend at the waist with your opposite hand supported on a bench.
        - Keep your back flat and your core engaged.



        2. EXECUTING THE MOVEMENT

        - Pull the dumbbell towards your hip, keeping your elbow close to your body.
        - Lower the dumbbell back down to the starting position.
        - Repeat for the other arm.



        3. TIPS

        - Avoid twisting your torso; keep your back flat.
        - Engage your core to maintain stability throughout the movement.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Plank",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("plank.jpg")  
        exercise4_img = exercise4_img.resize((700, 600))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM PLANK",
            """
        1. SET UP

        - Start in a forearm plank position, with your elbows directly beneath your shoulders.
        - Engage your core and keep your body in a straight line from head to heels.



        2. EXECUTING THE MOVEMENT

        - Hold the plank position for the designated time (30 seconds).
        - Keep your hips aligned with your body to avoid sagging.



        3. TIPS

        - Keep your core tight and avoid letting your back arch or your hips drop.
        """
        )

        app.mainloop()
        pass
    def day3():
        ## DAY 3

        app = ctk.CTkToplevel()
        app.title("Day 3: Cardio (HIIT)")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 3: Cardio (HIIT) 🏃‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Jumping Jacks",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("jacks.jpeg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM JUMPING JACKS",
            """
        1. SET UP

        - Stand with your feet together and arms at your sides.
        - Keep your core engaged and your posture upright.



        2. EXECUTING THE MOVEMENT

        - Jump up, spreading your feet to shoulder-width apart while raising your arms overhead.
        - Jump again to return to the starting position.



        3. TIPS

        - Move rhythmically and land softly to reduce impact.
        - Maintain control over your movements and avoid excessive bouncing.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. High Knees",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("high_knees.jpeg")  
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM HIGH KNEES",
            """
        1. SET UP

        - Stand with your feet hip-width apart.
        - Keep your arms at your sides, ready to pump with your movement.



        2. EXECUTING THE MOVEMENT

        - Lift your right knee towards your chest and quickly switch to lift your left knee.
        - Continue alternating at a fast pace.



        3. TIPS

        - Engage your core and keep your back straight.
        - Pump your arms in sync with your legs for balance and momentum.
        - Aim to lift your knees to hip level or higher.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Mountain Climbers",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("mountain_climbers.jpeg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM MOUNTAIN CLIMBERS",
            """
        1. SET UP

        - Start in a high plank position, with your hands directly under your shoulders.
        - Engage your core and keep your body in a straight line.



        2. EXECUTING THE MOVEMENT

        - Bring your right knee towards your chest, then quickly switch legs.
        - Continue alternating legs at a steady pace.



        3. TIPS

        - Maintain a controlled and steady rhythm.
        - Avoid letting your hips sag or lifting them too high.
        - Keep your core tight for stability.
        """
        )

        hiit_circuit_title = ctk.CTkLabel(
            scrollable_frame,
            text="HIIT Circuit Instructions",
            font=("Arial", 22, "bold"),
            text_color="#ffaa00"
        )
        hiit_circuit_title.pack(pady=10)

        create_section(
            scrollable_frame,
            "CIRCUIT DETAILS",
            """
        - Perform each exercise for 30 seconds.
        - Rest for 30 seconds between exercises.
        - Complete 4-5 rounds of the circuit.

        TIPS:
        - Warm up before starting to prepare your muscles and joints.
        - Cool down after completing the circuit to gradually lower your heart rate.
        - Stay hydrated and listen to your body throughout.
        """
        )

        app.mainloop()
        pass
    def day4():
        ## DAY 4

        app = ctk.CTkToplevel()
        app.title("Day 4: Active Recovery (Yoga/Stretching)")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 4: Active Recovery (Yoga/Stretching) 🧘‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Child's Pose",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("child_pose.jpeg")  
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM CHILD'S POSE",
            """
        1. SET UP

        - Kneel on the floor with your big toes touching and knees apart.
        - Sit back on your heels and stretch your arms forward.



        2. EXECUTING THE MOVEMENT

        - Lower your torso between your thighs and rest your forehead on the floor.
        - Hold the position for 1-2 minutes while breathing deeply.



        3. TIPS

        - Relax your shoulders and neck.
        - Breathe deeply and evenly.
        - Use a cushion under your forehead for comfort.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Downward Dog",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("downward_dog.jpeg")  
        exercise2_img = exercise2_img.resize((700, 300))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DOWNWARD DOG",
            """
        1. SET UP

        - Start on your hands and knees.
        - Lift your hips up and back, straightening your legs.



        2. EXECUTING THE MOVEMENT

        - Press your heels towards the floor and extend your arms forward.
        - Hold the position for 1-2 minutes while breathing deeply.



        3. TIPS

        - Keep your spine long and straight.
        - Avoid locking your knees.
        - Engage your core and breathe deeply.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Cat-Cow Stretch",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("cat.jpg")  
        exercise3_img = exercise3_img.resize((700, 300))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM CAT-COW STRETCH",
            """
        1. SET UP

        - Start on your hands and knees with your wrists directly under your shoulders.
        - Keep your knees under your hips.



        2. EXECUTING THE MOVEMENT

        - Inhale and arch your back, lifting your head and tailbone (Cow Pose).
        - Exhale and round your back, tucking your chin and tailbone (Cat Pose).
        - Continue to alternate between Cat and Cow poses for 1-2 minutes.



        3. TIPS

        - Move smoothly between poses.
        - Keep your shoulders relaxed.
        - Breathe deeply and evenly.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Seated Forward Bend",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("seated_forward_bend.jpeg")  
        exercise4_img = exercise4_img.resize((700, 300))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM SEATED FORWARD BEND",
            """
        1. SET UP

        - Sit on the floor with your legs extended straight in front of you.
        - Inhale and lengthen your spine.



        2. EXECUTING THE MOVEMENT

        - Exhale and hinge at your hips to reach for your toes.
        - Hold the position for 1-2 minutes while breathing deeply.



        3. TIPS

        - Keep your back straight and avoid rounding your spine.
        - Reach as far as comfortable without forcing the stretch.
        - Use a strap around your feet if you can't reach your toes.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Pigeon Pose",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("pigeon_pose.jpeg")  
        exercise5_img = exercise5_img.resize((700, 300))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM PIGEON POSE",
            """
        1. SET UP

        - Start in a plank position.
        - Bring your right knee forward and place it behind your right wrist.
        - Extend your left leg back, keeping your hips square.



        2. EXECUTING THE MOVEMENT

        - Lower your torso over your right leg and rest on your forearms or forehead.
        - Hold the position for 1-2 minutes, then switch sides.



        3. TIPS

        - Keep your hips square to the floor.
        - Avoid forcing the stretch, go as deep as comfortable.
        - Use a cushion under your hip for support if needed.
        """
        )

        tips_title = ctk.CTkLabel(
            scrollable_frame,
            text="Tips for Active Recovery",
            font=("Arial", 22, "bold"),
            text_color="#ffaa00"
        )
        tips_title.pack(pady=10)

        create_section(
            scrollable_frame,
            "ACTIVE RECOVERY TIPS",
            """
        - Focus on Breathing: Deep, steady breathing helps relax your muscles and improve the effectiveness of the stretches.
        - Stay Hydrated: Drink plenty of water to help flush out toxins and aid in muscle recovery.
        - Listen to Your Body: Stretch gently and avoid any movements that cause pain or discomfort.
        """
        )

        app.mainloop()
        pass
    def day5():
        ##DAY 5

        app = ctk.CTkToplevel()
        app.title("Day 5: Lower Body Strength Training")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 5: Lower Body Strength Training 🦵",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Lunges",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("lunges.jpg")  
        exercise1_img = exercise1_img.resize((700, 300))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM LUNGES",
            """
        1. SET UP

        - Step forward with one leg, keeping your body upright.
        - Lower your hips until both knees are bent at 90 degrees.



        2. EXECUTING THE MOVEMENT

        - Push off your front leg to return to standing position.



        3. TIPS

        - Keep your front knee over your ankle.
        - Engage your core and keep your back straight.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Glute Bridges",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("glute_bridges.jpeg")  
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM GLUTE BRIDGES",
            """
        1. SET UP

        - Lie on your back with your knees bent and feet flat on the floor.
        - Place your arms at your sides for stability.



        2. EXECUTING THE MOVEMENT

        - Press through your heels to lift your hips toward the ceiling.
        - Lower your hips back down to the starting position.



        3. TIPS

        - Squeeze your glutes and engage your core as you lift.
        - Avoid arching your back excessively.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Calf Raises",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("calf_raises.jpeg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM CALF RAISES",
            """
        1. SET UP

        - Stand with your feet hip-width apart.
        - Keep your legs straight, engage your core.



        2. EXECUTING THE MOVEMENT

        - Raise your heels off the ground as high as possible.
        - Slowly lower your heels back to the floor.



        3. TIPS

        - Keep your movements controlled and avoid bouncing.
        - Focus on the contraction in your calves.
        """
        )

        app.mainloop()
        pass
    def day6():
        ##DAY 6

        app = ctk.CTkToplevel()
        app.title("Day 6: Upper Body Strength Training")
        app.geometry("900x700")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 6: Upper Body Strength Training 💪",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=550, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Bicep Curls",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("bicep_curls.jpeg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM BICEP CURLS",
            """
        1. SET UP

        - Stand with a dumbbell in each hand, palms facing forward.
        - Keep your elbows close to your body.



        2. EXECUTING THE MOVEMENT

        - Curl the weights towards your shoulders.
        - Lower the dumbbells back down with control.



        3. TIPS

        - Focus on squeezing your biceps at the top of the curl.
        - Avoid swinging your arms, keep the movement slow and controlled.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Tricep Dips",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("tricep_dips.jpeg")  
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM TRICEP DIPS",
            """
        1. SET UP

        - Sit on the edge of a bench or chair with your hands next to your hips.
        - Slide your hips off the edge, keeping your feet flat on the ground.



        2. EXECUTING THE MOVEMENT

        - Lower your body by bending your elbows at a 90-degree angle.
        - Push back up to return to the starting position.



        3. TIPS

        - Keep your elbows pointing straight back, not flaring out.
        - Engage your core to prevent your body from sinking.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Shoulder Press",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("shoulder_press.jpeg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM SHOULDER PRESS",
            """
        1. SET UP

        - Stand with a dumbbell in each hand at shoulder height.
        - Keep your elbows bent at a 90-degree angle.



        2. EXECUTING THE MOVEMENT



        - Press the dumbbells overhead until your arms are fully extended.
        - Lower the dumbbells back down to shoulder height.



        3. TIPS

        - Keep your core tight and avoid arching your back.
        - Perform the movement slowly and with control.
        """
        )

        app.mainloop()
        pass
    def day7():
        #DAY 7

        app = ctk.CTkToplevel()
        app.title("Day 7: Cardio (Steady-State) + Mobility Work")
        app.geometry("900x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        header = ctk.CTkLabel(
            main_frame,
            text="Day 7: Cardio (Steady-State) + Mobility Work 🏃‍♂️",
            font=("Arial", 28, "bold"),
            text_color="#00aaff"
        )
        header.pack(pady=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        def create_section(parent, title, content, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff"):
            title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
            title_label.pack(anchor="w", padx=20, pady=(10, 5))

            content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
            content_label.pack(anchor="w", padx=20, pady=5)

        exercise1_title = ctk.CTkLabel(
            scrollable_frame,
            text="1. Steady-State Cardio (Jogging/Cycling)",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise1_title.pack(pady=10)

        exercise1_img = Image.open("steady_state_cardio.jpeg")  
        exercise1_img = exercise1_img.resize((700, 600))
        exercise1_photo = ImageTk.PhotoImage(exercise1_img)

        exercise1_image_label = ctk.CTkLabel(scrollable_frame, image=exercise1_photo, text="")
        exercise1_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM STEADY-STATE CARDIO",
            """
        1. WARM-UP

        - Start with 5-10 minutes of light jogging or brisk walking.
        - Gradually prepare your muscles and joints for the main activity.



        2. MAIN ACTIVITY

        - Maintain a steady, moderate pace where you can hold a conversation.
        - If jogging, aim for a pace that feels sustainable for the entire duration.
        - If cycling, adjust the resistance to a moderate level.



        3. COOL-DOWN

        - Finish with 5-10 minutes of light jogging or walking to bring your heart rate down.



        4. TIPS

        - Keep your form upright and relaxed.
        - Breathe steadily and rhythmically.
        - Hydrate before, during, and after your session.
        """
        )

        exercise2_title = ctk.CTkLabel(
            scrollable_frame,
            text="2. Hip Circles",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise2_title.pack(pady=10)

        exercise2_img = Image.open("hip_curls.jpeg")  
        exercise2_img = exercise2_img.resize((700, 600))
        exercise2_photo = ImageTk.PhotoImage(exercise2_img)

        exercise2_image_label = ctk.CTkLabel(scrollable_frame, image=exercise2_photo, text="")
        exercise2_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM HIP CIRCLES",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart.
        - Place your hands on your hips.



        2. EXECUTING THE MOVEMENT

        - Rotate your hips in large circular motions.
        - Perform 10-15 circles in one direction, then switch to the other direction.



        3. TIPS

        - Keep your upper body still.
        - Gradually increase the size of your circles.
        - Maintain control and avoid jerky movements.
        """
        )

        exercise3_title = ctk.CTkLabel(
            scrollable_frame,
            text="3. Arm Circles",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise3_title.pack(pady=10)

        exercise3_img = Image.open("arm_circles.jpeg")  
        exercise3_img = exercise3_img.resize((700, 600))
        exercise3_photo = ImageTk.PhotoImage(exercise3_img)

        exercise3_image_label = ctk.CTkLabel(scrollable_frame, image=exercise3_photo, text="")
        exercise3_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM ARM CIRCLES",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart.
        - Extend your arms out to the sides, parallel to the ground.



        2. EXECUTING THE MOVEMENT

        - Make small circles with your arms, gradually increasing the size.
        - Perform 10-15 circles in one direction, then switch to the other direction.



        3. TIPS

        - Keep your back straight and core engaged.
        - Move your arms smoothly without straining your shoulders.
        - Focus on breathing steadily throughout.
        """
        )

        exercise4_title = ctk.CTkLabel(
            scrollable_frame,
            text="4. Thoracic Rotations",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise4_title.pack(pady=10)

        exercise4_img = Image.open("thoracic_rotations.jpeg")  
        exercise4_img = exercise4_img.resize((700, 600))
        exercise4_photo = ImageTk.PhotoImage(exercise4_img)

        exercise4_image_label = ctk.CTkLabel(scrollable_frame, image=exercise4_photo, text="")
        exercise4_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM THORACIC ROTATIONS",
            """
        1. SET UP

        - Start on your hands and knees, wrists under shoulders and knees under hips.
        - Place one hand behind your head.



        2. EXECUTING THE MOVEMENT

        - Rotate your upper body to bring your elbow towards the ceiling.
        - Return to starting position and repeat on the other side.



        3. TIPS

        - Engage your core and avoid arching your back.
        - Focus on rotating your thoracic spine slowly and with control.
        """
        )

        exercise5_title = ctk.CTkLabel(
            scrollable_frame,
            text="5. Ankle Circles",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise5_title.pack(pady=10)

        exercise5_img = Image.open("ankle_circles.jpeg")  
        exercise5_img = exercise5_img.resize((700, 600))
        exercise5_photo = ImageTk.PhotoImage(exercise5_img)

        exercise5_image_label = ctk.CTkLabel(scrollable_frame, image=exercise5_photo, text="")
        exercise5_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM ANKLE CIRCLES",
            """
        1. SET UP

        - Sit or stand with one leg lifted off the ground.



        2. EXECUTING THE MOVEMENT

        - Rotate your ankle in a circular motion.
        - Perform 10-15 circles in one direction, then switch to the other.



        3. TIPS

        - Keep your leg still and focus on the ankle movement.
        - Gradually increase the size of the circles for a better range of motion.
        """
        )

        exercise6_title = ctk.CTkLabel(
            scrollable_frame,
            text="6. Deep Squat Hold",
            font=("Arial", 22, "bold"),
            text_color="#00aaff"
        )
        exercise6_title.pack(pady=10)

        exercise6_img = Image.open("deep_squat_hold.jpeg")  
        exercise6_img = exercise6_img.resize((700, 600))
        exercise6_photo = ImageTk.PhotoImage(exercise6_img)

        exercise6_image_label = ctk.CTkLabel(scrollable_frame, image=exercise6_photo, text="")
        exercise6_image_label.pack(pady=10)

        create_section(
            scrollable_frame,
            "HOW TO PERFORM DEEP SQUAT HOLD",
            """
        1. SET UP

        - Stand with your feet shoulder-width apart.



        2. EXECUTING THE MOVEMENT

        - Lower your body into a deep squat position, with hips below your knees.
        - Hold the position for 1-2 minutes, keeping your heels on the ground.



        3. TIPS

        - Keep your back straight and chest lifted.
        - Use your arms for balance if needed.
        - Adjust your position or reduce the duration if uncomfortable.
        """
        )

        app.mainloop()
        pass
    days=[day1,day2,day3,day4,day5,day6,day7]
    for i, day in enumerate(days):
        button = ctk.CTkButton(app, text=f"Day{i+1}", font=("Arial", 14), width=200,command=day)
        button.pack(pady=10)

    pass

def flexibility_beginner():
    def day1():
        
        pass
    def day2():
        pass
    def day3():
        pass
    def day4():
        pass
    def day5():
        pass
    def day6():
        pass
    def day7():
        pass
    days=[day1,day2,day3,day4,day5,day6,day7]
    for i, day in enumerate(days):
        button = ctk.CTkButton(app, text=f"Day{i+1}", font=("Arial", 14), width=200,command=day)
        button.pack(pady=10)
    pass

def flexibility_advance():
    def day1():
        pass
    def day2():
        pass
    def day3():
        pass
    def day4():
        pass
    def day5():
        pass
    def day6():
        pass
    def day7():
        pass
    days=[day1,day2,day3,day4,day5,day6,day7]
    for i, day in enumerate(days):
        button = ctk.CTkButton(app, text=f"Day{i+1}", font=("Arial", 14), width=200,command=day)
        button.pack(pady=10)
    pass

def basic_exercises():

    app = ctk.CTkToplevel()
    app.title("Basic Exercises")
    app.geometry("900x900")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
    main_frame.pack(fill="both", expand=True)

    header = ctk.CTkLabel(
        main_frame,
        text="Basic Exercises 💪",
        font=("Arial", 28, "bold"),
        text_color="#ff9900"
    )
    header.pack(pady=10)

    scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
    scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

    def create_section_with_image(parent, title, content, image_path, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff", img_width=250, img_height=250):
        title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
        title_label.pack(anchor="w", padx=20, pady=(10, 5))

        content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
        content_label.pack(anchor="w", padx=20, pady=5)

        try:
            img = Image.open(image_path)
            img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)

            img_label = ctk.CTkLabel(parent, image=img)
            img_label.image = img  
            img_label.pack(pady=(10, 20))
        except Exception as e:
            print(f"Error loading image '{image_path}': {e}")

    create_section_with_image(
        scrollable_frame,
        "1. Bodyweight Squats",
        """
    Description: A fundamental lower body exercise that targets the quadriceps, hamstrings, and glutes.

    How to Do It:
    1. Stand with your feet shoulder-width apart.
    2. Lower your body by bending your knees and hips, as if sitting back into a chair.
    3. Keep your chest up and back straight.
    4. Go down until your thighs are parallel to the ground.
    5. Push through your heels to return to the starting position.

    Things to Take Care Of:
    - Keep your knees in line with your toes.
    - Avoid rounding your back.
    - Engage your core throughout the movement.
    """,
        "squats.jpg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "2. Push-Ups",
        """
    Description: A classic upper body exercise that works the chest, shoulders, triceps, and core.

    How to Do It:
    1. Start in a high plank position with hands slightly wider than shoulder-width apart.
    2. Lower your body until your chest nearly touches the floor.
    3. Keep your body in a straight line from head to heels.
    4. Push back up to the starting position.

    Things to Take Care Of:
    - Avoid flaring your elbows out too much.
    - Engage your core to maintain a straight body line.
    - Keep your neck neutral.
    """,
        "pushups.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "3. Plank",
        """
    Description: A core exercise that strengthens the abdominal muscles, back, and shoulders.

    How to Do It:
    1. Start in a forearm plank position with elbows directly under your shoulders.
    2. Keep your body in a straight line from head to heels.
    3. Hold the position for as long as you can while maintaining good form.

    Things to Take Care Of:
    - Avoid letting your hips sag or pike up.
    - Engage your core and glutes.
    - Keep your neck in line with your spine.
    """,
        "plank.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "4. Lunges",
        """
    Description: A lower body exercise that targets the quadriceps, hamstrings, and glutes.

    How to Do It:
    1. Stand with feet together.
    2. Step forward with one leg and lower your hips until both knees are bent at about 90 degrees.
    3. Push through your front heel to return to the starting position.
    4. Repeat on the other leg.

    Things to Take Care Of:
    - Keep your front knee over your ankle.
    - Avoid letting your back knee touch the ground.
    - Engage your core for balance.
    """,
        "lunges.jpg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "5. Bicep Curls",
        """
    Description: An upper body exercise that targets the biceps.

    How to Do It:
    1. Stand with feet shoulder-width apart, holding a dumbbell in each hand.
    2. Curl the dumbbells up towards your shoulders.
    3. Lower the dumbbells back to the starting position.

    Things to Take Care Of:
    - Keep your elbows close to your body.
    - Avoid swinging the weights.
    - Engage your core and maintain a steady pace.
    """,
        "bicep_curls.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "6. Tricep Dips",
        """
    Description: An upper body exercise that targets the triceps.

    How to Do It:
    1. Sit on the edge of a bench or chair with your hands next to your hips.
    2. Slide your hips off the bench and lower your body by bending your elbows.
    3. Push back up to the starting position.

    Things to Take Care Of:
    - Keep your elbows pointing straight back.
    - Avoid letting your shoulders hunch up.
    - Engage your core and keep your movements controlled.
    """,
        "tricep_dips.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "7. Glute Bridges",
        """
    Description: A lower body exercise that targets the glutes and hamstrings.

    How to Do It:
    1. Lie on your back with your knees bent and feet flat on the floor.
    2. Lift your hips towards the ceiling, squeezing your glutes at the top.
    3. Lower your hips back to the starting position.

    Things to Take Care Of:
    - Keep your feet flat on the floor.
    - Avoid arching your lower back.
    - Engage your core and glutes throughout the movement.
    """,
        "glute_bridges.jpeg",
        img_width=700, img_height=600
    )

    app.mainloop()

    pass
# Initialize the main window
app = ctk.CTk()
app.title("Fitness App")
app.geometry("500x600")

# Function to clear the current screen
def clear_frame():
    for widget in app.winfo_children():
        widget.destroy()

# Function to create the main page
def main_page():
    clear_frame()
    label = ctk.CTkLabel(app, text="Exercises", font=("Arial", 20, "bold"))
    label.pack(pady=20)

    exercises_button = ctk.CTkButton(app, text="Exercises", command=exercises_page, font=("Arial", 16))
    exercises_button.pack(pady=20)

# Function to create the exercises category page
def exercises_page():
    clear_frame()
    label = ctk.CTkLabel(app, text="Choose Exercise Category", font=("Arial", 18, "bold"))
    label.pack(pady=10)

    categories = [
        ("Weight Gain", weight_gain_page),
        ("Weight Loss", weight_loss_page),
        ("Flexibility", flexibility_page),
        ("Basic Exercises", basic_exercises_page),
    ]

    for text, command in categories:
        button = ctk.CTkButton(app, text=text, command=command, font=("Arial", 14), width=200)
        button.pack(pady=10)

# Function for Weight Gain page
def weight_gain_page():
    clear_frame()
    label = ctk.CTkLabel(app, text="Weight Gain", font=("Arial", 18, "bold"))
    label.pack(pady=10)

    beginner_button = ctk.CTkButton(app, text="Beginner", command=weight_gain_beginner, font=("Arial", 14))
    beginner_button.pack(pady=10)

    advanced_button = ctk.CTkButton(app, text="Advanced", command=weight_gain_advanced, font=("Arial", 14))
    advanced_button.pack(pady=10)

# Function for Weight Loss page
def weight_loss_page():
    clear_frame()
    label = ctk.CTkLabel(app, text="Weight Loss", font=("Arial", 18, "bold"))
    label.pack(pady=10)

    beginner_button = ctk.CTkButton(app, text="Beginner", command=weight_loss_beginner, font=("Arial", 14))
    beginner_button.pack(pady=10)

    advanced_button = ctk.CTkButton(app, text="Advanced", command=weight_loss_advanced, font=("Arial", 14))
    advanced_button.pack(pady=10)

# Function for Flexibility page
def flexibility_page():
    clear_frame()
    label = ctk.CTkLabel(app, text="Flexibility", font=("Arial", 18, "bold"))
    label.pack(pady=10)

    beginner_button = ctk.CTkButton(app, text="Beginner", command=flexibility_beginner, font=("Arial", 14))
    beginner_button.pack(pady=10)

    advanced_button = ctk.CTkButton(app, text="Advanced", command=flexibility_advance, font=("Arial", 14))
    advanced_button.pack(pady=10)

# Function for Basic Exercises page
def basic_exercises_page():
    clear_frame()
    main_frame = ctk.CTkFrame(app, fg_color="#1c1c1c", corner_radius=0)
    main_frame.pack(fill="both", expand=True)

    header = ctk.CTkLabel(
        main_frame,
        text="Basic Exercises 💪",
        font=("Arial", 28, "bold"),
        text_color="#ff9900"
    )
    header.pack(pady=10)

    scrollable_frame = ctk.CTkScrollableFrame(main_frame, width=800, height=600, fg_color="#292929", corner_radius=10)
    scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

    def create_section_with_image(parent, title, content, image_path, font=("Arial", 14), title_color="#ffaa00", text_color="#e0e0e0", subheading_color="#00aaff", img_width=250, img_height=250):
        title_label = ctk.CTkLabel(parent, text=title, font=("Arial", 18, "bold"), text_color=title_color)
        title_label.pack(anchor="w", padx=20, pady=(10, 5))

        content_label = ctk.CTkLabel(parent, text=content, font=font, text_color=text_color, wraplength=750, anchor="w", justify="left")
        content_label.pack(anchor="w", padx=20, pady=5)

        try:
            img = Image.open(image_path)
            img = img.resize((img_width, img_height), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)

            img_label = ctk.CTkLabel(parent, image=img)
            img_label.image = img  
            img_label.pack(pady=(10, 20))
        except Exception as e:
            print(f"Error loading image '{image_path}': {e}")

    create_section_with_image(
        scrollable_frame,
        "1. Bodyweight Squats",
        """
    Description: A fundamental lower body exercise that targets the quadriceps, hamstrings, and glutes.

    How to Do It:
    1. Stand with your feet shoulder-width apart.
    2. Lower your body by bending your knees and hips, as if sitting back into a chair.
    3. Keep your chest up and back straight.
    4. Go down until your thighs are parallel to the ground.
    5. Push through your heels to return to the starting position.

    Things to Take Care Of:
    - Keep your knees in line with your toes.
    - Avoid rounding your back.
    - Engage your core throughout the movement.
    """,
        "squats.jpg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "2. Push-Ups",
        """
    Description: A classic upper body exercise that works the chest, shoulders, triceps, and core.

    How to Do It:
    1. Start in a high plank position with hands slightly wider than shoulder-width apart.
    2. Lower your body until your chest nearly touches the floor.
    3. Keep your body in a straight line from head to heels.
    4. Push back up to the starting position.

    Things to Take Care Of:
    - Avoid flaring your elbows out too much.
    - Engage your core to maintain a straight body line.
    - Keep your neck neutral.
    """,
        "pushups.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "3. Plank",
        """
    Description: A core exercise that strengthens the abdominal muscles, back, and shoulders.

    How to Do It:
    1. Start in a forearm plank position with elbows directly under your shoulders.
    2. Keep your body in a straight line from head to heels.
    3. Hold the position for as long as you can while maintaining good form.

    Things to Take Care Of:
    - Avoid letting your hips sag or pike up.
    - Engage your core and glutes.
    - Keep your neck in line with your spine.
    """,
        "plank.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "4. Lunges",
        """
    Description: A lower body exercise that targets the quadriceps, hamstrings, and glutes.

    How to Do It:
    1. Stand with feet together.
    2. Step forward with one leg and lower your hips until both knees are bent at about 90 degrees.
    3. Push through your front heel to return to the starting position.
    4. Repeat on the other leg.

    Things to Take Care Of:
    - Keep your front knee over your ankle.
    - Avoid letting your back knee touch the ground.
    - Engage your core for balance.
    """,
        "lunges.jpg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "5. Bicep Curls",
        """
    Description: An upper body exercise that targets the biceps.

    How to Do It:
    1. Stand with feet shoulder-width apart, holding a dumbbell in each hand.
    2. Curl the dumbbells up towards your shoulders.
    3. Lower the dumbbells back to the starting position.

    Things to Take Care Of:
    - Keep your elbows close to your body.
    - Avoid swinging the weights.
    - Engage your core and maintain a steady pace.
    """,
        "bicep_curls.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "6. Tricep Dips",
        """
    Description: An upper body exercise that targets the triceps.

    How to Do It:
    1. Sit on the edge of a bench or chair with your hands next to your hips.
    2. Slide your hips off the bench and lower your body by bending your elbows.
    3. Push back up to the starting position.

    Things to Take Care Of:
    - Keep your elbows pointing straight back.
    - Avoid letting your shoulders hunch up.
    - Engage your core and keep your movements controlled.
    """,
        "tricep_dips.jpeg",
        img_width=700, img_height=600
    )

    create_section_with_image(
        scrollable_frame,
        "7. Glute Bridges",
        """
    Description: A lower body exercise that targets the glutes and hamstrings.

    How to Do It:
    1. Lie on your back with your knees bent and feet flat on the floor.
    2. Lift your hips towards the ceiling, squeezing your glutes at the top.
    3. Lower your hips back to the starting position.

    Things to Take Care Of:
    - Keep your feet flat on the floor.
    - Avoid arching your lower back.
    - Engage your core and glutes throughout the movement.
    """,
        "glute_bridges.jpeg",
        img_width=700, img_height=600
    )
    

# Function to create the 7-day week page
def week_page(title):
    clear_frame()
    label = ctk.CTkLabel(app, text=title, font=("Arial", 18, "bold"))
    label.pack(pady=10)

    for day in range(1, 8):
        button = ctk.CTkButton(app, text=f"Day {day}", font=("Arial", 14), width=200)
        button.pack(pady=10)

# Start the app with the main page
main_page()

app.mainloop()
