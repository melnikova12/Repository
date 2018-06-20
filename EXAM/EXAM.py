#задание 1

import os
import re

#восстановление исходного текста
#исходная директория - папка news - код должен лежать в ней 

def file1():
    with open ("itartass1.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "itartass1.html")
        b = re.findall('title>(.*?)</title', "itartass1.html")
        row = a + b 
        text = text.replace(row, '')
    return text


def file2():
    with open ("itartass2.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "itartass2.html")
        b = re.findall('title>(.*?)</title', "itartass2.html")
        row = a + b 
        text = text.replace(row, '')
    return text
    
def file3():
    with open ("itartass3.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "itartass3.html")
        b = re.findall('title>(.*?)</title', "itartass3.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file4():
    with open ("itartass4.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "itartass4.html")
        b = re.findall('title>(.*?)</title', "itartass4.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file5():
    with open ("itartass5.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "itartass5.html")
        b = re.findall('title>(.*?)</title', "itartass5.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file6():
    with open ("rbk2.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rbk2.html")
        b = re.findall('title>(.*?)</title', "rbk2.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file7():
    with open ("rbk3.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rbk3.html")
        b = re.findall('title>(.*?)</title', "rbk3.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file8():
    with open ("rbk4.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rbk4.html")
        b = re.findall('title>(.*?)</title', "rbk4.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file9():
    with open ("rbk6.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rbk6.html")
        b = re.findall('title>(.*?)</title', "rbk6.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file10():
    with open ("rbk7.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rbk7.html")
        b = re.findall('title>(.*?)</title', "rbk7.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file11():
    with open ("rian1.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rian1.html")
        b = re.findall('title>(.*?)</title', "rian1.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file12():
    with open ("rian2.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rian2.html")
        b = re.findall('title>(.*?)</title', "rian2.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file13():
    with open ("rian3.html", encoding = 'utf-8') as f:
        text = f.read().lower()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rian3.html")
        b = re.findall('title>(.*?)</title', "rian3.html")
        row = a + b 
        text = text.replace(row, '')
    return text

def file14():
    with open ("rian5.html", encoding = 'utf-8') as f:
        text = f.read()
        symbols_to_remove = """`"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        a = re.findall('meta content="(.*?)" ', "rian5.html")
        b = re.findall('title>(.*?)</title', "rian5.html")
        row = a + b 
        text = text.replace(row, '')
    return text


def all_files():
    k = file1() + file2() + file3() + file4() + file5() + file6() + file7() + file8() + file9() + file10() + file11() + file12() + file13() + file14()
    return k
all_files()


def write_in_file(k):
    with open ('news.txt', 'w', encoding = 'ср1251') as f:
        f = f.write(k)
    return f 

write_in_file(k)



        
