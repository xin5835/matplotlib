np.zeros(10)                # 创建10个0，一维
np.zeros((2, 3))            # 创建0，2行3列
np.zeros((2, 3, 2))         # 创建0，第一个2，表示分为2堆，3行2列
np.empty((2, 3, 2))
np.arange(1,10, 2)        # arange 是python内置range的数组版，生成的是一个步长为2的序列
np.linspace(1,10,4)        # 1--10个数生成4个数，均匀分成三段
np.eye((2, 3))
np.identity((3, 3))
