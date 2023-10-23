#import click
from concurrent.futures.process import _chain_from_iterable_of_lists
from dataclasses import replace
import textwrap
from tkinter.messagebox import RETRY
from unittest import result
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import randfacts
import pyjokes
import urllib.request
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import datetime
import pytz
from translate import Translator #pip install translate
from tkinter import *
import webbrowser
from urllib.request import urlopen
import textwrap
import operator
import wikipedia
import math

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('D:\\Sem 6 Mini Project\\MOCK(13-04-2022)\\intentsbot.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
#print(classes)

tag_name=""
message = ""
class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<4:
        state="Welcome. I am your Buddy. How may I help you?"
    elif hour>=4 and hour<12:
        state="Hello,Good Morning. I am your Buddy. How may I help you?"
    elif hour>=12 and hour<17:
        state="Hello,Good Afternoon. I am your Buddy. How may I help you?"
    else:
       state="Hello,Good Evening. I am your Buddy. How may I help you?"
    return state   

def word_meaning(msg):
    wrd=msg.split()
    if wrd[1]=="does":
        word=wrd[2].strip()
    else:
        word = wrd[-1].strip()

    url = "https://www.vocabulary.com/dictionary/" + word + ""
    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'lxml')

    soup1 = soup.find(class_="short")

    try:
        soup1 = soup1.get_text()
        # Print short meaning
        print ('-' * 25 + '->',word,"<-" + "-" * 25)
        print ("SHORT MEANING: \n\n",soup1)
        print ('-' * 65)

        # Print long meaning
        soup2 = soup.find(class_="long")
        soup2 = soup2.get_text()
        print ("LONG MEANING: \n\n",soup2)

        print ('-' * 65)

        # Print instances like Synonyms, Antonyms, etc.
        soup3 = soup.find(class_="instances") 
        txt = soup3.get_text()
        txt1 = txt.rstrip()

        print (' '.join(txt1.split()))  

    except AttributeError:
        soup1='Cannot find such word! Check spelling.'

    return soup1 

def synonym(msg):
    synon=""
    list_synonyms = []
    wrd=msg.split()
    word = wrd[-1].strip()

    for syn in wordnet.synsets(word): 
        for lemm in syn.lemmas(): 
            list_synonyms.append(lemm.name())
    set_syn=set(list_synonyms) 
    c=1  
    for x in set_syn:
        if c==len(set_syn):
            synon=synon+x   
        else:
            synon=synon+x+","
        c=c+1   
    return(synon)        

def antonym(msg):
    ant=""
    list_antonyms = []
    wrd=msg.split()
    word = wrd[-1].strip()

    for syn in wordnet.synsets(word): 
        for lemm in syn.lemmas():
            if lemm.antonyms(): 
                list_antonyms.append(lemm.antonyms()[0].name())

    set_ant=set(list_antonyms) 
    c=1  
    for x in set_ant:
        if c==len(set_ant):
            ant=ant+x   
        else:
            ant=ant+x+","
        c=c+1   
    return(ant)        

def get_category(categry):
    cat = {'1':'',
            '2':'national',
            '3':'business',
            '4':'sports',
            '5':'world',
            '6':'politics',
            '7':'technology',
            '8':'startup',
            '9':'entertainment',
            '10':'miscellaneous',
            '11':'hatke',
            '12':'science',
            '13':'automobile'
            }
    return(cat.get(categry))

def category():
    ChatLog.config(state=NORMAL)
    res="Select the category:\n1.All news\n2.India\n3.Business\n4.Sports\n5.World\n6.Politics\n7.Technology\n8.Startup\n9.Entertainment\n10.Miscellaneous\n11.Hatke\n12.Science\n13.Automobile"    
    ChatLog.insert(END, "Bot: " + res + '\n\n')
    
    """msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    #ChatLog.config(state=DISABLED)
    ChatLog.yview(END)   
    cat=get_category(msg)
    return cat"""

