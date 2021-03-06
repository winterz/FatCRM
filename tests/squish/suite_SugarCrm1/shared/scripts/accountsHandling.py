from squish import *
import test

def createAccount():
    clickTab(waitForObject(":SugarCRM Client: admin@SugarCRM on localhost.qt_tabwidget_tabbar_QTabBar"), "Accounts")
    clickButton(waitForObject(":Page.New_QPushButton"))
    
def registerDetails( list ):    
    type(waitForObject(":Details.name_QLineEdit"), "<Ctrl+A>")   
    type(waitForObject(":Details.name_QLineEdit"), list[0])
    type(waitForObject(":Details.website_QLineEdit"), "<Ctrl+A>")    
    type(waitForObject(":Details.website_QLineEdit"), list[1])    
    type(waitForObject(":Details.tyckerSymbol_QLineEdit"), "<Ctrl+A>")
    type(waitForObject(":Details.tyckerSymbol_QLineEdit"), list[2]) 
    if(list[3] != ''):         
        findObject(":Details.parentName_QComboBox")
        mouseClick(waitForObjectItem(":Details.parentName_QComboBox", list[3]))            
    type(waitForObject(":Details.ownership_QLineEdit"), "<Ctrl+A>")        
    type(waitForObject(":Details.ownership_QLineEdit"), list[4])           
    type(waitForObject(":Details.industry_QComboBox"), list[5])
    type(waitForObject(":Details.accountType_QComboBox"), list[6])    
    if(list[7] != ''):
        findObject(":Details.campaignName_QComboBox")
        mouseClick(waitForObjectItem(":Details.campaignName_QComboBox", list[7]))    
    type(waitForObject(":Details.assignedUserName_QComboBox"), list[8])
    
def registerOtherDetails( list ):
    type(waitForObject(":Other Details.phoneOffice_QLineEdit"), "<Ctrl+A>")
    type(waitForObject(":Other Details.phoneOffice_QLineEdit"), list[0])
    type(waitForObject(":Other Details.phoneFax_QLineEdit"), "<Ctrl+A>")    
    type(waitForObject(":Other Details.phoneFax_QLineEdit"), list[1])
    type(waitForObject(":Other Details.phoneAlternate_QLineEdit"), "<Ctrl+A>")    
    type(waitForObject(":Other Details.phoneAlternate_QLineEdit"), list[2])
    type(waitForObject(":Other Details.employees_QLineEdit"), "<Ctrl+A>")    
    type(waitForObject(":Other Details.employees_QLineEdit"), list[3])
    type(waitForObject(":Other Details.rating_QLineEdit"), "<Ctrl+A>")
    type(waitForObject(":Other Details.rating_QLineEdit"), list[4]) 
    type(waitForObject(":Other Details.sicCode_QLineEdit"), "<Ctrl+A>")   
    type(waitForObject(":Other Details.sicCode_QLineEdit"), list[5])    
    type(waitForObject(":Other Details.annualRevenue_QLineEdit"), "<Ctrl+A>")
    type(waitForObject(":Other Details.annualRevenue_QLineEdit"), list[6])
    type(waitForObject(":Other Details.email1_QLineEdit"), "<Ctrl+A>")    
    type(waitForObject(":Other Details.email1_QLineEdit"), list[7])
    
def registerAddresses( bList, sList):  
    type(waitForObject(":Addresses.billingAddressStreet_QLineEdit"), "<Ctrl+A>")
    type(waitForObject(":Addresses.billingAddressStreet_QLineEdit"), bList[0])
    type(waitForObject(":Addresses.billingAddressCity_QLineEdit"), "<Ctrl+A>")    
    type(waitForObject(":Addresses.billingAddressCity_QLineEdit"), bList[1])
    type(waitForObject(":Addresses.billingAddressState_QLineEdit"), "<Ctrl+A>")         
    type(waitForObject(":Addresses.billingAddressState_QLineEdit"), bList[2])     
    type(waitForObject(":Addresses.billingAddressPostalcode_QLineEdit"), "<Ctrl+A>")  
    type(waitForObject(":Addresses.billingAddressPostalcode_QLineEdit"), bList[3])
    type(waitForObject(":Addresses.billingAddressCountry_QLineEdit"), "<Ctrl+A>")       
    type(waitForObject(":Addresses.billingAddressCountry_QLineEdit"), bList[4])
    type(waitForObject(":Addresses.shippingAddressStreet_QLineEdit"), "<Ctrl+A>")           
    type(waitForObject(":Addresses.shippingAddressStreet_QLineEdit"), sList[0])
    type(waitForObject(":Addresses.shippingAddressCity_QLineEdit"), "<Ctrl+A>")    
    type(waitForObject(":Addresses.shippingAddressCity_QLineEdit"), sList[1]) 
    type(waitForObject(":Addresses.shippingAddressState_QLineEdit"), "<Ctrl+A>")      
    type(waitForObject(":Addresses.shippingAddressState_QLineEdit"), sList[2])     
    type(waitForObject(":Addresses.shippingAddressPostalcode_QLineEdit"), "<Ctrl+A>")  
    type(waitForObject(":Addresses.shippingAddressPostalcode_QLineEdit"), sList[3])
    type(waitForObject(":Addresses.shippingAddressCountry_QLineEdit"), "<Ctrl+A>")       
    type(waitForObject(":Addresses.shippingAddressCountry_QLineEdit"), sList[4])       
    
