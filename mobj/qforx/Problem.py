import geatpy as ea
import numpy as np


class ProblemMul(ea.Problem):  # 继承Problem父类

    def __init__(self, M=2):  # 初始化M（目标维数2）
        name = 'qforxProblemMul'  # 多目标问题
        maxormins = [-1] * M  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 6  # 初始化Dim（决策变量维数）
        varTypes = [1, 1, 1, 1, 1,
                    1]  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [0, 0, 1, 0, 0, 6]  # 决策变量下界
        ub = [5, 10, 15, 6, 10, 20]  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [1] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self,
                            name,
                            M,
                            maxormins,
                            Dim,
                            varTypes,
                            lb,
                            ub,
                            lbin,
                            ubin)

    def evalVars(self, X):  # 目标函数
        x1 = X[:, [0]]
        x2 = X[:, [1]]
        x3 = X[:, [2]]
        y1 = X[:, [3]]
        y2 = X[:, [4]]
        y3 = X[:, [5]]
        f1 = 2 * x1 + 3 * x2 + 7 * x3 - 10
        f2 = 2 * y1 + 5 * y2 + 7 * y3 - 15
        f = np.hstack([f1, f2])
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
        return f, CV
