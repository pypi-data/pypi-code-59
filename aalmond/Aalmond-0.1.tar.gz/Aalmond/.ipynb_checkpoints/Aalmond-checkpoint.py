#!/usr/bin/env python
# coding: utf-8


# =========== * =========== * =========== * =========== * =========== * =========== v

# Project : Aalmond!
# Contents: This file contains three (3) Function Definitions that provides Primary EDA (Exploratory Data Analysis) functionality: 
# Function: Dataframe Vital Stats, Outliers Detection, Data View from various sections of a DataFrame.

# 1. vitalStats() : Displays Pandas DataFrame Vital Stats, an exended output of seeded describe()
# 2. showdfQ()    : Displays data rows of a Pandas DataFrame selectively from Mid, Mid Q1, Mid Q3 section of a Dataframe
# 3. showOutL()   : Displays and/or Imputes Outlier values, based on IQR Method, of Pandas DataFrame Numeric Column(s) 

# Usage, Parameter & General Notes documented inside each function as Docstring.

# =========== * =========== * =========== * =========== * =========== * =========== ^


# Dependencies / Requirements: The follwing libraries are needed: 

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"  # Multiple output displays per cell 

from IPython.display import Image, Markdown
from IPython.core.display import display, HTML

import numpy as np  # Numerical Python libraries
import pandas as pd  # to handle data in form of rows and columns 

# =========== * =========== * =========== * =========== #

# BEGIN: Function vitalStats(): Manoj S Bhave: My Original Code Work. Package & Publish on PyPi Python Package Index / Python Library, etc... 

# Future: Add Params: Dup.Rows = 'y/n', Dup.Cols = 'y/n' (for speed), #Modes to Display = n (0,1,2,3..n), ... 
# ... ColType = 'all/num/obj' (All / Numeric / Object), Display Sample Row = True/False, etc... 

# Pending: Code Comments...

