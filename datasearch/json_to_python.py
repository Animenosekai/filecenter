from time import sleep
json_dict = [
 {
   "FIELD1": ".KRAB",
   "FIELD2": "GandCrab V4 Ransomware Encrypted File",
   "FIELD3": 125
 },
 {
   "FIELD1": ".ECD",
   "FIELD2": "Encrypted Cryptee Document",
   "FIELD3": 127
 },
 {
   "FIELD1": ".FILEBOLT",
   "FIELD2": "Filebolt Encrypted File",
   "FIELD3": 129
 },
 {
   "FIELD1": ".LASTLOGIN",
   "FIELD2": "Minecraft User Credential File",
   "FIELD3": 140
 },
 {
   "FIELD1": ".RZK",
   "FIELD2": "Red Zion Key File",
   "FIELD3": 150
 },
 {
   "FIELD1": ".GDCB",
   "FIELD2": "GandCrab Ransomware Encrypted File",
   "FIELD3": 150
 },
 {
   "FIELD1": ".GXK",
   "FIELD2": "Galaxkey Secured File",
   "FIELD3": 150
 },
 {
   "FIELD1": ".PXF",
   "FIELD2": "Pendix Firmware File",
   "FIELD3": 162
 },
 {
   "FIELD1": ".PACK",
   "FIELD2": "Pack200 Packed Jar File",
   "FIELD3": 164
 },
 {
   "FIELD1": ".VLT",
   "FIELD2": "WinVault File Archive",
   "FIELD3": 167
 },
 {
   "FIELD1": ".PWV",
   "FIELD2": "Password Vault Archive",
   "FIELD3": 167
 },
 {
   "FIELD1": ".MEO",
   "FIELD2": "MEO Encrypted Archive",
   "FIELD3": 167
 },
 {
   "FIELD1": ".KDE",
   "FIELD2": "KryptoStorage Container File",
   "FIELD3": 167
 },
 {
   "FIELD1": ".JMC",
   "FIELD2": "JM-Crypt Encrypted File",
   "FIELD3": 167
 },
 {
   "FIELD1": ".BHX",
   "FIELD2": "BinHex Encoded File",
   "FIELD3": 167
 },
 {
   "FIELD1": ".SCB",
   "FIELD2": "Euro Truck Simulator 2 Product Key File",
   "FIELD3": 168
 },
 {
   "FIELD1": ".SUF",
   "FIELD2": "Ccrypt Encrypted File",
   "FIELD3": 175
 },
 {
   "FIELD1": ".SRF",
   "FIELD2": "Samsung Smart TV Recording File",
   "FIELD3": 180
 },
 {
   "FIELD1": ".MNC",
   "FIELD2": "AutoCAD Compiled Menu File",
   "FIELD3": 180
 },
 {
   "FIELD1": ".ATSOFTS",
   "FIELD2": "LetEncrypt Encrypted File",
   "FIELD3": 187
 },
 {
   "FIELD1": ".AXX",
   "FIELD2": "AxCrypt Encrypted File",
   "FIELD3": 190
 },
 {
   "FIELD1": ".PLP",
   "FIELD2": "Photo Locker Picture",
   "FIELD3": 192
 },
 {
   "FIELD1": ".BIN",
   "FIELD2": "Macbinary Encoded File",
   "FIELD3": 193
 },
 {
   "FIELD1": ".ASC",
   "FIELD2": "PGP ASCII Armored File",
   "FIELD3": 197
 },
 {
   "FIELD1": ".WNRY",
   "FIELD2": "WannaCry Virus Encrypted File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".VIIVO",
   "FIELD2": "Viivo Encrypted File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".SDTID",
   "FIELD2": "SecurID Soft Token File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".STXT",
   "FIELD2": "Sealed Text File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".SJPG",
   "FIELD2": "Sealed JPG File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".DCO",
   "FIELD2": "Safetica Free Encrypted Virtual Disk Archive",
   "FIELD3": 200
 },
 {
   "FIELD1": ".WRYPT",
   "FIELD2": "Panwrypter Depleted Storage Volume File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".SEF",
   "FIELD2": "Encryptafile Signature File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".CNG",
   "FIELD2": "CryptoNG Encrypted Archive",
   "FIELD3": 200
 },
 {
   "FIELD1": ".CERBER2",
   "FIELD2": "Cerber2 Ransomware Encrypted File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".BLOWER",
   "FIELD2": "Blower Ransomware Encrypted File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".MJD",
   "FIELD2": "Adobe Acrobat MIME Encoded Job Definition File",
   "FIELD3": 200
 },
 {
   "FIELD1": ".TAR.MD5",
   "FIELD2": "Android System File",
   "FIELD3": 201
 },
 {
   "FIELD1": ".ACID",
   "FIELD2": "ACID Encrypted File",
   "FIELD3": 208
 },
 {
   "FIELD1": ".CPIO",
   "FIELD2": "Unix CPIO Archive",
   "FIELD3": 217
 },
 {
   "FIELD1": ".JCEKS",
   "FIELD2": "JCEKS Keystore File",
   "FIELD3": 217
 },
 {
   "FIELD1": ".SAFE",
   "FIELD2": "SIGLock Encrypted File",
   "FIELD3": 218
 },
 {
   "FIELD1": ".ODIN",
   "FIELD2": "Locky Ransomware Encrypted File",
   "FIELD3": 220
 },
 {
   "FIELD1": ".BIT",
   "FIELD2": "FinalCrypt Encrypted Data File",
   "FIELD3": 220
 },
 {
   "FIELD1": ".BFA",
   "FIELD2": "Blowfish Encrypted File",
   "FIELD3": 220
 },
 {
   "FIELD1": ".WOLF",
   "FIELD2": "Wolf RPG Editor Game Data Archive",
   "FIELD3": 225
 },
 {
   "FIELD1": ".UUE",
   "FIELD2": "Uuencoded File",
   "FIELD3": 229
 },
 {
   "FIELD1": ".NC",
   "FIELD2": "mcrypt Encrypted File",
   "FIELD3": 230
 },
 {
   "FIELD1": ".VP",
   "FIELD2": "Verilog Encrypted Source Code File",
   "FIELD3": 233
 },
 {
   "FIELD1": ".UU",
   "FIELD2": "Uuencoded File",
   "FIELD3": 233
 },
 {
   "FIELD1": ".BSK",
   "FIELD2": "Nero SecurDisc Private Key File",
   "FIELD3": 233
 },
 {
   "FIELD1": ".FILM",
   "FIELD2": "Filmkey Player Media File",
   "FIELD3": 233
 },
 {
   "FIELD1": ".DDOC",
   "FIELD2": "DigiDoc Signature File",
   "FIELD3": 233
 },
 {
   "FIELD1": ".CRYPTRA",
   "FIELD2": "Cryptra Encrypted File",
   "FIELD3": 233
 },
 {
   "FIELD1": ".BPW",
   "FIELD2": "Bitser Password File",
   "FIELD3": 233
 },
 {
   "FIELD1": ".ENC",
   "FIELD2": "Encoded File",
   "FIELD3": 235
 },
 {
   "FIELD1": ".RSDF",
   "FIELD2": "RapidShare Download File",
   "FIELD3": 236
 },
 {
   "FIELD1": ".SXLS",
   "FIELD2": "Sealed Excel Spreadsheet",
   "FIELD3": 237
 },
 {
   "FIELD1": ".CPT",
   "FIELD2": "Ccrypt Encrypted Archive",
   "FIELD3": 244
 },
 {
   "FIELD1": ".HQX",
   "FIELD2": "BinHex 4.0 Encoded File",
   "FIELD3": 246
 },
 {
   "FIELD1": ".XTBL",
   "FIELD2": "XTBL Ransomware Encrypted File",
   "FIELD3": 250
 },
 {
   "FIELD1": ".SCB",
   "FIELD2": "Scrambls Encrypted File",
   "FIELD3": 250
 },
 {
   "FIELD1": ".PDEX",
   "FIELD2": "Orient Computer Encrypted Data File",
   "FIELD3": 250
 },
 {
   "FIELD1": ".NXL",
   "FIELD2": "Nextlabs Encrypted Data File",
   "FIELD3": 250
 },
 {
   "FIELD1": ".BPK",
   "FIELD2": "Nero SecurDisc Public Key File",
   "FIELD3": 250
 },
 {
   "FIELD1": ".ENX",
   "FIELD2": "Max PC Safe Encrypted File",
   "FIELD3": 250
 },
 {
   "FIELD1": ".B2A",
   "FIELD2": "Btoa Encoded File",
   "FIELD3": 250
 },
 {
   "FIELD1": ".CRYPT",
   "FIELD2": "WhatsApp Encrypted Database File",
   "FIELD3": 253
 },
 {
   "FIELD1": ".VDATA",
   "FIELD2": "Vaulty Vault File",
   "FIELD3": 254
 },
 {
   "FIELD1": ".PDC",
   "FIELD2": "Lizard Safeguard Secure PDF File",
   "FIELD3": 254
 },
 {
   "FIELD1": ".SDOC",
   "FIELD2": "Sealed Word Document",
   "FIELD3": 255
 },
 {
   "FIELD1": ".WNCRY",
   "FIELD2": "Wana Decrypt0r 2.0 Encrypted File",
   "FIELD3": 256
 },
 {
   "FIELD1": ".XMDX",
   "FIELD2": "ExamSoft Answer File",
   "FIELD3": 256
 },
 {
   "FIELD1": ".CDOC",
   "FIELD2": "Encrypted DigiDoc File",
   "FIELD3": 257
 },
 {
   "FIELD1": ".ESLOCK",
   "FIELD2": "ES File Explorer File Manager Encrypted File",
   "FIELD3": 258
 },
 {
   "FIELD1": ".ZZZZZ",
   "FIELD2": "Ransomware Encrypted File",
   "FIELD3": 259
 },
 {
   "FIELD1": ".SFI",
   "FIELD2": "SafeFolder Encrypted File",
   "FIELD3": 267
 },
 {
   "FIELD1": ".LOCKED",
   "FIELD2": "Ransomware Encrypted File",
   "FIELD3": 267
 },
 {
   "FIELD1": ".CGP",
   "FIELD2": "PixelCryptor Encrypted File",
   "FIELD3": 267
 },
 {
   "FIELD1": ".YKCOL",
   "FIELD2": "Locky Ransomware Encrypted File",
   "FIELD3": 267
 },
 {
   "FIELD1": ".ADOBE",
   "FIELD2": "Dharma Ransomware Encrypted File",
   "FIELD3": 267
 },
 {
   "FIELD1": ".AZS",
   "FIELD2": "AirZip FileSECURE File",
   "FIELD3": 267
 },
 {
   "FIELD1": ".XXE",
   "FIELD2": "XXEncoded File",
   "FIELD3": 268
 },
 {
   "FIELD1": ".AES",
   "FIELD2": "AES Crypt Encrypted File",
   "FIELD3": 271
 },
 {
   "FIELD1": ".ZPS",
   "FIELD2": "Zebra Portable Safe File",
   "FIELD3": 275
 },
 {
   "FIELD1": ".DC4",
   "FIELD2": "ViaThinkSoft (De)Coder 4 File",
   "FIELD3": 275
 },
 {
   "FIELD1": ".SPDF",
   "FIELD2": "Sealed PDF File",
   "FIELD3": 275
 },
 {
   "FIELD1": ".DIME",
   "FIELD2": "Direct Internet Message Encapsulation File",
   "FIELD3": 275
 },
 {
   "FIELD1": ".DCF",
   "FIELD2": "Safetica Free Encrypted Archive",
   "FIELD3": 280
 },
 {
   "FIELD1": ".EMC",
   "FIELD2": "Striata Reader Encrypted Document",
   "FIELD3": 283
 },
 {
   "FIELD1": ".MIM",
   "FIELD2": "Multi-Purpose Internet Mail Message File",
   "FIELD3": 284
 },
 {
   "FIELD1": ".GFE",
   "FIELD2": "Glarysoft Encrypted File",
   "FIELD3": 286
 },
 {
   "FIELD1": ".HID2",
   "FIELD2": "KeepSafe File",
   "FIELD3": 287
 },
 {
   "FIELD1": ".MIME",
   "FIELD2": "Multi-Purpose Internet Mail Extension",
   "FIELD3": 289
 },
 {
   "FIELD1": ".KEYSTORE",
   "FIELD2": "Java Keystore File",
   "FIELD3": 292
 },
 {
   "FIELD1": ".AFP",
   "FIELD2": "FileProtector Encrypted File",
   "FIELD3": 292
 },
 {
   "FIELD1": ".DM",
   "FIELD2": "LG Encrypted Gallery File",
   "FIELD3": 293
 },
 {
   "FIELD1": ".DLC",
   "FIELD2": "Download Link Container File",
   "FIELD3": 294
 },
 {
   "FIELD1": ".HEX",
   "FIELD2": "BinHex Encoded File",
   "FIELD3": 294
 },
 {
   "FIELD1": ".YNC",
   "FIELD2": "yEnc Encoded File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".WALLET",
   "FIELD2": "Wallet Ransomware",
   "FIELD3": 300
 },
 {
   "FIELD1": ".SDO",
   "FIELD2": "Signed Document",
   "FIELD3": 300
 },
 {
   "FIELD1": ".SIA",
   "FIELD2": "Sia Metadata File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".SHY",
   "FIELD2": "ShyFile Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".SPD",
   "FIELD2": "Sealed Acrobat Document",
   "FIELD3": 300
 },
 {
   "FIELD1": ".PPDF",
   "FIELD2": "Rights Management Protected File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".REPP",
   "FIELD2": "Repp Ransomware Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".ESF",
   "FIELD2": "Password Manager Container File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".PSW6",
   "FIELD2": "Password Depot 6 File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".NBES",
   "FIELD2": "Nbes Ransomware Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".LCN",
   "FIELD2": "License File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".KODE",
   "FIELD2": "KodeFile Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".HID",
   "FIELD2": "KeepSafe File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".JMCE",
   "FIELD2": "JM-Crypt Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".JMCX",
   "FIELD2": "JM-Crypt Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".JCRYPT",
   "FIELD2": "JCRYPT File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".JAC",
   "FIELD2": "JaStaCry Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".WLU",
   "FIELD2": "Jaff Ransomware Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".FPENC",
   "FIELD2": "FileProtect Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".EFU",
   "FIELD2": "Encryptafile Public Key File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".ENX",
   "FIELD2": "eDataSecurity Management Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".SIGNATURE",
   "FIELD2": "e-Filing Digital Signature File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".DIM",
   "FIELD2": "DIME File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".BIP",
   "FIELD2": "Dharma Ransomware Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".CERBER",
   "FIELD2": "Cerber Ransomware Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".CEF",
   "FIELD2": "CenturionMail Encrypted Package",
   "FIELD3": 300
 },
 {
   "FIELD1": ".AURORA",
   "FIELD2": "Aurora Ransomware Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".HTPASSWD",
   "FIELD2": "Apache HTACCESS File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".ADAME",
   "FIELD2": "Adame Ransomware Encrypted File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".MSE",
   "FIELD2": "3ds Max Encrypted MAXScript File",
   "FIELD3": 300
 },
 {
   "FIELD1": ".JKS",
   "FIELD2": "Java Keystore File",
   "FIELD3": 304
 },
 {
   "FIELD1": ".PFILE",
   "FIELD2": "Rights Management Protected File",
   "FIELD3": 307
 },
 {
   "FIELD1": ".LOCKY",
   "FIELD2": "Locky Ransomware Encrypted File",
   "FIELD3": 313
 },
 {
   "FIELD1": ".KSD",
   "FIELD2": "KeepSafe File",
   "FIELD3": 314
 },
 {
   "FIELD1": ".NULL",
   "FIELD2": "Null Ransomware Encrypted File",
   "FIELD3": 317
 },
 {
   "FIELD1": ".SWITCH",
   "FIELD2": "Switch Package",
   "FIELD3": 319
 },
 {
   "FIELD1": ".CRYPT",
   "FIELD2": "CryptXXX Ransomware Encrypted File",
   "FIELD3": 320
 },
 {
   "FIELD1": ".CRYPTED",
   "FIELD2": "WinOptimizer Encrypted File",
   "FIELD3": 325
 },
 {
   "FIELD1": ".IDEA",
   "FIELD2": "Tresor IDEA Encrypted File",
   "FIELD3": 325
 },
 {
   "FIELD1": ".KLQ",
   "FIELD2": "Kaspersky Quarantine File",
   "FIELD3": 325
 },
 {
   "FIELD1": ".DCD",
   "FIELD2": "DisCryptor Encrypted Database",
   "FIELD3": 325
 },
 {
   "FIELD1": ".SEB",
   "FIELD2": "Safe Exam Browser Configuration File",
   "FIELD3": 327
 },
 {
   "FIELD1": ".SGZ",
   "FIELD2": "SigzaLock Encrypted File",
   "FIELD3": 329
 },
 {
   "FIELD1": ".UUD",
   "FIELD2": "UUDecoded File",
   "FIELD3": 333
 },
 {
   "FIELD1": ".CRYPT1",
   "FIELD2": "UltraCrypter Ransomware Encrypted File",
   "FIELD3": 340
 },
 {
   "FIELD1": ".PKEY",
   "FIELD2": "PowerKey Encrypted File",
   "FIELD3": 340
 },
 {
   "FIELD1": ".XXX",
   "FIELD2": "Extractor Ransomware Encrypted File",
   "FIELD3": 340
 },
 {
   "FIELD1": ".BVD",
   "FIELD2": "Bitdefender Vault File",
   "FIELD3": 344
 },
 {
   "FIELD1": ".SNK",
   "FIELD2": "Strong Name Key File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".MCRP",
   "FIELD2": "MobyExplorer Encrypted File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".JMCK",
   "FIELD2": "JM-Crypt Key File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".RZX",
   "FIELD2": "File Crypt Encrypted File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".EFL",
   "FIELD2": "Encryptafile Encrypted File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".EDOC",
   "FIELD2": "Electronically Certified Document",
   "FIELD3": 350
 },
 {
   "FIELD1": ".COOT",
   "FIELD2": "Coot Ransomware Encrypted File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".CHML",
   "FIELD2": "Chameleon Encrypted Database File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".AEP",
   "FIELD2": "Advanced Encryption Package Encrypted File",
   "FIELD3": 350
 },
 {
   "FIELD1": ".CCF",
   "FIELD2": "CryptLoad Container File",
   "FIELD3": 356
 },
 {
   "FIELD1": ".MME",
   "FIELD2": "Multi-Purpose Internet Mail",
   "FIELD3": 360
 },
 {
   "FIELD1": ".PFO",
   "FIELD2": "Private Folder",
   "FIELD3": 367
 },
 {
   "FIELD1": ".KKK",
   "FIELD2": "KKK Ransomware Encrypted File",
   "FIELD3": 371
 },
 {
   "FIELD1": ".ZEPTO",
   "FIELD2": "Zepto Virus File",
   "FIELD3": 373
 },
 {
   "FIELD1": ".IWA",
   "FIELD2": "iWork Archive File",
   "FIELD3": 397
 },
 {
   "FIELD1": ".UFR",
   "FIELD2": "Upfiring File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".SLE",
   "FIELD2": "Steganos Safe Encrypted Drive",
   "FIELD3": 400
 },
 {
   "FIELD1": ".FSM",
   "FIELD2": "Splitty Master Split File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".SXML",
   "FIELD2": "Sealed XML File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".RAP",
   "FIELD2": "Scarab Ransomware Encrypted File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".RDI",
   "FIELD2": "Rohos Disk Image File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".UEA",
   "FIELD2": "Protector Suite QL Encrypted Archive",
   "FIELD3": 400
 },
 {
   "FIELD1": ".MFS",
   "FIELD2": "MetFS Encrypted File System",
   "FIELD3": 400
 },
 {
   "FIELD1": ".MBA",
   "FIELD2": "Martus Bulletin Archive",
   "FIELD3": 400
 },
 {
   "FIELD1": ".LITAR",
   "FIELD2": "Litar Virus Encrypted File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".KS",
   "FIELD2": "Keystore File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".PXX",
   "FIELD2": "Keyman Developer Encrypted Customization File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".JMCR",
   "FIELD2": "JM-Crypt Encrypted File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".JMCP",
   "FIELD2": "JM-Crypt Encrypted File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".EFR",
   "FIELD2": "Encryptafile Private Key File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".E4A",
   "FIELD2": "Encrypt4all Archive",
   "FIELD3": 400
 },
 {
   "FIELD1": ".EXC",
   "FIELD2": "eDataSecurity Management Self-extracting File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".CLX",
   "FIELD2": "Ceelox SecureMail Secure Message",
   "FIELD3": 400
 },
 {
   "FIELD1": ".CAROTE",
   "FIELD2": "Carote Ransomware Encrypted File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".GZQUAR",
   "FIELD2": "Bitdefender Antivirus Quarantine File",
   "FIELD3": 400
 },
 {
   "FIELD1": ".WLS",
   "FIELD2": "R-Link Update File",
   "FIELD3": 425
 },
 {
   "FIELD1": ".SEF",
   "FIELD2": "Password Manager Container File",
   "FIELD3": 425
 },
 {
   "FIELD1": ".KXX",
   "FIELD2": "Keyman Developer Encrypted Keyboard File",
   "FIELD3": 425
 },
 {
   "FIELD1": ".WCRY",
   "FIELD2": "WannaCry Virus Encrypted File",
   "FIELD3": 433
 },
 {
   "FIELD1": ".SME",
   "FIELD2": "SmartEncryptor Encrypted File",
   "FIELD3": 433
 },
 {
   "FIELD1": ".BTOA",
   "FIELD2": "Binary-to-ASCII Encoded File",
   "FIELD3": 433
 },
 {
   "FIELD1": ".WERD",
   "FIELD2": "Werd Ransomware Encrypted File",
   "FIELD3": 450
 },
 {
   "FIELD1": ".LILOCKED",
   "FIELD2": "Lilocked Ransomware Encrypted File",
   "FIELD3": 450
 },
 {
   "FIELD1": ".EXTR",
   "FIELD2": "COW App Extractor File",
   "FIELD3": 450
 },
 {
   "FIELD1": ".AZF",
   "FIELD2": "AirZip FileSECURE File",
   "FIELD3": 450
 },
 {
   "FIELD1": ".YENC",
   "FIELD2": "yEnc File",
   "FIELD3": 467
 },
 {
   "FIELD1": ".BC5B",
   "FIELD2": "Ransomware Encrypted File",
   "FIELD3": 475
 },
 {
   "FIELD1": ".WPE",
   "FIELD2": "WordPerfect Entrust Document",
   "FIELD3": 500
 },
 {
   "FIELD1": ".LVIVT",
   "FIELD2": "Lvivtotoro Encrypted Game File",
   "FIELD3": 500
 },
 {
   "FIELD1": ".HBX",
   "FIELD2": "BinHex Encoded File",
   "FIELD3": 500
 }
]
final_dict = {}
final_list = []
for line in json_dict:
  final_list.append(line["FIELD1"].lower())
print(final_list)
sleep(3)