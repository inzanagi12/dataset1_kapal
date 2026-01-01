print(20*"=", "episode 1 pendahuluan OOP",20*"=")
class Hero: #template
	pass

hero1 = Hero() #object
hero2 = Hero()
hero3 = Hero()

hero1.name  = "ucup"
hero1.health = 100

hero2.name = "samsul"
hero2.health = 100

hero3.name = "kiye"
hero3.health = 100

print(hero1) #menampilkan tipe dia dan letak posisi memori
print(hero1.__dict__) #menampilakn seluruh isi di variabel hero1

print("\n")
print(20*"=", "episode 2 constructor __init__", 20*"=")
class Hero:
	def __init__(self, inputName, inputHealth, inputPower,inputArmor):
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		#penggunaan diatas tu sama aja kaya ==> hero1.name = akmal, namun bedanya diatas make constructor init
	
hero1 = Hero("akmal", 100, 10, 5)
hero2 = Hero("ojan", 100, 5 ,20)
hero3 = Hero("ucup", 1000, 30, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

print("\n")
print(20*"=", "episode 3 class dan instace variable", 20*"=")
#apa itu variabel static adalah variabel yang ada di dalam class itu sendiri
class Hero:
	#Class variable
	jumlah = 0
	
	def __init__(self, inputName, inputHealth, inputAtt, inputArmor):
		self.name = inputName
		self.health = inputHealth
		self.power = inputAtt
		self.armor = inputArmor
		Hero.jumlah += 1
		print("membuat hero dengan nama" + inputName )

hero1 = Hero("kucek", 90, 30, 35)
print(Hero.jumlah)
hero2 = Hero("kulkul", 100, 15, 10)
print(Hero.jumlah)
hero3 = Hero ("pnoy", 200,10,50)
print(Hero.jumlah)

print("\n")
print(20*'=', "episode 4 method", 20*'=')
class Hero:
    jumlah = 0
    def __init__(self, name, health, attackPower, armorDefens):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorDefens = armorDefens
    
    def siapa(self): #method tanpa return dan argumen
        print("namaku adalah: " + self.name)
    
    def healthUp(self, up): #method dengan argumen, tanpa return
        self.health += up
        
    def getHealth(self): #method dengan argumen
        return self.health
        
hero1 = Hero("sniper", 100, 5, 10)
hero2 = Hero("sniper", 100, 10, 5)

hero1.siapa()
hero2.healthUp(10)

print(hero1.getHealth())

print("\n")
print(20*'=', "episode 5 latihan sederhana",  20*'=')
class Hero:
    jumlah = 0
    def	__init__(self, name, health, attPower, armor):
        self.name = name
        self.health = health
        self.attPower = attPower
        self.armor = armor
    
    def menyerang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attPower)
    
    def diserang(self, lawan, att_Power):
        print(self.name + " diserang oleh " + lawan.name)    
        att_Diterima = att_Power/self.armor
        print("serangan terasa " + str(att_Diterima))
        self.health -= att_Diterima
        print("sisa darah " + str(self.health))
        
sniper = Hero("sniper", 100, 5, 10)		  		
kimimaru = Hero("kimimaru", 100, 10, 5)		  		

sniper.menyerang(kimimaru)

print("\n")
print(20*'=', "episode 6 Tk inter", 20*'=')
# import tkinter 

# main_window = tkinter.Tk()

# label1 = tkinter.Label(main_window, text = "label1")
# label2 = tkinter.Label(main_window, text = "label2")

# tombol1 = tkinter.Button(main_window, text = "tombol1")
# tombol2 = tkinter.Button(main_window, text = "tombol2")

# label1.pack()
# label2.pack()
# tombol1.pack()
# tombol2.pack()

# main_window.mainloop()

print("\n")
print(20*'=', "episode 7 private variable", 20*'=')
class Hero:
    jumlah = 0
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
        # variabel instance private
        self.__private = "private"
        #variabel instance pprotected =
        self._protected = "protected"
        
lina = Hero("lina", 100)

print(lina.__dict__)
lina.__private = "testing" #terbentuk nya suatu variabel dan tidak mengubah variabel private diatasnya 
#variabel private tetaplah private, t1idak bisa di akses
print(lina.__dict__)
print(lina.__private) 
lina._protected = "test" #protect sama seperti public, bisa diakses 
print(lina.__dict__)
print(lina._protected)
print("hello world")

print("\n")
print(20*"=", "episode 8 encapsulasi", 20*"=")
class Hero:
    jumlahh = 0
    def __init__(self, name, health, attPower, armor):
         self.__nama = name
         self.__darah = health
         self.__attack = attPower
         self.__armor = armor
         self.__armorAwal = armor
    # getter
    def getNama(self):
        return self.__nama
    
    def getDarah(self):
        return self.__darah
    
    def getAtt(self):
        return self.__attack
    
    def getdefens(self):
        return self.__armor
    
    # setter
    def setDarah(self, ambilDarah):
        self.__darah -= ambilDarah
        
    def setSerang(self, tenaga): 
        if self.__armor > 0:
            sisa_damage = tenaga - self.__armor
            self.__armor -= tenaga
            if self.__armor < 0:
                self.__armor = 0
            if self.__armor > 0:
                self.__darah -= sisa_damage
                # self.__armor = self.__armorAwal
        else:
            self.__darah -= tenaga
            self.__armor = self.__armorAwal
        
        
         
