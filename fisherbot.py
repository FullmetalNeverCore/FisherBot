import pyautogui as pt 
import time 


class Fisher:
    global times 
    times = 0 
    def locate_image_on_screen(image_name,cross):
        global times
        if times > 15: times = 0 
        imgloc = pt.locateOnScreen(image_name,grayscale=True,confidence=0.6,region=(535,150,1500,600))
        pt.screenshot("./png/screen.png",region = (535,150,1500,600))
        print(imgloc)
        if imgloc == None:
                print(" not found")
                pt.screenshot("test.png",region=cross)
                time.sleep(0.2)
        else:
                print("! found")
                pt.click(button="right")
                return True
        if pt.locateOnScreen("onedot.jpg",grayscale=True,confidence=0.5,region=(535,150,1500,600)) or pt.locateOnScreen("./png/twodots.jpg",grayscale=True,confidence=0.5,region=(535,150,1500,600)) or pt.locateOnScreen("./png/threedots.jpg",grayscale=True,confidence=0.5,region=(535,150,1500,600)) != None:
            #print(pt.locateOnScreen("onedot.jpg",grayscale=True,confidence=0.7,region=(535,150,1500,600)))
            times = times + 1
            print("times:",times)
            print("Seraching for !!!...")
            return False 
        else:
            if times == 0:
                times = times + 1
                print("Starting the fishing process...")
                pt.click(button="right")
                time.sleep(2)
                return False
            else:
                if pt.locateOnScreen("onedot.jpg",grayscale=True,confidence=0.5,region=(535,150,1500,600)) or pt.locateOnScreen("./png/twodots.jpg",grayscale=True,confidence=0.5,region=(535,150,1500,600)) or pt.locateOnScreen("./png/threedots.jpg",grayscale=True,confidence=0.5,region=(535,150,1500,600)) == None:
                    print('skipping...')
                    print('dots are none')
                    times = 0
                    return False
if __name__ == "__main__":
    print("FisherBot is starting...")
    time.sleep(3)
    print("starting the fishing process...")
    pt.keyDown("ctrl")
    #get center of the screen using pyautogui
    cross = pt.locateOnScreen("./png/cross.png",grayscale=True,confidence=0.9)
    pt.keyDown("F1")
    pt.click(button="right")
    while True:
        #print(cross)
        img = Fisher.locate_image_on_screen("./png/one.jpg",cross)
        if img == True:
            pt.keyUp("F1")
            pt.keyUp("ctrl")
            print("sleeping for 20 secs....")
            time.sleep(20)
            pt.keyDown("F1")
            pt.keyDown("ctrl")
            pt.click(button="right")
            continue

