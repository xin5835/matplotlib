# 箭头和标注
plt.plot([1,1], [0,3], 'r--', linewidth=2)
plt.annotate(r'$2x+1$', xy=(1,3), xycoords='data', xytext=(+40, -20),textcoords='offset points',
             arrowprops=dict(arrowstyle="->",color='b', connectionstyle='arc3, rad=0.2'))

plt.text(0.97,2, r'$this\ is\ apple\ \mu$', color='r')

plt.xticks(())
