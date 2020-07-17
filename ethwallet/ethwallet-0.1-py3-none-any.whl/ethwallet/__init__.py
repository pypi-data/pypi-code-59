from api import GetApi
from uswapper import USwapper

base = 'https://api.ethplorer.io/'


class Wallet:
    def __init__(self, key, address):

        self.a = GetApi( base, f'?apiKey={key}' )
        self.wallet = self.a.resp( 'getAddressInfo/', address )
        self.us = USwapper()

    def getethprice(self):
        return float( self.wallet['ETH']['balance'] ) * float( self.wallet['ETH']['price']['rate'] )

    def getwallet(self):

        wallet_d = {'ETH': self.getethprice()}

        for t in self.wallet['tokens']:
            symbol = t['tokenInfo']['symbol']
            p = self.us.getprice( str.upper( symbol ) )

            try:
                pot = float( t['tokenInfo']['decimals'] )
            except KeyError:
                pot = 0
                p = 0

            if symbol != 'WETH':  # TODO dirty fix since ethplorer is stuck not updating WETH value
                p = p * self.us.ethprice
                q = float( t['balance'] ) / 10 ** pot
                balance = p * q

                if balance != 0.0:
                    wallet_d[symbol] = balance

            else:
                q = 0

        return wallet_d

    def printwallet(self):

        wallet_d = self.getwallet()

        out = 'Your holdings are: '
        for s in wallet_d:
            out += '\n'
            out += f'{s}: {wallet_d[s]:.2f}$'

        out += '\n'
        out += f'Total: {sum( wallet_d.values() ):.2f}$'

        return out

    def gettotal(self):
        wallet_d = self.getwallet()
        return sum( wallet_d.values() )


if __name__ == "__main__":
    import os
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument( 'address' )
    args = parser.parse_args()

    key = os.getenv( 'ETHPLORER' )
    myw = Wallet( key, args[0] )
    myw.printwallet()
