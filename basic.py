import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
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
