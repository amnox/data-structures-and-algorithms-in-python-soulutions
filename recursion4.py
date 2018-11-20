import os


def find_cumulative_size(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            total += find_cumulative_size(os.path.join(path, filename))
    print('{0:<7}'.format(total), path)
    return total


find_cumulative_size('C:\Titanfall\\')