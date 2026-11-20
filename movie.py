
import tkinter as tk
from tkinter import ttk, messagebox
import random

# ==========================================
# CINEMATCH - MOVIE RECOMMENDATION SYSTEM
# ==========================================

# Movie database: 7 movies per genre per language

movie_data = {

    "Hindi": {
        "Comedy": [
            "3 Idiots", "Chhichhore", "Hera Pheri",
            "Phir Hera Pheri", "Munna Bhai M.B.B.S.",
            "Welcome", "Bajrangi Bhaijaan"
        ],
        "Romance": [
            "Yeh Jawaani Hai Deewani", "Jab We Met",
            "Veer-Zaara", "Kal Ho Naa Ho",
            "Aashiqui 2", "Rockstar", "Barfi!"
        ],
        "Horror": [
            "Bhool Bhulaiyaa", "Raaz", "1920",
            "Stree", "Tumbbad", "Pari", "Bhoot"
        ],
        "Action": [
            "War", "Pathaan", "Jawan",
            "Dhoom 2", "Singham", "Tiger Zinda Hai",
            "Bang Bang"
        ],
        "Thriller": [
            "Drishyam", "Andhadhun", "Kahaani",
            "Talaash", "Badla", "A Wednesday",
            "Special 26"
        ]
    },

    "English": {
        "Comedy": [
            "Home Alone", "The Hangover", "Jumanji",
            "Mean Girls", "Mr. Bean's Holiday",
            "The Mask", "Johnny English"
        ],
        "Romance": [
            "Titanic", "The Notebook", "La La Land",
            "The Fault in Our Stars", "Me Before You",
            "Pride and Prejudice", "Five Feet Apart"
        ],
        "Horror": [
            "The Conjuring", "Insidious", "Annabelle",
            "The Nun", "IT", "Sinister", "Hereditary"
        ],
        "Action": [
            "Avengers: Endgame", "Iron Man",
            "Mission Impossible", "John Wick",
            "The Dark Knight", "Gladiator",
            "Mad Max: Fury Road"
        ],
        "Thriller": [
            "Inception", "Shutter Island", "Gone Girl",
            "Prisoners", "Se7en", "The Prestige",
            "Fight Club"
        ]
    },

    "Korean": {
        "Comedy": [
            "Extreme Job", "Midnight Runners",
            "Secret Zoo", "Twenty", "Luck-Key",
            "Miss Granny", "My Sassy Girl"
        ],
        "Romance": [
            "20th Century Girl", "Tune in for Love",
            "The Classic", "On Your Wedding Day",
            "Always", "A Moment to Remember",
            "Be With You"
        ],
        "Horror": [
            "Train to Busan", "The Wailing",
            "Gonjiam: Haunted Asylum",
            "The Call", "The Medium",
            "A Tale of Two Sisters", "Death Bell"
        ],
        "Action": [
            "The Man from Nowhere", "The Villainess",
            "The Roundup", "Veteran", "The Suspect",
            "Confidential Assignment", "Deliver Us from Evil"
        ],
        "Thriller": [
            "Forgotten", "Memories of Murder",
            "The Chaser", "I Saw the Devil",
            "Oldboy", "No Mercy", "The Gangster, the Cop, the Devil"
        ]
    },

    "Tamil": {
        "Comedy": [
            "Boss Engira Bhaskaran", "Soodhu Kavvum",
            "Nanban", "Kalakalappu",
            "Panchathanthiram", "Doctor", "Don"
        ],
        "Romance": [
            "96", "Vinnaithaandi Varuvaayaa",
            "Raja Rani", "Alaipayuthey",
            "Mouna Ragam", "OK Kanmani", "Thiruchitrambalam"
        ],
        "Horror": [
            "Maya", "Pizza", "Demonte Colony",
            "Aranmanai", "Eeram", "Aval", "Pisasu"
        ],
        "Action": [
            "Vikram", "Leo", "Master",
            "Kaithi", "Thuppakki", "Jailer",
            "Enthiran"
        ],
        "Thriller": [
            "Ratsasan", "Vikram Vedha",
            "Dhuruvangal Pathinaaru", "Maharaja",
            "Por Thozhil", "Imaikkaa Nodigal",
            "Thegidi"
        ]
    },

    "Telugu": {
        "Comedy": [
            "Jathi Ratnalu", "F2", "DJ Tillu",
            "Venky", "Ready", "Pelli Choopulu",
            "Ala Vaikunthapurramuloo"
        ],
        "Romance": [
            "Geetha Govindam", "Sita Ramam",
            "Fidaa", "Arjun Reddy",
            "Tholi Prema", "Hi Nanna", "Ye Maaya Chesave"
        ],
        "Horror": [
            "Arundhati", "Masooda", "Virupaksha",
            "Raju Gari Gadhi", "Prema Katha Chitram",
            "Bhaagamathie", "Kanchana"
        ],
        "Action": [
            "Baahubali", "RRR", "Pushpa",
            "Salaar", "Magadheera", "Eega",
            "Akhanda"
        ],
        "Thriller": [
            "Evaru", "Goodachari", "HIT",
            "Kshanam", "Anukokunda Oka Roju",
            "Agent Sai Srinivasa Athreya", "1: Nenokkadine"
        ]
    }
}


