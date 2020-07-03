#include<iostream>
#include<fstream>
#include<vector>
#include"TFile.h"
#include<sstream>
#include <iterator>
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
using namespace std;


/*
Roy Salinas 


*/


//function to read in csv to conver to TTree. Returns pointer to vector with our row data from csv.
std::vector<string>* reader(string filename)
{
	cout<<"Beginning to read in the file..."<<endl;
	ifstream data_stream;
	data_stream.open(filename.c_str()); //open the filestream to receive the data from the csv file
	string data,a;
	std::vector<string> *_row = new std::vector<string>;
	std::vector<string> *row = new std::vector<string>; //read initial data from csv
	if(data_stream.is_open())		
	{	
		cout<<"Opened the data stream!"<<endl;
		while(data_stream>>a)
			row->push_back(a);

	//iterate through the dynamic vector with an iterator (which is  pointer in it self)
		std::vector<string>::iterator itr; //iterator for string vector
		int counter=0;
		for (itr = row->begin(); itr != row->end(); ++itr){

			if(*itr != "angle") //once it finds this word, we are pass the column names
			{	
		//		cout<<*itr<<endl;
				counter++;
				continue;
			}
			else
				break;
		}

		itr = row->begin() + counter +1; //start where we have actual data +1 to get rid of angle word
		while(itr != row->end()){
		//	cout<<*itr<<endl;
			_row->push_back(*itr);
			++itr;
		}
		//cout<<"LOOPING THROUgh TO CHECK\n";
		//for (itr = _row->begin(); itr != _row->end(); ++itr)
		//	cout<<*itr<<endl;
	}	
	data_stream.close();
	return _row; //return the memory address of the vector with new data
}



//function that plots it and saves to a file
void plotdist()
{									
										// The path depends on the file, could use shell scrip to iterate through it all
	std::vector<string> *data = reader("/ENTER/THE/PATH/TO/FILE/Mg_32_finetune_10_data_LISE++.csv");
	std::vector<string>::iterator itr;
	//printf(" The size of your vector is %s\n", data->size());
	TFile *file = TFile::Open("test.root","recreate");
	//TTree *tree = new TTree("Isotope_Data","TTree with isotope data");
	float Intensity=99999.,wangle=99999,I2_slitwidht=99999.,Target_thickness=99999,wthick=99.;
	//tree->Branch("Intensity",&Intensity,"Intensity/F");
	TH2F *wedge_wedgeangle = new TH2F("wedge_wedgeangle", "Wedge and angle", 9,2000,3200,9,1.2,1.8);
	itr = data->begin();
	string junk; 
	std::vector<string> *temp = new std::vector<string>;
 	while(itr != data->end())//iterate through every row
 	{	 	
 		temp->clear();
		stringstream ss(*itr); //pass what the iterator is pointing to to the stringstream
		while(ss.good()){

			string junk;
			getline(ss,junk,','); //grab each word that appears before the comma
			temp->push_back(junk); //temporarily save it
		}
			
		cout<<junk<<endl;
		cout<<"Size is: "<<temp->size()<<endl;
		stringstream temp_ss(temp->at(7));
		temp_ss >> wthick;
		stringstream temp_sss(temp->at(8));
		temp_sss >> wangle;
		cout<<"You have: "<<wthick<<" and "<<wangle<<endl;
		wedge_wedgeangle ->Fill(wthick,wangle);
		//tree->Fill();
		++itr;
	}
	//tree->Write();
	wedge_wedgeangle ->Draw();
	file->Write();

}