#開車年齡
driving = input('請問你沒有開過車?')
if driving != '有' and driving != '沒有':
    print('請輸入 有/沒有')
    raise SystemExit
age = input('請問你的年紀?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗!')
	else:
		print('抓去關!')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照囉')
	else:
		print('再忍幾年你就可以考駕照了')
	