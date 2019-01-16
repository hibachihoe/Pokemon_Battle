import time
import random
print()
print('-' * 60)
print('A Wild Jigglypuff appears!')
time.sleep(0.4)
print('You only have one Pokémon.')
time.sleep(0.4)
print()
print('I choose you, Snorlax!')
time.sleep(0.4)
print()
time.sleep(0.4)

#Starting HPs
snorlax_hp = 200
jiggly_hp = 125

print('Orignial HP')
print('- Snorlax HP: ' + str(snorlax_hp))
time.sleep(0.3)
print('-Jigglypuff HP: ' + str(jiggly_hp))
time.sleep(0.3)
print()
time.sleep(0.3)

while snorlax_hp > 0 and jiggly_hp > 0:
	print('Battle options:')
	time.sleep(0.3)
	print('- [1] Amnesia')
	time.sleep(0.3)
	print('- [2] Tackle')
	time.sleep(0.3)
	print('- [3] Lick')
	time.sleep(0.3)
	print('- [4] Crunch')
	time.sleep(0.3)
	print('- [5] Capture')
	time.sleep(0.3)
	print('- [6] Run')
	time.sleep(0.3)
	your_move = input('Chose a move using the corresponding number: ')
	print()

	if your_move == '1':
		snorlax_hp = snorlax_hp + 50
		print('Snorlax uses Amnesia, his HP increases to ' + str(snorlax_hp))
		time.sleep(0.3)
	elif your_move == '2':
		jiggly_hp = jiggly_hp - 10
		print('Snorlax uses Tackle and deals 10 damage to Jigglypuff')
		time.sleep(0.3)
	elif your_move == '3':
		jiggly_hp = jiggly_hp - 30
		print('Snorlax uses Lick and deals 30 damage to Jigglypuff')
		time.sleep(0.3)
	elif your_move == '4':
		jiggly_hp = jiggly_hp - 40
		print ('Snorlax uses Crunch and deals 40 damage to Jigglypuff')
		time.sleep(0.3)
	elif your_move == '5':
		capture_roll = random.randint(0,125)
		if capture_roll > jiggly_hp:
			print('You have caught Jigglypuff')
			break
		else:
			print('You tried to capture Jigglypuff, but it escaped')
	elif your_move =='6':
		run_away = random.randint(0,200)
		if run_away < snorlax_hp:
			print('You have ran from the battle')
			break
		else:
			print('You tried to run from the battle but failed')
	print()

	#Jigglypuff attacks
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)

	if enemy_move == '1':
		snorlax_hp = snorlax_hp - 30
		jiggly_hp = jiggly_hp + 30
		print('Jigglypuff uses Sing and deals 30 damage while recovering 30 HP')
		time.sleep(0.3)
	elif enemy_move == '2':
		snorlax_hp = snorlax_hp - 50
		print('Jigglypuff uses Body Slam and deals 50 damage')
		time.sleep(0.3)
	print()

	# check for overkill
	if snorlax_hp < 0:
		snorlax_hp = 0 
	if jiggly_hp < 0:
		jiggly_hp = 0
	print('Updated HP')
	print('- Snorlax HP: ' + str(snorlax_hp))
	time.sleep(0.3)
	print('-Jigglypuff HP: ' + str(jiggly_hp))
	time.sleep(0.3)
	print()
	time.sleep(0.3)
 


if snorlax_hp == 0:
	print('Snorlax has lost the battle the winner is Jigglypuff')
elif jiggly_hp == 0:
	print('Jigglypuff has lost the battle the winner is Snorlax')



