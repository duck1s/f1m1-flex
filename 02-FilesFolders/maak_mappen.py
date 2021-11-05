import io
import os

bestand = open("klasgenoten.txt", "r")

naam1 = bestand.readline()
naam2 = bestand.readline()
naam3 = bestand.readline()

os.mkdir(str(naam1))
os.mkdir(str(naam2))
os.mkdir(str(naam3))
