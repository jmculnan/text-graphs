#helper functions

def addinput(data):
    """
    Read in the data and add to an array
    that is split by sentences.
    """
    with open(data, 'r') as dfile:
        all_data = []
        for line in dfile:
            all_data.append(line.strip())
    return all_data

def count_common_points(sent1,sent2):
    """
    Count number of identical items in two sentences
    """
    i = -1 #to counteract periods
    for item in sent1:
        if item in sent2:
            i += 1
    return i
