data = []
count = 0

with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 : 
			print(len(data))
print ('檔案讀取完了,總共有', len(data), '筆資料')
print (data[0])

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

# List comprehension
good = [d for d in data if 'good' in d]
	
print ('一共有', len(good), '筆留言有good')

wc = {} # word count 

for d in data : 
	words = d.split()
	for word in words: 
		if word in wc: 
			wc[word] += 1
		else :
			wc [word] = 1  # 新增新的Key到wc字典  
# print (wc)
for word in wc :
	if wc[word] > 1000000 :
		print (word, wc[word])
print (len(wc))

while True : 
	word = input ('請問要查什麼字: ')
	if word == 'q' :
		break
	if word in wc : 
		print (word, '出現過的次數為: ', wc[word])
	else :
		print ('這個字沒有出現過哦')

print ('感謝使用本查詢功能')



