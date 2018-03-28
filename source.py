import time
import webbrowser

# include the domain
url = input("Enter the website you want to open:")

# Time in 24 hour format
# use %I for 12 hour format
presentTime = time.strftime("%H:%M:%S")
print("The present time is " + presentTime)


alarmTime = input("Set the alarm as H:M:S(24hour format):")


while(presentTime != alarmTime):
    presentTime = time.strftime("%H:%M:%S")
    print("The time is " + presentTime)
    time.sleep(1)

if(presentTime == alarmTime):
    print("Your website opens now !!")
    # for linux
    #chrome_path = "/usr/bin/google-chrome %s"

    # for MacOs
    #chrome_path = "open -a /Applications/Google\ Chrome.app %s"

    # for windows
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    webbrowser.get(chrome_path).open(url)
