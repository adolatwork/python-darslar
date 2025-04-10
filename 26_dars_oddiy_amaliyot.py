import random as r

words = ["salom", "olma", "nok", "un", "anor"]


def chiziq_yasovchi(n):
    char = ""
    for i in range(n):
        char += "-"
    return char

def chiziqni_uzgartiruvchi(idx, letter, char):
    new_char = ""
    for i, _ in enumerate(char):
        if i == idx:
            new_char += letter
        else:
            new_char += _

    return new_char


def func():
    num = r.randint(0, len(words)-1)
    print("num:", num)
    
    word = words[num]
    print("word:", word)
    word_len = len(word)
    
    char = chiziq_yasovchi(word_len)
    print("char:", char)
    
    print("\n\n")
    
    print(f"Men {word_len} xonali so'z o'yladim topa olasizmi?")
    
    text = (
        f"Harf kiriting! {char}: "
    )
    
    counter = 0
    
    while True:
        counter += 1
        answer = input(text)
        
        if len(answer) > 1:
            print("Iltimos bitta harf kiriting.")
            continue
        
        word_dict = {}
        
        if answer in word:
            for idx, letter in enumerate(word):
                if answer == letter:
                    word_dict[idx] = letter
                    print("martta", counter)
                    char = chiziqni_uzgartiruvchi(idx, letter, char)
                    text = (
                        f"Bitta harf kiriting! {char}: "
                    )
        else:
            print("Bu harf so'z ichida yo'q.")
            continue

    return

func()

print("Ofarin! Siz yutdingiz rahmat uyin uynaganingiz uchun 😍 ") 





































