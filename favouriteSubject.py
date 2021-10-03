#!/bin/python3

favouriteSubject = 'unknown' 

while True:
  favouriteSubject = input('What is your favourite subject? ')
  if (favouriteSubject.lower() == 'computing'):
    print('Well done. You got the answer right. ' + 
    'Computing is the best subject.')
    break
  print('Sorry ' + favouriteSubject + 
  ' is not the right answer. Please try again.')