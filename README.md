# Typing Speed and Error Calculation

This program measures your typing speed and calculates the number of errors made while typing a given text. It prompts you to enter the text and then provides the results. You can take multiple tests by running the program multiple times.

## Prerequisites
- Python 3.x

## Instructions

1. Import the required modules: `time` and `random`.
2. Define two functions:
   - `mistake(paratest, usertest)`: Calculates the number of errors between the `paratest` (provided text) and `usertest` (user's input).
   - `speed_time(time_s, time_e, userinput)`: Measures the typing speed in words per second based on the time taken to type and the length of the input.
3. Run an infinite loop:
   - Prompt the user to indicate if they are ready to take the test.
   - If the user enters "yes", select a random text from the available options and display it.
   - Measure the time taken to type the input.
   - Calculate and display the typing speed and the number of errors made.
   - If the user enters "no", end the program.
   - If the user enters any other input, display an error message.
   
## Usage

1. Run the program.
2. When prompted, enter "yes" to start the test or "no" to exit.
3. If you choose to start the test, a random text will be displayed.
4. Type the text accurately and press Enter.
5. The program will display your typing speed in words per second and the number of errors made.
6. You can choose to take more tests or exit by entering "yes" or "no" when prompted.

## Example
```
Ready to take the test (Yes/No): yes
***** Typing speed *****
Hey there this is an era of dancing

Enter: Hey there this is an era of dancing
Speed:  5  words/sec
Error:  0

Ready to take the test (Yes/No): yes
***** Typing speed *****
Hey there i am a programmer and can solve your every day programming related problems

Enter: Hey there i am a programmer and can solve your every day programming related problems
Speed:  6  words/sec
Error:  0

Ready to take the test (Yes/No): no
Thank you
```

Feel free to modify the program to suit your needs and preferences. Happy typing!
