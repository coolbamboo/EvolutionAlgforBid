import time
import geatpy as ea  # import geatpy
import numpy as np

from SobjGAProb import SobjGAProb


# 定义outFunc()函数
def everygenOut(alg: ea.Algorithm, pop: ea.Population):  # alg 和 pop为outFunc的固定输入参数，分别为算法对象和每次迭代的种群对象。
    print('第 %d 代' % alg.currentGen)
    bestIndi = pop[np.argmax(pop.FitnV)]  # 获取最优个体
    print('最好的目标函数值： %d ' % bestIndi.ObjV[0][0])
    print('决策变量：')
    chroms = bestIndi.Phen[0]
    for i in chroms:
        print('%d,' % i)


if __name__ == '__main__':
    # 实例化问题对象
    problem = SobjGAProb()

    # 构建算法
    algorithm = ea.soea_EGA_templet(
        problem,
        ea.Population(Encoding='RI', NIND=50),
        MAXGEN=30,  # 最大进化代数。
        logTras=1,  # 表示每隔多少代记录一次日志信息，0表示不记录。
        trappedValue=1e-6,  # 单目标优化陷入停滞的判断阈值。
        maxTrappedCount=10,  # 进化停滞计数器最大上限值。
        outFunc=everygenOut
    )
    # 修改变异和交叉概率需要重写这个算法模版
    # 求解
    res = ea.optimize(algorithm,
                      verbose=True,
                      drawing=0,
                      outputMsg=True,
                      drawLog=False,
                      saveFlag=True,
                      dirName='sobjGA_' + str(time.strftime("%Y-%m-%d %Hh-%Mm-%Ss", time.localtime()))
                      )
    # 结果成功
    if res['success']:
        print(res['Vars'][0, 0], res['Vars'][0, 1])
