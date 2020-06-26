import time
import pyautogui as pag 
import json 
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import pyperclip as pc 
import pandas as pd 
#import numpy as np
import csv
import xlrd 

pag.PAUSE=1
pag.FAILSAFE=True
width, height = pag.size()
print(f"Scren size is: {width},{height}")


#put the path to my desktop to reduce amounts of click
def txt2csv(path): 
	with open(path, 'r') as in_file:
		stripped = (line.strip() for line in in_file)	#get rid of any spaces (by default)
		lines = (line.split() for line in stripped if line) 
		with open('junk.csv', 'w') as out_file:
			writer = csv.writer(out_file)
			writer.writerows(lines) #write each line


#pixel locations for each isotope based on my screen (Resolution: 1536x864)
pixel_locations = { "Mg_32":{"x":1121,"y":626},"Mg_33":{"x":1116,"y":626},\
"Mg_34":{"x":1116,"y":626} ,"Mg_35":{"x":1116,"y":626},"Mg_36":{"x":1136,"y":626},\
"Mg_37":{"x":1116,"y":626},"Mg_38":{"x":1116,"y":626},"Mg_40":{"x":1824,"y":626}}

#array of maps
isotope_info = [ \
{"isotope":"Mg_32", "data":0.0}, \
{"isotope":"Mg_33","data":0.0},  \
{"isotope":"Mg_34","data":0.0},  \
{"isotope":"Mg_35","data":0.0},  \
{"isotope":"Mg_36","data":0.0},  \
{"isotope":"Mg_37","data":0.0},  \
{"isotope":"Mg_38","data":0.0},  \
{"isotope":"Mg_40","data":0.0}   ]

#dictionary of dictionary
beam_info = {"O_16": {"Energy":150,"Intensity":175}, "O_18":{"Energy":120,"Intensity":150},\
"Ne_20": {"Energy":170,"Intensity":80},"Ne_22":{"Energy":150,"Intensity":100},  \
"Mg_24":{"Energy":170,"Intensity":60},"Si_28":{"Energy":160,"Intensity":10},   \
"S_32" : {"Energy":150,"Intensity":60}, "Ar_36":{"Energy":150,"Intensity":75}, \
"Ca_40":{"Energy":140,"Intensity":50}, "Ca_48":{"Energy":90,"Intensity":15},   \
"Ca_48":{"Energy":140,"Intensity":80}, "Ni_58":{"Energy":160,"Intensity":20},\
"Ni_64":{"Energy":140,"Intensity":7}, "Ge_76":{"Energy":130,"Intensity":25}
}


#Didn't include the rest of the beam list, intensity was too low.
"""
,   \
"Se_82":{"Energy":140,"Intensity":45}, "Kr_78":{"Energy":150,"Intensity":25},  \
"Kr_86":{"Energy":100,"Intensity":15},"Zr_96":{"Energy":120,"Intensity":3},    \
"Mo_92":{"Energy":140,"Intensity":10}, "Sn_112":{"Energy":120,"Intensity":4},  \
"Sn_124":{"Energy":120,"Intensity":1.5} #incomplete but enough for our purposes
 } 

"""


def start():
	x,y=pag.center(pag.locateOnScreen("LISE++.png")) #find the app based on a picture, then
	pag.moveTo(x,y)									 #return coordinates for the cetner 
	pag.doubleClick()								
	time.sleep(2.5)
	pag.moveTo(18,44) #file
	pag.doubleClick()
	pag.dragTo(112, 257,.5) #configuration
	pag.click(interval=.5) 
	pag.moveTo(398,251) #load
	pag.click(interval=.5)
	pag.moveTo(154,326) #textbox
	pag.click()
	pag.write("NSCL")
	pag.moveTo(471,323) #Open button
	pag.click()
	pag.moveTo(95,213) #A1900 file 
	pag.click()
	pag.moveTo(471,323) #Open button
	pag.click()
	flag = True #to indicate it has been opened	

def set_projectile(projectile_name,energy,intensity,A):
	print("Setting projectile...")
	pag.moveTo(16,124) #projectile button 
	pag.click()
	pag.moveTo(262,213) #element text box
	pag.doubleClick()
	pag.write(projectile_name)
	pag.moveTo(231,211) # The mass number box
	pag.doubleClick()
	pag.write(A)
	pag.moveTo(519,213) #energy
	pag.doubleClick()
	pag.write(str(energy))
	pag.moveTo(523,421) #beam intensity 
	pag.doubleClick()
	pag.write(str(intensity))
	pag.moveTo(269,445)
	pag.click()
	time.sleep(1)

def tune_spectrometer():
	print("Tuning spectrometer...")
	pag.moveTo(335,78)
	pag.click()
	time.sleep(1)

def set_fragment(fragment,A):
	print("Setting fragment...")
	pag.moveTo(20,170) #projectile button 
	pag.click()
	pag.moveTo(250,463) #element text box
	pag.doubleClick()
	#pag.press("delete")
	pag.write(str(A))
	pag.moveTo(309,470) #element text box
	pag.doubleClick()
	#pag.press("delete")
	pag.write(fragment)
	pag.moveTo(624,521) #energy
	pag.click()
	time.sleep(1)

