from abc import ABC, abstractmethod
"""
1. Range funsiyasi nima va u qanday parametorlari bor ?
"""

# Range funksiyasi ma'lum oraliqdagi sonlarni yaratish uchun ishlatiladi.
# Va unda uchta parametorlari bor va ulaarning nomalri START, STOP, STEP, 
# Start ning defaulti 0 bolib uni ozgartirish mumku start malum bir sondan boshlab sanash uchun beriladi
# Stop bu majburiy parametor bolib startdan boshlab malum bir raqamlargachan bolgan raqamlar yaratiladi
# Step bu malum bir son orqali qadam berasiz va shu reaqam boylab sanaydi masalan stepga 3 bersangiz u startdan boshlab stopgacha uchta raqam tashlab sanaydi


"""
2. Pythonning asosiy xususiyatlari qanday?
"""

# Python - mashhur dasturlash tili. U Guido van Rossum tomonidan yaratilgan va 1991 yilda chiqarilgan.

# Python deyarliy hamma ooperatsiyon sistamalarida ishlaydi massaln (Windows, Mac, Linux, Respberry Pi, va hokazo)
# Python ingliz tiliga o'xshash oddiy sintaksisga ega.
# Python interpritator tizimida ishlaydi, ya'ni kod yozilishi bilanoq bajarilishi mumkin. Bu prototip yaratish juda tez bo'lishi mumkinligini anglatadi.
# Python functsiyonal va OOP yonalishida ishlashi mumkin

"""
3. Python moduli nima
"""

# Proektizga kiritmoqchi bo'lgan funktsiyalar to'plamini o'z ichiga olgan fayl.
# Modulni hamma funcsiylarini faylda ishlatish uchun importni ishlatish kerag
# Modulni faylda ishlatayotkanda modulni ismni yozim nuxta qoyib kegin modldagi keragli funksiyani nomini yozish kerag

"""
4. Gitni qanday ishlatadi?
"""  

# Git - bu bepul, ochiq manbali, Linus Torvalds tomonidan 2005 yilda yaratilgan versiyani boshqarish tizimi yoki talqinlarni boshqarish tizimi.
# VCS asosan vaqt o'tishi bilan bir yoki bir nechta fayl ichidagi o'zgarishlarni yozib olish uchun mo'ljallangan dasturdir.

"""
5. 'is' bilan '==' farqi nimada? misol keltiring
"""

# '==' ozgaruvchini valuese boyicha tekshiradi lekin is uning 'id'si boyicha tekshiradi
#  masalan a = [10, 20, 30, 40] b = [10, 20, 30, 40] ani id boshq a bni id si boshqa bolgani uchun ham is False korsatade ammo == true qaytaradi
# id bu obektning identifikatori

"""
6. Qanday ozgaruvchi va ozgarmaydigon tiplar bor?
"""
# int, foat, bool, str, touple ozgarmaydiogoni tiplar
# list, dict, set, dict ozgaruvchi tiplar

# ozgaruvchi tiplarni indexi yooki keyi boyicha ozgartirib boladi 
# setni eleentni nomi bilan discard yoki remove orqali olib tashlay olasiz
# dictni esakey boyicha va listni indexsi boyicha

"""
7. Lambda funcsiya nima?
"""

# Lambda funsiya bu bir qatorli va qisqa funncsiya bolib unga uzun logika yoza olmaysiz
# Va lyambidada nomi bu qaysi ozgaruvchiga yozsangiz osha ozgaruvchining nomi lyambda funcsiyaning ismi bolib hisoblanadi

"""
8. Qnday qilib (set, dict, list)ning ozining kollektsiyalarini ishlatib boladi?
""" 

# Uning uchun siz ozgaruvchingizzni nomini yozib nuxta qoyib kegin metodini yozish kerag

#list

"""

append() - listga element koshadi
clear() - listdagi barcha elementlarni ochiradi
copy() - listdagi barcha elementlarni copy qiladi
count()	- listdagi elementlarni sanaydi
extend() - listga list koshish uchun agar 'dsf' bersa 'd' 's' 'f' qilib koshadi
index()	- listdagi elementning indexini korsatadi
insert() - birinchi index yozib kegin elementni yozish kere shunda indexiga eleent qoyadi
pop() - agar ichiqa indexini yozsez osha indexidagi elementni sug'irib beradi yoki ohiridagi elementni
remove() - aniq bir elementni ochirib tashlaydi
reverse() - listni ichidagi elemmentlarni teskari qilib beradi
sort() - sort metodi elementlarni osish tartibida sortlab beradi u ikta argument key (optional) va reverse True yoki False qabul qiladi

"""

# dictionary

