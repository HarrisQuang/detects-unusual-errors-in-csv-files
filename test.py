# import numpy as np
# import pandas as pd
# import view_point

# df = pd.DataFrame([1, 2, 3, 4, 5], columns=["Demo"])
# ser = df.apply(view_point.check_numeric, axis=0)

# data = np.array(["[OK, 1.0]"])
# ser = pd.Series(["[OK, 1.0]"], index=["BANKCode"])

# data = pd.Series([1, 2, 3, 4, 5, 6])
# result = view_point.check_numeric(data)
# print(type(result))

# print(round(2/7, 2))


# print(ser)

# import sys
# sys.path.append(
#     '/home/home/Downloads/big-assignment-2/DSP101x_ASM2_haiqkFX03099/')

# print(sys.path)

# import sys
# sys.path.append("..")


# from my_project.utils.utility import *

import numpy as np
import pandas as pd

# list = [1, 2, None, 4]

# print(summary_for_check_length(list))

# item_1 = list[2]
# ser = pd.Series(list)
# item = str(ser.to_list()[2])
# result = item + "Jai"
# print(item_1)
# print(result)

# df = pd.read_csv("my_project/data/DetectOutlier.csv")
# print(df)

# list = [1, 2, 3, None]
# sr = pd.Series(list)
# new_list = sr.to_list()
# print(new_list[3])
# if str(new_list[3]) == 'nan':
#     a = 5
# else:
#     a = 0
# print(a)


# list = [None, None, None]
# df = pd.DataFrame(list)
# ser = df.stack().value_counts()
# count_list = df.stack().value_counts().to_list()


# std = np.std(count_list)


# print(std)

df = pd.read_csv("data/DetectOutlier.csv")
print(df[["BANKCode"]])
df_convert = df["CIF_NO"].astype(
    str).str.replace(".", "", 1).str.isdigit()
