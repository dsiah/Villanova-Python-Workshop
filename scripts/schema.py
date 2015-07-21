import os

#file path escapes the space character by using a forward slash
#os.popen('open /Applications/Google\ Chrome.app')
#if chrome is open already it just switches to the chrome window
def returnApps():
    #Return a list of mac OS apps.
    apps = os.listdir('/Applications/')
    for i in apps:

        print i
    return apps

returnApps()
