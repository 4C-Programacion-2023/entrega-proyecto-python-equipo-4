import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import smtplib
import ssl
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
url = 'https://www.promiedos.com.ar'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
entry_correo = None
entry_contrasena = None
entry_codigo_verificacion = None
codigo_verificacion = None




try:
    equipo_local1=soup.find('span', class_='datoequipo', id='t1_35_48').text.strip()
    equipo_visitante1=soup.find('span', class_='datoequipo', id='t2_35_48').text.strip()
    hora_partido1=soup.find('td', class_='game-time', id='ti_35_48').text.strip()
    resultado = soup.find('span', id='r1_35_48').text.strip()
    resultado1 = soup.find('span', id='r2_35_48').text.strip()
except AttributeError:
    try:
        equipo_local1 = soup.find('span', class_='datoequipo', id='t1_35_48').text.strip()
        equipo_visitante1 = soup.find('span', class_='datoequipo', id='t2_35_48').text.strip()
        hora_partido1 = soup.find('td', class_='game-play', id='ti_35_48').text.strip()
        resultado = soup.find('span', id='r1_35_48').text.strip()
        resultado1 = soup.find('span', id='r2_35_48').text.strip()
    except AttributeError:
        equipo_local1 = soup.find('span', class_='datoequipo', id='t1_35_48').text.strip()
        equipo_visitante1 = soup.find('span', class_='datoequipo', id='t2_35_48').text.strip()
        hora_partido1 = soup.find('td', class_='game-fin', id='ti_35_48').text.strip()
        resultado = soup.find('span', id='r1_35_48').text.strip()
        resultado1 = soup.find('span', id='r2_35_48').text.strip()

try:
    equipo_local2=soup.find('span', class_='datoequipo', id='t1_35_50').text.strip()
    equipo_visitante2=soup.find('span', class_='datoequipo', id='t2_35_50').text.strip()
    hora_partido2=soup.find('td', class_='game-time', id='ti_35_50').text.strip()
    resultado2 = soup.find('span', id='r1_35_50').text.strip()
    resultado3 = soup.find('span', id='r2_35_50').text.strip()
except AttributeError:
    try:
        equipo_local2 = soup.find('span', class_='datoequipo', id='t1_35_50').text.strip()
        equipo_visitante2 = soup.find('span', class_='datoequipo', id='t2_35_50').text.strip()
        hora_partido2 = soup.find('td', class_='game-play', id='ti_35_48').text.strip()
        resultado2 = soup.find('span', id='r1_35_50').text.strip()
        resultado3 = soup.find('span', id='r2_35_50').text.strip()
    except AttributeError:
        equipo_local2 = soup.find('span', class_='datoequipo', id='t1_35_50').text.strip()
        equipo_visitante2 = soup.find('span', class_='datoequipo', id='t2_35_50').text.strip()
        hora_partido2 = soup.find('td', class_='game-fin', id='ti_35_50').text.strip()
        resultado2 = soup.find('span', id='r1_35_50').text.strip()
        resultado3 = soup.find('span', id='r2_35_50').text.strip()
try:
    equipo_local3=soup.find('span', class_='datoequipo', id='t1_36_50').text.strip()
    equipo_visitante3=soup.find('span', class_='datoequipo', id='t2_36_50').text.strip()
    hora_partido3=soup.find('td', class_='game-time', id='ti_36_50').text.strip()
    resultado4 = soup.find('span', id='r1_36_50').text.strip()
    resultado5 = soup.find('span', id='r2_36_50').text.strip()
except AttributeError:
    try:
        equipo_local3 = soup.find('span', class_='datoequipo', id='t1_36_50').text.strip()
        equipo_visitante3 = soup.find('span', class_='datoequipo', id='t2_36_50').text.strip()
        hora_partido3 = soup.find('td', class_='game-play', id='ti_36_50').text.strip()
        resultado4 = soup.find('span', id='r1_36_50').text.strip()
        resultado5 = soup.find('span', id='r2_36_50').text.strip()
    except AttributeError:
            equipo_local3 = soup.find('span', class_='datoequipo', id='t1_36_50').text.strip()
            equipo_visitante3 = soup.find('span', class_='datoequipo', id='t2_36_50').text.strip()
            hora_partido3 = soup.find('td', class_='game-fin', id='ti_36_50').text.strip()
            resultado4 = soup.find('span', id='r1_36_50').text.strip()
            resultado5 = soup.find('span', id='r2_36_50').text.strip()
try:
    equipo_local4=soup.find('span', class_='datoequipo', id='t1_34_49').text.strip()
    equipo_visitante4=soup.find('span', class_='datoequipo', id='t2_34_49').text.strip()
    hora_partido4=soup.find('td', class_='game-time', id='ti_34_49').text.strip()
    resultado6 = soup.find('span', id='r1_34_49').text.strip()
    resultado7 = soup.find('span', id='r2_34_49').text.strip()
except AttributeError:
    try:
        equipo_local4 = soup.find('span', class_='datoequipo', id='t1_34_49').text.strip()
        equipo_visitante4 = soup.find('span', class_='datoequipo', id='t2_34_49').text.strip()
        hora_partido4 = soup.find('td', class_='game-play', id='ti_34_49').text.strip()
        resultado6 = soup.find('span', id='r1_34_49').text.strip()
        resultado7 = soup.find('span', id='r2_34_49').text.strip()
    except AttributeError:
        equipo_local4 = soup.find('span', class_='datoequipo', id='t1_34_49').text.strip()
        equipo_visitante4 = soup.find('span', class_='datoequipo', id='t2_34_49').text.strip()
        hora_partido4 = soup.find('td', class_='game-fin', id='ti_34_49').text.strip()
        resultado6 = soup.find('span', id='r1_34_49').text.strip()
        resultado7 = soup.find('span', id='r2_34_49').text.strip()
try:
    equipo_local5=soup.find('span', class_='datoequipo', id='t1_34_56').text.strip()
    equipo_visitante5=soup.find('span', class_='datoequipo', id='t2_34_56').text.strip()
    hora_partido5=soup.find('td', class_='game-time', id='ti_34_56').text.strip()
    resultado8 = soup.find('span', id='r1_34_56').text.strip()
    resultado9 = soup.find('span', id='r2_34_56').text.strip()
except AttributeError:
    try:
        equipo_local5 = soup.find('span', class_='datoequipo', id='t1_34_56').text.strip()
        equipo_visitante5 = soup.find('span', class_='datoequipo', id='t2_34_56').text.strip()
        hora_partido5 = soup.find('td', class_='game-play', id='ti_34_56').text.strip()
        resultado8 = soup.find('span', id='r1_34_56').text.strip()
        resultado9 = soup.find('span', id='r2_34_56').text.strip()
    except AttributeError:
            equipo_local5 = soup.find('span', class_='datoequipo', id='t1_34_56').text.strip()
            equipo_visitante5 = soup.find('span', class_='datoequipo', id='t2_34_56').text.strip()
            hora_partido5 = soup.find('td', class_='game-fin', id='ti_34_56').text.strip()
            resultado8 = soup.find('span', id='r1_34_56').text.strip()
            resultado9 = soup.find('span', id='r2_34_56').text.strip()
