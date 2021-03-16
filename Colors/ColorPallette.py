import matplotlib.pyplot as plt

#Set Default colors for charts
LP_Blue = '#3DB3B5'
LP_BlueGreen = '30AAAF'
LP_Green = '#2A9282'
LP_Pink = '#E66CA6'
LP_Red = '#EB3893'
LP_Gold = '#ECBF46'
color_list = [LP_Blue, LP_BlueGreen, LP_Green, LP_Pink, LP_Red, LP_Gold]
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)