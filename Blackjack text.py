import random
shoe = []
p_hand = []
d_hand = []
score = [0,0]
card = None
game = True
with open('shoe.txt','w+') as file:
	for suits in ['hearts','diamonds','clubs','spades']:
		for vaule in range(13):
			if vaule < 10:
				file.write('{}_{}\n'.format(str(vaule),suits))
			elif vaule == 10:
				file.write('{}_{}\n'.format('J',suits))
			elif vaule == 11:
				file.write('{}_{}\n'.format('Q',suits))
			else:
				file.write('{}_{}\n'.format('J',suits))
with open('shoe.txt','r') as d:
	for line in d:
		shoe.append(line.strip('\n'))
		
random.shuffle(shoe)

def draw_card(hand):
	global card
	card = shoe[0]
	shoe.pop(0)
	hand.append(card)
	return card

def find_score(p):
	if card[0] == 'K':
		score[p] += 10
	elif card[0] == 'Q':
		score[p] += 10
	elif card[0] == 'J':
		score[p] += 10
	elif card[0] == '1':
		score[p] += 10
	elif card[0] == 'A':
		if score[p] <= 10:
			score[p] += 11
		else:
			score[p] += 1
	else:
		score[p] += int(card[0])

def check(p):
	global game_over
	if score[p] > 21:
		print('Busted')
		game_over = True
	elif score[p] == 21:
		print('Blackjack')
		game_over = True
		
while game:
	game_over = False
	for draw in range(2):
		draw_card(p_hand)
		find_score(0)
		draw_card(d_hand)
		find_score(1)
	print(p_hand)
	check(0)
	while game_over == False:
		h_s = input('stand or hit: ')
		if h_s == 'hit':
			draw_card(p_hand)
			find_score(0)
			print(p_hand)
			check(0)
		elif h_s == 'stand':
			game_over = True
		else:
			print('pleas type hit or stand')
	while score[1] != 21 and score[1] < 17:
		draw_card(d_hand)
		find_score(1)
	print('dealer')
	print(d_hand)
	if score[0] > score[1] or score[1] > 21 and score[0] <= 21:
		print('you win')
	elif score[0] == score[1] and score[0] <= 21:
		print('push')
	else:
		print('you lose')
	play = input('do you want play again')
	if play == 'yes':
		p_hand.clear()
		d_hand.clear()
		score = [0,0]
	elif play == 'no':
		game = False
	else:
		print('pls type yes or no')
