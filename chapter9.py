# 9.1
fin = open('words.txt')

def count(word):
	if len(word) > 20:
		print(word)

'''for word in fin:
	count(word)'''

# 9.2
def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True

'''for word in fin:
	if has_no_e(word) == True:
		print(word)'''

# 9.3 (not able to interpret via Sublime Text 3)
def avoids(word, nono):
	for letter in word:
		if letter == nono:
			return False
	return True

nonono = input('What shall I avoid?')

count = 0

for word in fin:
	if avoids(word, nonono) == True:
		count += 1

print(count)