try:
    equipo_local6 = soup.find('span', class_='datoequipo', id='t1_34_55').text.strip()
    equipo_visitante6 = soup.find('span', class_='datoequipo', id='t2_34_55').text.strip()
    hora_partido6 = soup.find('td', class_='game-time', id='ti_34_55').text.strip()
    resultado10 = soup.find('span', id='r1_34_55').text.strip()
    resultado11 = soup.find('span', id='r2_34_55').text.strip()
except AttributeError:
    try:
        equipo_local6 = soup.find('span', class_='datoequipo', id='t1_34_55').text.strip()
        equipo_visitante6 = soup.find('span', class_='datoequipo', id='t2_34_55').text.strip()
        hora_partido6 = soup.find('td', class_='game-play', id='ti_34_55').text.strip()
        resultado10 = soup.find('span', id='r1_34_55').text.strip()
        resultado11 = soup.find('span', id='r2_34_55').text.strip()
    except AttributeError:
        equipo_local6 = soup.find('span', class_='datoequipo', id='t1_34_55').text.strip()
        equipo_visitante6 = soup.find('span', class_='datoequipo', id='t2_34_55').text.strip()
        hora_partido6 = soup.find('td', class_='game-fin', id='ti_34_55').text.strip()
        resultado10 = soup.find('span', id='r1_34_55').text.strip()
        resultado11 = soup.find('span', id='r2_34_55').text.strip()
try:
    equipo_local7 = soup.find('span', class_='datoequipo', id='t1_51_29').text.strip()
    equipo_visitante7 = soup.find('span', class_='datoequipo', id='t2_51_29').text.strip()
    hora_partido7 = soup.find('td', class_='game-time', id='ti_51_29').text.strip()
    resultado12 = soup.find('span', id='r1_51_29').text.strip()
    resultado13 = soup.find('span', id='r2_51_29').text.strip()
except AttributeError:
    try:
        equipo_local7 = soup.find('span', class_='datoequipo', id='t1_51_29').text.strip()
        equipo_visitante7 = soup.find('span', class_='datoequipo', id='t2_51_29').text.strip()
        hora_partido7 = soup.find('td', class_='game-play', id='ti_51_29').text.strip()
        resultado12 = soup.find('span', id='r1_51_29').text.strip()
        resultado13 = soup.find('span', id='r2_51_29').text.strip()
    except AttributeError:
            equipo_local7 = soup.find('span', class_='datoequipo', id='t1_51_29').text.strip()
            equipo_visitante7 = soup.find('span', class_='datoequipo', id='t2_51_29').text.strip()
            hora_partido7 = soup.find('td', class_='game-fin', id='ti_51_29').text.strip()
            resultado12 = soup.find('span', id='r1_51_29').text.strip()
            resultado13 = soup.find('span', id='r2_51_29').text.strip()
try:
    equipo_local8 = soup.find('span', class_='datoequipo', id='t1_51_31').text.strip()
    equipo_visitante8 = soup.find('span', class_='datoequipo', id='t2_51_31').text.strip()
    hora_partido8 = soup.find('td', class_='game-time', id='ti_51_31').text.strip()
    resultado14 = soup.find('span', id='r1_51_31').text.strip()
    resultado15 = soup.find('span', id='r2_51_31').text.strip()
except AttributeError:
    try:
        equipo_local8 = soup.find('span', class_='datoequipo', id='t1_51_31').text.strip()
        equipo_visitante8 = soup.find('span', class_='datoequipo', id='t2_51_31').text.strip()
        hora_partido8 = soup.find('td', class_='game-play', id='ti_51_31').text.strip()
        resultado14 = soup.find('span', id='r1_51_31').text.strip()
        resultado15 = soup.find('span', id='r2_51_31').text.strip()
    except AttributeError:
        equipo_local8 = soup.find('span', class_='datoequipo', id='t1_51_31').text.strip()
        equipo_visitante8 = soup.find('span', class_='datoequipo', id='t2_51_31').text.strip()
        hora_partido8 = soup.find('td', class_='game-fin', id='ti_51_31').text.strip()
        resultado14 = soup.find('span', id='r1_51_31').text.strip()
        resultado15 = soup.find('span', id='r2_51_31').text.strip()
try:
    equipo_local9 = soup.find('span', class_='datoequipo', id='t1_51_32').text.strip()
    equipo_visitante9 = soup.find('span', class_='datoequipo', id='t2_51_32').text.strip()
    hora_partido9 = soup.find('td', class_='game-time', id='ti_51_32').text.strip()
    resultado16 = soup.find('span', id='r1_51_32').text.strip()
    resultado17 = soup.find('span', id='r2_51_32').text.strip()
except AttributeError:
    try:
        equipo_local9 = soup.find('span', class_='datoequipo', id='t1_51_32').text.strip()
        equipo_visitante9 = soup.find('span', class_='datoequipo', id='t2_51_32').text.strip()
        hora_partido9 = soup.find('td', class_='game-play', id='ti_51_32').text.strip()
        resultado16 = soup.find('span', id='r1_51_32').text.strip()
        resultado17 = soup.find('span', id='r2_51_32').text.strip()
    except AttributeError:
        equipo_local9 = soup.find('span', class_='datoequipo', id='t1_51_32').text.strip()
        equipo_visitante9 = soup.find('span', class_='datoequipo', id='t2_51_32').text.strip()
        hora_partido9 = soup.find('td', class_='game-fin', id='ti_51_32').text.strip()
        resultado16 = soup.find('span', id='r1_51_32').text.strip()
        resultado17 = soup.find('span', id='r2_51_32').text.strip()
try:
    equipo_local10 = soup.find('span', class_='datoequipo', id='t1_51_34').text.strip()
    equipo_visitante10 = soup.find('span', class_='datoequipo', id='t2_51_34').text.strip()
    hora_partido10 = soup.find('td', class_='game-time', id='ti_51_34').text.strip()
    resultado18 = soup.find('span', id='r1_51_34').text.strip()
    resultado19 = soup.find('span', id='r2_51_34').text.strip()
except AttributeError:
    try:
        equipo_local10 = soup.find('span', class_='datoequipo', id='t1_51_34').text.strip()
        equipo_visitante10 = soup.find('span', class_='datoequipo', id='t2_51_34').text.strip()
        hora_partido10 = soup.find('td', class_='game-play', id='ti_51_34').text.strip()
        resultado18 = soup.find('span', id='r1_51_34').text.strip()
        resultado19 = soup.find('span', id='r2_51_34').text.strip()
    except AttributeError:
        equipo_local10 = soup.find('span', class_='datoequipo', id='t1_51_34').text.strip()
        equipo_visitante10 = soup.find('span', class_='datoequipo', id='t2_51_34').text.strip()
        hora_partido10 = soup.find('td', class_='game-fin', id='ti_51_34').text.strip()
        resultado18 = soup.find('span', id='r1_51_34').text.strip()
        resultado19 = soup.find('span', id='r2_51_34').text.strip()
try:
    equipo_local11 = soup.find('span', class_='datoequipo', id='t1_51_35').text.strip()
    equipo_visitante11 = soup.find('span', class_='datoequipo', id='t2_51_35').text.strip()
    hora_partido11 = soup.find('td', class_='game-time', id='ti_51_35').text.strip()
    resultado20 = soup.find('span', id='r1_51_35').text.strip()
    resultado21 = soup.find('span', id='r2_51_35').text.strip()