def get_thickness():
	print("Retrieving thickness...")
	pag.moveTo(453,38) #calculations 
	pag.click()
	pag.dragTo(504, 151,.5) #Optimum target
	time.sleep(.6)
	pag.moveTo(381,485) # first ok 
	pag.click()
	pag.moveTo(326,655) # second ok 
	pag.click()
	time.sleep(15)
	pag.moveTo(260,451) #load thickness
	pag.click()
	pag.moveTo(1629,160) #exit first plot
	pag.click()
	pag.moveTo(1600,93) #exit second plot
	pag.click()
	pag.moveTo(24,196) #target button 
	pag.click()
	pag.moveTo(477,286) #box containing info 
	pag.doubleClick()
	pag.hotkey('ctrl' , 'c') #copy 
	thickness = pc.paste() #paste it to a variable 
	print(f"Thickness is {thickness} microns")
	"""
	for i,m in enumerate(isotope_info):
		if isotope_info[i]["isotope"] == isotope_select:
			isotope_info[i]["thickness"] = s
			iso_name, iso_t = isotope_info[i]["isotope"] , isotope_info[i]["thickness"]
			print(iso_name,iso_t)
	"""
	pag.moveTo(456,459) #ok button to close
	pag.click()
	return thickness 

def get_intensity(isotope,beam_element,beam_mass):
	flag = False
	print(isotope)
	#get pixel location of isotope on screen
	print("Retrieving intensity...")
	x = pixel_locations[isotope]["x"]
	y = pixel_locations[isotope]["y"]
	#print(x,y)
	pag.position()
	pag.moveTo(x,y)
	pag.click(button="right")
	pag.moveTo(1483,417) #File save button 
	pag.click()
	pag.moveTo(532,121) #drop down 
	pag.click()
	pag.press("d",presses=2,interval=1)
	pag.press("enter")
	pag.moveTo(531,339) #file save text box
	pag.click()
	pag.write("junk.txt")
	pag.press("enter")
	pag.press("left")
	pag.press("enter") #this "enter" saves the file to desktop
	pag.moveTo(1563,44)
	pag.click()
	df = pd.read_csv("C:\\Users\Owner\Desktop\junk.txt") #path to temporary file
	#print(df)
	intensity_check=df.iloc[0,0]  #location of the intensity in the data frame. Usually included an extra line if it is zero
	intensity_check = intensity_check.split()
	print(intensity_check)
	if len(intensity_check) == 6:
		if intensity_check[5] == "0!":
			print("TRANSMISSION IS 0.0% WITH THIS PROJECTILE ")
			flag = True
			return 0,flag 
	else: 
		_intensity=df.iloc[6,0] #location of the intensity in the data frame 
		_intensity=_intensity.split()
		print(f"The intensity for {isotope} with {beam_element} {beam_mass} is {_intensity[4]}.") #intensity value
		"""
		for i in range(len(isotope_info)):
			if isotope_info[i]["isotope"] == isotope:
				isotope_info[i]["intensity"] = _intensity[4] #change value in the dictionary
				print(isotope_info[i]["isotope"],isotope_info[i]["intensity"])
		"""
		return _intensity[4],flag


def isotope_loop():
	beam_data = []
	#with open("LISE_data.txt")
	start = time.time()
	for i,dic in enumerate(isotope_info): #loop for fragments
		df = pd.DataFrame(None)
		df = pd.DataFrame(columns=["Beam element","A (u)","Beam energy (MeV/u)","Beam Intensity (pnA)","Target thickness (microns)","Fragment Intensity (pnA)"])
		data = [] 
		iso=dic['isotope'].replace("_"," ") #get rid of the underscore in the isotope name
		print(f"You are looking at the {iso} isotope.")  #returns the name of the isotope
		iso = iso.split()
		set_fragment(iso[0],iso[1]) #fragment name, mass number
		for i,beam_element in enumerate(beam_info): #now loop for all the provided beams
			print(f"You are using {beam_element} as your primary beam at {beam_info[beam_element]['Energy']} MeV/u with {beam_info[beam_element]['Intensity']} pnA.")
			beam_energy= beam_info[beam_element]["Energy"]
			beam_intensity=beam_info[beam_element]["Intensity"]
			beam_element=beam_element.replace("_"," ")
			beam_element=beam_element.split()
			if beam_element[1] <= iso[1]:
				print(f"Skipping {beam_element[0]} {beam_element[1]}. Not greater than {iso[1]} nucleons.")
				continue
			#				name, energy, intensity, mass number A
			set_projectile(beam_element[0],beam_energy,beam_intensity,beam_element[1])
			thickness = get_thickness() #thickness with that particular beam for a particular fragment 
			tune_spectrometer()
			frag_intensity,flag = get_intensity(dic['isotope'],beam_element[0],beam_element[1]) #pass the isotope name to get intensity and save it to the map with the frag info
			if flag == True:
				continue
			print(f"Data being appended in the following format -> beam element, A,beam energy, beam intensity, thickness, fragment intensity: {beam_element[0]},{beam_element[1]} ,{beam_energy},{beam_intensity},{thickness}, {frag_intensity}")
			df.loc[i] = [beam_element[0],beam_element[1],beam_energy,beam_intensity,thickness,frag_intensity]
			print(df)
		print(f"DATA FRAME FOR {iso[0]} {iso[1]} ISOTOPE.")
		print(df)
		df.to_csv(f"{iso[0]}_{iso[1]}_data_LISE++.csv")
		print(f"File saved as: {iso[0]}_{iso[1]}_data_LISE++.csv")
	end = time.time()
	print(f"It took {end-start} to run everything.")

def save():
	with open("thickness.txt","w") as file:
		file.write(json.dumps(isotope_info))
	file.close()

#python 3 version 
def show_pixels():
	print('Press Ctrl-C to quit.')
	try:
		while True:
			x, y = pag.position()
			positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
			print(positionStr, end='')
			print('\b' * len(positionStr), end='', flush=True)
	except KeyboardInterrupt:
		print('\n')
    
    
   
  