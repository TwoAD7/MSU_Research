import automation4LISE as a4l 
import pandas as pd
import numpy as np 
import os 
import matplotlib.pyplot as plt
from matplotlib  import cm
import seaborn as sns

#file that contains the interface to the automation 

def main():
	
	print("Beginning the automation for LISE++...")
	res = input("Are you opening the program for the first time? (yes or no) ")
	if res == "yes":
		bool_val,FP_slit_width,isotope_start,wedge_range=a4l.start() #NEED TO UPDATE TO INCLUDE ISOTOPE_END
	else:
		bool_val,FP_slit_width,isotope_start,isotope_end,wedge_range=a4l.start2()
	#a4l.show_pixels()
	#a4l.FP_slit_X_transmission_percent()
	#a4l.start()
	#a4l.set_projectile("Ca",48,67)
	#a4l.set_fragment("Al",22)
	#a4l.get_thickness()
	#a4l.save()
	#a4l.isotope_loop()
	#a4l.get_intensity("Mg_35","Ar",36)
	a4l.isotope_tuning_values(bool_val,FP_slit_width,isotope_start,isotope_end,wedge_range)
	#a4l.purity_percent("Mg_36")
	#a4l.set_I2_wedge(2300)
main()
