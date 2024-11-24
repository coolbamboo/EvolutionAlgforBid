import geatpy as ea
import numpy as np

from MyProblem import MyProblem


class ProblemMul(ea.Problem):  # 继承Problem父类

    def __init__(self, M=2):  # 初始化M（默认目标维数2）
        self.M = M
        name = 'qforxProblemMul'  # 多目标问题的名称
        mp = MyProblem(M=self.M)
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self,
                            name,
                            mp.M,
                            mp.maxormins,
                            mp.Dim,
                            mp.varTypes,
                            mp.lb,
                            mp.ub,
                            mp.lbin,
                            mp.ubin)

    def evalVars(self, X):  # 目标函数
        mp = MyProblem(M=self.M)
        f1, f2, CV, f = mp.myEvalVars(X)
        return f, CV