# ==========================================
# MOOD DATABASE
# ==========================================

mood_options = [
    "Any Mood",
    "Happy",
    "Sad",
    "Romantic",
    "Excited",
    "Scared",
    "Relaxed",
    "Motivated",
    "Curious"
]

# Suggested moods for each genre

genre_moods = {
    "Comedy": ["Happy", "Relaxed"],
    "Romance": ["Romantic", "Sad"],
    "Horror": ["Scared", "Excited"],
    "Action": ["Excited", "Motivated"],
    "Thriller": ["Curious", "Excited"]
}


# ==========================================
# CREATE MOVIE DATABASE
# ==========================================

movies = []

for language, genres in movie_data.items():

    for genre, movie_names in genres.items():

        for name in movie_names:

            movies.append({
                "name": name,
                "genre": genre,
                "language": language,
                "mood": random.choice(genre_moods[genre]),
                "rating": round(random.uniform(7.0, 9.0), 1)
            })


# ==========================================
# MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("CineMatch - Movie Recommendation System")
root.geometry("950x750")
root.configure(bg="#141421")


# ==========================================
# HEADING
# ==========================================

heading = tk.Label(
    root,
    text="🎬 CINEMATCH",
    font=("Arial", 32, "bold"),
    bg="#141421",
    fg="#ff477e"
)

heading.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Discover Movies That Match Your Mood!",
    font=("Arial", 14),
    bg="#141421",
    fg="white"
)

subtitle.pack(pady=5)


# ==========================================
# SELECTION FRAME
# ==========================================

selection_frame = tk.Frame(
    root,
    bg="#25253b",
    padx=20,
    pady=20
)

selection_frame.pack(pady=20)


# Genre

tk.Label(
    selection_frame,
    text="🎭 Genre",
    bg="#25253b",
    fg="white",
    font=("Arial", 12, "bold")
).grid(row=0, column=0, padx=15, pady=10)

genre_box = ttk.Combobox(
    selection_frame,
    values=list(movie_data["Hindi"].keys()),
    state="readonly",
    width=17
)

genre_box.grid(row=1, column=0, padx=15)
genre_box.set("Comedy")


# Language

tk.Label(
    selection_frame,
    text="🌍 Language",
    bg="#25253b",
    fg="white",
    font=("Arial", 12, "bold")
).grid(row=0, column=1, padx=15, pady=10)

language_box = ttk.Combobox(
    selection_frame,
    values=list(movie_data.keys()),
    state="readonly",
    width=17
)

language_box.grid(row=1, column=1, padx=15)
language_box.set("Hindi")


# Mood

tk.Label(
    selection_frame,
    text="💖 Mood",
    bg="#25253b",
    fg="white",
    font=("Arial", 12, "bold")
).grid(row=0, column=2, padx=15, pady=10)

mood_box = ttk.Combobox(
    selection_frame,
    values=mood_options,
    state="readonly",
    width=17
)

mood_box.grid(row=1, column=2, padx=15)
mood_box.set("Any Mood")


# ==========================================
# RESULTS FRAME
# ==========================================

result_frame = tk.Frame(
    root,
    bg="#141421"
)

result_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)


# Scrollable Results

canvas = tk.Canvas(
    result_frame,
    bg="#141421",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    result_frame,
    orient="vertical",
    command=canvas.yview
)

scrollable_frame = tk.Frame(
    canvas,
    bg="#141421"
)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas_window = canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.bind(
    "<Configure>",
    lambda e: canvas.itemconfig(
        canvas_window,
        width=e.width
    )
)


# ==========================================
# RECOMMENDATION FUNCTION
# ==========================================

