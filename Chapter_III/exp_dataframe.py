import pandas as pd

data_dict = {
    "Ten": ["Anh", "Bình", "Minh", "Tuấn"],
    "Lop": ["23CT1", "23CT1", "23CT1", "23CT2"],
    "DiemTB": [8.0, 7.9, None, 9.0],
    "Tuoi": [20, 20, 21, 23],
}

df_input = pd.DataFrame(data=data_dict)
print(df_input)
# Thêm cột địa chỉ(DiaChi)
print("________________________________________________")

# truy xuất cột: Ten
print(df_input["Ten"])
print("________________________________________________")

# Truy xuất cột: DiemTB
print(df_input["DiemTB"])
print("________________________________________________")

# truy xuất dòng: row
print(df_input.loc[0])
print("________________________________________________")

# lấy ra giá trị trong ô =index, tên cột
print(df_input.loc[1, "Ten"])
print("________________________________________________")

# Lấy ra giá trị tại cột DiemTB dòng cuối cùng

# Lọc dữ liệu
# Lọc ra những học sinh có DiemTB >= 8.0
df_filter_point = df_input[df_input["DiemTB"] >= 8.0]
print(df_filter_point)
print("________________________________________________")

# Lọc ra những học sinh có DiemTB >= 8.0 và Lớp 23CT1
df_filter_2 = df_input[(df_input["DiemTB"] >= 8.0) & (df_input["Lop"] == "23CT1")]
print(df_filter_2)
print("________________________________________________")

# So sánh None(NULL) với ""
my_var = None
my_str = " "
my_name = "An"
print("________________________________________________")

# Xóa dữ liệu dòng trống: NaN
print(df_input.dropna())
print("________________________________________________")

# Điền dữ liệu vào dòng trống: NaN
print(df_input.fillna(0))
print("________________________________________________")

# groupby: cột Lớp - lấy ra bảng điểm theo lớp
df_group_by = df_input.groupby("Lop")
print(df_group_by)
for i_group in df_group_by:
    print(i_group)
    print("_____________________________")
print()