def vitalStats(df, dcols = False, srows='', outl='iqr'):

    """ 

Input   : dataframe, parameters 
Output  : 1. dataframe via display() 2. strings via print() 
Usage   : vitalStats(dataframe) 
Author  : Manoj S Bhave 
Version : 0.1 Good To Go!

Function "vitalStats()" entends the output of the regular pd.df.describe() features with various other basic df stats features \
in a single snapshot tabulated output for convenience:

Inputs: dataframe (df)
Params: 
1. dcols = False (default). If True, detects Duplicate COLUMNS in df. Can be SLOW for large df: If df.size > 1M, then: NOT Computed!

2. srows = '' (default). When specified, calls function showdfQ() to display df rows with various row selection criteria. 

3. outl = 'iqr' (default). When specified, calls function showOutL() to show Outliers in all columns. 

NOTE: More param info, Shift+Tab on functions: showdfQ(), showOutL() 

Outputs: Extended Descriptive Statistics in a Unified Compact Tabular Snapshot for all Numeric and/or Object type df columns as \
applicable. These extended / aditional Features are as follows: 

* "unq"   : Unique values count * "null" : Null values count 
* "zero"  : Zero values count   * "skew" : Skewness of column data distribution 
* "OutL"  : Number of Outliers Lower/Less  than Q1-IOR*1.5 of column 
* "OutH"  : Number of Outliers HIgher/Less than Q3+IOR*1.5 of column 
* "mode"  : Mode value of col, displayed when UniMode ONLY
* "mode1" : 1st Mode value of col, displayed when MultiMode ONLY
* "mode2" : 2nd Mode value of col, displayed when MultiMode ONLY
* "modeN" : Total NUMBER of modes for the col, displayed when MultiMode ONLY

NOTE: Limited Output: Mode: When MultiMode, displays ONLY first TWO Modes for Simplicity. Indicates existance of multiple modes for a column. 

Dataframe Level Overall Features: Displayed at the bottom of above Stats Table: 

* "Rows"     : Number of Rows   in df * "Cols"     : Number of Columns in df 
* "DUP.Rows" : Duplicate Rows   in df * "DUP.Cols" : df.size>1M=NOT Computed!
* "Elements" : Number of values in df (rows x cols) 
* "Outliers" : Method to detect outliers' count in "OutL", "OutH" cols. 

    """
    
    import numpy as np  # Numerical Python libraries
    import pandas as pd  # to handle data in form of rows and columns frame
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"  # Multiple output displays per cell 

    dfs = pd.DataFrame()
    dfs['cols'] = df.columns
    dfs = dfs.set_index(keys=['cols'])
    dfs['dtype'] = df.dtypes

    dfs = dfs.join(df.describe(include='all').T)
    drop_cols = ['count']
    if 'unique' in dfs.columns:
        drop_cols = ['count', 'unique']
    dfs.drop(drop_cols, axis=1, inplace=True)

    dfs['unq'] = df.nunique()
    dfs['null'] = df.isna().sum()
    dfs['zero'] = (df == 0).sum()
    dfs['<0'] = (df.select_dtypes(include='number') < 0).sum()
    dfs['skew'] = df.skew()

    # Final: Outliers: Works OK!

    outlrs = []
    for col in df.select_dtypes(include='number'):
        q1 = round(df[col].quantile(.25),2)
        q3 = round(df[col].quantile(.75),2)
        otr = round((q3-q1)*1.5, 2)
        otl = round(q1 - otr, 2)
        oth = round(q3 + otr, 2)
        otls = (df[col] < otl).sum()
        oths = (df[col] > oth).sum()
        outlrs.append((col, otls, oths))

    outlrs_df = pd.DataFrame(outlrs)
    outlrs_df = outlrs_df.set_index(keys=[0])
    dfs['OutL'] = outlrs_df[1]
    dfs['OutH'] = outlrs_df[2]

    # Final: Mode: It Works OK!
    tmp_df = df.mode().T
    if len(tmp_df.columns) > 1:
        dfs['mode1'] = tmp_df[0]
        dfs['mode2'] = tmp_df[1]
        dfs['modeN'] = tmp_df.T.count()
    else:
        dfs['mode'] = tmp_df[0]

    print('* DF Stats For All Columns:')
    dfs.reset_index(inplace=True)
    display(dfs)

    dupcols = 'dcols=False'
    if dcols: 
        if df.size < 1000000:
            dupcols = df.T.duplicated().sum()
        else:
            dupcols = 'n/a:df.size>1M'

    print('* Rows:', df.shape[0], ' * Cols:', df.shape[1], ' * Elements:', df.size, 
      ' * DUP.Rows:', df.duplicated().sum(), ' * DUP.Cols:', dupcols, 
      ' * Outliers: OutL < Q1-IORx1.5, OutH > Q3+IORx1.5') #' * Type:', type(df)

    if srows != '': showdfQ(df, srows)

# End: Function vitalStats(). 

# =========== * =========== * =========== * =========== #

# BEGIN: Function showdfQ(): Manoj S Bhave: My Original Code Work. Package & Publish on PyPi Python Package Index / Python Library, etc... 

# Future: Add Params: ???

