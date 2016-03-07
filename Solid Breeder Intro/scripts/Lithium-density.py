import numpy as np
import matplotlib.pyplot as plt
color_idx = [[0./255,107./255,164./255], 
             [255./255, 128./255, 14./255], 
             [171./255, 171./255, 171./255], 
             [89./255, 89./255, 89./255],
             [44./255, 160./255, 44./255],
             [95./255, 158./255, 209./255],
             [200./255, 82./255, 0./255],
             [255./255, 152./255, 150./255]]


Limm = 6.941
Zrmm = 91.224
Almm = 26.981539
Timm = 47.867
Simm = 28.0855
Omm = 15.9994

A = {}
A['lio'] = {}
A['liz'] = {}
A['lit'] = {}
A['lis'] = {}
A['lial'] = {}

A['lio']['mol_mass'] = 2*Limm + Omm
A['liz']['mol_mass'] = 2*Limm + Zrmm + 3*Omm
A['lit']['mol_mass'] = 2*Limm + Timm + 3*Omm
A['lis']['mol_mass'] = 4*Limm + Simm + 4*Omm
A['lial']['mol_mass'] = Limm + Almm + 2*Omm

A['lio']['num'] = 2
A['liz']['num'] = 2
A['lit']['num'] = 2
A['lis']['num'] = 4
A['lial']['num'] = 1

A['lio']['density'] = 2.013
A['liz']['density'] = 4.15
A['lit']['density'] = 3.43
A['lis']['density'] = 2.326
A['lial']['density'] = 2.615

A['lio']['Tmelt'] = 1706
A['liz']['Tmelt'] = 1888
A['lit']['Tmelt'] = 1806
A['lis']['Tmelt'] = 1523
A['lial']['Tmelt'] = 1883

A['lio']['name'] = r"Li$_2$O"
A['liz']['name'] = r"Li$_2$ZrO$_3$"
A['lit']['name'] = r"Li$_2$TiO$_3$"
A['lis']['name'] = r"Li$_4$SiO$_4$"
A['lial']['name'] = r"LiAlO$_2$"

NA = 6.022e23
NLi = np.zeros(len(A))


# #fig, ax1 = plt.subplots()
# #ax1.set_ylim([1000, 2000])
# plt.ylabel("Melt Temperature (K)")
plt.ylabel(r"Lithium atom density $\times 10^{-23}$ (#/cm$^3$)")
#ax2.set_ylim([0, 1])
x_ticks = []
for i, key in enumerate(A):
	#ax1.scatter(i, A[key]['Tmelt']*0.6, color = color_idx[0], s = 40)
	NLi[i] = (A[key]['density']*NA/A[key]['mol_mass'])*A[key]['num']/10**23
	plt.bar(i, NLi[i], color = color_idx[0], align='center')
	x_ticks.append(A[key]['name'])
# for tl in ax1.get_yticklabels():
#     tl.set_color(color_idx[0])
# for tl in ax2.get_yticklabels():
#     tl.set_color(color_idx[1])
x = range(len(A))
plt.xticks(x, x_ticks)#, rotation='vertical')
plt.grid('on', 'both')
plt.show()