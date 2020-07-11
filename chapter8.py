prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	word = letter + suffix
	f_letter = word[0]
	if f_letter == 'O' or f_letter == 'Q':
		word = letter + 'u' + suffix
		print (word)
	else:
		print(word)

def find(word, letter, start):
	index = start
	while index < len(word):
		if word[index] == letter:
			print(index)
			return
		index = index + 1
	print(-1)
	return

find('start', 't', 2)

def count(word, letter, start):
	amount = 0
	index = start
	while index < len(word):
		if word[index] == letter:
			amount = amount + 1
		index = index + 1
	print(amount)
	return

count('kkakekkakwkkek', 'k', 0)



