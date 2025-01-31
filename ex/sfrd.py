import customtkinter as ctk

# List of 55 motivational quotes (replace with your quotes)
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