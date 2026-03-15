# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game looked like a browser application with an okay UI, built on Streamlit. 

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

12. (This one was found by Claude code) Scoring rewards wrong guesses. On even attempts, a "Too High" wrong guess gives you +5 points instead of penalizing you.

13. You can enter an empty string as a guess. Whenever the user inputs an empty string as a guess the game should reject the input and respond with "Enter a guess."

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I utilized Claude code as my AI teammate! It aided me tremendously sorting through the lines of app.py that needed the #FIXME comments. 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

An example of an AI suggestion that was correct was whenever I asked it to find any additional bugs I might've missed. Bug #12 says 'Scoring rewards wrong guesses. On even attempts, a "Too High" wrong guess gives you +5 points instead of penalizing you.' -- This is indeed correct, and I tested it multiple times by running the app on Streamlit and verifying the score each even attempt time I submitted a wrong answer to confirm.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

An example of an AI suggestion that was incorrect, although my fault, was when I asked it to correct a #FIXME in the app.py file. I did not give it a precise instruction when I asked it to correct the logic of identifying duplicate guesses. Claude's fix was to stop the Streamlit rendering pipeline whenever the user inputs a duplicate number, which caused the Developer Debug panel and footer to disappear from the screen. I verified this was wrong by playing the game and noticing that the bottom half of the page was missing after submitting a duplicate guess. I then reprompted Claude with a more specific description of the bug. I explained that the debug panel and footer were disappearing, and it correctly fixed it by removing st.stop() and restructuring the logic with an if/else block instead.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was really fixed by playing the game multiple times, checking off each bug after testing them. Additionally, I made sure to ask Claude to help me by creating pytests for each bug, ensuring we covered every single base. 

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

One manual test I ran was submitting a duplicate number. I discovered that Claude's initial fix (which was caused by a vague prompt) called st.stop(), which caused the Developer Debug panel and footer to disappear entirely. Catching this visually showed me that a fix can bring new bugs if not tested end-to-end.

Another manual test was switching difficulty mid-game; I watched the Developer Debug panel closely and confirmed the secret, attempts, score, and history all reset correctly when the difficulty changed.

- Did AI help you design or understand any tests? How?

To be transparent, Claude wrote every pytest case in test_game_logic.py. I'm not yet familiar with pytest's structure, so I asked Claude to generate the tests while explaining each one so I could follow along. I made sure to ask it directly to generate tests targetting specific bugs, like guessing a number outside of the range and what the expected outcome should look like. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain it to a friend by telling them to imagine a web app where every single time they interacted with a button, the whole website refreshed, except it's python code running over again from the top. Session state is like a sticky note the app keeps on the side so it doesn't forget things like your score or guess history each time it restarts.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

One habit I learned from this project that I want to reuse in future labs is definitely the pytests. This makes it to where I do not have to keep running and closing the application as it is way quicker, which is something I struggled with when creating a vibecoded app for my previous internship. Although I got the job done by continuously testing, I spent an extrordinarily large amount of time doing so. Additionally, I learned how to use git to document my project. I want to continue doing it to expand my professional portfolio!

Something I would do differently the next time I work with AI on a coding tast is to be more specific when prompting it. I sometimes give vague instructions which lead to Claude guessing what I want, which sometimes is good, but most of the time it's bad.

This project made me realize that AI generated code can be a building block towards creating production-ready applications. I am very interested in continuing to work with AI generated programs and refining them to work as intended!