# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:20:07 2022

@author: Devanshu Roy
"""
#imports of all the required libraries
import cv2 #opencv
import pytesseract
from gtts import gTTS
from playsound import playsound
import os
from translate import Translator
from langdetect import detect

#linking tesseract to python with pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_img = ""

def imageToLang(to_lang, ocr_lang, path_to_img):

    #reading the image using opencv
    img = cv2.imread(path_to_img)

    #showing the image - not compulsory
    cv2.imshow("Image", img)

    #setting language
    tes_lang = 'en'

    #using Tesseractv5 OCR to detect and recognize the chars in image
    text = pytesseract.image_to_string(img, lang=ocr_lang)
    from_lang = detect(text)

    #detecting OCR language
    print('Detected language =', detect(text))

    #printing the detected text - unnecessary
    print(text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    current = 'This is the original language'
    new = 'And now, this is the translation'
    current_info = gTTS(current, lang = from_lang)
    current_info.save('current.mp3')
    audio_info = gTTS(text, lang = from_lang)
    audio_info.save('output.mp3')
    new_info = gTTS(new, lang = 'en')
    new_info.save('next.mp3')

    translator = Translator(from_lang = from_lang, to_lang = to_lang)
    translated_lang = translator.translate(text)
    print("The translated text is: ")
    print(translated_lang)
    translated_info = gTTS(translated_lang, lang='en')
    translated_info.save('translated.mp3')
    #playsound('C:/dROY_stuff/Education/MajorProject/Code/MajorProj/current.mp3')
    playsound('./output.mp3')
    #playsound('C:/dROY_stuff/Education/MajorProject/Code/MajorProj/next.mp3')
    playsound('./translated.mp3')
    os.remove('current.mp3')
    os.remove('output.mp3')
    os.remove('next.mp3')
    os.remove('translated.mp3')

def returnTranslatedText(to_lang, ocr_lang, path_to_img):

    #reading the image using opencv
    img = cv2.imread(path_to_img)

    #showing the image - not compulsory
    cv2.imshow("Image", img)

    #setting language
    tes_lang = 'en'

    #using Tesseractv5 OCR to detect and recognize the chars in image
    text = pytesseract.image_to_string(img, lang=ocr_lang)
    from_lang = detect(text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    translator = Translator(from_lang = from_lang, to_lang = to_lang)
    translated_lang = translator.translate(text)

    return translated_lang