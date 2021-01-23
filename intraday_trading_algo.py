import pandas as pd

class basicAlgo:

    @staticmethod
    def resample(x):
        principle = 1000
        og_principle = principle

        ticker = 'tsla'.upper()
        df = pd.read_csv('tsla_1_min.csv', parse_dates=['Datetime'], index_col='Datetime')
        df = df.resample(x).agg(
        {'Close': 'last',
         'High': 'max',
         'Low': 'min',
         'Open': 'first',
         'Volume': 'sum'}).dropna()
        buy = []
        sell = []

        def algo():
            pos = 0
            for i in range(0, len(df.index)):

                five_ema = df.Close.ewm(span=5, adjust=False).mean()[i]
                nine_ema = df.Close.ewm(span=9, adjust=False).mean()[i]
                high = df['High'][i]
                close = df['Close'][i]
                current_vol = df['Volume'][i]

                if high > five_ema and pos == 0 and current_vol > df['Volume'][i - 1]:
                    pos = 1
                    buying_price = close
                    buy.append(buying_price)
                    print('--buying {} at'.format(ticker), close)

                elif pos == 1 and close > five_ema:
                    print('holding {} at'.format(ticker), close)

                elif close < nine_ema and pos == 1:
                    pos = 0
                    selling_price = close
                    sell.append(selling_price)
                    # print('**Exit: ', selling_price.round(2), ' || lock in profit')
                    print('--selling {} at'.format(ticker), close)

            def math():
                principle = 1000
                og_principle = principle
                if len(buy) - 1 == len(sell):
                    if len(buy) != len(sell):
                        del buy[-1]
                else:
                    pass

                wins = []
                losses = []
                percent_change = []
                for user_mpl in range(len(buy)):
                    deci_pc = ((sell[user_mpl] - buy[user_mpl]) / buy[user_mpl])
                    percent_change.append(deci_pc)
                    pc = ((sell[user_mpl] - buy[user_mpl]) / buy[user_mpl]) * 100
                    if pc < 0:
                        losses.append(pc)
                    else:
                        wins.append(pc)
                print('Wins:', len(wins))
                print('Losses: ', len(losses))

                # from algo
                total_pc_change = []
                for y in range(0, len(percent_change)):
                    new_principle = principle + (principle * percent_change[y])
                    principle = new_principle
                    total_pc_change.append(new_principle)

                print('Algo trading ', ticker, 'turned ', og_principle, "into: ", total_pc_change[-1].round(2),
                      '(only long trades)')
            math()
        algo()

time_frame = input('enter time frame to backtest on')
y = basicAlgo()
y.resample(time_frame)