count = 0
def news(wrd):
    global message
    global count
    ct=wrd.strip()
    dummy_url="https://inshorts.com/en/read/"+ct
    data_dummy=requests.get(dummy_url)
    soup=BeautifulSoup(data_dummy.content,'html.parser')
    #print(soup.prettify)
    #print(soup)
    sent=message.split()
    print(sent)
    for x in sent:
        print(x)
        if x=="headline" or x=="headlines":
            #headlines
            headlines=""
            for i in range(1,5):
                news1=soup.find_all('div', class_=["news-card-title news-right-box"])[i]
                title=news1.find('span',attrs={'itemprop':"headline"}).string
                headlines= headlines + title +"\n\n"
            res=headlines    
        elif x=="news":
            #news
            news1=soup.find_all('div', class_=["news-card-content news-right-box"])[count]
            res=news1.find('div',attrs={'itemprop':"articleBody"}).string
            count=count+1
        else:
            pass  
    ChatLog.insert(END, "Bot: " + res + '\n\n\n\n')
 
    link.pack(side=BOTTOM)
    link.insert(END, "Click here for more")
    link.bind("<Button-1>", lambda e:webbrowser.open_new_tab(dummy_url))

    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)  

def get_language(language):
    lang = {'english':'en',
            'chinese':'zh-TW',
            'french':'fr',
            'german':'de',
            'gujarati':'gu',
            'japanese':'ja',
            'kannada':'kn',
            'malayalam':'ml',
            'marathi':'mr',
            'punjabi':'pa',
            'russian':'ru',
            'spanish':'es',
            'tamil':'ta',
            'telugu':'te',
            'korean':'ko',
            'hindi':'hi'
            }
    return lang.get(language)

def translateto(msg):
    global lang
    string =''
    sentence = msg
    words = sentence.split()
    length = len(words)
    #print(length)
    search_term = words[1:len(words)-2]
    # search_term = words[6:len(words)-2]
    for x in search_term:
        string+=' ' +x
    #print(string.strip())
    search_term = string.strip()
    if words[-2]=="in":
        language = sentence.split(" in ")[-1]
    elif words[-2]=="to":
        language = sentence.split(" to ")[-1]   
    #print(language)
    #url = "https://translate.google.co.in/?sl=auto&tl="+str(get_language(language))+"&text="+search_term+"&op=translate"
    #webbrowser.get().open(url)       

    translator= Translator(to_lang=str(get_language(language.lower())))
    translation = translator.translate(search_term)
    print(translation)
    return(translation)

def date():
    today = datetime.datetime.now()
    date = today.strftime("%B %d, %Y")
    day = today.strftime("%A")
    return(date+" "+day)

def day():
    x = datetime.datetime.now()
    day = x.strftime("%A")
    print(day)
    return("Today is " + day) 

