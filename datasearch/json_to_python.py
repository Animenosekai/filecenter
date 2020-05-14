from time import sleep
json_dict = {'.doc': 'Microsoft Word Document', '.docx': 'Microsoft Word Open XML Document', '.log': 'Log File', '.msg': 'Outlook Mail Message', '.odt': 'OpenDocument Text Document', '.pages': 'Pages Document', '.rtf': 'Rich Text Format File', '.tex': 'LaTeX Source Document', '.txt': 'Plain Text File', '.wpd': 'WordPerfect Document', '.wps': 'Microsoft Works Word Processor Document', '.csv': 'Comma Separated Values File', '.dat': 'Data File', '.ged': 'GEDCOM Genealogy Data File', '.key': 'Keynote Presentation', '.keychain': 'Mac OS X Keychain File', '.pps': 'PowerPoint Slide Show', '.ppt': 'PowerPoint Presentation', '.pptx': 'PowerPoint Open XML Presentation', '.sdf': 'Standard Data File', '.tar': 'Consolidated Unix File Archive', '.tax2016': 'TurboTax 2016 Tax Return', '.tax2019': 'TurboTax 2019 Tax Return', '.vcf': 'vCard File', '.xml': 'XML File', '.aif': 'Audio Interchange File Format', '.iff': 'Interchange File Format', '.m3u': 'Media Playlist File', '.m4a': 'MPEG-4 Audio File', '.mid': 'MIDI File', '.mp3': 'MP3 Audio File', '.mpa': 'MPEG-2 Audio File', '.wav': 'WAVE Audio File', '.wma': 'Windows Media Audio File', '.3g2': '3GPP2 Multimedia File', '.3gp': '3GPP Multimedia File', '.asf': 'Advanced Systems Format File', '.avi': 'Audio Video Interleave File', '.flv': 'Flash Video File', '.m4v': 'iTunes Video File', '.mov': 'Apple QuickTime Movie', '.mp4': 'MPEG-4 Video File', '.mpg': 'MPEG Video File', '.rm': 'RealMedia File', '.srt': 'SubRip Subtitle File', '.swf': 'Shockwave Flash Movie', '.vob': 'DVD Video Object File', '.wmv': 'Windows Media Video File', '.3dm': 'Rhino 3D Model', '.3ds': '3D Studio Scene', '.max': '3ds Max Scene File', '.obj': 'Wavefront 3D Object File', '.bmp': 'Bitmap Image File', '.dds': 'DirectDraw Surface', '.gif': 'Graphical Interchange Format File', '.heic': 'High Efficiency Image Format', '.jpg': 'JPEG Image', '.png': 'Portable Network Graphic', '.psd': 'Adobe Photoshop Document', '.pspimage': 'PaintShop Pro Image', '.tga': 'Targa Graphic', '.thm': 'Thumbnail Image File', '.tif': 'Tagged Image File', '.tiff': 'Tagged Image File Format', '.yuv': 'YUV Encoded Image File', '.ai': 'Adobe Illustrator File', '.eps': 'Encapsulated PostScript File', '.svg': 'Scalable Vector Graphics File', '.indd': 'Adobe InDesign Document', '.pct': 'Picture File', '.pdf': 'Portable Document Format File', '.xlr': 'Works Spreadsheet', '.xls': 'Excel Spreadsheet', '.xlsx': 'Microsoft Excel Open XML Spreadsheet', '.accdb': 'Access 2007 Database File', '.db': 'Database File', '.dbf': 'Database File', '.mdb': 'Microsoft Access Database', '.pdb': 'Program Database', '.sql': 'Structured Query Language Data File', '.apk': 'Android Package File', '.app': 'macOS Application', '.bat': 'DOS Batch File', '.cgi': 'Common Gateway Interface Script', '.com': 'DOS Command File', '.exe': 'Windows Executable File', '.gadget': 'Windows Gadget', '.jar': 'Java Archive File', '.wsf': 'Windows Script File', '.b': 'Grand Theft Auto 3 Saved Game File', '.dem': 'Video Game Demo File', '.gam': 'Saved Game File', '.nes': 'Nintendo (NES) ROM File', '.rom': 'N64 Game ROM File', '.sav': 'Saved Game', '.dwg': 'AutoCAD Drawing Database File', '.dxf': 'Drawing Exchange Format File', '.gpx': 'GPS Exchange File', '.kml': 'Keyhole Markup Language File', '.kmz': 'Google Earth Placemark File', '.asp': 'Active Server Page', '.aspx': 'Active Server Page Extended File', '.cer': 'Internet Security Certificate', '.cfm': 'ColdFusion Markup File', '.csr': 'Certificate Signing Request File', '.css': 'Cascading Style Sheet', '.dcr': 'Shockwave Media File', '.htm': 'Hypertext Markup Language File', '.html': 'Hypertext Markup Language File', '.js': 'JavaScript File', '.jsp': 'Java Server Page', '.php': 'PHP Source Code File', '.rss': 'Rich Site Summary', '.xhtml': 'Extensible Hypertext Markup Language File', '.crx': 'Chrome Extension', '.plugin': 'Mac OS X Plugin', '.fnt': 'Windows Font File', '.fon': 'Generic Font File', '.otf': 'OpenType Font', '.ttf': 'TrueType Font', '.cab': 'Windows Cabinet File', '.cpl': 'Windows Control Panel Item', '.cur': 'Windows Cursor', '.deskthemepack': 'Windows 8 Desktop Theme Pack File', '.dll': 'Dynamic Link Library', '.dmp': 'Windows Memory Dump', '.drv': 'Device Driver', '.icns': 'macOS Icon Resource File', '.ico': 'Icon File', '.lnk': 'Windows Shortcut', '.sys': 'Windows System File', '.cfg': 'Configuration File', '.ini': 'Windows Initialization File', '.prf': 'Outlook Profile File', '.hqx': 'BinHex 4.0 Encoded File', '.mim': 'Multi-Purpose Internet Mail Message File', '.uue': 'Uuencoded File', '.7z': '7-Zip Compressed File', '.cbr': 'Comic Book RAR Archive', '.deb': 'Debian Software Package', '.gz': 'Gnu Zipped Archive', '.pkg': 'Mac OS X Installer Package', '.rar': 'WinRAR Compressed Archive', '.rpm': 'Red Hat Package Manager File', '.sitx': 'StuffIt X Archive', '.tar.gz': 'Compressed Tarball File', '.zip': 'Zipped File', '.zipx': 'Extended Zip File', '.bin': 'Binary Disc Image', '.cue': 'Cue Sheet File', '.dmg': 'Apple Disk Image', '.iso': 'Disc Image File', '.mdf': 'Media Disc Image File', '.toast': 'Toast Disc Image', '.vcd': 'Virtual CD', '.c': 'C/C++ Source Code File', '.class': 'Java Class File', '.cpp': 'C++ Source Code File', '.cs': 'C# Source Code File', '.dtd': 'Document Type Definition File', '.fla': 'Adobe Animate Animation', '.h': 'C/C++/Objective-C Header File', '.java': 'Java Source Code File', '.lua': 'Lua Source File', '.m': 'Objective-C Implementation File', '.pl': 'Perl Script', '.py': 'Python Script', '.sh': 'Bash Shell Script', '.sln': 'Visual Studio Solution File', '.swift': 'Swift Source Code File', '.bak': 'Backup File', '.tmp': 'Temporary File', '.crdownload': 'Chrome Partially Downloaded File', '.ics': 'Calendar File', '.msi': 'Windows Installer Package', '.part': 'Partially Downloaded File', '.torrent': 'BitTorrent File'}
final_dict = {}
final_list = []
for line in json_dict:
  final_list.append(line)
print(final_list)
sleep(3)