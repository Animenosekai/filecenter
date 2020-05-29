# filecenter
 
 ### **An easy file management and information center for Python**

[![PyPI version](https://badge.fury.io/py/filecenter.svg)](https://badge.fury.io/py/filecenter)
 
## Table of Content
- [Installation](#installation)  
- [What is File Center?](#whatis)
- [Usage](#usage)
   - [File Actions](#fileactions)  
   - [Extension Info](#extension)
   - [File Base Info](#filebase)
   - [File Info](#fileinfo)
   - [Advanced](#advanced)
- [List of file types in the database](#listoftypes)
- [Development](#development) 
- [Legals](#legals)
 
 
<a name="installation"/>

## Installation
You can install this library with **`PIP`**, the Python Package Manager

Simply type `pip install filecenter` in your terminal/command-line prompt.

> This library has no external/third-party dependencies.

<a name="whatis"/>

## What is File Center?
File Center is a simple library to make developers life easier when it comes to file management and information.
> You just have to import it to your project! `import filecenter`


<a name="usage"/>

## Usage

<a name="fileactions"/>

### File Actions 
- **`open(filepath)`**

**Opens the given file in its default software**

Arguments:

    file: the path to the file.

> Returns 0 if success and 1 if failed

---
- **`move(filepath, new_path)`**

**Moves the given file to the provided new path.**

Arguments:

    origin: the path to the file.
    destination: the new path
    
> Returns 0 if success and 1 if failed

---
- **`delete(filepath)`**

**Deletes the given file.**

Arguments:

    file: the path of the file

> Returns 0 if success, 1 if failed at getting the file, 2 if failed at moving a file and 3 if failed at moving a directory. 

---
- **`makedir(path)`**

**Makes a directory at the given path.**

Arguments:

    path_of_new_dir: the path where the directory needs to be created

> Returns the path of the directory if success, the string 'Error while making the new folder' if failed.

---

<a name="extension"/>

### Extension Information

- **`popularity(extension)`**

**Gives the popularity of a given file extension.**

Arguments:

    file_extension: the extension you want to check.

> Returns 'Very popular', 'Quite popular' or 'Not very popular'.

---

- **`type_from_extension(extension)`**

**Gives the type of file using the given extension.**

Arguments:

    extension: the extension you want to check.

> Returns a string with the type (see below for the full list of supported types).
---

- **`extension_to_human_readeable(extension)`**

**Gives the human readeable version of a given extension.**

Arguments:

    extension: the file extension you want to get the human readeable version from.

> Returns a string of the human readeable version.

---

- **`extension_info(extension)`**

**Gives a dictionnary with multiple information of a given extension.**

Arguments:

    extension: the file extension you want to get information from.

> Returns a python dictionary.

---

- **`extension_description(extension)`**

**Gives the description of a given file extension.**

Arguments:

    extension: the file extension you want to get the description from.

> Returns a string with the extension's description.

---

- **`extension_usage(extension)`**

**Gives the softwares using a given file extension.**

Arguments:

    extension: the file extension you want to get the using softwares from.

> Returns a list of softwares name.

---

<a name="filebase"/>

### File Base Information

- **`name_from_base(base)`**

**Returns the name of a file from the given file base.**

A file base is the file name and its extension (i.e. something.png)

Arguments:

    base: the file base you want to get the name from.

> Returns a string with the file name.

---

- **`extension_from_base(base)`**

**Returns the extension of a file from the given file base.**

Arguments:

    base: the file base you want to get the extension from.

> Returns a string with the file extension. (including the dot)

---

<a name="fileinfo"/>

### File Information

#### Boolean Values

- **`exists(path)`**

**Checks if a fiven file or directory exists.**

Arguments:

    file: the file path to check.

> Returns a boolean value.


---

- **`isdir(path)`**

**Checks is a given path is a directory.**

Arguments:

    path: the path to check.

> Returns a boolean value.


---

- **`isfile(path)`**

**Checks if a given path is a file.**

Arguments:

    path: the path to check.

> Returns a boolean value.


---

- **`issymboliclink(path)`**

**Checks if a given path is a symbolic link (an alias).**

Arguments:

    path: the path to check.

> Returns a boolean value.


---

- **`ismountpoint(path)`**

**Checks if the given path is a disk mountpoint.**

Arguments:

    path: the path to check.

> Returns a boolean value.


---

- **`iscommon(extension)`**

**Checks if a given file extension is commonly used.**

Arguments:

    file_extension: the extension you want to check.

> Returns a boolean value.

##### Informations

- **`permissions(file)`**

**Returns the permissions for a given file.**

Arguments:

    file: the path to the file you want to get the permissions from.

> Returns a dictionnary with the permissions for the owner, the group and others of the given file.
> Returns the `{'information': 'Unable to get permissions'}` dictionnary the file isn't found.

---

- **`mimetype(file)`**

**Returns the MIME type for a given file.**

Arguments:

    file: the path of the file you want to get the MIME type from.

> Returns a string with the MIME type or 'An error occured while getting the file' if failed to retrieve it.

---

- **`base(file)`**

**Returns the file base from a given path.**

Arguments:

    file: the path of the file you want to get the base from.

> Returns a string with the file base.

---

- **`path(file)`**

**Returns the absolute path of a file path.**

Arguments:

    file: the path of the file you want to get the absolute path from.

> Returns a string with the path.

---

- **`name(file)`**

**Gives the name of a file based on its path.**

Arguments:

    file: the path of the file you want to get the name from.

> Returns a string with the name of the file.


---

- **`extension(file)`**

**Returns the extension of a file based on its path.**

Arguments:

    file: the path of the file you want to get the extension from.

> Returns a string with the file extension (including the dot).


---

- **`size(file)`**

**Returns the size of a file.**

Arguments:

    file: the path to the file you want to get the size from.

> Returns a string with the file size (in a correctly scaled, human readeable format).


---

- **`get_real_path(path)`**

**Checks for the real path of a file/directory (without symbolic links).**

Arguments:

    path: the path to check.

> Returns a boolean value.

---
- **`files_in_dir(path_to_folder)`**

**Gives a list of files in a given directory.**

Arguments:

    path_of_dir: the path of the directory where the files are located.

> Returns the a list of files basename.

---
##### Time

- **`last_access(file)`**

**Gives the last access time.**

Arguments:

    file: the path to the file you want to get the last access time from.

> Returns a datetime object.

---

- **`last_modification(file)`**

**Gives the last modification time.**

Arguments:

    file: the path to the file you want to get the last modification time from.

> Returns a datetime object.

---

- **`last_metadata_change(file)`**

**Gives the last metadata change time.**

Arguments:

    file: the path to the file you want to get the last modification time from.

> Returns a datetime object.

---

- **`type(file)`**

**Returns the type of file.**

Arguments:

    file: the path of the file you want to know the type from.

> Returns a string with the type.

---
### Every Information at once

- **`info(file)`**

**Gives every info you could get from filecenter on a given file.**

Arguments:

    file: the path to the file you want to get the infos from.

> Returns a python dictionnary containing everything.

---

### Other

- **`os_name()`**

**Returns the operating system's name.**

---
- **`get_readeable_size(bytes, suffix)`**

**To scale bytes to its proper format.**

Arguments:

    bytes: the number of bytes to convert.
    suffix: if you want to change the suffix of the given size.

> Returns the correctly scales size.

---

- **`get_correct_path(path)`**

**Change a non-python usable path into a python-usable one.**

Arguments:

    path: the path to check.

> Returns the path usable in python.

---

<a name="advanced"/>

### Advanced

- **`osstat_mode(file)`**

**Returns the mode part of os.stat() for a given file.**

Mostly used to get the permissions of a file from (even if you can use permissions() or permissions_in_oct() to do so)

Arguments:

    file: the path to the file you want to get the mode part from.

> Returns a os.stat() class or 0 if failed.


---

- **`permissions_in_oct(file)`**

**Returns the octal version of the permissions for a given file.**

Arguments:

    file: the path to the file you want to get the permissions from.

> Returns an octal string or the string 'Unable to get the file permissions' if the file isn't found.

---

- **`size_in_bytes(file)`**

**Returns the size of a file in bytes.**

Arguments:

    file: the path to the file you want to get the size from.

> Returns an integer with the number of bytes.


---

- **`file_stat(file)`**

**Returns the os.stat() of a given file.**

Arguments:

    file: the path to the file you want to get the stats from.

> Returns a os.stat() class object.


---

- **`last_access_raw(file)`**

**Gives the last access time as a timestamp.**

Arguments:

    file: the path to the file you want to get the last access timestamp from.

> Returns an integer with the timestamp of the last access time.

---

- **`last_modification_raw(file)`**

**Gives the last modification time as a timestamp.**

Arguments:

    file: the path to the file you want to get the last modification timestamp from.

> Returns an integer with the timestamp of the last modification time.

---

- **`last_metadata_change_raw(file)`**

**Gives the last metadata change time as a timestamp.**

Arguments:

    file: the path to the file you want to get the last metadata change time from.

> Returns an integer with the timestamp of the last metadata change time.

<a name="listoftypes"/>

## List of types

- Archive
- Audio
- Backup
- eBook
- Database File
- Developer
- Disk Image
- Encoded File
- Application/Executable
- Font
- 3D Image
- Plugin
- Preset/Settings
- Image
- Raw Image
- ROM/Game File
- Spreadsheet
- System file
- Text File/Document
- Vector Image
- Video
- Web Document
- Folder
- Document

> The type is defined as "unknown" if not in the database

<a name="development"/>

## Development
File Center is in constant development and fixes are made on a regular basis (but I also try to add some new features ehe)

#### If you have any issues, questions, development problem: feel free to ask in the issues section.

If you want to help us and join me here is a quick guide.

### Files
`__init.py__` is the main module

`data_` All files with a `data_` suffix are data files (list of extensions for example).

`data_common.py` is a list of file extensions that are common.

`data_ext_to_human_readable.py` is a list of file extensions and its human readeable format.

`data_extension_desc.py` is a list of file extensions and their description, using softwares.

`data_type.py` is a list of file extensions and their general type (file types, i.e. Images, Web Development).

`README.md` is the text file you're currently reading, with all the documentations and explanations.

`LICENSE` is a text file with File Center's license

#### Dependencies
The File Center Library has no third-party dependencies needed.

### Sources
Datafile | Source
------------ | -------------
data_common | [**FileInfo**](https://fileinfo.com/browse/),[**Wikipedia**](https://en.wikipedia.org/wiki/Main_Page), [**ComputerHope**](https://www.computerhope.com/)
data_ext_to_human_readeable | [**Webopedia**](https://www.webopedia.com/quick_ref/fileextensionsfull.asp)
data_extension_desc.py | [**Wikipedia**](https://en.wikipedia.org/wiki/List_of_filename_extensions)
data_type | [**FileInfo**](https://fileinfo.com/browse/)

<a name="legals"/>

## Copyrights and Legals

Every data here has been pulled from websites (and myself too lol) by hand (yea it took quite some time)

**If you think that there is any kind of copyright infrigements, feel free to ask me to remove it and I will try to do so as soon as possible**

**Wikipedia** is hosted by the Wikimedia Foundation

**Computer Hope** belongs to [Nathan Emberton](https://www.computerhope.com/people/nathan_emberton.htm)

**Webopedia** is a brand which belongs to TechnologyAdvice, LLC

**FileInfo** belongs to Sharpened Productions

**GitHub** is a brand which belongs to GitHub, Inc. (Microsoft)

**Python** belongs to the Python Software Foundation


I am in now way affiliated to FileInfo.com

> ©Anime no Sekai - 2020 ✨
