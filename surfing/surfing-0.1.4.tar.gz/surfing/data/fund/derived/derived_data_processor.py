
from typing import List

from .fund_score_processor import FundScoreProcessor
from .fund_indicator_processor import FundIndicatorProcessor
from .derived_index_val import IndexValProcess
from .style_analysis_processor import StyleAnalysisProcessor
from .derived_data_helper import DerivedDataHelper
from .fund_indicator_processor_weekly import FundIndicatorProcessorWeekly
from .fund_indicator_processor_monthly import FundIndicatorProcessorMonthly
from ...api.basic import BasicDataApi


class DerivedDataProcessor:
    def __init__(self):
        self._data_helper = DerivedDataHelper()
        self.fund_indicator_processor = FundIndicatorProcessor(self._data_helper)
        self.fund_indicator_processor_weekly = FundIndicatorProcessorWeekly(self._data_helper)
        self.fund_indicator_processor_monthly = FundIndicatorProcessorMonthly(self._data_helper)
        self.fund_score_processor = FundScoreProcessor(self._data_helper)
        self.index_val_processor = IndexValProcess(self._data_helper)
        self.style_analysis_processors: List[StyleAnalysisProcessor] = []
        # 暂时只算这三个universe
        for universe in ('hs300', 'csi800', 'all'):
            sap = StyleAnalysisProcessor(self._data_helper, universe)
            self.style_analysis_processors.append(sap)

    def process_all(self, start_date, end_date):
        failed_tasks = []
        failed_tasks.extend(self.fund_indicator_processor.process(start_date, end_date))
        failed_tasks.extend(self.fund_score_processor.process(start_date, end_date))
        failed_tasks.extend(self.index_val_processor.process(start_date, end_date))
        for sap in self.style_analysis_processors:
            failed_tasks.extend(sap.process(start_date, end_date))

        # 获取下一个交易日
        api = BasicDataApi()
        trading_day_df = api.get_trading_day_list(start_date=end_date)
        if trading_day_df.shape[0] <= 1:
            print(f'get trading days start with {end_date} failed')
            failed_tasks.append('get_trading_day for weekly/monthly indicator')
        else:
            next_trading_day = trading_day_df.iloc[1, :].datetime
            print(f'got next trading day {next_trading_day}')
            failed_tasks.extend(self.fund_indicator_processor_weekly.process(start_date, end_date, next_trading_day))
            failed_tasks.extend(self.fund_indicator_processor_monthly.process(start_date, end_date, next_trading_day))
        return failed_tasks

    def get_updated_count(self):
        return self._data_helper._updated_count


if __name__ == '__main__':
    ddp = DerivedDataProcessor()
    start_date = '20200605'
    end_date = '20200605'
    # ddp.process_all(start_date, end_date)
    # ddp.fund_indicator_processor.process(start_date, end_date)
    # ddp.fund_score_processor.process(start_date, end_date)
    # import pandas as pd
    # date_list = pd.date_range(end='2010-05-31', periods=65, freq='M').sort_values(ascending=False).to_pydatetime()
    # for date in date_list:
    #     date = date.strftime('%Y%m%d')
    #     ddp.fund_indicator_processor_monthly.process(date, date)
