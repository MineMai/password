password = "a123"
inputTime = 3

while True:
	userInput = input("請輸入密碼")
	
	if userInput == password:
		print("登入成功！")
		break
	else:
		inputTime = inputTime - 1
		if inputTime == 0:
			print("帳號已鎖定")
			break
		print("密碼錯誤！還有", inputTime, "機會")
	

