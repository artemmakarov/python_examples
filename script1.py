print("Enter 'stop' to exit" )
while True:
	reply = input("Enter the number: ")
	if reply == 'stop': break
	try:
		num = int(reply)
	except:
		print("Bad!" * 8)
	else:
		print(int(reply) ** 2)
	
print("Bye!")

