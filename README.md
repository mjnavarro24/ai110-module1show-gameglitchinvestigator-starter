# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose:
The purpose of the game is to guess the randomly selected secret number within a range depending on the difficulty. THe goal is to guess the number within the certain amount of attempts. The lower the number of attempts it takes to guess the secret, the higher the score. 

- [X] Detail which bugs you found:
I found that the hints given were incorrect, most of the time I wasn't able to start a new game, the # of attempts left was not correct, it didn't make sense for the normal mode to have a larger range than hard mode, the # of attempts for the difficulties were not correct, the text said "Guess a number between 1 and 100" for every difficutly, I was able to make guesses out of the range and it would count as an attempt.

- [X] Explain what fixes you applied:
I fixed how it determined what hint to give so that the correct hint is shown.
I fixed being able to start a new game by setting the status to "playing".
I set the number of attempts left to be set after a guess is processed. This fixes the attempt number updating correctly. 
I fixed the mapping of the ranges so that normal is 1-50 and hard is 1-100. 
I fixed the mapping of the attempts so that Easy is 5, Normal is 6, and Hard is 8. 
I updated the static string "Guess a number between 1 and 100" to take in the low and high values.
I implemented a check for out of range guesses and only incremented the attempts when a valid guess was given. 



## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User sets difficulty to normal.
2. User enters guess of 30.
3. Game hint says to "Go lower".
4. User enters guess of 15. 
5. Game hint says to "Go higher".
6. User enters guess of 23. 
7. Game hint says to "Go higher".
8. User enters guess of 29. 
9. Guess is correct and game ends. 
10. Score updates correctly. 
11. User attempts to submit a guess.
12. Game says to "Start a new game to play again". 
13. User selects New Game.
14. Game restarts and attempts left is reset to 6. 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

```
python3 -m pytest
=========================================================================== test session starts ============================================================================
platform darwin -- Python 3.13.0, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/melaynanavarro/codepath/GameGlitchInvestigator/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 14 items                                                                                                                                                         

tests/test_game_logic.py ..............                                                                                                                              [100%]

==================== 14 passed in 0.01s ================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
