from . import DataManager
import pandas as pd
import datetime
import time
import io
import contextlib
from ..wrapper.mysql import BasicDatabaseConnector, DerivedDatabaseConnector
from .fund_info_filter import filter_fund_info, fund_info_update
from ..struct import AssetPrice, FundScoreParam, TaaTunerParam, AssetTimeSpan
from .score import FundScoreManager
from .data_tables import FundDataTables
from ..view.basic_models import *
from ..view.derived_models import *


@contextlib.contextmanager
def profiled(file_name=None):
    import cProfile
    import pstats

    pr = cProfile.Profile()
    pr.enable()
    yield
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    # uncomment this to see who's calling what
    # ps.print_callers()
    if file_name is None:
        print(s.getvalue())
    else:
        open(file_name, 'w').write(s.getvalue())


class FundDataManager(DataManager):

    def __init__(self, start_time=None, end_time=None, fund_score_param: FundScoreParam = None, score_manager: FundScoreManager = None):
        DataManager.__init__(self,
            start_time or datetime.datetime(2005, 1, 1),
            end_time or datetime.datetime.now()
        )
        self._fund_score_param = fund_score_param or FundScoreParam(tag_type=1, score_method=1, is_full=1)
        self.dts = FundDataTables()
        self._is_inited = False
        self._score_manager = score_manager or FundScoreManager()
        self.set_score_param(self._fund_score_param)

    @property
    def inited(self):
        return self._is_inited

    def init(self, index_list=None, score_pre_calc=True, print_time=False, use_weekly_monthly_indicators=False):
        _tm_start = time.time()
        index_list = index_list or list(AssetTimeSpan.__dataclass_fields__.keys())

        def fetch_table(session, view):
            query = session.query(view)
            return pd.read_sql(query.statement, query.session.bind)

        # info is necessary
        with BasicDatabaseConnector().managed_session() as quant_session:
            _tm_basic_start = time.time()
            self.dts.fund_info = fetch_table(quant_session, FundInfo)
            _tm_basic_fetch_info = time.time()
            self.dts.fund_info = fund_info_update(self.dts.fund_info)
            _filter_fund_info = filter_fund_info(self.dts.fund_info, index_list)
            _tm_basic_filter_info = time.time()
            self.dts.fund_list = set(_filter_fund_info.fund_id)
            self.dts.fund_index_map = {cur.fund_id: cur.index_id for cur in _filter_fund_info.itertuples()}
            self.end_date_dic = self.dts.fund_info[['fund_id', 'end_date']].set_index('fund_id').to_dict()['end_date']
            _tm_basic_prep_struct = time.time()
            self.dts.trading_days = fetch_table(quant_session, TradingDayList)
            self.dts.trading_days = self.dts.trading_days[self.dts.trading_days.datetime <= self.end_date]
            trim_trading_days = self.dts.trading_days[(self.dts.trading_days.datetime >= self.start_date) & (self.dts.trading_days.datetime <= self.end_date)].datetime
            _tm_basic_fetch_days = time.time()
            # index
            self.dts.index_info = fetch_table(quant_session, IndexInfo)
            _tm_basic_fetch_index_info = time.time()
            _index_query = quant_session.query(
                    IndexPrice.index_id,
                    IndexPrice.datetime,
                    IndexPrice.close
                ).filter(
                    IndexPrice.index_id.in_(index_list),
                    IndexPrice.datetime >= self.start_date,
                    IndexPrice.datetime <= self.end_date
                )
            self.dts.index_price = pd.read_sql(_index_query.statement, _index_query.session.bind).pivot_table(index='datetime', columns='index_id', values='close').reindex(trim_trading_days).fillna(method='ffill')
            _tm_basic_fetch_index_price = time.time()
            # fund nav
            _fund_nav_query = quant_session.query(
                    FundNav.fund_id,
                    FundNav.adjusted_net_value,
                    FundNav.unit_net_value,
                    FundNav.datetime
                    # FundNav.subscribe_status,
                    # FundNav.redeem_status,
                ).filter(
                    FundNav.fund_id.in_(self.dts.fund_list),
                    FundNav.datetime >= self.start_date,
                    FundNav.datetime <= self.end_date,
                )
            _nav_df = pd.read_sql(_fund_nav_query.statement, _fund_nav_query.session.bind)
            _tm_basic_fetch_fund_nav = time.time()

            # 这里我们制作一个总的pivot_table再取值，会比分别两次pivot_table快一些
            # 如果index-column pair有重复的值，pivot会报错而pivot_table不会，所以这里用pivot也许更好些
            # 但是pivot里边会调用set_index，导致datetime列的dtype从object变为datetime64[ns]
            _temp_fund_nav = _nav_df.pivot_table(index='datetime', columns='fund_id')
            self.dts.fund_nav = _temp_fund_nav['adjusted_net_value'].dropna(axis=1, how='all').fillna(method='ffill')
            self.dts.fund_unit_nav = _temp_fund_nav['unit_net_value'].dropna(axis=1, how='all').fillna(method='ffill')
            _tm_basic_pivot_fund_nav = time.time()

            # fund size and fund com hold
            # 机构持仓比例每六个月更新，提前取半年以上, 填充空白值用
            # fund_com_hold fund_size 和 fund_nav同结构，日期纵轴，基金代码横轴
            _fund_size_and_hold_rate_query = quant_session.query(
                    Fund_size_and_hold_rate.fund_id,
                    Fund_size_and_hold_rate.size,
                    Fund_size_and_hold_rate.institution_holds,
                    Fund_size_and_hold_rate.datetime
                ).filter(
                    Fund_size_and_hold_rate.fund_id.in_(self.dts.fund_list),
                    Fund_size_and_hold_rate.datetime >= self.start_date - datetime.timedelta(days=200),
                    Fund_size_and_hold_rate.datetime <= self.end_date,
                )
            _size_and_hold_rate = pd.read_sql(_fund_size_and_hold_rate_query.statement, _fund_size_and_hold_rate_query.session.bind)
            _dt_index = self.dts.trading_days[self.dts.trading_days.datetime >= (self.start_date - datetime.timedelta(days=200))].datetime
            _temp_size_and_hold_rate = _size_and_hold_rate.pivot(index='datetime', columns='fund_id').reindex(_dt_index).fillna(method='ffill')
            self.dts.fund_size = _temp_size_and_hold_rate['size']
            self.dts.fund_com_hold = _temp_size_and_hold_rate['institution_holds']
            _tm_basic_fetch_fund_size = time.time()

            if print_time:
                print(f'\t[time][basic] fetch fund info : {_tm_basic_fetch_info - _tm_basic_start}')
                print(f'\t[time][basic] filter fund info: {_tm_basic_filter_info - _tm_basic_fetch_info}')
                print(f'\t[time][basic] prep fund struct: {_tm_basic_prep_struct - _tm_basic_filter_info}')
                print(f'\t[time][basic] fetch trade days: {_tm_basic_fetch_days - _tm_basic_prep_struct}')
                print(f'\t[time][basic] fetch index info: {_tm_basic_fetch_index_info - _tm_basic_fetch_days}')
                print(f'\t[time][basic] fetch index price: {_tm_basic_fetch_index_price - _tm_basic_fetch_index_info}')
                print(f'\t[time][basic] fetch fund navs: {_tm_basic_fetch_fund_nav - _tm_basic_fetch_index_price}')
                print(f'\t[time][basic] pivot fund navs: {_tm_basic_pivot_fund_nav - _tm_basic_fetch_fund_nav}')
                print(f'\t[time][basic] fetch fund size: {_tm_basic_fetch_fund_size - _tm_basic_pivot_fund_nav}')
        _tm_basic = time.time()

        # get derived data first
        with DerivedDatabaseConnector().managed_session() as derived_session:
            _tm_deriv_start = time.time()
            _fund_indicator_query = derived_session.query(
                    FundIndicator.fund_id,
                    FundIndicator.datetime,
                    FundIndicator.alpha,
                    FundIndicator.beta,
                    FundIndicator.fee_rate,
                    FundIndicator.track_err,
                    FundIndicator.year_length,
                    # FundIndicator.down_risk,
                    # FundIndicator.info_ratio,
                    # FundIndicator.ret_over_period,
                    # FundIndicator.info_ratio,
                    # FundIndicator.treynor,
                    # FundIndicator.mdd,
                    # FundIndicator.m_square,
                    # FundIndicator.var,
                    # FundIndicator.r_square,
                    # FundIndicator.sharpe,
                    # FundIndicator.annual_ret,
                    # FundIndicator.annual_vol,
                    # FundIndicator.time_ret,
                ).filter(
                    FundIndicator.fund_id.in_(self.dts.fund_list),
                    FundIndicator.datetime >= self.start_date,
                    FundIndicator.datetime <= self.end_date,
                )
            self.dts.fund_indicator = pd.read_sql(_fund_indicator_query.statement, _fund_indicator_query.session.bind)
            _tm_deriv_fetch_fund_indicator = time.time()
            self.dts.fund_indicator['index_id'] = self.dts.fund_indicator.fund_id.apply(lambda x: self.dts.fund_index_map[x])
            _tm_deriv_apply_fund_indicator = time.time()
            # fetch index val data from derived table, and choose different pct value for different index_id
            _tm_deriv_fetch_index_pct = time.time()
            pct_index_list = list(TaaTunerParam.POOL.keys())
            _index_pct_query = derived_session.query(
                    IndexValuationDevelop
                ).filter(
                    IndexValuationDevelop.index_id.in_(pct_index_list),
                    IndexValuationDevelop.datetime >= self.start_date,
                    IndexValuationDevelop.datetime <= self.end_date,
                ).order_by(IndexValuationDevelop.datetime.asc())
            self._index_pct_df = pd.read_sql(_index_pct_query.statement, _index_pct_query.session.bind).set_index('index_id')
            # 按照trading date 作为index, fillna
            date_list = self.dts.trading_days.datetime.tolist()
            res = []
            for index_id in pct_index_list:
                df = self._index_pct_df[self._index_pct_df.index == index_id].set_index('datetime').reindex(date_list).reset_index().fillna(method='ffill')
                df.loc[:, 'index_id'] = index_id
                res.append(df)
            _index_pct_df = pd.concat(res, axis=0)
            self.dts.index_pct = _index_pct_df.pivot_table(index=['datetime', 'index_id'], values=['pe_pct', 'pb_pct', 'ps_pct'])
            self.dts.index_date_list = self.dts.index_pct.index.remove_unused_levels().levels[0]
            _tm_deriv_apply_index_pct = time.time()

            if use_weekly_monthly_indicators:
                # indicator weekly 只有周日有值 在每一个fund上fillna, merge week_ly into indicator
                _fund_indicator_weekly_query = derived_session.query(
                        FundIndicatorWeekly.fund_id,
                        FundIndicatorWeekly.datetime,
                        FundIndicatorWeekly.alpha_w,
                        FundIndicatorWeekly.beta_w,
                        FundIndicatorWeekly.track_err_w,
                    ).filter(
                        FundIndicatorWeekly.fund_id.in_(self.dts.fund_list),
                        FundIndicatorWeekly.datetime >= self.start_date,
                        FundIndicatorWeekly.datetime <= self.end_date,
                    )
                _fund_indicator_weekly = pd.read_sql(_fund_indicator_weekly_query.statement, _fund_indicator_weekly_query.session.bind)
                _fund_indicator_weekly = _fund_indicator_weekly.pivot_table(index='datetime', columns='fund_id')
                _dt = _fund_indicator_weekly.index.union(date_list).set_names('datetime')  # 交易日，和现有indicator index 周日做并集
                _fund_indicator_weekly = _fund_indicator_weekly.reindex(index=_dt).fillna(method='ffill').stack().swaplevel()
                _fund_indicator_weekly = _fund_indicator_weekly.groupby(level='fund_id').apply(lambda x: x.droplevel(level=0).loc[:self.end_date_dic[x.index.get_level_values(0).array[0]], :])
                _tm_process_indicator_weekly = time.time()

                # indicator monthly 只有每月最后一天有值 在每一个fund上fillna, merge monthly into indicator
                _fund_indicator_monthly = fetch_table(derived_session, FundIndicatorMonthly).drop(columns='_update_time')
                _fund_indicator_monthly = _fund_indicator_monthly.pivot_table(index='datetime', columns='fund_id')
                _dt = _fund_indicator_monthly.index.union(date_list).set_names('datetime')  # 交易日，和现有indicator index做并集
                _fund_indicator_monthly = _fund_indicator_monthly.reindex(index=_dt).fillna(method='ffill').stack().swaplevel()
                _fund_indicator_monthly = _fund_indicator_monthly.groupby(level='fund_id').apply(lambda x: x.droplevel(level=0).loc[:self.end_date_dic[x.index.get_level_values(0).array[0]], :])
                _tm_process_indicator_monthly = time.time()
                # 本来join可以传一个list of df进去一起join，效率应该更高，但这里用了on参数指定fund_indicator的其中两列（而不是index），这样便只能一次传一个df进去（pandas不支持这种情况下传一个list）
                for df in [_fund_indicator_weekly, _fund_indicator_monthly]:
                    self.dts.fund_indicator = self.dts.fund_indicator.join(df, on=['fund_id', 'datetime'], how='left')
                _tm_process_indicator_join = time.time()
            else:
                _tm_process_indicator_weekly = time.time()
                _tm_process_indicator_monthly = _tm_process_indicator_weekly
                _tm_process_indicator_join = _tm_process_indicator_weekly
            if print_time:
                print(f'\t[time][deriv] fetch fund indicator: {_tm_deriv_fetch_fund_indicator - _tm_deriv_start}')
                print(f'\t[time][deriv] apply fund indicator: {_tm_deriv_apply_fund_indicator - _tm_deriv_fetch_fund_indicator}')
                print(f'\t[time][deriv] fetch index val: {_tm_deriv_fetch_index_pct - _tm_deriv_apply_fund_indicator}')
                print(f'\t[time][deriv] pivot raw index: {_tm_deriv_apply_index_pct - _tm_deriv_fetch_index_pct}')
                print(f'\t[time][deriv] process indicator weekly: {_tm_process_indicator_weekly - _tm_deriv_apply_index_pct}')
                print(f'\t[time][deriv] process indicator monthly: {_tm_process_indicator_monthly - _tm_process_indicator_weekly}')
                print(f'\t[time][deriv] process indicator join: {_tm_process_indicator_join - _tm_process_indicator_monthly}')
        _tm_derived = time.time()
        self.dts.fix_data()
        _tm_fix = time.time()

        self._is_inited = True
        self._score_manager.set_dts(self.dts)
        if score_pre_calc:
            self._score_manager.pre_calculate(is_filter_c=True,use_weekly_monthly_indicators=use_weekly_monthly_indicators)
        _tm_finish = time.time()
        print(self.dts)
        if print_time:
            print(f'[time] basic: {_tm_basic - _tm_start}')
            print(f'[time] deriv: {_tm_derived - _tm_basic}')
            print(f'[time] fix_d: {_tm_fix - _tm_derived}')
            print(f'[time] score: {_tm_finish - _tm_fix}')
            print(f'[time] total: {_tm_finish - _tm_start}')

    def set_score_param(self, score_param: FundScoreParam):
        self._score_manager.set_param(score_param)

    def get_index_pcts(self, dt):
        # jch: only pct within 7 days take effect
        INDEX_PCT_EFFECTIVE_DELAY_DAY_NUM = 7
        res = {}
        for index_id in self.dts.index_pct.columns:
            df = self.dts.index_pct[index_id]
            _filtered = df[(df.index <= dt) & (df.index >= dt - datetime.timedelta(days=INDEX_PCT_EFFECTIVE_DELAY_DAY_NUM))]
            if len(_filtered) > 0:
                res[index_id] = _filtered.iloc[-1]
        return res

    def get_index_pcts_df(self, dt):
        if dt not in self.dts.index_date_list:
            return pd.DataFrame()
        return self.dts.index_pct.loc[dt]

    def get_fund_score(self, dt, index_id, is_filter_c=True, fund_score_funcs=None) -> dict:
        return self._score_manager.get_fund_score(dt, index_id, is_filter_c, fund_score_funcs)

    def get_fund_scores(self, dt, is_filter_c=True, fund_score_funcs=None) -> dict:
        return self._score_manager.get_fund_scores(dt, self.dts.index_list, is_filter_c, fund_score_funcs)

    def get_fund_nav(self, dt):
        df = self.dts.fund_nav
        return df.loc[dt].to_dict()

    def get_fund_unit_nav(self, dt):
        df = self.dts.fund_unit_nav
        return df.loc[dt].to_dict()

    def get_fund_purchase_fees(self):
        return self.dts.fund_info.set_index('fund_id').purchase_fee.to_dict()

    def get_fund_redeem_fees(self):
        return self.dts.fund_info.set_index('fund_id').redeem_fee.to_dict()

    def get_fund_info(self):
        return self.dts.fund_info

    def get_trading_days(self):
        return self.dts.trading_days.copy()

    def get_index_price(self, dt=None):
        if dt:
            return self.dts.index_price.loc[dt]
        else:
            return self.dts.index_price.copy()

    def get_index_price_data(self, dt):
        _index_price = self.get_index_price(dt)
        return AssetPrice(**_index_price.to_dict())

    def white_and_black_list_filter(self, score, score_raw, disproved_list):
        return self._score_manager._white_and_black_list_filter(score, score_raw, disproved_list)


def test():
    # m = FundDataManager('20190101', '20200101', score_manager=FundScoreManager())
    m = FundDataManager('20190101', '20200101')
    m.init()
    print(m.get_fund_info())
    print(m.get_trading_days())
    print(m.get_fund_score(datetime.date(2019, 1, 3), 'hs300'))


if __name__ == '__main__':
    with profiled(file_name='/tmp/test.txt'):
        m = FundDataManager('20190101', '20200101', score_manager=FundScoreManager())
        m.init()
