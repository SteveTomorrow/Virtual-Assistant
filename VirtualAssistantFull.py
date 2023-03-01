import speech_recognition
import pyttsx3
from datetime import date , datetime
from selenium import webdriver # to control browser operations
import os # to save/open files
import wolframalpha # to calculate strings into formula
from gtts import gTTS # google text to speech
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import wikipedia
import webbrowser
import playsound
import codecs
#from googletrans import Translator
#translator = Translator()
#import Speech
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init('sapi5')
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)
robot_brain = ""
name = ""
name_name = "Hậu Lưu"
i = 0
def robot_Speaks(robot_brain):
    print("Robot: " + robot_brain)
    output = gTTS(robot_brain,lang = "vi",slow = False)
    output.save("output.mp3")
    playsound.playsound('output.mp3')
    os.remove('output.mp3')
    #speech = Speech(robot_brain,lang)
    #speech.play()
def get_audio():
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic,phrase_time_limit = 10)

    print("Robot:...")

    try:
        you = robot_ear.recognize_google(audio,language ='vi-VN')
    except:
        you = ""

    print("You: " + you)
    return you
def browser_web(input):
    if "chrome" in input:
        robot_Speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
    elif "firefox" in input or "mozilla" in input:
        robot_Speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
def search_web(input):
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome(executable_path=r"C:\Users\hauzi\AppData\Local\Programs\Python\Python38\Lib\site-packages\chromedriver_binary\chromedriver.exe")

    #binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #options = Options()
    #options.headless = False
    #options.binary = binary
    #cap = DesiredCapabilities().FIREFOX
    #cap["marionette"] = True #optional
    #driver = webdriver.Firefox(options=options, capabilities=cap, executable_path="C:\\Users\\hauzi\\OneDrive\\Documents\\Python\\AI_TTNT\\geckodriver-v0.23.0-win32\\geckodriver.exe")
    #driver = webdriver.Firefox(capabilities=cap,executable_path="C:\\Users\\hauzi\\OneDrive\\Documents\\Python\\AI_TTNT\\geckodriver-v0.23.0-win32\\geckodriver.exe")
    #driver.implicitly_wait(1)
    #driver.maximize_window()
    if "youtube" in input.lower():
        try:
            #robot_brain = "Opening in youtube"
            #robot_Speaks(robot_brain)
            for j in range(0,len(input)):
                if input[j-7:j].lower() == "youtube":
                    res = j + 1
                    name = input[res:None]
            #indx = input.lower().split().index('youtube')
            #query = input.split()[indx + 1:]
            #os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            #driver.get("http://www.youtube.com")
            #driver.get("https://www.youtube.com/results?search_query=" + name  )
            webbrowser.open('https://www.youtube.com/results?search_query='+ name ,new =2 )
            return
        except:
            webbrowser.open('https://www.youtube.com/results?search_query=',new=2)
    elif "nhạc" in input.lower() or "music" in input.lower():
        try:
            webbrowser.open('https://www.youtube.com/watch?v=W3B2C0nNpFU',new = 2)
        except:
            webbrowser.open('https://www.youtube.com/watch?v=7sIiiSJ_sIc',new=2)

    elif "wikipedia" in input.lower():

        try:
            #robot_brain = "Opening Wikipedia"
            #robot_Speaks(robot_brain)
            for j in range(0,len(input)):
                if input[j-9:j].lower() == "wikipedia":
                    res = j + 1
                    name = input[res:None]

            #indx = input.lower().split().index('wikipedia')
            #query = input.split()[indx + 1:]
            #driver.get("https://en.wikipedia.org")
            webbrowser.open('https://en.wikipedia.org/wiki/' +name,new = 2 )
            return
        except:
            webbrowser.open('https://en.wikipedia.org/wiki/',new = 2)
    elif "web" in input.lower():
        try:
            #robot_brain = "Opening Web"
            #robot_Speaks(robot_brain)
            for j in range(0,len(input)):
                if input[j-3:j].lower() == "web":
                    res = j + 1
                    name = input[res:None]
            print("http://www."+name.replace(" ","")+".com")
            webbrowser.open("http://www."+name.replace(" ","")+".com")
            return
        except:
            print("Fail")
            nameGG = "&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6DggAEOoCELQCEJoBEOUCOgUIABCxAzoGCAAQFhAeUO9SWMtuYPBwaANwAHgAgAFZiAG9BZIBATmYAQCgAQGqAQdnd3Mtd2l6sAEG&sclient=psy-ab&ved=0ahUKEwi0j77n64DqAhXJZSsKHebWDMkQ4dUDCAY&uact=5"

            webbrowser.open('https://www.google.com/search?source=hp&ei=sNnlXrT3JsnLrQHmrbPIDA&q='+'python'+'&oq='+'python' + nameGG )
    else:

        if "google" in input.lower():
            try:
                #robot_brain = "Opening in Google"
                #robot_Speaks(robot_brain)
                for j in range(0,len(input)):
                    if input[j-6:j].lower() == "google":
                        res = j + 1
                        name = input[res:None]
                        nameGG = "&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6DggAEOoCELQCEJoBEOUCOgUIABCxAzoGCAAQFhAeUO9SWMtuYPBwaANwAHgAgAFZiAG9BZIBATmYAQCgAQGqAQdnd3Mtd2l6sAEG&sclient=psy-ab&ved=0ahUKEwi0j77n64DqAhXJZSsKHebWDMkQ4dUDCAY&uact=5"

                webbrowser.open('https://www.google.com/search?source=hp&ei=sNnlXrT3JsnLrQHmrbPIDA&q='+name+'&oq='+name + nameGG )
                #webdriver.open("https://www.google.com/search?source=hp&ei=sNnlXrT3JsnLrQHmrbPIDA&q="+name+"&oq="+name + nameGG,new = 2)
            except:
                webbrowser.open('https://www.google.com/search?q =')
        elif "file" in input.lower() or "tập tin" in input.lower():
            try:
                for j in range(0,len(input)):
                    if input[j-4:j].lower() == "file":
                        res = j + 1
                        name = input[res:None]
                    elif input[j-7:j].lower() == "tập tin":
                        res = j + 1
                        name = input[res:None]
                os.system(name)
            except:
                print("File not found")
        elif "gmail" in input.lower():
            try:
                print("Open in Gmail ")
                webbrowser.open('https://mail.google.com/mail/u/0/#inbox',new=2)
            except:
                print("Sorry")
        elif "search" in input.lower() or "tìm kiếm" in input.lower():
            try:
                #robot_brain = "Opening in Google"
                #robot_Speaks(robot_brain)
                for j in range(0,len(input)):
                    if input[j-6:j].lower() == "google":
                        res = j + 1
                        name = input[res:None]
                        nameGG = "&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6DggAEOoCELQCEJoBEOUCOgUIABCxAzoGCAAQFhAeUO9SWMtuYPBwaANwAHgAgAFZiAG9BZIBATmYAQCgAQGqAQdnd3Mtd2l6sAEG&sclient=psy-ab&ved=0ahUKEwi0j77n64DqAhXJZSsKHebWDMkQ4dUDCAY&uact=5"

                webbrowser.open('https://www.google.com/search?source=hp&ei=sNnlXrT3JsnLrQHmrbPIDA&q='+name+'&oq='+name + nameGG )
            except:
                webbrowser.open('https://www.google.com/search?q =')
        else:
            try:
                #robot_brain = "Opening in Google"
                #robot_Speaks(robot_brain)
                for j in range(0,len(input)):
                    if input[j-6:j].lower() == "google":
                        res = j + 1
                        name = input[res:None]
                        nameGG = "&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6DggAEOoCELQCEJoBEOUCOgUIABCxAzoGCAAQFhAeUO9SWMtuYPBwaANwAHgAgAFZiAG9BZIBATmYAQCgAQGqAQdnd3Mtd2l6sAEG&sclient=psy-ab&ved=0ahUKEwi0j77n64DqAhXJZSsKHebWDMkQ4dUDCAY&uact=5"

                webbrowser.open('https://www.google.com/search?source=hp&ei=sNnlXrT3JsnLrQHmrbPIDA&q='+name+'&oq='+name + nameGG )
            except:
                webbrowser.open('https://www.google.com/search?q =')
        return


