"""This module will expand a list, it provides one funtion
 expand_list"""
def expand_list(listo):
    """This function prints each item in a list on a 
    separate line, it takes one argument which 
    should be a list"""
    if isinstance(listo, list):
        for each_item in listo:
            if isinstance(each_item, list):
                expand_list(each_item)
            else:
                print(each_item)
    else:
        print(listo)
