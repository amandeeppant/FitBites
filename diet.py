from tkinter import *
import customtkinter

# Constants for calorie recommendations
CALORIE_GOALS = {
    "breakfast": 389,
    "lunch": 454,
    "snacks": 130,
    "dinner": 324,
}

# Initialize global calorie variables
calories = 0
remaining_calories = sum(CALORIE_GOALS.values())

# Theme and Appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  # Set theme to blue

# Color Palette for Blue-Black Theme
COLOR_BACKGROUND = "#0D1117"  # Dark background
COLOR_PRIMARY = "#161B22"  # Slightly lighter black
COLOR_HIGHLIGHT = "#1F6AA5"  # Blue for accents
COLOR_TEXT = "white"  # White text
COLOR_HOVER = "#144a7c"  # Hover effect blue

# Initialize the main window
root = customtkinter.CTk()
root.title("Caloriegram")
root.geometry("1100x600")


# Function to dynamically update calories
def update_calories(consumed):
    global calories, remaining_calories
    calories += consumed
    remaining_calories = max(0, sum(CALORIE_GOALS.values()) - calories)
    calorie_label.configure(
        text=f"Eaten: {calories} Cal\nRemaining: {remaining_calories} Cal"
    )


# Function to create the meal addition window
def open_meal_window():
    new_window = customtkinter.CTkToplevel(root)
    new_window.title("Add Meal")
    new_window.geometry("800x500")
    new_window.resizable(False, False)

    # Frame for the form
    form_frame = customtkinter.CTkFrame(new_window, fg_color=COLOR_PRIMARY, corner_radius=10)
    form_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

    # Food Name Entry
    food_name_label = customtkinter.CTkLabel(form_frame, text="Food Name:", font=("Lucida Sans", 14), text_color=COLOR_TEXT)
    food_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    food_name_entry = customtkinter.CTkEntry(form_frame, placeholder_text="Enter food name", fg_color=COLOR_BACKGROUND, text_color=COLOR_TEXT)
    food_name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Food Category Dropdown
    food_category_label = customtkinter.CTkLabel(form_frame, text="Food Category:", font=("Lucida Sans", 14), text_color=COLOR_TEXT)
    food_category_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    categories = [
        "Fruits and Juices", "Snacks", "Baby Foods", "Spices and Herbs",
        "Fats and Oils", "Poultry Products", "Beverages", "Meat Products",
        "Cereals", "Fast Food", "Sweets", "Baked Goods",
    ]
    food_category_combo = customtkinter.CTkComboBox(form_frame, values=categories, fg_color=COLOR_BACKGROUND, text_color=COLOR_TEXT)
    food_category_combo.grid(row=1, column=1, padx=10, pady=10)

    # Serving Size and Unit
    serving_label = customtkinter.CTkLabel(form_frame, text="Serving Size:", font=("Lucida Sans", 14), text_color=COLOR_TEXT)
    serving_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    serving_frame = customtkinter.CTkFrame(form_frame, fg_color=COLOR_PRIMARY)
    serving_frame.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    serving_entry = customtkinter.CTkEntry(serving_frame, width=120, placeholder_text="Amount", fg_color=COLOR_BACKGROUND, text_color=COLOR_TEXT)
    serving_entry.pack(side=LEFT, padx=5)
    unit_options = ["g", "kg", "ml", "cup", "ounce"]
    unit_menu = customtkinter.CTkOptionMenu(serving_frame, values=unit_options, fg_color=COLOR_BACKGROUND, text_color=COLOR_TEXT)
    unit_menu.pack(side=LEFT, padx=5)

    # Nutrient Information
    # nutrient_frame = customtkinter.CTkFrame(form_frame, fg_color=COLOR_PRIMARY)
    # nutrient_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
    # nutrients = {"Calories": "calories", "Carbs (g)": "carbs", "Protein (g)": "protein", "Fat (g)": "fat"}
    # nutrient_entries = {}
    # for idx, (label, key) in enumerate(nutrients.items()):
    #     nutrient_label = customtkinter.CTkLabel(nutrient_frame, text=f"{label}:", font=("Lucida Sans", 14), text_color=COLOR_TEXT)
    #     nutrient_label.grid(row=idx, column=0, padx=10, pady=5, sticky=W)
    #     nutrient_entry = customtkinter.CTkEntry(nutrient_frame, placeholder_text=f"Enter {label.lower()}", fg_color=COLOR_BACKGROUND, text_color=COLOR_TEXT)
    #     nutrient_entry.grid(row=idx, column=1, padx=10, pady=5)
    #     nutrient_entries[key] = nutrient_entry

    # Save Button
    def save_meal():
        try:
            consumed_calories = int(nutrient_entries["calories"].get())
            update_calories(consumed_calories)
            new_window.destroy()
        except ValueError:
            print("Please enter valid numeric values for calories.")

    save_button = customtkinter.CTkButton(
        form_frame, text="Save", command=save_meal, fg_color=COLOR_HIGHLIGHT, hover_color=COLOR_HOVER
    )
    save_button.grid(row=4, column=1, pady=20, sticky=E)


# Main Calorie Display
calorie_frame = customtkinter.CTkFrame(root, fg_color=COLOR_PRIMARY, corner_radius=10)
calorie_frame.pack(pady=20, padx=20, fill=X)
calorie_label = customtkinter.CTkLabel(
    calorie_frame,
    text=f"Eaten: {calories} Cal\nRemaining: {remaining_calories} Cal",
    font=("Lucida Sans", 20),
    text_color=COLOR_TEXT,
)
calorie_label.pack(pady=10)

# Meal Sections (Breakfast, Lunch, Snacks, Dinner)
meal_frame = customtkinter.CTkFrame(root, fg_color=COLOR_BACKGROUND, corner_radius=10)
meal_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

meals = ["Breakfast", "Lunch", "Snacks", "Dinner"]
for meal in meals:
    meal_section = customtkinter.CTkFrame(meal_frame, fg_color=COLOR_PRIMARY, corner_radius=10)
    meal_section.pack(pady=10, padx=10, fill=X)
    meal_label = customtkinter.CTkLabel(meal_section, text=f"   {meal}", font=("Lucida Sans", 18), text_color=COLOR_TEXT)
    meal_label.pack(side=LEFT, padx=20)
    meal_button = customtkinter.CTkButton(
        meal_section, text="Add +", command=open_meal_window, fg_color=COLOR_HIGHLIGHT, hover_color=COLOR_HOVER
    )
    meal_button.pack(side=RIGHT, padx=20)

# Run the application
root.mainloop()

