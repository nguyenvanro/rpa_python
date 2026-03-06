# # Toán tử số học
a = 8
b = 3
# Cộng
c = a + b
# Trừ
d = a - b
# Nhân
e = a * b
# Chia
f = a / b
# Chia lấy phần dư
g = a % b
print("Kết quả chia lấy dư: ", g)
# Chia lấy phần nguyên
h = a // b
print("Kết quả chia lấy phần nguyên: ", h)

# Lũy thừa
k = a ** b
print("Kết quả lũy thừa: ", k)

# ưu tiên phép tính: dấu ngoặc, **, *, /, +, -
result_1 =  2 + 3 * 3**2
print(result_1) # 29
result_2 =  2 + (3 * 3)**2
print(result_2) # 83


# Toán tử gán
money_init = 2000000
# Mua áo quần 1.000.000 đồng
buy_clothes = 1000000
# money_init = money_init - buy_clothes
money_init -= buy_clothes

# Mua đồ ăn 1.550.000 đồng
buy_food = 1555000
# money_init = money_init - buy_food
money_init -= buy_food

# Đi làm thêm được 3.000.000 đồng
work = 3000000
# money_init = money_init + work
money_init += work

# Số tiền còn lại là bao nhiêu?
print("Số tiền còn lại là: ", money_init)


# Toán tử so sánh
# Một sản phẩm giá 350.000 đồng.
product_price = 350.000
# Nhập số tiền khách đưa vào và kiểm tra:
money_guest = float(input("Nhập số tiền khách: "))
result_compare = money_guest >= product_price
# Có đủ tiền để mua không?
if result_compare:
    print("Có đủ tiền để mua")

else:
    print("Không đủ tiền để mua")
    
# Có dư tiền không?


# 4. Nhập vào một số nguyên, kiểm tra số đó là chẵn hay lẻ

# Câu điều kiện
diem_trung_binh = float(input("Nhập điểm trung bình: "))
# Giỏi >= 8.5
if diem_trung_binh >= 8.5:
    print("Giỏi")
# Khá >= 6.5
elif diem_trung_binh >= 6.5:
    print("Khá")
# Trung bình >=5
elif diem_trung_binh >= 5:
    print("Trung bình")
# Yếu < 5
else:
    print("Yếu")


# Toán tử so sánh
price_product = 350000
money_guest = int(input("Nhập vào số tiền của khách: "))
result_compare = money_guest >= price_product
print("So sánh tiền guest với sản phẩm: ", result_compare)
if result_compare:
    print("Đủ tiền mua")
else:
    print("Không Đủ tiền mua")

# kiểm tra số chẵn, lẻ
number = int(input("Nhập vào số nguyên: "))
if number % 2 == 0:
    print("số chẵn")
else:
    print("Số lẻ")

# Câu điều kiện
diem_trung_binh = float(input("Nhập vào số điểm trung bình: "))
if diem_trung_binh > 0:
    pass

if diem_trung_binh >= 8.5:
    print("Giỏi")
if diem_trung_binh >= 6.5:
    print("Khá")
if diem_trung_binh >= 5:
    print("trung bình")
else:
    print("yếu")

def func():
    pass

# for: vòng Lặp đi hết phần tử
for element in [1,3,3,4,5,6,7,9]:
    if element == 3:
        # pass: lệnh viết cho đẹp cú pháp
        pass
    if element == 4:
        # thoát khỏi vòng lặp
        break
    if element == 5:
        # tiếp tục vòng lặp và bỏ quả những dòng code phía sau continue
        continue
    print('abc')
    if element == 6:
        print(element)

# while: vòng lặp đến khi điều kiện còn thỏa mãn


# 3. Tính tổng các số chẵn từ 1 đến 100
print(sum([i for i in range(1, 101) if i % 2 == 0]))
