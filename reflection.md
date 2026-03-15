# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. The hints were backwards. Whenever I clicked on the 'Submit Guess' button while guessing a number that is higher than the secret number, a message popped up saying "Go HIGHER!". Whenever I guess a number that is lower than the secret number, a message popped up saying "Go LOWER!".

2. Guessing a number out of the number range is valid. For example: In normal difficulty, if I guess a number out of the normal difficulty range [1 to 100], let's say -1 or 101, the game does not show any error message stating that the input number is out of range. 

3. The "New Game" button does not work when you're out of attempts left. I expect the attempts amount to reset, as well as the History dictionary and Score to also reset.

4. The "New Game" button does not work when you have guessed the secret number correctly. I expect the attempts amount to reset, as well as the score and history.

5. There's no duplicate guess detection. If I guess the same number twice, I'd expect a message saying "you already guessed this number".

6. The difficulty ranges for 'Easy' and 'Hard' mode do not function properly. In easy mode, the secret number's range should be from 1 to 20, however the game can pick numbers greater than 20. In hard mode, the secret number's range should be from 1 to 50, but the game can pick numbers greater than 50.

7. Attempts left missrepresentation. The attempts left on the blue rounded rectangle show one number less than the amount of attempts that we should have in each difficulty. In easy mode, we expect 6 attempts, but get 5. In normal mode we expect 8 attempts, but get 7. In hard mode, we expect 5 attempts, but get 4.

8. Guess a number between range in the blue rounded rectangle missrepresentation. In easy, normal and hard mode, it says "Guess a number between 1 and 100." under the Make a guess header when it should list different ranges per difficulty.

9. Normal and Hard mode mixed up. Normal difficulty seems to be more difficult than Hard mode, where in normal difficulty you have an 8% chance to get the number, while in hard mode you get a 10% chance. 

10. The history of guessed numbers dictionary is delayed. Each time I input a number and click "Submit Guess", I expect the History dictionary to add that number, however it adds the first guessed number when you guess an additional number, then the second number whenever you guess a third and so on...

11. Changing the game difficulty does not immediately start a new game. I would expect whenever I switch up the difficulty to start a new game, however only the difficulty seems to change in the developer debug info and nothing else.

11b. Adding to the previous bug, if you for example make 6 attempted guesses in normal difficulty (where you currently have 7 attempts) and switch to Easy mode, the Attempts left counter on the blue rounded rectangle goes into negative integers.

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
