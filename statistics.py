import os
import subprocess


def collect_statistics(directory):
    positive = 0
    negative = 0
    false_positive = 0
    false_negative = 0
    rej = 1
    acc = 0

    for filename in os.listdir(directory):

        file_path = directory + '\\' + filename
        my_result = subprocess.run(['py', 'main.py', file_path], capture_output=True, text=True)

        if my_result.returncode and rej:
            negative += 1
        elif not my_result.returncode and not rej:
            positive += 1
        elif not my_result.returncode and rej:
            false_positive += 1
        elif my_result.returncode and not rej:
            false_negative += 1

    return {
        'positive': positive,
        'negative': negative,
        'false_positive': false_positive,
        'false_negative': false_negative
    }


print(collect_statistics("C:\\Users\\sasho\\PycharmProjects\\MatrixIndentation\\indent_check-master2\\indent_check-master\\tests\\rej"))
