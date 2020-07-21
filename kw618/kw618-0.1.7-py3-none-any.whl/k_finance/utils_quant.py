import json
import pandas as pd


# 导入常用的固定路径(多平台通用)
from kw618._file_path import *
# 本脚本依赖很多 utils_requests的函数和模块, 直接用*  (注意要避免循环导入问题)
from kw618.k_requests.utils_requests import *
from kw618.k_python.utils_python import *
from kw618.k_pandas.utils_pandas import *

req = myRequest().req



def get_hist_data(stock_code="0.002505", period=30, pt=True):
    """
        function: 从'xxxx'获取xxxx
        params:
            stock_code: stock代码
            period: 区间 (0代表全部区间)
    """
    # 1. 请求数据
        # beg:0(开始日期); end:20500101(结束日期);  lmt:120(限制呈现的天数)
    url = ("http://push2his.eastmoney.com/api/qt/stock/kline/get"
            "?fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf61&klt=101&fqt=1"
            f"&secid={stock_code}&beg=0&end=20500000"
            )
    j = req(url)
    # 2. 把结果转化成可处理的df
    d = json.loads(j)
    all_stock_data = d.get("data", {})
    k_lines_lst = all_stock_data.get("klines", [])
    k_lines_lst = [k_info_str.split(",") for k_info_str in k_lines_lst]
    df = pd.DataFrame(
        k_lines_lst, columns=[
            "market_date", "start_price", "end_price", "max_price", "min_price",
            "trading_volumn", "trading_money", "swing_rate", "turnover_rate"
            ],
        dtype="float64",
        )
    df["market_date"] = pd.to_datetime(df["market_date"])
    start_index = -period -100 if period else 0 # note: 这里-100是为了方便后面计算30日移动平均值
    df = df[start_index:]
    # 3. 处理数据
        # df: 源数据
        # k_lines_df: 历史完整的"k线图"数据df
        # growth_df: 增量/增幅的df (使用shift平移)
        # rolling_df: 移动平均的df (使用rolling平移/求均值)
        # show_df: 最终呈现的df (方便我查看走势的)
    k_lines_df = df.set_index("market_date")

    s = k_lines_df["end_price"]
    growth_amount = s-s.shift(1)
    growth_rate = growth_amount / s.shift(1)
    growth_df = pd.DataFrame({"growth_amount":growth_amount, "growth_rate":growth_rate})

    s1 = df["end_price"].rolling(5).mean()
    s2 = df["end_price"].rolling(10).mean()
    s3 = df["end_price"].rolling(20).mean()
    s4 = df["end_price"].rolling(30).mean()
    rolling_df = pd.DataFrame({"market_date":k_lines_df.index, "5d_avg":s1, "10d_avg":s2, "20d_avg":s3, "30d_avg":s4})
    rolling_df["market_date"] = pd.to_datetime(rolling_df["market_date"])
    rolling_df = rolling_df.set_index("market_date")

    show_df = pd.concat([k_lines_df[["end_price"]], growth_df, rolling_df], axis=1)
    show_df = round_df(show_df[-period:], 3) # 取3位小数
    if pt == True:
        print(f"\n\n\n代码 - {stock_code} - '历史数据' 如下:")
        print(show_df)
    return show_df




