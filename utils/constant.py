import yaml


class FilePath:
    CONFIG = "config/DetectOutlier.yml"
    DATA = "data/DetectOutlier.csv"
    LOG = "logs/log_file.txt"


class ErrorMessage:
    ERROR_NOT_EXIST = "Error: {0} does not exist."


class THRESHOLD:
    def __init__(self):
        with open(FilePath.CONFIG, "r") as File:
            stream = File.read()
        data = yaml.load(stream, Loader=yaml.FullLoader)
        self.CHECK_NUMERIC = data["threshold"]["check_numeric"]
        self.CHECK_LENGTH = data["threshold"]["check_length"]
        self.CHECK_CATEGORY = data["threshold"]["check_category"]
        self.THRESHOLD_ZSCORE = data["threshold"]["threshold_zscore"]
        self.THRESHOLD_IQR = data["threshold"]["threshold_iqr"]
