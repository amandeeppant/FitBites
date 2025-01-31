import customtkinter as ctk
from tkinter import messagebox

# Set up the app appearance
ctk.set_appearance_mode("dark")  # Use Dark Mode
ctk.set_default_color_theme("blue")  # Use Blue Color Theme

# Initialize the main window
root = ctk.CTk()
root.title("7-Day Yoga and Meditation Plan")
root.geometry("800x800")
root.configure(bg="#2e2e2e")

# Dictionary to store routines
routines = {
    1: """
Day 1: Grounding and Stress Relief
Focus: Reducing stress, grounding the mind, and cultivating presence.

- Child's Pose (Balasana) – Hold for 2–3 minutes
- Mountain Pose (Tadasana) – Hold for 1 minute
- Standing Forward Fold (Uttanasana) – Hold for 1–2 minutes
- Cat-Cow Pose (Marjaryasana-Bitilasana) – Hold for 1–2 minutes
- Seated Forward Fold (Paschimottanasana) – Hold for 2 minutes
- Legs Up the Wall (Viparita Karani) – Hold for 5 minutes
    """,
    2: """
Day 2: Emotional Release and Relaxation
Focus: Releasing pent-up emotions and cultivating relaxation.

- Cat-Cow Pose (Marjaryasana-Bitilasana) – 2 minutes
- Low Lunge (Anjaneyasana) – Hold for 1 minute per side
- Seated Bound Angle Pose (Baddha Konasana) – Hold for 2 minutes
- Pigeon Pose (Eka Pada Rajakapotasana) – Hold for 2 minutes per side
- Supine Twist (Supta Matsyendrasana) – Hold for 2 minutes per side
- Savasana (Corpse Pose) – 5–10 minutes
    """,
    # Add other routines for Day 3 to Day 7 here...
    7: """
Day 7: Releasing Tension and Relaxing the Mind
Focus: Full-body relaxation and releasing residual tension.

- Child's Pose (Balasana) – Hold for 2 minutes
- Seated Forward Fold (Paschimottanasana) – Hold for 2 minutes
- Pigeon Pose (Eka Pada Rajakapotasana) – Hold for 1–2 minutes per side
- Cat-Cow Pose (Marjaryasana-Bitilasana) – 1–2 minutes
- Legs Up the Wall (Viparita Karani) – Hold for 5 minutes
- Savasana (Corpse Pose) – 10 minutes
    """,
}

# Function to display routine for a selected day
def display_routine(day):
    routine_label.configure(text=routines[day])

# Header
header_label = ctk.CTkLabel(
    root,
    text="7-Day Yoga and Meditation Plan",
    font=("Helvetica", 24, "bold"),
    text_color="#3CB3E5"
)
header_label.pack(pady=20)

# Frame for Day Selection
days_frame = ctk.CTkFrame(root, fg_color="#444", corner_radius=10)
days_frame.pack(padx=20, pady=20, fill="x")

# Days Buttons
days = [
    "Day 1: Grounding & Stress Relief",
    "Day 2: Emotional Release & Relaxation",
    "Day 3: Focus & Clarity",
    "Day 4: Self-Awareness & Introspection",
    "Day 5: Anxiety Relief & Relaxation",
    "Day 6: Positivity & Gratitude",
    "Day 7: Releasing Tension & Relaxation",
]
for index, day in enumerate(days):
    button = ctk.CTkButton(
        days_frame,
        text=day,
        font=("Helvetica", 14),
        fg_color="#3CB3E5",
        hover_color="#47A9D6",
        command=lambda i=index: display_routine(i + 1),
    )
    button.pack(pady=5, padx=20, fill="x")

# Frame for Routine Display
routine_frame = ctk.CTkFrame(root, fg_color="#444", corner_radius=10)
routine_frame.pack(padx=20, pady=20, fill="both", expand=True)

routine_label = ctk.CTkLabel(
    routine_frame,
    text="Select a day to view the routine",
    font=("Helvetica", 16),
    text_color="#EEE",
    justify="left",
)
routine_label.pack(padx=20, pady=20)

# Run the App
root.mainloop()