def talk_to_Robot(you):
    try:
        if "search" in you.lower() or "play" in you.lower() or "truy cập" in you.lower() or "mở" in you.lower():
            # a basic web crawler using selenium
            search_web(you)
            return
            robot_brain = "Tuyệt Vời"
        elif "hẹn giờ" in you.lower() :
            robot_brain = ("Tắt máy 7200 giây = 120 phút = 2 giờ")
            cmd = 'shutdown -s -t 7200'
            os.system(cmd)
        elif "xin chào" in you.lower():
            robot_brain="Xin chào ! Tôi có thể giúp được gì cho bạn !"
        elif "vợ tôi là ai" in you.lower():
            robot_brain = "Bạn chưa bao giờ có bạn gái ! Huống hồ chi là vợ !"
        elif "tôi tên" in you.lower():
                res = None
                for i in range(0, len(you)):
                    if you[i-3:i].upper() =="TÊN":
                        res = "null"
                        for j in range(i,len(you)):
                            if you[j-2:j].upper() == "LÀ":
                                res = j + 1
                                name = you[res:None]
                                break
                    if res == "null":
                        res = i + 1
                        name = you[res:None]
                name_name = name
                robot_brain = "Xin chào "+name + "Tôi có thể giúp gì cho bạn nào ?"
        elif "tổng thống mỹ" in you.lower():
            robot_brain = "Tổng thống mỹ là ông Donald Trump ! Ông chủ của chuỗi tập đoàn thức ăn nhanh lớn hàng đầu thế giới MCdonald "
        elif "chủ tịch nước việt nam" in you.lower():
            robot_brain ="Chủ tịch nước việt nam hiện tại là Nguyễn Phú Trọng"
        elif "đẹp trai" in you.lower() :
            robot_brain = "Hậu Lưu là người đẹp trai vô địch khắp vũ trụ "
        elif "hôm nay" in you.lower():
            today = date.today()
            robot_brain = today.strftime("%A Ngày %d tháng %m năm %Y")
        elif "giờ" in you.lower():
            now = datetime.now()
            robot_brain = now.strftime("%r")
        elif "yêu bạn" in you.lower():
            robot_brain = "Tôi cũng thế"
        elif "bạn là ai" in you.lower():
            robot_brain = '''Xin chào, tôi là Robot Steve. Trợ lý cá nhân của bạn.
            Tôi ở đây để làm cho cuộc sống của bạn dễ dàng hơn. Bạn có thể ra lệnh cho tôi thực hiện
            các nhiệm vụ khác nhau như tính toán tổng hoặc mở ứng dụng vvetra'''
        elif "i am" in you.lower():
            res = None
            for i in range(0, len(you)):
                if you[i] == "m":
                    res = i + 1
                    name = you[res:None]
                    break
            robot_brain="Hello"+name + " Can I Help You ?"

        elif "my name" in you.lower():
            res = None
            for i in range(0, len(you)):
                if you[i-4:i] =="name":
                    res = "null"
                    for j in range(i,len(you)):
                        if you[j-2:j] == "is":
                            res = j + 1
                            name = you[res:None]
                            break
                if res == "null":
                    res = i + 1
                    name = you[res:None]
                    break
            robot_brain="Hello "+name + " Can I Help You ?"
        elif "hello" in you.lower():
            robot_brain = "Hello Hau Luu !!! " + "Can I Help You ?"
        elif "today" in you.lower():
            today = date.today()
            robot_brain = today.strftime("%B %d, %Y")
        elif "time" in you.lower():
            now = datetime.now()
            robot_brain = now.strftime("%H hours %M munites %S seconds")
        elif "president" in you.lower() :
            robot_brain = "Mr.Donald Trump"
        elif "help me" in you.lower():
            robot_brain = "Can I Help You ?"
        elif "your name"in you:
            robot_brain = "My Name is Robot_Steve "
        elif "love you" in you.lower():
            robot_brain = "Me Too"
        elif "thank" in you.lower():
            robot_brain = " You're Welcome"
        elif 'shut down' in you.lower() or 'tắt máy' in you.lower():
            robot_brain= "Tôi sẽ shutdown máy tính của bạn sau vài giây !"
            os.system('shutdown -s')
        elif 'restart' in you.lower() or 'reset'in you.lower():
            robot_brain = "Tôi sẽ restart lại máy tính của bạn sau vài giây !"
            os.system('shutdown -r')
        elif "game" in you.lower() or "trò chơi"in you.lower():
            os.system('python FlappyBird.py')
            robot_brain = "Open FlappyBird Game"
        else:
            robot_brain = "I'm Fine thank you and you"
        robot_Speaks(robot_brain)
    except :
        robot_brain = "Tôi không hiểu, tôi có thể tìm kiếm trên web cho bạn, Bạn có muốn tiếp tục không?"
        robot_Speaks(robot_brain)
        ans = get_audio()
        if 'yes' in str(ans) or 'ok' in str(ans) or 'có' in str(ans):
            search_web(you)
if __name__ == "__main__":
    while i < 5:
            try :
                text = get_audio()
            except :
                text = ""
            if text == "":
                i = i+1
                continue

            if "tạm biệt" in text.lower() or "bye" in text.lower():
                robot_brain = ("Tạm Biệt " + name_name + " Hẹn gặp lại bạn !!!")
                robot_Speaks(robot_brain)
                break

            # calling process text to process the query
            talk_to_Robot(text)