sasuke = Hero("sasuke", 100, 10, 5)
print(sasuke.getNama())
print("Darah: ", sasuke.getDarah())
print("Armor: ", sasuke.getdefens())

for i in range(1, 11):
    print(f"\nSerangan ke-{i}")
    sasuke.setSerang(4)  # bisa ganti damage sesuai kebutuhan
    print("Darah:", sasuke.getDarah())
    print("Armor:", sasuke.getdefens())
    
print("\n")
print(20*"=", "episode 9 static method dan class method")
class Hero:
    __jumlah = 0
    def __init__(self, name):
        self.__nama = name
        Hero.__jumlah += 1
        #  self.__darah = health
        #  self.__attack = attPower
        #  self.__armor = armor
    # tidak bisa karena penggunaan self hanya uuntuk object
    def getJumlah(self):
        return Hero.__jumlah
    # berlaku untuk class tapi tidak untuk objek
    def getJumlah1():
        return Hero.__jumlah     
    
    # penggunaan static harus menggunakan decorator
    # decorator nempel ke objek dan kelas 
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah     
    
    # penggunaan class sama saja seperti static
    # namun kalo class dia ada argumen sedangkan staticc tidak
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
sniper = Hero("sniper")
# print(Hero.getJumlah())
rikimaru = Hero("rikimaru")
# print(Hero.getJumlah1())
drowranger = Hero("drowranger")
print(Hero.getJumlah2())
print(Hero.getJumlah3())

print("\n")
print(20*"=", "episode 10 getter dan setter", 20*"=")
class Hero:
    __jumlah = 0
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {} \n\tarmor: {}".format(self.__name, self.__health, self.__armor)
    # def getHealth(self):
    #     return self.__health
    @property
    def info(self): #method ini akan dianggep seperti variabel
        return "name {} : \n\thealth: {} \n\tarmor: {}".format(self.name, self.__health, self.__armor)
        # return self.info #kalo ini seperti getter
    
    # dalam penggunaan self.info dan property, kalo property itu dia bisa diubah nilai nya karena bersifat dinamis
    # sedangkan self.info, dia sifatnya static dan tidak bisa berubah dari awal ppembentukannya
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, val):
        self.__armor = val
    
    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None

print("merubah info")
sniper = Hero("sniper",100,10)
print(sniper.info)         
# print(sniper.getHealth())
# print(sniper.__dict__)
sniper.name = "ucup"
print(sniper.info)

print("getter dan setter untuk __armor")
print(sniper.armor)
print(sniper.__dict__)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

print("delete armor")
del sniper.armor
print(sniper.__dict__)

print("\n")
print(20*"=", "episode 11 latihan encapsulasi", 20*"=")
class Hero:
    __jumlah = 0
    
    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__attPowerStandar = attPower
        self.__healthStandar = health
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar *self.__level
        self.__health = self.__healthMax
        Hero.__jumlah += 1
    
    @property
    def info(self):
        return "{} level {} : \n\thealth: {}/{} \n\tattack = {} \n\tarmor: {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)
    
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level
            if (self.__level == 15):
                print(self.__name, "level max")
                
    def attack(self, musuh):
        self.gainExp = 50
            
sniper = Hero("sniper", 100, 10, 5)
dadang = Hero("dadang", 100, 10, 5)
print(sniper.info)

sniper.gainExp = 110
print(sniper.info)
sniper.gainExp = 110
print(sniper.info)

for i in range(10):
    sniper.attack(dadang)
    print(sniper.info)         
    # next pr coba bikin gabungin ama multi thread 
    
print(20*"=", "eps 12 pendahuluan inheritance", 20*"=")
class Hero:
    __jumlah = 0
    
    def __init__(self, name, health, attPower, defens):
        self.__name = name
        self.__health = health
        self.__attack = attPower
        self.__defens = defens
        
class Hero_intelligent(Hero): #parameter dari subclass ini adalah super class nya
    pass
    # penggunaan parameter super class di subclass, tingkah laku nya akan sama seperti superclass
    # jadi tidak perlu menggunakan __init__ nya kembali

class Hero_strength(Hero):
    pass

lina = Hero('lina', 100, 50, 10)
ucup = Hero_intelligent("ucup", 100, 20, 25) 
axe = Hero_strength("axe", 100, 30, 80)

print(lina.__dict__)
# print(help(axe))
# fungsi help() digunakan untuk menampilkan dokumentasi dan informasi tentang berbagai
# objek python, seperti modul, fungsi, kelas, dan variabel

# lalu ada penjelasan tentang weakref: Weakref tidak mencegah objek untuk dihapus, sehingga cocok dipakai untuk menghindari
# referensi siklik yang tidak bisa dibersihkan GC, atau untuk cache yang fleksibel.
# Referensi kuat (biasa) harus digunakan dengan hati-hati saat dua objek saling mereferensikan, karena bisa menyebabkan siklus. 
# Untuk itu, salah satu sisi bisa pakai weakref agar GC tetap bisa bekerja.

