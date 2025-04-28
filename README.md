# Follow-Fame

🎮 Higher Lower Game

A simple command-line game where you guess which celebrity has more Instagram followers. Keep guessing correctly to increase your score—one wrong guess and it's game over!

🧠 How It Works

- Two random celebrities are shown.
- You guess which one has more followers.
- Correct guesses increase your score.
- A wrong guess ends the game.
- Your final score is compared with a saved high score in `score.txt`.

🚀 Getting Started

1. Clone the repository or download the code files:
2. Make sure you have the following files/modules:
- `main.py` *(the file containing the code above)*
- `gamedata.py` *(a file containing the `game_data` list with celebrity dictionaries)*
- `logos.py` *(a file containing ASCII art for `higherlower` and `vs`)*

Example `gamedata.py`:
```python
game_data = [
    {"name": "Cristiano Ronaldo", "follower_count": 500, "description": "footballer", "country": "Portugal"},
    {"name": "Ariana Grande", "follower_count": 350, "description": "singer", "country": "USA"},
    ...
]
```

Example `logos.py`:
```python
higherlower = """
 _     _ _       _               
| |   (_) |     | |              
| |__  _| |_ ___| |__   ___ _ __ 
| '_ \| | __/ __| '_ \ / _ \ '__|
| | | | | || (__| | | |  __/ |   
|_| |_|_|\__\___|_| |_|\___|_|  
"""

vs = """
 _    __    
| |  / /    
| | / /     
| |/ /      
|___/       
"""
```

---

💾 File Requirements

- `score.txt`: A text file that stores the high score. It must be present in the same directory. If it doesn’t exist, create one with a single number (e.g., `0`).

▶️ How to Run

Run the game using Python:
```bash
python main.py
```

📦 Dependencies

This game uses only Python’s built-in libraries:
- `random`

No external packages required.

 🏆 Features

- Interactive gameplay via terminal
- Real-time scoring and feedback
- High score tracking saved to file
- ASCII art for added visual appeal

 📌 Notes

- Make sure the celebrities in `game_data` have unique names and valid `follower_count` values.
- This game is best run in a terminal or command prompt with UTF-8 support for proper display of ASCII art.

🛠️ License

This project is open-source. Feel free to use and modify it for learning or fun!
