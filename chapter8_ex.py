"""exercise1 = 'Read documentation at: http://docs.python.org/3/library/stdtypes.html#string-methods'

word = 'banana'
print(word.count('a'))

word1 = 'house' 
word2 =	'esuoh'

if word1 == word2[::-1]:
	print(True)
else:
	print(False)

exercise4 = 'in Book and below'"""

"""def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			print('True')
			return 'True'
		else:
			print('False')
			return 'False'

any_lowercase2('HOUSE')"""

"""def any_lowercase3(s):
	for c in s:
		flag = c.islower()
	print(flag)
	return

any_lowercase3('HOUSE')"""

"""def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
		print(flag)
	return

any_lowercase4('HOUse')"""

"""def any_lowercase1(s):
	for c in s:
		if c.islower():
			print(True)
			return
		else:
			print(False)
			return

any_lowercase1('douse')"""

"""def any_lowercase5(s):
	for c in s:
		if not c.islower():
			print(False)
			return
	print(True)
	return

any_lowercase5('House')"""

def rotate_word(word, enc):
	og_string = word
	new_string = ''
	index = 0
	while index < len(og_string):
		letter = og_string[index]
		position = ord(letter)
		new_position = position + enc
		new_letter = chr(new_position)
		new_string += new_letter
		index += 1
	print(new_string)

rotate_word('ibm', -1)