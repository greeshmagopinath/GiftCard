def read_file(filename):
    '''
    Reads a file with keys and values and converts to an array
    :param filename: name of the file
    todo:
     * input validation
     * create model objects for item, value
    :return:  array containing keys and values
    '''
    content = open(filename)
    lines = content.readlines()
    arr = []
    for line in lines:
        item,value = line.strip('\n').split(',')
        arr.append([item,int(value)])
    return arr