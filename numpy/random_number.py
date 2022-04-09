np.random.seed(1234)            # global
rng = np.random.RandomState(1234)     # local
rng.randn(10)
np.random.rand                        # 均匀分布
np.random.randint                     # 上下限范围内的整数
np.random.randn                       # 标准正态分布
np.random.normal(size=(4, 4))         # 正态分布


np.random.binomial                    # 二项分布
np.random.beta                        # Beta分布
np.random.chisquare                   # 卡方分布
np.random.gamma                       # 伽玛分布
np.random.uniform                     # [0,1)中的均匀分布
np.random.shuffle                     # 将一个序列的顺序打散
np.random.permutation                 # 返回一个序列的随机排列