except AttributeError:
    try:
        equipo_local11 = soup.find('span', class_='datoequipo', id='t1_51_35').text.strip()
        equipo_visitante11 = soup.find('span', class_='datoequipo', id='t2_51_35').text.strip()
        hora_partido11 = soup.find('td', class_='game-play', id='ti_51_35').text.strip()
        resultado20 = soup.find('span', id='r1_51_35').text.strip()
        resultado21 = soup.find('span', id='r2_51_35').text.strip()
    except AttributeError:
        equipo_local11 = soup.find('span', class_='datoequipo', id='t1_51_35').text.strip()
        equipo_visitante11 = soup.find('span', class_='datoequipo', id='t2_51_35').text.strip()
        hora_partido11 = soup.find('td', class_='game-fin', id='ti_51_35').text.strip()
        resultado20 = soup.find('span', id='r1_51_35').text.strip()
        resultado21 = soup.find('span', id='r2_51_35').text.strip()
try:
    equipo_local12 = soup.find('span', class_='datoequipo', id='t1_68_616').text.strip()
    equipo_visitante12 = soup.find('span', class_='datoequipo', id='t2_68_616').text.strip()
    hora_partido12 = soup.find('td', class_='game-time', id='ti_68_616').text.strip()
    resultado22 = soup.find('span', id='r1_68_616').text.strip()
    resultado23 = soup.find('span', id='r2_68_616').text.strip()
except AttributeError:
    try:
        equipo_local12 = soup.find('span', class_='datoequipo', id='t1_68_616').text.strip()
        equipo_visitante12 = soup.find('span', class_='datoequipo', id='t2_68_616').text.strip()
        hora_partido12 = soup.find('td', class_='game-play', id='ti_68_616').text.strip()
        resultado22 = soup.find('span', id='r1_68_616').text.strip()
        resultado23 = soup.find('span', id='r2_68_616').text.strip()
    except AttributeError:
        equipo_local12 = soup.find('span', class_='datoequipo', id='t1_68_616').text.strip()
        equipo_visitante12 = soup.find('span', class_='datoequipo', id='t2_68_616').text.strip()
        hora_partido12 = soup.find('td', class_='game-fin', id='ti_68_616').text.strip()
        resultado22 = soup.find('span', id='r1_68_616').text.strip()
        resultado23 = soup.find('span', id='r2_68_616').text.strip()
try:
    equipo_local13 = soup.find('span', class_='datoequipo', id='t1_68_610').text.strip()
    equipo_visitante13 = soup.find('span', class_='datoequipo', id='t2_68_610').text.strip()
    hora_partido13 = soup.find('td', class_='game-time', id='ti_68_610').text.strip()
    resultado24 = soup.find('span', id='r1_68_610').text.strip()
    resultado25 = soup.find('span', id='r2_68_610').text.strip()
except AttributeError:
    try:
        equipo_local13 = soup.find('span', class_='datoequipo', id='t1_68_610').text.strip()
        equipo_visitante13 = soup.find('span', class_='datoequipo', id='t2_68_610').text.strip()
        hora_partido13 = soup.find('td', class_='game-play', id='ti_68_610').text.strip()
        resultado24 = soup.find('span', id='r1_68_610').text.strip()
        resultado25 = soup.find('span', id='r2_68_610').text.strip()
    except AttributeError:
        equipo_local13 = soup.find('span', class_='datoequipo', id='t1_68_610').text.strip()
        equipo_visitante13 = soup.find('span', class_='datoequipo', id='t2_68_610').text.strip()
        hora_partido13 = soup.find('td', class_='game-fin', id='ti_68_610').text.strip()
        resultado24 = soup.find('span', id='r1_68_610').text.strip()
        resultado25 = soup.find('span', id='r2_68_610').text.strip()
try:
    equipo_local14 = soup.find('span', class_='datoequipo', id='t1_87_45').text.strip()
    equipo_visitante14 = soup.find('span', class_='datoequipo', id='t2_87_45').text.strip()
    hora_partido14 = soup.find('td', class_='game-time', id='ti_87_45').text.strip()
    resultado26 = soup.find('span', id='r1_87_45').text.strip()
    resultado27 = soup.find('span', id='r2_87_45').text.strip()
except AttributeError:
    try:
        equipo_local14 = soup.find('span', class_='datoequipo', id='t1_87_45').text.strip()
        equipo_visitante14 = soup.find('span', class_='datoequipo', id='t2_87_45').text.strip()
        hora_partido14 = soup.find('td', class_='game-play', id='ti_87_45').text.strip()
        resultado26 = soup.find('span', id='r1_87_45').text.strip()
        resultado27 = soup.find('span', id='r2_87_45').text.strip()
    except AttributeError:
        equipo_local14 = soup.find('span', class_='datoequipo', id='t1_87_45').text.strip()
        equipo_visitante14 = soup.find('span', class_='datoequipo', id='t2_87_45').text.strip()
        hora_partido14 = soup.find('td', class_='game-fin', id='ti_87_45').text.strip()
        resultado26 = soup.find('span', id='r1_87_45').text.strip()
        resultado27 = soup.find('span', id='r2_87_45').text.strip()
try:
    equipo_local15 = soup.find('span', class_='datoequipo', id='t1_87_43').text.strip()
    equipo_visitante15 = soup.find('span', class_='datoequipo', id='t2_87_43').text.strip()
    hora_partido15 = soup.find('td', class_='game-time', id='ti_87_43').text.strip()
    resultado28 = soup.find('span', id='r1_87_43').text.strip()
    resultado29 = soup.find('span', id='r2_87_43').text.strip()
except AttributeError:
    try:
        equipo_local15 = soup.find('span', class_='datoequipo', id='t1_87_43').text.strip()
        equipo_visitante15 = soup.find('span', class_='datoequipo', id='t2_87_43').text.strip()
        hora_partido15 = soup.find('td', class_='game-play', id='ti_87_43').text.strip()
        resultado28 = soup.find('span', id='r1_87_43').text.strip()
        resultado29 = soup.find('span', id='r2_87_43').text.strip()
    except AttributeError:
        equipo_local15 = soup.find('span', class_='datoequipo', id='t1_87_43').text.strip()
        equipo_visitante15 = soup.find('span', class_='datoequipo', id='t2_87_43').text.strip()
        hora_partido15 = soup.find('td', class_='game-fin', id='ti_87_43').text.strip()
        resultado28 = soup.find('span', id='r1_87_43').text.strip()
        resultado29 = soup.find('span', id='r2_87_43').text.strip()
try:
    equipo_local16 = soup.find('span', class_='datoequipo', id='t1_88_367').text.strip()
    equipo_visitante16 = soup.find('span', class_='datoequipo', id='t2_88_367').text.strip()
    hora_partido16 = soup.find('td', class_='game-time', id='ti_88_367').text.strip()
    resultado30 = soup.find('span', id='r1_88_367').text.strip()
    resultado31 = soup.find('span', id='r2_88_367').text.strip()