def universaltime(msg):
    geolocator = Nominatim(user_agent="geoapiExercises")
    lad=msg.split("in")[-1].strip()
    location = geolocator.geocode(lad)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timeZ_Kl = pytz.timezone(result) 
    dt_Kl = datetime.datetime.now(timeZ_Kl)
    return("Time zone : " + result + "\n" + dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z'))

def curr_time(msg):
    search_term=msg.split()
    if len(search_term)<=4:   #what is the time in New York
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        #return(time.ctime())
        return(f"The time is {strTime}") 

def month():
    x = datetime.datetime.now()
    month = x.strftime("%B")
    return(month)         

def weather(msg):
    city1=msg.split("in")[-1]
    city2=city1.split("for")[-1]
    print("after split in/for",city2)
    if "weather" in city2 or "temperature" in city2:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        #region=data['region']
        city=data['city']
    else:
        city=city2        
    print(city)

    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # printing all data
    data= "Temperature is" + temp + "\nTime: " + time + "\nSky Description: " + sky + other_data
    return data
    """print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data) """

#tell me about something
def tell_me_about(msg):
    msg = msg.replace("tell me about","")
    try:
        results = wikipedia.summary(msg,sentences=3)    
        #print(results)
        #engine_speak(results) 
    except Exception:
        results = "Try saying what is" + msg
    return results

def who(msg):
    statement = msg.replace("who is","").replace("who's","").replace("who's a","").replace("who is a","").replace("?","").replace("!","")
    try:
        result = wikipedia.summary(statement,sentences=3)        
    except wikipedia.exceptions.PageError:
        result = "Try saying who is" + msg
    return result

def what(msg):
    statement = msg.replace("what is","").replace("what's","").replace("what's a","").replace("what is a","").replace("?","").replace("!","")
    try:
        result = wikipedia.summary(statement,sentences=3)        
    except wikipedia.exceptions.PageError:
        result = "Try saying who is" + msg
    return result

"""def enter_range():
    ChatLog.config(state=NORMAL)
    res="Enter the range Eg: 1 to 10"    
    ChatLog.insert(END, "Bot: " + res + '\n\n')"""

def where_am_i():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    region=data['region']
    city=data['city']
    res = f"You must be somewhere in {city},{region}"
    return res

def random_number_selection(msg):
    msg=msg.split()
    if(len(msg)>3 or len(msg)<3):
        ChatLog.insert(END, "Bot: " + "Invalid option." + '\n\n')
    else:
        start = int(msg[0])
        end = int(msg[2])
        n=random.randrange(start,end+1)
        print(n)
        ChatLog.insert(END, "Bot: " + str(n) + '\n\n')

def tossacoin():
    moves=["head", "tails"]   
    cmove=random.choice(moves)
    return(cmove)

def get_operator_fn(op):
    return {'+' : operator.add,
            'plus': operator.add,
            'add' : operator.add,
            '-' : operator.sub,
            'minus' : operator.sub,
            'subtract' : operator.sub,
            'x' : operator.mul,
            'multiply' : operator.mul,
            'multiplied' : operator.mul,
            'into' : operator.mul,
            '*' : operator.mul,
            'divide' :operator.__truediv__,
            'divided' :operator.__truediv__,
            '/' :operator.__truediv__,
            'by' :operator.__truediv__,
            'Mod' : operator.mod,
            'mod' : operator.mod,
            '^' : operator.xor,
            'power':operator.pow,
            'raised':operator.pow,
            'raise':operator.pow
            }[op]

def eval_binary_expr(op1,oper,op2):
    try:
        op1,op2 = float(op1),float(op2)
        if(math.ceil(op1)==math.floor(op1)):
            op1=int(op1)
        if(math.ceil(op2)==math.floor(op2)):
            op2=int(op2)    
        return get_operator_fn(oper)(op1,op2)
    except ValueError as ve:
        res = "Please provide valid numbers."  
    except ZeroDivisionError:
        res = "Dividing any number by zero does not make sense.There's no solution,so any non-zero number divided by 0 is undefined."    
    except ArithmeticError:
        return True  
    return(res)
#calculator
def calculator1(msg):
    msg=msg.lower()
    oprs = msg.split()
    print(oprs)
    if len(oprs)==3:
        res = eval_binary_expr(oprs[0],oprs[1],oprs[2])
        if res is True:
            result = "Sorry,cannot perform the operation"
        elif res is not None:
            if type(res)==float: #isinstance(res,float):
                res= round(res,4)
            result = str(res)
    elif len(oprs)==4:
        res = eval_binary_expr(oprs[1],oprs[2],oprs[3])    
        if res is True:
            result = "Sorry,cannot perform the operation"
        elif res is not None:
            if type(res)==float: #isinstance(res,float):
                res= round(res,4)
            result = str(res)
    else:
        result = "Invalid expression"
    return(result)

"""def calculator2(msg):
    msg=msg.lower()
    oprs = msg.split()
    if len(oprs)==4:
        res = eval_binary_expr(oprs[1],oprs[2],oprs[3])
        if res is True:
            result = "Sorry,cannot perform the operation"
        elif res is not None:
            if type(res)==float: #isinstance(res,float):
                res= round(res,4)
            result = str(res)
    else:
        result = "Invalid expression"
    return(result)
"""
def calculator3(msg):
    msg=msg.lower()
    opr = msg.split()
    if len(opr)==4:
        result = eval_binary_expr(opr[1], opr[0], opr[3])
        if result is True:
            result = "Sorry,cannot perform the operation"
        elif result is not None:
            if type(result)==float: #isinstance(res,float):
                result= round(result,4)
            result = str(result)
    else:
        result = "Invalid expression"
    return(result)  

def calculator4(msg):
    msg=msg.lower()
    opr = msg.split()
    if len(opr)==4:
        result = eval_binary_expr(opr[0], opr[1], opr[3])
        if result is True:
            result = "Sorry,cannot perform the operation"
        elif result is not None:
            if type(result)==float: #isinstance(res,float):
                result = round(result,4)
            result = str(result)
    elif len(opr)==5:
        result = eval_binary_expr(opr[1], opr[2], opr[4])
        if result is True:
            result = "Sorry,cannot perform the operation"
        elif result is not None:
            if type(result)==float: #isinstance(res,float):
                result= round(result,4)
            result = str(result)
    else:
        result = "Invalid expression"
    return(result)            

def calculator5(msg):
    msg=msg.lower()
    opr2 = msg.split()
    if len(opr2)==4:
        result2 = eval_binary_expr(opr2[3],opr2[0],opr2[1])
        if result2 is True:
            result = "Sorry,cannot perform the operation"
        elif result2 is not None:
            if type(result2)==float: #isinstance(res,float):
                result2= round(result2,4)
            result = str(result2)
    else:
        result = "Invalid expression"
    return(result)

def calculator6(msg):
    msg=msg.lower()
    opr3 = msg.split()
    if len(opr3)==4:
        result3 = eval_binary_expr(opr3[1],opr3[0],opr3[3])
        if result3 is True:
            result = "Sorry,cannot perform the operation"
        elif result3 is not None:
            if type(result3)==float: #isinstance(res,float):
                result3= round(result3,4)
            result = str(result3)
    else:
        result = "Invalid expression"
    return(result)  

def calculator7(msg):
    msg=msg.lower()
    opr3 = msg.split()
    if len(opr3)==4:
        result3 = eval_binary_expr(opr3[1],opr3[0],opr3[3])
        if result3 is True:
            result = "Sorry,cannot perform the operation"
        elif result3 is not None:
            if type(result3)==float: #isinstance(res,float):
                result3= round(result3,4)
            result = str(result3)
    else:
        result = "Invalid expression"
    return(result)         

def calculator8(msg):
    msg=msg.lower()
    search_term = msg.replace("how","").replace("many","").replace("degrees","").replace("degree","").replace("is","").replace("radians","").replace("radian","")
    try:
        search_term = float(search_term)
        if(math.floor(search_term)==math.ceil(search_term)):
            search_term = int(search_term)
        #else:
            #pass #engine_speak("I did not get that. Could you please repeat?")
        result = str(round(math.degrees(search_term),4))
    except ValueError as ve:
        result = "Please provide valid numbers."
    return(result)

def calculator9(msg):
    msg=msg.lower()
    search_term = msg.split()
    try: 
        search_term[0] = float(search_term[0])
        if(math.floor(search_term[0])==math.ceil(search_term[0])):
            search_term[0] = int(search_term[0])
        #else:
            #engine_speak("I did not get that. Could you please repeat?")
        result = str(round(math.degrees(search_term[0]),4))
    except ValueError as ve:
        result = "Please provide valid numbers."
    return(result)

def calculator10(msg):
    msg=msg.lower()
    search_term = msg.replace("how","").replace("many","").replace("degrees","").replace("degree","").replace("is","").replace("radians","").replace("radian","")
    try: 
        search_term = float(search_term)
        if(math.floor(search_term)==math.ceil(search_term)):
            search_term = int(search_term)
        #else:
            #engine_speak("I did not get that. Could you please repeat?")
        result = str(round(math.radians(search_term),4))
    except ValueError as ve:
        result = "Please provide valid numbers."
    return(result)        


def calculator11(msg):
    msg=msg.lower()
    search_term = msg.split()
    try:
        search_term[0] = float(search_term[0])
        if(math.floor(search_term[0])==math.ceil(search_term[0])):
            search_term[0] = int(search_term[0])
            result  = str(round(math.radians(search_term[0]),4))
    except ValueError as ve:
        result = "Please provide valid numbers." 
    return(result)

def calculator12(msg):
    msg=msg.lower()
    operator = msg.split("of")[-1]
    operator = float(operator)
    if(math.floor(operator)==math.ceil(operator)):
        result = math.factorial(int(operator))
        operator = int(operator)
        result = "factorial of " + str(operator) + " is " + str(result)
    else:
        result = "Please provide an integer number"
    return(result)

def category_quotes(msg):
    global tag_name
    flag=0
    if len(msg)>1:
        userquery=msg.lower().split()
        cat_list=["love","life","inspirational","inspiring","inspiration","humor","humorous","truth","honesty","wisdom","poetry","hope","hopeful","death","happiness","faith","life","lessons","motivational","motivation","motivating","relationships","writing","spirituality","success","time","knowledge","science","funny","friends","friendship","positive","positivity"]
        for x in userquery:
            for y in cat_list:
                if x==y:
                    tag_name=""
                    scrape_quotes(y) 
                    flag=1   
        if flag==0:
            ChatLog.config(state=NORMAL)
            res="Select the category:\n1.All\n2.Love\n3.Life\n4.Inspirational\n5.Humor\n6.Truth\n7.Wisdom\n8.Poetry\n9.Hope\n10.Death\n11.Happiness\n12.Faith\n13.Life Lessons\n14.Motivational\n15.Relationships\n16.Writing\n17.Spirituality\n18.Success\n19.Time\n20.Knowledge\n21.Science\n22.Funny\n23.Friends\n24.Positive"
            ChatLog.insert(END, "Bot: " + res + '\n\n')
                        
    else:                
        ChatLog.config(state=NORMAL)
        res="Select the category:\n1.All\n2.Love\n3.Life\n4.Inspirational\n5.Humor\n6.Truth\n7.Wisdom\n8.Poetry\n9.Hope\n10.Death\n11.Happiness\n12.Faith\n13.Life Lessons\n14.Motivational\n15.Relationships\n16.Writing\n17.Spirituality\n18.Success\n19.Time\n20.Knowledge\n21.Science\n22.Funny\n23.Friends\n24.Positive"
        ChatLog.insert(END, "Bot: " + res + '\n\n')

def get_tag(quotetag):
    cat =  {'1':'',
            '2':'love',
            '3':'life',
            '4':'inspirational',
            '5':'humor',
            '6':'truth',
            '7':'wisdom',
            '8':'poetry',
            '9':'hope',
            '10':'death',
            '11':'happiness',
            '12':'faith',
            '13':'life-lessons',
            '14':'motivational',
            '15':'relationships',
            '16':'writing',
            '17':'spirituality',
            '18':'success',
            '19':'time',
            '20':'knowledge',
            '21':'science',
            '22':'funny',
            '23':'friends',
            '24':'positive'
            }
    return(cat.get(quotetag))    
page_num=1
c=0
combined_list=[]
#page_num=1,c,i
def scrape_quotes(wrd):
    global c
    global page_num
    global combined_list
    authors = []
    quotes = []
    
    ct=wrd.strip()
    if (ct=="inspiring" or ct=="inspiration"):
        ct="inspirational"
    elif ct=="humorous":
        ct="humor"
    elif ct=="honesty":
        ct="truth"    
    elif ct=="hopeful":
        ct="hope" 
    elif ct=="lessons":
        ct="life-lessons" 
    elif (ct=="motivation" or ct=="motivating"):
        ct="motivational" 
    elif ct=="positivity":
        ct="positive"  
    elif ct=="friendship":
        ct="friends"                        
    
    if len(combined_list)==0:
        page_num=random.randrange(1,21)
    page_number=str(page_num) #Convert the page number to a string
    URL = 'https://www.goodreads.com/quotes/tag/'+ ct +'?page='+page_number #append the page number to complete the URL
    webpage = requests.get(URL)  #Make a request to the website
    soup = BeautifulSoup(webpage.text, "html.parser") #Parse the text from the website
    quoteText = soup.find_all('div', attrs={'class':'quoteText'}) #Get the tag and it's class
    for i in quoteText:
        quote = i.text.strip().split('\n')[0]#Get the text of the current quote, but only the sentence before a new line
        author = i.find('span', attrs={'class':'authorOrTitle'}).text.strip()
        #print(quote)
        quotes.append(quote)
        #print(author)
        authors.append(author)

    for i in range(len(quotes)):
        combined_list.append(quotes[i]+'-'+authors[i])
    #Show the combined list
    ChatLog.insert(END, "Bot: " + combined_list[c] + '\n\n')
    #print(combined_list[c])
    c=c+1
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)  

