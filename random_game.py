import random 
def game_on(): 
	random_num = random.randint(1, 2) 
	input_num = int(input("Вам было загадано число от 1 до 2, попробуйте угадать его>>>")) 
	

	if random_num == input_num: 
		print("Вы восхитительны!") 
		answer = input("Хоите повторить? (y/n)>>>") 
		if answer == "y": 
		random_game() 
	elif answer == 'n': 
		print("Благодарим за игру!") 
	else: 
		random_game() 
	else: 
		print("Вы не угадали, думаю вам в следующий раз повезет") 
		random_game() 

def random_game(): answer = input("Я ваш крупье не желаете сыграть в одну рандомную игру? (y/n)>>> ") 
	if answer == "y": game_on() elif answer == 'n': 
		print("До свидания") 
	else: 
	random_game() 
random_game()
