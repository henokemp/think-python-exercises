def eval_loop():
	while True:
		a = input('What math should I do for you?\n')
		print (eval(a))
		if a == 'done':
			break
	print (eval(a))
	
eval_loop()


