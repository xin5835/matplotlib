x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))
plt.ylim((-2, 3))

# 设置坐标轴刻度
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)

# 设置刻度的标签
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])


# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none') # 取消右边坐标轴
ax.spines['top'].set_color('none')  # 取消上边坐标轴

ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0)) # 将下方坐标轴移至0点


ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))  # 将左方坐标轴移至0点


plt.xticks(())  # 不显示x坐标轴刻度

plt.show()