def registerDescription( description ):
    type(waitForObject(":Description:.description_QTextEdit"), "<Ctrl+A>" )
    type(waitForObject(":Description:.description_QTextEdit"), description )
    
def saveAccount():
    clickButton(waitForObject(":&Account Details.Save_QPushButton"))
    label = findObject(':Account Information.modifiedDate_QLineEdit')
    waitFor("label.text !=''")  
    
def checkDetailsValues( dList):
    test.compare(findObject(":Details.name_QLineEdit").text, dList[0])    
    test.compare(findObject(":Details.website_QLineEdit").text, dList[1])    
    test.compare(findObject(":Details.tyckerSymbol_QLineEdit").text, dList[2]) 
    test.compare(findObject(":Details.parentName_QComboBox").currentText, dList[3])                  
    test.compare(findObject(":Details.ownership_QLineEdit").text, dList[4])    
    test.compare(findObject(":Details.industry_QComboBox").currentText, dList[5])      
    test.compare(findObject(":Details.accountType_QComboBox").currentText, dList[6])   
    test.compare(findObject(":Details.campaignName_QComboBox").currentText, dList[7])        
    test.compare(findObject(":Details.assignedUserName_QComboBox").currentText, dList[8])
            
def checkOtherDetailsValues( oList):            
    test.compare(findObject(":Other Details.phoneOffice_QLineEdit").text, oList[0])        
    test.compare(findObject(":Other Details.phoneFax_QLineEdit").text, oList[1])        
    test.compare(findObject(":Other Details.phoneAlternate_QLineEdit").text, oList[2])        
    test.compare(findObject(":Other Details.employees_QLineEdit").text, oList[3])        
    test.compare(findObject(":Other Details.rating_QLineEdit").text, oList[4])        
    test.compare(findObject(":Other Details.sicCode_QLineEdit").text, oList[5])        
    test.compare(findObject(":Other Details.annualRevenue_QLineEdit").text, oList[6])        
    test.compare(findObject(":Other Details.email1_QLineEdit").text, oList[7])
            
def checkAddressesValues(bList, sList):            
    test.compare(findObject(":Addresses.billingAddressStreet_QLineEdit").text, bList[0])        
    test.compare(findObject(":Addresses.billingAddressCity_QLineEdit").text, bList[1])        
    test.compare(findObject(":Addresses.billingAddressState_QLineEdit").text, bList[2])        
    test.compare(findObject(":Addresses.billingAddressPostalcode_QLineEdit").text, bList[3])    
    test.compare(findObject(":Addresses.billingAddressCountry_QLineEdit").text, bList[4])    
    test.compare(findObject(":Addresses.shippingAddressStreet_QLineEdit").text, sList[0])    
    test.compare(findObject(":Addresses.shippingAddressCity_QLineEdit").text, sList[1])    
    test.compare(findObject(":Addresses.shippingAddressState_QLineEdit").text, sList[2])    
    test.compare(findObject(":Addresses.shippingAddressPostalcode_QLineEdit").text, sList[3])    
    test.compare(findObject(":Addresses.shippingAddressCountry_QLineEdit").text, sList[4])
    
def checkDescriptionValue(description):    
    test.compare(findObject(":Description:.description_QTextEdit").plainText, description)      
    
def removeAccount( accountName ):
     clickTab(waitForObject(":SugarCRM Client: admin@SugarCRM on localhost.qt_tabwidget_tabbar_QTabBar"), "Accounts")
     type(waitForObject(":Page.searchLE_QLineEdit"), accountName)
     waitForObjectItem(":Page.treeView_Akonadi::EntityTreeView", "admin")          
     clickButton(waitForObject(":Page.Remove_QPushButton"))
     clickButton(waitForObject(":SugarClient - Delete record.Yes_QPushButton"))
     clickButton(waitForObject(":Page.Clear_QToolButton"))     
     type(waitForObject(":Page.searchLE_QLineEdit"), accountName)
     treeView = waitForObject(":Page.treeView_Akonadi::EntityTreeView")
     model = treeView.model()
     count = model.rowCount()
     test.compare(count, 0)
    