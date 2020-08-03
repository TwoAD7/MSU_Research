import automation4LISE as a4l 
import pandas as pd
import numpy as np 
import os 
import matplotlib.pyplot as plt
from matplotlib  import cm
import seaborn as sns

#interface to the automation script

def main():
	
	print("Beginning the automation for LISE++...")
	res = input("Are you opening the program for the first time? (yes or no) ")
	if res == "yes":
		FP_slit_width,isotope_start,isotope_end,wedge_range=a4l.start()  
	else:
		FP_slit_width,isotope_start,isotope_end,wedge_range=a4l.start2()
	a4l.isotope_tuning_values(FP_slit_width,isotope_start,isotope_end,wedge_range)
	
main()
