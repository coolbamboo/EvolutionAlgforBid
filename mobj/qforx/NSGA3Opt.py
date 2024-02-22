import time

import geatpy as ea  # import geatpy
import numpy as np

from Problem import ProblemMul

# 定义outFunc()函数
def everygenOut(alg: ea.Algorithm, pop: ea.Population):  # alg 和 pop为outFunc的固定输入参数，分别为算法对象和每次迭代的种群对象。
    print('第 %d 代' % alg.currentGen)
    bestIndi = pop[np.argmax(pop.FitnV)]  # 获取最优个体
    print('最好的目标函数值： (1)%d, (2)%d' % (bestIndi.ObjV[0][0], bestIndi.ObjV[0][1]))
    print('决策变量：')
    chroms = bestIndi.Phen[0]
    for i in chroms:
        print('%d,' % i, end='')

'''
设置使用的问题
设置输出的文件夹
'''
runProb = "Mul"
outDir = "Mul"

if __name__ == '__main__':
    # 实例化问题对象
    if runProb == 'Mul':
        problem = ProblemMul()
    else:
        raise RuntimeError('未设置问题')

    # 构建算法
    algorithm = ea.moea_NSGA3_templet(
        problem,
        ea.Population(Encoding='RI', NIND=50),
        MAXGEN=200,  # 最大进化代数。
        logTras=1,  # 表示每隔多少代记录一次日志信息，0表示不记录。
        outFunc=everygenOut
    )
    # 修改变异和交叉概率需要重写这个算法模版
    # 求解
    res = ea.optimize(algorithm,
                      verbose=True,
                      drawing=1,
                      outputMsg=True,
                      drawLog=False,
                      saveFlag=True,
                      dirName='mobj_qforx_NSGA3_'+ outDir + str(time.strftime("%Y-%m-%d %Hh-%Mm-%Ss", time.localtime()))
                      )