def get_pitchfork(URL):
    #Create a Request object by gathering information from the URL below
    res = requests.get(URL + '/best/')
    
    #Check that the request worked (status code should be 200)
    if res.status_code == 200:
        #Convert the raw text into a BS object. This is much easier to sort through!
        best = BeautifulSoup(res.text, 'lxml')

        #All the albums or tracks have the following class tages
        class_tags = ['bnm-hero__review-block', 'bnm-small album-small', 'bnm-small track-small']

        #This is a list of all the entries, looping through this should gather all of the information
        reviews = best.find_all('div', {'class' : class_tags})
        
        
        #List to hold all of the dicationaries:
        all_dict = []
        count=0
        #For loop for each review. 
        for i, review in enumerate(reviews):
            
            #If it's one of the first 3, follow first strucutre, otherwise follow the second
            if i <= 2:
                entry = {
                #Artist
                'artist' : review.find_all(['h3'])[0].text,

                #Title of Album or Track
                'title' : review.find_all(['h3'])[1].text,

                #Album or track? This can be found in the URL
                'album_track' : review.find('a').attrs['href'].split('/')[2][:-1].title(),

                #Genre
                'genre' : [genre.text for genre in review.find_all('li', {'class' : 'genre-list__item'})],
                }
            else:
                entry = {
                #Artist
                'artist' : ', '.join([i.text for i in review.find_all(['ul'], {'class' : 'artist-list'})]),

                #Title of Album or Track
                'title' : review.find(['h2']).text,

                #Album or track? This can be found in the URL
                'album_track' : review.find('a').attrs['href'].split('/')[2][:-1].title(),

                #Genre
                'genre' : [genre.text for genre in review.find_all('li', {'class' : 'genre-list__item'})],

                }
            
            rev_res = requests.get(URL + review.find('a').attrs['href'])
            
            if rev_res.status_code == 200:
                rev = BeautifulSoup(rev_res.text, 'lxml')

                #Pitchfork Writer
                entry['author'] = rev.find('a', {'class': 'authors-detail__display-name'}).text
                    
            all_dict.append(entry)
            count=count+1
            if count==3:
                break
    #print(all_dict)
    return pd.DataFrame(all_dict)



