# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The game wasn't actually playable. I could makes guesses but the hints were not accurate, leading me to continue to make incorrect guesses. Sometimes I was unable to restart the game. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  After tapping submit guess after out of guesses and starting a new game I am unable to submit a guess.

  Should receive an error when inputting 0 but got a hint instead.

  100 tells me to guess higher when 100 is the highest. I expected the answer to be correct or for the hint to tell me to go lower.

  Incorrect hints: Telling me to go higher even though my guess was higher than the secret.

  .When restarting the game you hve 8 attempts, the # of attempts is inconsistent with the first time. The # of attempts should be the same. 

  It says you have 1 attempt left but that you're out of guesses. 

  When you submit a guess for the first time the attempts left number doesn’t decrease. 

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

  I used ClaudeCode for this project. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  I asked ClaudeCode what was causing the hint to say higher when I inputted 100 as a guess on Normal mode. It correctly pointed me to the comparison logic that was flipped, but also that there was another bug where on even number attempts the secret was being converted to a string resulting in the secret and the guess to be compared as strings instead. I fixed those two things and the hints afterwards were accurate. 

  I asked ClaudeCode what it thought of checking for out of range guesses in check_guess and it told me that it was better suited to do the fix in parse_guess becuase of the function purpose of validation . It also surfaced a bug related to out of range guesses where the # of attempts was decreased before validation of the guess. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  After I made a few changes, ClaudeCode was telling me there was a bug that would cause the attempt # to be incorrect because it was incremented beforehand. I didn't see where this was happening in the code and was confused so I aksed it to explain further and walk me through it. I found that it was referring to a stale version of the code before I made changes to the line it was referring to. Claude didn't automatically recognize my code changes and had to be told when changes are made. 

  When refactoring and copying over code, ClaudeCode failed to also copy over the comments I added. When I told it to fix the tests so that they pass, instead of fixing the asssert to check for a tuple, it just fixed the assignment from check_guess so that the test passed but didnt modify the assert to a tuple to check message as well. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I tried to reproduce the bug, and if I couldn't reproduce it anymore I knew it was fixed. I also validated that the logic was correct with unit tests. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I ran a test on the function parse_guess with 1.5 as the input. I learned that a decimal input is considered valid and passses because it rounds the number down. 

- Did AI help you design or understand any tests? How?
  After I asked the agent to create tests for the ones I could come up with, I asked it for suggestions on what else should be tested. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit re-runs the script from top to bottom on every click. Python variables get reset but the session state survives reruns. Through the session state is how we're able to keep track of things like attempts and score even when the script is being rerun. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  - This could be a testing habit, a prompting strategy, or a way you used Git.
  
 I liked how the project instructions told us to do give it a multi-command. It showed me that the agent can handle it given clarity, I want to practice using multi-commands instead of giving it commands one at a time. 

- What is one thing you would do differently next time you work with AI on a coding task?

I would open new chats for each new task to avoid context switching in one chat. With this I could avoid re-giving context of what I want it to focus on and instead open up my previous chat.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI generated code is pretty accurate given that it understands the context and what you want it to do. Even with higher models or more context, I still need to be specific and can't assume that the agent can always infer what I want. 