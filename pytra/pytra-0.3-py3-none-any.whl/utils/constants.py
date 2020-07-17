#
# Help messages for options
TRANSLATE_FROM_HELP = 'Language code to translate from. Default: "auto".'
TRANSLATE_TO_HELP = 'Language code to translate to. Default: "en".'
OUTPUT_FILE_NAME_HELP = 'Specify output file name. Relative and absolute paths are allowed'
TRANSLATED_FILE_LANGUAGE_HELP = 'Language code to translate to. Default: "en".'

# Help messages for commands
TRANSLATE_HELP = 'Translate stuff'
DETECT_HELP = 'Detect languages'
DETECT_FILE_COMMAND_HELP = '''
                              Detect file\'s language. 
                              Assuming that whole file is in single language.
                           '''
SHOW_LANGUAGE_CODE_HELP = '''
                              Show language codes. 
                              If language argument is provided
                              show only for provided language.
                           '''
TRANSLATE_FILE_COMMAND_HELP = '''
                                 Text file to translate.
                                 By default to "en" from "auto".
                                 Use -t option to specify language 
                                 of the output file.
                                 By default pytra looks for the file
                                 ii current directory. But it is possible
                                 to specify relative or absolute path too.
                              '''
