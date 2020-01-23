import pandas as pd
import numpy as np
from datetime import datetime
import argparse
import xlsxwriter
import yaml
import utils.utility as util
import utils.constant as const
import view_point

parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    metavar="<folder path>",
    help="designate the path to the directory containing files to check",
    required="true",
)
parser.add_argument(
    "-c", metavar="<config file>", help="designate to the config file", required="true"
)
parser.add_argument(
    "-o",
    metavar="<output_folder>",
    help="the output folder contains summary report and detail report after checking files",
    required="true",
)
args = parser.parse_args()
in_data_file_path = args.i
in_config_file_path = args.c
out_file_path = args.o


file_name = in_data_file_path[in_data_file_path.rfind(
    "/") + 1: in_data_file_path.rfind(".")]
file_extension = in_data_file_path.split(".")[1]
full_file_name = file_name + '.' + file_extension

date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message_type = "ERROR/WARNING"

if __name__ == "__main__":

    if util.check_folder_exist(in_data_file_path) == "False":
        raise argparse.ArgumentTypeError(
            const.ErrorMessage.ERROR_NOT_EXIST.format(in_data_file_path))

    if util.check_folder_exist(out_file_path) == "False":
        raise argparse.ArgumentTypeError(
            const.ErrorMessage.ERROR_NOT_EXIST.format(out_file_path))

    if not file_extension == "csv":
        with open(const.FilePath.LOG, "a") as file:
            file.write(
                "{date_time} {message_type}: The format of {file_name} file is incorrect\n"
            )
    util.create_data_file(in_data_file_path)
    util.create_config_file(in_config_file_path)
    df = util.read_data_file()
    df_check_numeric = df.apply(view_point.check_numeric, axis=0)
    df_check_range = df.apply(view_point.check_range, axis=0)
    df_check_length = df.apply(view_point.check_length, axis=0)
    df_check_category = df.apply(view_point.check_category, axis=0)

    df_check_numeric = df_check_numeric.reset_index()

    df_check_range = df_check_range.reset_index()
    df_check_length = df_check_length.reset_index()
    df_check_category = df_check_category.reset_index()
    list_check_range = util.create_list_from_df(
        df_check_range, "checkRange", full_file_name)
    list_check_numeric = util.create_list_from_df(
        df_check_numeric, "checkNumeric", full_file_name)
    list_check_length = util.create_list_from_df(
        df_check_length, "checkLength", full_file_name)
    list_check_category = util.create_list_from_df(
        df_check_category, "checkCategory", full_file_name)
    total_list = list_check_range + list_check_numeric + \
        list_check_length + list_check_category
    total_df = pd.DataFrame(
        total_list, columns=["File-Name", "Column", "Viewpoint", "Result", "Summary"])
    total_df.to_excel(f"{out_file_path}/summary.xlsx",
                      sheet_name="Sheet 1", index=False, header=True)
