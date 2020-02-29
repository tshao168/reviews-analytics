data = []
count = 0

with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 : 
			print(len(data))
print ('檔案讀取完了,總共有', len(data), '筆資料')
#### 計算平均長度 用 While loop ########
##i = 0 
##Total_len = 0
##while i < len(data) : 
	##Total_len = Total_len + len(data[i])
	##i += 1 
##print ('留言總長度:', Total_len)
##print ('留言總平均長度:', Total_len / len(data))
#### 計算平均長度 用 for loop ########
sum_len = 0 
for d in data :
	sum_len = sum_len + len(d)
print ('留言總長度:', sum_len)
print ('留言平均長度:', sum_len / len(data))
new = []
for d in data :
	if len(d) < 100 :
		new.append(d)
print ('一共有', len(new), '筆留言長度小於100')

good = [] 
for d in data :
	if 'good' in d :
		good.append(d)
print ('一共有', len(good), '筆留言有good')

