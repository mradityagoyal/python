'''
Created on Feb 1, 2016

@author: aditygoy
'''
import xlrd
from com.goyal.addy.util import PropertiesFile

KEY_COLUMN_POSITION = 0
ORIGINAL_MESSAGE_COLUMN_POSITION = 1;
MESSAGE_COLUMN_POSITION = 2
CAUSE_COLUMN_POSITION = 3
RESOLUTION_COLUMN_POSITION = 4

def updateCauseResolution(props, key, origMessage, updatedMessage, updatedCause, updatedResolution):
    if not key and not props and key in props.propertyNames():
        if not updatedMessage :
            props.setProperty(key ,updatedMessage)
        if not updatedCause:
            props.setProperty(key + ".cause", updatedCause)
        if not updatedResolution:
            props.setProperty(key + ".resolution", updatedResolution)
    return 


props = PropertiesFile.Properties()
fileStream = open("/home/aditygoy/pythonWS/MessagesStringsUpdaer/AES.properties")
# Load the porperties from the .properties file.
props.load(fileStream)

# Load the excel file.
wb = xlrd.open_workbook("/home/aditygoy/pythonWS/MessagesStringsUpdaer/AES.xls")
ws = wb.sheet_by_index(0)
# for each row in excel file.. read the msg, cause and resolution. 
for row in range(ws.nrows):
    enum_key = ws.cell_value(row, KEY_COLUMN_POSITION);
    origMessage = ws.cell_value(row, ORIGINAL_MESSAGE_COLUMN_POSITION)
    updatedMessage = ws.cell_value(row, MESSAGE_COLUMN_POSITION)
    updatedCause = ws.cell_value(row, CAUSE_COLUMN_POSITION)
    updatedResolution = ws.cell_value(row, RESOLUTION_COLUMN_POSITION)
    # update message, cause and resolution in the props
    updateCauseResolution(props, enum_key, origMessage, updatedMessage, updatedCause, updatedResolution)
    
# output the updated props.
props.store(open("/home/aditygoy/pythonWS/MessagesStringsUpdaer/PythonOut.properties", "w"))


