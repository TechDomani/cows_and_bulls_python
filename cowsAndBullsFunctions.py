import random

def generate_random_number():
    number = []
    for _ in range(4):
       digit = random.randint(0, 9)
       while (digit in number):
           digit = random.randint(0, 9)
       number.append(digit)
    return number

def validate_input(currentInput):
    currentInput = currentInput.strip()
    if (currentInput.lower() == 'exit'):
        return True, []
    if (not currentInput.isdigit()) or (len(currentInput) != 4):
        return validate_input(input('You did not enter a four digit number. Please try again or type exit to leave the game: '))
    userNumber = []
    for num in currentInput:
        if (int(num) in userNumber):            
           return validate_input(input('You entered a number with the duplicate digit ' + num + '. Please try again or type exit to leave the game: '))
        else:
            userNumber.append(int(num))
    return False, userNumber

def check_guess(currentGuess, requiredNumber):
    bulls = 0
    cows = 0
    for guessIndex, guessDigit in enumerate(currentGuess):
        for requiredIndex, requiredDigit in enumerate(requiredNumber):
            if (guessDigit == requiredDigit):
                if (guessIndex == requiredIndex):
                    bulls += 1
                else:
                    cows += 1
                break
    return cows, bulls

def cows_and_bulls(requiredNumber):
    success = False
    guesses = 0
    while (not success):
        [exit, userInput] = validate_input(input('Please enter a four digit number or type exit to quit the game: '))
        if (exit):
            print('The number required is ' + ''.join(map(str, requiredNumber)))
            break       
        [cows, bulls] = check_guess(userInput, requiredNumber) 
        guesses += 1
        success = bulls == 4
        if (not success):
            print(f'You have {str(cows)} cows and {str(bulls)} bulls')    
    if (success):
        print(f"Well done. You have guessed the number correctly in {str(guesses)} attempt{'s' if guesses > 1 else ''}")