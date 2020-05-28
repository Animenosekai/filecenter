# FileInfo
 
 ### **A quick gif sending discord bot written in python**

## Installation
You can install this library with **`PIP`**, the Python Package Manager

Simply type `pip install fileinfo` in your terminal/command-line prompt.

> This library has no external/third-party dependencies.

## What is FileInfo?
FileInfo is a simple library to make developers life easier when it comes to file management and information.
> You just have to import it to your project! `import fileinfo`

### Usage

##### File Actions 
- `open(*filepath*)`: Opens the given file in its default software

Arguments:
    *file*: the path to the file.

> Returns 0 if success and 1 if failed

- `move(*filepath*, *new_path*)`: Moves the given file to the provided new path.

Arguments:
    *origin*: the path to the file.
    *destination*: the new path
    
> Returns 0 if success and 1 if failed

- `delete(*filepath*)`: Deletes the given file.

Arguments:
    *file*: the path of the file

> Returns 0 if success, 1 if failed at getting the file, 2 if failed at moving a file and 3 if failed at moving a directory. 

- `makedir(*path*)`: Makes a directory at the given path.

Arguments:
    *path_of_new_dir*: the path where the directory needs to be created

> Returns the path of the directory if success, the string 'Error while making the new folder' if failed.

- `files_in_dir(*path_to_folder*)`: Gives a list of files in a given directory.

Arguments:
    *path_of_dir*: the path of the directory where the files are located.

> Returns the a list of files basename.

- `os_name()`: Returns the operating system's name.

- `get_correct_path(*path*)`: Change a non-python usable path into a python-usable one.

Arguments:
    *path*: the path to check.

> Returns the path usable in python.

- `get_readeable_size(*bytes*, *suffix*)`: To scale bytes to its proper format.

Arguments:
    *bytes*: the number of bytes to convert.
    *suffix*: if you want to change the suffix of the given size.

> Returns the correctly scales size.

- `get_correct_path(*path*)`: Change a non-python usable path into a python-usable one.

Arguments:
    *path*: the path to check.

> Returns the path usable in python.



## Development
FileInfo is in constant development and fixes are made on a regular basis (but I also try to add some new features ehe)

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

`LICENSE` is a text file with FileInfo's license

#### Dependencies
The FileInfo Library has no third-party dependencies needed.

### Sources
Datafile | Source
------------ | -------------
Firebase | [**Firebase Admin SDK Documentations**](https://firebase.google.com/docs/database/admin/start)
Heroku | [**Heroku Documentations**](https://devcenter.heroku.com/categories/reference)
discord.py | [**discord.py Documentations**](https://discordpy.readthedocs.io/en/latest/index.html#)
Discord (API) | [**Discord Developper Portal**](https://discord.com/developers/docs/intro)
Giphy | [**Giphy API Documentations**](https://developers.giphy.com/docs/api#quick-start-guide)
Tenor | [**Tenor GIF API Documentations**](https://tenor.com/gifapi/documentation)


## Copyrights and Legals

**Giphy** is a brand which belongs to Giphy, Inc.

**Tenor GIF** is a brand which belongs to Tenor, Inc.

**Firebase** is a brand which belongs to Google, Inc.

**Heroku** is a brand which belongs to Salesforce, Inc.

**Netlify** is a brand which belongs to Netlify Co.

**GitHub** is a brand which belongs to GitHub, Inc. (Microsoft)

**Discord** is a brand which belongs to Discord, Inc.

**Python** belongs to the Python Software Foundation

**Rebrand.ly** is a service/brand which belongs to Radiate Capital Limited


> ©Anime no Sekai - 2020 ✨
