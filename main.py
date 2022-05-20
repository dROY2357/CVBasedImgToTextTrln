from image_to_lang import returnTranslatedText

path_to_img_main = "./hindi_test2.jpg"

input_choice = input("Translate Image text to: \n1. Language\n2. Braille\nYour input: ")

if input_choice == '1':
    to_lang = input("Enter the to_lang:")
    from_lang = input("Enter the from_lang:")
    import image_to_lang
    image_to_lang.imageToLang(to_lang, from_lang, path_to_img_main)
elif input_choice == '2':
    ocr_input_lang = input("Enter the image language:")
    import braille
    braille.input_lang = ocr_input_lang
    braille.path_to_img = path_to_img_main
    print("Text in image translated to English:")
    print(returnTranslatedText('en', ocr_input_lang, path_to_img_main))
    print("Detected text in Braille is:")
    print(braille.toBraille())
else:
    print("The input choice is invalid")