except AttributeError:
    try:
        equipo_local16 = soup.find('span', class_='datoequipo', id='t1_88_367').text.strip()
        equipo_visitante16 = soup.find('span', class_='datoequipo', id='t2_88_367').text.strip()
        hora_partido16 = soup.find('td', class_='game-play', id='ti_88_367').text.strip()
        resultado30 = soup.find('span', id='r1_88_367').text.strip()
        resultado31 = soup.find('span', id='r2_88_367').text.strip()
    except AttributeError:
        equipo_local16 = soup.find('span', class_='datoequipo', id='t1_88_367').text.strip()
        equipo_visitante16 = soup.find('span', class_='datoequipo', id='t2_88_367').text.strip()
        hora_partido16 = soup.find('td', class_='game-fin', id='ti_88_367').text.strip()
        resultado30 = soup.find('span', id='r1_88_367').text.strip()
        resultado31 = soup.find('span', id='r2_88_367').text.strip()

try:
    equipo_local17 = soup.find('span', class_='datoequipo', id='t1_88_369').text.strip()
    equipo_visitante17 = soup.find('span', class_='datoequipo', id='t2_88_369').text.strip()
    hora_partido17 = soup.find('td', class_='game-time', id='ti_88_369').text.strip()
    resultado32 = soup.find('span', id='r1_88_369').text.strip()
    resultado33 = soup.find('span', id='r2_88_369').text.strip()
except AttributeError:
    try:
        equipo_local17 = soup.find('span', class_='datoequipo', id='t1_88_369').text.strip()
        equipo_visitante17 = soup.find('span', class_='datoequipo', id='t2_88_369').text.strip()
        hora_partido17 = soup.find('td', class_='game-play', id='ti_88_369').text.strip()
        resultado32 = soup.find('span', id='r1_88_369').text.strip()
        resultado33 = soup.find('span', id='r2_88_369').text.strip()
    except AttributeError:
        equipo_local17 = soup.find('span', class_='datoequipo', id='t1_88_369').text.strip()
        equipo_visitante17 = soup.find('span', class_='datoequipo', id='t2_88_369').text.strip()
        hora_partido17 = soup.find('td', class_='game-fin', id='ti_88_369').text.strip()
        resultado32 = soup.find('span', id='r1_88_369').text.strip()
        resultado33 = soup.find('span', id='r2_88_369').text.strip()
try:
    equipo_local18 = soup.find('span', class_='datoequipo', id='t1_88_372').text.strip()
    equipo_visitante18 = soup.find('span', class_='datoequipo', id='t2_88_372').text.strip()
    hora_partido18 = soup.find('td', class_='game-time', id='ti_88_372').text.strip()
    resultado34 = soup.find('span', id='r1_88_372').text.strip()
    resultado35 = soup.find('span', id='r2_88_372').text.strip()
except AttributeError:
    try:
        equipo_local18 = soup.find('span', class_='datoequipo', id='t1_88_372').text.strip()
        equipo_visitante18 = soup.find('span', class_='datoequipo', id='t2_88_372').text.strip()
        hora_partido18 = soup.find('td', class_='game-play', id='ti_88_372').text.strip()
        resultado34 = soup.find('span', id='r1_88_372').text.strip()
        resultado35 = soup.find('span', id='r2_88_372').text.strip()
    except AttributeError:
        equipo_local18 = soup.find('span', class_='datoequipo', id='t1_88_372').text.strip()
        equipo_visitante18 = soup.find('span', class_='datoequipo', id='t2_88_372').text.strip()
        hora_partido18 = soup.find('td', class_='game-fin', id='ti_88_372').text.strip()
        resultado34 = soup.find('span', id='r1_88_372').text.strip()
        resultado35 = soup.find('span', id='r2_88_372').text.strip()
try:
    equipo_local19 = soup.find('span', class_='datoequipo', id='t1_88_374').text.strip()
    equipo_visitante19 = soup.find('span', class_='datoequipo', id='t2_88_374').text.strip()
    hora_partido19 = soup.find('td', class_='game-time', id='ti_88_374').text.strip()
    resultado36 = soup.find('span', id='r1_88_374').text.strip()
    resultado37 = soup.find('span', id='r2_88_374').text.strip()
except AttributeError:
    try:
        equipo_local19 = soup.find('span', class_='datoequipo', id='t1_88_374').text.strip()
        equipo_visitante19 = soup.find('span', class_='datoequipo', id='t2_88_374').text.strip()
        hora_partido19 = soup.find('td', class_='game-play', id='ti_88_374').text.strip()
        resultado36 = soup.find('span', id='r1_88_374').text.strip()
        resultado37 = soup.find('span', id='r2_88_374').text.strip()
    except AttributeError:
        equipo_local19 = soup.find('span', class_='datoequipo', id='t1_88_374').text.strip()
        equipo_visitante19 = soup.find('span', class_='datoequipo', id='t2_88_374').text.strip()
        hora_partido19 = soup.find('td', class_='game-fin', id='ti_88_374').text.strip()
        resultado36 = soup.find('span', id='r1_88_374').text.strip()
        resultado37 = soup.find('span', id='r2_88_374').text.strip()
try:
    equipo_local20 = soup.find('span', class_='datoequipo', id='t1_88_375').text.strip()
    equipo_visitante20 = soup.find('span', class_='datoequipo', id='t2_88_375').text.strip()
    hora_partido20 = soup.find('td', class_='game-time', id='ti_88_375').text.strip()
    resultado38 = soup.find('span', id='r1_88_375').text.strip()
    resultado39 = soup.find('span', id='r2_88_375').text.strip()
except AttributeError:
    try:
        equipo_local20 = soup.find('span', class_='datoequipo', id='t1_88_375').text.strip()
        equipo_visitante20 = soup.find('span', class_='datoequipo', id='t2_88_375').text.strip()
        hora_partido20 = soup.find('td', class_='game-play', id='ti_88_375').text.strip()
        resultado38 = soup.find('span', id='r1_88_375').text.strip()
        resultado39 = soup.find('span', id='r2_88_375').text.strip()
    except AttributeError:
        equipo_local20 = soup.find('span', class_='datoequipo', id='t1_88_375').text.strip()
        equipo_visitante20 = soup.find('span', class_='datoequipo', id='t2_88_375').text.strip()
        hora_partido20 = soup.find('td', class_='game-fin', id='ti_88_375').text.strip()
        resultado38 = soup.find('span', id='r1_88_375').text.strip()
        resultado39 = soup.find('span', id='r2_88_375').text.strip()
try:
    equipo_local21 = soup.find('span', class_='datoequipo', id='t1_88_379').text.strip()
    equipo_visitante21 = soup.find('span', class_='datoequipo', id='t2_88_379').text.strip()
    hora_partido21 = soup.find('td', class_='game-time', id='ti_88_379').text.strip()
    resultado40 = soup.find('span', id='r1_88_379').text.strip()
    resultado41 = soup.find('span', id='r2_88_379').text.strip()
