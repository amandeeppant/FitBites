import tkinter as tk
from tkinter import messagebox

class FlexibilityRoutineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Flexibility Routine")
        self.root.geometry("500x600")
        self.root.config(bg="#2e2e2e")  # Dark background color
        self.create_widgets()

    def create_widgets(self):
        header_label = tk.Label(self.root, text="Advanced Flexibility Routine", font=("Helvetica", 18, "bold"), fg="#3CB3E5", bg="#2e2e2e")
        header_label.pack(pady=10)

        day_frame = tk.Frame(self.root, bg="#2e2e2e")
        day_frame.pack(pady=20)

        # Buttons with yellow color and dark background
        day1_button = tk.Button(day_frame, text="Day 1: Lower Body Flexibility", width=30, height=2, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), command=self.day1)
        day1_button.grid(row=0, column=0, padx=10, pady=10)

        day2_button = tk.Button(day_frame, text="Day 2: Upper Body Flexibility", width=30, height=2, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), command=self.day2)
        day2_button.grid(row=1, column=0, padx=10, pady=10)

        day3_button = tk.Button(day_frame, text="Day 3: Full Body Mobility", width=30, height=2, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), command=self.day3)
        day3_button.grid(row=2, column=0, padx=10, pady=10)

        day4_button = tk.Button(day_frame, text="Day 4: Active Recovery", width=30, height=2, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), command=self.day4)
        day4_button.grid(row=3, column=0, padx=10, pady=10)

        day5_button = tk.Button(day_frame, text="Day 5: Lower Body Focus", width=30, height=2, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), command=self.day5)
        day5_button.grid(row=4, column=0, padx=10, pady=10)

        day6_button = tk.Button(day_frame, text="Day 6: Upper Body and Core", width=30, height=2, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), command=self.day6)
        day6_button.grid(row=5, column=0, padx=10, pady=10)

        day7_button = tk.Button(day_frame, text="Day 7: Full Body Recovery Stretch", width=30, height=2, bg="#FFD700", fg="black", font=("Helvetica", 12, "bold"), command=self.day7)
        day7_button.grid(row=6, column=0, padx=10, pady=10)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def day1(self):
        message = """
Day 1: Lower Body Flexibility

Warm-Up (5 minutes):
- Light cardio: Treadmill walking or stationary cycling.
- Dynamic Stretches:
    - Leg swings (front-to-back, 10 per leg).
    - Side-to-side leg swings (10 per leg).

Routine:
- Hamstring Stretch with Bench: Hold for 20-30 seconds per leg.
- Seated Hamstring Stretch (Machine): Hold for 20 seconds per leg.
- Hip Flexor Stretch: Hold for 20 seconds per side.
- Calf Stretch on Step: Hold for 20-30 seconds.
- Foam Rolling (Optional): Roll hamstrings and calves for 1-2 minutes.
        """
        self.show_message("Day 1: Lower Body Flexibility", message)

    def day2(self):
        message = """
Day 2: Upper Body Flexibility

Warm-Up (5 minutes):
- Arm circles (small to large, 10 each direction).
- Shoulder rolls (forward and backward, 10 each).

Routine:
- Chest Stretch on Wall: Hold for 20 seconds per arm.
- Overhead Triceps Stretch: Hold for 20 seconds per arm.
- Cross-Body Shoulder Stretch: Hold for 20 seconds per arm.
- Lat Stretch on Pull-Up Bar: Hold for 15-20 seconds.
- Neck Stretch: Hold for 15 seconds per side.
        """
        self.show_message("Day 2: Upper Body Flexibility", message)

    def day3(self):
        message = """
Day 3: Full Body Mobility and Stretching

Warm-Up (5 minutes):
- Dynamic stretches:
    - Walking lunges with a twist (10 reps per side).
    - High knees (1 minute).

Routine:
- Hamstring Stretch with Resistance Band: Hold for 20 seconds per leg.
- Standing Side Stretch: Hold for 20 seconds per side.
- Spinal Twist (Seated Machine or Mat): Hold for 20 seconds per side.
- Quadriceps Stretch: Hold for 20 seconds per leg.
- Foam Rolling: Roll back and glutes for 2 minutes.
        """
        self.show_message("Day 3: Full Body Mobility", message)

    def day4(self):
        message = """
Day 4: Active Recovery

Focus on light flexibility work:
- Treadmill Walking (5–10 minutes).
- Light stretches (choose any from the earlier days).
- Optional: Foam rolling for relaxation (1–2 minutes per major muscle group).
        """
        self.show_message("Day 4: Active Recovery", message)

    def day5(self):
        message = """
Day 5: Lower Body Focus

Warm-Up (5 minutes):
- Dynamic leg swings and high knees.

Routine:
- Inner Thigh Stretch (Seated Machine or Mat): Hold for 20-30 seconds.
- Glute Stretch: Hold for 20 seconds per leg.
- Hip Circles: Do 10 circles each direction.
- Standing Calf Stretch: Hold for 20 seconds per leg.
        """
        self.show_message("Day 5: Lower Body Focus", message)

    def day6(self):
        message = """
Day 6: Upper Body and Core

Warm-Up (5 minutes):
- Light arm swings and spinal twists.

Routine:
- Chest Opener on Bench: Hold for 20 seconds.
- Lat Stretch on Cable Machine: Hold for 20 seconds per arm.
- Oblique Side Stretch: Hold for 15 seconds per side.
- Foam Rolling: Focus on the lats and upper back for 1–2 minutes.
        """
        self.show_message("Day 6: Upper Body and Core", message)

    def day7(self):
        message = """
Day 7: Full Body Recovery Stretch

Warm-Up (5 minutes):
- Treadmill walking or cycling.

Routine:
- Dynamic Arm and Leg Swings: Swing arms and legs to loosen joints (10 reps each).
- Seated Forward Stretch: Hold for 20–30 seconds.
- Standing Forward Fold: Hold for 20 seconds.
- Light Foam Rolling: Cover all major muscle groups for 2–3 minutes.
        """
        self.show_message("Day 7: Full Body Recovery Stretch", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlexibilityRoutineApp(root)
    root.mainloop()
