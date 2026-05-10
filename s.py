from tkinter import *
from tkinter import ttk
from random import randint

# Main window
root = Tk()
root.geometry("600x500")
root.title("Rock Paper Scissors")
root.config(bg="#1e1e2f")

# Game options
choices = ["Rock", "Paper", "Scissors"]
icons = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

player_score = 0
computer_score = 0

# Title
title_label = Label(
    root,
    text="Rock Paper Scissors Game",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=20)

# Computer choice label
computer_label = Label(
    root,
    text="Computer Choice: ?",
    font=("Arial", 18),
    bg="#1e1e2f",
    fg="cyan"
)
computer_label.pack(pady=20)

# User selection dropdown
user_select = ttk.Combobox(
    root,
    values=choices,
    font=("Arial", 14),
    state="readonly"
)
user_select.current(0)
user_select.pack(pady=20)

# Result label
result_label = Label(
    root,
    text="Choose your move!",
    font=("Arial", 16, "bold"),
    bg="#1e1e2f",
    fg="yellow"
)
result_label.pack(pady=20)

# Score label
score_label = Label(
    root,
    text="Player: 0   Computer: 0",
    font=("Arial", 16),
    bg="#1e1e2f",
    fg="white"
)
score_label.pack(pady=20)


def play():
    global player_score, computer_score

    user_choice = user_select.get()
    computer_choice = choices[randint(0, 2)]

    computer_label.config(
        text=f"Computer Choice: {icons[computer_choice]} {computer_choice}"
    )

    # Game logic
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Player: {player_score}   Computer: {computer_score}"
    )


# Play button
play_button = Button(
    root,
    text="PLAY",
    font=("Arial", 16, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=play
)
play_button.pack(pady=20)

# Exit button
exit_button = Button(
    root,
    text="EXIT",
    font=("Arial", 14),
    bg="red",
    fg="white",
    width=10,
    command=root.destroy
)
exit_button.pack(pady=10)

root.mainloop()