def showdfQ(df, srows='m5'):

    """ 

Input   : dataframe, parameters 
Output  : dataframe rows via display() 
Usage   : showdfQ(dataframe, params) 

Author  : Manoj S Bhave 
Created : Tue.Jul.21 2020 
Version : 0.1 (OK To Go!)

Function "showdfQ()" displays a section of dataframe (df) rows as selected by the given params in a single convenient output. Most \
Important functionality is its ability to show rows from around the Middle of df and Middle of Q1 and Q2 which not available easily \
in packaged form of a Function() or an df.attribute()

Inputs: dataframe (df) 
Params: srows = 'hmtrqQ9' : Optional. Default = 'm5': Middle 5 rows shown 

Each letter in the 'srows' param string is a separate parameter (max seven) and can be specified in any combination thereof. \
It takes only the First Seven characters of the param string, rest all chars are ignored. Also, it considers only ONE Digit that \
that occurs First in the param string, rest all digits are ignored: 

'h' : df rows from Head = df.head() 
't' : df rows from Tail = df.tail() 
'r' : df rows Random = df.sample() 
'm' : df rows from around Middle of df 
'q' : df rows from around middle of Q1 
'Q' : df rows from around middle of Q3 
0..9: df rows to display (1..9) per specified criteria above. Optional. Default = '0'. Display 10 rows (Max) when '0' 

NOTE: Limitations: 
A. Minimum row count in the input df MUST be at least 20, otherwise when len(df) < 20 this function will not produce any output. No Show! 
B. When srows is '' or does NOT contain any of the VALID chars above, then this function does not produce any output. No Show! 

Outputs: Data rows from the specified dataframe (df) are displayed as per the specified params above. If all or multiple criteria \
(letters in params) are specified then the order of dataset display is as follows: (whichever is applicable based on params):

1. 'h' Head (0 thru n)
2. 'q' Q1
3. 'm' Middle
4. 'Q' Q3
5. 't' Tail
6. 'r' Random

NOTE: Limitation: The Output is limitd to Max 10 (Ten) rows in any case / combinations of chars within the 'srows' params string. 

    """
    
    import numpy as np  # Numerical Python libraries
    import pandas as pd  # to handle data in form of rows and columns frame
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"  # Multiple output displays per cell 

    if len(df) < 20: srows = ''

    if len(srows) > 7: srows = srows[0:7]
    srows

    nrows = 10
    for i in srows:
        if i.isdigit():
            nrows = int(i)
            break

    if nrows < 1 or nrows > len(df) : nrows = 10
    nrows, df.shape[0]

    mid = len(df)//2 
    low = mid-nrows//2
    high = mid+1+nrows//2

    qmid = len(df)//4 
    qlow = qmid-nrows//2
    qhigh = qmid+1+nrows//2

    Qmid = mid + qmid
    Qlow = Qmid-nrows//2
    Qhigh = Qmid+1+nrows//2

    print('')
    if 'h' in srows: display('\n Showing Head '      + str(nrows) + ' Rows: \n', df.head(nrows))
    if 'q' in srows: display('\n Showing Q1 Middle ' + str(nrows) + ' Rows: \n', df.iloc[qlow : qhigh])
    if 'm' in srows: display('\n Showing Middle '    + str(nrows) + ' Rows: \n', df.iloc[low : high])
    if 'Q' in srows: display('\n Showing Q3 Middle ' + str(nrows) + ' Rows: \n', df.iloc[Qlow : Qhigh])
    if 't' in srows: display('\n Showing Tail '      + str(nrows) + ' Rows: \n', df.tail(nrows))
    if 'r' in srows: display('\n Showing Random '    + str(nrows) + ' Rows: \n', df.sample(nrows))

# End: Function showdfQ(). 

# =========== * =========== * =========== * =========== #

# BEGIN: Function showOutL(): Manoj S Bhave: My Original Code Work. Package & Publish on PyPi Python Package Index / Python Library, etc... 

# Future: Add Params: Activate 'zscore', Outlier_Update_Method = zscore < 0.3, iqr, inside_whisker_end, Q1/Q3 mean, median, mode, KNN, 