def recommend_movies():

    genre = genre_box.get()
    language = language_box.get()
    mood = mood_box.get()

    # Clear previous results

    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    # Filter movies by genre and language

    recommendations = [
        movie for movie in movies
        if movie["genre"] == genre
        and movie["language"] == language
    ]

    # Sort according to mood

    if mood != "Any Mood":

        recommendations.sort(
            key=lambda movie: movie["mood"] == mood,
            reverse=True
        )

    if not recommendations:

        tk.Label(
            scrollable_frame,
            text="No movies found!",
            bg="#141421",
            fg="white",
            font=("Arial", 16)
        ).pack(pady=30)

        return

    # Heading

    tk.Label(
        scrollable_frame,
        text="✨ YOUR MOVIE RECOMMENDATIONS",
        font=("Arial", 18, "bold"),
        bg="#141421",
        fg="#ff477e"
    ).pack(pady=15)

    # Display movies

    for index, movie in enumerate(recommendations, 1):

        card = tk.Frame(
            scrollable_frame,
            bg="#25253b",
            padx=20,
            pady=12
        )

        card.pack(
            fill="x",
            padx=15,
            pady=7
        )

        details = (
            f"🎬 {index}. {movie['name']}\n"
            f"⭐ Rating: {movie['rating']}/10\n"
            f"🎭 Genre: {movie['genre']}\n"
            f"🌍 Language: {movie['language']}\n"
            f"💖 Mood: {movie['mood']}"
        )

        tk.Label(
            card,
            text=details,
            bg="#25253b",
            fg="white",
            font=("Arial", 12),
            justify="left",
            anchor="w"
        ).pack(anchor="w")

    canvas.yview_moveto(0)


# ==========================================
# SURPRISE ME FUNCTION
# ==========================================

def surprise_movie():

    selected_genre = genre_box.get()
    selected_language = language_box.get()

    available_movies = [
        movie for movie in movies
        if movie["genre"] == selected_genre
        and movie["language"] == selected_language
    ]

    if available_movies:

        movie = random.choice(available_movies)

        messagebox.showinfo(
            "🎲 Surprise Movie",
            f"Your movie is:\n\n"
            f"🎬 {movie['name']}\n\n"
            f"⭐ Rating: {movie['rating']}/10\n"
            f"🌍 Language: {movie['language']}\n"
            f"🎭 Genre: {movie['genre']}"
        )


# ==========================================
# SEARCH FUNCTION
# ==========================================

def search_movie():

    search_window = tk.Toplevel(root)

    search_window.title("Search Movies")
    search_window.geometry("400x250")
    search_window.configure(bg="#25253b")

    tk.Label(
        search_window,
        text="🔍 Search Movie",
        font=("Arial", 20, "bold"),
        bg="#25253b",
        fg="#ff477e"
    ).pack(pady=20)

    search_entry = tk.Entry(
        search_window,
        font=("Arial", 13),
        width=30
    )

    search_entry.pack(pady=10)

    def find_movie():

        query = search_entry.get().strip().lower()

        results = [
            movie for movie in movies
            if query in movie["name"].lower()
        ]

        if results:

            result_text = "\n\n".join(
                f"{m['name']} | {m['language']} | "
                f"{m['genre']} | ⭐ {m['rating']}"
                for m in results
            )

            messagebox.showinfo(
                "Search Results",
                result_text
            )

        else:

            messagebox.showinfo(
                "Search Results",
                "No movie found!"
            )

    tk.Button(
        search_window,
        text="Search",
        command=find_movie,
        bg="#ff477e",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=15)


# ==========================================
# BUTTONS
# ==========================================

button_frame = tk.Frame(
    root,
    bg="#141421"
)

button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="✨ Recommend Movies",
    command=recommend_movies,
    bg="#ff477e",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=10
).grid(row=0, column=0, padx=8)


tk.Button(
    button_frame,
    text="🎲 Surprise Me",
    command=surprise_movie,
    bg="#6941c6",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=10
).grid(row=0, column=1, padx=8)


tk.Button(
    button_frame,
    text="🔍 Search Movie",
    command=search_movie,
    bg="#247ba0",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=10
).grid(row=0, column=2, padx=8)


# ==========================================
# FOOTER
# ==========================================

footer = tk.Label(
    root,
    text="Made with Python | CINEMATCH 2026",
    bg="#141421",
    fg="gray",
    font=("Arial", 10)
)

footer.pack(side="bottom", pady=10)


# ==========================================
# RUN APPLICATION
# ==========================================

root.mainloop()