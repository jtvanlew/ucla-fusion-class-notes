import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

filename0 = 'Be-n2n.txt'
filename1 = 'Be-nalpha.txt'


n2n  = pd.read_csv(filename0, header = 1, delim_whitespace=True)
nalpha = pd.read_csv(filename1, header = 1, delim_whitespace=True)


ax = n2n.plot(x='Energy(eV)', y='XS(b)', label=r'$n-2n$', logx=True, logy=True, linewidth=2)
nalpha.plot(ax = ax, x='Energy(eV)', y='XS(b)', label=r'$n-\alpha$', logx=True, logy=True, linewidth=2)
ax.set_ylabel('Cross-section (barns)')
plt.show()