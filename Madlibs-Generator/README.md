# 📝 Mad Libs Generator in Python

This is a simple **Mad Libs Generator** written in Python.
It reads a story template from a file (`story.txt`), finds all placeholders like `<adjective>` or `<animal>`, asks the user to fill them in, and then generates a fun story.

---



## 📂 Project Structure

madlibs/

│── story.txt        # The story template with placeholders

│── madlibs.py       # The Python code that runs the generator

│── README.md        # Project documentation

---



## 📖 How It Works

1. The program opens `story.txt` and scans for placeholders (anything inside `< >`, like `<animal>`).
2. It keeps a dictionary of explanations for each placeholder, so the user knows what kind of word to enter.
3. For each unique placeholder in the story:
   - The program asks the user for input (e.g., "Please give me a describing word").
   - The input is stored and reused everywhere the placeholder appears in the story.
4. Finally, it replaces all placeholders with the user’s answers and prints the completed story.

---



## 🚀 How to Run

1. Open the project in VS Code (or any IDE).
2. Make sure you have Python installed (Python 3.6+ recommended).
3. Open a terminal in VS Code (`Ctrl + ~`).
4. Run the program:

   ```bash
   python madlibs.py
   ```

---



## 🛠  Features

* Automatically detects placeholders in the story.
* Only asks once for each unique placeholder (even if it appears multiple times).
* Gives helpful explanations for each word type.
* Easy to add new placeholders and explanations.

---



## 📌 Customizing

* To change the story, just edit `story.txt`.
* To add new placeholder types, update the `placeholders` dictionary in `madlibs.py`.
