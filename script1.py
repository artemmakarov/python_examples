print("Enter 'stop' to exit" )
while True:
	reply = input("Enter the number: ")
	if reply == 'stop': break
	elif not reply.isdigit():
		print("Bad!" * 8)
	else:
		print(int(reply) ** 2)
	
print("Bye!")