except AttributeError:
    try:
        equipo_local21 = soup.find('span', class_='datoequipo', id='t1_88_379').text.strip()
        equipo_visitante21 = soup.find('span', class_='datoequipo', id='t2_88_379').text.strip()
        hora_partido21 = soup.find('td', class_='game-play', id='ti_88_379').text.strip()
        resultado40 = soup.find('span', id='r1_88_379').text.strip()
        resultado41 = soup.find('span', id='r2_88_379').text.strip()
    except AttributeError:
        equipo_local21 = soup.find('span', class_='datoequipo', id='t1_88_379').text.strip()
        equipo_visitante21 = soup.find('span', class_='datoequipo', id='t2_88_379').text.strip()
        hora_partido21 = soup.find('td', class_='game-fin', id='ti_88_379').text.strip()
        resultado40 = soup.find('span', id='r1_88_379').text.strip()
        resultado41 = soup.find('span', id='r2_88_379').text.strip()
try:
    equipo_local22 = soup.find('span', class_='datoequipo', id='t1_88_368').text.strip()
    equipo_visitante22 = soup.find('span', class_='datoequipo', id='t2_88_368').text.strip()
    hora_partido22 = soup.find('td', class_='game-time', id='ti_88_368').text.strip()
    resultado42 = soup.find('span', id='r1_88_368').text.strip()
    resultado43 = soup.find('span', id='r2_88_368').text.strip()
except AttributeError:
    try:
        equipo_local22 = soup.find('span', class_='datoequipo', id='t1_88_368').text.strip()
        equipo_visitante22 = soup.find('span', class_='datoequipo', id='t2_88_368').text.strip()
        hora_partido22 = soup.find('td', class_='game-play', id='ti_88_368').text.strip()
        resultado42 = soup.find('span', id='r1_88_368').text.strip()
        resultado43 = soup.find('span', id='r2_88_368').text.strip()
    except AttributeError:
        equipo_local22 = soup.find('span', class_='datoequipo', id='t1_88_368').text.strip()
        equipo_visitante22 = soup.find('span', class_='datoequipo', id='t2_88_368').text.strip()
        hora_partido22 = soup.find('td', class_='game-fin', id='ti_88_368').text.strip()
        resultado42 = soup.find('span', id='r1_88_368').text.strip()
        resultado43 = soup.find('span', id='r2_88_368').text.strip()
try:
    equipo_local23 = soup.find('span', class_='datoequipo', id='t1_88_370').text.strip()
    equipo_visitante23 = soup.find('span', class_='datoequipo', id='t2_88_370').text.strip()
    hora_partido23 = soup.find('td', class_='game-time', id='ti_88_370').text.strip()
    resultado44 = soup.find('span', id='r1_88_370').text.strip()
    resultado45 = soup.find('span', id='r2_88_370').text.strip()
except AttributeError:
    try:
        equipo_local23 = soup.find('span', class_='datoequipo', id='t1_88_370').text.strip()
        equipo_visitante23 = soup.find('span', class_='datoequipo', id='t2_88_370').text.strip()
        hora_partido23 = soup.find('td', class_='game-play', id='ti_88_370').text.strip()
        resultado44 = soup.find('span', id='r1_88_370').text.strip()
        resultado45 = soup.find('span', id='r2_88_370').text.strip()
    except AttributeError:
        equipo_local23 = soup.find('span', class_='datoequipo', id='t1_88_370').text.strip()
        equipo_visitante23 = soup.find('span', class_='datoequipo', id='t2_88_370').text.strip()
        hora_partido23 = soup.find('td', class_='game-fin', id='ti_88_370').text.strip()
        resultado44 = soup.find('span', id='r1_88_370').text.strip()
        resultado45 = soup.find('span', id='r2_88_370').text.strip()
try:
    equipo_local24 = soup.find('span', class_='datoequipo', id='t1_88_371').text.strip()
    equipo_visitante24 = soup.find('span', class_='datoequipo', id='t2_88_371').text.strip()
    hora_partido24 = soup.find('td', class_='game-time', id='ti_88_371').text.strip()
    resultado46 = soup.find('span', id='r1_88_371').text.strip()
    resultado47 = soup.find('span', id='r2_88_371').text.strip()
except AttributeError:
    try:
        equipo_local24 = soup.find('span', class_='datoequipo', id='t1_88_371').text.strip()
        equipo_visitante24 = soup.find('span', class_='datoequipo', id='t2_88_371').text.strip()
        hora_partido24 = soup.find('td', class_='game-play', id='ti_88_371').text.strip()
        resultado46 = soup.find('span', id='r1_88_371').text.strip()
        resultado47 = soup.find('span', id='r2_88_371').text.strip()
    except AttributeError:
        equipo_local24 = soup.find('span', class_='datoequipo', id='t1_88_371').text.strip()
        equipo_visitante24 = soup.find('span', class_='datoequipo', id='t2_88_371').text.strip()
        hora_partido24 = soup.find('td', class_='game-fin', id='ti_88_371').text.strip()
        resultado46 = soup.find('span', id='r1_88_371').text.strip()
        resultado47 = soup.find('span', id='r2_88_371').text.strip()
try:
    equipo_local25 = soup.find('span', class_='datoequipo', id='t1_88_373').text.strip()
    equipo_visitante25 = soup.find('span', class_='datoequipo', id='t2_88_373').text.strip()
    hora_partido25 = soup.find('td', class_='game-time', id='ti_88_373').text.strip()
    resultado48 = soup.find('span', id='r1_88_373').text.strip()
    resultado49 = soup.find('span', id='r2_88_373').text.strip()
except AttributeError:
    try:
        equipo_local25 = soup.find('span', class_='datoequipo', id='t1_88_373').text.strip()
        equipo_visitante25 = soup.find('span', class_='datoequipo', id='t2_88_373').text.strip()
        hora_partido25 = soup.find('td', class_='game-play', id='ti_88_373').text.strip()
        resultado48 = soup.find('span', id='r1_88_373').text.strip()
        resultado49 = soup.find('span', id='r2_88_373').text.strip()
    except AttributeError:
        equipo_local25 = soup.find('span', class_='datoequipo', id='t1_88_373').text.strip()
        equipo_visitante25 = soup.find('span', class_='datoequipo', id='t2_88_373').text.strip()
        hora_partido25 = soup.find('td', class_='game-fin', id='ti_88_373').text.strip()
        resultado48 = soup.find('span', id='r1_88_373').text.strip()
        resultado49 = soup.find('span', id='r2_88_373').text.strip()
try:
    equipo_local26 = soup.find('span', class_='datoequipo', id='t1_88_378').text.strip()
    equipo_visitante26 = soup.find('span', class_='datoequipo', id='t2_88_378').text.strip()
    hora_partido26 = soup.find('td', class_='game-time', id='ti_88_378').text.strip()
    resultado50 = soup.find('span', id='r1_88_378').text.strip()
    resultado51 = soup.find('span', id='r2_88_378').text.strip()
except AttributeError:
    try:
        equipo_local26 = soup.find('span', class_='datoequipo', id='t1_88_378').text.strip()
        equipo_visitante26 = soup.find('span', class_='datoequipo', id='t2_88_378').text.strip()
        hora_partido26 = soup.find('td', class_='game-play', id='ti_88_378').text.strip()
        resultado50 = soup.find('span', id='r1_88_378').text.strip()
        resultado51 = soup.find('span', id='r2_88_378').text.strip()
    except AttributeError:
        equipo_local26 = soup.find('span', class_='datoequipo', id='t1_88_378').text.strip()
        equipo_visitante26 = soup.find('span', class_='datoequipo', id='t2_88_378').text.strip()
        hora_partido26 = soup.find('td', class_='game-fin', id='ti_88_378').text.strip()
        resultado50 = soup.find('span', id='r1_88_378').text.strip()
        resultado51 = soup.find('span', id='r2_88_378').text.strip()
