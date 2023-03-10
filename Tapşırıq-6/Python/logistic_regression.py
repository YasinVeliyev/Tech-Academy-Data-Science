import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("exams.csv")
data = df.copy()


def do_min_max_normalize(data, col):
    data[col] = (data[col]-data[col].min())/(data[col].max()-data[col].min())


def do_z_score_normalize(data, col):
    data[col] = (data[col]-data[col].mean())/data[col].std()


do_min_max_normalize(data, "exam_1")
do_min_max_normalize(data, "exam_2")

x0 = np.ones(len(data))
X = np.array([x0, data["exam_1"], data["exam_2"]])
Y = data["admitted"]
W = np.array([0, 1, 2])
X = X.T


def sigmoid(X, W):
    z = np.dot(X, W)
    return 1/(1+np.e**-z)


def gradientDescent(X, Y, W, alpha=0.05, iteration=10_000):
    costH = []
    for i in range(iteration+1):

        H = sigmoid(X, W)
        g = np.dot(X.T, H-Y)/len(Y)
        W = W-alpha*g

        J = (-Y*np.log(H)-(1-Y)*np.log(1-H)).mean()
        costH.append(J)

        if i % 1000 == 0:
            print(f"Iteration {i}")
            print(J)
    return costH, W


def decision_boundary(y=0):
    plt.ylabel("Exam_2")
    plt.xlabel("Exam_1")

    plt.scatter(data[data["admitted"] == 1]["exam_1"],
                data[data["admitted"] == 1]["exam_2"], color="#006629")

    plt.scatter(data[data["admitted"] == 0]["exam_1"],
                data[data["admitted"] == 0]["exam_2"], color="#b50404")

    xline = [data["exam_1"].min(), data["exam_1"].max()]
    if y == 0:
        yline = -(Wn[0] + np.dot(Wn[1], xline))/Wn[2]
    else:
        yline = (1-(Wn[0] + np.dot(Wn[1], xline)))/Wn[2]
    plt.plot(xline, yline)
    plt.show()


def calculate_precision(df, actual, predicted):
    tp = len(df[(df[actual] == 1) &
                (df[predicted] == 1)])
    fp = len(df[(df[actual] == 0) & (
        df[predicted] == 1)])
    return tp/(tp+fp)


def calculate_recall(df, actual, predicted):
    tp = len(df[(df[actual] == 1) &
                (df[predicted] == 1)])
    fn = len(df[(df[actual] == 1) &
                (df[predicted] == 0)])
    return tp/(fn+tp)


costH, Wn = gradientDescent(X, Y, W.copy())
# plt.plot(costH)
# plt.show()
P = sigmoid(X, Wn)
P[P < 0.5] = 0
P[P >= 0.5] = 1


compareDf = pd.DataFrame(P)
compareDf.columns = ["Prediction"]
compareDf["admitted"] = data["admitted"].copy()
# decision_boundary(1)
print(
    f"True Positive: {len(compareDf[(compareDf['admitted'] == 1) &(compareDf['Prediction'] == 1)])}")

print(
    f"True Negative: {len(compareDf[(compareDf['admitted'] == 0) &(compareDf['Prediction'] == 0)])}")


print(
    f"False Positive: {len(compareDf[(compareDf['admitted'] == 0) &(compareDf['Prediction'] == 1)])}")

print(
    f"False Negative: {len(compareDf[(compareDf['admitted'] == 1) &(compareDf['Prediction'] == 0)])}")


print(
    f"Precision: {calculate_precision(compareDf,actual='admitted',predicted ='Prediction' )}")
print(
    f"Recall: {calculate_recall(compareDf,actual='admitted',predicted ='Prediction')}")
