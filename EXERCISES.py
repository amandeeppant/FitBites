# EXERCISES  DAY1
import customtkinter as ctk
from PIL import Image, ImageTk
import os

os.chdir('bakchodi')
# Initialize the app
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





# EXERCISES  DAY 2


import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
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





# Day 3: Rest or Active Recovery

import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
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




# DAY 4


import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
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




#DAY 5


import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
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




# DAY6


import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
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



#DAY 7

import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
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
