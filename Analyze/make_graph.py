import matplotlib.pyplot as plt
import matplotlib


def make_graph_presidents(presidents, value, y_label, title):
    fig = plt.figure()
    plot = plt.subplot()
    plot.bar(presidents, value)
    plot.set_ylabel(y_label)
    plot.set_title(title)
    fig.savefig("results\\" + title + ".png")


def make_graph_economy(presidents, value):
    datas = { \
        "이승만" : 5.3, \
        "박정희" : 10.1, \
        "전두환" : 8.5, \
        "노태우" : 9, \
        "김영삼" : 7.8, \
        "김대중" : 5.2, \
        "노무현" : 4.5, \
        "이명박" : 3.2, \
        "박근혜" : 3 \
        }
    x = []
    y = []
    for i in range(len(presidents)):
        try:
            if datas[presidents[i]]:
                check = True
            x.append(value[i])
            y.append(datas[presidents[i]])
        except:
            pass
    fig = plt.figure()
    plot = plt.subplot()
    
    tmp = []
    for i in range(len(x)):
        tmp.append([x[i], y[i]])
    tmp.sort()
    x_set = []
    y_set = []
    for a, b in tmp:
        x_set.append(a)
        y_set.append(b)
    
    plot.plot(x_set, y_set)
    plot.set_xlabel("감성점수")
    plot.set_ylabel("경제 성장률")
    plot.set_title("역대 정부(현 정부 제외)에 대한\n뉴스 제목 감성점수와 경제성장률 비교")
    fig.savefig("results\\뉴스 제목 감성점수와 경제성장률 비교.png")


if __name__ == "__main__":
    data = [1.8, -0.12, 0.0, 0.33, 0.11, -0.12, -0.5, 0.0, -1.0, 0.5]
    presidents = ["이승만", "박정희", "전두환", "노태우", "김영삼", "김대중", "노무현", "이명박", "박근혜", "문재인"]
    make_graph_economy(presidents, data)