import time
while True:
	with open("f.txt", "a") as f:
		f.write("hello\n")
	time.sleep(1)
