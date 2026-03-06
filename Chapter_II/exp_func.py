# Hàm
1 + 2
2 + 3
4 + 10

def tinh_tong(a, b):
    tong = a + b
    # return tong, "abc", True

result = tinh_tong(a=1, b=2)
print("tong 1: ", result)
print("type tong: ", type(result))

tong, my_str, my_boolean = tinh_tong(a=4, b=10)
print("tong 2: ", tong)
print("type tong: ", type(tong))
print("type my_str: ", type(my_str))

# print()

# # viết hàm trả về danh sách số chẵn từ 1 -> 10
def danh_sach_so_chan():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    so_chan = []
    tong = 0
    for i in numbers:
        if i % 2 == 0:
            so_chan.append(i)
            tong += i
    return so_chan, tong

so_chan, tong = danh_sach_so_chan()
 
def say_welcom(name="You"):
    print("hello ", name)

say_welcom()
say_welcom(name="An")

# Viết hàm trả về tổng số chẵn từ 1 -> 10


# local vs global
var_global = 12
def func_test():
    var_local = 10
    print("local: ", var_local)
    print("global: ", var_global)

func_test()
print("local: ", var_local)
print("global: ", var_global)