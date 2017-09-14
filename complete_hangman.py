import re
import random

def getrandomword():
	with open('scrabble_words.txt', 'r') as f:
		lines = f.read().splitlines()
	random_word = lines[random.randint(0,len(lines))]
	return random_word.lower()

def return_word(input_list):
	result = ""
	for x in input_list:
		result += x
	return result
	

def hangman_logic(word,difficulty):
	current_word = ["*" for n in range(len(word))]
	print (return_word(current_word))
	guessed_letters = ""
	counter = 0
	while True:
		user_guess = raw_input("What is your guess?: \n")
		if len(user_guess) != 1:
			print ("please input a single letter")
		elif user_guess in guessed_letters:
			print ("Wait, you've already guessed that.")
		else:
			guessed_letters += user_guess
			if user_guess not in word:
				counter += 1
				if counter == difficulty:
					print("Sorry you lose, the word was %s" %word)
					return False
				print ("Sorry, thats not in there, and you have %s guesses left." % (difficulty - counter))
			else:
				print ("Yes, the word contains a/an %s!" %user_guess)
				letter_indices = [m.start() for m in re.finditer(user_guess, word)]
				for x in letter_indices:
					current_word[x] = user_guess
		if "*" not in return_word(current_word):
			print ("You got it!, the word is", word)
			return True
		print ("the word so far is: ",return_word(current_word))
		#print "letters not in the word: ",guessed_letters
	print ("the word is: ",return_word(current_word))	
	print ("You took %s guesses." %counter)

def play_hangman():
	won = 0
	lost = 0
	difficulty_condition = False
	while True:
		wtp = raw_input("Would you like to play a new game of hangman?")
		if not difficulty_condition:
			user_difficulty = raw_input("Do you want easy, medium, or hard diffculty?")
			difficulty_condition = True
		if user_difficulty == "easy":
			guesses = 10
		elif user_difficulty == "medium":
			guesses = 8
		else:
			guesses = 6
		if wtp == "yes" or wtp == "y":
			if hangman_logic(getrandomword(),guesses):
				won += 1
			else:
				lost += 1
		else:
			print("thanks for playing, you won %s games and lost %d games." % (won,lost))
			break
		print ("you've won:", won, "and lost", lost)
	
play_hangman()

