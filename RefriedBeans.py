#Opens all MBeans for performance testing
import threading
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DEBUG = False

#Log printing
def log(s):
    if DEBUG:
        print(s)

class myThread (threading.Thread):
    def __init__(self, name, counter, bean):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
        self.bean = bean
        self.driver = webdriver.Firefox()
    def run(self):
        log("Starting " + self.name)
        #Open the individual MBean
        self.driver = openMBeans(self.bean, self.driver)
        log("Exiting " + self.name)

#Starts threads for the two instances to be opened
def threadMBeans(mBeans):
    try:
        #List for drivers to return
        
        #Create and start 2 threads
        thread1 = myThread("Thread WAS01", 1, mBeans[0])
        thread2 = myThread("Thread WAS02", 2, mBeans[1])
        thread1.start()
        thread2.start()
        driverList = [thread1.driver, thread2.driver]
        thread1.join()
        thread2.join()
        #Threads are finished
        log("Done")
        return driverList
    except Exception as e:
        print("Error: Could not start threads " + str(e))
    return

#Handles the opening of each pair of MBeans
def openMBeans(bean, driver):
    #Go to MBeans page
    driver.get(bean)
    #Go to main menu
    driver.find_element_by_partial_link_text('ProcessMonitor').click()
    #Turn on monitoring
    driver.find_element_by_xpath("//*[@name='action'][@value='turnOnMonitoring']").click()
    #Go back to main menu
    driver.find_element_by_partial_link_text('MBean').click()
    #Go to htmlOutput
    driver.find_element_by_xpath("//*[@name='action'][@value='htmlOutput']").click()
    #Refresh page
    driver.refresh()
    return driver

#Gets info for file naming
def nameMBeans(driver):
    #Find the paragraph with bean name
    elements = driver.find_elements_by_tag_name("p")
    #Get the name
    paragraph = elements[2].text
    #Parse name from paragraph
    regex = re.search('name=(.*)_ProcessMonitor', paragraph)
    name = regex.group(1)
    #Shorten name if applicable
    if(name == "ConsolidationServerMDB"):
        name = "CS"
    elif(name == "WebServices"):
        name = "WBI"
    elif(name == "PassportIntegrationWeb"):
        name = "PI"
    elif(name == "WebDataSink"):
        name = "WDS"
    #Get url
    url = driver.current_url
    regex = re.search('\d\d\d\.\d\d\.\d\d\.(\d+):', url)
    ip = regex.group(1)
    #Rename ip if applicable
    if(ip == "95"):
        ip = "WAS02"
    elif(ip == "96"):
        ip = "WAS01"
    #Create full file name
    fileName = name + "_" + ip
    return fileName

#Collect and save MBeans
def collectMBeans(driverList):
    #Iterate through every driver
    for driver in driverList:
        #Refresh page
        driver.refresh()
        #Get MBean name
        fileName = nameMBeans(driver)
        #Save page
        page_src = driver.page_source
        path = "C:\\Users\\admin\\Downloads\\"  + fileName + ".html"
        file = open(path, 'w')
        file.write(page_src)

#MBean pair urls
WDS = ["http://153.71.88.96:8082/", "http://153.71.88.95:8082/"]
WBI = ["http://153.71.88.96:8083/", "http://153.71.88.95:8083/"]
PI = ["http://153.71.88.96:8084/", "http://153.71.88.95:8084/"]
CS = ["http://153.71.88.96:8085/", "http://153.71.88.95:8085/"]
CPWERecognition = ["http://153.71.88.99:8082/", "http://153.71.88.100:8082/"]

#User input to choose what MBean to open up
mBeanChoice = input("1.WDS\n2.WBI\n3.PI\n4.CPWERecognition\n5.Quit\n")
#Choice parsing
beanSplit = mBeanChoice.split()
#Change string list into int list
beanSplit = list(map(int, beanSplit))
#Start threads for each call
driverList = []
for b in beanSplit:
    tempList = []
    if b == 1:
        tempList = threadMBeans(WDS)
    elif b == 2:
        tempList = threadMBeans(WBI)
    elif b == 3:
        tempList = threadMBeans(PI)
    elif b == 4:
        tempList = threadMBeans(CPWERecognition)
    driverList.extend(tempList)
        
#Wait for command to collect MBeans
collect = input("Collect MBeans? (y/n)")
#Collect MBeans
if collect == "y":
    collectMBeans(driverList)



