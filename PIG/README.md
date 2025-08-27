# 🎲 Dice Game (Pig Style) in Python

This is a simple **multiplayer dice game** written in Python.
Each player takes turns rolling a die. The goal is to reach **15 points** first. But be careful—if you roll a `1`, your score resets to `0` for that round!

---

## 📂 Project Structure

dice-game/
│── dice_game.py # The Python code for the game
│── README.md # Project documentation

---

## 📖 How the Game Works

1. The program asks how many players will play (**2–4 players allowed**).
2. Each player starts with `0` points.
3. On their turn, a player may **roll the dice**:
   - If they roll a number between `2–6`, that value is added to their total score.
   - If they roll a `1`, their score is reset to `0` for that turn, and their turn ends immediately.
4. A player can **choose to stop rolling** at any time and keep their current score.
5. The first player to reach **15 points** wins the game!

---

## 🚀 How to Run

1. Make sure Python is installed (Python 3.6+ recommended).
2. Save the game script as `dice_game.py`.
3. Run the script in your terminal:
   ```bash
   python dice_game.py
   ```

---

## 🛠 Features

* Supports  **2–4 players** .
* Random dice rolls from `1–6`.
* Rolling a **1** resets your score for that turn.
* Automatically declares the winner.

---

## 📌 Customizing

* Change `max_score = 15` to increase or decrease the winning score.
* You can expand the game with extra rules (e.g., multiple dice, bonus points, penalties).
