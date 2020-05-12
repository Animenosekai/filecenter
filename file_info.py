#                                  File Info
#
# for Python 3
# ©Anime no Sekai - 2020
#


# Imports
import os

########## TOOLS ##########
def get_size(bytes, suffix="B"):
    """
    Credit to PythonCode for this function.
    > https://www.thepythoncode.com/article/get-hardware-system-information-python
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_correct_path(path):
    indexes_of_slash = [i for i, ltr in enumerate(path) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = path[index + 1 - number_of_iterations]
        print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            path = path[:index - number_of_iterations] + path[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    return path


########## INDIVIDUAL ##########

def exists(file):
    correct_path = get_correct_path(file)
    return(os.path.exists(correct_path))

def isdir(file):
    correct_path = get_correct_path(file)
    return(os.path.isdir(correct_path))

def isfile(file):
    correct_path = get_correct_path(file)
    return(os.path.isfile(correct_path))

def base(file):
    file_base = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_base = os.path.basename(correct_path)
    else:
        file_base = 'An error occured while getting the file'
    return(file_base)

def path(file):
    file_path = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_path = os.path.abspath(correct_path)
    else:
        file_path = 'An error occured while getting the file'
    return(file_path)

def name(file):
    file_base = ''
    filename = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_base = os.path.basename(correct_path)
        filename, file_extension = os.path.splitext(file_base)
    else:
        filename = 'An error occured while getting the file'
    return(filename)

def extension(file):
    file_base = ''
    file_extension = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_base = os.path.basename(correct_path)
        filename, file_extension = os.path.splitext(file_base)
    else:
        file_extension = 'An error occured while getting the file'
    return(file_extension)

def size(file):
    size = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        size_in_bytes = os.path.getsize(correct_path)
        size = get_size(size_in_bytes)
    else:
       size = 'An error occured while getting the file'
    return(size)

def size_in_bytes(file):
    size_in_bytes = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        size_in_bytes = os.path.getsize(correct_path)
    else:
       size_in_bytes = 'An error occured while getting the file'
    return(size_in_bytes)

def file_stat(file):
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
    else:
        file_stat = 'An error occured while getting the file'
    return(file_stat)

def last_access(file):
    last_access = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_access = file_stat.st_atime
    else:
       last_access = 'An error occured while getting the file'
    return(last_access)

def last_access_nanoseconds(file):
    last_access_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_access_nanoseconds = file_stat.st_atime_ns
    else:
       last_access_nanoseconds = 'An error occured while getting the file'
    return(last_access_nanoseconds)

def last_modification(file):
    last_modification = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_modification = file_stat.st_mtime
    else:
       last_modification = 'An error occured while getting the file'
    return(last_modification)

def last_modification_nanoseconds(file):
    last_modification_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_modification_nanoseconds = file_stat.st_mtime_ns
    else:
       last_modification_nanoseconds = 'An error occured while getting the file'
    return(last_modification_nanoseconds)

def last_metadata_change(file):
    last_metadata_change = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_metadata_change = file_stat.st_ctime
    else:
       last_metadata_change = 'An error occured while getting the file'
    return(last_metadata_change)

def last_metadata_change_nanoseconds(file):
    last_metadata_change_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_metadata_change_nanoseconds = file_stat.st_ctime_ns
    else:
       last_metadata_change_nanoseconds = 'An error occured while getting the file'
    
    return(last_metadata_change_nanoseconds)



########## GROUPS ##########

def get_path_info(file):
    path_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        #FILENAME, EXTENSTION AND LOCATION
        try:
            file_base = os.path.basename(correct_path)
            file_path = os.path.abspath(correct_path)
            filename, file_extension = os.path.splitext(file_base)
            path_info['file_base'] = file_base
            path_info['file_path'] = file_path
            path_info['filename'] = filename
            path_info['file_extension'] = file_extension
        except:
            print("An error occured while getting this file's name")
            path_info['file_base'] = 'Error'
            path_info['file_path'] = 'Error'
            path_info['filename'] = 'Error'
            path_info['file_extension'] = 'Error'
    else:
       path_info['information'] = 'An error occured while searching for your file.'

    return(path_info)

def get_size_info(file):
    size_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        #SIZE
        try:
            size_in_bytes = os.path.getsize(correct_path)
            size_info['size_in_bytes'] = size_in_bytes
            size_info['size'] = get_size(size_in_bytes)
        except:
            print("An error occured while getting this file's size")
            size_info['size_in_bytes'] = 'Error'
            size_info['size'] = 'Error'
    else:
       size_info['information'] = 'An error occured while searching for your file.'

    return(size_info)

def get_timestamps(file):
    timestamps_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        #TIMESTAMPS
        try:
            file_stat = os.stat(correct_path)
            last_access = file_stat.st_atime
            last_access_nanoseconds = file_stat.st_atime_ns
            last_modif = file_stat.st_mtime
            last_modif_nanoseconds = file_stat.st_mtime_ns
            last_metadata_change = file_stat.st_ctime
            last_metadata_change_nanoseconds = file_stat.st_ctime_ns
            
            timestamps_info['file_stat'] = file_stat
            timestamps_info['last_access'] = last_access
            timestamps_info['last_access_nanoseconds'] = last_access_nanoseconds
            timestamps_info['last_modification'] = last_modif
            timestamps_info['last_modification_nanoseconds'] = last_modif_nanoseconds
            timestamps_info['last_metadata_change'] = last_metadata_change
            timestamps_info['last_metadata_change_nanoseconds'] = last_metadata_change_nanoseconds
        except:
            print("An error occured while getting timestamps for this file")
            timestamps_info['file_stat'] = 'Error'
            timestamps_info['last_access'] = 'Error'
            timestamps_info['last_access_nanoseconds'] = 'Error'
            timestamps_info['last_modification'] = 'Error'
            timestamps_info['last_modification_nanoseconds'] = 'Error'
            timestamps_info['last_metadata_change'] = 'Error'
            timestamps_info['last_metadata_change_nanoseconds'] = 'Error'
    else:
       timestamps_info['information'] = 'An error occured while searching for your file.'

    return(timestamps_info)







########## EVERYTHING ##########

def info(file):
    file_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        #FILENAME, EXTENSTION AND LOCATION
        try:
            file_base = os.path.basename(correct_path)
            file_path = os.path.abspath(correct_path)
            filename, file_extension = os.path.splitext(file_base)
            file_info['file_base'] = file_base
            file_info['file_path'] = file_path
            file_info['filename'] = filename
            file_info['file_extension'] = file_extension
        except:
            print("An error occured while getting this file's name")
            file_info['file_base'] = 'Error'
            file_info['file_path'] = 'Error'
            file_info['filename'] = 'Error'
            file_info['file_extension'] = 'Error'
        #SIZE
        try:
            size_in_bytes = os.path.getsize(correct_path)
            file_info['size_in_bytes'] = size_in_bytes
            file_info['size'] = get_size(size_in_bytes)
        except:
            print("An error occured while getting this file's size")
            file_info['size_in_bytes'] = 'Error'
            file_info['size'] = 'Error'
        #TIMESTAMPS
        try:
            file_stat = os.stat(correct_path)
            last_access = file_stat.st_atime
            last_access_nanoseconds = file_stat.st_atime_ns
            last_modif = file_stat.st_mtime
            last_modif_nanoseconds = file_stat.st_mtime_ns
            last_metadata_change = file_stat.st_ctime
            last_metadata_change_nanoseconds = file_stat.st_ctime_ns
            
            file_info['file_stat'] = file_stat
            file_info['last_access'] = last_access
            file_info['last_access_nanoseconds'] = last_access_nanoseconds
            file_info['last_modification'] = last_modif
            file_info['last_modification_nanoseconds'] = last_modif_nanoseconds
            file_info['last_metadata_change'] = last_metadata_change
            file_info['last_metadata_change_nanoseconds'] = last_metadata_change_nanoseconds
        except:
            print("An error occured while getting timestamps for this file")
            file_info['file_stat'] = 'Error'
            file_info['last_access'] = 'Error'
            file_info['last_access_nanoseconds'] = 'Error'
            file_info['last_modification'] = 'Error'
            file_info['last_modification_nanoseconds'] = 'Error'
            file_info['last_metadata_change'] = 'Error'
            file_info['last_metadata_change_nanoseconds'] = 'Error'
    else:
       file_info['information'] = 'An error occured while searching for your file.' 
    return file_info




# Testing

os.system('cls' if os.name == 'nt' else 'clear')
file = input('File: ')
os.system('cls' if os.name == 'nt' else 'clear')
results = info(file)
print('{')
for info in results:
    print(info + ': ' + str(results[info]))
print('     }')