def rock_paper_scissors(msg):
    msg=msg.lower()
    if msg=="scissors":
        msg="scissor"
    moves=["rock", "paper","scissor"]
    if msg not in moves:
        res = "Invalid move"
        ChatLog.insert(END, "Bot: " + res + '\n\n')
    else: 
        cmove=random.choice(moves)
        pmove=msg
        res = "The computer chose " + cmove
        res = res + "\nYou chose " + pmove
        #engine_speak("hi")
        if pmove==cmove:
            result = res + "\nThe match is draw"
        elif pmove== "rock" and cmove== "scissor":
            result = res + "\nPlayer wins"
        elif pmove== "rock" and cmove== "paper":
            result = res + "\nComputer wins"
        elif pmove== "paper" and cmove== "rock":
            result = res + "\nPlayer wins"
        elif pmove== "paper" and cmove== "scissor":
            result = res + "\nComputer wins"
        elif pmove== "scissor" and cmove== "paper":
            result = res + "\nPlayer wins"
        elif pmove== "scissor" and cmove== "rock":
            result = res + "\nComputer wins"
        ChatLog.insert(END, "Bot: " + result + '\n\n')

def botname():
    if person_obj.name:
        str=f"My name is {asis_obj.name}, thanks for asking, {person_obj.name}"
    else:
        str=f"My name is {asis_obj.name}. What's your name?" #incase you haven't provided your name.
    return str    

