from select import select
import pyautogui as bot
import time
import config as cf

bot.PAUSE = 0.5
bot.FAILSAFE = True
autoPlayMap = cf.aPM.copy()
autoPlayDif = cf.aPD.copy()


def Tempo():
    return str(time.localtime().tm_hour)+'h:'+str(time.localtime().tm_min)+'m:'+str(time.localtime().tm_sec)+'s = '

# Reset the difficult
def AutoPlayResetD():
    for y in range(len(cf.aPD)):
            autoPlayDif[y] = cf.aPD[y]
            print('Difficult ',autoPlayDif[y])

# Reset the AutoPlay
def AutoPlaySetUP(first):
    #global autoPlayMap, autoPlayDif
    if(first):
        print('SETTING AUTO PLAY...')
    else:
        print('RESTARTING AUTO PLAY...')
    for x in range(len(cf.aPM)):        
        #print(x)
        autoPlayMap[x] = cf.aPM[x]
        print('MAP: ',autoPlayMap[x])        
        
        for y in range(len(cf.aPD)):
            autoPlayDif[y] = cf.aPD[y]
            print('Difficult: ',autoPlayDif[y])


def AutoPlay():
    diffCount =1
    for x in range(len(autoPlayMap)):          
        #x = x-1
        if(autoPlayMap[x] !=3):   
                                
            for y in range(len(autoPlayDif)):
                #y =y-1
                if(autoPlayDif[y] !=3):                    
                    SelectMap(autoPlayMap[x],autoPlayDif[y],True)
                    autoPlayDif[y] = 3
                    diffCount = y
                    break
                
                
                if(y == len(autoPlayDif)-1):
                    autoPlayMap[x] = 3
                    AutoPlayResetD()
                
        
        if(autoPlayMap[x] == 3):
            if(autoPlayMap[len(autoPlayMap)-1] ==3):
                AutoPlaySetUP(False)
            
        if(diffCount != 3 and autoPlayMap[x] !=3):
            diffCount =0
            break
        
        
        
            
    
def SelectMap(name, dif,auto):#BAD CODE
    a =0
    
    if(dif == 0):
        for pos in bot.locateAllOnScreen('imagens/normal.png',confidence = cf.generalconfidence):
            if(a == 0 and name == 0):
                bot.click(pos)
                break
            if(a == 1 and name == 1):
                bot.click(pos)
                break
            if(a == 2 and name == 2):
                bot.click(pos)
                break
            a+= 1
    if(dif == 1):
        for pos in bot.locateAllOnScreen('imagens/hard.png',confidence = cf.generalconfidence):
            
            if(a == 0 and name == 0):
                bot.click(pos)
                break
            if(a == 1 and name == 1):
                bot.click(pos)
                break
            if(a == 2 and name == 2):
                bot.click(pos)
                break
            a+= 1
    if(dif == 2):
        for pos in bot.locateAllOnScreen('imagens/nightmare.png',confidence = cf.generalconfidence):
            if(a == 0 and name == 0):
                bot.click(pos)
                break
            if(a == 1 and name == 1):
                bot.click(pos)
                break
            if(a == 2 and name == 2):
                bot.click(pos)
                break
            a+= 1
    time.sleep(1)
    if(auto):
        print('         AUTO PLAY')
        print(Tempo(),name,':',dif)
        print('         AUTO PLAY')
    bot.click(bot.locateOnScreen('imagens/confirm.png',confidence = cf.generalconfidence))
    

    
    
if(cf.autoPlayOn):
    AutoPlaySetUP(True)

while True:
    #Click to start the game
    if(bot.locateOnScreen('imagens/pickup.png',confidence = cf.generalconfidence)):
        bot.click(bot.locateOnScreen('imagens/confirm.png',confidence = cf.generalconfidence))

    if(bot.locateOnScreen('imagens/bug.png',confidence = cf.generalconfidence)):bot.click(bot.locateOnScreen('imagens/bugx.png',confidence = cf.generalconfidence))
#Change the time
    if(cf.time):
        if(bot.locateOnScreen('imagens/time1x.png',confidence = cf.generalconfidence)):            
            bot.click(bot.locateOnScreen('imagens/time1x.png',confidence = cf.generalconfidence))
    if(bot.locateCenterOnScreen('imagens/ad/okay.png',confidence = cf.generalconfidence)):bot.click(bot.locateCenterOnScreen('imagens/ad/okay.png',confidence = cf.generalconfidence))
