#讓使用者輸入商品名稱、價格
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append ([name, price])
print(products)

for p in products:
	print(p[0])

#印出購買紀錄
for p in products:
	print(p[0],'的價格是', p[1])

#讀取檔案
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品名稱,價格' in line:
			continue #繼續
		name, price = line. stripe().spilt(',')
		products.append([name, price])
print(products)

#寫入檔案
with open('products.csv', 'w' , encoding='utf-8') as f:
	f.write('商品名稱,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')