def username(msg):
    person_name = msg.split("is")[-1].split("am")[-1].strip().replace("myself","")
    ChatLog.insert(END, "Bot: " + "That's a beautiful name " + person_name + ". Nice to know you!" + '\n\n')
    person_obj.setName(person_name) # remember name in person object
    return ""

def myusername():
    if (person_obj.name):
        ChatLog.insert(END, "Bot: " + "Your name is " + person_obj.name + '\n\n')
    else:
        ChatLog.insert(END, "Bot: " + "You haven't told me your name.")     
    return ""   

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    print(results)
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    print(results)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json,msg):
    global tag_name
    tag = ints[0]['intent']
    print(tag)
    tag_name=tag
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            #print(tag)
            if(i['tag']=="facts"):
                return(randfacts.get_fact()) 
            if(i['tag']=="jokes"):
                return(pyjokes.get_joke(category="all"))     
            if(i['tag']=="wordmeaning"):
                return(word_meaning(msg))
            if(i['tag']=="wish"):
                return(wishMe()) 
            if(i['tag']=="botname"):
                return(botname())  
            if(i['tag']=="username"):
                return(username(msg))
            if(i['tag']=="myusername"):
                return(myusername())       
            if(i['tag']=="date"):
                return(date())     
            if(i['tag']=="day"):
                return(day())
            if(i['tag']=="month"):
                return(month())    
            if(i['tag']=="time"):   
                return(curr_time(msg)) 
            if(i['tag']=="universaltime"):
                return(universaltime(msg))
            if(i['tag']=="synonym"):
                return(synonym(msg))
            if(i['tag']=="antonym"):
                return(antonym(msg))    
            if(i['tag']=="translate"):
                return(translateto(msg))  
            if(i['tag']=="news"):
                category()
                return("Enter your choice")
            if(i['tag']=="weather"):
                return(weather(msg)) 
            if(i['tag']=="quotes"):
                category_quotes(msg)
                return("Enter your choice")   
            if(i['tag']=="information"):
                return(tell_me_about(msg))  
            if(i['tag']=="whois"):
                return(who(msg))  
            if(i['tag']=="whatis"):
                return(what(msg))  
            if(i['tag']=="random number"):
                return("Enter the range Eg: 1 to 10")
            if(i['tag']=="tossacoin"):
                return(tossacoin()) 
            if(i['tag']=="calculator1"):
                return(calculator1(msg))  
            if(i['tag']=="calculator3"):
                return(calculator3(msg)) 
            if(i['tag']=="calculator4"):
                return(calculator4(msg)) 
            if(i['tag']=="calculator5"):
                return(calculator5(msg)) 
            if(i['tag']=="calculator6"):
                return(calculator6(msg)) 
            if(i['tag']=="calculator7"):
                return(calculator7(msg)) 
            if(i['tag']=="calculator8"):
                return(calculator8(msg)) 
            if(i['tag']=="calculator9"):
                return(calculator9(msg)) 
            if(i['tag']=="calculator10"):
                return(calculator10(msg)) 
            if(i['tag']=="calculator11"):
                return(calculator11(msg))
            if(i['tag']=="calculator12"):
                return(calculator12(msg))
            if(i['tag']=="rock_paper_scissor"):
                return("Choose rock, paper or scissors")
            if(i['tag']=="where_am_i"):
                return(where_am_i())
            if(i['tag']=="userbored"):
               n=random.randint(1,3)  
               if n==1:
                   return("Choose rock, paper or scissors")
               if n==2:
                   return(randfacts.get_fact())
               if n==3:
                    return(pyjokes.get_joke(category="all"))       
            else:
                return(random.choice(i['responses']))
    else:
        noans=["Sorry, can't understand you", "Please give me more info", "Not sure I understand","Sorry, I didn't get you","Sorry, couldn't help you, please refer the Ask me section for help"]
        return(random.choice(noans))        
            
