""" Celem tego ćwiczenia jest odpowiedzenie na kilka pytań dotyczących informacji zawartych w bazie danych.
 Pytanie 1 Które opinie są średnio dłuższe, pozytywne czy negatywne?
 Pytanie 2 W których opiniach jest więcej przekleństw, w pozytywnych czy w negatywnych? Wiadomo:-)
 Pytanie 3 Ile razy wystąpiła fraza Polecam a ile Nie polecam """
import sqlite3
import numpy as np
from nltk.tokenize import word_tokenize
from sqlalchemy.orm import sessionmaker

connection = sqlite3.connect("sqlalchemy.db")
cursor = connection.cursor()

# # Ad Pytanie 1
# select_query1 = "SELECT * FROM MyTable where Sentiment = 1;"
# result_neg = cursor.execute(select_query1)
#
# lista_negative = []
# print(len([lista_negative.append(r) for r in result_neg])) # 514 tyle jest negatywnych opinii
#
# select_query2 = "SELECT * FROM MyTable where Sentiment = 5;"
# result_pos = cursor.execute(select_query2)
#
# lista_positive = []
# print(len([lista_positive.append(r) for r in result_pos])) # 626 tyle jest pozytywnych opinii
#
# print(sum([len(i[1]) for i in lista_negative])/len(lista_negative)) # 539.40 Tyle jest średnio znaków w negatywnych opiniach
#
# print(sum([len(i[1]) for i in lista_positive])/len(lista_positive)) # 52.48 Tyle jest średnio znaków w pozytywnych opiniach

# Ad Pytanie 2

