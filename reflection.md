# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game wasn't actually playable. I could makes guesses but the hints were not accurate, leading me to continue to make incorrect guesses. Sometimes I was unable to restart the game. 

- After tapping submit guess after out of guesses and starting a new game I am unable to submit a guess 

- Should receive an error when inputting 0 but got a hint instead

- 100 tells me to guess higher when 100 is the highest. I expected the answer to be correct or for the hint to tell me to go lower

- Incorrect hints: Telling me to go higher even though my guess was higher than the secret

- When restarting the game you hve 8 attempts, the # of attempts is inconsistent with the first time. The # of attempts should be the same. 

- It says you have 1 attempt left but that you're out of guesses. 

- When you submit a guess for the first time the attempts left number doesn’t decrease. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                   | Expected Behavior       | Actual Behavior               | Console Output / Error |
|-------------------------|-------------------------|-------------------------------|------------------------|
|  100                    | Correct or go lower.    | Go higher                     | None
|  0                      | Invalid input.          | Go lower                      | None
| Submit guess first time | Attempts decreases by 1 |  # of attempts stays the same | None 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
