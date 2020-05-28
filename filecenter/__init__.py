#                                  File Center
#
# for Python 3
# © Anime no Sekai - 2020
#

# Imports
import shutil
import subprocess
import platform
import os
import mimetypes
import datetime

# Data imports
from . import data_ext_to_human_readeable
from . import data_extension_desc
from . import data_type
from . import data_common

########## TOOLS ##########
def get_readeable_size(bytes, suffix="B"):
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
        #print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            path = path[:index - number_of_iterations] + path[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    return path

def move(origin, destination):
    correct_path_of_origin = get_correct_path(origin)
    correct_path_of_destination = get_correct_path(destination)
    try:
        shutil.move(correct_path_of_origin, correct_path_of_destination)
        return 0
    except:
        return 1

def delete(file):
    correct_path = get_correct_path(file)
    if os.path.isdir(correct_path):
        try:
            shutil.rmtree(correct_path)
            return 0
        except:
            return 3
    elif os.path.isfile(correct_path):
        try:
            os.remove(correct_path)
            return 0
        except:
            return 2
    else:
        return 1

def open(file):
    file_path = get_correct_path(file)
    try:
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', file_path))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(file_path)
        else:                                   # linux variants
            subprocess.call(('xdg-open', file_path))
        return 0
    except:
        return 1

def make_dir(path_of_new_dir):
    path = get_correct_path(path_of_new_dir)
    try:
        os.makedirs(path)
        return path
    except:
        return 'Error while making the new folder'

def files_in_dir(path_of_dir):
    path = get_correct_path(path_of_dir)
    return os.listdir(path)

def os_name():
    return os.name

########## INDIVIDUAL ##########

def exists(path):
    correct_path = get_correct_path(file)
    return(os.path.exists(correct_path))

def isdir(path):
    correct_path = get_correct_path(file)
    return(os.path.isdir(correct_path))

def isfile(path):
    correct_path = get_correct_path(file)
    return(os.path.isfile(correct_path))

def issymboliclink(path):
    correct_path = get_correct_path(file)
    return(os.path.islink(correct_path))

def ismountpoint(path):
    correct_path = get_correct_path(file)
    return(os.path.ismount(correct_path))

def get_real_path(path):
    correct_path = get_correct_path(file)
    return(os.path.realpath(correct_path))

###### FROM EXTENSION ######

def iscommon(file_extension):
    if file_extension in data_common.common_extensions():
        common = True
    else:
        common = False
    return(common)

def popularity(file_extension):
    if file_extension in data_common.common_extensions():
        popularity = 'Very popular'
    elif file_extension in data_common.common_extensions_extended():
        popularity = 'Quite popular'
    else:
        popularity = 'Not very popular'

    return(popularity)

def type_from_extension(extension):
    file_extension = extension
    if file_extension in data_type.archive():
        type = 'Archive'
    elif file_extension in data_type.audio():
        type = 'Audio'
    elif file_extension in data_type.backup():
        type = 'Backup'
    elif file_extension in data_type.book():
        type = 'eBook'
    elif file_extension in data_type.database():
        type = 'Database File'
    elif file_extension in data_type.developer():
        type = 'Developer'
    elif file_extension in data_type.disk_image():
        type = 'Disk Image'
    elif file_extension in data_type.encoded():
        type = 'Encoded File'
    elif file_extension in data_type.executable():
        type = 'Application/Executable'
    elif file_extension in data_type.font():
        type = 'Font'
    elif file_extension in data_type.image_3d():
        type = '3D Image'
    elif file_extension in data_type.plugin():
        type = 'Plugin'
    elif file_extension in data_type.preset():
        type = 'Preset/Settings'
    elif file_extension in data_type.raster_image():
        type = 'Image'
    elif file_extension in data_type.raw_image():
        type = 'Raw Image'
    elif file_extension in data_type.rom():
        type = 'ROM/Game File'
    elif file_extension in data_type.spreadsheet():
        type = 'Spreadsheet'
    elif file_extension in data_type.system():
        type = 'System File'
    elif file_extension in data_type.text():
        type = 'Text File/Document'
    elif file_extension in data_type.vector_image():
        type = 'Vector Image'
    elif file_extension in data_type.video():
        type = 'Video'
    elif file_extension in data_type.web():
        type = 'Web Document'
    elif file_extension == '':
        type = 'Folder'
    elif file_extension == '.pdf':
        type = 'Document'
    else:
        type = 'unknown'
    return type