#Take free stufs
    if(bot.locateCenterOnScreen('imagens/coin.png',confidence = cf.generalconfidence)):
        bot.click(bot.locateCenterOnScreen('imagens/coin.png',confidence = cf.generalconfidence))
        bot.click(bot.locateCenterOnScreen('imagens/ad/okay.png',confidence = cf.generalconfidence))
    
    
    if(bot.locateCenterOnScreen('imagens/ad/watchVideo.png',confidence=0.9)):
        bot.click(bot.locateCenterOnScreen('imagens/nothanks.png',confidence = cf.generalconfidence))
    # Verify if has a AD (BAD CODE)
    if(cf.ad):
        if(bot.locateCenterOnScreen('imagens/ad/watchVideo.png',confidence=0.9)):
            ad = True;
            # Click to watch the AD        
            bot.moveTo(bot.locateCenterOnScreen('imagens/ad/watchVideo.png',confidence=0.9))
            time.sleep(1)
            bot.click(bot.locateCenterOnScreen('imagens/ad/watchVideo.png',confidence=0.9),clicks=1,interval=1)
            print(Tempo() +'AD')
            #Verify if we can exit the AD
            while ad:
                time.sleep(1)
                #if the AD dons't work
                if(bot.locateCenterOnScreen('imagens/ad/watchVideo.png',confidence=0.9)):
                    bot.click(bot.locateCenterOnScreen('imagens/nothanks.png',confidence=0.9),clicks=1,interval=1)
                    print(Tempo() +'AD bug!')
                    break
                
                # AD 1
                if(bot.locateCenterOnScreen('imagens/ad/x.png',confidence=0.9)):
                    bot.click(bot.locateCenterOnScreen('imagens/ad/x.png',confidence=0.9),clicks=1,interval=1)  
                    time.sleep(1)
                    ad = False;
                # AD 2
                if(bot.locateOnScreen('imagens/ad/p.png',confidence=0.7,grayscale=True)):
                    bot.click(bot.locateOnScreen('imagens/ad/p.png',confidence=0.7,grayscale=True),clicks=1,interval=1)
                # AD 2-1
                if(bot.locateOnScreen('imagens/ad/px.png',confidence=0.8,grayscale=True)):
                    bot.click(bot.locateOnScreen('imagens/ad/px.png',confidence=0.9),clicks=1,interval=1)
                # AD 3
                if(bot.locateOnScreen('imagens/ad/px.png')):
                    bot.click(bot.locateOnScreen('imagens/ad/px.png',confidence=0.9),clicks=1,interval=1)

                # AD END
                if(bot.locateOnScreen('imagens/ad/xa.png')):
                    bot.click(bot.locateOnScreen('imagens/ad/xa.png',confidence=0.9),clicks=1,interval=1)               
                    
                #ADBUG
                if(bot.locateOnScreen('imagens/bug/install.png',confidence=0.9)):
                    bot.click(bot.locateOnScreen('imagens/bug/a.png',confidence=0.9),clicks=1,interval=1)
                    bot.click(bot.locateOnScreen('imagens/bug/b.png',confidence=0.9),clicks=1,interval=1)
                    bot.click(bot.locateOnScreen('imagens/ad/px.png',confidence=0.9),clicks=1,interval=1)
                    
                if(bot.locateCenterOnScreen('imagens/ad/okay.png',confidence=0.9)):
                    bot.click(bot.locateCenterOnScreen('imagens/ad/okay.png',confidence=0.9),clicks=1,interval=1)
                    ad = False
                    print(Tempo()+'AD Done')
    
        
#Verify if we has a achievement
    if(bot.locateCenterOnScreen('imagens/achievements.png',confidence = cf.generalconfidence)):
        print(Tempo()+ 'achievement')
        bot.click(bot.locateCenterOnScreen('imagens/achievements.png',confidence = cf.generalconfidence))
        for pos in bot.locateAllOnScreen('imagens/reward.png',confidence = 0.9):
            bot.click(pos)
            continue
            
        bot.click(bot.locateOnScreen('imagens/exit.png',confidence = cf.generalconfidence))

    
#Verify if we has a weekly achievement
    if(bot.locateCenterOnScreen('imagens/weekchievements.png',confidence = cf.generalconfidence)):
        print(Tempo()+ 'weekly achievement')
        bot.click(bot.locateCenterOnScreen('imagens/weekchievements.png',confidence = cf.generalconfidence))
        for pos in bot.locateAllOnScreen('imagens/rewardw.png',confidence = cf.generalconfidence):
            bot.click(pos)
            
            
        bot.click(bot.locateOnScreen('imagens/exit.png',confidence = cf.generalconfidence))
    
    # If you win or lose
    if(bot.locateOnScreen('imagens/win.png',confidence = cf.generalconfidence) or bot.locateOnScreen('imagens/selectmap.png',confidence = cf.generalconfidence)):
        if(bot.locateOnScreen('imagens/win.png',confidence = 0.8)):
            bot.click(bot.locateOnScreen('imagens/continue.png',confidence = 0.8))
            print(Tempo()+"Winner,")
        if(cf.autoPlayOn):
            AutoPlay()
        else:
            SelectMap(cf.map,cf.hard,False)
        
    if(bot.locateOnScreen('imagens/timeWarp.png',confidence = cf.generalconfidence)):
        print(Tempo()+"Loser")
        bot.click(bot.locateOnScreen('imagens/timeWarp.png',confidence = cf.generalconfidence))
        bot.click(bot.locateOnScreen('imagens/selectmapBTN.png',confidence = cf.generalconfidence))
        
    #Close any game window (Temp achievement bug fix)
    if(bot.locateOnScreen('imagens/exit.png',confidence = cf.generalconfidence) and not bot.locateOnScreen('imagens/selectmap.png',confidence = cf.generalconfidence)):
        bot.click(bot.locateOnScreen('imagens/exit.png',confidence = cf.generalconfidence))
        print(Tempo()+"Closed a game window")
    