def chatbot_response(msg):
    global tag_name
    if tag_name=="news":
        c=get_category(msg)
        if c!=None:
            news(c)
            tag_name="" 
        else:
            ChatLog.config(state=NORMAL)   
            ChatLog.insert(END, "Bot: " + "Invalid option. Try choosing another" + '\n\n')
        res=""
    elif tag_name=="quotes":
        c=get_tag(msg)
        if c!=None:
            scrape_quotes(c)
            tag_name="" 
        else:
            ChatLog.config(state=NORMAL)   
            ChatLog.insert(END, "Bot: " + "Invalid option. Try choosing another" + '\n\n')
        res=""   
    elif tag_name=="random number":
        random_number_selection(msg)
        res="" 
        tag_name=""
    elif tag_name=="botname":
        person_name = msg.split("is")[-1].split("am")[-1].strip().replace("myself","")
        #person_name = msg.replace("my name is ","")  
        ChatLog.insert(END, "Bot: " + "That's a beautiful name " + person_name + ". Nice to know you!" + '\n\n')
        person_obj.setName(person_name) # remember name in person object        
        res=""
        tag_name=""    
    elif tag_name=="rock_paper_scissor":
        rock_paper_scissors(msg)
        res=""
        tag_name=""   
    else:
        ints = predict_class(msg, model)
        print(ints)
        res = getResponse(ints, intents,msg)
    return res


#Creating GUI with tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *


def send():
    link.delete("1.0","end")
    link.pack_forget()
    global message
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if not msg.isdigit():
        message = msg
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.tag_configure('tag-right', justify='right')
        ChatLog.insert(END, msg + " :You" + '\n\n','tag-right')
        ChatLog.config(foreground="#EAECEE", font=("Helvetica", 14))
          
        res = chatbot_response(msg)
        if res!= '':
            ChatLog.insert(END, "Bot: " + res + '\n\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)   

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Buddy'
person_obj.name = ""

base = Tk()
base.title("Buddy Bot")
base.geometry("400x500")
base.resizable(width=TRUE, height=TRUE) #FALSE
#w, h = base.winfo_screenwidth(), base.winfo_screenheight()
#base.geometry("%dx%d+0+0" % (w, h))

notebook = ttk.Notebook(base)
notebook.pack(fill=BOTH, expand=True)

tab1 = ttk.Frame(notebook, width=800, height=800)
tab2 = ttk.Frame(notebook, width=800, height=800)

tab1.place(height="8", width="50")
tab2.place(height="8", width="50")

notebook.add(tab1, text='Buddy')
notebook.add(tab2, text='Ask Me')

#Create Chat window
ChatLog = Text(tab1, bd=10, bg="#17202A", height="8", width="50", font=("Helvetica",14),foreground="#EAECEE",wrap=WORD)
ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(tab1, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#text box for link
link= Text(ChatLog, bd=0, bg="white", height="1.5", width="50", font=('Arial', 12), fg="blue", cursor="hand2", wrap = WORD)

#Create Button to send message
SendButton = Button(tab1, font=("Verdana",12,'bold'), text="Send", width="12", height=3,
                    bd=7, bg="#A3AAB6", activebackground="#00bfff",fg='#2C3E50',
                    command= send)

#Create the box to enter message
EntryBox = Text(tab1, bd=0, bg="#2C3E50",width="25", height="3", font=("Arial",14), foreground="white",insertbackground="white")
#EntryBox.bind("<Return>", send)

#Place all components on the screen
"""scrollbar.place(x=375,y=5, height=385)
ChatLog.place(x=6,y=6, height=385, width=370)
EntryBox.place(x=128, y=400, height=88, width=260)
EntryBox.focus()
SendButton.place(x=6, y=400, height=88)"""

scrollbar.pack(side=RIGHT,fill=Y)
ChatLog.pack(side=TOP, fill=BOTH, expand=True)
EntryBox.pack(side=RIGHT, fill=BOTH, expand=True)
EntryBox.focus()
SendButton.pack(side=LEFT, fill=BOTH)

ChatLog.config(state=NORMAL)
ChatLog.insert(END, "Bot: " + "WELCOME BUDDY!" + '\n\n')
ChatLog.config(state=DISABLED)
ChatLog.yview(END)

Help = Text(tab2, bd=1, bg="#17202A", height="10", width="50", font=("Arial",14),foreground="white",wrap=WORD)
Help.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar2 = Scrollbar(tab2, command=Help.yview, cursor="heart")
Help['yscrollcommand'] = scrollbar2.set

"""scrollbar2.place(x=375,y=5, height=385)
Help.place(x=6,y=6, height=385, width=370)
"""

scrollbar2.pack(side=RIGHT,fill=Y)
Help.pack(side=TOP, fill=BOTH, expand=True)
Help.config(state=NORMAL)

Help.insert(END,"Name:"+"\n\n"+"botname, username"+"\n\n"+"Emotions"+"\n\n"+"I am angry"+"\n"+"I am happy"+"\n"+"I am sad"+"\n"+"I am lonely"+"\n"+"This is boring"+"\n\n"+"General:"+"\n\n"+"Weather,date,day,time,month"+"\n"+"Translate hello in (language)"+"\n\n"+"Entertainment"+"\n\n"+"Facts,Joke,Meaning,Toss a coin,Generate random number,Quotes,Rock paper scissor"+"\n\n"+"Information:"+"\n\n"+"Tell me about,what is,who is,News,Headlines"+"\n\n"+"Calculations")
Help.config(state=DISABLED)
"""ChatLog.pack(side=LEFT,fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT,fill=BOTH)
EntryBox.pack(side=RIGHT,fill=BOTH, expand=True)
SendButton.pack(side=LEFT,fill=BOTH,expand=True)"""

base.mainloop()