try:
    equipo_local27 = soup.find('span', class_='datoequipo', id='t1_88_376').text.strip()
    equipo_visitante27 = soup.find('span', class_='datoequipo', id='t2_88_376').text.strip()
    hora_partido27 = soup.find('td', class_='game-time', id='ti_88_376').text.strip()
    resultado52 = soup.find('span', id='r1_88_376').text.strip()
    resultado53 = soup.find('span', id='r2_88_376').text.strip()
except AttributeError:
    try:
        equipo_local27 = soup.find('span', class_='datoequipo', id='t1_88_376').text.strip()
        equipo_visitante27 = soup.find('span', class_='datoequipo', id='t2_88_376').text.strip()
        hora_partido27 = soup.find('td', class_='game-play', id='ti_88_376').text.strip()
        resultado52 = soup.find('span', id='r1_88_376').text.strip()
        resultado53 = soup.find('span', id='r2_88_376').text.strip()
    except AttributeError:
        equipo_local27 = soup.find('span', class_='datoequipo', id='t1_88_376').text.strip()
        equipo_visitante27 = soup.find('span', class_='datoequipo', id='t2_88_376').text.strip()
        hora_partido27 = soup.find('td', class_='game-fin', id='ti_88_376').text.strip()
        resultado52 = soup.find('span', id='r1_88_376').text.strip()
        resultado53 = soup.find('span', id='r2_88_376').text.strip()
try:
    equipo_local28 = soup.find('span', class_='datoequipo', id='t1_88_377').text.strip()
    equipo_visitante28 = soup.find('span', class_='datoequipo', id='t2_88_377').text.strip()
    hora_partido28 = soup.find('td', class_='game-time', id='ti_88_377').text.strip()
    resultado54 = soup.find('span', id='r1_88_377').text.strip()
    resultado55 = soup.find('span', id='r2_88_377').text.strip()
except AttributeError:
    try:
        equipo_local28 = soup.find('span', class_='datoequipo', id='t1_88_377').text.strip()
        equipo_visitante28 = soup.find('span', class_='datoequipo', id='t2_88_377').text.strip()
        hora_partido28 = soup.find('td', class_='game-play', id='ti_88_377').text.strip()
        resultado54 = soup.find('span', id='r1_88_377').text.strip()
        resultado55 = soup.find('span', id='r2_88_377').text.strip()
    except AttributeError:
        equipo_local28 = soup.find('span', class_='datoequipo', id='t1_88_377').text.strip()
        equipo_visitante28 = soup.find('span', class_='datoequipo', id='t2_88_377').text.strip()
        hora_partido28 = soup.find('td', class_='game-fin', id='ti_88_377').text.strip()
        resultado54 = soup.find('span', id='r1_88_377').text.strip()
        resultado55 = soup.find('span', id='r2_88_377').text.strip()




















def enviar_codigo_verificacion():
    global entry_correo, entry_contrasena, entry_codigo_verificacion, codigo_verificacion

    correo = entry_correo.get()

    if not correo or '@gmail.com' not in correo:
        lbl_resultado.config(text="Ingresa un correo válido")
        lbl_resultado.place(x=500, y=50)
        return
    lbl_resultado.destroy()
    codigo_verificacion = random.randint(100000, 999999)

    email_sender = 'bautistadaveloze@gmail.com'
    email_password = "gpvynfczlqtwgyuf"
    email_receiver = correo
    subject = 'Verifica Tu Correo'
    body = f"Gracias por registrarte.\nTu código de verificación es {codigo_verificacion}"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    lbl_correo.destroy()
    entry_correo.destroy()
    lbl_contrasena.destroy()
    entry_contrasena.destroy()
    boton_enviar.destroy()

    lbl_resultado7 = ttk.Label(ventana, text="Te hemos enviado un codigo de verificacion", font=font_estetico, foreground="white",
                              background="black")
    lbl_resultado7.place(x=400, y=90)
    lbl_resultado2 = ttk.Label(ventana, text="Compruébalo y escríbelo aquí:", font=font_estetico, foreground="white",
                               background="black")
    lbl_resultado2.place(x=400, y=150)



    global entry_codigo_verificacion
    entry_codigo_verificacion = ttk.Entry(ventana, font=font_estetico)
    entry_codigo_verificacion.place(x=540, y=350)

    boton_verificar = tk.Button(
        ventana,
        text="Verificar",
        font=font_estetico,
        padx=30,
        pady=20,
        bg="#2ecc71",
        fg="white",
        relief=tk.RAISED,
        command=verificar_codigo
    )
    boton_verificar.place(x=600, y=450)


