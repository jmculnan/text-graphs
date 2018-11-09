#helper functions

def preprocess(data):
    """
    Read in the data and add to an array
    that is split by sentences.
    """
    with open(data, 'r') as dfile:
        all_data = []
        for line in dfile:
            all_data.append(line.strip())
    return all_data
