import time
import geatpy as ea  # import geatpy
import numpy as np

from MyProblem import MyProblem
from Problem import ProblemWFunc, ProblemFunc1, ProblemFunc2

myProbUtil = MyProblem()
# 定义outFunc()函数
def everygenOut(alg: ea.Algorithm, pop: ea.Population):  # alg 和 pop为outFunc的固定输入参数，分别为算法对象和每次迭代的种群对象。
    print('第 %d 代' % alg.currentGen)
    bestIndi = pop[np.argmax(pop.FitnV)]  # 获取最优个体
    print('最好的目标函数值： %.3f ' % bestIndi.ObjV[0][0])
    print('决策变量：',end='')
    chroms = bestIndi.Phen[0]
    for i in chroms:
        print('%.3f,' % i, end='')
    f1, f2 = myProbUtil.cal_f1_f2(chroms)
    print()
    print('f1: %.3f, f2: %.3f' % (f1, f2))
    print()

'''
设置使用的问题
设置输出的文件夹
'''
runProb = "Func1"
outDir = "_Func1_"

if __name__ == '__main__':
    # 实例化问题对象
    if runProb == 'WFunc':
        problem = ProblemWFunc()
    elif runProb == 'Func1':
        problem = ProblemFunc1(priceB=[2.5, 5.5, 7.5])
    elif runProb == 'Func2':
        problem = ProblemFunc2()
    else:
        raise RuntimeError('未设置问题')
    # 构建算法
    iter_num = 50
    pop_num = 50
    algorithm = ea.soea_EGA_templet(
        problem,
        ea.Population(Encoding='RI', NIND=pop_num),
        MAXGEN=iter_num,  # 最大进化代数。
        logTras=1,  # 表示每隔多少代记录一次日志信息，0表示不记录。
        trappedValue=1e-6,  # 单目标优化陷入停滞的判断阈值。
        maxTrappedCount=10,  # 进化停滞计数器最大上限值。
        outFunc=everygenOut
    )
    # 修改变异和交叉概率
    algorithm.recOper.XOVR = 0.7  # 交叉概率
    algorithm.mutOper.Pm = 0.02  # 变异概率
    # 求解
    if problem.priceB is not None:
        priceBstr = 'priceB['+','.join(str(i) for i in problem.priceB)+']_'
    else:
        priceBstr = ''
    res = ea.optimize(algorithm,
                      verbose=True,
                      drawing=1,
                      outputMsg=True,
                      drawLog=True,
                      saveFlag=True,
                      dirName='sobj_qforx_EGA_iter' + str(iter_num) + "_pop" + str(pop_num) + outDir + priceBstr + str(time.strftime("%Y-%m-%d %Hh-%Mm-%Ss", time.localtime()))
                      )
