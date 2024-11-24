import numpy as np


class MyProblem:
    def myEvalVars(self, X, priceA=None, priceB=None):  # 构建目标函数和约束条件
        x1 = X[:, [0]]
        x2 = X[:, [1]]
        x3 = X[:, [2]]
        y1 = X[:, [3]]
        y2 = X[:, [4]]
        y3 = X[:, [5]]
        if priceA is None:
            p1 = X[:, [6]]
            p2 = X[:, [7]]
            p3 = X[:, [8]]
        else:
            p1 = priceA[0]
            p2 = priceA[1]
            p3 = priceA[2]
        if priceB is None:
            q1 = X[:, [9]]
            q2 = X[:, [10]]
            q3 = X[:, [11]]
        else:
            q1 = priceB[0]
            q2 = priceB[1]
            q3 = priceB[2]

        p1_plus = np.where(p1 <= q1, p1, 0)
        p2_plus = np.where(p2 <= q2, p2, 0)
        p3_plus = np.where(p3 <= q3, p3, 0)
        q1_plus = np.where(q1 < p1, q1, 0)
        q2_plus = np.where(q2 < p2, q2, 0)
        q3_plus = np.where(q3 < p3, q3, 0)
        f1 = p1_plus * x1 + p2_plus * x2 + p3_plus * x3 - 10
        f2 = q1_plus * y1 + q2_plus * y2 + q3_plus * y3 - 15
        if self.M >= 2:
            f = np.hstack([f1, f2])  # 2维以上目标函数处理方案
        else:
            f = 0.5 * (f1 + f2) + 0.3 * f1 + 0.2 * f2  # 1维目标函数的处理
        # 采用可行性法则处理约束
        CV = np.hstack(
            [x1 + x2 - 10,
             x1 + x2 + x3 - 15,
             11 - (x1 + x2 + x3),
             y1 + y2 - 10,
             y1 + y2 + y3 - 20,
             16 - (y1 + y2 + y3),
             np.abs(x1 + x2 + x3 + y1 + y2 + y3 - 30)
             ])
        return f1, f2, CV, f

    # 初始化M（目标维数默认1）
    def __init__(self, M=1):
        self.M = M
        self.maxormins = [-1] * self.M  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        self.Dim = 12  # 初始化Dim（决策变量维数）
        self.varTypes = [1, 1, 1, 1, 1,
                         1, 0, 0, 0, 0, 0, 0]  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        self.lb = [0, 0, 1, 0, 0, 6, 2, 3, 7, 2, 5, 7]  # 决策变量下界
        self.ub = [5, 10, 15, 6, 10, 20, 8, 8, 8, 8, 8, 8]  # 决策变量上界
        self.lbin = [1] * self.Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        self.ubin = [1] * self.Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）

    '''
    对每一次的迭代结果，最好的那个染色体代表的决策变量，取得对应的目标函数值，作为当前迭代的最好的f1、f2
    '''
    def cal_f1_f2(self, chroms):
        a = np.array(chroms)  # 决策变量数组
        # 取X、Y、P、Q
        x1 = a[0]
        x2 = a[1]
        x3 = a[2]
        y1 = a[3]
        y2 = a[4]
        y3 = a[5]
        p1 = a[6]
        p2 = a[7]
        p3 = a[8]
        q1 = a[9]
        q2 = a[10]
        q3 = a[11]
        f1 = p1 * x1 + p2 * x2 + p3 * x3 - 10
        f2 = q1 * y1 + q2 * y2 + q3 * y3 - 15
        return f1, f2
