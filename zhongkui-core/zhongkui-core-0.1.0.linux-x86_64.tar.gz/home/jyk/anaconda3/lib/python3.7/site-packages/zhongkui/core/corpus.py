class MAGIC:
    MIME = "mime_type"
    ENCODING = "encoding"
    TYPE = "type_name"


class DIEC:
    PROTECTOR = "protector"
    PACKER = "packer"
    COMPILER = "compiler"
    LINKER = 'linker'


class PEFILE:
    ISPROBABLYPACKED = "isProbablyPacked"


class FILETYPE:
    PE = ("win32exe", "win32dll", "win64dll", "win64exe")
    ELF = ("elfexecutable", "elfsharedlibrary")


class EXIFTOOL:
    FILESIZE = "FileSize"
    FILETYPE = "FileType"
    FILETYPEEXTENSION = "FileTypeExtension"


class BasicInfo:
    name = 'name'
    md5 = 'md5'
    sha1 = 'sha1'
    sha256 = 'sha256'
    fileType = 'fileType'
    fileSize = 'fileSize'
    isProbablyPacked = 'isProbablyPacked'


class PEHeader:
    timestamp = 'timestamp'
    entryPoint = 'entryPoint'
    sections = 'sections'


class PESection:
    name = 'name'
    virtualAddress = 'virtualAddress'
    virtualSize = 'virtualSize'
    rawSize = 'rawSize'
    entropy = 'entropy'
    md5 = 'md5'


class PEImport:
    dllName = 'dllName'
    importFunctions = 'importFunctions'


class PEInfo:
    header = 'header'
    sections = 'sections'
    imports = 'imports'
    isProbablyPacked = 'isProbablyPacked'