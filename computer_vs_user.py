print('********************   ROCK   ********************'.center(600))
print('********************   PAPER   ********************'.center(600))
print('********************   SCISSORS   ********************'.center(600)+'\n\n')
# importing random package
import random
name=input('Enter Your Name : ')
print('\n\n')
user_score=0
computer_score=0
winning_score=3
while True:
	
	while user_score<winning_score and computer_score<winning_score:
		print(f'{name}\'s Score :{user_score}   Computers Score: {computer_score} \n\n')
		user=input(name + ' Enter your choice : ')
		user=user.lower()
		print('\n')

		if user=='quit' or user=='q':
			break
		computer=random.randint(0,2)

		if user=='rock' or user=='paper' or user =='scissor':
			#assigning the random  value for computer
			if computer == 0:
				computer='rock'
			elif computer ==1:
				computer='paper'
			else:
				computer='scissor'
			print('Computer\'s Choice : '+computer)
				
			if user == computer:
				print('oops its a tie\n\n')
			elif user == 'rock':
				if computer == 'paper':
					print('computer wins the game\n\n')
					computer_score+=1
				elif computer == 'scissor':
					print(f'{name} wins the game \n\n')
					user_score+=1
				else :
					print('computer enter valid value \n\n')
			elif user =='paper':
				if computer == 'rock':
					print(f'{name} wins the game \n\n')
					user_score+=1
				elif computer == 'scissor':
					print('computer wins the game \n\n')
					computer_score+=1
				else :
					print('computer enter valid value \n\n')
			elif user == 'scissor':
				if computer == 'rock':
					print(f'{name} wins the game \n\n')
					user_score+=1
				elif computer == 'paper':
					print(f'{name} wins the game \n\n')
					user_score+=1
				else :
					print('computer enter valid value \n\n')
			else:
				print('something went wrong \n\n')
		else:
			print(f'{name} enter a valid value \n\n')
	print('\n\n\nGame Over!!\n\n')
	
	if user_score>computer_score:
		print(f'Final Scores :  {name}\'s Score :{user_score}   Computers Score: {computer_score} \n\n')
		print(f'Congatualations {name} You won the game \n\n')
		note=input('wanna play again [y/n] : ')
		if note == 'y':
			user_score=0
			computer_score=0
			winning_score=3
		else:
			break
			
	elif user_score == computer_score:
		print('Oops its a tie')
		note=input('wanna play again [y/n] : ')
		if note == 'y':
			user_score=0
			computer_score=0
			winning_score=3
		else:
			break
	else:
		print('oops Computer won the game')
		note=input('wanna play again [y/n] : ')
		if note == 'y':
			user_score=0
			computer_score=0
			winning_score=3
		else:
			break