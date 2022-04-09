# np.save & np.load

arr = np.arange(10)

np.save('some_array', arr)
np.load('some_array.npy')
np.savez('array_archive.npz', a=arr, b=arr)    # 将多个数组保存到一个未压缩文件中

arch = np.load('array_archive.npz')            # 加载npz文件
np.savez_compressed('array_achieve.npz', a=arr, b=arr)    # 将多个数组保存到一个压缩文件中
