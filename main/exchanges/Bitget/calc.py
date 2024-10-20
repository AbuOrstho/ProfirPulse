import json


class OrderCalculator:
    class OrderCalculator:
        """
        Класс для вычисления количества ордеров на покупку и продажу, необходимых для выполнения торговых операций
        на сумму money, исходя из текущих данных рыночных заявок (asks и bids).

        :param data: Словарь с данными о рыночных заявках, включает информацию о заявках на покупку и продажу,
                     а также об инструменте и других метаданных.

        :type data: Dict

        :method calculate_asks: Вычисляет количество заявок (ордеров) на покупку и среднюю цену для покупки на указанную
                                сумму денег (money).

        :param money: Сумма денег, на которую необходимо рассчитать покупку
        :type money: float

        :return: Выводит количество ордеров, необходимых для покупки на указанную сумму, и среднюю цену этих ордеров.

        :method calculate_bids: Вычисляет количество заявок (ордеров) на продажу и среднюю цену для продажи на указанную
                                сумму денег (money).

        :param money: Сумма денег, на которую необходимо рассчитать продажу
        :type money: float

        :return: Выводит количество ордеров, необходимых для продажи на указанную сумму, и среднюю цену этих ордеров.
        """

    def __init__(self, data):
        self.data_info = data.get('data', None)
        self.data_arg = data.get('arg', None)
        self.instType = self.data_arg.get('instType', None)
        self.channel = self.data_arg.get('channel', None)
        self.coin_name = self.data_arg.get('instId', None)

        self.asks = self.data_info[0].get('asks', None)
        self.bids = self.data_info[0].get('bids', None)
        self.checksum = self.data_info[0].get('checksum', None)
        self.ts = self.data_info[0].get('ts', None)

    def calculate_asks(self, money):
        asks_sum_order = 0
        asks_price = 0
        asks_x = 0

        for ask in self.asks:
            if asks_sum_order < money:
                asks_x += 1
                asks_sum_order += float(ask[0]) * float(ask[1])
                asks_price += float(ask[0])
            elif asks_sum_order >= money:
                avg_price = asks_price / asks_x if asks_x > 0 else 0
                print(
                    f'Для покупки {self.coin_name} на {money}$ потребуется {asks_x} ордеров, которые в сумме дают {asks_sum_order}$'
                    f' по средней цене {avg_price}$')
                break

    def calculate_bids(self, money):
        bids_sum_order = 0
        bids_price = 0
        bids_x = 0

        for bid in self.bids:
            if bids_sum_order < money:
                bids_x += 1
                bids_sum_order += float(bid[0]) * float(bid[1])
                bids_price += float(bid[0])
            elif bids_sum_order >= money:
                avg_price = bids_price / bids_x if bids_x > 0 else 0
                print(
                    f'Для продажи {self.coin_name} на {money}$ потребуется {bids_x} ордеров, которые в сумме дают {bids_sum_order}$'
                    f' по средней цене {avg_price}$')
                break


# Пример использования класса:

with open('data.json', 'r') as file:
    data = json.load(file)

calculator = OrderCalculator(data)
calculator.calculate_asks(10000)
calculator.calculate_bids(10000)
