import dateinfer
import operator
import pandas as pd

def get_period_in_data(data_frame, column_name, correlation_threshold, window_coeff):
    """
    Functions takes input as data frame and the column name.
    Here it's assumed that the data would be sorted
    """
    # It only makes sense to iterate to midway because patterns after that would not be needed
    window_size = int(data_frame.shape[0] / 2) - 1
    
    period_dict = dict()
    
    # make sure that we start the wndow size from 30 percent records or more
    start_value = int(window_coeff*data_frame.shape[0])
    for i in range(start_value,window_size+1):
        # pandas autocorr function is used to find the auto correlation
        try:
            correlation_value = data_frame[column_name].autocorr(lag = i)
        except:
            correlation_value = 0
        period_dict[i] = correlation_value
        
    # the idea is find auto correlation of all the elements and then depending on the value find the most
    # correlated index and return it
    if period_dict.items():
        max_index = max(period_dict.items(), key=operator.itemgetter(1))[0]
        max_value = max(period_dict.items(), key=operator.itemgetter(1))[1]
    else:
        return None
    
    # if correlation is below a particular threshold then return None
    if max_value < correlation_threshold:
        return None
    return max_value,max_index

def aggregate_data(data_frame, column, function, kpi_column, agg_func):
    return_df = None
    if function == "month":
        data_frame[function] = data_frame[column].dt.month
    elif function == "week":
        data_frame[function] = data_frame[column].dt.week
    elif function == "quarter":
        data_frame[function] = data_frame[column].dt.quarter
    elif function == "year":
        data_frame[function] = data_frame[column].dt.year
    elif function == "raw":
        return_df = data_frame.groupby(column).agg({kpi_column:agg_func}).reset_index()
        return return_df
             
    return_df = data_frame.groupby(function).agg({kpi_column:agg_func}).reset_index()

    return return_df

def get_date_format(data_frame, column):
    date_format = dateinfer.infer(data_frame[column].tolist())
    if date_format:
        try:
            pd.to_datetime(data_frame[column], errors="raise", format = date_format)
        except:
            return None
    
    return date_format

def trend_identification(data_frame, date_period_column, kpi_column, agg_function, window_coeff = 0.3, auto_aggregate = True, auto_sort = True,correlation_threshold = 0.7):
    # validate function should be from, avg,max,min,sum
    # column dtype should be numeric
    # vallidate if group_column is date
    
    #if group_column is not date:
    
    """
    Steps
    1. get date format -- get_date_format(data_frame, column)
    2. convert into date -- pd.to_datetime(data_frame[column], errors="raise", format = date_format)
    3. get aggregated data for raw,week,month,quarter,year -- aggregate_data(data_frame, column, function, kpi_column, agg_func)
    4. run trend code -- get_period_in_data(data_frame, column_name, correlation_threshold, window_coeff)
    """
    working_df = data_frame[[date_period_column,kpi_column]]
    
    # step 1
    dt_formate = get_date_format(working_df, date_period_column)
    
    #step 2
    if dt_formate:
        working_df[date_period_column] = pd.to_datetime(working_df[date_period_column], errors="raise", format = dt_formate)
        
    #step 3
    
    period_list = ["raw","week","month","quarter","year"]
    return_list = []
    for period in period_list:
        agg_df = aggregate_data(working_df, date_period_column, period, kpi_column, agg_function)
        out = get_period_in_data(agg_df, kpi_column, correlation_threshold, window_coeff)
        if out:
            text = "Repeating Trend found after every " + str(out[1]) + " " + period + "s"
            return_list.append(text)
            
    if len(return_list) == 0:
        return "No trends found"

    else:
        return return_list