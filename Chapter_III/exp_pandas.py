import pandas

# Series
names = ['An', 'Bình', 'Hòa', 'Nam', 'Tiến']

data_series_name = pandas.Series(data=names, name="Name")
print(data_series_name)

print("____________________________________________________-")

ages = ['22', '23', '25', '20', '29']
data_series_ages = pandas.Series(data=ages, name="Age")
print(data_series_ages) 

