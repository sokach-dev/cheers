from math import log
import tomllib
import logging
import pybitget as Client
from utils import get_logger
import argparse

import utils


def run(exchange, symbol, marginCoin, debug_mode):
    client = Client(exchange['ak'], exchange['sk'], exchange['passphrase'])

    orders = client.mix_get_plan_order_tpsl(symbol, isPlan='plan')['data']
    # 初始化订单状态

    while True:
        try:
            marketPrice = client.mix_get_market_price(symbol)
            current_price = float(marketPrice['data']['markPrice'])
            logger.info('current price: {}'.format(current_price))
        except Exception as e:
            logger.error('get market price error: {}'.format(e))
            continue
        pass


if __name__ == "__main__":
    logger = get_logger()
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--exchange', help='exchange name')
    parser.add_argument('-c',
                        '--config',
                        help='config file',
                        default='configs/config.toml')
    parser.add_argument('-d',
                        '--debug_mode',
                        help='debug mode',
                        action='store_true',
                        default=False)

    args = parser.parse_args()
    exchange = args.exchange
    debug_mode = args.debug_mode

    config = utils.get_config(args.config)

    logger.debug('config: {}'.format(config))
    symbol = 'BTCUSDT_UMCBL'
    marginCoin = 'USDT'
    logger.info('run debug mode: {}'.format(debug_mode))

    run(config[exchange], symbol, marginCoin, debug_mode)
