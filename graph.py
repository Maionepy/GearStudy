import scipy.io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mat_nofault = scipy.io.loadmat('Gearbox_no_fault_full_load_01_December_2009_10kHz_pos1.mat')
mat_chipped_tooth  = scipy.io.loadmat('Gearbox_a_chipped_tooth_full_load_03_December_2009_10kHz_pos1.mat')

mat_nofault = mat_nofault['acc']
df_nofault = pd.DataFrame({'Vibration': mat_nofault[:, 0]})
df_nofault['time'] = df_nofault.index/10000
plt.scatter(df_nofault.time, df_nofault.Vibration,marker='.', s=1, color='b', linewidths=0)
plt.title('Plot of Gearbox with No Fault')
plt.xlabel('Time [s]')
plt.ylabel('Vibration Signal')
plt.show()
max_nofault = df_nofault.loc[df_nofault['Vibration'].idxmax()]
print('Here we have our extreme incident:')
print(max_nofault)

mat_chipped_tooth = mat_chipped_tooth['acc']
df_chipped_tooth = pd.DataFrame({'Vibration': mat_chipped_tooth[:, 0]})
df_chipped_tooth['time'] = df_chipped_tooth.index/10000
plt.scatter(df_chipped_tooth.time, df_chipped_tooth.Vibration,marker='.', s=1, color='g', linewidths=0)
plt.title('Plot of Gearbox with a Chipped Tooth')
plt.xlabel('Time [s]')
plt.ylabel('Vibration Signal')
plt.show()
max_chipped_tooth = df_chipped_tooth.loc[df_chipped_tooth['Vibration'].idxmax()]
print('Here we have our extreme incident:')
print(max_chipped_tooth)
