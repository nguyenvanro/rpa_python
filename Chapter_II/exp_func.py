a = 1 + 2
c = 2 + 4
d = 5 + 7
e = 10 + 7

def tinh_tong(a, b):
    tong = a + b
    return tong, "abc", True

tong = tinh_tong(a=1, b=2)
print("tong = ", tong)
print("tong type", type(tong))

tong_2, my_str, my_boolean = tinh_tong(a=2, b=4)
print("tong_2 = ", tong_2)
print("tong_2 type", type(tong_2))
print("my_str type", type(my_str))

# Viết hàm trả về danh sách số chẵn từ 1 -> 10
def so_chan():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    danh_sach_so_chan = []
    tong = 0
    for element in numbers:
        if element % 2 == 0:
            danh_sach_so_chan.append(element)
            tong += element
    return danh_sach_so_chan, tong

danh_sach_so_chan, tong = so_chan()
print(danh_sach_so_chan)
print(tong)

def say_welcome(name="You"):
    print("Hello, ", name)

say_welcome()
say_welcome('Anh')


var_global = 10
def func():
    var_local = 20
    print("var_local", var_local)
    print("var_global", var_global)

func()
print("var_local", var_local)
print("var_global", var_global)

# Viết hàm trả về tổng số chẵn từ 1 -> 10