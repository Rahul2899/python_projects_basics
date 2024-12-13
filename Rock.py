import random

def game():
    options = ['Rock', 'Paper', 'Scissors']
    user_score = system_score = 0

    for _ in range(3):
        user = input("\nEnter your choice (Rock, Paper, Scissors): ").capitalize()
        if user not in options:
            print("Invalid choice! Try again.")
            continue
        
        system = random.choice(options)
        print(f"You: {user} | Computer: {system}")

        if user == system:
            print("It's a tie!")
        elif (user == "Rock" and system == "Scissors") or (user == "Paper" and system == "Rock") or (user == "Scissors" and system == "Paper"):
            user_score += 1
            print("You win this round!")
        else:
            system_score += 1
            print("Computer wins this round!")
        
        print(f"Score: You {user_score} - {system_score} Computer")

    print("\n=== Game Over ===")
    print(f"Final Score: You {user_score} - {system_score} Computer")
    print("🎉 You win!" if user_score > system_score else "😢 Computer wins!" if system_score > user_score else "🤝 It's a tie!")

game()
