# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:16:12 2022

@author: Devanshu Roy
"""
import pytesseract
import image_to_lang

#linking tesseract to python with pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_img = ''

input_lang = ''

asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
          '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
        '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

ascii_braille = {asciicodes[i]:brailles[i] for i in range(len(asciicodes))}

def toBraille() :
    text = image_to_lang.returnTranslatedText('en', input_lang, path_to_img)
    conv_string = ""
    for char in text:
        char = char.lower()
        conv_string += ascii_braille[char]
    return conv_string
