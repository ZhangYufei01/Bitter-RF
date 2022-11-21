
def Main_data_name(File):
    file = File
    file_list = file.split('/')
    length = len(file_list)
    file_path = ''
    for i in range(length-2):
        file_path = file_path + file_list[i] + '/'
    file_path = file_path.rstrip('/')

    file_name_total = file_list[length-1]
    file_name = file_name_total.split('.')
    file_name = file_name[0]
    list = [file_path,file_name]

    return(list)