def extension_to_human_readeable(extension):
    if extension in data_common.common_extensions_extended():
        result = data_common.common_extensions_human_readable()[extension]
    else:
        result = data_ext_to_human_readeable.file_extension_to_human_readable(extension)
    return result

def extension_info(extension):
    result = data_extension_desc.extension_info(extension)
    result['type'] = type_from_extension(extension)
    return result

def extension_description(extension):
    result = data_extension_desc.extension_description(extension)
    return result

def extension_usage(extension):
    result = data_extension_desc.extension_usage(extension)
    return result

###### FROM BASE ######

def name_from_base(base):
    filename = ''
    try:
        filename, _ = os.path.splitext(base)
    except:
        filename = 'An error occured while getting the file base'
    return filename


def extension_from_base(base):
    extension = ''
    try:
        _, extension = os.path.splitext(base)
    except:
        extension = 'An error occured while getting the file base'
    return extension


###### FROM EXISTING FILE ######
def osstat_mode(file):
    permissions = 0
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        permissions = file_stat.st_mode
    else:
       permissions = 0
    return(permissions)

def permissions_in_oct(file):
    permissions = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        permissions = oct(file_stat.st_mode & 0o777)
    else:
       permissions = 'Unable to get the file permissions'
    return(permissions)


def permissions(file):
    octal = {'0': 'no permission', '1': 'execute', '2': 'write', '3': 'write and execute', '4': 'read', '5': 'read and execute', '6': 'read and write', '7': 'read, write and execute'}
    permissions = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        octal_permissions = permissions_in_oct(file)
        owner = octal_permissions[2]
        group = octal_permissions[3]
        others = octal_permissions[4]
        permissions['owner'] = octal[owner]
        permissions['group'] = octal[group]
        permissions['others'] = octal[others]
    else:
       permissions = {'information': 'Unable to get permissions'}
    return(permissions)




def mimetype(file):
    mimetype = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        mimetype_tuple = mimetypes.guess_type(correct_path)
        mimetype = mimetype_tuple[0]
    else:
        mimetype = 'An error occured while getting the file'
    return(mimetype)

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
        filename, _ = os.path.splitext(file_base)
    else:
        filename = 'An error occured while getting the file'
    return(filename)


def extension(file):
    file_base = ''
    file_extension = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_base = os.path.basename(correct_path)
        _, file_extension = os.path.splitext(file_base)
    else:
        file_extension = 'An error occured while getting the file'
    return(file_extension)

def size(file):
    size = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        size_in_bytes = os.path.getsize(correct_path)
        size = get_readeable_size(size_in_bytes)
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


def last_access_raw(file):
    last_access_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_access_nanoseconds = file_stat.st_atime_ns
    else:
       last_access_nanoseconds = 'An error occured while getting the file'
    return(last_access_nanoseconds)


def last_modification_raw(file):
    last_modification_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_modification_nanoseconds = file_stat.st_mtime_ns
    else:
       last_modification_nanoseconds = 'An error occured while getting the file'
    return(last_modification_nanoseconds)

def last_metadata_change_raw(file):
    last_metadata_change_nanoseconds = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_metadata_change_nanoseconds = file_stat.st_ctime_ns
    else:
       last_metadata_change_nanoseconds = 'An error occured while getting the file'
    
    return(last_metadata_change_nanoseconds)

def last_access(file):
    last_access = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_access = file_stat.st_atime
        last_access = datetime.datetime.fromtimestamp(last_access)
    else:
       last_access = 'An error occured while getting the file'
    return(last_access)

def last_modification(file):
    last_modification = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_modification = file_stat.st_mtime
        last_modification = datetime.datetime.fromtimestamp(last_modification)
    else:
       last_modification = 'An error occured while getting the file'
    return(last_modification)

def last_metadata_change(file):
    last_metadata_change = ''
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_stat = os.stat(correct_path)
        last_metadata_change = file_stat.st_ctime
        last_metadata_change = datetime.datetime.fromtimestamp(last_metadata_change)
    else:
       last_metadata_change = 'An error occured while getting the file'
    return(last_metadata_change)

#mod_timestamp = datetime.datetime.fromtimestamp(path.getmtime(<YOUR_PATH_HERE>))

