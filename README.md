# SPFYUserlyzer

**Description**
- The python script screen scrapes the data storage by record, by user (based on SOQL) in
  Salesforce org and export the results to an Excel spreadsheet.
- Works only in Salesforce classic but can be extended for lightning as well.
- The script scrapes the data from the URL https://<salesforce org
  URL>/setup/user/userstorageusage.jsp?id=005r0000005BrMAAU, where 005r0000005BrMAAU is the  
  user Id.
- Uses simple-salesforce, selenium and chromedriver libraries for automation.
- Provides flexibility to configure the SOQL based on which the export is generated.   
- Modify the `resources/config.py` file with your salesforce credentials and other settings to use the app.
- A 30 seconds wait is added to the `SPFYUserlyzer.py` after login to allow the user to complete 2FA or identity verification. You can increase this wait as desired.
  
To run the script from terminal:
`python3 <PATH to SPFYUserlyzer.py>/SPFYUserlyzer.py`
  

Original Author : https://github.com/ekenigsberg.  
This repo is a modified version of https://github.com/ekenigsberg/SPFYUserlyzer.   
The original script is published as Jupyter Notebook. I installed the required dependencies and converted it into a .py script beacuse i am more comfortable working with .py files.
  
Commands used on MAC to install dependencies for original script if you are a newbie to python:
  
```
brew install python  
brew link python@3.9

// not required for this version
ipython nbconvert --to script "/Users/maninder.singh/Downloads/SPFYUserlyzer-master/SPFYUserlyzer.ipynb” 

// not required for this version
cd /Users/maninder.singh/Downloads/SPFYUserlyzer-master
  
// not required for this version
pip install pipreqs 

// not required for this version
pipreqs .

pip install -r requirements.txt
pip install selenium
  
// alternatively, you can also install the correct version of chromedriver from https://chromedriver.chromium.org/downloads
brew install chromedriver 
  
pip3 install lxml
pip3 install html5lib
pip3 install openpyxl
pip3 install BeautifulSoup4
```
Please contribute to the original repo to support the developer. You are also welcome to contribute to this version.
  




    



 
  



