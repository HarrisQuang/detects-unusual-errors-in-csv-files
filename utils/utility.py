import yaml
import pandas as pd
import numpy as np
import os
import functools
import shutil
import utils.constant as const
from datetime import datetime

config_file_path = const.FilePath.CONFIG
log_file_path = const.FilePath.LOG
data_file_path = const.FilePath.DATA


def check_folder_exist(folder_path):
    if not os.path.isdir(folder_path):
        return False
    return True


def create_data_file(in_data_file_path):
    shutil.copy2(in_data_file_path, data_file_path)


def create_config_file(in_config_file_path):
    shutil.copy2(in_config_file_path, config_file_path)


def read_data_file():
    df = pd.read_csv(data_file_path)
    return df


def create_list_from_df(old_df, title, file_name):
    new_list = []
    i = 0
    while i < old_df.shape[0]:
        rearrange_list = []
        temp_list = old_df.iloc[i].tolist()
        rearrange_list.extend(
            [file_name, temp_list[0], title, temp_list[1][0], temp_list[1][1]])
        new_list.append(rearrange_list)
        i += 1
    return new_list


def summary_for_check_length(items):
    num_of_values = len(items)
    list_of_length = []
    for item in items:
        item = str(item)
        if item == "nan" or item == "None":
            list_of_length.append(0)
        list_of_length.append(len(item))
    df = pd.DataFrame(list_of_length)
    count_ser = df.stack().value_counts()
    max_count = max(count_ser.array)
    summary = max_count/num_of_values
    return summary


def summary_for_check_category(items):
    df = pd.DataFrame(items)
    frequency_list = df.stack().value_counts().to_list()
    mean = np.mean(frequency_list)
    std = np.std(frequency_list)
    summary = round(mean/std, 2)
    return summary
