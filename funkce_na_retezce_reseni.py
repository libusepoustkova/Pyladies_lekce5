# Napis funkci, ktera prevede text na velka pismena.
def upper_char(retezec):
    return retezec.upper()


# Napis funkci, ktera pocita pocet znaku v retezci.
def count_char(retezec):
    return len(retezec)


# Napis funcki, ktera pocita pocet mezer v retezci
def count_spaces(retezec):
    return retezec.count(' ')


# Napis funcki, ktera pocita pocet "samohlasek"
def count_aeiou(retezec):
    samohlasky = 'aeiouAEIOU'
    pocet = 0
    for i in retezec:
        if i in samohlasky:
            pocet = pocet + 1
    return pocet


# Napis funkci, ktera obrati retezec
def reverse_string(retezec):
    return retezec[::-1]


# Napis funkci, ktera vlozi retezec doprostred jineho retezce.
def string_in_string(ret,retvloz):
    stred = count_char(ret)//2
    return ret[:stred] + retvloz + ret [stred:]


# Napis funkci, ktera prehodi tecku a carku v retezci
def swap_dot_comma(retezec):
    maketrans = str.maketrans()
    return retezec.translate.maketrans((',.', '.,'))



retezec_znaku = 'pokus'
print(reverse_string('pokus'))
print(upper_char(rezetec_znaku))
print(count_char('pokus'))
print(count_spaces('pok \n us \t'))
print(count_aeiou('pokus'))
print(string_in_string('pokusy', 'ahoj'))
print(swap_dot_comma("ahoj, libo."))