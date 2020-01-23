import numpy as np
import pandas as pd
import utils.constant as const


def check_numeric(items):
    # num_of_values = sum(1 - item.isnull())
    threshold = const.THRESHOLD().CHECK_NUMERIC
    num_of_values = len(items)
    num_of_numerics = sum(items.astype(
        str).str.replace(".", "", 1).str.isdigit())
    if not num_of_values == 0:
        summary = round(num_of_numerics / num_of_values, 2)
        if summary < threshold:
            return ["NA", summary]
        elif summary >= threshold and summary < 1:
            return ["NG", summary]
        else:
            return ["OK", summary]


def check_range(items):
    threshold_iqr = const.THRESHOLD().THRESHOLD_IQR
    threshold_z_score = const.THRESHOLD().THRESHOLD_ZSCORE
    num_of_values = len(items)
    num_of_numeral = sum(items.astype(
        str).str.replace(".", "", 1).str.isdigit())
    if num_of_numeral / num_of_values == 1:
        q2 = np.quantile(items, 0.50)
        q1 = np.quantile(items, 0.25)
        q3 = np.quantile(items, 0.75)
        iqr = q3 - q1
        low = q1 - threshold_iqr * iqr
        up = q3 + threshold_iqr * iqr
        mean = np.mean(items)
        std = np.std(items)
        summary = round(mean / std, 2)
        outliers = 0
        for item in items:
            z_score_i = (item - mean) / std
            if item < low or item > up or np.absolute(z_score_i) > threshold_z_score:
                outliers += 1
        if outliers == 0:
            return ["OK", summary]
        else:
            return ["NG", summary]
    else:
        return ["NA", "null"]


def check_length(items):
    threshold = const.THRESHOLD().CHECK_LENGTH
    # num_of_values = sum(1 - items.isnull())
    num_of_values = len(items)
    length_list = []
    for item in items.astype(str):
        if item == "nan":
            length_list.append(0)
        length_list.append(len(item))
    df = pd.DataFrame(length_list)
    # mean = df.mean()
    # std = df.std()
    counts_dict = df.stack().value_counts().to_dict()
    max_count = max(counts_dict.values())
    summary = round(max_count / num_of_values, 2)
    if not num_of_values == 0:
        if summary < threshold:
            return ["NA", summary]
        elif summary >= threshold and summary < 1:
            return ["NG", summary]
        else:
            return ["OK", summary]


def check_category(items):
    threshold = const.THRESHOLD().CHECK_CATEGORY
    df = pd.DataFrame(items)
    freq_range_list = df.stack().value_counts().to_list()
    # freq_range_list = list(freq_range_dict.values())
    if not freq_range_list == []:
        mean = np.mean(freq_range_list)
        std = np.std(freq_range_list)
        if not std == 0:
            summary = round(mean / std, 2)
            z_score_list = []
            for item in freq_range_list:
                z_score = round((item - mean) / std, 2)
                z_score_list.append(z_score)
            outliers = 0
            for item in z_score_list:
                if item < -threshold:
                    outliers += 1
            if outliers == 0:
                return ["OK", summary]
            else:
                return ["NG", summary]
        else:
            return["NA", "null"]
    else:
        return["NA", "null"]