# namun lebih tepatnya weakref memungkinkan kita menyimpan referensi ke objek tanpa mencegah objek tersebut dihapus oleh garbage collector, 
# cocok untuk cache dan struktur data siklik agar menghindari memory leak.

print(20*"=", "eps 13 Super", 20*"=")
class Hero:
    __jumlah = 0
    
    def __init__(self, name, health):
        self.__name = name
        self.__health = health
    
    def showInfo(self):
        print("{} dengan health {}".format(self.__name, self.__health))
        
class Hero_intelligence(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 100) --> bisa juga cara menggunakannya seperti ini untuk memanggil super class
        # namun tidak efektif ketika superclass(Hero) berganti nama variabel nya
        super().__init__(name, 100)
        super().showInfo()
        
class Hero_strength(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 200)
        super().__init__(name, 200)
        super().showInfo()

lina = Hero_intelligence('lina')        
axe = Hero_strength('axe')        

print(20*"=", "eps 14 Override Method", 20*"=")
class Hero:
    __jumlah = 0
    
    def __init__(self, name, health):
        self._name = name
        self._health = health

    def showInfo(self):
        print("showInfo di class Hero")
        print("{} health: {}".format(self._name, self._health))

class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent")
        print("{} health: {}".format(self._name, self._health))
        # super().showInfo()
        
class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

researcher = Hero_intelligent('researcher')
axe = Hero_strength('axe')

researcher.showInfo()
# print(researcher._name)
# print(researcher.__dict__)
# print(help(researcher))
axe.showInfo()

print(20*"=", "eps 15 latihan inheritance", 20*"=")
class Hero:
    __jumlah = 0
    
    def __init__(self, name):
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.attackPower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 10, 20, 30, 40, 50] 
        self.__name = name
        self.__exp = 0
        self.__level = 0
    
    def showInfo(self):
        print("{} \n\tlevel: {} \n\thealth: {} \n\tattack: {} \n\tarmor: {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__attPower,
            self.__armor
            )
        )
    
    @property 
    def health_pool(self):
        pass
    
    @property
    def attackPower_pool(self):
        pass
    
    @property
    def armor_pool(self):
        pass
    
    @property
    def levelUp(self):
        pass
    
    @property
    def gainExp(self):
        pass
    
    @health_pool.setter
    def health_pool(self, input):
        self.__health_pool = input
        
    @attackPower_pool.setter
    def attackPower_pool(self, input):
        self.__attackPower_pool = input
        
    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input
        
    @gainExp.setter
    def gain_exp(self, input):
        self.__exp = input
        if(self.__exp  >= 100):
            self.levelUp = self.__exp // 100
            self.__exp %= 100
            
    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attackPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
            
class Hero_intelligent(Hero):
     def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 50, 100, 150, 200, 250]
        self.attackPower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 0.5, 1, 1.5, 2, 2.5 ]
        self.levelUp = 1
        
class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 200, 300, 400, 500, 600]
        self.attackPower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 2, 4, 6, 8, 10 ]
        self.levelUp = 1
        
asep = Hero_intelligent("asep")
ucup = Hero_strength("ucup")

asep.showInfo()

print(20*"=", "eps 16 multiple inheritance", 20*"=")
class Team:
    def setTeam(self, team):
        self.team = team
        
    def showTeam(self):
        print(self.team)
        
class Tipe:
    def setTipeHero(self, tipe):
        self.tipe = tipe
    
    def showTipe(self):
        print(self.tipe)
        
class Hero(Team, Tipe):
    def __init__(self, name, health):
        self.name = name
        self.health = health

arkan = Hero("arkan", 100)
kunyuk = Hero("arkan", 100)
arkan.setTipeHero("agen")
kunyuk.setTeam("merah")

arkan.showTipe()
kunyuk.showTeam()

print(20*"=", "eps 17 Method Resolution Order // multiple inheritance", 20*"=")
class A:
    def show(self):
        print("ini adlah show A")
class B:
    def show(self):
        print("ini adlah show B")
# permasalahan jika show nya menjadi sama bukan show_a atau show_b, melainkan show saja
# maka bisa menggunakan help() untuk melihat multiple order nya
# jika di dalam parameter urutannya adalah A dlu baru B, maka show A lah yang keluar
# begitupun sebaliknyaa
class C(A,B):
    pass
# namun permasalahan muncul jika subclass C tidak memiliki value/pass
# jika subclass C memiliki value, maka show_C lah yang akan muncul

objek = C()
objek.show()
# help(objek)

print(20*"=", "eps 17 Method Resolution Order // multiple inheritance", 20*"=")
class A:
    def show(self):
        print("ini adalah show A")
class B(A):
    def show(self):
        print("ini adalah show B")
class C(A):
    def show(self):
        print("ini adalah show C")
class D(B,C):
    pass
# permasalahannya sama seperti method reslotuion order
objek = D()
objek.show()