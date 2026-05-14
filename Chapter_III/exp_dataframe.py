import pandas as pd

data_dict = {
    # key: value
    # cột: giá trị trong cột
    "Ten": ["An", "Bình", "Minh", "Tuấn"],
    "Tuoi": [22, 23, 22, 24],
    "DiemTB": [8.9, 8.0, 8.5, None],
    "Lop": ["23CT1", "23CT4", "23CT4","23CT1"],
}

df_input = pd.DataFrame(data=data_dict)
print(df_input)
print("______________________________________________________")
# Thêm cột DiaChi, DiemPython


# Lọc dữ liệu
# Truy xuất dòng theo vị trí index
print(df_input.loc[0])
print(df_input.loc[1])
print(df_input.loc[2])
print("______________________________________________________")

# Truy xuất theo tên cột
print(df_input["Ten"])
print("______________________________________________________")

print(df_input["DiemTB"])
print("______________________________________________________")

# truy xuất một ô bất kì: index, tên cột
name = df_input.loc[1, "Ten"]
print(name)
print("______________________________________________________")

# Lọc ra dữ liệu có DiemTB >= 8.0
df_filter = df_input[df_input["DiemTB"] >= 8.0]
print(df_filter)
print("______________________________________________________")

# Lọc ra dữ liệu có DiemTB >= 8.0 và Lớp 23CT4
df_filter_class = df_input[(df_input["DiemTB"] >= 8.0) & (df_input["Lop"] == "23CT4")]
print(df_filter_class)

# Lọc ra dữ liệu học sinh yếu

# Lọc ra dữ liệu học sinh trung bình

# phân biệt None(NULL) với ''
my_var = None
my_str = ''
my_name = 'An'
print("______________________________________________________")

# Xóa dữ liệu trống
print(df_input.dropna())
print("______________________________________________________")

# Điềm số 0 vào ô trống
print(df_input.fillna(0))
print("______________________________________________________")

# Nhóm theo Lop
df_group = df_input.groupby("Lop")
print(df_group)
for i_group in df_group:
    print(i_group)
    print("---------------------------------------")
print()