def type(file):
    type = ''
    correct_path = get_correct_path(file)
    file_extension = extension(file)
    if os.path.isdir(correct_path):
        type = 'Folder/Directory'
    elif file_extension in data_type.archive():
        type = 'Archive'
    elif file_extension in data_type.audio():
        type = 'Audio'
    elif file_extension in data_type.backup():
        type = 'Backup'
    elif file_extension in data_type.book():
        type = 'eBook'
    elif file_extension in data_type.database():
        type = 'Database File'
    elif file_extension in data_type.developer():
        type = 'Developer'
    elif file_extension in data_type.disk_image():
        type = 'Disk Image'
    elif file_extension in data_type.encoded():
        type = 'Encoded File'
    elif file_extension in data_type.executable():
        type = 'Application/Executable'
    elif file_extension in data_type.font():
        type = 'Font'
    elif file_extension in data_type.image_3d():
        type = '3D Image'
    elif file_extension in data_type.plugin():
        type = 'Plugin'
    elif file_extension in data_type.preset():
        type = 'Preset/Settings'
    elif file_extension in data_type.raster_image():
        type = 'Image'
    elif file_extension in data_type.raw_image():
        type = 'Raw Image'
    elif file_extension in data_type.rom():
        type = 'ROM/Game File'
    elif file_extension in data_type.spreadsheet():
        type = 'Spreadsheet'
    elif file_extension in data_type.system():
        type = 'System File'
    elif file_extension in data_type.text():
        type = 'Text File/Document'
    elif file_extension in data_type.vector_image():
        type = 'Vector Image'
    elif file_extension in data_type.video():
        type = 'Video'
    elif file_extension in data_type.web():
        type = 'Web Document'
    elif file_extension == '':
        type = 'Folder'
    elif file_extension == '.pdf':
        type = 'Document'
    else:
        type = 'unknown'
    return type








########## EVERYTHING ##########

def info(file):
    file_info = {}
    correct_path = get_correct_path(file)
    if os.path.exists(correct_path):
        file_info['exists'] = exists(file)
        file_info['isdir'] = isdir(file)
        file_info['isfile'] = isfile(file)
        file_info['issymboliclink'] = issymboliclink(file)
        file_info['ismountpoint'] = ismountpoint(file)
        file_info['iscommon'] = iscommon(extension(file))
        file_info['extension_popularity'] = popularity(extension(file))
        file_info['mimetype'] = mimetype(file)
        file_info['base'] = base(file)
        file_info['given_path'] = file
        file_info['usable_path'] = correct_path
        file_info['real_path'] = get_real_path(file)
        file_info['name'] = name(file)
        file_info['name_from_base'] = name_from_base(base(file))
        file_info['extension'] = extension(file)
        file_info['extension_from_base'] = extension_from_base(base(file))
        file_info['size'] = size(file)
        file_info['size_in_bytes'] = size_in_bytes(file)
        file_info['full_file_stat'] = file_stat(file)
        file_info['last_access'] = last_access(file)
        file_info['last_modification'] = last_modification(file)
        file_info['last_metadata_change'] = last_metadata_change(file)
        file_info['last_access_nanoseconds_raw'] = last_access_raw(file)
        file_info['last_modification_nanoseconds_raw'] = last_modification_raw(file)
        file_info['last_metadata_change_nanoseconds_raw'] = last_metadata_change_raw(file)
        file_info['osstat_mode'] = osstat_mode(file)
        file_info['permissions_in_oct'] = permissions_in_oct(file)
        file_info['permissions'] = permissions(file)
        file_info['type'] = type(file)
        file_info['type_from_extension'] = type_from_extension(extension(file))
        file_info['human_readable_extension'] = extension_to_human_readeable(file_info['extension'])
        file_info['extension_info'] = extension_info(file_info['extension'])
        file_info['extension_description'] = extension_description(file_info['extension'])
        file_info['extension_usage'] = extension_usage(file_info['extension'])
        file_info['move_command'] = 'file_info.move("{}", <destination path>)'.format(correct_path)
        file_info['delete_command'] = 'file_info.delete("{}")'.format(correct_path)
        file_info['open_command'] = 'file_info.open("{}")'.format(correct_path)
    else:
       file_info['information'] = 'An error occured while searching for your file.' 
    return file_info


# Testing

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    file = input('File: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    results = info(file)
    for info in results:
        print(info + ': ' + str(results[info]))
    print('')
    input('Press enter to quit... ')