def verificar_codigo():

    lbl_resultadop = ttk.Label(text="")
    lbl_resultadop.place(x=0,y=0)

    global entry_codigo_verificacion, codigo_verificacion

    codigo_ingresado = entry_codigo_verificacion.get()
    if codigo_ingresado == str(codigo_verificacion):
        # Cerrar la ventana después de 3 segundos
        lbl_resultadop.config(text="¡Código de verificación correcto!")
        lbl_resultadop.destroy()
        ventana.after(3000, lambda: ventana.destroy())
        inicio = Tk()
        panel = ttk.Notebook(inicio)
        panel.pack(fill="both", expand="yes")

        tab1 = ttk.Frame(panel)
        panel.add(tab1, text="Partidos")



        tab2 = ttk.Frame(panel)
        panel.add(tab2, text="Copa Sudamericana")

        tab3 = ttk.Frame(panel)
        panel.add(tab3, text="Copa Argentina")

        tab4 = ttk.Frame(panel)
        panel.add(tab4, text="MLS")

        tab5 = ttk.Frame(panel)
        panel.add(tab5, text="Copa Libertadores")

        tab6 = ttk.Frame(panel)
        panel.add(tab6, text="Copa Proyeccion")

        tab7= ttk.Frame(panel)
        panel.add(tab7, text="Liga Colombiana")

        tab8= ttk.Frame(panel)
        panel.add(tab8,text="Liga Mexicana")

        etiquta1 = Label(tab1, text=
        "Partido:" + equipo_local1 + resultado + "   "
        + resultado1 + " " + equipo_visitante1 + "\n"
        "Hora del partido: " + hora_partido1 + "\n\n\n\n"
       "Partido:" + equipo_local2 + resultado2 + "   "
        + resultado3 + " " + equipo_visitante2 + "\n"
        "Hora del partido: " + hora_partido2 + "\n\n\n\n"
       "Partido:" + equipo_local3 + resultado4 + "   "
        + resultado5 + " " + equipo_visitante3 + "\n"
        "Hora del partido: " + hora_partido3 + "\n\n\n\n"
       "Partido:" + equipo_local4 + resultado6 + "   "
        + resultado7 + " " + equipo_visitante4 + "\n"
        "Hora del partido: " + hora_partido4 + "\n\n\n\n"
       "Partido:" + equipo_local5 + resultado8 + "   "
        + resultado9 + " " + equipo_visitante5 + "\n"
        "Hora del partido: " + hora_partido5 + "\n\n\n\n"
       "Partido:" + equipo_local6 + resultado10 + "   "
        + resultado11 + " " + equipo_visitante6 + "\n"
        "Hora del partido: " + hora_partido6 + "\n\n\n\n"
       "Partido:" + equipo_local7 + resultado12 + "   "
        + resultado13 + " " + equipo_visitante7 + "\n"
        "Hora del partido: " + hora_partido7 + "\n\n\n\n"
       "Partido:" + equipo_local8 + resultado14 + "   "
        + resultado15 + " " + equipo_visitante8 + "\n"
        "Hora del partido: " + hora_partido8 + "\n\n\n\n")
        etiquta1.place(x=10, y=10)

        etiquta2 = Label(tab1, text=
        "Partido:" + equipo_local9 + resultado16 + "   "
        + resultado17 + " " + equipo_visitante9 + "\n"
        "Hora del partido: " + hora_partido9 + "\n\n\n\n"
       "Partido:" + equipo_local10 + resultado18 + "   "
        + resultado19 + " " + equipo_visitante10 + "\n"
        "Hora del partido: " + hora_partido10 + "\n\n\n\n"
        "Partido:" + equipo_local11 + resultado20 + "   "
        + resultado21 + " " + equipo_visitante11 + "\n"
        "Hora del partido: " + hora_partido11 + "\n\n\n\n"
        "Partido:" + equipo_local12 + resultado22 + "   "
        + resultado23 + " " + equipo_visitante12 + "\n"
        "Hora del partido: " + hora_partido12 + "\n\n\n\n"
       "Partido:" + equipo_local13 + resultado24 + "   "
        + resultado25 + " " + equipo_visitante13 + "\n"
        "Hora del partido: " + hora_partido13 + "\n\n\n\n"
        "Partido:" + equipo_local14 + resultado26 + "   "
        + resultado27 + " " + equipo_visitante14 + "\n"
        "Hora del partido: " + hora_partido14 + "\n\n\n\n"
        "Partido:" + equipo_local15 + resultado28 + "   "
        + resultado29 + " " + equipo_visitante15 + "\n"
        "Hora del partido: " + hora_partido15 + "\n\n\n\n"
        "Partido:" + equipo_local16 + resultado30 + "   "
        + resultado31 + " " + equipo_visitante16 + "\n"
        "Hora del partido: " + hora_partido16 + "\n\n\n\n")
        etiquta2.place(x=310,y=10)

        etiquta3 = Label(tab1, text=
        "Partido:" + equipo_local17 + resultado32 + "   "
        + resultado33 + " " + equipo_visitante17 + "\n"
        "Hora del partido: " + hora_partido17 + "\n\n\n\n"
        "Partido:" + equipo_local18 + resultado34 + "   "
        + resultado35 + " " + equipo_visitante18 + "\n"
        "Hora del partido: " + hora_partido18 + "\n\n\n\n"
        "Partido:" + equipo_local19 + resultado36 + "   "
        + resultado37 + " " + equipo_visitante19 + "\n"
        "Hora del partido: " + hora_partido19 + "\n\n\n\n"
        "Partido:" + equipo_local20 + resultado38 + "   "
        + resultado39 + " " + equipo_visitante20 + "\n"
        "Hora del partido: " + hora_partido20 + "\n\n\n\n"
        "Partido:" + equipo_local21 + resultado40 + "   "
        + resultado41 + " " + equipo_visitante21 + "\n"
        "Hora del partido: " + hora_partido21 + "\n\n\n\n"
        "Partido:" + equipo_local22 + resultado42 + "   "
        + resultado43 + " " + equipo_visitante22 + "\n"
        "Hora del partido: " + hora_partido22 + "\n\n\n\n"
        "Partido:" + equipo_local23 + resultado44 + "   "
        + resultado45 + " " + equipo_visitante23 + "\n"
        "Hora del partido: " + hora_partido23 + "\n\n\n\n"
        "Partido:" + equipo_local24 + resultado46 + "   "
        + resultado47 + " " + equipo_visitante24 + "\n"
        "Hora del partido: " + hora_partido24 + "\n\n\n\n")

        etiquta3.place(x=620, y= 10)

        etiquta4=Label(tab1, text=
        "Partido:" + equipo_local25 + resultado48 + "   "
        + resultado49 + " " + equipo_visitante25 + "\n"
       "Hora del partido: " + hora_partido25 + "\n\n\n\n"
       "Partido:" + equipo_local26 + resultado50 + "   "
        + resultado51 + " " + equipo_visitante26 + "\n"
       "Hora del partido: " + hora_partido26 + "\n\n\n\n"
       "Partido:" + equipo_local26 + resultado50 + "   "
        + resultado51 + " " + equipo_visitante26 + "\n"
       "Hora del partido: " + hora_partido26 + "\n\n\n\n"
       "Partido:" + equipo_local27 + resultado52 + "   "
        + resultado53 + " " + equipo_visitante27 + "\n"
       "Hora del partido: " + hora_partido27 + "\n\n\n\n"
       "Partido:" + equipo_local28 + resultado54 + "   "
        + resultado55 + " " + equipo_visitante28 + "\n"
       "Hora del partido: " + hora_partido28 + "\n\n\n\n")

        etiquta4.place(x=900,y=10)

        etiquta5=Label(tab5,text=
        "Partido:" + equipo_local1 + resultado + "   "
        + resultado1 + " " + equipo_visitante1 + "\n"
        "Hora del partido: " + hora_partido1 + "\n\n\n\n"
       "Partido:" + equipo_local2 + resultado2 + "   "
        + resultado3 + " " + equipo_visitante2 + "\n"
        "Hora del partido: " + hora_partido2 + "\n\n\n\n")
        etiquta5.place(x=500, y=10)

        etiquta6=Label(tab2, text=
        "Partido:" + equipo_local3 + resultado4 + "   "
        + resultado5 + " " + equipo_visitante3 + "\n"
        "Hora del partido: " + hora_partido3 + "\n\n\n\n")
        etiquta6.place(x=500, y=10)

        etiquta7=Label(tab3, text=
        "Partido:" + equipo_local4 + resultado6 + "   "
        + resultado7 + " " + equipo_visitante4 + "\n"
        "Hora del partido: " + hora_partido4 + "\n\n\n\n"
       "Partido:" + equipo_local5 + resultado8 + "   "
        + resultado9 + " " + equipo_visitante5 + "\n"
        "Hora del partido: " + hora_partido5 + "\n\n\n\n"
       "Partido:" + equipo_local6 + resultado10 + "   "
        + resultado11 + " " + equipo_visitante6 + "\n"
        "Hora del partido: " + hora_partido6 + "\n\n\n\n")
        etiquta7.place(x=500, y=10)

        etiquta8=Label(tab6, text=
        "Partido:" + equipo_local11 + resultado20 + "   "
        + resultado21 + " " + equipo_visitante11 + "\n"
       "Hora del partido: " + hora_partido11 + "\n\n\n\n"
       "Partido:" + equipo_local7 + resultado12 + "   "
        + resultado13 + " " + equipo_visitante7 + "\n"
        "Hora del partido: " + hora_partido7 + "\n\n\n\n"
       "Partido:" + equipo_local8 + resultado14 + "   "
        + resultado15 + " " + equipo_visitante8 + "\n"
        "Hora del partido: " + hora_partido8 + "\n\n\n\n"
       "Partido:" + equipo_local9 + resultado16 + "   "
        + resultado17 + " " + equipo_visitante9 + "\n"
        "Hora del partido: " + hora_partido9 + "\n\n\n\n"
       "Partido:" + equipo_local10 + resultado18 + "   "
        + resultado19 + " " + equipo_visitante10 + "\n"
        "Hora del partido: " + hora_partido10 + "\n\n\n\n")
        etiquta8.place(x=500, y=10)

        etiquta9=Label(tab7, text=
        "Partido:" + equipo_local12 + resultado22 + "   "
        + resultado23 + " " + equipo_visitante12 + "\n"
        "Hora del partido: " + hora_partido12 + "\n\n\n\n"
        "Partido:" + equipo_local13 + resultado24 + "   "
        + resultado25 + " " + equipo_visitante13 + "\n"
        "Hora del partido: " + hora_partido13 + "\n\n\n\n")
        etiquta9.place(x=500, y=10)

        etiquta10=Label(tab8, text=
        "Partido:" + equipo_local14 + resultado26 + "   "
        + resultado27 + " " + equipo_visitante14 + "\n"
        "Hora del partido: " + hora_partido14 + "\n\n\n\n"
        "Partido:" + equipo_local15 + resultado28 + "   "
        + resultado29 + " " + equipo_visitante15 + "\n"
        "Hora del partido: " + hora_partido15 + "\n\n\n\n")
        etiquta10.place(x=500, y=10)

        etiquta11=Label(tab4, text=
        "Partido:" + equipo_local16 + resultado30 + "   "
        + resultado31 + " " + equipo_visitante16 + "\n"
        "Hora del partido: " + hora_partido16 + "\n\n\n\n"
        "Partido:" + equipo_local17 + resultado32 + "   "
        + resultado33 + " " + equipo_visitante17 + "\n"
        "Hora del partido: " + hora_partido17 + "\n\n\n\n"
        "Partido:" + equipo_local18 + resultado34 + "   "
        + resultado35 + " " + equipo_visitante18 + "\n"
        "Hora del partido: " + hora_partido18 + "\n\n\n\n"
        "Partido:" + equipo_local19 + resultado36 + "   "
        + resultado37 + " " + equipo_visitante19 + "\n"
        "Hora del partido: " + hora_partido19 + "\n\n\n\n"
        "Partido:" + equipo_local20 + resultado38 + "   "
        + resultado39 + " " + equipo_visitante20 + "\n"
        "Hora del partido: " + hora_partido20 + "\n\n\n\n"
        "Partido:" + equipo_local21 + resultado40 + "   "
        + resultado41 + " " + equipo_visitante21 + "\n"
        "Hora del partido: " + hora_partido21 + "\n\n\n\n"
        "Partido:" + equipo_local22 + resultado42 + "   "
        + resultado43 + " " + equipo_visitante22 + "\n"
        "Hora del partido: " + hora_partido22 + "\n\n\n\n")
        etiquta11.place(x=250, y=10)

        etiquta12=Label(tab4, text=
        "Partido:" + equipo_local22 + resultado42 + "   "
        + resultado43 + " " + equipo_visitante22 + "\n"
       "Hora del partido: " + hora_partido22 + "\n\n\n\n"
        "Partido:" + equipo_local23 + resultado44 + "   "
        + resultado45 + " " + equipo_visitante23 + "\n"
        "Hora del partido: " + hora_partido23 + "\n\n\n\n"
        "Partido:" + equipo_local24 + resultado46 + "   "
        + resultado47 + " " + equipo_visitante24 + "\n"
        "Hora del partido: " + hora_partido24 + "\n\n\n\n"
        "Partido:" + equipo_local25 + resultado48 + "   "
        + resultado49 + " " + equipo_visitante25 + "\n"
       "Hora del partido: " + hora_partido25 + "\n\n\n\n"
       "Partido:" + equipo_local26 + resultado50 + "   "
        + resultado51 + " " + equipo_visitante26 + "\n"
       "Hora del partido: " + hora_partido26 + "\n\n\n\n"
       "Partido:" + equipo_local27 + resultado52 + "   "
        + resultado53 + " " + equipo_visitante27 + "\n"
       "Hora del partido: " + hora_partido27 + "\n\n\n\n"
       "Partido:" + equipo_local28 + resultado54 + "   "
        + resultado55 + " " + equipo_visitante28 + "\n"
       "Hora del partido: " + hora_partido28 + "\n\n\n\n")
        etiquta12.place(x=750, y=10)


        inicio.geometry("1300x700")
        inicio.title("BET SOCCER")
        inicio.configure(bg="black")
        inicio.mainloop()



    else:
        entry_codigo_verificacion.delete(0, tk.END)  # Borrar el contenido del campo de texto
        lbl_resultadop.config(text="Código de verificación incorrecto",font=font_estetico, foreground="red",
                               background="black")
        lbl_resultadop.place(y=250,x=400)





