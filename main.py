import random
import logos  as  art
import gamedata as data
print(art.higherlower)
print("Welcome to the Higher Lower Game! \n")
print("You have to guess which celebrity has more followers.\n")
print("If you guess wrong, you lose.\n")
print("If you guess right, you win.\n")

User_name = input("Enter your name: ")
print("")
print(f"Hello {User_name}, let's start the game!\n")
score = 0
game_continue = True
while game_continue:
    # Randomly select two celebrities from the game data
    celebrity_a = random.choice(data.game_data)
    celebrity_b = random.choice(data.game_data)
    # Ensure that the two celebrities are not the same
    while celebrity_a == celebrity_b:
        celebrity_b = random.choice(data.game_data)
    # Display the options to the user
    print(f"Compare A: {celebrity_a['name']}, a {celebrity_a['description']}, from {celebrity_a['country']}")
    print(art.vs)
    print(f"Against B: {celebrity_b['name']}, a {celebrity_b['description']}, from {celebrity_b['country']} \n")
    # Get user's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("")
    # Check if the guess is correct and update score accordingly
    if (guess == "A" and celebrity_a["follower_count"] > celebrity_b["follower_count"]) or \
       (guess == "B" and celebrity_b["follower_count"] > celebrity_a["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}. \n")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}\n")
        print("Game Over! \n")
    
filee = open("score.txt", "r+")
highscore_text = filee.read().strip()  # Remove leading/trailing spaces or newlines

if highscore_text.isdigit():
    highscore = int(highscore_text)
else:
    highscore = 0  # Default if file is empty or invalid

if score > highscore:
    filee.seek(0)
    filee.write(str(score))
    filee.truncate()  # Clear anything after the new score
    filee.write("x\n")
    x = (f"Congratulations! {User_name} you have set a new high score of {score}!\n")
    print(x)
else:
    print(f" {User_name} Your score is not enough to beat the high score of {highscore}.\n")

filee.close()
