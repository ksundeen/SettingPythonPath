# See these help documents
## http://python-docx.readthedocs.org/en/latest/user/install.html
## https://python-docx.readthedocs.org/en/latest/api/style.html
## https://raw.githubusercontent.com/mikemaccana/python-docx/master/example-makedocument.py

# Use this site to use the docx module
## http://python-docx.readthedocs.org/en/latest/user/quickstart.html

# If module isn't loading, then temporarily append to sys.path variable
import os, sys

###########################################################################
# Checks that Anaconda path is in system path variable to access 64-bit Python modules
def checkPathAdded(pathToAppend):
    if pathToAppend in sys.path: 
        print 'Directory {0} already added to system path'.format(pathToAppend)
    else: 
        sys.path.append(pathToAppend)
        print 'Added {0} directory to system path'.format(pathToAppend)
        
        
checkPathAdded(r'C:\Anaconda\Lib\site-packages')
checkPathAdded(r'C:\Python27\ArcGISx6410.3')
checkPathAdded(r'C:\Program Files (x86)\ArcGIS\Desktop10.3')

# Add arcpy packages from ArcGIS
arcpy32PythonPaths = [
'C:\\Python27\\ArcGIS10.3'
, 'C:\\Python27\\ArcGIS10.3\\lib\\site-packages'
, 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\bin'
, 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\ArcPy'
, 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\ArcToolBox\\Scripts'
, 'C:\\Python27\\ArcGIS10.3\\lib\\site-packages\\win32'
, 'C:\\Python27\\ArcGIS10.3\\lib\\site-packages\\win32\\lib']

# Paths were taken from the sys.path (PYTHONPATH variable) when running
# python 64-bit exe located C:\Python27\ArcGISx6410.3\python.exe
# If working in QGIS, these paths need to be added to sys.path
arcpy64PythonPaths = [
u'c:\\program files (x86)\\arcgis\\desktop10.3\\arcpy'
, 'C:\\windows\\system32\\python27.zip'
, 'C:\\Python27\\ArcGISx6410.3\\DLLs'
, 'C:\\Python27\\ArcGISx6410.3\\lib'
, 'C:\\Python27\\ArcGISx6410.3\\lib\\plat-win'
, 'C:\\Python27\\ArcGISx6410.3\\lib\\lib-tk'
, 'C:\\Python27\\ArcGISx6410.3'
, 'C:\\Python27\\ArcGISx6410.3\\lib\\site-packages'
, 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\bin64'
, 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\ArcPy'
, 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.3\\ArcToolBox\\Scripts'
, 'C:\\Anaconda\\Lib\\site-packages']

# Adds or removes paths temporarily to sys.path variable
def addPythonPath(pathList, Add_or_Remove):
    if Add_or_Remove == 'Add':
        for eachPath in pathList:
            checkPathAdded(eachPath)
    elif Add_or_Remove == 'Remove':
        for eachPath in pathList:
            if eachPath not in sys.path: 
                continue
            else: 
                sys.path.remove(eachPath)

# Runs function to add all 64-bit python paths to the current sys.path
addPythonPath(arcpy64PythonPaths, 'Add')
###########################################
