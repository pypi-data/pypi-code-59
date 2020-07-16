from ViyaCasual.Casual import Casual
from ViyaCasual.Database import MSSQLConnector
from ViyaCasual.CAS.CASTableBase import CASTableBase
import pandas as pd


class WarehouseConnector(MSSQLConnector):
    server = 'datawarehouse.boddienoell.com'
    username = 'python1'
    password = 'Cb7Ampdpnq'
    driver = '/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.1.so.9.2'


casual = Casual(server='reports.boddienoell.com', username='willhaley', password='wi1587ha',
                db_conn=WarehouseConnector())
casual.viya.get_library_details()
pass