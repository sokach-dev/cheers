import unittest

from . import api
import pybitget as Client

import utils.utilss as utilss


class TestDataAPI(unittest.TestCase):

    def test_get_api_data(self):
        config = utilss.get_config('configs/config.toml')
        exchange = config['bitget']
        c = Client.Client(exchange['ak'], exchange['sk'],
                          exchange['passphrase'])
        data_api = api.DataAPI(c)

        self.assertEqual(
            len(
                data_api.get_candles('BTCUSDT_UMCBL', '1D',
                                     utilss.get_previous_day_timestamp(),
                                     utilss.get_previous_day_timestamp())), 1)


if __name__ == '__main__':
    unittest.main()