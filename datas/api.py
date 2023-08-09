import pybitget as Client


class DataAPI():

    def __init__(self, client: Client) -> None:
        self.client = client
        pass

    def get_candles(self, symbol, period, start, end):
        try:
            candles = self.client.mix_get_candles(symbol, period, start, end)
            return candles
        except Exception as e:
            print('get candles error: {}'.format(e))