# bad_words = ['chuj','chuja', 'chujek', 'chuju', 'chujem', 'chujnia',
# 'chujowy', 'chujowa', 'chujowe', 'cipa', 'cipę', 'cipe', 'cipą',
# 'cipie', 'dojebać','dojebac', 'dojebie', 'dojebał', 'dojebal',
# 'dojebała', 'dojebala', 'dojebałem', 'dojebalem', 'dojebałam',
# 'dojebalam', 'dojebię', 'dojebie', 'dopieprzać', 'dopieprzac',
# 'dopierdalać', 'dopierdalac', 'dopierdala', 'dopierdalał',
# 'dopierdalal', 'dopierdalała', 'dopierdalala', 'dopierdoli',
# 'dopierdolił', 'dopierdolil', 'dopierdolę', 'dopierdole', 'dopierdoli',
# 'dopierdalający', 'dopierdalajacy', 'dopierdolić', 'dopierdolic',
# 'dupa', 'dupie', 'dupą', 'dupcia', 'dupeczka', 'dupy', 'dupe', 'huj',
# 'hujek', 'hujnia', 'huja', 'huje', 'hujem', 'huju', 'jebać', 'jebac',
# 'jebał', 'jebal', 'jebie', 'jebią', 'jebia', 'jebak', 'jebaka', 'jebal',
# 'jebał', 'jebany', 'jebane', 'jebanka', 'jebanko', 'jebankiem',
# 'jebanymi', 'jebana', 'jebanym', 'jebanej', 'jebaną', 'jebana',
# 'jebani', 'jebanych', 'jebanymi', 'jebcie', 'jebiący', 'jebiacy',
# 'jebiąca', 'jebiaca', 'jebiącego', 'jebiacego', 'jebiącej', 'jebiacej',
# 'jebia', 'jebią', 'jebie', 'jebię', 'jebliwy', 'jebnąć', 'jebnac',
# 'jebnąc', 'jebnać', 'jebnął', 'jebnal', 'jebną', 'jebna', 'jebnęła',
# 'jebnela', 'jebnie', 'jebnij', 'jebut', 'koorwa', 'kórwa', 'kurestwo',
# 'kurew', 'kurewski', 'kurewska', 'kurewskiej', 'kurewską', 'kurewska',
# 'kurewsko', 'kurewstwo', 'kurwa', 'kurwaa', 'kurwami', 'kurwą', 'kurwe',
# 'kurwę', 'kurwie', 'kurwiska', 'kurwo', 'kurwy', 'kurwach', 'kurwami',
# 'kurewski', 'kurwiarz', 'kurwiący', 'kurwica', 'kurwić', 'kurwic',
# 'kurwidołek', 'kurwik', 'kurwiki', 'kurwiszcze', 'kurwiszon',
# 'kurwiszona', 'kurwiszonem', 'kurwiszony', 'kutas', 'kutasa', 'kutasie',
# 'kutasem', 'kutasy', 'kutasów', 'kutasow', 'kutasach', 'kutasami',
# 'matkojebca', 'matkojebcy', 'matkojebcą', 'matkojebca', 'matkojebcami',
# 'matkojebcach', 'nabarłożyć', 'najebać', 'najebac', 'najebał',
# 'najebal', 'najebała', 'najebala', 'najebane', 'najebany', 'najebaną',
# 'najebana', 'najebie', 'najebią', 'najebia', 'naopierdalać',
# 'naopierdalac', 'naopierdalał', 'naopierdalal', 'naopierdalała',
# 'naopierdalala', 'naopierdalała', 'napierdalać', 'napierdalac',
# 'napierdalający', 'napierdalajacy', 'napierdolić', 'napierdolic',
# 'nawpierdalać', 'nawpierdalac', 'nawpierdalał', 'nawpierdalal',
# 'nawpierdalała', 'nawpierdalala', 'obsrywać', 'obsrywac', 'obsrywający',
# 'obsrywajacy', 'odpieprzać', 'odpieprzac', 'odpieprzy', 'odpieprzył',
# 'odpieprzyl', 'odpieprzyła', 'odpieprzyla', 'odpierdalać',
# 'odpierdalac', 'odpierdol', 'odpierdolił', 'odpierdolil',
# 'odpierdoliła', 'odpierdolila', 'odpierdoli', 'odpierdalający',
# 'odpierdalajacy', 'odpierdalająca', 'odpierdalajaca', 'odpierdolić',
# 'odpierdolic', 'odpierdoli', 'odpierdolił', 'opieprzający',
# 'opierdalać', 'opierdalac', 'opierdala', 'opierdalający',
# 'opierdalajacy', 'opierdol', 'opierdolić', 'opierdolic', 'opierdoli',
# 'opierdolą', 'opierdola', 'piczka', 'pieprznięty', 'pieprzniety',
# 'pieprzony', 'pierdel', 'pierdlu', 'pierdolą', 'pierdola', 'pierdolący',
# 'pierdolacy', 'pierdoląca', 'pierdolaca', 'pierdol', 'pierdole',
# 'pierdolenie', 'pierdoleniem', 'pierdoleniu', 'pierdolę', 'pierdolec',
# 'pierdola', 'pierdolą', 'pierdolić', 'pierdolicie', 'pierdolic',
# 'pierdolił', 'pierdolil', 'pierdoliła', 'pierdolila', 'pierdoli',
# 'pierdolnięty', 'pierdolniety', 'pierdolisz', 'pierdolnąć',
# 'pierdolnac', 'pierdolnął', 'pierdolnal', 'pierdolnęła', 'pierdolnela',
# 'pierdolnie', 'pierdolnięty', 'pierdolnij', 'pierdolnik', 'pierdolona',
# 'pierdolone', 'pierdolony', 'pierdołki', 'pierdzący', 'pierdzieć',
# 'pierdziec', 'pizda', 'pizdą', 'pizde', 'pizdę', 'piździe', 'pizdzie',
# 'pizdnąć', 'pizdnac', 'pizdu', 'podpierdalać', 'podpierdalac',
# 'podpierdala', 'podpierdalający', 'podpierdalajacy', 'podpierdolić',
# 'podpierdolic', 'podpierdoli', 'pojeb', 'pojeba', 'pojebami',
# 'pojebani', 'pojebanego', 'pojebanemu', 'pojebani', 'pojebany',
# 'pojebanych', 'pojebanym', 'pojebanymi', 'pojebem', 'pojebać',
# 'pojebac', 'pojebalo', 'popierdala', 'popierdalac', 'popierdalać',
# 'popierdolić', 'popierdolic', 'popierdoli', 'popierdolonego',
# 'popierdolonemu', 'popierdolonym', 'popierdolone', 'popierdoleni',
# 'popierdolony', 'porozpierdalać', 'porozpierdala', 'porozpierdalac',
# 'poruchac', 'poruchać', 'przejebać', 'przejebane', 'przejebac',
# 'przyjebali', 'przepierdalać', 'przepierdalac', 'przepierdala',
# 'przepierdalający', 'przepierdalajacy', 'przepierdalająca',
# 'przepierdalajaca', 'przepierdolić', 'przepierdolic', 'przyjebać',
# 'przyjebac', 'przyjebie', 'przyjebała', 'przyjebala', 'przyjebał',
# 'przyjebal', 'przypieprzać', 'przypieprzac', 'przypieprzający',
# 'przypieprzajacy', 'przypieprzająca', 'przypieprzajaca',
# 'przypierdalać', 'przypierdalac', 'przypierdala', 'przypierdoli',
# 'przypierdalający', 'przypierdalajacy', 'przypierdolić',
# 'przypierdolic', 'qrwa', 'rozjebać', 'rozjebac', 'rozjebie',
# 'rozjebała', 'rozjebią', 'rozpierdalać', 'rozpierdalac', 'rozpierdala',
# 'rozpierdolić', 'rozpierdolic', 'rozpierdole', 'rozpierdoli',
# 'rozpierducha', 'skurwić', 'skurwiel', 'skurwiela', 'skurwielem',
# 'skurwielu', 'skurwysyn', 'skurwysynów', 'skurwysynow', 'skurwysyna',
# 'skurwysynem', 'skurwysynu', 'skurwysyny', 'skurwysyński',
# 'skurwysynski', 'skurwysyństwo', 'skurwysynstwo', 'spieprzać',
# 'spieprzac', 'spieprza', 'spieprzaj', 'spieprzajcie', 'spieprzają',
# 'spieprzaja', 'spieprzający', 'spieprzajacy', 'spieprzająca',
# 'spieprzajaca', 'spierdalać', 'spierdalac', 'spierdala', 'spierdalał',
# 'spierdalała', 'spierdalal', 'spierdalalcie', 'spierdalala',
# 'spierdalający', 'spierdalajacy', 'spierdolić', 'spierdolic',
# 'spierdoli', 'spierdoliła', 'spierdoliło', 'spierdolą', 'spierdola',
# 'srać', 'srac', 'srający', 'srajacy', 'srając', 'srajac', 'sraj',
# 'sukinsyn', 'sukinsyny', 'sukinsynom', 'sukinsynowi', 'sukinsynów',
# 'sukinsynow', 'śmierdziel', 'udupić', 'ujebać', 'ujebac', 'ujebał',
# 'ujebal', 'ujebana', 'ujebany', 'ujebie', 'ujebała', 'ujebala',
# 'upierdalać', 'upierdalac', 'upierdala', 'upierdoli', 'upierdolić',
# 'upierdolic', 'upierdoli', 'upierdolą', 'upierdola', 'upierdoleni',
# 'wjebać', 'wjebac', 'wjebie', 'wjebią', 'wjebia', 'wjebiemy',
# 'wjebiecie', 'wkurwiać', 'wkurwiac', 'wkurwi', 'wkurwia', 'wkurwiał',
# 'wkurwial', 'wkurwiający', 'wkurwiajacy', 'wkurwiająca', 'wkurwiajaca',
# 'wkurwić', 'wkurwic', 'wkurwi', 'wkurwiacie', 'wkurwiają', 'wkurwiali',
# 'wkurwią', 'wkurwia', 'wkurwimy', 'wkurwicie', 'wkurwiacie', 'wkurwić',
# 'wkurwic', 'wkurwia', 'wpierdalać', 'wpierdalac', 'wpierdalający',
# 'wpierdalajacy', 'wpierdol', 'wpierdolić', 'wpierdolic', 'wpizdu',
# 'wyjebać', 'wyjebac', 'wyjebali', 'wyjebał', 'wyjebac', 'wyjebała',
# 'wyjebały', 'wyjebie', 'wyjebią', 'wyjebia', 'wyjebiesz', 'wyjebie',
# 'wyjebiecie', 'wyjebiemy', 'wypieprzać', 'wypieprzac', 'wypieprza',
# 'wypieprzał', 'wypieprzal', 'wypieprzała', 'wypieprzala', 'wypieprzy',
# 'wypieprzyła', 'wypieprzyla', 'wypieprzył', 'wypieprzyl', 'wypierdal',
# 'wypierdalać', 'wypierdalac', 'wypierdala', 'wypierdalaj',
# 'wypierdalał', 'wypierdalal', 'wypierdalała', 'wypierdalala',
# 'wypierdalać', 'wypierdolić', 'wypierdolic', 'wypierdoli',
# 'wypierdolimy', 'wypierdolicie', 'wypierdolą', 'wypierdola',
# 'wypierdolili', 'wypierdolił', 'wypierdolil', 'wypierdoliła',
# 'wypierdolila', 'zajebać', 'zajebac', 'zajebie', 'zajebią', 'zajebia',
# 'zajebiał', 'zajebial', 'zajebała', 'zajebiala', 'zajebali', 'zajebana',
# 'zajebani', 'zajebane', 'zajebany', 'zajebanych', 'zajebanym',
# 'zajebanymi', 'zajebiste', 'zajebisty', 'zajebistych', 'zajebista',
# 'zajebistym', 'zajebistymi', 'zajebiście', 'zajebiscie', 'zapieprzyć',
# 'zapieprzyc', 'zapieprzy', 'zapieprzył', 'zapieprzyl', 'zapieprzyła',
# 'zapieprzyla', 'zapieprzą', 'zapieprza', 'zapieprzy', 'zapieprzymy',
# 'zapieprzycie', 'zapieprzysz', 'zapierdala', 'zapierdalać',
# 'zapierdalac', 'zapierdalaja', 'zapierdalał', 'zapierdalaj',
# 'zapierdalajcie', 'zapierdalała', 'zapierdalala', 'zapierdalali',
# 'zapierdalający', 'zapierdalajacy', 'zapierdolić', 'zapierdolic',
# 'zapierdoli', 'zapierdolił', 'zapierdolil', 'zapierdoliła',
# 'zapierdolila', 'zapierdolą', 'zapierdola', 'zapierniczać',
# 'zapierniczający', 'zasrać', 'zasranym', 'zasrywać', 'zasrywający',
# 'zesrywać', 'zesrywający', 'zjebać', 'zjebac', 'zjebał', 'zjebal',
# 'zjebała', 'zjebala', 'zjebana', 'zjebią', 'zjebali', 'zjeby']
#
#
# select_query = "SELECT MyTable.Opinion FROM MyTable where Sentiment = 1;"
# result = cursor.execute(select_query)
#
# res = [''.join(i) for i in list(result)]
#
# bw = []
# def profanity_checker(text):
#     text = text.split()
#     for word in text:
#         if word in bad_words:
#             bw.append(word)
#     return bw
#
# for string in res:
#     resultat = profanity_checker(string)
#
# print(resultat)

# # Ad Pytanie 3

# select_query = "SELECT MyTable.Opinion FROM MyTable where Sentiment = 1 and Opinion like '%nie polecam%';"
# result = cursor.execute(select_query)
# print(len([''.join(i) for i in list(result)]))
#
# select_query = "SELECT MyTable.Opinion FROM MyTable where Sentiment = 5 and Opinion like '%polecam%'" \
#                " and Opinion not like '%nie polecam%';"
# result = cursor.execute(select_query)
# print(len([''.join(i) for i in list(result)]))
#
# cursor.close()
# connection.close()