class Strategies:
    def __init__(self, prices, period):
        self.extracted_lst = None
        self.min_points = None
        self.max_points = None
        self.prices = prices
        self.period = period
        self.prices_length = len(self.prices)

    def find_max_in_period(self):
        self.max_points = []
        curr_period = 0
        while curr_period + self.period < self.prices_length:
            curr_lst = self.prices[curr_period:curr_period + self.period]
            max_price = max(curr_lst)
            for i in curr_lst:
                if i == max_price:
                    self.max_points.append(i)
                else:
                    self.max_points.append(None)
            curr_period += self.period

    def find_min_in_period(self):
        self.min_points = []
        curr_period = 0
        while curr_period + self.period < self.prices_length:
            curr_lst = self.prices[curr_period:curr_period + self.period]
            min_price = min(curr_lst)
            for i in curr_lst:
                if i == min_price:
                    self.min_points.append(i)
                else:
                    self.min_points.append(None)
            curr_period += self.period

    def extract_min_max(self):
        self.extracted_lst = []
        self.find_min_in_period()
        self.find_max_in_period()
        length = len(self.max_points)
        for i in range(length):
            if self.min_points[i] is not None:
                self.extracted_lst.append(self.min_points[i])
            elif self.max_points[i] is not None:
                self.extracted_lst.append(self.max_points[i])

    def find_head_shoulders_pattern(self):
        length = len(self.extracted_lst)
        if length >= 5:
            if self.extracted_lst[-1] < self.extracted_lst[-2]:
                return False
            elif self.extracted_lst[-3] < self.extracted_lst[-1]:
                return False
            elif self.extracted_lst[-4] > self.extracted_lst[-1]:
                return False
            elif self.extracted_lst[-5] < self.extracted_lst[-4] or self.extracted_lst[-5] > self.extracted_lst[-3]:
                return False

            return True

    def find_double_top(self):
        length = len(self.extracted_lst)
        if length >= 4:
            if self.extracted_lst[-1] < self.extracted_lst[-2]:
                return False
            elif self.extracted_lst[-2] > self.extracted_lst[-3]:
                return False
            elif self.extracted_lst[-4] > self.extracted_lst[-3]:
                return False
        return True
