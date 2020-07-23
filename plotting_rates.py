import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

barWidth = 0.25
plt.figure(figsize=(7,7)) 
# set height of bar
intensity_NSCL = [1.78e4,2.92e3, 4.01e2,52.9,6.22,.654,.0642,8.11e-4] #32,33,34,35,36,37
intensity_FRIB = [2.27e6,3.6e5 ,4.44e4,7.45e3,9.32e2, 5.33e1,9.75,.114]
intensity_FRIB_online = [1.79e6,2.97e5 ,4.41e4,6.05e3,7.88e2, 9.85e1,13.1,.232]

# Set position of bar on X axis
r1 = np.arange(len(intensity_NSCL))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

 
# Make the plot
plt.bar(r1,intensity_NSCL, color='#ff0000', width=barWidth, edgecolor='white', label='NSCL')
plt.bar(r2, intensity_FRIB, color='#4B8BBE', width=barWidth, edgecolor='white', label='FRIB')
plt.bar(r3, intensity_FRIB_online, color='#2d7f5e', width=barWidth, edgecolor='white', label='FRIB Online')
 
# Add xticks on the middle of the group bars
plt.xlabel('Isotopes',fontweight='bold',fontsize=15)
plt.ylabel('log(Intensity)', fontweight='bold',fontsize=15)
plt.title("Intensities for Mg 32 - Mg 40 comparison between NSCL/FRIB",fontsize=20)
plt.xticks([r + barWidth for r in range(len(intensity_NSCL))], ['Mg_32', 'Mg_33', 'Mg_34',"Mg_35","Mg_36","Mg_37","Mg_38","Mg_40"],fontsize=15)

plt.yscale('log',basey=10)
 
# Create legend & Show graphic
plt.legend()
plt.savefig("Intensity_comparison_NSCL_FRIB.png")
plt.show()