def mostrar_campos():
    global entry_correo, entry_contrasena, boton_enviar, lbl_correo, lbl_contrasena

    registro.destroy()
    lbl_logo.destroy()

    lbl_correo = ttk.Label(ventana, text="Correo Electrónico:", font=font_estetico)
    lbl_correo.place(x=350, y=200)
    entry_correo = ttk.Entry(ventana, font=font_estetico)
    entry_correo.place(x=650, y=200)

    lbl_contrasena = ttk.Label(ventana, text="Contraseña:", font=font_estetico)
    lbl_contrasena.place(x=455, y=250)
    entry_contrasena = ttk.Entry(ventana, font=font_estetico, show="*")
    entry_contrasena.place(x=650, y=250)

    boton_enviar = tk.Button(
        ventana,
        text="Enviar",
        font=font_estetico,
        padx=30,
        pady=20,
        bg="#3498db",
        fg="white",
        relief=tk.RAISED,
        command=enviar_codigo_verificacion
    )
    boton_enviar.place(x=600, y=350)


ventana = tk.Tk()
ventana.geometry("1510x700")
ventana.title("BetSoccer")
ventana.configure(bg="black")

font_estetico = ("Arial", 20, "bold")

registro = tk.Button(
    ventana,
    text="Registrarse",
    font=font_estetico,
    padx=30,
    pady=20,
    bg="#3498db",
    fg="white",
    relief=tk.RAISED,
    command=mostrar_campos
)
registro.place(x=560, y=400)

lbl_resultado = ttk.Label(ventana, text="", font=font_estetico, foreground="white", background="black")
lbl_resultado.place(x=200, y=350)

logo = tk.PhotoImage(file="Logo.PNG")
lbl_logo = tk.Label(ventana, image=logo, borderwidth=0)
lbl_logo.place(x=430, y=50)

ventana.mainloop()