def get_trend_data(stock_code="0.002505", period=0, pt=True):
    """
        function: 从'xxxx'获取xxxx
    """
    # 1. 请求数据
    url = ("http://push2.eastmoney.com/api/qt/stock/trends2/get"
            "?fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6%2Cf7%2Cf8%2Cf9%2Cf10%2Cf11%2Cf12%2Cf13"
            "&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58"
            f"&secid={stock_code}&&ut=e1e6871893c6386c5ff6967026016627"
            )
    j = req(url)
    # 2. 把结果转化成可处理的df
    d = json.loads(j)
    all_stock_data = d.get("data", {})
    trends_lst = all_stock_data.get("trends", [])
    trends_lst = [trends_info_str.split(",") for trends_info_str in trends_lst]
    df = pd.DataFrame(
        trends_lst, columns=[
            "market_date", "start_price", "end_price", "max_price", "min_price",
            "trading_volumn", "trading_money", "avg_price???"
            ],
        dtype="float64",
        )
    df["market_date"] = pd.to_datetime(df["market_date"])
    opening_price = df["end_price"].iloc[0] if len(df["end_price"]) else None # 开盘价格 (实际上是9:15集合竞价的价格)

    start_index = -period -100 if period else 0 # note: 这里-100是为了方便后面计算30日移动平均值
    df = df[start_index:]
    # 3. 处理数据
        # df: 源数据
        # trends_df: 今天的"分时图"数据df
        # growth_df: 增量/增幅的df (使用shift平移)
        # rolling_df: 移动平均的df (使用rolling平移/求均值)
        # show_df: 最终呈现的df (方便我查看走势的)
    trends_df = df.set_index("market_date")
    end_price_ss = trends_df["end_price"]
    if opening_price:
        today_growth_rate_ss = ((end_price_ss/opening_price -1)*100).round(2).astype("str")+"%" # 数据类型为:object
        growth_amount_ss = end_price_ss-end_price_ss.shift(1)
        growth_rate_ss = growth_amount_ss / end_price_ss.shift(1)
        growth_df = pd.DataFrame({"end_price":end_price_ss, "今日涨幅":today_growth_rate_ss, "growth_amount":growth_amount_ss, "growth_rate":growth_rate_ss})
        growth_df.insert(0, "stock_code", stock_code)

        ss1 = end_price_ss.rolling(5).mean()
        ss2 = end_price_ss.rolling(10).mean()
        ss3 = end_price_ss.rolling(20).mean()
        ss4 = end_price_ss.rolling(30).mean()
        ss5 = end_price_ss.rolling(60).mean()
        rolling_df = pd.DataFrame({"market_date":trends_df.index, "5min_avg":ss1, "10min_avg":ss2, "20min_avg":ss3, "30min_avg":ss4, "60min_avg":ss5})
        rolling_df["market_date"] = pd.to_datetime(rolling_df["market_date"])
        rolling_df = rolling_df.set_index("market_date")

        show_df = pd.concat([growth_df, rolling_df], axis=1)
        show_df = round_df(show_df[-period:], 3) # 取3位小数
        if pt == True:
            print(f"\n\n\n代码 - {stock_code} - '分时数据' 如下:")
            print(show_df)
        return show_df
    else:
        print({"k_msg":"\n还没开盘, 无法获取开盘价, 无法得到df.\n"})


def get_main_data(stock_code="0.002505"):
    # """
    #     罗列 secid 的多种对应关系:
    #     1.000001:上证指数; 0.399001:深证成指;  0.399006:创业板指;  90.BK0433: 农牧饲渔(板块)
    #     0.000001:中国平安; 0.000002:万科A;  0.002505:大康农业;
    # """
    """
        function: 同时获取'历史数据'和'今日分时数据'
    """


    get_hist_data(stock_code)
    get_trend_data(stock_code)



# 0.002168:;  1.600757:长江
# 沪市:1开头; 深市:0开头
def get_live_data(stock_code="0.002505"):
    "获取自动清屏的'实时数据'!"
    count = 0
    while True:
        count += 1
        print(f"count: {count}")
        get_trend_data(stock_code)
        time.sleep(60)
        os.system("clear")



def get_my_stock(stock_code_lst=[]):
    if len(stock_code_lst) == 0:
        stock_code_lst = ["1.000001", "0.002505", "0.002168", "1.600757"]

    to_concat_lst = []
    for stock_code in stock_code_lst:
        last_trend_data_df = get_trend_data(stock_code, period=1, pt=False) # 最新一行的'分时数据' (df类型)
        to_concat_lst.append(last_trend_data_df)

    # 合并多个stock的'最新'数据
    df = pd.concat(to_concat_lst, axis=0) # 行方向:上下扩展行
    print(df)
    return df




def main():
    get_live_data()


if __name__ == '__main__':
    print("Start test!\n\n")
    main()
    print("\n\n\nIt's over!")
