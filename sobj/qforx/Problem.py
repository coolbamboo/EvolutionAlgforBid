import geatpy as ea
import numpy as np

from MyProblem import MyProblem


class ProblemWFunc(ea.Problem):  # 继承自定义Problem类

    def __init__(self):
        mp = MyProblem()
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self,
                            'qforxProblemWeightFunc',
                            1,
                            mp.maxormins,
                            mp.Dim,
                            mp.varTypes,
                            mp.lb,
                            mp.ub,
                            mp.lbin,
                            mp.ubin)

    def evalVars(self, X):  # 目标函数
        mp = MyProblem()
        f1, f2, CV, f = mp.myEvalVars(X)
        return f, CV


class ProblemFunc1(ea.Problem):  # 继承Problem父类

    def __init__(self, priceB=None):
        name = 'qforxProblemFunc1'  # A公司的盈利作为单目标函数
        M = 1  # 初始化M（目标维数）
        if priceB is not None:
            self.priceB = priceB
        else:
            self.priceB = None
        mp = MyProblem()
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self,
                            name,
                            M,
                            mp.maxormins,
                            mp.Dim,
                            mp.varTypes,
                            mp.lb,
                            mp.ub,
                            mp.lbin,
                            mp.ubin)

    def evalVars(self, X):  # 目标函数
        mp = MyProblem()
        f1, f2, CV, f = mp.myEvalVars(X, priceB=self.priceB)
        return f1, CV


class ProblemFunc2(ea.Problem):  # 继承Problem父类

    def __init__(self):
        name = 'qforxProblemFunc2'  # B公司的盈利作为单目标函数
        M = 1  # 初始化M（目标维数）
        mp = MyProblem()
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self,
                            name,
                            M,
                            mp.maxormins,
                            mp.Dim,
                            mp.varTypes,
                            mp.lb,
                            mp.ub,
                            mp.lbin,
                            mp.ubin)

    def evalVars(self, X):  # 目标函数
        mp = MyProblem()
        f1, f2, CV, f = mp.myEvalVars(X)
        return f2, CV