"""

clear() - hamma elementlarni ochiradi
copy() - dictdagi hamma elementlarni copy qiladi
fromkeys() - from keysga element bergan holda dictgaa keylar yaratib beradi va hammasif\ga default qiymat bera olasiz
get() - keyga qarab element olb beradi
items()	- dictni key va valuesini tuple korinishda olib beradi
keys() - dictdagi barcha keylarni list korinishida olib beradi 
pop() - siz u erga keyni nomini yozsangiz u osha key va valueni sug'iriboladi
popitem() - dictnin ohiridan bita element sug'irib oladi
setdefault() - anik bir dictda key mavjud bosa u uni qaytaradi lekin unday key topilmasa u shunday key yaratib default qiymat qoyadi
update() - dictga dictni qoshib beradi
values() - hamma valuelarini listda  

""" 

# tuple

"""

count() - Belgilangan qiymat kortejda necha marta sodir bo'lishini qaytaradi
index() - Berilgan tupledagi elementning indexini qaytaradi

"""

# set

"""

add() - setga element koshib beradi
clear()	- setdagi hamma elementlarni ochirib tashlaydi
copy() - setdagi barcha elementlarni copy qiladi
difference() - (ozgaruvchiga olish kerag) ikinchi setda borini birinchi setda chiqormedi lekin qoganlarini chiqoradi
difference_update()	- (ozgaruvchiga olinmaydi) ikinchi setda borini birinchi setda chiqormedi lekin qoganlarini chiqoradi
discard() - (xato qaytarmaydi) elementni ochirish uchun ishlatiladi
intersection() -  (ozgaruvchiga olish kerag) birinchi va ikkinchi setda bor larni qaytaradi
intersection_update() - (ozgaruvchiga olinmaydi) birinchi va ikkinchi setda bor larni qaytaradi
isdisjoint() - agar ikkala setlarda birhil elementlar bolmasa True qaytaradi
issubset() - agar birinchi setdagi barcha elementlar ikkinchi elementning ichida bolsa True agar ikkinchi setda birinchi setdagi barcha elementlar bolmasa False qaytaradi
issuperset() - agar birinchi setda barcha ikkinchi setdagi elementlar bolsa True qaytaradi
pop() - pop setda ardument qabul qilmaydi va u setda qaysi element ohirgi bolib uchrgan bolsa oshani sug'irib beradi
remove() - remove aniq bir elementni ochirib tashlaydi
symmetric_difference() - (o'zgaruvchiga olish kerag) ikkala setda yoq bolgan elementlarni bita setda qaytaradi
symmetric_difference_update() - (o'zgaruvchiga olish kerag emas) ikkala setda yoq bolgan elementlarni bita setda qaytaradi
union()	- (o'zgaruvchiga olish kerag) ikta yoki undan ortiq setlarni birlashtirish uchun ishlatilinadi
update() - (ozgaruvchiga olinmaydi) aniq bir setga boshqa setni qoshish uchun ishatilinadi

"""

#OOP

# OOPda 4ta tamoyili bor va OOP class va methodlardan iborat

# Encapsulation - bu OOPning 4ta tamoilaridan biri bolib u classdagi Method yoki variableni protected yoki privat kilishi mumkun
# Protected degada bu masalan qaysidur method yoki veriableni boshiqa ikta paski chizig'cha qoysangiz u protected bolib hisoblanadi protectod
# Method yoki variableni o'zgartirib bolmaydi va uni boshqa classga voris qilish ilojisi yoq
# Privat method yoki variable yasash uchun methodni yoki variableni boshiga ikkta pasgi chizig'cha qoyish kerag
# Shunda u privat boladi privat method yoki variableni ozgartirib bolmaydi lekin ularnii voris qilib boladi

# Inheritance - bu OOPning 4ta tamoildan biri bolb u classni voris qilish uchun kerag
# Masalan sizda Animal degan classiz bor va sizga u classning method va variableari kerag bolib qoldi
# Siz uning uchun voris qilmoqchi bolgan klassizni yoniga qavs ochib u qavisning ichiga ota classning nomini yozsangiz
# U class voris class boladi ota classdagi methodlarni ozgartirish uchun siz Animaldek methodni yaratib ichida supper methodini ishlatishingiz kerag 
# uning uchun siz supper methodini ishlatishingiz kerag suuper qavisochamiz kegin nuhta methodning nomi va qavis ichida parametorlarini yozish kerag

# Polymarphysm - bu OOPning 4ta tamoildan biri bolb uni alright kilganda polimarphysim bolib hisoblanadi 
# alright bu ota classning methodini voris classda ozgartirsa alright boladi va bu Polimarphysm

# Abstraction - bu OOPning 4ta tamoildan biri bolib uni ishlatish uchun import abc from ABC, abstractmethod deb yozish kerag
# Va siz class yaratib uni ABCga voris qilish kerag va u classga method yaratyotkanda siz unga decorator kilishingiz kersg yani @abstractmethod deb yozib pasiga method yozish kerag
# Endi uni ishlatish uchun biz shablon yaratkan classni keragli klasga voris qilib u methodga logikasini yozishimiz mumkun
 

#../
