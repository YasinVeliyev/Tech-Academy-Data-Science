class Normalization:
    def do_min_max_normalization(self, columns: list):
        data = self.get_data_copy()
        for column in columns:
            data[column] = data[column].apply(lambda x: (
                x-data[column].min())/(data[column].max()-data[column].min()))
        self.data = data
    def do_mean_normalization(self, columns: list):
        data = self.get_data_copy()
        for column in columns:
            data[column] = data[column].apply(lambda x: (
                x-data[column].mean())/(data[column].max()-data[column].min()))
        self.data = data

    def do_z_score_normalization(self, columns: list):
        data = self.get_data_copy()
        for column in columns:
            mean = data[column].mean()
            standard_deviation = data[column].std()
            data[column] = data[column].apply(
                lambda x: (x-mean)/standard_deviation)
        self.data = data