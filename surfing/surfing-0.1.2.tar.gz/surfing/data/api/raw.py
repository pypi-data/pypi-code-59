from typing import List, Tuple
import pandas as pd
from ..wrapper.mysql import RawDatabaseConnector
from ..view.raw_models import *


class RawDataApi(object):
    def get_raw_cm_index_price_df(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    CmIndexPrice
                ).filter(
                    CmIndexPrice.datetime >= start_date,
                    CmIndexPrice.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_cxindex_index_price_df(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    CxindexIndexPrice
                ).filter(
                    CxindexIndexPrice.datetime >= start_date,
                    CxindexIndexPrice.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_yahoo_index_price_df(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    YahooIndexPrice
                ).filter(
                    YahooIndexPrice.datetime >= start_date,
                    YahooIndexPrice.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_rq_index_price_df(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqIndexPrice
                ).filter(
                    RqIndexPrice.datetime >= start_date,
                    RqIndexPrice.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_wind_fund_info(self, funds: Tuple[str] = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    WindFundInfo
                )
                if funds:
                    query = query.filter(
                        WindFundInfo.wind_id.in_(funds),
                    )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_fund_fee(self):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    FundFee
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_fund_rating(self):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    FundRating
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_stock_fin_fac(self, stock_id_list, start_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqStockFinFac
                ).filter(
                    RqStockFinFac.stock_id.in_(stock_id_list),
                    RqStockFinFac.datetime >= start_date,
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_rq_stock_valuation(self, stock_id_list, start_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqStockValuation.datetime,
                    RqStockValuation.stock_id,
                    RqStockValuation.pb_ratio_lf,
                    RqStockValuation.pe_ratio_ttm,
                    RqStockValuation.peg_ratio_ttm,
                    RqStockValuation.dividend_yield_ttm,
                ).filter(
                    RqStockValuation.stock_id.in_(stock_id_list),
                    RqStockValuation.datetime >= start_date,

                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_rq_index_weight(self, index_id_list, start_date):
        with RawDatabaseConnector().managed_session() as quant_session:
            try:
                query = quant_session.query(
                        RqIndexWeight.index_id,
                        RqIndexWeight.datetime,
                        RqIndexWeight.stock_list,
                    ).filter(
                        RqIndexWeight.index_id.in_(index_id_list),
                        RqIndexWeight.datetime >= start_date,
                    )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_index_val_pct(self):
        with RawDatabaseConnector().managed_session() as quant_session:
            try:
                query = quant_session.query(
                        IndexValPct
                    )
                df = pd.read_sql(query.statement, query.session.bind)
                return df

            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))

    def get_rq_fund_indicator(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqFundIndicator
                ).filter(
                    RqFundIndicator.datetime >= start_date,
                    RqFundIndicator.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_rq_trading_day_list(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    TradingDayList
                ).filter(
                    TradingDayList.datetime >= start_date,
                    TradingDayList.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_tradedates(self, start_date='', end_date=''):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmTradeDates
                )
                if start_date:
                    query = query.filter(
                        EmTradeDates.TRADEDATES >= start_date,
                    )
                if end_date:
                    query = query.filter(
                        EmTradeDates.TRADEDATES <= end_date,
                    )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_stock_info(self):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    StockInfo
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_rq_fund_nav(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqFundNav
                ).filter(
                    RqFundNav.datetime >= start_date,
                    RqFundNav.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_fund_nav(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmFundNav
                ).filter(
                    EmFundNav.DATES >= start_date,
                    EmFundNav.DATES <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def delete_em_fund_nav(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmFundNav
                ).filter(
                    EmFundNav.DATES >= start_date,
                    EmFundNav.DATES <= end_date
                ).delete(synchronize_session=False)
                db_session.commit()
                return True
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_rq_fund_size(self):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqFundSize
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_rq_stock_price(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqStockPrice
                ).filter(
                    RqStockPrice.datetime >= start_date,
                    RqStockPrice.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_rq_stock_post_price(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    RqStockPostPrice
                ).filter(
                    RqStockPostPrice.datetime >= start_date,
                    RqStockPostPrice.datetime <= end_date
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_index_price(self, start_date, end_date, index_id_list: Tuple = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmIndexPrice
                )
                if index_id_list:
                    query = query.filter(
                        EmIndexPrice.em_id.in_(index_id_list),
                    )
                query = query.filter(
                    EmIndexPrice.datetime >= start_date,
                    EmIndexPrice.datetime <= end_date,
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def delete_em_index_price(self, index_id_list, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                db_session.query(
                    EmIndexPrice
                ).filter(
                    EmIndexPrice.em_id.in_(index_id_list),
                    EmIndexPrice.datetime >= start_date,
                    EmIndexPrice.datetime <= end_date,
                ).delete(synchronize_session=False)
                db_session.commit()
                return True
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_index_val(self, start_date, end_date, index_id_list):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmIndexVal
                ).filter(
                    EmIndexVal.CODES.in_(index_id_list),
                    EmIndexVal.DATES >= start_date,
                    EmIndexVal.DATES <= end_date,
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_fund_scale(self, start_date, end_date):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmFundScale
                ).filter(
                    EmFundScale.DATES >= start_date,
                    EmFundScale.DATES <= end_date,
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_stock_price(self, start_date: str, end_date: str, stock_list: Tuple[str] = (), columns: Tuple[str] = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmStockPrice.CODES,
                    EmStockPrice.DATES,
                )
                if columns:
                    query = query.add_columns(*columns)
                if stock_list:
                    query = query.filter(
                        EmStockPrice.CODES.in_(stock_list)
                    )
                query = query.filter(
                    EmStockPrice.DATES >= start_date,
                    EmStockPrice.DATES <= end_date,
                )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print(f'Failed to get data <err_msg> {e} from {EmStockPrice.__tablename__}')
                return None

    def get_em_stock_post_price(self, start_date: str, end_date: str, stock_list: Tuple[str] = (), columns: Tuple[str] = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmStockPostPrice.CODES,
                    EmStockPostPrice.DATES,
                )
                if columns:
                    query = query.add_columns(*columns)
                if stock_list:
                    query = query.filter(
                        EmStockPostPrice.CODES.in_(stock_list)
                    )
                query = query.filter(
                    EmStockPostPrice.DATES >= start_date,
                    EmStockPostPrice.DATES <= end_date,
                )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print(f'Failed to get data <err_msg> {e} from {EmStockPostPrice.__tablename__}')
                return None

    def get_em_stock_info(self, stock_list: Tuple[str] = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmStockInfo
                )
                if stock_list:
                    query = query.filter(
                        EmStockInfo.CODES.in_(stock_list)
                    )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print(f'Failed to get data <err_msg> {e} from {EmStockInfo.__tablename__}')
                return None

    def get_em_daily_info(self, start_date: str, end_date: str, stock_list: Tuple[str] = (), columns: Tuple[str] = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmStockDailyInfo.CODES,
                    EmStockDailyInfo.DATES,
                )
                if columns:
                    query = query.add_columns(*columns)
                if stock_list:
                    query = query.filter(
                        EmStockDailyInfo.CODES.in_(stock_list)
                    )
                query = query.filter(
                    EmStockDailyInfo.DATES >= start_date,
                    EmStockDailyInfo.DATES <= end_date,
                )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print(f'Failed to get data <err_msg> {e} from {EmStockDailyInfo.__tablename__}')
                return None

    def get_em_stock_fin_fac(self, stock_list: Tuple[str] = (), date_list: Tuple[str] = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmStockFinFac
                )
                if stock_list:
                    query = query.filter(
                        EmStockFinFac.CODES.in_(stock_list)
                    )
                if date_list:
                    query = query.filter(
                        EmStockFinFac.DATES.in_(date_list)
                    )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print(f'Failed to get data <err_msg> {e} from {EmStockFinFac.__tablename__}')
                return None

    def get_em_index_component(self, start_date: str, end_date: str, index_list: Tuple[str] = ()):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmIndexComponent
                )
                if index_list:
                    query = query.filter(
                        EmIndexComponent.index_id.in_(index_list)
                    )
                query = query.filter(
                    EmIndexComponent.datetime >= start_date,
                    EmIndexComponent.datetime <= end_date,
                )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print(f'Failed to get data <err_msg> {e} from {EmIndexComponent.__tablename__}')
                return None

    def get_em_fund_holding_rate(self, start_date: str):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmFundHoldingRate
                ).filter(
                    EmFundHoldingRate.DATES >= start_date,
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_fund_list(self, date: str, limit = -1):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmFundList.datetime,
                    EmFundList.all_live_fund_list,
                    EmFundList.delisted_fund_list,
                ).filter(
                    EmFundList.datetime <= date,
                )
                if limit != -1:
                    query = query.order_by(EmFundList.datetime.desc()).limit(limit)
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_fund_info(self, funds: List[str]):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmFundInfo
                ).filter(
                    EmFundInfo.CODES.in_(funds),
                )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_em_fund_benchmark(self, end_date: str):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    EmFundBenchmark
                ).filter(
                    EmFundBenchmark.DATES <= end_date,
                )
                return pd.read_sql(query.statement, query.session.bind)
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_wind_holder_structure(self, start_date: str, wind_fund_list:list):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    WindFundHolderStructure
                ).filter(
                    WindFundHolderStructure.END_DT >= start_date,
                    WindFundHolderStructure.S_INFO_WINDCODE.in_(wind_fund_list),
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_wind_fund_stock_portfolio(self, start_date: str, wind_fund_list:list):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    WindFundStockPortfolio
                ).filter(
                    WindFundStockPortfolio.F_PRT_ENDDATE >= start_date,
                    WindFundStockPortfolio.S_INFO_WINDCODE.in_(wind_fund_list),
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_wind_fund_nav(self, start_date: str, wind_fund_list:list):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    WindFundNav
                ).filter(
                    WindFundNav.PRICE_DATE >= start_date,
                    WindFundNav.F_INFO_WINDCODE.in_(wind_fund_list),
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_wind_manager_info(self, wind_fund_list:list):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    WindFundManager
                ).filter(
                    WindFundManager.F_INFO_WINDCODE.in_(wind_fund_list),
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None

    def get_wind_indus_portfolio(self, start_date: str, wind_fund_list:list):
        with RawDatabaseConnector().managed_session() as db_session:
            try:
                query = db_session.query(
                    WindIndPortfolio
                ).filter(
                    WindIndPortfolio.F_PRT_ENDDATE >= start_date,
                    WindIndPortfolio.S_INFO_WINDCODE.in_(wind_fund_list),
                )
                df = pd.read_sql(query.statement, query.session.bind)
                return df
            except Exception as e:
                print('Failed to get data <err_msg> {}'.format(e))
                return None