import re
import pandas as pd
import plotly.express as px
import numpy as np


class LinearRegression():
    def __init__(self, data_path: str, columns: list) -> None:
        self.__df = pd.read_csv(data_path)
        self.data = self.__df[columns]

    def __len__(self):
        return len(self.data)

    def clean_data(self, columns: list):
        for column in columns:
            self.data.loc[:, column] = self.data[column].apply(
                self.do_type_conversions)

    def do_type_conversions(self, value):
        if type(value) != str:
            return int(value)
        value = re.split("\s+", value)
        if value[-1].upper() == "KM":
            return int("".join(value[:-1]))
        elif value[-1].upper() == "AZN":
            return float(value[0])
        elif value[-1].upper() == "$":
            return float(value[0])*1.70

    def clean_price_and_convert(self, col):
        self.data.loc[:, col] = self.data[col].apply(self.do_type_conversions)

    def get_data_copy(self):
        self.__data_copy = self.data.copy()
        return self.__data_copy.copy()

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

    def calculate_cost(self, columns, Y, W):
        X = [[1]*len(self)] + [self.data[column] for column in columns]
        self.X = np.array(X).T
        self.Y = np.array(self.data[Y])
        self.W = np.array(W)
        pred = self.X.dot(self.W)
        J = np.sum((pred-self.Y)**2)*0.5
        return J/len(self.Y)

    def gradient_descent(self, columns, Y, W, alpha=0.001, iterations=10_000) -> None:
        cost = self.calculate_cost(columns, Y, W)
        self.costH = [cost]
        for i in range(0, iterations):
            if i % 1000 == 0:
                print(f"Iteration {i}")
                print(f"Cost Function {self.costH[-1]}")
            h = self.X.dot(self.W)
            diff = h-self.Y
            g = self.X.T.dot(diff)/len(self)
            self.W = self.W-alpha*g
            self.costH.append(self.calculate_cost(columns, Y, self.W))

    def visualize_gradient_descent(self):
        fig = px.line(self.costH)
        fig.show()

    def visualize_data(self, x, y, z=None):
        if z:
            df = self.data[[x, y, z]]
            print(z)
            fig = px.scatter_3d(df, x=x, y=y, z=z)
        else:
            df = self.data[[x, y]]
            fig = px.scatter(df, x=x, y=y)

        fig.show()


linear = LinearRegression(
    "./turboaz.csv", columns=["Buraxilish ili", "Yurush", "Qiymet"])
print(linear.data)
linear.clean_price_and_convert("Qiymet")
linear.clean_data(columns=["Yurush", "Buraxilish ili"])
# linear.visualize_data(x="Yurush", y="Qiymet")
# linear.visualize_data(x="Buraxilish ili", y="Qiymet")
# linear.visualize_data(x="Buraxilish ili", y="Qiymet",z="Yurush")
linear.do_min_max_normalization(["Yurush", "Qiymet", "Buraxilish ili"])
linear.do_mean_normalization(["Yurush", "Qiymet", "Buraxilish ili"])
linear.do_z_score_normalization(["Yurush", "Qiymet", "Buraxilish ili"])
linear.gradient_descent(["Buraxilish ili", "Yurush"], "Qiymet", [0, 11, 5])
linear.visualize_gradient_descent()
