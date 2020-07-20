'''
Created by Begonia ,June 21st 2020, in SH
It's the Package for sorting functions
'''

__author__="Begonia"
__all__=["bubble_sort",
         "bucket_sort",
         "count_sort",
         "insert_sort",
         "merge_sort",
         "quick_sort",
         "radix_sort",
         "select_sort",
         "shell_sort"]
if __name__=="__main__":
    for i in __all__:
        __import__(i)
else:
    print("Created by Begonia ,June 21st 2020, in SH\nIt's the Package for sorting functions")