def showOutL(df, mthd='iqr', impute=False):

    """ 

Input   : dataframe, parameters 
Output  : Lists Column wise Outliers via print() 
Usage   : showOutL(dataframe, params) 

Author  : Manoj S Bhave 
Created : Tue.Jul.21 2020 
Version : 0.1 (Good To Go!)

Function "showOutL" Detects and Displays all Outliers, based on IQR Method, for all Numeric columns. For each column it displays \
Total Outlier count (Low + High), Separate Low & High counts, Low & High Whisker values, Q1 & Q3 values as potential Imputing values.

Inputs: dataframe (df) 
Params: 
1. 'mthd' = 'iqr (default): Method to be used for Outlier Detection. Other Method value: 'zscore' (Not yet Implemented)

2. 'impute' = False (default): Outliers Display only (No Update). When True, it updates the Outlier value with applicable Q1 / Q3 values \
for each Column, for all Rows. Then to check & verify Imputations, it reruns itself in 'impute' = False mode to Update & Display \
the New metrics based on New Imputed values for verification. 

IQR Method Used: LOW Whisker End = Q1 - (IQR * 1.5); HIGH Whisker End = Q3 + (IQR *1.5) are calculated for a Column. Column values \
that are Below (Less Than) the Low End and/or Col values that are Above (Greater Than) the High End and identified as "Outliers" for \
"Display Only" for "Update" based on param value 'Impute' = False/True.

NOTE: Limitation: Outlier values are update with Q1 and Q3 values only. Other values can be used like 'Mean', 'Median', 'Mode', etc. 

Outputs: 
1. When 'impute' = False: Lists all Outliers for each Numeric Col as mentioned above with Total (Low + High) Outliers counts along \
with individual Low & High subcounts. Displays Low & High cut off Whisker end values along with Q1 & Q3 values for each Col resp.

2. When 'impute' = True: Lists the completion status collectively & individually for each Col along with Total values Imputed for \
each Col. After completion, this function ReRuns itself (without Further Imputation) to ReDetect any New Outliers to check, verify, \
update the new Metrics due to the newly updated Outlier values.

NOTE: If New Outliers are noticed, then if needed, this process can be Rerun in 'impute' = True to fix these new outliers. Process can \
be repeated till it makes business sense to live with some marginal outliers or not without compromising too much on information loss \
due to 'fixed' Col values as a result of Outlier Elimination process. 

    """

    import numpy as np  # Numerical Python libraries
    import pandas as pd  # to handle data in form of rows and columns frame
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"  # Multiple output displays per cell 

    
    # Detect & Display All Outliers for All Numeric Cols with IQR Method and Impute with respective columns' Q1 or Q3 values as applicable: 

    print('\n* Outliers Detection: IQR Method: For All Numerical Columns: LOW Whisker = Q1 - (IQR * 1.5); HIGH Whisker = Q3 + (IQR *1.5): \n')

    for col in df.select_dtypes(include='number'):

        q1  = round(df[col].quantile(.25),2)
        q3  = round(df[col].quantile(.75),2)

        otr = round((q3 - q1) * 1.5, 2)
        otl = round(q1 - otr,2)
        oth = round(q3 + otr,2)

        otls = (df[col] < otl).sum()
        oths = (df[col] > oth).sum()

        if impute:
            df[col] = np.where((df[col] < otl), q1, df[col])
            df[col] = np.where((df[col] > oth), q3, df[col])
            print('Col:', col, otls+oths, 'Values Imputed') 
            
        elif (otls + oths) != 0:
            print('\n* Column:', col, ': Total', otls+oths, 'Outlier Values:') 
            
            if otls != 0:
                print(' ', str(otls).rjust(3, ' '), 'outliers Under Low  Whisker =', str(otl).rjust(7, ' '), ': Impute with Q1 value:', q1) 
            if oths != 0:
                print(' ', str(oths).rjust(3, ' '), 'outliers Over  High Whisker =', str(oth).rjust(7, ' '), ': Impute with Q3 value:', q3) 

        else: print('\n* Column:', col, ': Total', otls+oths, 'Outlier Values: NO OUTLIERS!') 
            
    if impute:  # ReRun to get new matrix after Outlier fix to display the New Outlier count:
        print(*'\nImpute Complete by IQR Method: Check to verify Outliers Elimination')
        showOutL(df, impute=False)
    
# End: Function showOutL(). 

# =========== EOF ===========

