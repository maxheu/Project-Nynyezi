# !/usr/bin/env python3
#Installation:
#sudo pip3 install pygame

#Commands:
#'q' - Game Exit
#

#TestEdit
import pygame
import time
import random
import socket
from threading import Thread
import json
import pygame.gfxdraw
import math

gameTitle = "Nyenyezi - Astronomiespiel"

display_x = 1000
display_y = 750

infoBox_x = 300
infoBox_y = 350     #max. display_y/2

eventBox_x = 600
eventBox_y = round(600*6/16)

fontSizeSmall = 12
fontSizeMiddle = 20
fontSize = 30

#Colors:
black = (0,0,0,100)
white = (255,255,255,100)
red = (255,0,0,100)
green = (0,255,0,100)
blue = (0,0,255,100)
darkgray = (50, 50, 50, 50)
violet = (153, 50, 204)
gainsboro = (220,220,220)
lightgray = (211,211,211)
silver = (192,192,192)

lightgray = (150,150,150)
yellow = (250, 250, 0)

black80 = (0,0,0,80)
white80 = (255,255,255,80)
gray80 = (100,100,100,80)

gray20 = (100,100,100,20)

team1_color = (255, 100, 100)
hostileteam1_color = (0, 255, 150)
hostileteam2_color = (200, 100, 255)
team2_color = (100, 255, 100)
special_color = white
infoBoxColor = white80
errorBoxColor = blue
colorLaser = violet
StrahlungTextColor = white
MetallTextColor = white
TechButtonColor = white
TechButtonTextColor = black
TechHeaderTextColor = black
TechSubHeaderTextKraftColor = black
TechSubHeaderTextWeisheitColor = black
TechSubHeaderTextPerfektionColor = black
TechStrahlungTextColor = black
TechMetallTextColor = black
TechIconOverlayColor = gray80
TechInfoColor = lightgray
NewStarButtonColor = white
NewStarButtonTextColor = black
NewStarColor = white
NewStarHeaderTextColor = black
NewStarSizeTextColor = black
NewStarSizeSliderLineColor = black
NewStarSizeSliderCircleColor = violet

fontSizeBig = 60

star_space = 25
star_size = 3
click_size = 10
border_space = 70
spaceInfoBox = 10
star_size_opened = 10
star_size_choose = 10

strahlungTextX = display_x - 200
strahlungTextY = 10

metallTextX = display_x - 400
metallTextY = 10

InfoIconURL = "Pictures/ic_info_outline_white_36dp_1x.png"
InfoIconSize = 36


KraftBackgroundBlackURL = "Pictures/KraftMainS.jpg"
KraftBackgroundColorURL = "Pictures/KraftMainF.jpg"
PerfektionBackgroundBlackURL = "Pictures/PerfektionMainS.jpg"
PerfektionBackgroundColorURL = "Pictures/PerfektionMainF.jpg"
WeisheitBackgroundBlackURL = "Pictures/WeisheitMainS.jpg"
WeisheitBackgroundColorURL = "Pictures/WeisheitMainF.jpg"
SternabzeichenURL = "Pictures/SternBadget.jpg"



MusicOnIconURL = "Pictures/ic_volume_up_white_36dp_1x.png"
MusicOffIconURL = "Pictures/ic_volume_off_white_36dp_1x.png"
VolumeIconSize = 36

settingsIconURL = "Pictures/ic_settings_white_36dp_1x.png"
SettingsIconSize = 36

#BackgroundURL = "Pictures/background_planet.jpg"
BackgroundURL = "Pictures/background_galaxy.jpg"
#BackgroundURL = "Pictures/background_stars.jpg"
#BackgroundURL = "Pictures/background_fantasy.jpg"

LogoURL = "Pictures/logo_neu_dick.png"
LogoSize = 60

metallIconURL = "Pictures/metalle_neu.png"
strahlungIconURL = "Pictures/ic_polymer_white_36dp_1x.png"
MetallIconSize = 36
StrahlungIconSize = 36


Button1HoverURL = "Pictures/Button1hover.png"
Button1unHoverURL = "Pictures/Button1unhover.png"
TechIconURL = "Pictures/TechIcon.png"
NewStarIconURL = "Pictures/ic_create_white_36dp_1x.png"
IconSize = 36

RahmenSizeObenX = 275
RahmenSizeObenY = 111
RahmenSizeUntenX = 273
RahmenSizeUntenY = 97
RahmenWeissObenLinksURL = "Pictures/rahmen_weiß_oben_links.png"
RahmenWeissObenRechtsURL = "Pictures/rahmen_weiß_oben_rechts.png"
RahmenWeissUntenLinksURL = "Pictures/rahmen_weiß_unten_links.png"
RahmenWeissUntenRechtsURL = "Pictures/rahmen_weiß_unten_rechts.png"
EventBoxBackgroundURL = "Pictures/EventBoxBackground.jpg"


Crisis_Dark_Matter_Timer = {"time": 24, "name": "Crisis_Dark_Matter_Timer", "effect": "self.drawEvent('Crisis_Dark_Matter_Breakout')", "ongoingeffect": " "}


TechButtonTextSpace = 5
TechButtonX = 65
TechButtonY = fontSizeSmall + 2 * TechButtonTextSpace
TechButtonSpace = 10
TechButtonTextX = TechButtonTextSpace
TechButtonTextY = TechButtonTextSpace

NewStarButtonTextSpace = 5
NewStarButtonX = 70
NewStarButtonY = fontSizeSmall + 2 * NewStarButtonTextSpace
NewStarButtonSpace = 10
NewStarButtonTextX = NewStarButtonTextSpace
NewStarButtonTextY = NewStarButtonTextSpace

NewStarSizeX = 300
NewStarSizeY = 200
NewStarHeaderTextX = 500
NewStarHeaderTextY = 150
NewStarCloseIconX = NewStarSizeX - 5 - 20
NewStarCloseIconY = 5
NewStarNameTextX = 10
NewStarNameTextY = NewStarHeaderTextY + 30
NewStarSizeTextX = 10
NewStarSizeTextY = NewStarNameTextY + 30
NewStarSizeSliderCircleSize = 10


TechHeaderTextX = display_x / 2 - 100
TechHeaderTextY = 20

TechSubHeaderTextKraftX = display_x / 2 - 50
TechSubHeaderTextKraftY = 100

TechSubHeaderTextWeisheitX = display_x - 200
TechSubHeaderTextWeisheitY = 100

TechSubHeaderTextPerfektionX = 100
TechSubHeaderTextPerfektionY = 100

spaceTechCloseIcon = 10
sizeTechCloseIconX = 48
sizeTechCloseIconY = 48

TechIconSizeX = 64
TechIconSizeY = 64

TechInfoSizeX = 300
TechInfoSizeY = 200
TechInfoSpace = TechIconSizeX + 10
TechInfoHeaderTextColor = black
TechInfoHeaderTextX = 10
TechInfoHeaderTextY = 10
TechInfoDescriptionSpaceX = 10
TechInfoDescriptionSpaceY = 10
TechInfoDescriptionTextColor = black
TechInfoErforschenTextColor = black

#searchTop

PerfektionICost = 3000
PerfektionIconI_X = TechSubHeaderTextPerfektionX + 75
PerfektionIconI_Y = TechSubHeaderTextPerfektionY + 50
PerfektionIconIURL = "Pictures/PerfektionI.jpg"
PerfektionIconIBlockedURl = "Pictures/PerfektionI_sw.jpg"
PerfektionIconIHeader = "Zirkumstellare Akkumulation"
PerfektionIconIDescription = ("Mithilfe", "der", "verbesserten", "Akkumulation", "absorbieren", "neue",
                                "Sterne", "die", "gesamte", "zirkumstellare", "Scheibe.", "Die", "Bildung",
                                "der", "Sterne", "wird", "damit", "weniger", '"Strahlung"', "verbrauchen",
                                "und", "effektiver", "sein.", "Kosten bei Sternbildung * 0.9", " ") #letzter string wird nicht angezeigt

PerfektionIICost = 3000
PerfektionIconII_X = TechSubHeaderTextPerfektionX
PerfektionIconII_Y = PerfektionIconI_Y + 100
PerfektionIconIIURL = "Pictures/PerfektionII.jpg"
PerfektionIconIIBlockedURL = "Pictures/PerfektionII_sw.jpg"
PerfektionIconIIHeader = "Schnelle Akkumulation"
PerfektionIconIIDescription = ["Unsere", "Sterne", "werden", "in", "ihrer", "Geburtsphase", "viel",
                                "schneller", "Teile", "der", "Akkumulationsscheibe", "absorbieren",
                                "und", "schneller", "zu", "vollen", "Sternen", "anwachsen",
                                "Zeit für Entwicklung (Geburt) * 0.75", " "]

PerfektionIIICost = 3000
PerfektionIconIII_X = PerfektionIconI_X + 75
PerfektionIconIII_Y = PerfektionIconI_Y + 100
PerfektionIconIIIURL = "Pictures/PerfektionIII.jpg"
PerfektionIconIIIBlockedURL = "Pictures/PerfektionIII_sw.jpg"
PerfektionIconIIIHeader = "Sorgfältige Akkumulation"
PerfektionIconIIIDescription = ["Unsere", "Sterne", "werden", "bei", "der", "Akkumulation", "sehr", "sorgsam",
                                "vorgehen", "und", "dadurch", "mehr", "Masse", "aus", "ihrer", "Umgebung", "aufnehmen.",
                                "Ihre", "Kosten", "bei", "der", "Bildung", "werden", "daher", "gesenkt.",
                                "Kosten bei Sternbildung * 0.8", " "]

PerfektionIVCost = 3000
PerfektionIconIV_X = PerfektionIconI_X
PerfektionIconIV_Y = PerfektionIconI_Y + 200
PerfektionIconIVURL = "Pictures/PerfektionIV.jpg"
PerfektionIconIVBlockedURL = "Pictures/PerfektionIV_sw.jpg"
PerfektionIconIVHeader = "Rho-Ophindi-Strahlung"
PerfektionIconIVDescription = ["Durch", "ihre", "noch", "geringere", "Masse", "und", "den", "hohen", "Prozentsatz",
                                "an", "reinem", "Brennstoff", "werden", "Sterne", "während", "ihrer", "Entstehung",
                                "sogar", "stärker", "strahlen", "als", "in", "ihrer", "Hauptreihenphase",
                                "Strahlung in Geburtsstadium * 3", " "]

PerfektionVCost = 3000
PerfektionIconV_X = PerfektionIconI_X
PerfektionIconV_Y = PerfektionIconI_Y + 300
PerfektionIconVURL = "Pictures/PerfektionV.jpg"
PerfektionIconVBlockedURL = "Pictures/PerfektionV_sw.jpg"
PerfektionIconVHeader = "Braune Zwerge"
PerfektionIconVDescription = ["Sterne", "können", "jetzt", "mit", "sehr", "geringer", "Masse", "stabilisiert", "werden",
                                "Sie", "können", "so", "leicht", "sein,", "dass", "sie", "nach", "ihrer", "Entstehung",
                                "sofort", "zu", "Zwergen", "werden", "ohne", "die", "Hauptreihe", "zu", "erreichen.",
                                "Sterne zwischen 0.01 und 0.3 Massen sind möglich", " "]

PerfektionVICost = 3000
PerfektionIconVI_X = PerfektionIconI_X - 75
PerfektionIconVI_Y = PerfektionIconI_Y + 300
PerfektionIconVIURL = "Pictures/PerfektionVI.jpg"
PerfektionIconVIBlockedURL = "Pictures/PerfektionVI_sw.jpg"
PerfektionIconVIHeader = "Riesen"
PerfektionIconVIDescription = ["Durch", "eine", "erfolgreiche", "Erforschung", "des", "Aldebaran", "können", "sich",
                                "unsere", "Sterne", "nach", "dem", "Hauptreihenstadium", "zu", "Riesen", "entwickeln",
                                "und", "viel", "Strahlung", "abgeben,", "bevor", "sie", "zu", "Zwergen", "werden.",
                                "Typ Riese wird freigeschalten", "Kosten: " + str(PerfektionVICost) + " Metall", " "]

PerfektionVIICost = 3000
PerfektionIconVII_X = PerfektionIconI_X - 150
PerfektionIconVII_Y = PerfektionIconI_Y + 400
PerfektionIconVIIURL = "Pictures/PerfektionVII.jpg"
PerfektionIconVIIBlockedURL = "Pictures/PerfektionVII_sw.jpg"
PerfektionIconVIIHeader = "Ausdauernd"
PerfektionIconVIIDescription = ["Unsere", "Sterne", "optimieren", "ihren", "Brennstoffhaushalt,", "sodass", "sie",
                                "viel", "länger", "in", "einer", "Phase", "verweilen", "können,", "bevor", "sie",
                                "sich", "weitereintwickeln.", "Zeit bis zur Umwandlung * 1.25",
                                "Kosten: " + str(PerfektionVIICost) + " Metall", " "]

PerfektionVIIICost = 3000
PerfektionIconVIII_X = PerfektionIconI_X
PerfektionIconVIII_Y = PerfektionIconI_Y + 400
PerfektionIconVIIIURL = "Pictures/PerfektionVIII.jpg"
PerfektionIconVIIIBlockedURL = "Pictures/PerfektionVIII_sw.jpg"
PerfektionIconVIIIHeader = "Schnelles Schalenbrennen"
PerfektionIconVIIIDescription = ["Die", "äußeren", "Schalen", "werden", "stärker", "Aufgebläht,", "sodass", "sie", "ihren",
                                    "Brennstoff", "schneller", "und", "unter", "größerer", "Strahlungsabgabe", "umsetzen",
                                    "können.", "Zeit bis zur Umwandlung * 0.8", "Strahlung * 1.4",
                                    "Kosten: " + str(PerfektionVIIICost) + " Metall", " "]

KraftICost = 3000
KraftIconI_X = TechSubHeaderTextKraftX
KraftIconI_Y = TechSubHeaderTextKraftY + 50
KraftIconIURL = "Pictures/KraftI.jpg"
KraftIconIBlockedURL = "Pictures/KraftI_sw.jpg"
KraftIconIHeader = "Q-Burst"
KraftIconIDescription = ["Wir", "können", "nun", "einem", "Stern", "befehlen,", "eine", "gewisse", "Menge", "Strahlung",
                            "zu", "benutzen", "und", "seinem", "momentanen", "Feind", "enormen", "Schaden", "zuzufügen.",
                            "Ermöglicht Q-Burst", "Kosten: " + str(KraftICost) + " Metall", " "]

KraftIICost = 3000
KraftIconII_X = KraftIconI_X
KraftIconII_Y = KraftIconI_Y + 100
KraftIconIIURL = "Pictures/KraftII.jpg"
KraftIconIIBlockedURL = "Pictures/KraftII_sw.jpg"
KraftIconIIHeader = "Konzentrierte Jets"
KraftIconIIDescription = ["Die", "Auswürfe", "reiner", "Energie", "an", "den", "beiden", "Rotationspolen", "der", "Sterne",
                            "werden", "verschmälert", "und", "konzentriert.", "Dadurch", "können", "sie", "auf", "eine",
                            "größere", "Entfernung", "Schaden", "verursachen.", "Kosten: " + str(KraftIICost) + " Metall", " "]

KraftIIICost = 3000
KraftIconIII_X = KraftIconI_X - 75
KraftIconIII_Y = KraftIconI_Y + 200
KraftIconIIIURL = "Pictures/KraftIII.jpg"
KraftIconIIIBlockedURL = "Pictures/KraftIII_sw.jpg"
KraftIconIIIHeader = "Sonnenwinde"
KraftIconIIIDescription = ["Wenn", "sie", "sich", "im", "Kampf", "befinden,", "können", "unsere", "Sterne", "bewusst",
                            "Eruptionen", "mit", "großen", "Energiedichten", "verursachen,", "die", "feindliche", "Angriffe",
                            "vor", "dem", "Auftreffen", "schwächen.", "Kosten: " + str(KraftIIICost) + " Metall", " "]

KraftIVCost = 3000
KraftIconIV_X = KraftIconI_X
KraftIconIV_Y = KraftIconI_Y + 200
KraftIconIVURL = "Pictures/KraftIV.jpg"
KraftIconIVBlockedURL = "Pictures/KraftIV_sw.jpg"
KraftIconIVHeader = "Blitzkrieg"
KraftIconIVDescription = ["Unsere", "Sterne", "sind", "darauf", "traniert,", "angeordnete", "Befehle", "sehr", "schnell",
                            "auszuführen", "und", "ihre", "Vorbereitungen", "möglichst", "schnell", "auszuführen.",
                            "Zeit bis zum Angriff * 0.6", "Kosten: " + str(KraftIVCost) + " Metall", " "]

KraftVCost = 3000
KraftIconV_X = KraftIconI_X + 75
KraftIconV_Y = KraftIconI_Y + 200
KraftIconVURL = "Pictures/KraftV.jpg"
KraftIconVBlockedURL = "Pictures/KraftV_sw.jpg"
KraftIconVHeader = "Schnelle Adaption"
KraftIconVDescription = ["Sterne,", "über", "die", "wir", "kürzlich", "die", "Kontrolle", "gewonnen", "haben,", "werden",
                            "schneller", "unseren", "Befehlen", "untergeordnet", "und", "sich", "mehr", "von", "den", "Wunden",
                            "erholen.", "HP nach Übernahme 80% statt 50%", "Kosten: " + str(KraftVCost) + " Metall", " "]

KraftVICost = 3000
KraftIconVI_X = KraftIconI_X
KraftIconVI_Y = KraftIconI_Y + 300
KraftIconVIURL = "Pictures/KraftVI.jpg"
KraftIconVIBlockedURL = "Pictures/KraftVI_sw.jpg"
KraftIconVIHeader = "Sternbild-Konfiguration"
KraftIconVIDescription = ["Um", "gemeinsame", "Angriffe", "auf", "einen", "Feind", "effektiver", "zu", "machen,", "werden",
                            "sich", "unsere", "Sterne", "als", "gemeinsames", "Sternbild", "und", "Kollektiv", "verstehen,",
                            "anstatt", "den", "Feind", "einzeln", "nierderzuringen.", "Kosten: " + str(KraftVICost) + " Metall", " "]

KraftVIICost = 3000
KraftIconVII_X = KraftIconI_X + 125
KraftIconVII_Y = KraftIconI_Y
KraftIconVIIURL = "Pictures/KraftVII.jpg"
KraftIconVIIBlockedURL = "Pictures/KraftVII_sw.jpg"
KraftIconVIIHeader = "Schwarzes Loch"
KraftIconVIIDescription = ["Durch", "die", "erfolgreiche", "Erforschung", "von", "Saggaitarius A*", "können", "unsere", "sehr",
                            "Massereichen", "Sterne", "nun", "nach", "ihrem", "Leben", "zu", "Schwarzen", "Löchern", "werden,",
                            "die", "stark", "genug", "sind", "um", "die", "ganze", "Raumzeit", "in", "Stücke", "zu", "reißen",
                            "Schwarzes Loch möglich", "Kosten: " + str(KraftVIICost) + " Metall", " "]

KraftVIIICost = 3000
KraftIconVIII_X = KraftIconI_X + 125
KraftIconVIII_Y = KraftIconI_Y + 100
KraftIconVIIIURL = "Pictures/KraftVIII.jpg"
KraftIconVIIIBlockedURL = "Pictures/KraftVIII_sw.jpg"
KraftIconVIIIHeader = "Kern-Neuausrichtung"
KraftIconVIIIDescription = ["Die", "Kerne", "aller", "Sterne", "werden", "neu", "ausgerichtet", "um", "ihre", "Energie", "im",
                                "Kampf", "besser", "nutzen", "zu", "können.", "Kosten: " + str(KraftVIIICost) + " Metall", " "]

WeisheitICost = 3000
WeisheitIconI_X = TechSubHeaderTextWeisheitX
WeisheitIconI_Y = TechSubHeaderTextWeisheitY + 50
WeisheitIconIURL = "Pictures/WeisheitI.jpg"
WeisheitIconIBlockedURL = "Pictures/WeisheitI_sw.jpg"
WeisheitIconIHeader = "Verbesserete Konvektion"
WeisheitIconIDescription = ["Indem", "die", "verschiedenen", "Schichten", "von", "Stoffen", "in", "unseren", "Hauptreihensternen",
                            "neu", "sortiert", "werden", "kann", "bedeutend", "mehr", "Strahlung", "ihre", "Oberfläche", "verlassen.",
                            "Hauptreihensterne: Strahlung + 20 %", "Kosten: " + str(WeisheitICost) + " Metall", " "]

WeisheitIICost = 3000
WeisheitIconII_X = WeisheitIconI_X - 75
WeisheitIconII_Y = WeisheitIconI_Y + 100
WeisheitIconIIURL = "Pictures/WeisheitII.jpg"
WeisheitIconIIBlockedURL = "Pictures/WeisheitII_sw.jpg"
WeisheitIconIIHeader = "Schnellvorlauf"
WeisheitIconIIDescription = ["Wir", "sind", "jetzt", "in", "der", "Lage,", "einen", "Stern", "verfrüht", "in", "seine", "nächste",
                                "Phase", "übergehen", "zu", "lassen,", "wenn", "wir", "ihm", "einige", "Stahlungsenergie", "zur",
                                "Verfügung", "stellen", "Schaltet Schnellvorlauf frei", "Kosten: " + str(WeisheitIICost) + " Metall", " "]

WeisheitIIICost = 3000
WeisheitIconIII_X = WeisheitIconI_X
WeisheitIconIII_Y = WeisheitIconI_Y + 100
WeisheitIconIIIURL = "Pictures/WeisheitIII.jpg"
WeisheitIconIIIBlockedURL = "Pictures/WeisheitIII_sw.jpg"
WeisheitIconIIIHeader = "Entkernung"
WeisheitIconIIIDescription = ["Wenn", "Sterne", "in", "eine", "andere", "Phase", "übergehen,", "können", "wir", "einen", "größeren",
                                "Anteil", "an", "Metallen", "aus", "ihrem", "Kern", "nutzen", "als", "bisher.",
                                "Metalle beim Übergang + 15%", "Kosten: " + str(WeisheitIIICost) + " Metall", " "]

WeisheitIVCost = 3000
WeisheitIconIV_X = WeisheitIconI_X
WeisheitIconIV_Y = WeisheitIconI_Y + 200
WeisheitIconIVURL = "Pictures/WeisheitIV.jpg"
WeisheitIconIVBlockedURL = "Pictures/WeisheitIV_sw.jpg"
WeisheitIconIVHeader = "Feldverteilung"
WeisheitIconIVDescription = ["Indem", "alle", "unsere", "Sterne", "ihre", "Magnetischen", "Felder", "neu", "ausrichten," "können", "wir",
                                "feindliche", "Attacken", "abschwächen,", "bevor", "sie", "überhaupt", "in", "die", "Nähe", "unserer",
                                "Sterne", "kommen.", "Kosten: " + str(WeisheitIVCost) + " Metall", " "]

WeisheitVCost = 3000
WeisheitIconV_X = WeisheitIconI_X + 75
WeisheitIconV_Y = WeisheitIconI_Y + 200
WeisheitIconVURL = "Pictures/WeisheitV.jpg"
WeisheitIconVBlockedURL = "Pictures/WeisheitV_sw.jpg"
WeisheitIconVHeader = "Gigantendoktrin"
WeisheitIconVDescription = ["Unsere", "Sterne", "im", "Riesenstadium", "geben", "sehr", "viel", "Strahlung", "ab,", "sind", "aber", "anfällig",
                            "für", "gegnerische", "Angriffe.", "Um", "diesen", "Zustand", "zu", "verändern,", "können", "wir", "ihnen", "mit",
                            "dieser", "Doktrin", "mehr", "Kraft", "geben,", "Angriffen", "zu", "wiederstehen.", "HP von Riesen + 10%",
                            "Kosten: " + str(WeisheitVCost) + " Metall", " "]

WeisheitVICost = 3000
WeisheitIconVI_X = WeisheitIconI_X + 50
WeisheitIconVI_Y = WeisheitIconI_Y + 300
WeisheitIconVIURL = "Pictures/WeisheitVI.jpg"
WeisheitIconVIBlockedURL = "Pictures/WeisheitVI_sw.jpg"
WeisheitIconVIHeader = "Erstschlag"
WeisheitIconVIDescription = ["Wenn", "wir", "Angriffe", "auf", "Feinde", "beginnen,", "können", "wir", "mit", "einem", "Erstschlag", "ihre",
                                "Verteidigung", "schwächen", "bevor", "der", "Kampf", "überhaupt", "begonnen", "hat.",
                                "Kosten: " + str(WeisheitVICost) + " Metall", " "]

WeisheitVIICost = 3000
WeisheitIconVII_X = WeisheitIconI_X + 125
WeisheitIconVII_Y = WeisheitIconI_Y
WeisheitIconVIIURL = "Pictures/WeisheitVII.jpg"
WeisheitIconVIIBlockedURL = "Pictures/WeisheitVII_sw.jpg"
WeisheitIconVIIHeader = "Neutronenstern"
WeisheitIconVIIDescription = ["Durch", "unser", "intensives", "Studium", "von", "Scorpio X-1", "können", "unsere", "Sterne", "nun", "den", "Status",
                                "eines", "Neutronensterns", "erlangen.", "In", "diesem", "Stadium", "können", "sie", "zwar", "keine", "Strahlung",
                                "abgeben,", "aber", "immense", "Energien", "im", "Kampf", "freisetzen.", "Neutronenstern wird freigeschalten",
                                "Kosten: " + str(WeisheitVIICost) + " Metall", " "]

WeisheitVIIICost = 3000
WeisheitIconVIII_X = WeisheitIconI_X + 125
WeisheitIconVIII_Y = WeisheitIconI_Y + 100
WeisheitIconVIIIURL = "Pictures/WeisheitVIII.jpg"
WeisheitIconVIIIBlockedURL = "Pictures/WeisheitVIII_sw.jpg"
WeisheitIconVIIIHeader = "Neutronenstern"
WeisheitIconVIIIDescription = ["Unsere", "Zwerge,", "Neutronensterne", "und", "Schwarzen", "Löcher,", "die", "ältesten", "unter", "unseren", "Sternen",
                                "werden", "ihr", "über", "Äonen", "gesammeltes", "Wissen", "noch", "besser", "nutzen", "können", "um", "unsere",
                                "Feinde", "zu", "zermalmen.", "Zwerge +20% Angriff",
                                "Kosten: " + str(WeisheitVIIICost) + " Metall", " "]

spaceCloseIcon = 5
sizeCloseIconX = 20
sizeCloseIconY = 20
closeIconURL = "Pictures/ic_close_black_48dp_1x.png"

headerTextX = 10
headerTextY = 5
HeaderTextColor = (10,10,10)

mainIconURL = "Pictures/logo_neu_klein.png"


InfoBoxPicX = 150
InfoBoxPicY = 150
PicSpaceX = 5
PicSpaceY = 50
schwarzesLochURL = "Pictures/SchwarzesLoch.jpg"
hauptreiheURL = "Pictures/Hauptreihe.jpg"
rieseURL = "Pictures/Riese.jpg"
zwergURL = "Pictures/Zwerg.jpg"
neutronensternURL = "Pictures/Neutronenstern.jpg"
geburtURL = "Pictures/Geburt.jpg"

textSpace = 5

catTextX = InfoBoxPicX + 2 * PicSpaceX
catTextY = PicSpaceY
CatTextColor = (0,0,0)

ageTextX = catTextX
ageTextY = catTextY + fontSizeSmall + textSpace
ageTextColor = (0,0,0)

massTextX = catTextX
massTextY = catTextY + 2 * fontSizeSmall + 2 * textSpace
massTextColor = (0,0,0)

NextLevelTextX = catTextX
NextLevelTextY = catTextY + 3 * fontSizeSmall + 3 * textSpace
nextLevelTextColor = black

attackTextX = catTextX
attackTextY = catTextY + 4 * fontSizeSmall + 4 * textSpace
attackTextColor = (0,0,0)

healthTextX = catTextX
healthTextY = catTextY + 5 * fontSizeSmall + 5 * textSpace
HealthTextColor = (0,0,0)

errorBoxX = 200
errorBoxY = 100
errorBoxHeaderSpaceX = 10
errorBoxHeaderSpaceY = 10
errorBoxTextSpaceX = 10
errorBoxTextSpaceY = errorBoxHeaderSpaceY + 2 * fontSize

InfoBoxIconSize = 48

buttonX = 32
buttonY = 32
attackIconURL = "Pictures/sword.png"
healIconURL = "Pictures/heal.png"
forwardIconURL = "Pictures/fastforward.png"
bombIconURL = "Pictures/bombe.jpg"
upgradeIconURL = "Pictures/arrow_up.png"

buttonSpaceX = 100
buttonSpaceY = 10

AnzahlStartSterne = 10

FPS = 10

starNameTeam1 = ["Sirius A",
                    "Beteigeuze",
                    "Deneb",
                    "Sol",
                    "Polaris",
                    "Regulus",
                    "Prokyon B",
                    "Gliese 86 B",
                    "S Doradus",
                    "Pistolenstern",
                    "Capella",
                    "Pollux",
                    "Mira"]

starMassTeam1 = [2.12,
                    10,
                    13,
                    1,
                    4.5,
                    3.5,
                    1.7,
                    0.79,
                    14,
                    19,
                    2.5,
                    1.86,
                    1.2]   #Sonnenmassen

starCatTeam1 = ["Hauptreihe", "Überriese", "Hyperriese", "Hauptreihe", "Überriese", "Hauptreihe", "Zwerg", "Zwerg", "Hyperriese", "Hyperriese", "Riese", "Riese", "Riese"]    #Kategorie in der der Stern startet
starAgeTeam1 = [238, 10, 69, 4500, 111, 50, 1700, 2400, 87, 2, 23, 16, 12] #Jahre

starNameTeam2 = ["Rigel", "Altair", "Wega", "Van Maansens Stern", "40 Eridani D", "P Cygni", "Eta Carinae", "Cygnus OB2", "Castor", "Gliese 583", "Acrux", "46 Leonis Mioris"]
starMassTeam2 = [10, 1.7, 2.2, 0.7, 0.75, 13, 16, 18, 2.15, 0.33, 14, 1.5]
starCatTeam2 = ["Riese", "Hauptreihe", "Hauptreihe", "Zwerg", "Zwerg", "Hyperriese", "Hyperriese", "Hyperriese", "Riese", "Hauptreihe", "Riese", "Riese"]
starAgeTeam2 = [100, 1000, 480, 4000, 3100, 27, 3, 4, 35, 12, 10, 8]

specialStarName = ["Scorpio X-1", "Saggittarius A*", "Aldebaran"]
specialStarMass = [1.4, 4000000, 2.5]
specialStarCat = ["Neutronenstern", "Schwarzes Loch", "Riese"]
specialStarAge = [5000, 5000, 137]

if not pygame.init():
    pass
   #print("Initilation not succesful")

pygame.font.init()
pygame.mixer.init()



exampleFontSize = 16

KaushanFontExample = pygame.font.Font("Fonts/Kaushan_Script/KaushanScript-Regular.ttf", exampleFontSize)
Noto_SansFontExample = pygame.font.Font("Fonts/Noto_Sans/NotoSans-Regular.ttf", exampleFontSize)
OrbitronFontExample = pygame.font.Font("Fonts/Orbitron/Orbitron-Regular.ttf", exampleFontSize)
QuicksandFontExample = pygame.font.Font("Fonts/Quicksand/Quicksand-Regular.ttf", exampleFontSize)
RalewayFontExample = pygame.font.Font("Fonts/Raleway/Raleway-Regular.ttf", exampleFontSize)
RighteousFontExample = pygame.font.Font("Fonts/Righteous/Righteous-Regular.ttf", exampleFontSize)
SatisfyFontExample = pygame.font.Font("Fonts/Satisfy/Satisfy-Regular.ttf", exampleFontSize)
UbuntuFontExample = pygame.font.Font("Fonts/Ubuntu/Ubuntu-Regular.ttf", exampleFontSize)

#pygame.display.flip()      #Gesamtes Display wird geupdatet
#pygame.display.update()     #Wenn keine Parameter ganzes Display, sonst nur Bereich wird updatet

class Nynyezi:
    def __init__(self):
        self.gameDisplay = pygame.display.set_mode([display_x, display_y])

        pygame.display.set_caption(gameTitle)
        pygame.display.set_icon(self.loadImage(mainIconURL, colorkey=(255,0,0)))#colorkey=(0,0,0)


        self.MasterVolume=0.5
        self.MusicVolume=0.7
        self.SFXVolume=0.6

        self.clock = pygame.time.Clock()

        self.infoBoxOpen = False
        self.infoBoxStar = {}
        self.infoBoxTeam = "kein Team"

        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.set_volume(self.MasterVolume*self.MusicVolume)
        pygame.mixer.music.play(loops=-1)

        self.showErrorOpen = False

        self.MainFontBig = pygame.font.Font("Fonts/Orbitron/Orbitron-Regular.ttf", fontSizeBig)
        self.MainFont = pygame.font.Font('Fonts/Orbitron/Orbitron-Regular.ttf', fontSize)
        self.MainFontSmall = pygame.font.Font('Fonts/Orbitron/Orbitron-Regular.ttf', fontSizeSmall)
        self.MainFontMiddle = pygame.font.Font('Fonts/Orbitron/Orbitron-Regular.ttf', fontSizeMiddle)

        self.TechOpen = False
        self.TechInfoOpen = False
        self.newtechinfo = False

        self.EventButtonHover = False
        self.NewStarHover = False
        self.TechHover = False
        self.StrahlungHover = False
        self.MetallHover = False

        self.InfoSettings = False
        self.SettingsOpen = False
        self.InfoInfo = False
        self.InfoOpen = False
        self.NewStarOpen = False
        self.NewStarBuild = False
        self.nameEingeben = 0
        self.nameFlag = 0
        self.nameString = " "
        self.NewStarCost = 0
        self.NewStarSizeCord = 175
        self.NewStarSlide = False
        self.NewStarNameTextColor = black
        self.choosePlace = False
        self.MasterVolumeSliderMove = False
        self.MusicVolumeSliderMove = False
        self.SFXVolumeSliderMove = False
        self.MasterVolumeSliderPos=0
        self.MusicVolumeSliderPos=70
        self.SFXVolumeSliderPos=55
        self.VolumeSliderSize=10

        self.Attacks = []

        self.EventButtonSurfaces = []
        self.timer = [{"time": 60*30, "name": "gameend", "effect": "self.gameover = True", "ongoingeffect": " "}, {"time": 40, "name": "Crisis_Dark_Matter", "effect":
"""
roll = random.randint(0, 100)
counter = 0
if self.yourTeam == 'Team1':
    for star in self.starArrayTeam1:
        if star['cat'] == 'Neutronenstern':
            counter += star['mass']*2/3
        elif star['cat'] == 'Schwarzes Loch':
            counter += star['mass']*1.2
else:
    for star in self.starArrayTeam2:
        if star['cat'] == 'Neutronenstern':
            counter += star['mass']*2/3
        elif star['cat'] == 'Schwarzes Loch':
            counter += star['mass']*1.2
print(roll, "roll", counter, "counter")
if roll in range(-15, round(counter-15)):
    self.drawEvent('Crisis_Dark_Matter_Start')
    for timer in self.timer:
        if timer['name'] == 'Crisis_Dark_Matter':
            self.timer.remove(timer)
else:
    for timer in self.timer:
        if timer['name'] == 'Crisis_Dark_Matter':
            timer['time'] = 40
""", "ongoingeffect": "perpetual"}]
        self.Events = [{"name": "ersteEntwicklung", "Header": "Die erste Entwicklung", "text": "Einer eurer Sterne hat lange genug gelebt um in eine neue Lebensphase überzugehen. Alle eure Sterne entwicklen sich mit der Zeit und durchlaufen verschiedene Stadien.", "state": False, "buttons": [{"name": "OK", "effect": " ", "bedingung": "True", "hovertext": None}]}, {"name": "RieseErforschen", "Header": "Die Geheimnisse des Aldebaran", "text": "Aldebaran ist wahrlich ein Riese mit Herz und Seele. Er ist 45 mal größer als die Sonne und leuchtet gigantische 150 mal so hell wie sie. Er verbrennt in seiner aufgeblähten Schale stoffe viel weiter als nur bis zum Helium und nutz viel mehr von seinem Brennstoffvorrat.", "state": False, "buttons": [{"name": "Später", "effect": " ", "bedingung": "True", "hovertext": None}, {"name": "Startet die Erforschung", "effect": "self.RieseErforschenStart()", "bedingung": "(self.metalleTeam1>500 and self.strahlungTeam1>=2000000 and self.yourTeam == 'Team1') or (self.metalleTeam2>500 and self.strahlungTeam2>=2000000 and self.yourTeam == 'Team2')", "hovertext": "Die Erforschung wird in einiger Zeit abgeschlossen sein. Kostet 2 Mio. Strahlung und 500 Metalle."}]}, {"name": "SchwarzeslochErforschen", "Header": "Die Macht des Saggitarius A*", "text": "In der Mitte der Galaxis trohnt Saggitarius A*. Mit ihrer tatsächlichen Masse von etwa 4 Mio Sonnenmassen ist sie gigantisch und kaum vorstellbar. Schon lange wollen wir seine Macht entschlüsseln. Nach so langer Zeit könnten wir dieses Ziel endlich erreichen.", "state": False, "buttons": [{"name": "Später", "effect": " ", "bedingung": "True", "hovertext": None}, {"name": "Startet die Erforschung", "effect": "self.SchwarzeslochErforschenStart()", "bedingung": "(self.metalleTeam1>500 and self.strahlungTeam1>=2000000 and self.yourTeam == 'Team1') or (self.metalleTeam2>500 and self.strahlungTeam2>=2000000 and self.yourTeam == 'Team2')", "hovertext": "Die Erforschung wird in weniger Zeit abgeschlossen sein. Kostet 2 Mio. Strahlung und 500 Metall"}]}, {"name": "NeutronsternErforschen", "Header": "Die Erfahrung des Scorpio X-1", "text": "Der Neutronenstern Scorpio X-1 ist ein gigant seiner eigenen Klasse. Er ist eine der stärksten Röntgenquellen in unserer Galaxis, unglaublich dicht und sehr mächtig. Dieses Stadium wollen wir schon lange für unsere eigenen Sterne erreichen.", "state": False, "buttons": [{"name": "Später", "effect": " ", "bedingung": "True", "hovertext": None}, {"name": "Startet die Erforschung", "effect": "self.NeutronsternErforschenStart()", "bedingung": "(self.metalleTeam1>500 and self.strahlungTeam1>=2000000 and self.yourTeam == 'Team1') or (self.metalleTeam2>500 and self.strahlungTeam2>=2000000 and self.yourTeam == 'Team2')", "hovertext": "Die Erforschung wird in weniger Zeit abgeschlossen sein. Kostet 2 Mio. Strahlung und 500 Metall."}]}, {"name": "RieseErforscht", "Header": "Geheimnisse Gelueftet", "text": "Du hast einen Riesen erforscht und dadurch die Entwicklungsstufe Riese freigeschaltet! Riesen sind Sterne, deren Radius zwischen 10 und 100 Sonnenradien beträgt. Aufgrund ihrer Größe emittieren Riesen sehr viel Strahlung und produzieren beim Übergang ins Zwergenstadium viele Metalle.", "state": False, "buttons": [{"name": "Ein Großer Schritt", "effect":
"""
if self.yourTeam=='Team1':
    self.techArrayTeam1['Perfektion'][5] = True
else:
    self.techArrayTeam2['Perfektion'][5] = True
""",
        "bedingung": "True", "hovertext": "Wir haben nun Zugriff auf Riesen."}]},
        {"name": "SchwarzeslochErforscht", "Header": "Macht absorbiert", "text": "Schwarze Löcher entstehen, wenn Sterne mit einer großen Masse sterben. Sie haben dann eine sehr große Masse, die in einer Singularität, einem unendlich kleinen Punkt, konzentriert ist. Schwarze Löcher ziehen daher alles in ihrer Umgebung an, sogar das Licht, und absorbieren es. Ein Schwarzes Loch kostet dich daher Strahlung und produziert keine Metaalle aber ist im Kampf, aufgrund seiner hohen Masse, sehr stark.", "state": False, "buttons": [{"name": "Eine große Erkenntnis", "effect":
"""
if self.yourTeam=='Team1':
    self.techArrayTeam1['Kraft'][6] = True
else:
    self.techArrayTeam2['Kraft'][6] = True
""",
        "bedingung": "True", "hovertext": "Wir haben nun Zugriff auf Schwarze Löcher"}]},
        {"name": "NeutronsternErforscht", "Header": "Lebenserfahrung gewonnen", "text": "Du hast einen Neutronenstern erforscht und dadurch die Entwicklungsstufe Neutronenstern freigeschaltet! Neutronensterne entstehen durch den Tod eines Sterns. Sie haben eine sehr große Masse und emittieren keine Strahlung mehr. Metalle produzieren Neutronensterne ebenfalls nicht aber ihre Masse macht sie im Kampf zu einer sehr starken Waffe.", "state": False, "buttons": [{"name": "Eine großer Zugewinn", "effect":
"""
if self.yourTeam=='Team1':
    self.techArrayTeam1['Weisheit'][6] = True
else:
    self.techArrayTeam2['Weisheit'][6] = True
""",
        "bedingung": "True", "hovertext": "Wir haben nun Zugriff auf Neutronsterne."}]},
        {"name": "chooseCat", "Header": "Wichtige Entscheidungen...", "text": "str(star['name']) hat seine Lebensphase beendet. Es liegt an euch, zu entscheiden, wie er sich jetzt weiterentwickeln soll.", "state": False, "buttons": [{"name": "Er soll ein Neutronenstern werden!", "effect":
"""
star['cat']='Neutronenstern'
star['nextLevel'] = 1/(star['mass']+1)**0.5*60/0.1
self.ersterNeutronenstern = True
if self.yourTeam == 'Team1':
    if self.techArrayTeam1['Weisheit'][2]:
        mod = 1.1
    else:
        mod = 1
    if star["mass"] <= 2.3 and star["mass"] < 3:
        self.metalleTeam1 += 400 * mod *(star["mass"]-2.3)/0.7+200
    elif star["mass"] > 3:
        self.metalleTeam1 += 400 * mod * (star["mass"]-3)/17+600
else:
    if self.techArrayTeam2['Weisheit'][2]:
        mod = 1.1
    else:
        mod = 1
    if star["mass"] <= 2.3 and star["mass"] < 3:
        self.metalleTeam2 += 400*(star["mass"]-2.3)/0.7+200
    elif star["mass"] > 3:
        self.metalleTeam2 += 400*(star["mass"]-3)/17+600
""", "bedingung": "(self.yourTeam=='Team1' and self.techArrayTeam1['Weisheit'][6] == True) or (self.yourTeam=='Team2' and self.techArrayTeam2['Weisheit'][6] == True)", "hovertext": "star['name'] wird zum Neutronenstern."}, {"name": "Er soll ein Schwarzes Loch werden!", "effect":
"""
star['cat']='Schwarzes Loch'
star['nextLevel'] = 1/(star['mass']+1)**0.5*60/0.1
self.erstesSchwarzesLoch = star
if self.yourTeam == 'Team1':
    if self.techArrayTeam1['Weisheit'][2]:
        mod = 1.1
    else:
        mod = 1
    if star["mass"] <= 2.3 and star["mass"] < 3:
        self.metalleTeam1 += 400 * mod *(star["mass"]-2.3)/0.7+200
    elif star["mass"] > 3:
        self.metalleTeam1 += 400 * mod * (star["mass"]-3)/17+600
else:
    if self.techArrayTeam2['Weisheit'][2]:
        mod = 1.1
    else:
        mod = 1
    if star["mass"] <= 2.3 and star["mass"] < 3:
        self.metalleTeam2 += 400*(star["mass"]-2.3)/0.7+200
    elif star["mass"] > 3:
        self.metalleTeam2 += 400*(star["mass"]-3)/17+600
""", "bedingung": "(self.yourTeam=='Team1' and self.techArrayTeam1['Kraft'][6]) or (self.yourTeam == 'Team2' and self.techArrayTeam2['Kraft'][6])", "hovertext": "str(star['name']) wird zum Schwarzen Loch."}]},
{"name": "sternhaufen", "Header": "Sternhaufen", "text": "Ihr habt 10 neue Sterne entstehen lassen. Dadurch habt ihr euren Einfluss in der Galaxis weithin ausgedehnt. Aber mit großer Macht kommt...", "state": False, "buttons": [{"name": "...große Weisheit", "effect": "self.techcostmod = 0.95", "bedingung": "True", "hovertext": "Verringert die Kosten für Technologien um 5% bis zum Ende des Spiels."}, {"name": "...kommt große Effizienz.", "effect": "self.starcostmod = 0.9", "bedingung": "True", "hovertext": "Verringert die Kosten für neue Sterne um str(10%) für das restliche Spiel."}, {"name": "...kommt große Verantwortung.", "effect": "self.attackmod = self.attackmod * 1.1", "bedingung": "True", "hovertext": "...erhöht den Schaden, den eure Sterne verursachen um str(10%) für den Rest des Spiels. Mit Vorsicht benutzen!"}]},
{"name": "gameoverlost", "Header": "Interstellare Macht", "text": "Dein Gegner hat ein stärkeres Imperium aufgebaut und sich die Vorherrschaft in diesem Cluster gesichert.", "state": False, "buttons": [{"name": "Wir werden unsere Revance haben!", "effect":
"""
print("Spiel wird geschlossen")
self.connectionFlag = False
#debugmode
self.s.close()
pygame.quit()
quit()
""", "bedingung": "True", "hovertext": "Fürs Spielen bedanken sich Max Heuschkel, Jonas Kubat und Jonathan Schleucher."}]},
{"name": "gameoverwon", "Header": "Interstellare Macht...", "text": "Du hast ein stärkeres Imperium aufgebaut und sich die Vorherrschaft in diesem Cluster gesichert.", "state": False, "buttons": [{"name": "Wir gewinnen!", "effect":
"""
print("Spiel wird geschlossen")
self.connectionFlag = False
#debugmode
self.s.close()
pygame.quit()
quit()
""", "bedingung": "True", "hovertext": "Fürs Spielen bedanken sich Max Heuschkel, Jonas Kubat und Jonathan Schleucher."}]},
{"name": "großerStaubsauger", "Header": "Großer Staubsauger", "text": "Die Masse von str(stern['name']) ist so gigantisch, dass die Gegenkräfte die seiner Gravitation entgegenwirken zu schwach werden um einen Kollaps zu verhindern. Die gesamte Masse fällt auf einen Punkt zusammen und es entsteht eine Singularität. Um sich herum krümmt es schon jetzt die Raumzeit erheblich und kein Licht kann dort noch entkommen. An diesem Beispielobjekt können wir unsere gesamte Strategie ausrichten, wenn ihr möchtet.", "state": False, "buttons": [{"name": "Lasst unsere Strategen arbeiten!", "effect": "self.Krafttechmod = 0.7; self.Perfektiontechmod = 1; self.Weisheittechmod = 1", "bedingung": "True", "hovertext": "Verringert die Kosten für Kraft Technologien drastisch. Setzt eventuelle Bonusse für Perfektion und Weisheit zurück."}, {"name": "Bleiben wir beim alten.", "effect": '', "bedingung": "True", "hovertext": "Behaltet eventuelle Boni auf Perfektion oder Weisheit."}]},
{"name": "ladungfürAnfänger", "Header": "Ladung ist was für Anfänger", "text": "Nachdem str(stern['name']) seinen gesamten Vorrat an Brennstoff zu Eisen umgewandelt hat, werden die Gegenkräfte immer schwächer, die den Stern vor dem Gravitationskollaps bewahrt haben. Die Protonen fangen Neutronen ein und der ganze Stern entartet zu einem einzelnen 'Neutronenbrei'. An diesem Beispielobjekt können wir unsere gesamte Strategie ausrichten, wenn ihr möchtet.", "state": False, "buttons": [{"name": "Lasst unsere Strategen arbeiten!", "effect": "self.Krafttechmod = 1; self.Perfektiontechmod = 1; self.Weisheittechmod = 0.7", "bedingung": "True", "hovertext": "Verringert die Kosten für Weisheit Technologien drastisch. Setzt eventuelle Bonusse für Perfektion und Kraft zurück."}, {"name": "Bleiben wir beim alten.", "effect": "", "bedingung": "True", "hovertext": "Behaltet eventuelle Boni auf Kraft oder Perfektion."}]},
{"name": "großeLeuchte", "Header": "Ein Licht für die Galaxis", "text": "Ihr Kontrolliert euren ersten neuen Riesen. Seine äußerste Schale brennt mit voller Kraft und gibt viel Strahlung ab. An diesem Beispielobjekt können wir unsere gesamte Strategie ausrichten, wenn ihr möchtet.", "state": False, "buttons": [{"name": "Lasst unsere Strategen arbeiten!", "effect": "self.Krafttechmod = 1; self.Perfektiontechmod = 0.7; self.Weisheittechmod = 1", "bedingung": "True", "hovertext": "Verringert die Kosten für Perfektion Technologien drastisch. Setzt eventuelle Bonusse für Kraft und Weisheit zurück."}, {"name": "Bleiben wir beim alten.", "effect": "", "bedingung": "True", "hovertext": "Behaltet eventuelle Boni auf Kraft oder Weisheit."}]},
{"name": "Stratege", "Header": "Großer Stratege", "text": "Durch die Erorberung von 6 feindlichen Sternen habt ihr euch einen Namen als strategisches Genie Gesichert.", "state": False, "buttons": [{"name": "Sehr gut", "bedingung": "True", "hovertext": None, "effect": ""}, {"name": "Steigert die Erfahrung unserer Sterne", "effect":
"""
self.attackmod = self.attackmod * 1.2
if self.yourTeam == 'Team1':
    self.metalleTeam1+=-700
    self.strahlungTeam1+=-1000000
else:
    self.metalleTeam2+=-700
    self.strahlungTeam1+=-1000000
""", "bedingung": "(self.yourTeam == 'Team1' and self.metalleTeam1>=700 and self.strahlungTeam1>=1000000) or (self.yourTeam == 'Team2' and self.metalleTeam2>=700 and self.strahlungTeam2>=1000000)", "hovertext": "Bezahlt 700 Metall und 1000000 Strahlung und erhöht den Schaden eurer Sterne um str(10%)."}]},
{"name": "Crisis_Dark_Matter_Start", "Header": "Dunkle Materie gesichtet", "text": "In unserem Reich wurde dunkle Materie gesichtet. Durch einen seltsamen und uns unerklärlichen Mechanismus konnten wir sie aufspühren, ohne dass sie instabil wurde. Unsere Experten sagen, wir könnten in ihrem Umfeld die abgestrahlten Energien absorbieren und für unsere Zwecke gebrauchen. Andere meinen, wir sollten versuchen, ihre gesamte Energie zu assimilieren, was allerdings als gefährlich angesehen wird.", "state": False, "buttons": [{"name": "Absorbiert nur die Strahlung in der Nähe", "effect":
"""
if self.yourTeam == 'Team1':
    self.strahlungTeam1+=500000
else:
    self.strahlungTeam2+=500000
""", "bedingung": "True", "hovertext": "erhaltet 500.000 Strahlung"}, {"name": "Assimiliert es komplet!", "effect": "self.timer.append(Crisis_Dark_Matter_Timer)", "bedingung": "True", "hovertext": "Der Erfolg unserer Mission wird sich in kurzer Zeit zeigen."}]},
{"name": "Crisis_Dark_Matter_Breakout", "Header": "Weißes Loch freigelassen", "text": "Unsere Versuche, die dunkle Materie zu assimilieren sind fehlgeschlagen. Noch viel schlimmer: unser unqualifizierter Eingriff hat zum Ausbruch eines Weißen Loches geführt. Genährt durch die Materie eines anderen Universum verschlingt es unsere Sterne. Wir müsen einen Weg findes es zurückzuschlagen!", "state": False, "buttons": [{"name": "Eine überwältigende Gefahr", "hovertext": "Ein Weißes Loch entsteht und verschlingt eure Sterne.", "bedingung": "True", "effect": "self.Crisis_Dark_Matter_Create()"}]}
]


        self.starArrayTeam1 = []
        self.starArrayTeam2 = []
        self.starArraySpecial = []
        self.starArrayHostileTeam1 = []
        self.starArrayHostileTeam2 = []
        self.gameExit = False
        self.chooseAttackStar = False
        self.OngoingAttacksMods = []
        self.techArrayTeam1 = {"Kraft": [False, False, False, False, False, False, False, False, False],
                                "Weisheit": [False, False, False, False, False, False, False, False],
                                "Perfektion": [False, False, False, False, False, False, False, False]}
        self.techArrayTeam2 = {"Kraft": [False, False, False, False, False, False, False, False, False],
                                "Weisheit": [False, False, False, False, False, False, False, False],
                                "Perfektion": [False, False, False, False, False, False, False, False]}

        #self.strahlungTeam1 = 0
        #self.metalleTeam1 = 0
        #self.strahlungTeam2  = 0
        #self.metalleTeam2 = 0

        self.strahlungTeam1 = 1000000000
        self.metalleTeam1 = 1200000
        self.strahlungTeam2 = 10000000000
        self.metalleTeam2 = 10000000

        #eventflags und mods
        self.techcostmod = 1.0
        self.starcostmod = 1.0
        self.attackmod = 1.0
        self.Perfektiontechmod = 1.0
        self.Krafttechmod = 1.0
        self.Weisheittechmod = 1.0

        self.ersterRiese = None
        self.ersterRieseflag = False
        self.erstesSchwarzesLoch = None
        self.erstesSchwarzesLochflag = False
        self.ersterNeutronenstern = None
        self.ersterNeutronensternflag = False
        self.Riesetechflag = False
        self.SchwarzesLochflag = False
        self.Neutronensternflag = False
        self.sterneerobert = 0
        self.gameover = False
        self.quit = False



        self.TechIcon = self.loadImage(TechIconURL, size=(IconSize, IconSize))
        self.NewStarIcon = self.loadImage(NewStarIconURL, size=(IconSize, IconSize))

        self.MetallIcon = self.loadImage(metallIconURL, size=(MetallIconSize, MetallIconSize))
        self.StrahlungIcon = self.loadImage(strahlungIconURL, size=(StrahlungIconSize, StrahlungIconSize))

        self.CloseIcon = self.loadImage(closeIconURL, size=(sizeCloseIconX,sizeCloseIconY))
        self.TechCloseIcon = self.loadImage(closeIconURL, size=(sizeTechCloseIconX, sizeTechCloseIconY))

        self.MusicOnIcon = self.loadImage(MusicOnIconURL, size=(VolumeIconSize, VolumeIconSize))
        self.MusicOffIcon = self.loadImage(MusicOffIconURL, size=(VolumeIconSize, VolumeIconSize))
        self.InfoIcon = self.loadImage(InfoIconURL, size=(InfoIconSize, InfoIconSize))
        self.SettingsIcon = self.loadImage(settingsIconURL, size=(SettingsIconSize, SettingsIconSize))
        self.Logo = self.loadImage(LogoURL, size=(LogoSize, LogoSize), colorkey=(0,0,0))

        self.RahmenWeissObenLinks = self.loadImage(RahmenWeissObenLinksURL, size=(RahmenSizeObenX, RahmenSizeObenY), colorkey=(0, 0, 0))
        self.RahmenWeissObenRechts = self.loadImage(RahmenWeissObenRechtsURL, size=(RahmenSizeObenX, RahmenSizeObenY), colorkey=(0,0,0))
        self.RahmenWeissUntenLinks = self.loadImage(RahmenWeissUntenLinksURL, size=(RahmenSizeUntenX, RahmenSizeUntenY), colorkey=(0,0,0))
        self.RahmenWeissUntenRechts = self.loadImage(RahmenWeissUntenRechtsURL, size=(RahmenSizeUntenX, RahmenSizeUntenY), colorkey=(0,0,0))
        self.EventBoxBackground = self.loadImage(EventBoxBackgroundURL, colorkey = (0,0,0))
        self.Button1unhover = self.loadImage(Button1unHoverURL)
        self.Button1hover = self.loadImage(Button1HoverURL)
        self.Sternabzeichen = self.loadImage(SternabzeichenURL, size = (40,40), colorkey = -1)


        self.BackgroundPicture = self.loadImage(BackgroundURL, size=(display_x, display_y))
        self.BackgroundPictureMain = self.loadImage("Pictures/BackgroundMain.jpg", size=(display_x, display_y))

        disp3=round(display_x/3)

        self.NameSchonVergeben = False

        self.HRD_UnDef = self.loadImage("Pictures/HRD_UnDef.jpg", size=(int(150 * 150/178), 150))
        self.HRD_Hauptreihe = self.loadImage("Pictures/HRD_Hauptreihe.jpg", size=(150, 146))
        self.HRD_Zwerge = self.loadImage("Pictures/HRD_Zwerge.jpg", size=(150, 146))
        self.HRD_Riese = self.loadImage("Pictures/HRD_Riesen.jpg", size=(150, 146))
        self.HRD_Riese_schwer = self.loadImage("Pictures/HRD_Riesen_schwer.jpg", size=(150, 146))

        self.PerfektionBackgroundBlack = self.loadImage(PerfektionBackgroundBlackURL, size=(disp3, display_y))
        self.PerfektionBackgroundColor = self.loadImage(PerfektionBackgroundColorURL, size=(disp3, display_y))
        self.KraftBackgroundBlack = self.loadImage(KraftBackgroundBlackURL, size=(disp3, display_y))
        self.KraftBackgroundColor = self.loadImage(KraftBackgroundColorURL, size=(disp3, display_y))
        self.WeisheitBackgroundBlack = self.loadImage(WeisheitBackgroundBlackURL, size=(disp3, display_y))
        self.WeisheitBackgroundColor = self.loadImage(WeisheitBackgroundColorURL, size=(disp3, display_y))


        self.PerfektionIconI = self.loadImage(PerfektionIconIURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconIBlocked = self.loadImage(PerfektionIconIBlockedURl, size=(TechIconSizeX, TechIconSizeY))

        self.PerfektionIconII = self.loadImage(PerfektionIconIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconIIBlocked = self.loadImage(PerfektionIconIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.PerfektionIconIII = self.loadImage(PerfektionIconIIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconIIIBlocked = self.loadImage(PerfektionIconIIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.PerfektionIconIV = self.loadImage(PerfektionIconIVURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconIVBlocked = self.loadImage(PerfektionIconIVBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.PerfektionIconV = self.loadImage(PerfektionIconVURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconVBlocked = self.loadImage(PerfektionIconVBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.PerfektionIconVI = self.loadImage(PerfektionIconVIURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconVIBlocked = self.loadImage(PerfektionIconVIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.PerfektionIconVII = self.loadImage(PerfektionIconVIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconVIIBlocked = self.loadImage(PerfektionIconVIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.PerfektionIconVIII = self.loadImage(PerfektionIconVIIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.PerfektionIconVIIIBlocked = self.loadImage(PerfektionIconVIIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconI = self.loadImage(KraftIconIURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconIBlocked = self.loadImage(KraftIconIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconII = self.loadImage(KraftIconIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconIIBlocked = self.loadImage(KraftIconIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconIII = self.loadImage(KraftIconIIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconIIIBlocked = self.loadImage(KraftIconIIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconIV = self.loadImage(KraftIconIVURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconIVBlocked = self.loadImage(KraftIconIVBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconV = self.loadImage(KraftIconVURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconVBlocked = self.loadImage(KraftIconVBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconVI = self.loadImage(KraftIconVIURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconVIBlocked = self.loadImage(KraftIconVIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconVII = self.loadImage(KraftIconVIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconVIIBlocked = self.loadImage(KraftIconVIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.KraftIconVIII = self.loadImage(KraftIconVIIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.KraftIconVIIIBlocked = self.loadImage(KraftIconVIIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconI = self.loadImage(WeisheitIconIURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconIBlocked = self.loadImage(WeisheitIconIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconII = self.loadImage(WeisheitIconIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconIIBlocked = self.loadImage(WeisheitIconIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconIII = self.loadImage(WeisheitIconIIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconIIIBlocked = self.loadImage(WeisheitIconIIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconIV = self.loadImage(WeisheitIconIVURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconIVBlocked = self.loadImage(WeisheitIconIVBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconV = self.loadImage(WeisheitIconVURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconVBlocked = self.loadImage(WeisheitIconVBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconVI = self.loadImage(WeisheitIconVIURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconVIBlocked = self.loadImage(WeisheitIconVIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconVII = self.loadImage(WeisheitIconVIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconVIIBlocked = self.loadImage(WeisheitIconVIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.WeisheitIconVIII = self.loadImage(WeisheitIconVIIIURL, size=(TechIconSizeX, TechIconSizeY))
        self.WeisheitIconVIIIBlocked = self.loadImage(WeisheitIconVIIIBlockedURL, size=(TechIconSizeX, TechIconSizeY))

        self.TechBuild = False

        self.PicSchwarzesLoch = self.loadImage(schwarzesLochURL, size=(int(InfoBoxPicY * (1166/1280)), InfoBoxPicY))
        self.PicHauptreihe = self.loadImage(hauptreiheURL, size=(InfoBoxPicX, InfoBoxPicY))
        self.PicRiese = self.loadImage(rieseURL, size=(InfoBoxPicX, InfoBoxPicY))
        self.PicZwerg = self.loadImage(zwergURL, size=(InfoBoxPicX, InfoBoxPicY))
        self.PicNeutronenstern = self.loadImage(neutronensternURL, size=(int(InfoBoxPicY * (357/403)), InfoBoxPicY))
        self.PicGeburt = self.loadImage(geburtURL, size=(int(InfoBoxPicY * (162/200)), InfoBoxPicY))

        self.AttackIcon = self.loadImage(attackIconURL, size=(buttonX, buttonY))
        self.HealIcon = self.loadImage(healIconURL, size=(buttonX, buttonY))
        self.FastForwardIcon = self.loadImage(forwardIconURL, size=(buttonX, buttonY))
        self.BombIcon = self.loadImage(bombIconURL, size=(InfoBoxIconSize, InfoBoxIconSize))
        self.UpgradeIcon = self.loadImage(upgradeIconURL, size=(buttonX, buttonY))

        self.WasAngekommen = False
        self.ConnectionError = False

    def MainMenu(self, error=None):
        self.mainMenu = True
        build = False
        Team1Hover = False
        Team2Hover = False
        inputState = 0
        self.IpGegner = ""
        scroll_y = 0
        flag = 0
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        self.yourIP = s.getsockname()[0]
        s.close()
        while self.mainMenu:
            self.MasterVolume=self.MasterVolumeSliderPos/100
            self.MusicVolume=self.MusicVolumeSliderPos/100
            self.SFXVolume=self.SFXVolumeSliderPos/100
            pygame.mixer.music.set_volume(self.MasterVolume*self.MusicVolume)


            self.gameDisplay.fill(black)
            self.gameDisplay.blit(self.BackgroundPicture, (0,0, display_x, display_y))

            self.LogoSurface = self.gameDisplay.blit(self.Logo, (display_x / 2 - (LogoSize + self.MainFontBig.size(" Nynyezi")[0]) / 2, 95))

            self.MainHeaderText = self.MainFontBig.render(" Nynyezi", True, white)
            self.MainHeaderTextSurface = self.gameDisplay.blit(self.MainHeaderText, (display_x / 2 - (LogoSize + self.MainFontBig.size(" Nynyezi")[0]) / 2 + LogoSize, 100))

            self.InfoIconSurface = self.gameDisplay.blit(self.InfoIcon, (display_x - 10 - InfoIconSize, 10, InfoIconSize, InfoIconSize))
            self.SettingsIconSurface = self.gameDisplay.blit(self.SettingsIcon, (10,10, SettingsIconSize, SettingsIconSize))


            if self.InfoSettings and not self.SettingsOpen and not self.InfoOpen:
                size = self.MainFontMiddle.size("Einstellungen")
                #pygame.draw.rect(self.gameDisplay, white, (display_x - 10 - InfoIconSize - 10 - SettingsIconSize - 10 - size[0] - 5, 10 + SettingsIconSize + 5, size[0] + 10, size[1] + 10))
                SettingsInfoText = self.MainFontMiddle.render("Einstellungen", True, gainsboro)
                self.gameDisplay.blit(SettingsInfoText, (SettingsIconSize + 20, SettingsIconSize + 5))

            if self.InfoInfo and not self.InfoOpen and not self.SettingsOpen:
                size = self.MainFontMiddle.size("Info")
                self.InfoInfoText = self.MainFontMiddle.render("Info", True, white)
                self.gameDisplay.blit(self.InfoInfoText, (display_x - InfoIconSize - 10 - size[0], InfoIconSize + 15))


            rectSizeX = 200
            rectSizeY = 50

            Team1X = 100
            Team1Y = 500
            Team2X = display_x - self.MainFont.size("Team 2")[0] - 100
            Team2Y = 500

            if error != None:
                if error == "Gleiches Team":
                    ErrorText = self.MainFont.render("Nicht das gleiche Team wählen", True, red)
                    ErrorTextSurface = self.gameDisplay.blit(ErrorText, (50, 200))

            RahmenWeissObenLinksKlein = self.loadImage("Pictures/rahmen_weiß_oben_links.png", colorkey=(0,0,0), size=(144,60))
            self.gameDisplay.blit(RahmenWeissObenLinksKlein, (Team1X + 180, Team1Y - 300))

            RahmenWeissObenRechtsKlein = self.loadImage("Pictures/rahmen_weiß_oben_rechts.png", colorkey=(0,0,0), size=(144,60))
            self.gameDisplay.blit(RahmenWeissObenRechtsKlein, (Team2X - 200, Team2Y - 300))

            RahmenWeissUntenLinksKlein = self.loadImage("Pictures/rahmen_weiß_unten_links.png", colorkey=(0,0,0), size=(168,60))
            self.gameDisplay.blit(RahmenWeissUntenLinksKlein, (Team1X + 180, Team1Y))

            RahmenWeissUntenRechtsKlein = self.loadImage("Pictures/rahmen_weiß_unten_rechts.png", colorkey=(0,0,0), size=(168,60))
            self.gameDisplay.blit(RahmenWeissUntenRechtsKlein, (Team2X - 224, Team2Y))

            pygame.draw.rect(self.gameDisplay, white, (Team1X + 180 + 144, Team1Y - 300, 150, 22))
            pygame.draw.line(self.gameDisplay, white, (Team1X + 184, Team1Y - 300 + 60), (Team1X + 184, Team1Y), 2)
            pygame.draw.line(self.gameDisplay, white, (Team2X - 61, Team1Y - 240), (Team2X - 61, Team1Y), 2)
            pygame.draw.line(self.gameDisplay, white, (Team1X + 180 + 168, Team1Y + 51), (Team2X - 224, Team1Y + 51), 2)

            self.FingerPrintIcon = self.loadImage("Pictures/ic_fingerprint_white_48dp_1x.png", size=(48,48))
            self.gameDisplay.blit(self.FingerPrintIcon, (Team2X  - 180, Team2Y - 200))

            #RahmenWeissObenLinksURLSurface = self.gameDisplay.blit(self.RahmenWeissObenLinks, (50, 250, RahmenSizeObenX, RahmenSizeObenY))
            #RahmenWeissObenRechtsSurface = self.gameDisplay.blit(self.RahmenWeissObenRechts, (display_x - 50 - 400, 250, 24, 10))

            YourIp = self.MainFont.render("Deine IP: ", True, white)
            YourIpSurface = self.gameDisplay.blit(YourIp, (Team1X + 150 + 50, 250))
            YourIpString = self.MainFont.render(str(self.yourIP), True, white)
            YourIpStringSurface = self.gameDisplay.blit(YourIpString, (Team1X + 225, 300))

            if inputState == 0:
                GegnerIp = self.MainFont.render("IP des Gegners: ", True, white)
                GegnerIpSurface = self.gameDisplay.blit(GegnerIp, (Team1X  + 200, 400))
                size = self.MainFont.size("25.25.25.25")
                pygame.draw.line(self.gameDisplay, white, (Team1X + 225, 455 + size[1]), (Team1X + 225 + size[0], 455 + size[1]), 3)
            elif inputState == 1:
                GegnerIp = self.MainFont.render("IP des Gegners: ", True, white)
                GegnerIpSurface = self.gameDisplay.blit(GegnerIp, (Team1X + 200, 400))
                GegnerIpString = self.MainFont.render(str(self.IpGegner), True, white)
                GegnerIpStringSurface = self.gameDisplay.blit(GegnerIpString, (Team1X + 225, 450))
                if int(time.time()) != lastTime:
                    lastTime = int(time.time())
                    if flag == 0:
                        flag = 1
                    elif flag == 1:
                        flag = 0
                if flag == 1:
                    pygame.draw.line(self.gameDisplay, white, (Team1X + 225 + self.MainFont.size(str(self.IpGegner))[0], 450), (Team1X + 225 + self.MainFont.size(str(self.IpGegner))[0], 450 + self.MainFont.size("IP")[1]), 3)
            elif inputState == 2:
                GegnerIp = self.MainFont.render("IP des Gegners: ", True, white)
                GegnerIpSurface = self.gameDisplay.blit(GegnerIp, (Team1X + 200, 400))
                GegnerIpString = self.MainFont.render(str(self.IpGegner), True, white)
                GegnerIpStringSurface = self.gameDisplay.blit(GegnerIpString, (Team1X + 225, 450))


            #pygame.draw.line(self.gameDisplay, white, (600 + self.MainFont.size("IP des Gegners: ")[0], 300 + self.MainFont.size("IP des Gegners: ")[1]), (display_x - 100, 300 + self.MainFont.size("IP des Gegners: ")[1]), 3)

            #Team1Button = pygame.Surface((rectSizeX, rectSizeY))
            #Team2Button = pygame.Surface((rectSizeX, rectSizeY))

            #Team1Button.fill(team1_color)
            #Team2Button.fill(team2_color)

            #Team1Text = self.MainFont.render("Team1", True, black)
            #Team2Text = self.MainFont.render("Team2", True, black)
            #Team1TextSurface = Team1Button.blit(Team1Text, (rectSizeX / 2 - self.MainFont.size("Team1")[0] / 2, rectSizeY / 2 - self.MainFont.size("Team1")[1] / 2))
            #Team2TextSurface = Team2Button.blit(Team2Text, (rectSizeX / 2 - self.MainFont.size("Team2")[0] / 2, rectSizeY / 2 - self.MainFont.size("Team2")[1] / 2))

            #Team1ButtonSurface = self.gameDisplay.blit(Team1Button, (Team1X, Team1Y, rectSizeX, rectSizeY))
            #Team2ButtonSurface = self.gameDisplay.blit(Team2Button, (Team2X, Team2Y, rectSizeX, rectSizeY))

            if Team1Hover:
                Team1Text = self.MainFont.render("Team 1", True, (255, 150, 150))
            else:
                Team1Text = self.MainFont.render("Team 1", True, white)

            if Team2Hover:
                Team2Text = self.MainFont.render("Team 2", True, (150, 255, 150))
            else:
                Team2Text = self.MainFont.render("Team 2", True, white)
            Team1ButtonSurface = self.gameDisplay.blit(Team1Text, (Team1X, Team1Y))
            Team2ButtonSurface = self.gameDisplay.blit(Team2Text, (Team2X, Team2Y))
            sizeTeam1 = self.MainFont.size("Team 1")
            sizeTeam2 = self.MainFont.size("Team 2")
            pygame.draw.circle(self.gameDisplay, (255,102,102), (int(Team1X + sizeTeam1[0] / 2), int(Team1Y + sizeTeam1[1] / 2)), int(sizeTeam1[0] / 2) + 10, 2)
            pygame.draw.circle(self.gameDisplay, (102,255,102), (int(Team2X + sizeTeam2[0] / 2), int(Team2Y + sizeTeam2[1] / 2)), int(sizeTeam2[0] / 2) + 10, 2)

            SettingsSizeX = 200
            SettingsSizeY = 300


            if self.SettingsOpen:   #Settings Graphik
                #Begrenzung des Fensters
                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(18, 82), (39, 55), (216, 55), (237, 82), (237, 325), (216, 352), (39, 352), (18, 325)], (255,255,255,50))
                pygame.gfxdraw.polygon(self.gameDisplay, [(18, 82), (39, 55), (216, 55), (237, 82), (237, 325), (216, 352), (39, 352), (18, 325)], (255, 255, 255))

                #Slider MasterVolume
                Text="Gesamtlautstärke"
                self.MasterVolumeSliderText=self.MainFontSmall.render(Text, True, white)
                self.MasterVolumeSliderTextSurface=self.gameDisplay.blit(self.MasterVolumeSliderText, (40,80))
                pygame.draw.line(self.gameDisplay, black, (42, 113), (210, 113), 3)
                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(32, 113), (42, 105), (42, 121)], white80)
                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(210, 105), (220, 113), (210, 121)], white80)
                pygame.draw.circle(self.gameDisplay, white, (round(42 + self.MasterVolumeSliderPos*168/100), 113), self.VolumeSliderSize)

                #slider MusicVolume
                Text="Musiklautstärke"
                self.MusicVolumeSliderText=self.MainFontSmall.render(Text, True, white)
                self.MusicVolumeSliderTextSurface=self.gameDisplay.blit(self.MusicVolumeSliderText, (40,180))
                pygame.draw.line(self.gameDisplay, black, (42, 213), (210, 213), 3)
                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(32, 213), (42, 205), (42, 221)], white80)
                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(210, 205), (220, 213), (210, 221)], white80)
                pygame.draw.circle(self.gameDisplay, white, (round(42 + self.MusicVolumeSliderPos*168/100), 213), self.VolumeSliderSize)

                #slider SFXVolume
                Text="Effektlautstärke"
                self.SFXVolumeSliderText=self.MainFontSmall.render(Text, True, white)
                self.SFXVolumeSliderTextSurface=self.gameDisplay.blit(self.SFXVolumeSliderText, (40,280))
                pygame.draw.line(self.gameDisplay, black, (42, 313), (210, 313), 3)
                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(32, 313), (42, 305), (42, 321)], white80)
                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(210, 305), (220, 313), (210, 321)], white80)
                pygame.draw.circle(self.gameDisplay, white, (round(42 + self.SFXVolumeSliderPos*168/100), 313), self.VolumeSliderSize)


            if self.InfoOpen:

                InfoSurface = pygame.gfxdraw.filled_polygon(self.gameDisplay, [(display_x - 245, 75), (display_x - 224, 55), (display_x - 50, 55), (display_x - 30, 75), (display_x - 30, 325), (display_x - 40, 350), (display_x - 234, 350), (display_x - 244, 325)], (255,255,255,50))
                pygame.gfxdraw.polygon(self.gameDisplay, [(display_x - 247, 75), (display_x - 226, 53), (display_x - 48, 53), (display_x - 28, 75), (display_x - 28, 325), (display_x - 38, 352), (display_x - 236, 352), (display_x - 246, 325)], (255, 255, 255))

                InfoTextArray = ["Herzlich", "Willkommen", "zu", "Nyenyezi.", "Die", "Weiten", "des", "Weltalls", "sind", "aufgeteilt", "in", "verschiedene", "Reiche.", "Als", "ihr", "Anführer",
                                    "wirst", "du", "über", "das", "Schicksal", "immenser", "Gewalten", "bestimmen.", "Treffe", "weise", "Entscheidungen,", "weite", "deinen", "Einflussbereich",
                                    "aus", "oder", "gehe", "unter", "deinen", "Feinden", "zu", "Grunde,", "wenn", "du", "nicht", "vorsichtig", "bist.", "Ab", "jetzt", "entscheidest", "du!",
                                    "                  ", "Bevor", "es", "losgeht", "solltest", "du", "noch", "einige", "Dinge", "wissen.", "Um", "deine", "Feinde", "anzugreifen,", "klicke",
                                    "auf", "einen", "deiner", "Sterne", "und", "Befehle", "ihm", "einen", "Angriff.", "Um zu Forschen", "oder", "neue", "Sterne", "entstehen", "zu", "lassen",
                                    "musst", "du", "über", "genug", "Strahlung", "und", "Metalle", "verfügen.", "Strahlung", "erhälst", "du", "durch", "alle", "deine", "Sterne", "und", "Metalle",
                                    "immer", "dann,", "wenn", "ein", "Stern", "von", "einer", "Brennphase", "in", "die", "nächste", "übergeht.", "Jeder Stern hat", "eine", "bestimmte", "Masse", "und",
                                    "wird", "dementsprechend", "eine", "bestimmte", "Entwicklung", "durchlaufen.", "Experimentiert und", "Entdeckt!", "Erobert", "und", "bezwingt!", "Forscht",
                                    "und", "erweitert", "eure", "Macht!", "Viel Spaß bei", "Nyenyezi!", " "]

                y = 10
                holder = ""
                InfoTextSurface = pygame.surface.Surface((190, 950), pygame.SRCALPHA, 32)
                InfoTextSurface.fill((0,0,0,0))

                for word in InfoTextArray:
                    if self.MainFontSmall.size(holder + " " + word)[0] < 170:
                        holder = holder  + " " + word
                    else:
                        InfoTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                        y += 20
                        #print(holder)
                        holder = word

                InfoTextSurface.blit(self.MainFontSmall.render("Created by: ", True, white), (10, y + 40))
                InfoTextSurface.blit(self.MainFontSmall.render("Max Heuschkel,", True, white), (20, y + 60))
                InfoTextSurface.blit(self.MainFontSmall.render("Jonathan Schleucher,", True, white), (20, y + 80))
                InfoTextSurface.blit(self.MainFontSmall.render("Jonas Kubat", True, white), (20, y + 100))
                InfoTextSurface.blit(self.MainFontSmall.render(str(y + 120), True, white), (10, y + 120))

                HolderSurface = pygame.surface.Surface((190, 230), pygame.SRCALPHA, 32)
                HolderSurface.fill((0,0,0,0))
                HolderSurface.blit(InfoTextSurface, (0, 0 + scroll_y))


                self.gameDisplay.blit(HolderSurface, (display_x - 225, 75))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   #print("Spiel wird geschlossen")
                    self.connectionFlag = False
                    #debugmode
                    #self.s.close()
                    pygame.quit()
                    quit()
                    self.quit = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and build == True:
                    pos = pygame.mouse.get_pos()
                    if Team1ButtonSurface.collidepoint(pos):
                        self.playSFX("Klick", True, 0.8)
                        connectionText = self.MainFontMiddle.render("Warten auf Verbindung...", True, white)
                        connectionTextSurface = self.gameDisplay.blit(connectionText, (50, display_y - 50))
                        pygame.display.update()
                        self.starConnection(1)
                    elif Team2ButtonSurface.collidepoint(pos):
                        self.playSFX("Klick", True, 0.8)
                        connectionText = self.MainFontMiddle.render("Warten auf Verbindung...", True, white)
                        connectionTextSurface = self.gameDisplay.blit(connectionText, (display_x - 300, display_y - 50))
                        pygame.display.update()
                        self.starConnection(2)
                    elif GegnerIpSurface.collidepoint(pos):
                        self.playSFX("Klick", True, 0.8)
                        inputState = 1
                        lastTime = int(time.time())
                    elif pos[0] > Team1X + 225 and pos[0] < Team1X + 225 + self.MainFont.size("25.25.25.25")[0] and pos[1] > 445 and pos[1] < 445 + self.MainFont.size("25")[1]:
                        self.playSFX("Klick", True, 0.8)
                        inputState = 1
                        lastTime = int(time.time())
                    elif self.SettingsIconSurface.collidepoint(pos):
                        self.playSFX("Klick", True, 0.8)
                        if self.SettingsOpen:
                           self.SettingsOpen = False
                        else:
                           self.SettingsOpen = True
                        if self.InfoOpen:
                            self.InfoOpen = False
                    elif self.InfoIconSurface.collidepoint(pos):
                        self.playSFX("Klick", True, 0.8)
                        if self.InfoOpen:
                            self.InfoOpen = False
                        else:
                            self.InfoOpen = True
                        if self.SettingsOpen:
                            self.SettingsOpen = False
                    else:
                        if self.SettingsOpen:
                            #liegt außerhalb
                            if pos[0]<18 or pos[0]>237 or pos[1]<55 or pos[1]>325:
                                self.SettingsOpen=False

                            #liegt auf Master Volume Knopf
                            if pos[0]>42+self.MasterVolumeSliderPos*168/100-self.VolumeSliderSize and pos[0]<42+self.MasterVolumeSliderPos*168/100+self.VolumeSliderSize and pos[1]>113-self.VolumeSliderSize and pos[1]<113+self.VolumeSliderSize:
                                self.MasterVolumeSliderMove=True
                                self.playSFX("Klick", True, 0.8)

                            #liegt auf Music Volume Knopf
                            if pos[0]>42+self.MusicVolumeSliderPos*168/100-self.VolumeSliderSize and pos[0]<42+self.MusicVolumeSliderPos*168/100+self.VolumeSliderSize and pos[1]>213-self.VolumeSliderSize and pos[1]<213+self.VolumeSliderSize:
                                self.MusicVolumeSliderMove=True
                                self.playSFX("Klick", True, 0.8)

                            #liegt auf SFX Volume Knopf
                            if pos[0]>42+self.SFXVolumeSliderPos*168/100-self.VolumeSliderSize and pos[0]<42+self.SFXVolumeSliderPos*168/100+self.VolumeSliderSize and pos[1]>313-self.VolumeSliderSize and pos[1]<313+self.VolumeSliderSize:
                                self.SFXVolumeSliderMove=True
                                self.playSFX("Klick", True, 0.8)

                        elif self.InfoOpen:
                            self.InfoOpen = False

                elif event.type == pygame.MOUSEBUTTONDOWN and self.InfoOpen:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > display_x - 225 and pos[0] < display_x - 30 and pos[1] > 75 and pos[1] < 275:
                        if event.button == 4: scroll_y = min(scroll_y + 15, 0)
                        if event.button == 5: scroll_y = max(scroll_y - 15, -950)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        self.IpGegner = self.IpGegner + "0"
                    elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        self.IpGegner = self.IpGegner + "1"
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        self.IpGegner = self.IpGegner + "2"
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        self.IpGegner = self.IpGegner + "3"
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        self.IpGegner = self.IpGegner + "4"
                    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        self.IpGegner = self.IpGegner + "5"
                    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        self.IpGegner = self.IpGegner + "6"
                    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        self.IpGegner = self.IpGegner + "7"
                    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        self.IpGegner = self.IpGegner + "8"
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        self.IpGegner = self.IpGegner + "9"
                    elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                        self.IpGegner = self.IpGegner + "."
                    elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        inputState = 2
                    elif event.key == pygame.K_BACKSPACE:
                        if self.IpGegner != "":
                            self.IpGegner = self.IpGegner[:-1]

                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if self.SettingsIconSurface.collidepoint(pos):
                        self.InfoSettings = True
                        if self.InfoInfo:
                            self.InfoInfo = False
                    elif self.InfoIconSurface.collidepoint(pos):
                        self.InfoInfo = True
                        if self.InfoSettings:
                            self.InfoSettings = False
                    elif Team1ButtonSurface.collidepoint(pos):
                        Team1Hover = True
                    elif Team2ButtonSurface.collidepoint(pos):
                        Team2Hover = True

                    else:
                        if self.InfoSettings:
                            self.InfoSettings = False
                        elif Team1Hover:
                            Team1Hover = False
                        elif Team2Hover:
                            Team2Hover = False
                        if self.InfoInfo:
                            self.InfoInfo = False

                    #Slider MasterVolume
                    if self.MasterVolumeSliderMove==True:
                        if pos[0]>=210:
                            self.MasterVolumeSliderPos=100
                        elif pos[0]<=42:
                            self.MasterVolumeSliderPos=0
                        else:
                            self.MasterVolumeSliderPos=(pos[0]-42)*100/168

                    #Slider MusicVolume
                    if self.MusicVolumeSliderMove==True:
                        if pos[0]>=210:
                            self.MusicVolumeSliderPos=100
                        elif pos[0]<=42:
                            self.MusicVolumeSliderPos=0
                        else:
                            self.MusicVolumeSliderPos=(pos[0]-42)*100/168

                    #Slider MusicVolume
                    if self.SFXVolumeSliderMove==True:
                        if pos[0]>=210:
                            self.SFXVolumeSliderPos=100
                        elif pos[0]<=42:
                            self.SFXVolumeSliderPos=0
                        else:
                            self.SFXVolumeSliderPos=(pos[0]-42)*100/168



                if event.type == pygame.MOUSEBUTTONUP:
                    self.MasterVolumeSliderMove=False
                    self.MusicVolumeSliderMove=False
                    self.SFXVolumeSliderMove=False
                #if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.NewStarSlide == True:
                #    pass

            pygame.display.update()
            self.dt = self.clock.tick(FPS) #Delay für FPS anzahl

            build = True

        self.connectionFlag = False
        print("Spiel wird geschlossen")
        pygame.quit()
        quit()

    def starConnection(self, team):
        if team == 1:
            self.host = self.yourIP
            self.port = 6667
            self.gegnerHost = self.IpGegner
            self.gegnerPort = 6668
        elif team == 2:
            self.host = self.yourIP
            self.port = 6668
            self.gegnerHost = self.IpGegner
            self.gegnerPort = 6667


        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host, self.port))    #Meine Adresse

       #print("Connection für Multiplayer wird gestartet")

        nachricht = "SpielStart" + str(team)
        self.s.sendto(nachricht.encode('utf-8'), (self.gegnerHost, self.gegnerPort))
        sendThread = Thread(target=self.sendStartMessage, args=(team,))
        self.sendStartMessageFlag = True
        sendThread.start()
        while True:
            data, addr = self.s.recvfrom(2048)
            if addr == (self.gegnerHost, self.gegnerPort):
                #print("Naricht von Gegner: ", data.decode('utf-8'))
                nachricht = "SpielStart" + str(team)
                self.s.sendto(nachricht.encode('utf-8'), (self.gegnerHost, self.gegnerPort))
                if team == 1:
                    if data.decode('utf-8') == "SpielStart2":
                        self.sendStartMessageFlag = False
                        self.startGame(1)
                    elif data.decode('utf-8') == "SpielStart1":
                        self.sendStartMessageFlag = False
                        self.MainMenu(error="Gleiches Team")
                elif team == 2:
                    if data.decode('utf-8') == "SpielStart1":
                        self.sendStartMessageFlag = False
                        self.startGame(2)
                    elif data.decode('utf-8') == "SpielStart2":
                        self.sendStartMessageFlag = False
                        self.MainMenu(error="Gleiches Team")


        data, addr = self.s.recvfrom(1024)
        #print("data: ", data)
        #print("addr: ", addr)

        self.s.sendto(data, addr)    #adresse anderes team


    def sendStartMessage(self, team):
        oldTime = int(time.time())
        nachricht = "SpielStart" + str(team)
        nachricht = nachricht.encode('utf-8')
        while self.sendStartMessageFlag:
            if oldTime != int(time.time()):
                oldTime = int(time.time())
                self.s.sendto(nachricht, (self.gegnerHost, self.gegnerPort))

    def Connection(self):
        while self.connectionFlag:
            data, addr = self.s.recvfrom(4096)
            #print("Received Message from", str(addr))
            if addr == (self.gegnerHost, self.gegnerPort):
                data = data.decode('utf-8')
                #print("Raw Data: ----------------")
                #print(data)
                if data != "SpielStart1" and data != "SpielStart2":

                    data = json.loads(data)
                    #print("Data: -----------------")
                    #print(data)
                    if data["action"] == "starArrayTeam1":
                        self.starArrayTeam1 = data["data"]
                       #print("starArrayTeam1 wurde angepasst")

                    elif data["action"] == "starArrayTeam2":
                        self.starArrayTeam2 = data["data"]
                       #print("starArrayTeam2 wurde angepasst")

                    elif data["action"] == "starArraySpecial":
                        self.starArraySpecial = data["data"]
                        #print("starArraySpecial wurde angepasst")

                    elif data["action"] == "OngoingAttacksMods":
                        self.OngoingAttacksMods = data["data"]

                    elif data["action"] == "techArray":
                        if self.yourTeam == "Team1":
                            self.techArrayTeam2 = data["data"]
                        else:
                            self.techArrayTeam1 = data["data"]
                        #print("techArrayTeam1 wurde angepasst")

                    elif data["action"] == "binNochDa": #bekommt Team1
                        self.WasAngekommen = True

                    elif data["action"] == "bistDuNochDa":  #bekommt Team2
                        message = '{"action": "binNochDa", "data": "Filler"}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        self.WasAngekommen = True

                    elif data["action"] == "NewAttack":
                        self.Attacks.append(data["data"])

                    #Attacks = [{"Angreifer": "test", "Verteidiger": "test2", "SchadenAng": 200, "SchadenVer": 10}, {...}]
                    elif data["action"] == "Schaden":   #{"action": "Schaden", "data": {"schaden": -100, "stern": "test", "von": "test2"}}
                        Schaden = data["data"]["schaden"]   #Positiver bereich -> Schaden, Negativer Bereich -> Heilen
                        Stern = data["data"]["stern"]
                        Von = data["data"]["von"]
                        if self.yourTeam == "Team1":
                            for star in self.starArrayTeam1:
                                if star["name"] == Stern:
                                    star["health"] -= Schaden
                                    if Schaden > 0:
                                        for angriff in self.Attacks:
                                            if angriff["Angreifer"] == Stern and angriff["Verteidiger"] == Von:
                                                angriff["SchadenVer"] = Schaden
                                                break
                                            elif angriff["Angreifer"] == Von and angriff["Verteidiger"] == Stern:
                                                angriff["SchadenAng"] = Schaden
                                                break
                                    if star["health"] <= 0:
                                        self.starCaptured(Stern, Von, "Gegner")
                        elif self.yourTeam == "Team2":
                            for star in self.starArrayTeam2:
                                if star["name"] == Stern:
                                    star["health"] -= Schaden
                                    if Schaden > 0:
                                        for angriff in self.Attacks:
                                            if angriff["Angreifer"] == Stern and angriff["Verteidiger"] == Von:
                                                angriff["SchadenVer"] = Schaden
                                                break
                                            elif angriff["Angreifer"] == Von and angriff["Verteidiger"] == Stern:
                                                angriff["SchadenAng"] = Schaden
                                                break
                                    if star["health"] <= 0:
                                        self.starCaptured(Stern, Von, "Gegner")

                    else:
                        pass
                       #print("_-_----------Data-Action nicht gefunden-------------------")


    def startGame(self, team):
        #debugMode
        self.connectionFlag = True
        self.ConnectionThread = Thread(target=self.Connection, args=())
        self.ConnectionThread.start()

        self.cheat = 0

        if team == 1:
            self.yourTeam = "Team1"

            q = 0
            #Generieren der StartSterne Team 1
            i = 0
            while i < AnzahlStartSterne:
                cord_x, cord_y = self.generateLocation(self.starArrayTeam1, "Team1")
                starHealth = starMassTeam1[i] * 300 #HealthFormel [für Suche]
                pygame.draw.circle(self.gameDisplay, team1_color, [cord_x, cord_y], star_size)
                if starCatTeam1[i] == "Hauptreihe":
                    nextLevel = 2 * 1/(starMassTeam1[i]+1)**0.5*60/0.1  #TimeFormel [für Suche]
                else:
                    nextLevel = 1/(starMassTeam1[i]+1)**0.5*60/0.1    #TimeFormel [für Suche]
                self.starArrayTeam1.append({"name": starNameTeam1[i],
                                            "cord_x": cord_x,
                                            "cord_y": cord_y,
                                            "mass": starMassTeam1[i],
                                            "age": starAgeTeam1[i],
                                            "cat": starCatTeam1[i],
                                            "inAttack": False,
                                            "team": 1,
                                            "health": starHealth,
                                            "nextLevel": nextLevel})
                i += 1

            #Generieren der StartSterne Team 2
            i = 0
            while i < AnzahlStartSterne:
                cord_x, cord_y = self.generateLocation(self.starArrayTeam2, "Team2")
                starHealth = starMassTeam2[i] * 300  #HealthFormel [für Suche]
                pygame.draw.circle(self.gameDisplay, team2_color, [cord_x, cord_y], star_size)
                if starCatTeam2[i] == "Hauptreihe":
                    nextLevel = 2 * 1/(starMassTeam2[i]+1)**0.5*60/0.1  #TimeFormel [für Suche]
                else:
                    nextLevel = 1/(starMassTeam2[i]+1)**0.5*60/0.1    #TimeFormel [für Suche]
                self.starArrayTeam2.append({"name": starNameTeam2[i],
                                            "cord_x": cord_x,
                                            "cord_y": cord_y,
                                            "mass": starMassTeam2[i],
                                            "age": starAgeTeam2[i],
                                            "cat": starCatTeam2[i],
                                            "inAttack": False,
                                            "team": 2,
                                            "health": starHealth,
                                            "nextLevel": nextLevel})
                i += 1

            #Generieren der SpecialSterne
            i = 0
            while i < 3:
                cord_x, cord_y = self.generateLocation(self.starArraySpecial, "Special")
                pygame.draw.circle(self.gameDisplay, special_color, [cord_x, cord_y], star_size)
                self.starArraySpecial.append({"name": specialStarName[i],
                                                "cord_x": cord_x,
                                                "cord_y": cord_y,
                                                "mass": specialStarMass[i],
                                                "cat": specialStarCat[i],
                                                "inAttack": False,
                                                "team": 0,
                                                "age": specialStarAge[i]})
                i += 1

            #debugMode
            pygame.display.update()
            message = '{"action": "starArrayTeam1", "data": ' + json.dumps(self.starArrayTeam1) + '}'
            message = message.encode('utf-8')
            self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
            v = '{"action": "starArraySpecial", "data": ' + json.dumps(self.starArraySpecial) + '}'
            v = v.encode('utf-8')
            self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
            message = '{"action": "starArrayTeam2", "data": ' + json.dumps(self.starArrayTeam2) + '}'
            message = message.encode('utf-8')
            self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
            self.GameLoop()
        else:
            self.yourTeam = "Team2"
            while self.starArrayTeam1 == [] and self.starArrayTeam2 == []:
                time.sleep(1)
            self.GameLoop()

    def GameLoop(self):
        healErrorStrahlung = False
        InfoFlag = False
        scroll_y = 0

        while not self.gameExit and not self.quit:
            if self.gameover == True:
                summe = 0
                for star in self.starArrayTeam1:
                    summe+=1
                for star in self.starArrayTeam2:
                    summe+=-1
                if self.yourTeam == "Team1":
                    if summe >= 0:
                        self.drawEvent("gameoverwon")
                    else:
                        self.drawEvent("gameoverlost")
                else:
                    if summe<=0:
                        self.drawEvent("gameoverwon")
                    else:
                        self.drawEvent("gameoverlost")


            for timer in self.timer:
                timer["time"]+= -1/FPS
                if timer["time"]<=0:
                    if timer['ongoingeffect']!='perpetual':
                        self.timer.remove(timer)
                    exec(timer['effect'])
                try:
                    exec(timer["ongoingeffect"])
                except:
                    pass

            for value in self.OngoingAttacksMods:
                if value["time"] > 0:
                    value["time"]+=-1/FPS
                elif value["time"] < 0:
                    value["time"] = 0


            self.MasterVolume=self.MasterVolumeSliderPos/100
            self.MusicVolume=self.MusicVolumeSliderPos/100
            self.SFXVolume=self.SFXVolumeSliderPos/100
            pygame.mixer.music.set_volume(self.MasterVolume*self.MusicVolume)

            if (self.ersterNeutronenstern!=None) and not self.ersterNeutronensternflag:
                self.drawEvent("ladungfürAnfänger", star=self.ersterNeutronenstern)
                self.ersterNeutronenstern = None
                self.ersterNeutronensternflag = True
            if (self.ersterRiese!=None) and not self.ersterRieseflag:
                self.drawEvent("großeLeuchte", star= self.ersterRiese)
                self.ersterRiese = None
                self.ersterRieseflag = True
            if (self.erstesSchwarzesLoch!=None) and not self.erstesSchwarzesLochflag:
                self.drawEvent("großerStaubsauger", star=self.erstesSchwarzesLoch)
                self.erstesSchwarzesLoch = None
                self.erstesSchwarzesLochflag = True

            for star in self.starArrayHostileTeam1:
                if not star['inAttack']:
                    beststar = []
                    bestdist = 100000
                    for choosestar in self.starArrayTeam1:
                        if (abs(star['cord_x']-choosestar['cord_x'])**2+abs(star['cord_y']-choosestar['cord_y'])**2)**0.5<bestdist:
                            beststar = choosestar
                            bestdist = (abs(star['cord_x']-choosestar['cord_x'])**2+abs(star['cord_y']-choosestar['cord_y'])**2)**0.5
                    self.starAttack(beststar, star)

            for star in self.starArrayHostileTeam2:
                if not star['inAttack']:
                    beststar = []
                    bestdist = 1000000
                    for choosestar in self.starArrayTeam2:
                        if (abs(star['cord_x']-choosestar['cord_x'])**2+abs(star['cord_y']-choosestar['cord_y'])**2)**0.5<bestdist:
                            beststar = choosestar
                            bestdist = (abs(star['cord_x']-choosestar['cord_x'])**2+abs(star['cord_y']-choosestar['cord_y'])**2)**0.5
                    self.starAttack(beststar, star)

            if self.TechOpen == True:

                self.gameDisplay.fill(white)

                disp=round(display_x/3)

                if self.TechInfoOpen and (self.TechInfoString in ["PerfektionI", "PerfektionII", "PerfektionIII", "PerfektionIV", "PerfektionV", "PerfektionVI", "PerfektionVII", "PerfektionVIII"]):
                    self.PerfektionBackgroundSurface = self.gameDisplay.blit(self.PerfektionBackgroundColor, (0,0))

                    self.KraftBackgroundSurface = self.gameDisplay.blit(self.KraftBackgroundBlack, (disp,0))
                    self.WeisheitBackgroundSurface = self.gameDisplay.blit(self.WeisheitBackgroundBlack, (disp*2, 0))


                elif self.TechInfoOpen and (self.TechInfoString in ["WeisheitI", "WeisheitII", "WeisheitIII", "WeisheitIV", "WeisheitV", "WeisheitVI", "WeisheitVII", "WeisheitVIII"]):
                    self.WeisheitBackgroundSurface = self.gameDisplay.blit(self.WeisheitBackgroundColor, (disp*2, 0))

                    self.KraftBackgroundSurface = self.gameDisplay.blit(self.KraftBackgroundBlack, (disp,0))
                    self.PerfektionBackgroundSurface = self.gameDisplay.blit(self.PerfektionBackgroundBlack, (0,0))



                elif self.TechInfoOpen and self.TechInfoString in ["KraftI", "KraftII", "KraftIII", "KraftIV", "KraftV", "KraftVI", "KraftVII", "KraftVIII"]:
                    self.KraftBackgroundSurface = self.gameDisplay.blit(self.KraftBackgroundColor, (disp, 0))

                    self.PerfektionBackgroundSurface = self.gameDisplay.blit(self.PerfektionBackgroundBlack, (0,0))
                    self.WeisheitBackgroundSurface = self.gameDisplay.blit(self.WeisheitBackgroundBlack, (disp*2, 0))

                elif pygame.mouse.get_pos()[0]<=disp:
                    self.PerfektionBackgroundSurface = self.gameDisplay.blit(self.PerfektionBackgroundColor, (0,0))

                    self.KraftBackgroundSurface = self.gameDisplay.blit(self.KraftBackgroundBlack, (disp,0))
                    self.WeisheitBackgroundSurface = self.gameDisplay.blit(self.WeisheitBackgroundBlack, (disp*2, 0))

                elif pygame.mouse.get_pos()[0]<=disp*2 and pygame.mouse.get_pos()[0]>disp:
                    self.KraftBackgroundSurface = self.gameDisplay.blit(self.KraftBackgroundColor, (disp, 0))

                    self.PerfektionBackgroundSurface = self.gameDisplay.blit(self.PerfektionBackgroundBlack, (0,0))
                    self.WeisheitBackgroundSurface = self.gameDisplay.blit(self.WeisheitBackgroundBlack, (disp*2, 0))


                elif pygame.mouse.get_pos()[0]>disp*2:
                    self.WeisheitBackgroundSurface = self.gameDisplay.blit(self.WeisheitBackgroundColor, (disp*2, 0))

                    self.KraftBackgroundSurface = self.gameDisplay.blit(self.KraftBackgroundBlack, (disp,0))
                    self.PerfektionBackgroundSurface = self.gameDisplay.blit(self.PerfektionBackgroundBlack, (0,0))



                if self.yourTeam == "Team1":
                    strahlung = self.strahlungTeam1
                    metalle = self.metalleTeam1
                else:
                    strahlung = self.strahlungTeam2
                    metalle = self.metalleTeam2


                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(display_x, 0), (display_x, 50), (480, 50), (428, 0)], (0,0,0))


                MetallIconSurface = self.gameDisplay.blit(self.MetallIcon, (500, 5))
                StrahlungIconSurface = self.gameDisplay.blit(self.StrahlungIcon, (750, 5))

                self.StrahlungText = self.MainFontMiddle.render(str(round(strahlung/1000000, 1)) + " Mio.", True, StrahlungTextColor)
                self.StrahlungTextSurface = self.gameDisplay.blit(self.StrahlungText, (800, 15))

                self.MetallText = self.MainFontMiddle.render(str(int(metalle)), True, MetallTextColor)
                self.MetallTextSurface = self.gameDisplay.blit(self.MetallText, (550, 15))

                pygame.draw.line(self.gameDisplay, black, (display_x, 50), (480, 50), 2)
                pygame.draw.line(self.gameDisplay, black, (428, 0), (488, 60), 3)




                self.TechCloseIconSurface = self.gameDisplay.blit(self.TechCloseIcon, (spaceTechCloseIcon, spaceTechCloseIcon))

                self.TechSubHeaderTextPerfektion = self.MainFont.render("Perfektion", True, TechSubHeaderTextPerfektionColor)
                self.TechSubHeaderTextPerfektionSurface = self.gameDisplay.blit(self.TechSubHeaderTextPerfektion, (TechSubHeaderTextPerfektionX, TechSubHeaderTextPerfektionY))

                self.TechSubHeaderTextKraft = self.MainFont.render("Kraft", True, TechSubHeaderTextKraftColor)
                self.TechSubHeaderTextKraftSurface = self.gameDisplay.blit(self.TechSubHeaderTextKraft, (TechSubHeaderTextKraftX, TechSubHeaderTextKraftY))

                self.TechSubHeaderTextWeisheit = self.MainFont.render("Weisheit", True, TechSubHeaderTextWeisheitColor)
                self.TechSubHeaderTextWeisheitSurface = self.gameDisplay.blit(self.TechSubHeaderTextWeisheit, (TechSubHeaderTextWeisheitX, TechSubHeaderTextWeisheitY))

                pygame.draw.line(self.gameDisplay, black, (100, TechSubHeaderTextPerfektionY + fontSize), (display_x - 100, TechSubHeaderTextWeisheitY + fontSize), 1)

                if self.yourTeam == "Team1":
                    techArray = self.techArrayTeam1
                else:
                    techArray = self.techArrayTeam2
                if techArray["Perfektion"][0] == True:
                    self.PerfektionIconISurface = self.gameDisplay.blit(self.PerfektionIconI, (PerfektionIconI_X, PerfektionIconI_Y))
                    if techArray["Perfektion"][1] == True:
                        self.PerfektionIconIISurface = self.gameDisplay.blit(self.PerfektionIconII, (PerfektionIconII_X, PerfektionIconII_Y))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconI_X + TechIconSizeX / 2, PerfektionIconI_Y + TechIconSizeY), (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + TechIconSizeY + PerfektionIconI_Y), (PerfektionIconII_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconII_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY), (PerfektionIconII_X + TechIconSizeX / 2, PerfektionIconII_Y))
                        self.PerfektionIconIVSurface = self.gameDisplay.blit(self.PerfektionIconIVBlocked, (PerfektionIconIV_X, PerfektionIconIV_Y))
                        if not techArray["Perfektion"][3]:
                            loccolor = violet
                        else:
                            loccolor = black
                        pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconII_X + TechIconSizeX / 2, PerfektionIconII_Y + TechIconSizeY), (PerfektionIconII_X + TechIconSizeX / 2, PerfektionIconII_Y + TechIconSizeY + (PerfektionIconIV_Y - PerfektionIconII_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconII_X + TechIconSizeX / 2, PerfektionIconII_Y + TechIconSizeY + (PerfektionIconIV_Y - PerfektionIconII_Y - TechIconSizeY) / 2), (PerfektionIconIV_X + TechIconSizeX / 2, PerfektionIconIV_Y - (PerfektionIconIV_Y - PerfektionIconII_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconIV_X + TechIconSizeX / 2, PerfektionIconIV_Y - (PerfektionIconIV_Y - PerfektionIconII_Y - TechIconSizeY) / 2), (PerfektionIconIV_X + TechIconSizeX / 2, PerfektionIconIV_Y))
                        if techArray["Perfektion"][3] == True:
                            self.PerfektionIconVSurface = self.gameDisplay.blit(self.PerfektionIconVBlocked, (PerfektionIconV_X, PerfektionIconV_Y))
                            pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconIV_X + TechIconSizeX/2, PerfektionIconIV_Y + TechIconSizeY), (PerfektionIconV_X + TechIconSizeX / 2, PerfektionIconV_Y))
                            if techArray["Perfektion"][4] == True:
                                self.PerfektionIconVSurface = self.gameDisplay.blit(self.PerfektionIconV, (PerfektionIconV_X, PerfektionIconV_Y))
                    elif techArray["Perfektion"][2] == True:
                        self.PerfektionIconIIISurface = self.gameDisplay.blit(self.PerfektionIconIII, (PerfektionIconIII_X, PerfektionIconIII_Y))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconI_X + TechIconSizeX / 2, PerfektionIconI_Y + TechIconSizeY), (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY), (PerfektionIconIII_X + TechIconSizeX / 2 , (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconIII_X + TechIconSizeX / 2 , (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY), (PerfektionIconIII_X + TechIconSizeX / 2, PerfektionIconIII_Y))
                        loccolor = black
                        if techArray["Perfektion"][3] == False:
                            loccolor = violet
                            self.PerfektionIconIVSurface = self.gameDisplay.blit(self.PerfektionIconIVBlocked, (PerfektionIconIV_X, PerfektionIconIV_Y))
                        pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconIII_X + TechIconSizeX / 2, PerfektionIconIII_Y + TechIconSizeY), (PerfektionIconIII_X + TechIconSizeX / 2, PerfektionIconIII_Y + TechIconSizeY + (PerfektionIconIV_Y - PerfektionIconIII_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconIII_X + TechIconSizeX / 2, PerfektionIconIII_Y + TechIconSizeY + (PerfektionIconIV_Y - PerfektionIconIII_Y - TechIconSizeY) / 2), (PerfektionIconIV_X + TechIconSizeX / 2, PerfektionIconIV_Y - (PerfektionIconIV_Y - PerfektionIconIII_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconIV_X + TechIconSizeX / 2, PerfektionIconIV_Y - (PerfektionIconIV_Y - PerfektionIconIII_Y - TechIconSizeY) / 2), (PerfektionIconIV_X + TechIconSizeX / 2, PerfektionIconIV_Y))
                        if techArray["Perfektion"][3] == True:
                            self.PerfektionIconIVSurface = self.gameDisplay.blit(self.PerfektionIconIV, (PerfektionIconIV_X, PerfektionIconIV_Y))
                            loccolor = black
                            if techArray["Perfektion"][4] == False:
                                loccolor = violet
                                self.PerfektionIconVSurface = self.gameDisplay.blit(self.PerfektionIconVBlocked, (PerfektionIconV_X, PerfektionIconV_Y))
                            pygame.draw.line(self.gameDisplay, loccolor, (PerfektionIconIV_X + TechIconSizeX/2, PerfektionIconIV_Y + TechIconSizeY), (PerfektionIconV_X + TechIconSizeX / 2, PerfektionIconV_Y))
                            if techArray["Perfektion"][4] == True:
                                self.PerfektionIconVSurface = self.gameDisplay.blit(self.PerfektionIconV, (PerfektionIconV_X, PerfektionIconV_Y))
                    else:
                        self.PerfektionIconIISurface = self.gameDisplay.blit(self.PerfektionIconIIBlocked, (PerfektionIconII_X, PerfektionIconII_Y))
                        self.PerfektionIconIIISurface = self.gameDisplay.blit(self.PerfektionIconIIIBlocked, (PerfektionIconIII_X, PerfektionIconIII_Y))
                        pygame.gfxdraw.filled_polygon(self.gameDisplay, [((PerfektionIconII_X+TechIconSizeX+PerfektionIconIII_X)/2-20, PerfektionIconII_Y+TechIconSizeY/2), ((PerfektionIconII_X+TechIconSizeX+PerfektionIconIII_X)/2-10, PerfektionIconII_Y+TechIconSizeY/2+10), ((PerfektionIconII_X+TechIconSizeX+PerfektionIconIII_X)/2-10, PerfektionIconII_Y+TechIconSizeY/2-10)], violet)
                        pygame.gfxdraw.filled_polygon(self.gameDisplay, [((PerfektionIconII_X+TechIconSizeX+PerfektionIconIII_X)/2+20, PerfektionIconII_Y+TechIconSizeY/2), ((PerfektionIconII_X+TechIconSizeX+PerfektionIconIII_X)/2+10, PerfektionIconII_Y+TechIconSizeY/2+10), ((PerfektionIconII_X+TechIconSizeX+PerfektionIconIII_X)/2+10, PerfektionIconII_Y+TechIconSizeY/2-10)], violet)
                        self.gameDisplay.blit(self.MainFontBig.render("!", True, red), ((PerfektionIconII_X+TechIconSizeX+PerfektionIconIII_X)/2-4, PerfektionIconII_Y+TechIconSizeY/2-20))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconI_X + TechIconSizeX / 2, PerfektionIconI_Y + TechIconSizeY), (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + TechIconSizeY + PerfektionIconI_Y), (PerfektionIconII_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconII_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY), (PerfektionIconII_X + TechIconSizeX / 2, PerfektionIconII_Y))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconI_X + TechIconSizeX / 2, PerfektionIconI_Y + TechIconSizeY), (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconI_X + TechIconSizeX / 2, (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY), (PerfektionIconIII_X + TechIconSizeX / 2 , (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconIII_X + TechIconSizeX / 2 , (PerfektionIconII_Y - (PerfektionIconI_Y + TechIconSizeY)) / 2 + PerfektionIconI_Y + TechIconSizeY), (PerfektionIconIII_X + TechIconSizeX / 2, PerfektionIconIII_Y))
                else:
                    self.PerfektionIconISurface = self.gameDisplay.blit(self.PerfektionIconIBlocked, (PerfektionIconI_X, PerfektionIconI_Y))

                if techArray["Perfektion"][5] == True:
                    self.PerfektionIconVISurface = self.gameDisplay.blit(self.PerfektionIconVI, (PerfektionIconVI_X, PerfektionIconVI_Y))
                    if techArray["Perfektion"][6] == True:
                        self.PerfektionIconVIISurface = self.gameDisplay.blit(self.PerfektionIconVII, (PerfektionIconVII_X, PerfektionIconVII_Y))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY), (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY + (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVII_Y - (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVII_X + TechIconSizeX / 2, PerfektionIconVII_Y - (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconVII_X + TechIconSizeX / 2, PerfektionIconVII_Y - (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVII_X + TechIconSizeX / 2, PerfektionIconVII_Y))
                    elif techArray["Perfektion"][7] == True:
                        self.PerfektionIconVIIISurface = self.gameDisplay.blit(self.PerfektionIconVIII, (PerfektionIconVIII_X, PerfektionIconVIII_Y))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY), (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY + (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVIII_Y - (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVIII_X + TechIconSizeX / 2, PerfektionIconVIII_Y - (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, black, (PerfektionIconVIII_X + TechIconSizeX / 2, PerfektionIconVIII_Y - (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVIII_X + TechIconSizeX / 2, PerfektionIconVIII_Y))
                    else:
                        self.PerfektionIconVIISurface = self.gameDisplay.blit(self.PerfektionIconVIIBlocked, (PerfektionIconVII_X, PerfektionIconVII_Y))
                        self.PerfektionIconVIIISurface = self.gameDisplay.blit(self.PerfektionIconVIIIBlocked, (PerfektionIconVIII_X, PerfektionIconVIII_Y))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY), (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY + (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVII_Y - (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVII_X + TechIconSizeX / 2, PerfektionIconVII_Y - (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconVII_X + TechIconSizeX / 2, PerfektionIconVII_Y - (PerfektionIconVII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVII_X + TechIconSizeX / 2, PerfektionIconVII_Y))
                        #pygame.draw.line(self.gameDisplay, black, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY), (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVI_Y + TechIconSizeY + (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconVI_X + TechIconSizeX / 2, PerfektionIconVIII_Y - (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVIII_X + TechIconSizeX / 2, PerfektionIconVIII_Y - (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, violet, (PerfektionIconVIII_X + TechIconSizeX / 2, PerfektionIconVIII_Y - (PerfektionIconVIII_Y - PerfektionIconVI_Y - TechIconSizeY) / 2), (PerfektionIconVIII_X + TechIconSizeX / 2, PerfektionIconVIII_Y))
                else:
                    self.PerfektionIconVISurface = self.gameDisplay.blit(self.PerfektionIconVIBlocked, (PerfektionIconVI_X, PerfektionIconVI_Y))

                if techArray["Kraft"][0] == True:
                    self.KraftIconISurface = self.gameDisplay.blit(self.KraftIconI, (KraftIconI_X, KraftIconI_Y))
                    if techArray["Kraft"][1] == False:
                        loccolor = violet
                    else:
                        loccolor = black
                    pygame.draw.line(self.gameDisplay, loccolor, (KraftIconI_X + TechIconSizeX / 2, KraftIconI_Y + TechIconSizeY), (KraftIconII_X + TechIconSizeX / 2, KraftIconII_Y))
                    if techArray["Kraft"][1] == True:
                        self.KraftIconIISurface = self.gameDisplay.blit(self.KraftIconII, (KraftIconII_X, KraftIconII_Y))
                        if techArray["Kraft"][3] == False and techArray["Kraft"][2] == False and techArray["Kraft"][4] == False:
                            loccolor = violet
                        else:
                            loccolor = black
                        pygame.draw.line(self.gameDisplay, loccolor, (KraftIconII_X + TechIconSizeX / 2, KraftIconII_Y + TechIconSizeY), (KraftIconIV_X + TechIconSizeX / 2, (KraftIconII_Y+KraftIconIV_Y+TechIconSizeY)/2))
                        if techArray["Kraft"][3] == False:
                            loccolor = violet
                        else:
                            loccolor = black
                        pygame.draw.line(self.gameDisplay, loccolor, (KraftIconIV_X + TechIconSizeX / 2, (KraftIconII_Y+KraftIconIV_Y)/2+TechIconSizeY/2), (KraftIconIV_X + TechIconSizeX / 2, KraftIconIV_Y))
                        if techArray["Kraft"][2] == False:
                            loccolor = violet
                        else:
                            loccolor = black
                        pygame.draw.line(self.gameDisplay, loccolor, (KraftIconII_X + TechIconSizeX / 2, KraftIconII_Y + TechIconSizeY + (KraftIconIII_Y - KraftIconII_Y - TechIconSizeY) / 2), (KraftIconIII_X + TechIconSizeX / 2, KraftIconII_Y + TechIconSizeY + (KraftIconIII_Y - KraftIconII_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, loccolor, (KraftIconIII_X + TechIconSizeX / 2, KraftIconII_Y + TechIconSizeY + (KraftIconIII_Y - KraftIconII_Y - TechIconSizeY) / 2), (KraftIconIII_X + TechIconSizeX / 2, KraftIconIII_Y))
                        if techArray["Kraft"][4] == False:
                            loccolor = violet
                        else:
                            loccolor = black
                        pygame.draw.line(self.gameDisplay, loccolor, (KraftIconII_X + TechIconSizeX / 2, KraftIconII_Y + TechIconSizeY + (KraftIconV_Y - KraftIconII_Y - TechIconSizeY) / 2), (KraftIconV_X + TechIconSizeX / 2, KraftIconII_Y + TechIconSizeY + (KraftIconV_Y - KraftIconII_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, loccolor, (KraftIconV_X + TechIconSizeX / 2, KraftIconII_Y + TechIconSizeY + (KraftIconV_Y - KraftIconII_Y - TechIconSizeY) / 2), (KraftIconV_X + TechIconSizeX / 2, KraftIconV_Y))
                        if techArray["Kraft"][5]:
                            loccolor = black
                        else:
                            loccolor = violet
                        if techArray["Kraft"][2] or techArray["Kraft"][3] or techArray["Kraft"][4]:
                            pygame.draw.line(self.gameDisplay, loccolor, (KraftIconVI_X + TechIconSizeX / 2, KraftIconIII_Y + TechIconSizeY + (KraftIconVI_Y - KraftIconIII_Y - TechIconSizeY) / 2), (KraftIconVI_X + TechIconSizeX / 2, KraftIconVI_Y))
                        if techArray["Kraft"][2] == True:
                            self.KraftIconIIISurface = self.gameDisplay.blit(self.KraftIconIII, (KraftIconIII_X, KraftIconIII_Y))
                            if techArray["Kraft"][5] == False:
                                loccolor = violet
                            else:
                                loccolor = black
                            pygame.draw.line(self.gameDisplay, loccolor, (KraftIconIII_X + TechIconSizeX / 2, KraftIconIII_Y + TechIconSizeY), (KraftIconIII_X + TechIconSizeX / 2, KraftIconIII_Y + TechIconSizeY +(KraftIconVI_Y - KraftIconIII_Y - TechIconSizeY) / 2))
                            pygame.draw.line(self.gameDisplay, loccolor, (KraftIconIII_X + TechIconSizeX / 2, KraftIconIII_Y + TechIconSizeY + (KraftIconVI_Y - KraftIconIII_Y - TechIconSizeY) / 2), (KraftIconVI_X + TechIconSizeX / 2, KraftIconIII_Y + TechIconSizeY + (KraftIconVI_Y - KraftIconIII_Y - TechIconSizeY) / 2))
                            if techArray["Kraft"][5]:
                                self.KraftIconVISurface = self.gameDisplay.blit(self.KraftIconVI, (KraftIconVI_X, KraftIconVI_Y)) #searchBaum
                            else:
                                self.KraftIconVISurface = self.gameDisplay.blit(self.KraftIconVIBlocked, (KraftIconVI_X, KraftIconVI_Y))
                        else:
                            self.KraftIconIIISurface = self.gameDisplay.blit(self.KraftIconIIIBlocked, (KraftIconIII_X, KraftIconIII_Y))

                        if techArray["Kraft"][3] == True:
                            self.KraftIconIVSurface = self.gameDisplay.blit(self.KraftIconIV, (KraftIconIV_X, KraftIconIV_Y))
                            if techArray["Kraft"][5] == False:
                                loccolor = violet
                            else:
                                loccolor = black
                            pygame.draw.line(self.gameDisplay, loccolor, (KraftIconIV_X + TechIconSizeX /  2, KraftIconIV_Y + TechIconSizeY), (KraftIconVI_X + TechIconSizeX / 2, KraftIconVI_Y))
                            if techArray["Kraft"][5]:
                                self.KraftIconVISurface = self.gameDisplay.blit(self.KraftIconVI, (KraftIconVI_X, KraftIconVI_Y))
                            else:
                                self.KraftIconVISurface = self.gameDisplay.blit(self.KraftIconVIBlocked, (KraftIconVI_X, KraftIconVI_Y))
                        else:
                            self.KraftIconIVSurface = self.gameDisplay.blit(self.KraftIconIVBlocked, (KraftIconIV_X, KraftIconIV_Y))
                        if techArray["Kraft"][4] == True:
                            self.KraftIconVSurface = self.gameDisplay.blit(self.KraftIconV, (KraftIconV_X, KraftIconV_Y))
                            if techArray["Kraft"][5] == True:
                                loccolor = black
                            else:
                                loccolor = violet
                            pygame.draw.line(self.gameDisplay, loccolor, (KraftIconV_X + TechIconSizeX / 2, KraftIconV_Y + TechIconSizeY), (KraftIconV_X + TechIconSizeX / 2, KraftIconV_Y + TechIconSizeY + (KraftIconVI_Y - KraftIconV_Y - TechIconSizeY) / 2))
                            pygame.draw.line(self.gameDisplay, loccolor, (KraftIconV_X + TechIconSizeX / 2, KraftIconV_Y + TechIconSizeY + (KraftIconVI_Y - KraftIconV_Y - TechIconSizeY) / 2), (KraftIconVI_X + TechIconSizeX / 2, KraftIconV_Y + TechIconSizeY + (KraftIconVI_Y - KraftIconV_Y - TechIconSizeY) / 2))
                            if techArray["Kraft"][5]:
                                self.KraftIconVISurface = self.gameDisplay.blit(self.KraftIconVI, (KraftIconVI_X, KraftIconVI_Y))
                            else:
                                self.KraftIconVISurface = self.gameDisplay.blit(self.KraftIconVIBlocked, (KraftIconVI_X, KraftIconVI_Y))
                        else:
                            self.KraftIconVSurface = self.gameDisplay.blit(self.KraftIconVBlocked, (KraftIconV_X, KraftIconV_Y))
                    else:
                        self.KraftIconIISurface = self.gameDisplay.blit(self.KraftIconIIBlocked, (KraftIconII_X, KraftIconII_Y))
                else:
                    self.KraftIconISurface = self.gameDisplay.blit(self.KraftIconIBlocked, (KraftIconI_X, KraftIconI_Y))

                if techArray["Kraft"][6]:
                    self.KraftIconVIISurface = self.gameDisplay.blit(self.KraftIconVII, (KraftIconVII_X, KraftIconVII_Y))
                    if techArray["Kraft"][7]:
                        loccolor = black
                    else:
                        loccolor = violet
                    pygame.draw.line(self.gameDisplay, loccolor, (KraftIconVII_X + TechIconSizeX / 2, KraftIconVII_Y + TechIconSizeY), (KraftIconVIII_X + TechIconSizeX / 2, KraftIconVIII_Y))
                    if techArray["Kraft"][7]:
                        self.KraftIconVIIISurface = self.gameDisplay.blit(self.KraftIconVIII, (KraftIconVIII_X, KraftIconVIII_Y))
                    else:
                        self.KraftIconVIIISurface = self.gameDisplay.blit(self.KraftIconVIIIBlocked, (KraftIconVIII_X, KraftIconVIII_Y))
                else:
                    self.KraftIconVIISurface = self.gameDisplay.blit(self.KraftIconVIIBlocked, (KraftIconVII_X, KraftIconVII_Y))

                if techArray["Weisheit"][0]:
                    self.WeisheitIconISurface = self.gameDisplay.blit(self.WeisheitIconI, (WeisheitIconI_X, WeisheitIconI_Y))
                    if techArray["Weisheit"][1] or techArray["Weisheit"][2]:
                        loccolor = black
                    else:
                        loccolor = violet
                    pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconI_X + TechIconSizeX / 2, WeisheitIconI_Y + TechIconSizeY), (WeisheitIconIII_X + TechIconSizeX / 2, (WeisheitIconIII_Y+WeisheitIconI_Y+TechIconSizeY)/2))
                    if techArray["Weisheit"][1]:
                        loccolor = black
                    else:
                        loccolor = violet
                    pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconI_X + TechIconSizeX / 2, WeisheitIconI_Y + TechIconSizeY + (WeisheitIconII_Y - WeisheitIconI_Y - TechIconSizeY) / 2), (WeisheitIconII_X + TechIconSizeX / 2, (WeisheitIconII_Y + WeisheitIconI_Y + TechIconSizeY) / 2))
                    pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconII_X + TechIconSizeX / 2, WeisheitIconI_Y + TechIconSizeY + (WeisheitIconII_Y - WeisheitIconI_Y - TechIconSizeY) / 2), (WeisheitIconII_X + TechIconSizeX / 2, WeisheitIconII_Y))
                    if techArray["Weisheit"][2]:
                        loccolor = black
                    else:
                        loccolor = violet
                    pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconI_X+TechIconSizeX/2, (WeisheitIconI_Y+TechIconSizeY+WeisheitIconIII_Y)/2), (WeisheitIconIII_X+TechIconSizeX/2, WeisheitIconIII_Y))
                    if techArray["Weisheit"][1] == True:
                        self.WeisheitIconIISurface = self.gameDisplay.blit(self.WeisheitIconII, (WeisheitIconII_X, WeisheitIconII_Y))
                    else:
                        self.WeisheitIconIISurface = self.gameDisplay.blit(self.WeisheitIconIIBlocked, (WeisheitIconII_X, WeisheitIconII_Y))
                    if techArray["Weisheit"][2]:
                        self.WeisheitIconIIISurface = self.gameDisplay.blit(self.WeisheitIconIII, (WeisheitIconIII_X, WeisheitIconIII_Y))
                        if techArray["Weisheit"][3] or techArray["Weisheit"][4]:
                            loccolor = black
                        else:
                            loccolor = violet
                        pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconIII_X + TechIconSizeX / 2, WeisheitIconIII_Y + TechIconSizeY), (WeisheitIconIV_X + TechIconSizeX / 2, (WeisheitIconIV_Y+WeisheitIconIII_Y+TechIconSizeY)/2))
                        if techArray["Weisheit"][3]:
                            loccolor = black
                        else:
                            loccolor = violet
                        pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconIV_X + TechIconSizeX / 2, (WeisheitIconIV_Y+WeisheitIconIII_Y+TechIconSizeY)/2), (WeisheitIconIV_X + TechIconSizeX / 2, WeisheitIconIV_Y))
                        if techArray["Weisheit"][4]:
                            loccolor = black
                        else:
                            loccolor = violet
                        pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconIII_X + TechIconSizeX / 2, WeisheitIconIII_Y + TechIconSizeY + (WeisheitIconV_Y - WeisheitIconIII_Y - TechIconSizeY) / 2), (WeisheitIconV_X + TechIconSizeX / 2, WeisheitIconIII_Y + TechIconSizeY + (WeisheitIconV_Y - WeisheitIconIII_Y - TechIconSizeY) / 2))
                        pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconV_X + TechIconSizeX / 2, WeisheitIconIII_Y + TechIconSizeY + (WeisheitIconV_Y - WeisheitIconIII_Y - TechIconSizeY) / 2), (WeisheitIconV_X + TechIconSizeX / 2, WeisheitIconV_Y))
                        if techArray["Weisheit"][3]:
                            self.WeisheitIconIVSurface = self.gameDisplay.blit(self.WeisheitIconIV, (WeisheitIconIV_X, WeisheitIconIV_Y))
                            if techArray["Weisheit"][5]:
                                loccolor = black
                            else:
                                loccolor = violet
                            pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconIV_X + TechIconSizeX / 2, WeisheitIconIV_Y + TechIconSizeY), (WeisheitIconIV_X + TechIconSizeX / 2, WeisheitIconIV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconIV_Y - TechIconSizeY) / 2))
                            pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconIV_X + TechIconSizeX / 2, WeisheitIconIV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconIV_Y - TechIconSizeY) / 2), (WeisheitIconVI_X + TechIconSizeX / 2, WeisheitIconIV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconIV_Y - TechIconSizeY) / 2))
                            pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconVI_X + TechIconSizeX / 2, WeisheitIconIV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconIV_Y - TechIconSizeY) / 2), (WeisheitIconVI_X + TechIconSizeX / 2, WeisheitIconVI_Y))
                            if techArray["Weisheit"][5]:
                                self.WeisheitIconVISurface = self.gameDisplay.blit(self.WeisheitIconVI, (WeisheitIconVI_X, WeisheitIconVI_Y))
                            else:
                                self.WeisheitIconVISurface = self.gameDisplay.blit(self.WeisheitIconVIBlocked, (WeisheitIconVI_X, WeisheitIconVI_Y))
                        else:
                            self.WeisheitIconIVSurface = self.gameDisplay.blit(self.WeisheitIconIVBlocked, (WeisheitIconIV_X, WeisheitIconIV_Y))
                        if techArray["Weisheit"][4]:
                            self.WeisheitIconVSurface = self.gameDisplay.blit(self.WeisheitIconV, (WeisheitIconV_X, WeisheitIconV_Y))
                            if techArray["Weisheit"][5]:
                                loccolor = black
                            else:
                                loccolor = violet
                            pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconV_X + TechIconSizeX / 2, WeisheitIconV_Y + TechIconSizeY), (WeisheitIconV_X + TechIconSizeX / 2, WeisheitIconV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconV_Y - TechIconSizeY) / 2))
                            pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconV_X + TechIconSizeX / 2, WeisheitIconV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconV_Y - TechIconSizeY) / 2), (WeisheitIconVI_X + TechIconSizeX / 2, WeisheitIconV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconV_Y - TechIconSizeY) / 2))
                            pygame.draw.line(self.gameDisplay, loccolor, (WeisheitIconVI_X + TechIconSizeX / 2, WeisheitIconV_Y + TechIconSizeY + (WeisheitIconVI_Y - WeisheitIconV_Y - TechIconSizeY) / 2), (WeisheitIconVI_X + TechIconSizeX / 2, WeisheitIconVI_Y))
                            if techArray["Weisheit"][5]:
                                self.WeisheitIconVISurface = self.gameDisplay.blit(self.WeisheitIconVI, (WeisheitIconVI_X, WeisheitIconVI_Y))
                            else:
                                self.WeisheitIconVISurface = self.gameDisplay.blit(self.WeisheitIconVIBlocked, (WeisheitIconVI_X, WeisheitIconVI_Y))
                        else:
                            self.WeisheitIconVSurface = self.gameDisplay.blit(self.WeisheitIconVBlocked, (WeisheitIconV_X, WeisheitIconV_Y))
                    else:
                        self.WeisheitIconIIISurface = self.gameDisplay.blit(self.WeisheitIconIIIBlocked, (WeisheitIconIII_X, WeisheitIconIII_Y))
                else:
                    self.WeisheitIconISurface = self.gameDisplay.blit(self.WeisheitIconIBlocked, (WeisheitIconI_X, WeisheitIconI_Y))

                if techArray["Weisheit"][6]:
                    self.WeisheitIconVIISurface = self.gameDisplay.blit(self.WeisheitIconVII, (WeisheitIconVII_X, WeisheitIconVII_Y))
                    if techArray["Weisheit"][7]:
                        loccolor = black
                    else:
                        loccolor = violet
                    pygame.draw.line(self.gameDisplay, black, (WeisheitIconVII_X + TechIconSizeX / 2, WeisheitIconVII_Y + TechIconSizeY), (WeisheitIconVIII_X + TechIconSizeX / 2, WeisheitIconVIII_Y))
                    if techArray["Weisheit"][7]:
                        self.WeisheitIconVIIISurface = self.gameDisplay.blit(self.WeisheitIconVIII, (WeisheitIconVIII_X, WeisheitIconVIII_Y))
                    else:
                        self.WeisheitIconVIIISurface = self.gameDisplay.blit(self.WeisheitIconVIIIBlocked, (WeisheitIconVIII_X, WeisheitIconVIII_Y))
                else:
                    self.WeisheitIconVIISurface = self.gameDisplay.blit(self.WeisheitIconVIIBlocked, (WeisheitIconVII_X, WeisheitIconVII_Y))


                if self.TechInfoOpen == True:
                    self.showInfo(self.TechInfoString)

                self.TechBuild = True



            else:   #Normale Sternübersicht
                self.gameDisplay.blit(self.BackgroundPictureMain, (0,0))

                if self.yourTeam == "Team1":
                    strahlung = self.strahlungTeam1
                    metalle = self.metalleTeam1
                else:
                    strahlung = self.strahlungTeam2
                    metalle = self.metalleTeam2


                #Zeichen der Sterne Team 1
                if self.chooseAttackStar == True and self.yourTeam == "Team2":
                    for star in self.starArrayTeam1:
                        pygame.draw.circle(self.gameDisplay, team1_color, [star["cord_x"], star["cord_y"]], star_size)
                        pygame.draw.circle(self.gameDisplay, team1_color, [star["cord_x"], star["cord_y"]], star_size_choose, 3)
                else:
                    for star in self.starArrayTeam1:
                        pygame.draw.circle(self.gameDisplay, team1_color, [star["cord_x"], star["cord_y"]], star_size)

                #Zeichnen der Sterne Team 2
                if self.chooseAttackStar == True and self.yourTeam == "Team1":
                    for star in self.starArrayTeam2:
                        pygame.draw.circle(self.gameDisplay, team2_color, [star["cord_x"], star["cord_y"]], star_size)
                        pygame.draw.circle(self.gameDisplay, team2_color, [star["cord_x"], star["cord_y"]], star_size_choose, 3)
                else:
                    for star in self.starArrayTeam2:
                        pygame.draw.circle(self.gameDisplay, team2_color, [star["cord_x"], star["cord_y"]], star_size)

                #Zeichnen der Special Sterne
                for star in self.starArraySpecial:
                    pygame.draw.circle(self.gameDisplay, special_color, [star["cord_x"], star["cord_y"]], star_size)

                if self.yourTeam == "Team1" and self.chooseAttackStar:
                    for star in self.starArrayHostileTeam1:
                        pygame.draw.circle(self.gameDisplay, hostileteam1_color, [star["cord_x"], star["cord_y"]], star_size)
                        pygame.draw.circle(self.gameDisplay, hostileteam1_color, [star["cord_x"], star["cord_y"]], star_size_choose, 3)
                else:
                    for star in self.starArrayHostileTeam1:
                        pygame.draw.circle(self.gameDisplay, hostileteam1_color, [star["cord_x"], star["cord_y"]], star_size)

                if self.yourTeam == "Team2" and self.chooseAttackStar:
                    for star in self.starArrayHostileTeam2:
                        pygame.draw.circle(self.gameDisplay, hostileteam2_color, [star["cord_x"], star["cord_y"]], star_size)
                        pygame.draw.circle(self.gameDisplay, hostileteam2_color, [star["cord_x"], star["cord_y"]], star_size_choose, 3)
                else:
                    for star in self.starArrayHostileTeam2:
                        pygame.draw.circle(self.gameDisplay, hostileteam2_color, [star["cord_x"], star["cord_y"]], star_size)

                self.SettingsIconSurface = self.gameDisplay.blit(self.SettingsIcon, (10,10, SettingsIconSize, SettingsIconSize))

                self.drawStarDisplay()

                if self.MetallHover:
                    InfoSurface = pygame.gfxdraw.filled_polygon(self.gameDisplay, [(display_x - 534, 90), (display_x - 514, 70), (display_x - 320, 70), (display_x - 300, 90), (display_x - 300, 280), (display_x - 320, 305), (display_x - 514, 305), (display_x - 534, 280)], (255,255,255,50))
                    pygame.gfxdraw.polygon(self.gameDisplay, [(display_x - 534, 90), (display_x - 514, 70), (display_x - 320, 70), (display_x - 300, 90), (display_x - 300, 280), (display_x - 320, 305), (display_x - 514, 305), (display_x - 534, 280)], (255, 255, 255))

                    MetallTextArray = ["Diese", "Zahl", "zeigt", "euch", "die", "momentane", "Anzahl", "an", "Metallen", "an.", "Ihr", "könnt", "Metalle", "benutzen", "um", "Technologien", "zu", "erwerben", "und", "Spezialfähigkeiten", "zu", "benutzen.", " "]

                    y = 10
                    holder = ""
                    MetallTextSurface = pygame.surface.Surface((190, 950), pygame.SRCALPHA, 32)
                    MetallTextSurface.fill((0,0,0,0))

                    k=0
                    for word in MetallTextArray:
                        k+=1
                        if self.MainFontSmall.size(holder + " " + word)[0] < 170 and k<len(MetallTextArray):
                            holder = holder  + " " + word
                        else:
                            MetallTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            holder = word

                    HolderSurface = pygame.surface.Surface((190, 230), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(MetallTextSurface, (0, 0))


                    self.gameDisplay.blit(HolderSurface, (display_x - 515, 75))


                if self.StrahlungHover:
                    InfoSurface = pygame.gfxdraw.filled_polygon(self.gameDisplay, [(display_x - 284, 90), (display_x - 264, 70), (display_x - 70, 70), (display_x - 50, 90), (display_x - 50, 280), (display_x - 70, 305), (display_x - 264, 305), (display_x - 284, 280)], (255,255,255,50))
                    pygame.gfxdraw.polygon(self.gameDisplay, [(display_x - 284, 90), (display_x - 264, 70), (display_x - 70, 70), (display_x - 50, 90), (display_x - 50, 280), (display_x - 70, 305), (display_x - 264, 305), (display_x - 284, 280)], (255, 255, 255))

                    StrahlungTextArray = ["Diese", "Zahl", "gibt", "an,", "über", "wie", "viel", "Strahlung", "ihr", "gerade", "verfügt.", "Strahlung", "wird", "genutzt", "um", "neue", "Sterne", "zu", "erzeugen", "und", "spezielle", "Fähigkeiten", "zu", "benutzen.", " "]

                    y = 10
                    holder = ""
                    StrahlungTextSurface = pygame.surface.Surface((190, 950), pygame.SRCALPHA, 32)
                    StrahlungTextSurface.fill((0,0,0,0))

                    k=0
                    for word in StrahlungTextArray:
                        k+=1
                        if self.MainFontSmall.size(holder + " " + word)[0] < 170 and k<len(StrahlungTextArray):
                            holder = holder  + " " + word
                        else:
                            StrahlungTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            holder = word

                    HolderSurface = pygame.surface.Surface((190, 230), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(StrahlungTextSurface, (0, 0))


                    self.gameDisplay.blit(HolderSurface, (display_x - 255, 75))

                if self.NewStarHover:
                    InfoSurface = pygame.gfxdraw.filled_polygon(self.gameDisplay, [(display_x - 284, display_y-40-IconSize-30 ), (display_x - 264, display_y-40-IconSize-10), (display_x - 70, display_y - 40 - IconSize - 10), (display_x - 50, display_y - 40 - IconSize- 30), (display_x - 50, display_y-40-IconSize - 120), (display_x - 70, display_y-40-IconSize-135), (display_x - 264, display_y-40-IconSize-135), (display_x - 284, display_y-40-IconSize-120)], (255,255,255,50))
                    pygame.gfxdraw.polygon(self.gameDisplay, [(display_x - 284, display_y-40-IconSize-30 ), (display_x - 264, display_y-40-IconSize-10), (display_x - 70, display_y - 40 - IconSize - 10), (display_x - 50, display_y - 40 - IconSize- 30), (display_x - 50, display_y-40-IconSize - 120), (display_x - 70, display_y-40-IconSize-135), (display_x - 264, display_y-40-IconSize-135), (display_x - 284, display_y-40-IconSize-120)], (255, 255, 255))

                    NewStarTextArray = ["Erschaffen", "Sie", "einen", "neuen", "Stern!", "Stellen", "Sie", "seine", "Masse", "ein", "und", "wählen", "sie", "anschließend", "eine", "Position", "aus!", " "]

                    y = 10
                    holder = ""
                    NewStarTextSurface = pygame.surface.Surface((190, 950), pygame.SRCALPHA, 32)
                    NewStarTextSurface.fill((0,0,0,0))

                    k=0
                    for word in NewStarTextArray:
                        k+=1
                        if self.MainFontSmall.size(holder + " " + word)[0] < 170 and k<len(NewStarTextArray):
                            holder = holder  + " " + word
                        else:
                            NewStarTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            holder = word

                    HolderSurface = pygame.surface.Surface((190, 230), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(NewStarTextSurface, (0, 0))

                    self.gameDisplay.blit(HolderSurface, (display_x - 255, display_y-40-IconSize-130))

                if self.TechHover:
                    InfoSurface = pygame.gfxdraw.filled_polygon(self.gameDisplay, [(display_x - 284, display_y-40-IconSize-30 ), (display_x - 264, display_y-40-IconSize-10), (display_x - 70, display_y - 40 - IconSize - 10), (display_x - 50, display_y - 40 - IconSize- 30), (display_x - 50, display_y-40-IconSize - 80), (display_x - 70, display_y-40-IconSize-95), (display_x - 264, display_y-40-IconSize-95), (display_x - 284, display_y-40-IconSize-80)], (255,255,255,50))
                    pygame.gfxdraw.polygon(self.gameDisplay, [(display_x - 284, display_y-40-IconSize-30 ), (display_x - 264, display_y-40-IconSize-10), (display_x - 70, display_y - 40 - IconSize - 10), (display_x - 50, display_y - 40 - IconSize- 30), (display_x - 50, display_y-40-IconSize - 80), (display_x - 70, display_y-40-IconSize-95), (display_x - 264, display_y-40-IconSize-95), (display_x - 284, display_y-40-IconSize-80)], (255, 255, 255))

                    TechTextArray = ["Erforschen", "Sie", "neue", "Möglichkeiten", "Ihre", "Sterne", "zu", "verbessern.", " "]

                    y = 10
                    holder = ""
                    TechTextSurface = pygame.surface.Surface((190, 950), pygame.SRCALPHA, 32)
                    TechTextSurface.fill((0,0,0,0))

                    k=0
                    for word in TechTextArray:
                        k+=1
                        if self.MainFontSmall.size(holder + " " + word)[0] < 170 and k<len(TechTextArray):
                            holder = holder  + " " + word
                        else:
                            TechTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            holder = word


                    HolderSurface = pygame.surface.Surface((190, 230), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(TechTextSurface, (0, 0))

                    self.gameDisplay.blit(HolderSurface, (display_x - 255, display_y-40-IconSize-90))

                if self.SettingsOpen:   #Settings Graphik
                    #Begrenzung des Fensters
                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(18, 82), (39, 55), (216, 55), (237, 82), (237, 325), (216, 352), (39, 352), (18, 325)], (255,255,255,50))
                    pygame.gfxdraw.polygon(self.gameDisplay, [(18, 82), (39, 55), (216, 55), (237, 82), (237, 325), (216, 352), (39, 352), (18, 325)], (255, 255, 255))

                    #Slider MasterVolume
                    Text="Gesamtlautstärke"
                    self.MasterVolumeSliderText=self.MainFontSmall.render(Text, True, white)
                    self.MasterVolumeSliderTextSurface=self.gameDisplay.blit(self.MasterVolumeSliderText, (40,80))
                    pygame.draw.line(self.gameDisplay, black, (42, 113), (210, 113), 3)
                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(32, 113), (42, 105), (42, 121)], white80)
                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(210, 105), (220, 113), (210, 121)], white80)
                    pygame.draw.circle(self.gameDisplay, white, (round(42 + self.MasterVolumeSliderPos*168/100), 113), self.VolumeSliderSize)

                    #slider MusicVolume
                    Text="Musiklautstärke"
                    self.MusicVolumeSliderText=self.MainFontSmall.render(Text, True, white)
                    self.MusicVolumeSliderTextSurface=self.gameDisplay.blit(self.MusicVolumeSliderText, (40,180))
                    pygame.draw.line(self.gameDisplay, black, (42, 213), (210, 213), 3)
                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(32, 213), (42, 205), (42, 221)], white80)
                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(210, 205), (220, 213), (210, 221)], white80)
                    pygame.draw.circle(self.gameDisplay, white, (round(42 + self.MusicVolumeSliderPos*168/100), 213), self.VolumeSliderSize)

                    #slider SFXVolume
                    Text="Effektlautstärke"
                    self.SFXVolumeSliderText=self.MainFontSmall.render(Text, True, white)
                    self.SFXVolumeSliderTextSurface=self.gameDisplay.blit(self.SFXVolumeSliderText, (40,280))
                    pygame.draw.line(self.gameDisplay, black, (42, 313), (210, 313), 3)
                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(32, 313), (42, 305), (42, 321)], white80)
                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(210, 305), (220, 313), (210, 321)], white80)
                    pygame.draw.circle(self.gameDisplay, white, (round(42 + self.SFXVolumeSliderPos*168/100), 313), self.VolumeSliderSize)


                MetallIconSurface = self.gameDisplay.blit(self.MetallIcon, (500, 5))
                StrahlungIconSurface = self.gameDisplay.blit(self.StrahlungIcon, (750, 5))


                self.StrahlungText = self.MainFontMiddle.render(str(round(strahlung/1000000, 1)) + " Mio.", True, StrahlungTextColor)
                self.StrahlungTextSurface = self.gameDisplay.blit(self.StrahlungText, (800, 15))

                self.MetallText = self.MainFontMiddle.render(str(int(metalle)), True, MetallTextColor)
                self.MetallTextSurface = self.gameDisplay.blit(self.MetallText, (550, 15))

                pygame.draw.line(self.gameDisplay, white, (display_x, 50), (480, 50), 2)
                pygame.draw.line(self.gameDisplay, white, (428, 0), (488, 60), 3)

                #self.TechButton = pygame.Surface((TechButtonX, TechButtonY))
                #self.TechButton.fill(TechButtonColor)
                #self.TechButtonText = self.MainFontSmall.render("Star-Tech", True, TechButtonTextColor)
                #self.TechButtonTextSurface = self.TechButton.blit(self.TechButtonText, (TechButtonTextX, TechButtonTextY))
                self.TechButtonSurface = self.gameDisplay.blit(self.TechIcon, (display_x - 70, display_y - 70))

                #self.NewStarButton = pygame.Surface((NewStarButtonX, NewStarButtonY))
                #self.NewStarButton.fill(NewStarButtonColor)
                #self.NewStarButtonText = self.MainFontSmall.render("Neuer Stern", True, NewStarButtonTextColor)
                #self.NewStarButtonTextSurface = self.NewStarButton.blit(self.NewStarButtonText, (NewStarButtonTextX, NewStarButtonTextY))
                self.NewStarButtonSurface = self.gameDisplay.blit(self.NewStarIcon, (display_x - 150, display_y - 70))

                pygame.draw.circle(self.gameDisplay, white, (int(display_x - 70 + IconSize / 2), int(display_y - 70 + IconSize / 2)), 30, 3)
                pygame.draw.circle(self.gameDisplay, white, (int(display_x - 150 + IconSize / 2), int(display_y - 70 + IconSize / 2)), 30, 3)




            for star in self.starArrayTeam1:
                if star['cat'] == 'Geburt':
                    if self.techArrayTeam1['Weisheit'][3]:
                        mod = 0.5
                    else:
                        mod = 1.0
                elif star['cat'] == 'Hauptreihe':
                    if self.techArrayTeam1["Weisheit"][0]:
                        mod = 1.1
                    else:
                        mod = 1.0
                elif star['cat'] == 'Riese' or star['cat'] == 'Hyperriese' or star['cat'] == 'Überriese':
                    mod = 1.5
                elif star['cat'] == 'Zwerg':
                    mod = 0.8
                elif star['cat'] == 'Neutronenstern':
                    mod = 0
                elif star['cat'] == 'Schwarzes Loch':
                    mod =-0.7
                elif star['cat'] == 'Weißes Loch':
                    mod = 1.5
                if self.yourTeam == "Team1":
                    if self.techArrayTeam1['Perfektion'][7]:
                        mod = mod * 1.25
                    self.strahlungTeam1 = self.strahlungTeam1 + mod * (2-1.5*(star["mass"]/20))*(10000 * star["mass"]  *(star["mass"]+1)**0.5/600) #StrahlungFormel für suche
                star["nextLevel"] = star["nextLevel"] - (1/FPS)
                if star["nextLevel"] <= 0:
                    self.nextLevel(star)

            for star in self.starArrayTeam2:
                if star['cat'] == 'Geburt':
                    mod = .5
                elif star['cat'] == 'Hauptreihe':
                    if self.techArrayTeam2["Weisheit"][0]:
                        mod = 1.1
                    else:
                        mod = 1
                elif star['cat'] == 'Riese' or star['cat'] == 'Hyperriese' or star['cat'] == 'Überriese':
                    mod = 1.5
                elif star['cat'] == 'Zwerg':
                    mod = 0.8
                elif star['cat'] == 'Neutronenstern':
                    mod = 0
                elif star['cat'] == 'Schwarzes Loch':
                    mod =-0.7
                elif star['cat'] == 'Weißes Loch':
                    mod = 1.5
                if self.yourTeam == "Team2":
                    if self.techArrayTeam2['Perfektion'][7]:
                        mod = mod * 1.25
                    self.strahlungTeam2 = self.strahlungTeam2 + (2-1.5*(star["mass"]/20))*(10000 * star["mass"]  *(star["mass"]+1)**0.5/600)
                star["nextLevel"] = star["nextLevel"] - (1/FPS)
                if star["nextLevel"] <= 0:
                    self.nextLevel(star)

            if self.Attacks is not []:
                for attack in self.Attacks:
                    Angreifer = attack["Angreifer"]
                    Verteidiger = attack["Verteidiger"]
                    TeamAng = attack["TeamAng"]
                    TeamVer = attack["TeamVer"]


                    if TeamAng != self.yourTeam:    #Wenn du nicht der angreifende Stern bist
                        if TeamAng == "Team1":      #Wenn der angreigende Stern aus Team1 ist
                            for star in self.starArrayTeam1:
                                if star["name"] == Angreifer:
                                    Gegner = star
                                    GegnerArray = "starArrayTeam1"
                            for star in self.starArrayTeam2:
                                if star["name"] == Verteidiger:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam2"
                        elif TeamAng == "Team2":     #Wenn deer angreifende Stern aus Team2 ist
                            for star in self.starArrayTeam2:
                                if star["name"] == Angreifer:
                                    Gegner = star
                                    GegnerArray = "starArrayTeam2"
                            for star in self.starArrayTeam1:
                                if star["name"] == Verteidiger:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam1"
                        elif TeamAng == "Team3":     #Der Stern ist einer durch Events entstandener Stern
                            for star in self.starArrayHostileTeam1:
                                if star["name"] == Angreifer:
                                    Gegner = star
                                    GegnerArray = "starArrayHostileTeam1"
                            for star in self.starArrayTeam1:
                                if star["name"] == Verteidiger:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam1"
                        elif TeamAng == "Team4":     #Der Stern ist einer durch Events entstandener Stern
                            for star in self.starArrayHostileTeam2:
                                if star["name"] == Angreifer:
                                    Gegner = star
                                    GegnerArray = "starArrayHostileTeam2"
                            for star in self.starArrayTeam1:
                                if star["name"] == Verteidiger:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam2"

                    elif TeamVer != self.yourTeam:
                        if TeamVer == "Team1":      #Wenn der angreigende Stern aus Team1 ist
                            for star in self.starArrayTeam1:
                                if star["name"] == Verteidiger:
                                    Gegner = star
                                    GegnerArray = "starArrayTeam1"
                            for star in self.starArrayTeam2:
                                if star["name"] == Angreifer:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam2"
                        elif TeamVer == "Team2":     #Wenn deer angreifende Stern aus Team2 ist
                            for star in self.starArrayTeam2:
                                if star["name"] == Verteidiger:
                                    Gegner = star
                                    GegnerArray = "starArrayTeam2"
                            for star in self.starArrayTeam1:
                                if star["name"] == Angreifer:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam1"
                        elif TeamVer == "Team3":     #Der Stern ist einer durch Events entstandener Stern
                            for star in self.starArrayHostileTeam1:
                                if star["name"] == Verteidiger:
                                    Gegner = star
                                    GegnerArray = "starArrayHostileTeam1"
                            for star in self.starArrayTeam1:
                                if star["name"] == Angreifer:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam1"
                        elif TeamVer == "Team4":     #Der Stern ist einer durch Events entstandener Stern
                            for star in self.starArrayHostileTeam2:
                                if star["name"] == Verteidiger:
                                    Gegner = star
                                    GegnerArray = "starArrayHostileTeam2"
                            for star in self.starArrayTeam2:
                                if star["name"] == Angreifer:
                                    DeinStern = star
                                    DeinArray = "starArrayTeam2"

                    elif TeamAng == TeamVer:
                        self.Attacks.remove(attack)
                        continue

                    DeinSchaden = 100*2**(-DeinStern["mass"]/20)
                    distance = ((abs(DeinStern["cord_x"] - Gegner["cord_x"]))** 2 + (abs(DeinStern["cord_y"] - Gegner["cord_y"]))** 2 )**0.5

                    rangeAt, rangeDef, attackAt, attackDef, defenseAt, defenseDef, stackingAt, modAt, modDef = 1, 1, 1, 1, 1, 1, 1, 1, 1

                    for value in self.OngoingAttacksMods:
                        if value["star"] == Angreifer:
                            timemod = value["time"]
                            break

                    if self.yourTeam == "Team1":
                        DeinTechBaum = self.techArrayTeam1
                        GegnerTechBaum = self.techArrayTeam2
                    elif self.yourTeam == "Team2":
                        DeinTechBaum = self.techArrayTeam2
                        GegnerTechBaum = self.techArrayTeam1

                    attackAt = attackAt * self.attackmod

                    if self.yourTeam == TeamAng:
                        if DeinStern['cat'] == 'Geburt':
                            modAt = 1
                        elif DeinStern['cat'] == 'Hauptreihe':
                            modAt = 1
                        elif DeinStern['cat'] == 'Riese' or DeinStern['cat'] == 'Hyperriese' or DeinStern['cat'] == 'Überriese':
                            modAt = 0.7
                        elif DeinStern['cat'] == 'Zwerg':
                            if DeinTechBaum['Weisheit'][7]:
                                modAt = 2.0
                            else:
                                modAt = 1.7
                        elif DeinStern['cat'] == 'Neutronenstern':
                            modAt = 2.5
                        elif DeinStern['cat'] == 'Schwarzes Loch':
                            modAt = 3
                        elif starAt['cat'] == 'Weißes Loch':
                            modAt = 4

                        if DeinTechBaum["Kraft"][1] == True:    #
                            rangeAt = rangeAt * 0.85
                        if DeinTechBaum['Weisheit'][3]:         #
                            rangeAt = rangeAt * 1.3
                        if DeinTechBaum["Kraft"][8] == True:    #
                            attackAt = attackAt * 1.1
                        if GegnerTechBaum["Kraft"][3] == True:  #
                            defenseDef = defenseDef * 0.85
                        if DeinTechBaum["Kraft"][6] == True:    #
                            stackingAt = stackingAt * 0.75
                        if DeinTechBaum["Kraft"][3] == True:    #
                            timepenaltyAt = 1
                        else:
                            timepenaltyAt = (5-timemod)/5

                        stackingpenalty = 3/2**stackingAt    #Stackingpenalty für einen einzelnen angreifenden Stern muss 1 sein

                        for Angriff in self.Attacks:
                            if Angriff["Verteidiger"] == Verteidiger:
                                if Angriff["Angreifer"] != Angreifer:     #Solange es nicht um genau das Battle geht
                                    stackingpenalty = stackingpenalty * (2/3)**stackingAt
                                else:
                                    break
                       #print(stackingpenalty)
                        DeinSchaden = DeinSchaden * modAt * attackAt * defenseDef * 3**(-distance*rangeAt/display_x) *timepenaltyAt * stackingpenalty * (1/FPS) * 0.1

                        if TeamVer == "Team3":
                            if DeinStern['cat'] == 'Geburt':
                                modDef = 1
                            elif DeinStern['cat'] == 'Hauptreihe':
                                modDef = 1
                            elif DeinStern['cat'] == 'Riese' or DeinStern['cat'] == 'Hyperriese' or DeinStern['cat'] == 'Überriese':
                                modDef = 0.7
                            elif DeinStern['cat'] == 'Zwerg':
                                if DeinTechBaum['Weisheit'][7]:
                                    modDef = 2.0
                                else:
                                    modDef = 1.7
                            elif DeinStern['cat'] == 'Neutronenstern':
                                modDef = 2.5
                            elif DeinStern['cat'] == 'Schwarzes Loch':
                                modDef = 3
                            elif starAt['cat'] == 'Weißes Loch':
                                modDef = 2.5

                            if DeinTechBaum["Kraft"][8] == True:
                                attackDef = attackDef * 1.1
                            if DeinTechBaum["Kraft"][3] == True:
                                defenseAt = defenseAt * 0.85
                            if DeinTechBaum["Kraft"][2] == True:
                                rangeDef = rangeDef * 0.85
                            if DeinTechBaum['Weisheit'][2]:
                                rangeDef = rangeDef * 1.3
                            if DeinTechBaum["Kraft"][3] == True:
                                timepenaltyDef = 1
                            else:
                                timepenaltyDef = (5-timemod)/5

                            GegnerSchaden = GegnerSchaden * modDef * attackDef * defenseAt * 3**(-distance*rangeDef/display_x) * timepenaltyDef * (1/FPS) * 0.1
                            attack["SchadenVer"] = GegnerSchaden
                            DeinStern["health"] - GegnerSchaden
                            Gegner["health"] - DeinSchaden
                            if  DeinStern["health"] < 0:
                                self.starCaptured(DeinStern["name"], Gegner["name"], "Gegner")
                            elif Gegner["health"] < 0:
                                self.starCaptured(DeinStern["name"], Gegner["name"], "DeinStern")
                            if self.yourTeam == "Team1":
                                for star in self.starArrayTeam1:
                                    if star["name"] == DeinStern["name"]:
                                        star = DeinStern
                                for star in self.starArrayHostileTeam1:
                                    if star["name"] == DeinStern["name"]:
                                        star = Gegner
                            elif self.yourTeam == "Team2":
                                for star in self.starArrayTeam2:
                                    if star["name"] == DeinStern["name"]:
                                        star = DeinStern
                                for star in self.starArrayHostileTeam2:
                                    if star["name"] == Gegner["name"]:
                                        star = Gegner
                        else:
                            message = '{"action": "Schaden", "data": {"schaden": ' + str(DeinSchaden) + ', "stern": "' + Gegner["name"] + '", "von": "' + DeinStern["name"] + '"}}'
                            message = message.encode('utf-8')
                            self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                            #print(DeinStern)
                            #print("-------------------------------------")
                            if self.yourTeam == "Team1":
                                for star in self.starArrayTeam2:
                                    if star["name"] == Gegner["name"]:
                                        star["health"] -= DeinSchaden
                                        #print("health wurde auf zeile 2767 angepasst", DeinSchaden)
                                        if star["health"] <= 0:
                                            self.starCaptured(DeinStern["name"], Gegner["name"], "DeinStern")
                            elif self.yourTeam == "Team2":
                                for star in self.starArrayTeam1:
                                    if star["name"] == Gegner["name"]:
                                        star["health"] -= DeinSchaden
                                        #print("health wurde auf zeile 2774 angepasst", DeinSchaden)
                                        if star["health"] <= 0:
                                            self.starCaptured(DeinStern["name"], Gegner["name"], "DeinStern")
                        attack["SchadenAng"] = DeinSchaden
                        if attack["SchadenVer"] == 0:
                            DeinEndPoint = DeinStern["health"]
                        else:
                            DeinEndPoint = DeinStern["health"]/attack["SchadenVer"]
                        if DeinSchaden == 0:
                            GegnerEndPoint = Gegner["health"]
                        else:
                            GegnerEndPoint = Gegner["health"]/DeinSchaden
                        DeineFightPoints = DeinSchaden * DeinStern["health"]
                        GegnerFightPoints = attack["SchadenVer"] * Gegner["health"]
                        if self.yourTeam == "Team1":
                            DeineFarbe = team1_color
                            if TeamVer == "Team2":
                                GegnerFarbe = team2_color
                            elif TeamVer == "Team3":
                                GegnerFarbe = hostileteam1_color
                        elif self.yourTeam == "Team2":
                            DeineFarbe = team2_color
                            if TeamVer == "Team1":
                                GegnerFarbe = team1_color
                            elif TeamVer == "Team4":
                                GegnerFarbe = hostileteam2_color

                    elif self.yourTeam == TeamVer:
                        if DeinStern['cat'] == 'Geburt':
                            modDef = 1
                        elif DeinStern['cat'] == 'Hauptreihe':
                            modDef = 1
                        elif DeinStern['cat'] == 'Riese' or DeinStern['cat'] == 'Hyperriese' or DeinStern['cat'] == 'Überriese':
                            modDef = 0.7
                        elif DeinStern['cat'] == 'Zwerg':
                            if DeinTechBaum['Weisheit'][7]:
                                modDef = 1.7
                            else:
                                modDef = 2.0
                        elif DeinStern['cat'] == 'Neutronenstern':
                            modDef = 2.5
                        elif DeinStern['cat'] == 'Schwarzes Loch':
                            modDef = 3
                        elif DeinStern['cat'] == 'Weißes Loch':
                            modDef = 2.5

                        if DeinTechBaum["Kraft"][8] == True:
                            attackDef = attackDef * 1.1
                        if GegnerTechBaum["Kraft"][3] == True:
                            defenseAt = defenseAt * 0.85
                        if DeinTechBaum["Kraft"][2] == True:
                            rangeDef = rangeDef * 0.85
                        if DeinTechBaum['Weisheit'][2]:
                            rangeDef = rangeDef * 1.3
                        if DeinTechBaum["Kraft"][3] == True:
                            timepenaltyDef = (3-timemod)/3
                        else:
                            timepenaltyDef = (5-timemod)/5

                        DeinSchaden = DeinSchaden * modDef * attackDef * defenseAt * 3**(-distance*rangeDef/display_x) * timepenaltyDef * (1/FPS) * 0.1
                        if TeamAng == "Team3":
                            modAt = 4

                            if DeinTechBaum["Kraft"][1] == True:    #
                                rangeAt = rangeAt * 0.85
                            if DeinTechBaum['Weisheit'][3]:         #
                                rangeAt = rangeAt * 1.3
                            if DeinTechBaum["Kraft"][8] == True:    #
                                attackAt = attackAt * 1.1
                            if DeinTechBaum["Kraft"][3] == True:  #
                                defenseDef = defenseDef * 0.85
                            if DeinTechBaum["Kraft"][6] == True:    #
                                stackingAt = stackingAt * 0.75
                            if DeinTechBaum["Kraft"][3] == True:    #
                                timepenaltyAt = (3-timemod)/3
                            else:
                                timepenaltyAt = (5-timemod)/5

                            stackingpenalty = 3/2**stackingAt    #Stackingpenalty für einen einzelnen angreifenden Stern muss 1 sein

                            for Angriff in self.Attacks:
                                if Angriff["Verteidiger"] == Verteidiger:
                                    if Angriff["Angreifer"] != Angreifer:     #Solange es nicht um genau das Battle geht
                                        stackingpenalty = stackingpenalty * (2/3)**stackingAt
                            GegnerSchaden = DeinSchaden * modAt * attackAt * defenseDef * 3**(-distance*rangeAt/display_x) * timepenaltyAt * stackingpenalty * (1/FPS) * 0.1
                            attack["SchadenAng"] = GegnerSchaden
                            DeinStern["health"] - GegnerSchaden
                            Gegner["health"] - DeinSchaden
                            if  DeinStern["health"] < 0:
                                self.starCaptured(DeinStern["name"], Gegner["name"], "Gegner")
                            elif Gegner["health"] < 0:
                                self.starCaptured(DeinStern["name"], Gegner["name"], "DeinStern")
                            if self.yourTeam == "Team1":
                                for star in self.starArrayTeam1:
                                    if star["name"] == DeinStern["name"]:
                                        star = DeinStern
                                for star in self.starArrayHostileTeam1:
                                    if star["name"] == DeinStern["name"]:
                                        star = Gegner
                            elif self.yourTeam == "Team2":
                                for star in self.starArrayTeam2:
                                    if star["name"] == DeinStern["name"]:
                                        star = DeinStern
                                for star in self.starArrayHostileTeam2:
                                    if star["name"] == Gegner["name"]:
                                        star = Gegner
                        else:
                            message = '{"action": "Schaden", "data": {"schaden": ' + str(DeinSchaden) + ', "stern": "' + Gegner["name"] + '", "von": "' + DeinStern["name"] + '"}}'
                            message = message.encode('utf-8')
                            self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                            #print(DeinStern, "------------------------")
                            if self.yourTeam == "Team1":
                                for star in self.starArrayTeam2:
                                    if star["name"] == Gegner["name"]:
                                        star["health"] -= DeinSchaden
                                        #print("health wurde auf zeile 2888 angepasse", DeinSchaden)
                                        if star["health"] <= 0:
                                            self.starCaptured(DeinStern["name"], Gegner["name"], "DeinStern")
                            elif self.yourTeam == "Team2":
                                for star in self.starArrayTeam1:
                                    if star["name"] == Gegner["name"]:
                                        star["health"] -= DeinSchaden
                                        #print("health wurde auf zeile 2895 angepasst", DeinSchaden)
                                        if star["health"] <= 0:
                                            self.starCaptured(DeinStern["name"], Gegner["name"], "DeinStern")
                        attack["SchadenVer"] = DeinSchaden
                        if attack["SchadenAng"] == 0:
                            DeinEndPoint = DeinStern["health"]
                        else:
                            DeinEndPoint = DeinStern["health"]/attack["SchadenAng"]
                        if DeinSchaden == 0:
                            GegnerEndPoint = Gegner["health"]
                        else:
                            GegnerEndPoint = Gegner["health"]/DeinSchaden
                        DeineFightPoints = DeinSchaden * DeinStern["health"]
                        GegnerFightPoints = attack["SchadenAng"] * Gegner["health"]
                        if self.yourTeam == "Team1":
                            DeineFarbe = team1_color
                            if TeamAng == "Team2":
                                GegnerFarbe = team2_color
                            elif TeamAng == "Team3":
                                GegnerFarbe = hostileteam1_color
                        elif self.yourTeam == "Team2":
                            DeineFarbe = team2_color
                            if TeamAng == "Team1":
                                GegnerFarbe = team1_color
                            elif TeamAng == "Team3":
                                GegnerFarbe = hostileteam2_color

                    try:
                        Verhaltniss = (DeineFightPoints)/(DeineFightPoints + GegnerFightPoints)  # Einfach Prozent ausrechnen :)
                    except:
                        Verhaltniss = 1

                    point = (int(DeinStern["cord_x"] + (Gegner["cord_x"] - DeinStern["cord_x"]) * Verhaltniss), int(DeinStern["cord_y"] + (Gegner["cord_y"] - DeinStern["cord_y"]) * Verhaltniss))

                    if self.TechOpen == False:
                        pygame.draw.line(self.gameDisplay, DeineFarbe, (DeinStern["cord_x"], DeinStern["cord_y"]), point, 1)
                        pygame.draw.line(self.gameDisplay, GegnerFarbe, (Gegner["cord_x"], Gegner["cord_y"]), point, 1)
                        pygame.draw.circle(self.gameDisplay, colorLaser, point, round(8*(1-timemod/5)))


                    for star in self.starArrayTeam1:
                        if star['name'] == DeinStern['name']:
                            star['health'] = DeinStern['health']
                    for star in self.starArrayTeam2:
                        if star['name'] == DeinStern['name']:
                            star['health'] = DeinStern['health']

                #InfoBoxEdit von Max
            if self.infoBoxOpen == True and self.TechOpen == False:
                #if self.infoBoxTeam == "Team1":
                #    color = team1_color
                #elif self.infoBoxTeam == "Team2":
                #    color = team2_color
                #elif self.infoBoxTeam == "Special":
                #    color = special_color
                #pygame.draw.circle(self.gameDisplay, color, [self.infoBoxStar["cord_x"], self.infoBoxStar["cord_y"]], star_size_opened)
                #self.drawInfo()

                #Damit immmer die aktuellsten Daten angezeigt werden immer am Anfang aktuallisieren

                if self.infoBoxStar["team"] == 1:
                    for star in self.starArrayTeam1:
                        if self.infoBoxStar!= {} and star["name"] == self.infoBoxStar["name"]:
                            break
                elif self.infoBoxStar["team"] == 2:
                    for star in self.starArrayTeam2:
                        if self.infoBoxStar!={} and star["name"] == self.infoBoxStar["name"]:
                            break
                else:
                    star = self.infoBoxStar

                ObenSizeX = 144
                UntenSizeX = 168
                SizeY = 60
                Diff = UntenSizeX - ObenSizeX

                text_color = white

                RahmenWeissObenLinksKlein = self.loadImage("Pictures/rahmen_weiß_oben_links.png", colorkey=(0,0,0), size=(ObenSizeX,SizeY))
                self.gameDisplay.blit(RahmenWeissObenLinksKlein, (100, 100))

                RahmenWeissObenRechtsKlein = self.loadImage("Pictures/rahmen_weiß_oben_rechts.png", colorkey=(0,0,0), size=(ObenSizeX, SizeY))
                self.gameDisplay.blit(RahmenWeissObenRechtsKlein, (display_x - 100 - ObenSizeX, 100))

                RahmenWeissUntenLinksKlein = self.loadImage("Pictures/rahmen_weiß_unten_links.png", colorkey=(0,0,0), size=(UntenSizeX, SizeY))
                self.gameDisplay.blit(RahmenWeissUntenLinksKlein, (100, display_y - 100 - SizeY))

                RahmenWeissUntenRechtsKlein = self.loadImage("Pictures/rahmen_weiß_unten_rechts.png", colorkey=(0,0,0), size=(UntenSizeX, SizeY))
                self.gameDisplay.blit(RahmenWeissUntenRechtsKlein, (display_x - 100 - ObenSizeX - Diff, display_y - 100 - SizeY))

                #pygame.draw.line(self.gameDisplay, white, (100, 100), (900, 100), 2)
                pygame.draw.rect(self.gameDisplay, white, (100 + ObenSizeX, 100, (display_x - 100 - ObenSizeX) - (100 + ObenSizeX), 20))    #Oben
                pygame.draw.rect(self.gameDisplay, white, (100 + UntenSizeX, display_y - 100 - 9, (display_x - 100 - UntenSizeX) - (100 + UntenSizeX), 3))  #Unten
                pygame.draw.rect(self.gameDisplay, white, (100 + 4, 100 + SizeY, 2, (display_y - 100 - SizeY) - (100 + SizeY) + 1)) #Links
                pygame.draw.rect(self.gameDisplay, white, (display_x - 100 - 6, 100 + SizeY, 2, (display_y - 100 - SizeY) - (100 + SizeY) + 1))

                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(110, 110), (display_x - 110, 110), (display_x - 110, display_y - 110), (110, display_y - 110)], (255,255,255,50))


                CloseIcon = self.loadImage("Pictures/ic_close_white_48dp_1x.png", size=(48, 48))
                CloseIconSurface = self.gameDisplay.blit(CloseIcon, (830, 130))

                NameText = self.MainFont.render(star["name"], True, text_color)
                self.gameDisplay.blit(NameText, (140, 150))

                CatText = self.MainFontMiddle.render("Kategorie: " + star["cat"], True, text_color)
                self.gameDisplay.blit(CatText, (325, 195))

                MasseText = self.MainFontMiddle.render("Masse: " + str(round(star["mass"], 1)) + " Sonnenmassen", True, text_color)
                self.gameDisplay.blit(MasseText, (325, 230))

                AlterText = self.MainFontMiddle.render("Alter: " + str(star["age"]) + " Mio. Jahre", True, text_color)
                self.gameDisplay.blit(AlterText, (325, 265))


                if star["team"] != 0:
                    HealthText = self.MainFontMiddle.render("Health: " + str(round(star["health"])), True, text_color)
                    self.gameDisplay.blit(HealthText, (325, 300))
                    NextLevelText = self.MainFontMiddle.render("Nächstes Level: " + str(round(star["nextLevel"])) + " sek.", True, text_color)
                    self.gameDisplay.blit(NextLevelText, (325, 335))



                InfoIcon = self.loadImage("Pictures/ic_info_outline_white_48dp_1x.png", size=(48, 48))
                InfoIconSurface = self.gameDisplay.blit(InfoIcon, (830, 340))

                PicX = 140
                PicY = 200
                PicSizeX = 0
                PicSizeY = 0

                if star["name"] == "Saggittarius A*" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("Dieses mächtige schwarze Loch, ein Artefakt längst vergessener", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("Gewalten, thront in der Mitte der Galaxie, bereit alles und", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("jeden zu zereißen, der es wagt ihre Einflussphäre zu betreten", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 400))
                    self.gameDisplay.blit(InfoText1, (140, 430))
                    self.gameDisplay.blit(InfoText2, (140, 460))

                    self.gameDisplay.blit(self.PicSchwarzesLoch, (PicX, PicY))
                    PicSizeX = int(InfoBoxPicY * (1166/1280))
                    PicSizeY = InfoBoxPicY

                elif star["name"] == "Scorpio X-1" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("Der Neutronenstern Scorpio X-1 ist eine extreme Röntgenquelle.", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("Durch diese Strahlung kann er sich selbst stabilisieren und", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("gleichzeitig sehr mächtig sein.", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 400))
                    self.gameDisplay.blit(InfoText1, (140, 430))
                    self.gameDisplay.blit(InfoText2, (140, 460))

                    self.gameDisplay.blit(self.PicNeutronenstern, (PicX, PicY))
                    PicSizeX = int(InfoBoxPicY + (357/200))
                    PicSizeY = InfoBoxPicY

                elif star["name"] == "Aldebaran" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("Der Riese Aldebaran gehört zu den größten Sternen in dieser", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("Galaxie. In seiner aüßeren aufgebläten Schale werden riesige", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("Stoffmengen umgesetzt und eine gigantische Mende Strahlung", True, text_color)
                    InfoText3 = self.MainFontMiddle.render("umgesetzt.", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 400))
                    self.gameDisplay.blit(InfoText1, (140, 430))
                    self.gameDisplay.blit(InfoText2, (140, 460))
                    self.gameDisplay.blit(InfoText3, (140, 490))

                    self.gameDisplay.blit(self.PicRiese, (PicX, PicY))
                    PicSizeX = InfoBoxPicX
                    PicSizeY = InfoBoxPicY

                elif star["cat"] == "Geburt" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("Dieser Stern wird gerade erst gebildet.Durch die Gravitations-", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("kraft zieht sich eine Wasserstoffwolke mehr und mehr zusammen", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("und es bildet sich ein dichter kugelförmiger Körper. Ab einer", True, text_color)
                    InfoText3 = self.MainFontMiddle.render("bestimmten Dichte setzt die Kernfusion ein und der junge Stern", True, text_color)
                    InfoText4 = self.MainFontMiddle.render("beginnt, unglaublich heiß zu werden und Energie abzustrahlen.", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 380))
                    self.gameDisplay.blit(InfoText1, (140, 410))
                    self.gameDisplay.blit(InfoText2, (140, 440))
                    self.gameDisplay.blit(InfoText3, (140, 470))
                    self.gameDisplay.blit(InfoText4, (140, 500))

                    self.gameDisplay.blit(self.PicGeburt, (PicX, PicY))
                    PicSizeX = int(InfoBoxPicY * (162/200))
                    PicSizeY = InfoBoxPicY

                    if "Team"+str(star['team']) == self.yourTeam:
                        HealIcon = self.loadImage("Pictures/plus_icon.png", size=(int(InfoBoxIconSize), int(InfoBoxIconSize)))
                        self.HealIconSurface = self.gameDisplay.blit(HealIcon, (500, 550))

                        NextIcon = self.loadImage("Pictures/ic_fast_forward_white_48dp_1x.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                        self.NextIconSurface = self.gameDisplay.blit(NextIcon, (700, 550))

                        if healErrorStrahlung == True:
                            StrahlungErrorText = self.MainFontMiddle.render("Nicht genug Strahlung", True, red)
                            self.gameDisplay.blit(StrahlungErrorText, (475, 610))
                            if self.yourTeam == "Team1":
                                if self.strahlungTeam1 >= 2000000:
                                    healErrorStrahlung = False
                            elif self.yourTeam == "Team2" and self.strahlungTeam2 >= 2000000:
                                healErrorStrahlung = False

                elif star["cat"] == "Geburt" and InfoFlag:
                    InfoTextString = "Das Hertzsprung-Russel-Diagramm, kurz HRD wurde 1913 von dem amerikanischen Astronomen Henry Norris Russel auf Grundlage der Erkenntnisse des dänischen Astronomen Ejnar Hertzsprung weiterentwickelt und veröffentlicht. Das HRD zeigt die Entwicklungsverteilung der Sterne, indem die Spektralklasse, also die Temperatur eines Sterns gegen die absolute Helligkeit abgetragen wird. Dadurch ergeben sich linienartige Häufungen, an denen man das Entwicklungsstadium eines Sterns ablesen kann.    Das Hertzsprung-Russel-Diagramm ist entlang der X-Achse in die Spektralkassen O, B, A, F, G, K, M, L und T eingeteilt. Die Spektralklassen geben Aufschluss über die Temperatur eines Sterns. Die Temperatur sinkt von der Spektralklasse O bis zur Spektralklasse T. Weiterhin kann man von der Spektralklasse auch auf charakteristische Brennstoffe schließen. So enthalten Sterne der Spektralklasse M neben den Hauptbrennstoffen Helium und Wasserstoff zusätzlich Titanoxid. Auf der Y-Achse des Hertzsprung-Russel-Diagramms ist die absolute Helligkeit eines Sterns abgetragen. Die absolute Helligkeit gibt die Leuchtkraft eines Sterns aus einer Entfernung 10 Parsec in Magnituden(mag) an und dient dazu, dass man die tatsächliche Helligkeit von Sternen vergleichen kann. Bei der absoluten Helligkeit gilt, je kleiner der Zahlenwert in mag, desto größer die Leuchtkraft. Das Hertzsprung-Russel-Diagramm lässt sich in charakteristische Bereiche unterteilen. Die meisten Sterne befinden sich in der Hauptreihe und werden auch Zwerge genannt, hierzu gehört auch unsere Sonne. Die Hauptreihe zieht sich von den Sternen der Spektralklasse O mit einer absoluten Helligkeit von -6 mag bis zu den Sternen der Spektralklasse M mit einer absoluten Helligkeit von 9-16 mag. Ein weiterer signifikanter Bereich ist der Riesenast. Der Riesenast umfasst Sterne der Spektralklassen G-M im Vergleich zu Sternen der Hauptreihe mit gleicher Spektralklasse besitzen sie eine größere absolute Helligkeit und damit eine größere leuchtende Oberfläche. Demzufolge haben sie einen größeren Durchmesser und werden oft Riesen genannt. Zwischen der Hauptreihe und dem Riesenast befinden sich die Unterriesen und über den Riesen gibt es noch die hellen Riesen, Überriesen und Hyperriesen. Weiterhin gibt es links oberhalb der Hauptreihe im Bereich der Spektralklassen A-G die Hertzsprung-Lücke, in der sich sehr wenige Sterne befinden. Die Hertzsprung-Lücke kommt dadurch zustande, dass massereiche Sterne nur kurze Zeit brauchen bis sie zu Riesen werden und im Riesenast aufgehen. Außerdem gibt es noch die Unterzwerge, die sich unter der Hauptreihe befinden und in der linken unteren Ecke die weißen Zwerge. Zudem schließen sich rechts unten an die Hauptreihe die roten Zwerge und daran wiederum die braunen Zwerge."
                    InfoTextArray = InfoTextString.split()
                    y = 10
                    holder = ""
                    InfoTextSurface = pygame.surface.Surface((720, 2000), pygame.SRCALPHA, 32)
                    InfoTextSurface.fill((0,0,0,0))

                    for word in InfoTextArray:
                        if self.MainFontSmall.size(holder + " " + word)[0] < 720:
                            holder = holder  + " " + word
                        else:
                            InfoTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            #print(holder)
                            holder = word
                    HolderSurface = pygame.surface.Surface((720, 250), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(InfoTextSurface, (0, 0 + scroll_y))
                    self.gameDisplay.blit(HolderSurface, (140, 380))

                    self.gameDisplay.blit(self.HRD_UnDef, (PicX, PicY))
                    PicSizeX = int(150 * 150/178)
                    PicSizeY = 150

                elif star["cat"] == "Hauptreihe" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("In dieser Phase verbringen Sterne den Großeil ihres Lebens. In", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("der Hauptreihenphase verbrennen sie kontinuierlich Wasserstoff", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("zu Helium. Wie lange sie das tun, hängt von ihrer Masse ab:", True, text_color)
                    InfoText3 = self.MainFontMiddle.render("leichte Sterne verbrennen weniger Wasserstoff und sind länger in", True, text_color)
                    InfoText4 = self.MainFontMiddle.render("der Hauptreihe zu finden als schwere Sterne.", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 380))
                    self.gameDisplay.blit(InfoText1, (140, 410))
                    self.gameDisplay.blit(InfoText2, (140, 440))
                    self.gameDisplay.blit(InfoText3, (140, 470))
                    self.gameDisplay.blit(InfoText4, (140, 500))

                    self.gameDisplay.blit(self.PicHauptreihe, (PicX, PicY))
                    PicSizeX = InfoBoxPicX
                    PicSizeY = InfoBoxPicY

                    if "Team"+str(star['team']) == self.yourTeam:
                        p = False
                        for attack in self.Attacks:
                            if attack["Angreifer"] == star["name"] or attack["Verteidiger"] == star["name"]:
                                p = True
                                break
                        if not p:
                            AttackIcon = self.loadImage("Pictures/sword_white.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                            self.AttackIconSurface = self.gameDisplay.blit(AttackIcon, (300, 550))
                        else:
                            self.BombIconSurface = self.gameDisplay.blit(self.BombIcon, (300, 550))

                        HealIcon = self.loadImage("Pictures/plus_icon.png", size=(int(InfoBoxIconSize), int(InfoBoxIconSize)))
                        self.HealIconSurface = self.gameDisplay.blit(HealIcon, (500, 550))

                        NextIcon = self.loadImage("Pictures/ic_fast_forward_white_48dp_1x.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                        self.NextIconSurface = self.gameDisplay.blit(NextIcon, (700, 550))

                        if healErrorStrahlung == True:
                            StrahlungErrorText = self.MainFontMiddle.render("Nicht genug Strahlung", True, red)
                            self.gameDisplay.blit(StrahlungErrorText, (475, 610))
                            if self.yourTeam == "Team1":
                                if self.strahlungTeam1 >= 2000000:
                                    healErrorStrahlung = False
                            elif self.yourTeam == "Team2" and self.strahlungTeam2 >= 2000000:
                                healErrorStrahlung = False

                elif star["cat"] == "Hauptreihe" and InfoFlag:
                    InfoTextString = "Das Hertzsprung-Russel-Diagramm, kurz HRD wurde 1913 von dem amerikanischen Astronomen Henry Norris Russel auf Grundlage der Erkenntnisse des dänischen Astronomen Ejnar Hertzsprung weiterentwickelt und veröffentlicht. Das HRD zeigt die Entwicklungsverteilung der Sterne, indem die Spektralklasse, also die Temperatur eines Sterns gegen die absolute Helligkeit abgetragen wird. Dadurch ergeben sich linienartige Häufungen, an denen man das Entwicklungsstadium eines Sterns ablesen kann.    Das Hertzsprung-Russel-Diagramm ist entlang der X-Achse in die Spektralkassen O, B, A, F, G, K, M, L und T eingeteilt. Die Spektralklassen geben Aufschluss über die Temperatur eines Sterns. Die Temperatur sinkt von der Spektralklasse O bis zur Spektralklasse T. Weiterhin kann man von der Spektralklasse auch auf charakteristische Brennstoffe schließen. So enthalten Sterne der Spektralklasse M neben den Hauptbrennstoffen Helium und Wasserstoff zusätzlich Titanoxid. Auf der Y-Achse des Hertzsprung-Russel-Diagramms ist die absolute Helligkeit eines Sterns abgetragen. Die absolute Helligkeit gibt die Leuchtkraft eines Sterns aus einer Entfernung 10 Parsec in Magnituden(mag) an und dient dazu, dass man die tatsächliche Helligkeit von Sternen vergleichen kann. Bei der absoluten Helligkeit gilt, je kleiner der Zahlenwert in mag, desto größer die Leuchtkraft. Das Hertzsprung-Russel-Diagramm lässt sich in charakteristische Bereiche unterteilen. Die meisten Sterne befinden sich in der Hauptreihe und werden auch Zwerge genannt, hierzu gehört auch unsere Sonne. Die Hauptreihe zieht sich von den Sternen der Spektralklasse O mit einer absoluten Helligkeit von -6 mag bis zu den Sternen der Spektralklasse M mit einer absoluten Helligkeit von 9-16 mag. Ein weiterer signifikanter Bereich ist der Riesenast. Der Riesenast umfasst Sterne der Spektralklassen G-M im Vergleich zu Sternen der Hauptreihe mit gleicher Spektralklasse besitzen sie eine größere absolute Helligkeit und damit eine größere leuchtende Oberfläche. Demzufolge haben sie einen größeren Durchmesser und werden oft Riesen genannt. Zwischen der Hauptreihe und dem Riesenast befinden sich die Unterriesen und über den Riesen gibt es noch die hellen Riesen, Überriesen und Hyperriesen. Weiterhin gibt es links oberhalb der Hauptreihe im Bereich der Spektralklassen A-G die Hertzsprung-Lücke, in der sich sehr wenige Sterne befinden. Die Hertzsprung-Lücke kommt dadurch zustande, dass massereiche Sterne nur kurze Zeit brauchen bis sie zu Riesen werden und im Riesenast aufgehen. Außerdem gibt es noch die Unterzwerge, die sich unter der Hauptreihe befinden und in der linken unteren Ecke die weißen Zwerge. Zudem schließen sich rechts unten an die Hauptreihe die roten Zwerge und daran wiederum die braunen Zwerge."
                    InfoTextArray = InfoTextString.split()
                    y = 10
                    holder = ""
                    InfoTextSurface = pygame.surface.Surface((720, 2000), pygame.SRCALPHA, 32)
                    InfoTextSurface.fill((0,0,0,0))

                    for word in InfoTextArray:
                        if self.MainFontSmall.size(holder + " " + word)[0] < 720:
                            holder = holder  + " " + word
                        else:
                            InfoTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            #print(holder)
                            holder = word
                    HolderSurface = pygame.surface.Surface((720, 250), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(InfoTextSurface, (0, 0 + scroll_y))
                    self.gameDisplay.blit(HolderSurface, (140, 380))

                    self.gameDisplay.blit(self.HRD_Hauptreihe, (PicX, PicY))
                    PicSizeX = 150
                    PicSizeY = 146

                elif star["cat"] == "Zwerg" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("Unter all den Sternen die es gibt, ist dieser sehr klein. Vor langer", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("Zeit endeten in ihm die Fusionsreaktionen und zurück blieb ein heißer,", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("dichter Klumpen von verbrauchtem Brennstoff und höheren Metallen.", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 380))
                    self.gameDisplay.blit(InfoText1, (140, 410))
                    self.gameDisplay.blit(InfoText2, (140, 440))

                    self.gameDisplay.blit(self.PicZwerg, (PicX, PicY))
                    PicSizeX = InfoBoxPicX
                    PicSizeY = InfoBoxPicY

                    if "Team"+str(star['team']) == self.yourTeam:
                        p = False
                        for attack in self.Attacks:
                            if attack["Angreifer"] == star["name"] or attack["Verteidiger"] == star["name"]:
                                p = True
                                break
                        if not p:
                            AttackIcon = self.loadImage("Pictures/sword_white.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                            self.AttackIconSurface = self.gameDisplay.blit(AttackIcon, (300, 550))
                        else:
                            self.BombIconSurface = self.gameDisplay.blit(self.BombIcon, (300, 550))

                        HealIcon = self.loadImage("Pictures/plus_icon.png", size=(int(InfoBoxIconSize), int(InfoBoxIconSize)))
                        self.HealIconSurface = self.gameDisplay.blit(HealIcon, (500, 550))

                        NextIcon = self.loadImage("Pictures/ic_fast_forward_white_48dp_1x.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                        self.NextIconSurface = self.gameDisplay.blit(NextIcon, (700, 550))

                        if healErrorStrahlung == True:
                            StrahlungErrorText = self.MainFontMiddle.render("Nicht genug Strahlung", True, red)
                            self.gameDisplay.blit(StrahlungErrorText, (475, 610))
                            if self.yourTeam == "Team1":
                                if self.strahlungTeam1 >= 2000000:
                                    healErrorStrahlung = False
                            elif self.yourTeam == "Team2" and self.strahlungTeam2 >= 2000000:
                                healErrorStrahlung = False

                elif star["cat"] == "Zwerg" and InfoFlag:
                    InfoTextString = "Das Hertzsprung-Russel-Diagramm, kurz HRD wurde 1913 von dem amerikanischen Astronomen Henry Norris Russel auf Grundlage der Erkenntnisse des dänischen Astronomen Ejnar Hertzsprung weiterentwickelt und veröffentlicht. Das HRD zeigt die Entwicklungsverteilung der Sterne, indem die Spektralklasse, also die Temperatur eines Sterns gegen die absolute Helligkeit abgetragen wird. Dadurch ergeben sich linienartige Häufungen, an denen man das Entwicklungsstadium eines Sterns ablesen kann.    Das Hertzsprung-Russel-Diagramm ist entlang der X-Achse in die Spektralkassen O, B, A, F, G, K, M, L und T eingeteilt. Die Spektralklassen geben Aufschluss über die Temperatur eines Sterns. Die Temperatur sinkt von der Spektralklasse O bis zur Spektralklasse T. Weiterhin kann man von der Spektralklasse auch auf charakteristische Brennstoffe schließen. So enthalten Sterne der Spektralklasse M neben den Hauptbrennstoffen Helium und Wasserstoff zusätzlich Titanoxid. Auf der Y-Achse des Hertzsprung-Russel-Diagramms ist die absolute Helligkeit eines Sterns abgetragen. Die absolute Helligkeit gibt die Leuchtkraft eines Sterns aus einer Entfernung 10 Parsec in Magnituden(mag) an und dient dazu, dass man die tatsächliche Helligkeit von Sternen vergleichen kann. Bei der absoluten Helligkeit gilt, je kleiner der Zahlenwert in mag, desto größer die Leuchtkraft. Das Hertzsprung-Russel-Diagramm lässt sich in charakteristische Bereiche unterteilen. Die meisten Sterne befinden sich in der Hauptreihe und werden auch Zwerge genannt, hierzu gehört auch unsere Sonne. Die Hauptreihe zieht sich von den Sternen der Spektralklasse O mit einer absoluten Helligkeit von -6 mag bis zu den Sternen der Spektralklasse M mit einer absoluten Helligkeit von 9-16 mag. Ein weiterer signifikanter Bereich ist der Riesenast. Der Riesenast umfasst Sterne der Spektralklassen G-M im Vergleich zu Sternen der Hauptreihe mit gleicher Spektralklasse besitzen sie eine größere absolute Helligkeit und damit eine größere leuchtende Oberfläche. Demzufolge haben sie einen größeren Durchmesser und werden oft Riesen genannt. Zwischen der Hauptreihe und dem Riesenast befinden sich die Unterriesen und über den Riesen gibt es noch die hellen Riesen, Überriesen und Hyperriesen. Weiterhin gibt es links oberhalb der Hauptreihe im Bereich der Spektralklassen A-G die Hertzsprung-Lücke, in der sich sehr wenige Sterne befinden. Die Hertzsprung-Lücke kommt dadurch zustande, dass massereiche Sterne nur kurze Zeit brauchen bis sie zu Riesen werden und im Riesenast aufgehen. Außerdem gibt es noch die Unterzwerge, die sich unter der Hauptreihe befinden und in der linken unteren Ecke die weißen Zwerge. Zudem schließen sich rechts unten an die Hauptreihe die roten Zwerge und daran wiederum die braunen Zwerge."
                    InfoTextArray = InfoTextString.split()
                    y = 10
                    holder = ""
                    InfoTextSurface = pygame.surface.Surface((720, 2000), pygame.SRCALPHA, 32)
                    InfoTextSurface.fill((0,0,0,0))

                    for word in InfoTextArray:
                        if self.MainFontSmall.size(holder + " " + word)[0] < 720:
                            holder = holder  + " " + word
                        else:
                            InfoTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            #print(holder)
                            holder = word
                    HolderSurface = pygame.surface.Surface((720, 250), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(InfoTextSurface, (0, 0 + scroll_y))
                    self.gameDisplay.blit(HolderSurface, (140, 380))

                    self.gameDisplay.blit(self.HRD_Zwerge, (PicX, PicY))
                    PicSizeX = 150
                    PicSizeY = 146

                elif star["cat"] == "Riese" and not InfoFlag or star["cat"] == "Hyperriese" and not InfoFlag or star["cat"] == "Überriese" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("Bei diesem Stern neigt sich das Leben langsam aber sicher dem", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("Ende zu. Während in der äußeren, aufgeblähten Schale noch", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("Wasserstoff verbrannt wird, bilden sich im Kern schwerere", True, text_color)
                    InfoText3 = self.MainFontMiddle.render("Stoffe als Helium, sogenannte Metalle.", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 380))
                    self.gameDisplay.blit(InfoText1, (140, 410))
                    self.gameDisplay.blit(InfoText2, (140, 440))
                    self.gameDisplay.blit(InfoText3, (140, 470))

                    self.gameDisplay.blit(self.PicRiese, (PicX, PicY))
                    PicSizeX = InfoBoxPicX
                    PicSizeY = InfoBoxPicY

                    if "Team"+str(star['team']) == self.yourTeam:
                        p = False
                        for attack in self.Attacks:
                            if attack["Angreifer"] == star["name"] or attack["Verteidiger"] == star["name"]:
                                p = True
                                break
                        if not p:
                            AttackIcon = self.loadImage("Pictures/sword_white.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                            self.AttackIconSurface = self.gameDisplay.blit(AttackIcon, (300, 550))
                        else:
                            self.BombIconSurface = self.gameDisplay.blit(self.BombIcon, (300, 550))

                        HealIcon = self.loadImage("Pictures/plus_icon.png", size=(int(InfoBoxIconSize), int(InfoBoxIconSize)))
                        self.HealIconSurface = self.gameDisplay.blit(HealIcon, (500, 550))

                        NextIcon = self.loadImage("Pictures/ic_fast_forward_white_48dp_1x.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                        self.NextIconSurface = self.gameDisplay.blit(NextIcon, (700, 550))

                        if healErrorStrahlung == True:
                            StrahlungErrorText = self.MainFontMiddle.render("Nicht genug Strahlung", True, red)
                            self.gameDisplay.blit(StrahlungErrorText, (475, 610))
                            if self.yourTeam == "Team1":
                                if self.strahlungTeam1 >= 2000000:
                                    healErrorStrahlung = False
                            elif self.yourTeam == "Team2" and self.strahlungTeam2 >= 2000000:
                                healErrorStrahlung = False

                elif star["cat"] == "Riese" and InfoFlag or star["cat"] == "Hyperriese" and InfoFlag or star["cat"] == "Überriese" and InfoFlag:
                    InfoTextString = "Das Hertzsprung-Russel-Diagramm, kurz HRD wurde 1913 von dem amerikanischen Astronomen Henry Norris Russel auf Grundlage der Erkenntnisse des dänischen Astronomen Ejnar Hertzsprung weiterentwickelt und veröffentlicht. Das HRD zeigt die Entwicklungsverteilung der Sterne, indem die Spektralklasse, also die Temperatur eines Sterns gegen die absolute Helligkeit abgetragen wird. Dadurch ergeben sich linienartige Häufungen, an denen man das Entwicklungsstadium eines Sterns ablesen kann.    Das Hertzsprung-Russel-Diagramm ist entlang der X-Achse in die Spektralkassen O, B, A, F, G, K, M, L und T eingeteilt. Die Spektralklassen geben Aufschluss über die Temperatur eines Sterns. Die Temperatur sinkt von der Spektralklasse O bis zur Spektralklasse T. Weiterhin kann man von der Spektralklasse auch auf charakteristische Brennstoffe schließen. So enthalten Sterne der Spektralklasse M neben den Hauptbrennstoffen Helium und Wasserstoff zusätzlich Titanoxid. Auf der Y-Achse des Hertzsprung-Russel-Diagramms ist die absolute Helligkeit eines Sterns abgetragen. Die absolute Helligkeit gibt die Leuchtkraft eines Sterns aus einer Entfernung 10 Parsec in Magnituden(mag) an und dient dazu, dass man die tatsächliche Helligkeit von Sternen vergleichen kann. Bei der absoluten Helligkeit gilt, je kleiner der Zahlenwert in mag, desto größer die Leuchtkraft. Das Hertzsprung-Russel-Diagramm lässt sich in charakteristische Bereiche unterteilen. Die meisten Sterne befinden sich in der Hauptreihe und werden auch Zwerge genannt, hierzu gehört auch unsere Sonne. Die Hauptreihe zieht sich von den Sternen der Spektralklasse O mit einer absoluten Helligkeit von -6 mag bis zu den Sternen der Spektralklasse M mit einer absoluten Helligkeit von 9-16 mag. Ein weiterer signifikanter Bereich ist der Riesenast. Der Riesenast umfasst Sterne der Spektralklassen G-M im Vergleich zu Sternen der Hauptreihe mit gleicher Spektralklasse besitzen sie eine größere absolute Helligkeit und damit eine größere leuchtende Oberfläche. Demzufolge haben sie einen größeren Durchmesser und werden oft Riesen genannt. Zwischen der Hauptreihe und dem Riesenast befinden sich die Unterriesen und über den Riesen gibt es noch die hellen Riesen, Überriesen und Hyperriesen. Weiterhin gibt es links oberhalb der Hauptreihe im Bereich der Spektralklassen A-G die Hertzsprung-Lücke, in der sich sehr wenige Sterne befinden. Die Hertzsprung-Lücke kommt dadurch zustande, dass massereiche Sterne nur kurze Zeit brauchen bis sie zu Riesen werden und im Riesenast aufgehen. Außerdem gibt es noch die Unterzwerge, die sich unter der Hauptreihe befinden und in der linken unteren Ecke die weißen Zwerge. Zudem schließen sich rechts unten an die Hauptreihe die roten Zwerge und daran wiederum die braunen Zwerge."
                    InfoTextArray = InfoTextString.split()
                    y = 10
                    holder = ""
                    InfoTextSurface = pygame.surface.Surface((720, 2000), pygame.SRCALPHA, 32)
                    InfoTextSurface.fill((0,0,0,0))

                    for word in InfoTextArray:
                        if self.MainFontSmall.size(holder + " " + word)[0] < 720:
                            holder = holder  + " " + word
                        else:
                            InfoTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            #print(holder)
                            holder = word
                    HolderSurface = pygame.surface.Surface((720, 250), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(InfoTextSurface, (0, 0 + scroll_y))
                    self.gameDisplay.blit(HolderSurface, (140, 380))

                    if star["mass"] >= 10:
                        self.gameDisplay.blit(self.HRD_Riese_schwer, (PicX, PicY))
                        PicSizeX = 150
                        PicSizeY = 146
                    else:
                        self.gameDisplay.blit(self.HRD_Riese, (PicX, PicY))
                        PicSizeX = 150
                        PicSizeY = 146

                elif star["cat"] == "Neutronenstern" and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("An der Grenze zum Möglichen schwebt dieser Neutronenstern. Er", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("besteht fast nur noch aus Neutronen, die dichter als Atom-", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("kerne sind. Die Neutronensterne sind das Endstadium massereicher", True, text_color)
                    InfoText3 = self.MainFontMiddle.render("Sterne. Nur wenig fehlt, und die Neutronensterne wären schwarze", True, text_color)
                    InfoText4 = self.MainFontMiddle.render("Löcher", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 380))
                    self.gameDisplay.blit(InfoText1, (140, 410))
                    self.gameDisplay.blit(InfoText2, (140, 440))
                    self.gameDisplay.blit(InfoText3, (140, 470))
                    self.gameDisplay.blit(InfoText4, (140, 500))

                    self.gameDisplay.blit(self.PicNeutronenstern, (PicX, PicY))
                    PicSizeX = int(InfoBoxPicY + (357/200))
                    PicSizeY = InfoBoxPicY

                    if "Team"+str(star['team']) == self.yourTeam:
                        p = False
                        for attack in self.Attacks:
                            if attack["Angreifer"] == star["name"] or attack["Verteidiger"] == star["name"]:
                                p = True
                                break
                        if not p:
                            AttackIcon = self.loadImage("Pictures/sword_white.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                            self.AttackIconSurface = self.gameDisplay.blit(AttackIcon, (300, 550))
                        else:
                            self.BombIconSurface = self.gameDisplay.blit(self.BombIcon, (300, 550))

                        HealIcon = self.loadImage("Pictures/plus_icon.png", size=(int(InfoBoxIconSize), int(InfoBoxIconSize)))
                        self.HealIconSurface = self.gameDisplay.blit(HealIcon, (500, 550))

                        NextIcon = self.loadImage("Pictures/ic_fast_forward_white_48dp_1x.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                        self.NextIconSurface = self.gameDisplay.blit(NextIcon, (700, 550))

                        if healErrorStrahlung == True:
                            StrahlungErrorText = self.MainFontMiddle.render("Nicht genug Strahlung", True, red)
                            self.gameDisplay.blit(StrahlungErrorText, (475, 610))
                            if self.yourTeam == "Team1":
                                if self.strahlungTeam1 >= 2000000:
                                    healErrorStrahlung = False
                            elif self.yourTeam == "Team2" and self.strahlungTeam2 >= 2000000:
                                healErrorStrahlung = False

                elif star["cat"] == "Neutronenstern" and InfoFlag:
                    InfoTextString = "Das Hertzsprung-Russel-Diagramm, kurz HRD wurde 1913 von dem amerikanischen Astronomen Henry Norris Russel auf Grundlage der Erkenntnisse des dänischen Astronomen Ejnar Hertzsprung weiterentwickelt und veröffentlicht. Das HRD zeigt die Entwicklungsverteilung der Sterne, indem die Spektralklasse, also die Temperatur eines Sterns gegen die absolute Helligkeit abgetragen wird. Dadurch ergeben sich linienartige Häufungen, an denen man das Entwicklungsstadium eines Sterns ablesen kann.    Das Hertzsprung-Russel-Diagramm ist entlang der X-Achse in die Spektralkassen O, B, A, F, G, K, M, L und T eingeteilt. Die Spektralklassen geben Aufschluss über die Temperatur eines Sterns. Die Temperatur sinkt von der Spektralklasse O bis zur Spektralklasse T. Weiterhin kann man von der Spektralklasse auch auf charakteristische Brennstoffe schließen. So enthalten Sterne der Spektralklasse M neben den Hauptbrennstoffen Helium und Wasserstoff zusätzlich Titanoxid. Auf der Y-Achse des Hertzsprung-Russel-Diagramms ist die absolute Helligkeit eines Sterns abgetragen. Die absolute Helligkeit gibt die Leuchtkraft eines Sterns aus einer Entfernung 10 Parsec in Magnituden(mag) an und dient dazu, dass man die tatsächliche Helligkeit von Sternen vergleichen kann. Bei der absoluten Helligkeit gilt, je kleiner der Zahlenwert in mag, desto größer die Leuchtkraft. Das Hertzsprung-Russel-Diagramm lässt sich in charakteristische Bereiche unterteilen. Die meisten Sterne befinden sich in der Hauptreihe und werden auch Zwerge genannt, hierzu gehört auch unsere Sonne. Die Hauptreihe zieht sich von den Sternen der Spektralklasse O mit einer absoluten Helligkeit von -6 mag bis zu den Sternen der Spektralklasse M mit einer absoluten Helligkeit von 9-16 mag. Ein weiterer signifikanter Bereich ist der Riesenast. Der Riesenast umfasst Sterne der Spektralklassen G-M im Vergleich zu Sternen der Hauptreihe mit gleicher Spektralklasse besitzen sie eine größere absolute Helligkeit und damit eine größere leuchtende Oberfläche. Demzufolge haben sie einen größeren Durchmesser und werden oft Riesen genannt. Zwischen der Hauptreihe und dem Riesenast befinden sich die Unterriesen und über den Riesen gibt es noch die hellen Riesen, Überriesen und Hyperriesen. Weiterhin gibt es links oberhalb der Hauptreihe im Bereich der Spektralklassen A-G die Hertzsprung-Lücke, in der sich sehr wenige Sterne befinden. Die Hertzsprung-Lücke kommt dadurch zustande, dass massereiche Sterne nur kurze Zeit brauchen bis sie zu Riesen werden und im Riesenast aufgehen. Außerdem gibt es noch die Unterzwerge, die sich unter der Hauptreihe befinden und in der linken unteren Ecke die weißen Zwerge. Zudem schließen sich rechts unten an die Hauptreihe die roten Zwerge und daran wiederum die braunen Zwerge."
                    InfoTextArray = InfoTextString.split()
                    y = 10
                    holder = ""
                    InfoTextSurface = pygame.surface.Surface((720, 2000), pygame.SRCALPHA, 32)
                    InfoTextSurface.fill((0,0,0,0))

                    for word in InfoTextArray:
                        if self.MainFontSmall.size(holder + " " + word)[0] < 720:
                            holder = holder  + " " + word
                        else:
                            InfoTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            #print(holder)
                            holder = word
                    HolderSurface = pygame.surface.Surface((720, 250), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(InfoTextSurface, (0, 0 + scroll_y))
                    self.gameDisplay.blit(HolderSurface, (140, 380))

                    self.gameDisplay.blit(self.HRD_UnDef, (PicX, PicY))
                    PicSizeX = int(150 * 150/178)
                    PicSizeY = 150

                elif (star["cat"] == "Schwarzes Loch" or star["cat"] == "Weißes Loch") and not InfoFlag:
                    InfoText = self.MainFontMiddle.render("Nach einem langen und ereignisreichen Leben ist dieser Stern nicht", True, text_color)
                    InfoText1 = self.MainFontMiddle.render("nur zu einem Zwerg geworden, sondern war so dicht, dass er die", True, text_color)
                    InfoText2 = self.MainFontMiddle.render("ganze Raumzeit aus den Fugen gerissen hat. In einem sigulären", True, text_color)
                    InfoText3 = self.MainFontMiddle.render("Punkt vereint er Masse von unendlicher Dichte. Aus seinem Ereignis-", True, text_color)
                    InfoText4 = self.MainFontMiddle.render("horizont kann nciht einmal Licht entfliehen.Dies ist ein wahrer Gigant", True, text_color)
                    self.gameDisplay.blit(InfoText, (140, 380))
                    self.gameDisplay.blit(InfoText1, (140, 410))
                    self.gameDisplay.blit(InfoText2, (140, 440))
                    self.gameDisplay.blit(InfoText3, (140, 470))
                    self.gameDisplay.blit(InfoText4, (140, 500))

                    self.gameDisplay.blit(self.PicSchwarzesLoch, (PicX, PicY))
                    PicSizeX = int(InfoBoxPicY * (1166/1280))
                    PicSizeY = InfoBoxPicY

                    if "Team"+str(star['team']) == self.yourTeam:
                        p = False
                        for attack in self.Attacks:
                            if attack["Angreifer"] == star["name"] or attack["Verteidiger"] == star["name"]:
                                p = True
                                break
                        if not p:
                            AttackIcon = self.loadImage("Pictures/sword_white.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                            self.AttackIconSurface = self.gameDisplay.blit(AttackIcon, (300, 550))
                        else:
                            self.BombIconSurface = self.gameDisplay.blit(self.BombIcon, (300, 550))

                        HealIcon = self.loadImage("Pictures/plus_icon.png", size=(int(InfoBoxIconSize), int(InfoBoxIconSize)))
                        self.HealIconSurface = self.gameDisplay.blit(HealIcon, (500, 550))

                        NextIcon = self.loadImage("Pictures/ic_fast_forward_white_48dp_1x.png", size=(InfoBoxIconSize, InfoBoxIconSize))
                        self.NextIconSurface = self.gameDisplay.blit(NextIcon, (700, 550))

                        if healErrorStrahlung == True:
                            StrahlungErrorText = self.MainFontMiddle.render("Nicht genug Strahlung", True, red)
                            self.gameDisplay.blit(StrahlungErrorText, (475, 610))
                            if self.yourTeam == "Team1":
                                if self.strahlungTeam1 >= 2000000:
                                    healErrorStrahlung = False
                            elif self.yourTeam == "Team2" and self.strahlungTeam2 >= 2000000:
                                healErrorStrahlung = False

                elif (star["cat"] == "Schwarzes Loch" or star["cat"] == "Weißes Loch") and InfoFlag:
                    InfoTextString = "Das Hertzsprung-Russel-Diagramm, kurz HRD wurde 1913 von dem amerikanischen Astronomen Henry Norris Russel auf Grundlage der Erkenntnisse des dänischen Astronomen Ejnar Hertzsprung weiterentwickelt und veröffentlicht. Das HRD zeigt die Entwicklungsverteilung der Sterne, indem die Spektralklasse, also die Temperatur eines Sterns gegen die absolute Helligkeit abgetragen wird. Dadurch ergeben sich linienartige Häufungen, an denen man das Entwicklungsstadium eines Sterns ablesen kann.    Das Hertzsprung-Russel-Diagramm ist entlang der X-Achse in die Spektralkassen O, B, A, F, G, K, M, L und T eingeteilt. Die Spektralklassen geben Aufschluss über die Temperatur eines Sterns. Die Temperatur sinkt von der Spektralklasse O bis zur Spektralklasse T. Weiterhin kann man von der Spektralklasse auch auf charakteristische Brennstoffe schließen. So enthalten Sterne der Spektralklasse M neben den Hauptbrennstoffen Helium und Wasserstoff zusätzlich Titanoxid. Auf der Y-Achse des Hertzsprung-Russel-Diagramms ist die absolute Helligkeit eines Sterns abgetragen. Die absolute Helligkeit gibt die Leuchtkraft eines Sterns aus einer Entfernung 10 Parsec in Magnituden(mag) an und dient dazu, dass man die tatsächliche Helligkeit von Sternen vergleichen kann. Bei der absoluten Helligkeit gilt, je kleiner der Zahlenwert in mag, desto größer die Leuchtkraft. Das Hertzsprung-Russel-Diagramm lässt sich in charakteristische Bereiche unterteilen. Die meisten Sterne befinden sich in der Hauptreihe und werden auch Zwerge genannt, hierzu gehört auch unsere Sonne. Die Hauptreihe zieht sich von den Sternen der Spektralklasse O mit einer absoluten Helligkeit von -6 mag bis zu den Sternen der Spektralklasse M mit einer absoluten Helligkeit von 9-16 mag. Ein weiterer signifikanter Bereich ist der Riesenast. Der Riesenast umfasst Sterne der Spektralklassen G-M im Vergleich zu Sternen der Hauptreihe mit gleicher Spektralklasse besitzen sie eine größere absolute Helligkeit und damit eine größere leuchtende Oberfläche. Demzufolge haben sie einen größeren Durchmesser und werden oft Riesen genannt. Zwischen der Hauptreihe und dem Riesenast befinden sich die Unterriesen und über den Riesen gibt es noch die hellen Riesen, Überriesen und Hyperriesen. Weiterhin gibt es links oberhalb der Hauptreihe im Bereich der Spektralklassen A-G die Hertzsprung-Lücke, in der sich sehr wenige Sterne befinden. Die Hertzsprung-Lücke kommt dadurch zustande, dass massereiche Sterne nur kurze Zeit brauchen bis sie zu Riesen werden und im Riesenast aufgehen. Außerdem gibt es noch die Unterzwerge, die sich unter der Hauptreihe befinden und in der linken unteren Ecke die weißen Zwerge. Zudem schließen sich rechts unten an die Hauptreihe die roten Zwerge und daran wiederum die braunen Zwerge."
                    InfoTextArray = InfoTextString.split()
                    y = 10
                    holder = ""
                    InfoTextSurface = pygame.surface.Surface((720, 2000), pygame.SRCALPHA, 32)
                    InfoTextSurface.fill((0,0,0,0))

                    for word in InfoTextArray:
                        if self.MainFontSmall.size(holder + " " + word)[0] < 720:
                            holder = holder  + " " + word
                        else:
                            InfoTextSurface.blit(self.MainFontSmall.render(holder, True, white), (10, y))
                            y += 20
                            #print(holder)
                            holder = word
                    HolderSurface = pygame.surface.Surface((720, 250), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(InfoTextSurface, (0, 0 + scroll_y))
                    self.gameDisplay.blit(HolderSurface, (140, 380))

                    self.gameDisplay.blit(self.HRD_UnDef, (PicX, PicY))
                    PicSizeX = int(150 * 150/178)
                    PicSizeY = 150


                pygame.draw.line(self.gameDisplay, white, (PicX - 10, PicY - 10), (PicX + 50, PicY - 10), 2)
                pygame.draw.line(self.gameDisplay, white, (PicX - 10, PicY - 10), (PicX - 10, PicY + 50), 2)

                pygame.draw.line(self.gameDisplay, white, (PicX - 10, PicY + PicSizeY - 50), (PicX - 10, PicY + PicSizeY + 10), 2)
                pygame.draw.line(self.gameDisplay, white, (PicX - 10, PicY + PicSizeY + 10), (PicX + 50, PicY + PicSizeY + 10), 2)

                pygame.draw.line(self.gameDisplay, white, (PicX + PicSizeX - 50, PicY - 10), (PicX + PicSizeX + 10, PicY - 10), 2)
                pygame.draw.line(self.gameDisplay, white, (PicX + PicSizeX + 10, PicY - 10), (PicX + PicSizeX + 10, PicY + 50), 2)

                pygame.draw.line(self.gameDisplay, white, (PicX + PicSizeX + 10, PicY + PicSizeY - 50), (PicX + PicSizeX + 10, PicY + PicSizeY + 10), 2)
                pygame.draw.line(self.gameDisplay, white, (PicX + PicSizeX - 50, PicY + PicSizeY + 10), (PicX + PicSizeX + 10, PicY + PicSizeY + 10), 2)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.gameExit = True

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button >= 4:
                        pos = pygame.mouse.get_pos()
                        if pos[0] > 140 and pos[0] < 860 and pos[1] > 380 and pos[1] < 630:
                            if event.button == 4: scroll_y = min(scroll_y + 15, 0)
                            if event.button == 5: scroll_y = max(scroll_y - 15, -2000)

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        p = False
                        for attack in self.Attacks:
                            if attack["Angreifer"] == star["name"] or attack["Verteidiger"] == star["name"]:
                                p = True
                                break
                        pos = pygame.mouse.get_pos()
                        if CloseIconSurface.collidepoint(pos):
                            self.infoBoxOpen = False
                            healErrorStrahlung = False
                        elif "Team"+str(star['team']) == self.yourTeam and star["cat"] != "Geburt" and not p and self.AttackIconSurface.collidepoint(pos):
                            self.infoBoxOpen = False
                            self.chooseAttackStar = True
                            self.AttackStar = self.infoBoxStar
                        elif "Team"+str(star['team']) == self.yourTeam and star["cat"] != "Geburt" and p and self.BombIconSurface.collidepoint(pos):
                            self.QBurst(star)
                        elif InfoIconSurface.collidepoint(pos):
                            if InfoFlag:
                                InfoFlag = False
                                scroll_y = 0
                            else:
                                InfoFlag = True
                        elif "Team"+str(star['team']) == self.yourTeam and self.HealIconSurface.collidepoint(pos):
                            if self.infoBoxStar["team"] == 1 and self.yourTeam == "Team1":
                                for star in self.starArrayTeam1:
                                    if star["name"] == self.infoBoxStar["name"]:
                                        if self.strahlungTeam1 > 2000000:
                                            healErrorStrahlung = False
                                            if self.techArrayTeam1["Kraft"][4]:
                                                mod = 8/5
                                            else:
                                                mod = 1


                                            if star["health"] < star["mass"] * 300 * mod:   #HealthFormel [für Suche]
                                                star["health"] = star["health"] + 100
                                               #print("Health Star nach heilung: ", star["health"])
                                                self.strahlungTeam1 -= 2000000
                                               #print("Stern wird geheilt: ", self.infoBoxStar["name"])
                                               #print(self.starArrayTeam1)
                                                v = '{"action": "starArrayTeam1", "data": ' + json.dumps(self.starArrayTeam1) + '}'
                                                v = v.encode('utf-8')
                                                self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
                                                v = '{"action": "Schaden", "data": {"schaden": -100, "stern": "' + star["name"] + '", "von": "' + star["name"] + '"}}'
                                                v = v.encode('utf-8')
                                                self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
                                            else:
                                                pass
                                               #print("Stern ist geheilt")
                                        else:
                                            pass
                                           #print("Nicht genug Strahlung")
                                            healErrorStrahlung = True
                                        break
                            elif self.infoBoxStar["team"] == 2 and self.yourTeam == "Team2":
                                for star in self.starArrayTeam2:
                                    if star["name"] == self.infoBoxStar["name"]:
                                        if self.strahlungTeam2 > 2000000:
                                           #print("Strahlung Team2: ", self.strahlungTeam2)
                                            healErrorStrahlung = False

                                            if self.techArrayTeam2["Kraft"][4]:
                                                mod = 8/5
                                            else:
                                                mod = 1

                                            if star["health"] < star["mass"] * 300 * mod:   #HealthFormel [für Suche]
                                                star["health"] = star["health"] + 100
                                               #print("Health Star nach Heilung: ", star["health"])
                                                self.strahlungTeam2 -= 2000000
                                                v = '{"action": "starArrayTeam2", "data": ' + json.dumps(self.starArrayTeam2) + '}'
                                                v = v.encode('utf-8')
                                                self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
                                                v = '{"action": "Schaden", "data": {"schaden": -100, "stern": "' + star["name"] + '", "von": "' + star["name"] + '"}}'
                                                v = v.encode('utf-8')
                                                self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
                                            else:
                                                self.showError("Stern ist geheilt")
                                        else:
                                           #print("Nicht genug Strahlung")
                                            healErrorStrahlung = True
                                        break
                        elif "Team"+str(star['team']) == self.yourTeam and self.NextIconSurface.collidepoint(pos):
                            if star["team"] == 1 and self.yourTeam == 'Team1':
                                if self.strahlungTeam1 >= 100000000:        #NextLevelCost
                                    for loopstar in self.starArrayTeam1:
                                        if loopstar["name"] == star["name"]:
                                            self.strahlungTeam1 -= 100000000    #NextLevelCost
                                            loopstar["nextLevel"] = 1
                                            star["nextLevel"]
                                            v = '{"action": "starArrayTeam1", "data": ' + json.dumps(self.starArrayTeam1) + '}'
                                            v = v.encode('utf-8')
                                            self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
                            elif star["team"] == 2 and self.yourTeam == "Team2":
                                if self.strahlungTeam2 >= 100000000:        #NextLevelCost
                                    for loopstar in self.starArrayTeam2:
                                        if loopstar["name"] == star["name"]:
                                            self.strahlungTeam2 -= 100000000
                                            loopstar["nextLevel"] = 1
                                            star["nextLevel"] = 1
                                            v = '{"action": "starArrayTeam2", "data": ' + json.dumps(self.starArrayTeam2) + '}'
                                            v = v.encode('utf-8')
                                            self.s.sendto(v, (self.gegnerHost, self.gegnerPort))



            if self.NewStarOpen == True and self.TechOpen == False:
                #self.NewStar = pygame.Surface((NewStarSizeX, NewStarSizeY))
                #self.NewStar.fill(NewStarColor)
                #self.NewStarHeaderText = self.MainFontMiddle.render("Neuen Stern kaufen", True, NewStarHeaderTextColor)
                #self.NewStarHeaderTextSurface = self.NewStar.blit(self.NewStarHeaderText, (NewStarHeaderTextX, NewStarHeaderTextY))
                #self.NewStarCloseIconSurface = self.NewStar.blit(self.CloseIcon, (NewStarCloseIconX, NewStarCloseIconY))

                ObenSizeX = 144
                UntenSizeX = 168
                SizeY = 60
                Diff = UntenSizeX - ObenSizeX

                text_color = white

                RahmenWeissObenLinksKlein = self.loadImage("Pictures/rahmen_weiß_oben_links.png", colorkey=(0,0,0), size=(ObenSizeX,SizeY))
                self.gameDisplay.blit(RahmenWeissObenLinksKlein, (100, 100))

                RahmenWeissObenRechtsKlein = self.loadImage("Pictures/rahmen_weiß_oben_rechts.png", colorkey=(0,0,0), size=(ObenSizeX, SizeY))
                self.gameDisplay.blit(RahmenWeissObenRechtsKlein, (display_x - 100 - ObenSizeX, 100))

                RahmenWeissUntenLinksKlein = self.loadImage("Pictures/rahmen_weiß_unten_links.png", colorkey=(0,0,0), size=(UntenSizeX, SizeY))
                self.gameDisplay.blit(RahmenWeissUntenLinksKlein, (100, display_y - 100 - SizeY))

                RahmenWeissUntenRechtsKlein = self.loadImage("Pictures/rahmen_weiß_unten_rechts.png", colorkey=(0,0,0), size=(UntenSizeX, SizeY))
                self.gameDisplay.blit(RahmenWeissUntenRechtsKlein, (display_x - 100 - ObenSizeX - Diff, display_y - 100 - SizeY))

                #pygame.draw.line(self.gameDisplay, white, (100, 100), (900, 100), 2)
                pygame.draw.rect(self.gameDisplay, white, (100 + ObenSizeX, 100, (display_x - 100 - ObenSizeX) - (100 + ObenSizeX), 20))    #Oben
                pygame.draw.rect(self.gameDisplay, white, (100 + UntenSizeX, display_y - 100 - 9, (display_x - 100 - UntenSizeX) - (100 + UntenSizeX), 3))  #Unten
                pygame.draw.rect(self.gameDisplay, white, (100 + 4, 100 + SizeY, 2, (display_y - 100 - SizeY) - (100 + SizeY) + 1)) #Links
                pygame.draw.rect(self.gameDisplay, white, (display_x - 100 - 6, 100 + SizeY, 2, (display_y - 100 - SizeY) - (100 + SizeY) + 1))

                pygame.gfxdraw.filled_polygon(self.gameDisplay, [(110, 110), (display_x - 110, 110), (display_x - 110, display_y - 110), (110, display_y - 110)], (255,255,255,50))

                NewStarHeaderText = self.MainFont.render("Neuen Stern kaufen", True, text_color)
                NewStarHeaderTextSurface = self.gameDisplay.blit(NewStarHeaderText, (350, 150))

                NewStarCloseIcon = self.loadImage("Pictures/ic_close_white_48dp_1x.png", size=(48, 48))
                NewStarCloseIconSurface = self.gameDisplay.blit(NewStarCloseIcon, (840, 125))

                if self.NameSchonVergeben:
                    NameErrorText = self.MainFontMiddle.render("Name schon vergeben", True, red)
                    self.gameDisplay.blit(NameErrorText, (200, 350))

                if self.nameEingeben == 0:   #Noch nichts eingeben
                    self.NewStarNameText = self.MainFontMiddle.render("Namen eingeben", True, text_color)
                elif self.nameEingeben == 1: #Beim eingeben
                    self.NewStarNameText = self.MainFontMiddle.render(self.nameString, True, text_color)
                    if self.nameFlag <= 3:
                        pygame.draw.line(self.gameDisplay, text_color, (180 + self.MainFontMiddle.size(self.nameString)[0], 300), (180 + self.MainFontMiddle.size(self.nameString)[0], 300 + self.MainFontMiddle.size(self.nameString)[1]), 2)
                        self.nameFlag = self.nameFlag + 1
                    elif self.nameFlag > 3 and self.nameFlag < 5:
                        self.nameFlag = self.nameFlag + 1
                    elif self.nameFlag == 5:
                        self.nameFlag = 0
                elif self.nameEingeben == 2:    #fertig mit eingeben
                    self.NewStarNameText = self.MainFontMiddle.render(self.nameString, True, text_color)
                self.NewStarNameSurface = self.gameDisplay.blit(self.NewStarNameText, (180, 300))
                if self.yourTeam == "Team1":
                    if self.techArrayTeam1["Perfektion"][4] == True:
                        self.NewStarMass = 0.01 + (self.NewStarSizeCord - 175) * (19.99 / (825 - 175))  #zischen 0.3 und 20 bzw wenn freigeschalten zwischen 0.01 und 20
                    else:
                        self.NewStarMass = 0.3 + (self.NewStarSizeCord - 175) * (19.7 / (650))
                else:
                    if self.techArrayTeam2["Perfektion"][4]:
                        self.NewStarMass = 0.01 + (self.NewStarSizeCord - 175) * (19.99 / (650))
                    else:
                        self.NewStarMass = 0.3 + (self.NewStarSizeCord - 175) * (19.7 / (650))
                self.NewStarCost = int(round(self.NewStarMass * 500000))
                string = "Größe wählen: " + str(round(self.NewStarMass, 1)) + " Sonnenmassen"
                self.NewStarSizeText = self.MainFontMiddle.render(string, True, text_color)
                self.NewStarSizeTextSurface = self.gameDisplay.blit(self.NewStarSizeText, (180, 425))
                pygame.draw.line(self.gameDisplay, text_color, (175, 400), (825, 400), 4)
                teamColor = team1_color
                if self.yourTeam == "Team1":
                    teamColor == team1_color
                elif self.yourTeam == "Team2":
                    teamColor == team2_color
                pygame.draw.circle(self.gameDisplay, teamColor, (self.NewStarSizeCord,  400), NewStarSizeSliderCircleSize)
                self.NewStarCostText = self.MainFontMiddle.render("Kosten: " + str(round(self.NewStarCost/1000000, 1)) + " Mio. Strahlung", True, text_color)
                self.NewStarCostTextSurface = self.gameDisplay.blit(self.NewStarCostText, (180, 455))


                self.NewStarOkText = self.MainFont.render("OK", True, text_color)
                self.NewStarOkTextSurface = self.gameDisplay.blit(self.NewStarOkText, (825,575))

                #self.NewStarSurface = self.gameDisplay.blit(self.NewStar, (display_x / 2 - NewStarSizeX / 2, display_y / 2 - NewStarSizeY, NewStarSizeX, NewStarSizeY))
                self.NewStarBuild = True

            if self.showErrorOpen == True:
                self.showError(self.showErrorString)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ConnectionFlag = False
                    pygame.quit()
                    quit()
                    self.quit = True
                if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_q:
                    #    self.gameExit = True
                    if self.NewStarOpen == True and self.nameEingeben == 1: #TODO: Sonderzeichen und Großschreibung möglich machen mit KEYDOWN and KEYUP
                                                                            #TODO: Mit Pfeiltasten und Stringveränderung Cursor bewegen
                                                                            #TODO: Zeilenumbruch am Ende des Fensters für längere Strings
                        if event.key == pygame.K_TAB:
                            self.nameString = self.nameString + "  "
                        elif event.key == pygame.K_BACKSPACE:
                            if self.nameString != "":
                                self.nameString = self.nameString[:-1]
                        elif event.key == pygame.K_SPACE:
                            self.nameString = self.nameString + " "
                        elif event.key == pygame.K_EXCLAIM:
                            self.nameString = self.nameString + "!"
                        elif event.key == pygame.K_QUOTEDBL:
                            self.nameString = self.nameString + '"'
                        elif event.key == pygame.K_HASH:
                            self.nameString = self.nameString + "#"
                        elif event.key == pygame.K_DOLLAR:
                            self.nameString = self.nameString + "$"
                        elif event.key == pygame.K_QUOTE:
                            self.nameString = self.nameString + "'"
                        elif event.key == pygame.K_LEFTPAREN:
                            self.nameString = self.nameString + "("
                        elif event.key == pygame.K_RIGHTPAREN:
                            self.nameString = self.nameString + ")"
                        elif event.key == pygame.K_ASTERISK or event.key == pygame.K_KP_MULTIPLY:
                            self.nameString = self.nameString + "*"
                        elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                            self.nameString = self.nameString + "+"
                        elif event.key == pygame.K_COMMA:
                            self.nameString = self.nameString + ","
                        elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                            self.nameString = self.nameString + "-"
                        elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                            self.nameString = self.nameString + "."
                        elif event.key == pygame.K_SLASH or event.key == pygame.K_KP_DIVIDE:
                            self.nameString = self.nameString + "/"
                        elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                            self.nameString = self.nameString + "0"
                        elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            self.nameString = self.nameString + "1"
                        elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            self.nameString = self.nameString + "2"
                        elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                            self.nameString = self.nameString + "3"
                        elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                            self.nameString = self.nameString + "4"
                        elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                            self.nameString = self.nameString + "5"
                        elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                            self.nameString = self.nameString + "6"
                        elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                            self.nameString = self.nameString + "7"
                        elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                            self.nameString = self.nameString + "8"
                        elif event.key == pygame.K_9:
                            self.nameString = self.nameString + "9"
                        elif event.key == pygame.K_KP9:
                            if self.cheat == 3:
                                if self.yourTeam == "Team1":
                                    self.strahlungTeam1 += 100000000
                                    self.metalleTeam1 += 100000
                                elif self.yourTeam == "Team2":
                                    self.strahlungTeam2 += 100000000
                                    self.metalleTeam2 += 100000
                                self.cheat = 0
                            else:
                                self.cheat += 1
                        elif event.key == pygame.K_COLON:
                            self.nameString = self.nameString + ":"
                        elif event.key == pygame.K_SEMICOLON:
                            self.nameString = self.nameString + ";"
                        elif event.key == pygame.K_LESS:
                            self.nameString = self.nameString + "<"
                        elif event.key == pygame.K_EQUALS or event.key == pygame.K_KP_EQUALS:
                            self.nameString = self.nameString + "="
                        elif event.key == pygame.K_GREATER:
                            self.nameString = self.nameString + ">"
                        elif event.key == pygame.K_QUESTION:
                            self.nameString = self.nameString + "?"
                        elif event.key == pygame.K_AT:
                            self.nameString = self.nameString + "@"
                        elif event.key == pygame.K_LEFTBRACKET:
                            self.nameString = self.nameString + "["
                        elif event.key == pygame.K_RIGHTBRACKET:
                            self.nameString = self.nameString + "]"
                        elif event.key == pygame.K_CARET:
                            self.nameString = self.nameString + "^"
                        elif event.key == pygame.K_UNDERSCORE:
                            self.nameString = self.nameString + "_"
                        elif event.key == pygame.K_BACKQUOTE:
                            self.nameString = self.nameString + "`"
                        elif event.key == pygame.K_a:
                            self.nameString = self.nameString + "a"
                        elif event.key == pygame.K_b:
                            self.nameString = self.nameString + "b"
                        elif event.key == pygame.K_c:
                            self.nameString = self.nameString + "c"
                        elif event.key == pygame.K_d:
                            self.nameString = self.nameString + "d"
                        elif event.key == pygame.K_e:
                            self.nameString = self.nameString + "e"
                        elif event.key == pygame.K_f:
                            self.nameString = self.nameString + "f"
                        elif event.key == pygame.K_g:
                            self.nameString = self.nameString + "g"
                        elif event.key == pygame.K_h:
                            self.nameString = self.nameString + "h"
                        elif event.key == pygame.K_i:
                            self.nameString = self.nameString + "i"
                        elif event.key == pygame.K_j:
                            self.nameString = self.nameString + "j"
                        elif event.key == pygame.K_k:
                            self.nameString = self.nameString + "k"
                        elif event.key == pygame.K_l:
                            self.nameString = self.nameString + "l"
                        elif event.key == pygame.K_m:
                            self.nameString = self.nameString + "m"
                        elif event.key == pygame.K_n:
                            self.nameString = self.nameString + "n"
                        elif event.key == pygame.K_o:
                            self.nameString = self.nameString + "o"
                        elif event.key == pygame.K_p:
                            self.nameString = self.nameString + "p"
                        elif event.key == pygame.K_q:
                            self.nameString = self.nameString + "q"
                        elif event.key == pygame.K_r:
                            self.nameString = self.nameString + "r"
                        elif event.key == pygame.K_s:
                            self.nameString = self.nameString + "s"
                        elif event.key == pygame.K_t:
                            self.nameString = self.nameString + "t"
                        elif event.key == pygame.K_u:
                            self.nameString = self.nameString + "u"
                        elif event.key == pygame.K_v:
                            self.nameString = self.nameString + "v"
                        elif event.key == pygame.K_w:
                            self.nameString = self.nameString + "w"
                        elif event.key == pygame.K_x:
                            self.nameString = self.nameString + "x"
                        elif event.key == pygame.K_y:
                            self.nameString = self.nameString + "y"
                        elif event.key == pygame.K_z:
                            self.nameString = self.nameString + "z"
                        elif event.key == pygame.K_EURO:
                            self.nameString = self.nameString + "€"
                        elif event.key == pygame.K_DELETE:
                            self.nameString = ""
                        elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                            flag = 0
                            for star in self.starArrayTeam1:
                                if self.nameString != star["name"]:
                                    pass
                                else:
                                    flag = 1

                            for star in self.starArrayTeam2:
                                if self.nameString != star["name"]:
                                    pass
                                else:
                                    flag = 1

                            for star in self.starArraySpecial:
                                if self.nameString == star["name"]:
                                    flag = 1

                            if flag == 1:
                                self.NameSchonVergeben = True
                            else:
                                self.NameSchonVergeben = False
                                self.nameEingeben = 3


                if event.type == pygame.MOUSEMOTION and self.NewStarSlide:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > 175 and pos[0] < 825:
                        self.NewStarSizeCord = pos[0]
                    elif pos[0] <= 175:
                        self.NewStarSizeCord = 175
                    elif pos[0] >= 825:
                        self.NewStarSizeCord = 825

                elif event.type == pygame.MOUSEMOTION and not self.NewStarSlide:
                    pos = pygame.mouse.get_pos()
                    for button in self.EventButtonSurfaces:
                        if pos[0]>button["pos"][0]-6 and pos[0]<button["pos"][0]+self.MainFontMiddle.size(button["name"])[0]+6 and pos[1]>button["pos"][1]-15 and pos[1]<button["pos"][1]+self.MainFontMiddle.size(button["name"])[1]+15:
                            self.EventButtonHover = True
                            break

                    if self.TechButtonSurface.collidepoint(pos):
                        self.TechHover=True
                    else:
                        self.TechHover=False

                    if self.NewStarButtonSurface.collidepoint(pos):
                        self.NewStarHover= True
                    else:
                        self.NewStarHover= False
                    if StrahlungIconSurface.collidepoint(pos) or self.StrahlungTextSurface.collidepoint(pos) or (pos[0]<strahlungTextX and pos[0]>strahlungTextX-40 and pos[1]<40):
                        self.StrahlungHover = True
                    else:
                        self.StrahlungHover = False
                    if MetallIconSurface.collidepoint(pos) or self.MetallTextSurface.collidepoint(pos) or (pos[0]<metallTextX and pos[0]>metallTextX-70 and pos [1]<40):
                        self.MetallHover = True
                    else:
                        self.MetallHover = False

                    #Slider MasterVolume
                    if self.MasterVolumeSliderMove==True:
                        if pos[0]>=210:
                            self.MasterVolumeSliderPos=100
                        elif pos[0]<=42:
                            self.MasterVolumeSliderPos=0
                        else:
                            self.MasterVolumeSliderPos=(pos[0]-42)*100/168

                    #Slider MusicVolume
                    if self.MusicVolumeSliderMove==True:
                        if pos[0]>=210:
                            self.MusicVolumeSliderPos=100
                        elif pos[0]<=42:
                            self.MusicVolumeSliderPos=0
                        else:
                            self.MusicVolumeSliderPos=(pos[0]-42)*100/168

                    #Slider MusicVolume
                    if self.SFXVolumeSliderMove==True:
                        if pos[0]>=210:
                            self.SFXVolumeSliderPos=100
                        elif pos[0]<=42:
                            self.SFXVolumeSliderPos=0
                        else:
                            self.SFXVolumeSliderPos=(pos[0]-42)*100/168

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.NewStarSlide == True:
                    self.NewStarSlide = False

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not self.NewStarSlide:
                    self.MasterVolumeSliderMove=False
                    self.MusicVolumeSliderMove=False
                    self.SFXVolumeSliderMove=False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    #print(pos)

                    actiontaken = False
                    for button in self.EventButtonSurfaces:
                        if pos[0]>button["pos"][0] and pos[0]<button["pos"][0]+self.MainFontMiddle.size(button["name"])[0] and pos[1]>button["pos"][1] and pos[1]<button["pos"][1]+self.MainFontMiddle.size(button["name"])[1] and eval(button["bedingung"]):
                            star = button["star"]
                            exec(button["effect"])
                            button["Event"]["state"] = False
                            self.EventbuttonHover = False
                            self.EventButtonSurfaces.remove(button)
                            self.playSFX("Klick", True, 0.8)
                            actiontaken = True
                            break
                    if actiontaken:
                        continue


                    if self.TechButtonSurface.collidepoint(pos):
                        #print("Auf TechButtonSurface geklickt")
                        self.TechOpen = True
                        self.playSFX("Klick", True, 0.8)
                        continue
                    elif self.SettingsIconSurface.collidepoint(pos) and not self.TechOpen:
                        self.playSFX("Klick", True, 0.8)
                        if self.SettingsOpen:
                            self.SettingsOpen = False
                        else:
                            self.SettingsOpen = True
                        continue

                    elif self.NewStarButtonSurface.collidepoint(pos):
                        #print("Auf NewStarButtonSurface geklickt")
                        self.NewStarOpen = True

                        self.SettingsOpen=False
                        Team1geklickt = False
                        Team2geklickt = False
                        Specialgeklickt = False
                        continue

                    else:
                        if self.SettingsOpen:
                            #liegt außerhalb
                            if pos[0]<18 or pos[0]>237 or pos[1]<55 or pos[1]>325:
                                self.SettingsOpen=False
                                continue

                            #liegt auf Master Volume Knopf
                            if pos[0]>42+self.MasterVolumeSliderPos*168/100-self.VolumeSliderSize and pos[0]<42+self.MasterVolumeSliderPos*168/100+self.VolumeSliderSize and pos[1]>113-self.VolumeSliderSize and pos[1]<113+self.VolumeSliderSize:
                                self.MasterVolumeSliderMove=True
                                self.playSFX("Klick", True, 0.8)
                                continue

                            #liegt auf Music Volume Knopf
                            if pos[0]>42+self.MusicVolumeSliderPos*168/100-self.VolumeSliderSize and pos[0]<42+self.MusicVolumeSliderPos*168/100+self.VolumeSliderSize and pos[1]>213-self.VolumeSliderSize and pos[1]<213+self.VolumeSliderSize:
                                self.MusicVolumeSliderMove=True
                                self.playSFX("Klick", True, 0.8)
                                continue

                            #liegt auf SFX Volume Knopf
                            if pos[0]>42+self.SFXVolumeSliderPos*168/100-self.VolumeSliderSize and pos[0]<42+self.SFXVolumeSliderPos*168/100+self.VolumeSliderSize and pos[1]>313-self.VolumeSliderSize and pos[1]<313+self.VolumeSliderSize:
                                self.SFXVolumeSliderMove=True
                                self.playSFX("Klick", True, 0.8)
                                continue

                    if self.TechOpen == False:
                        actiontaken = False
                        for star in self.starArrayTeam1:
                            if pos[0] > star["cord_x"] - click_size and pos[0] < star["cord_x"] + click_size and pos[1] > star["cord_y"] - click_size and pos[1] < star["cord_y"] + click_size:
                                if self.chooseAttackStar == True and self.yourTeam == "Team2":
                                    self.starAttack(star, self.AttackStar)
                                    break
                                elif self.chooseAttackStar and self.yourTeam == "Team1":
                                    self.chooseAttackStar = False
                                elif not self.choosePlace:
                                    self.infoBoxOpen = True
                                    self.infoBoxStar = star
                                    self.infoBoxTeam = "Team1"
                                Team1geklickt = True
                                actiontaken = True
                                break

                        if actiontaken:
                            continue

                        actiontaken = False
                        for star in self.starArrayTeam2:
                            if pos[0] > star["cord_x"] - click_size and pos[0] < star["cord_x"] + click_size and pos[1] > star["cord_y"] - click_size and pos[1] < star["cord_y"] + click_size:
                                if self.chooseAttackStar == True and self.yourTeam == "Team1":
                                    self.starAttack(star, self.AttackStar)
                                    break
                                elif self.chooseAttackStar == True and self.yourTeam == "Team2":
                                    self.chooseAttackStar = False
                                elif self.choosePlace == False:
                                    self.infoBoxOpen = True
                                    self.infoBoxStar = star
                                    self.infoBoxTeam = "Team2"
                                    #self.drawInfo()
                                Team2geklickt = True
                                actiontaken = True
                        if actiontaken:
                            continue


                        actiontaken = False
                        for star in self.starArrayHostileTeam1:
                            if pos[0] > star["cord_x"] - click_size and pos[0] < star["cord_x"] + click_size and pos[1] > star["cord_y"] - click_size and pos[1] < star["cord_y"] + click_size:
                                if self.chooseAttackStar == True and self.yourTeam == "Team1":
                                    self.starAttack(star, self.AttackStar)
                                    break
                                elif self.chooseAttackStar == True and self.yourTeam == "Team2":
                                    self.chooseAttackStar = False
                                elif self.choosePlace == False:
                                    self.infoBoxOpen = True
                                    self.infoBoxStar = star
                                    self.infoBoxTeam = "Team2"
                                    #self.drawInfo()
                                Team2geklickt = True
                                actiontaken = True
                        if actiontaken:
                            continue

                        actiontaken = False
                        for star in self.starArrayHostileTeam2:
                            if pos[0] > star["cord_x"] - click_size and pos[0] < star["cord_x"] + click_size and pos[1] > star["cord_y"] - click_size and pos[1] < star["cord_y"] + click_size:
                                if self.chooseAttackStar == True and self.yourTeam == "Team2":
                                    self.starAttack(star, self.AttackStar)
                                    break
                                elif self.chooseAttackStar == True and self.yourTeam == "Team1":
                                    self.chooseAttackStar = False
                                elif self.choosePlace == False:
                                    self.infoBoxOpen = True
                                    self.infoBoxStar = star
                                    self.infoBoxTeam = "Team2"
                                    #self.drawInfo()
                                Team2geklickt = True
                                actiontaken = True
                        if actiontaken:
                            continue

                        actiontaken = False
                        for star in self.starArraySpecial:
                            if pos[0] > star["cord_x"] - click_size and pos[0] < star["cord_x"] + click_size and pos[1] > star["cord_y"] - click_size and pos[1] < star["cord_y"] + click_size:
                                if self.chooseAttackStar == True:
                                    self.chooseAttackStar = False
                                else:
                                    #print("liegt drauf", star["name"])
                                    self.infoBoxOpen = True
                                    self.infoBoxStar = star
                                    self.infoBoxTeam = "Special"
                                    #self.drawInfo()
                                actiontaken = True
                                Specialgeklickt = True
                                continue
                        if actiontaken:
                            continue


                        if self.NewStarOpen == True and self.NewStarBuild == True:
                            if NewStarCloseIconSurface.collidepoint(pos):
                                self.NewStarOpen = False
                                self.NewStarBuild = False
                                continue
                            elif self.NewStarNameSurface.collidepoint(pos):
                                self.nameEingeben = 1
                                continue
                            elif pos[0] > self.NewStarSizeCord - 10 and pos[0] < self.NewStarSizeCord + 10 and pos[1] > 390 and pos[1] < 410:
                                #print("Auf NewStarSizeSliderCircle geklickt")
                                self.NewStarSlide = True
                                continue
                            elif self.NewStarOkTextSurface.collidepoint(pos):
                                if self.yourTeam == "Team1":
                                    if self.strahlungTeam1 >= self.NewStarCost:
                                        self.choosePlace = True
                                        self.NewStarOpen = False
                                        Team1geklickt = False
                                        Team2geklickt = False
                                        Specialgeklickt = False
                                        x = False
                                else:
                                    if self.strahlungTeam2 >= self.NewStarCost:
                                        self.choosePlace = True
                                        self.NewStarOpen = False
                                        Team1geklickt = False
                                        Team2geklickt = False
                                        Specialgeklickt = False
                                        x = False
                                continue


                        if self.choosePlace:    #Tag
                            if not Team1geklickt and not Team2geklickt and not Specialgeklickt:
                                if x == True:
                                    self.choosePlace = False
                                    if self.yourTeam == "Team1":
                                        self.strahlungTeam1 = self.strahlungTeam1 - self.NewStarCost
                                        self.playSFX("AddStar", 1, 0.7)
                                        if self.techArrayTeam1['Perfektion'][1]:
                                            mod = 0.8
                                        else:
                                            mod = 1.0
                                        if self.techArrayTeam1['Perfektion'][6]:
                                            mod = mod * 1.3
                                        elif self.techArrayTeam1['Perfektion'][7]:
                                            mod = mod * 0.8
                                        if self.techArrayTeam1["Kraft"][4]:
                                            healthmod = 8/5
                                        else:
                                            healthmod = 1
                                        self.starArrayTeam1.append({"name": self.nameString,
                                                                        "cord_x": pos[0],
                                                                        "cord_y": pos[1],
                                                                        "mass": self.NewStarMass,
                                                                        "cat": "Geburt",
                                                                        "inAttack": False,
                                                                        "team": 1,
                                                                        "age": 0,
                                                                        "health": 300 * self.NewStarMass * healthmod, #HealthFormel [für Suche]
                                                                        "nextLevel": mod * 1/(self.NewStarMass+1)**0.5*60/0.1})  #TimeFormel [für Suche]

                                        v = '{"action": "starArrayTeam1", "data": ' + json.dumps(self.starArrayTeam1) + '}'
                                        v = v.encode('utf-8')

                                        #debugMode
                                        self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
                                        self.nameEingeben = 0
                                        self.nameString = " "

                                    elif self.yourTeam == "Team2":
                                        self.strahlungTeam2 = self.strahlungTeam2 - self.NewStarCost
                                        self.playSFX("AddStar", 2, 0.7)
                                        if self.techArrayTeam2['Perfektion'][1]:
                                            mod = 0.8
                                        else:
                                            mod = 1.0
                                        if self.techArrayTeam2['Perfektion'][6]:
                                            mod = mod * 1.3
                                        elif self.techArrayTeam2['Perfektion'][7]:
                                            mod = mod * 0.8
                                        if self.techArrayTeam2["Kraft"][4]:
                                            healthmod = 8/5
                                        else:
                                            healthmod = 1
                                        self.starArrayTeam2.append({"name": self.nameString,
                                                                        "cord_x": pos[0],
                                                                        "cord_y": pos[1],
                                                                        "mass": self.NewStarMass,
                                                                        "cat": "Geburt",
                                                                        "inAttack": False,
                                                                        "team": 2,
                                                                        "age": 0,
                                                                        "nextLevel": mod * 1/(self.NewStarMass+1)**0.5*60/0.1,    #TimeFormel [für Suche]
                                                                        "health": 300 * self.NewStarMass * healthmod})    #HealthFormel [für Suche]

                                        v = '{"action": "starArrayTeam2", "data": ' + json.dumps(self.starArrayTeam2) + '}'
                                        v = v.encode('utf-8')
                                        #DebugMode
                                        self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
                                        self.nameEingeben = 0
                                        self.nameString = " "

                                else:
                                    x = True

                    else:
                        #print("Es wurde was in Tech geklickt")
                        if self.TechBuild == True:
                            if self.TechCloseIconSurface.collidepoint(pos):
                                self.TechOpen = False
                                self.TechBuild = False

                            elif self.PerfektionIconISurface.collidepoint(pos):
                                if self.TechInfoOpen == False:
                                    self.showInfo("PerfektionI")
                                elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionI":
                                    self.showInfo("PerfektionI")
                                else:
                                    self.TechInfoOpen = False

                            elif self.PerfektionIconVISurface.collidepoint(pos):
                                if self.TechInfoOpen == False:
                                    self.showInfo("PerfektionVI")
                                elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionVI":
                                    self.showInfo("PerfektionVI")
                                else:
                                    self.TechInfoOpen = False

                            elif self.KraftIconISurface.collidepoint(pos):
                                if self.TechInfoOpen == False:
                                    self.showInfo("KraftI")
                                elif self.TechInfoOpen == True and self.TechInfoString != "KraftI":
                                    self.showInfo("KraftI")
                                else:
                                    self.TechInfoOpen = False

                            elif self.KraftIconVIISurface.collidepoint(pos):
                                if self.TechInfoOpen == False:
                                    self.showInfo("KraftVII")
                                elif self.TechInfoOpen == True and self.TechInfoString != "KraftVII":
                                    self.showInfo("KraftVII")
                                else:
                                    self.TechInfoOpen = False

                            elif self.WeisheitIconISurface.collidepoint(pos):
                                if self.TechInfoOpen == False:
                                    self.showInfo("WeisheitI")
                                elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitI":
                                    self.showInfo("WeisheitI")
                                else:
                                    self.TechInfoOpen = False

                            elif self.WeisheitIconVIISurface.collidepoint(pos):
                                if self.TechInfoOpen == False:
                                    self.showInfo("WeisheitVII")
                                elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitVII":
                                    self.showInfo("WeisheitVII")
                                else:
                                    self.TechInfoOpen = False

                            if self.yourTeam == "Team1":
                                if self.techArrayTeam1["Perfektion"][0] == True:
                                    if self.PerfektionIconIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionII":
                                            self.showInfo("PerfektionII")
                                        else:
                                            self.TechInfoOpen = False
                                    elif self.PerfektionIconIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionIII":
                                            self.showInfo("PerfektionIII")
                                        else:
                                            self.TechInfoOpen = False
                                    if self.techArrayTeam1["Perfektion"][1] == True or self.techArrayTeam1["Perfektion"][2]:
                                        if self.PerfektionIconIVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("PerfektionIV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionIV":
                                                self.showInfo("PerfektionIV")
                                            else:
                                                self.TechInfoOpen = False
                                        if self.techArrayTeam1["Perfektion"][3] == True:
                                            if self.PerfektionIconVSurface.collidepoint(pos):
                                                if self.TechInfoOpen == False:
                                                    self.showInfo("PerfektionV")
                                                elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionV":
                                                    self.showInfo("PerfektionV")
                                                else:
                                                    self.TechInfoOpen = False

                                if self.techArrayTeam1["Perfektion"][5] == True:
                                    if self.PerfektionIconVIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionVII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionVII":
                                            self.showInfo("PerfektionVII")
                                        else:
                                            self.TechInfoOpen = False

                                    elif self.PerfektionIconVIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionVIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionVIII":
                                            self.showInfo("PerfektionVIII")
                                        else:
                                            self.TechInfoOpen = False

                                if self.techArrayTeam1["Kraft"][0] == True:
                                    if self.KraftIconIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("KraftII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "KraftII":
                                            self.showInfo("KraftII")
                                        else:
                                            self.TechInfoOpen = False

                                    if self.techArrayTeam1["Kraft"][1] == True:
                                        if self.KraftIconIIISurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("KraftIII")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "KraftIII":
                                                self.showInfo("KraftIII")
                                            else:
                                                self.TechInfoOpen = False

                                        elif self.KraftIconIVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("KraftIV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "KraftIV":
                                                self.showInfo("KraftIV")
                                            else:
                                                self.TechInfoOpen = False

                                        elif self.KraftIconVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("KraftV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "KraftV":
                                                self.showInfo("KraftV")
                                            else:
                                                self.TechInfoOpen = False

                                        if self.techArrayTeam1["Kraft"][2] == True or self.techArrayTeam1["Kraft"][3] == True or self.techArrayTeam1["Kraft"][4]:
                                            if self.KraftIconVISurface.collidepoint(pos):
                                                if self.TechInfoOpen == False:
                                                    self.showInfo("KraftVI")
                                                elif self.TechInfoOpen == True and self.TechInfoString != "KraftVI":
                                                    self.showInfo("KraftVI")
                                                else:
                                                    self.TechInfoOpen = False

                                if self.techArrayTeam1["Kraft"][6] == True:
                                    if self.KraftIconVIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("KraftVIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "KraftVIII":
                                            self.showInfo("KraftVIII")
                                        else:
                                            self.TechInfoOpen = False

                                if self.techArrayTeam1["Weisheit"][0] == True:
                                    if self.WeisheitIconIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("WeisheitII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitII":
                                            self.showInfo("WeisheitII")
                                        else:
                                            self.TechInfoOpen = False

                                    elif self.WeisheitIconIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("WeisheitIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitIII":
                                            self.showInfo("WeisheitIII")
                                        else:
                                            self.TechInfoOpen = False

                                    if self.techArrayTeam1["Weisheit"][2] == True:
                                        if self.WeisheitIconIVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("WeisheitIV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitIV":
                                                self.showInfo("WeisheitIV")
                                            else:
                                                self.TechInfoOpen = False

                                        elif self.WeisheitIconVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("WeisheitV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitV":
                                                self.showInfo("WeisheitV")
                                            else:
                                                self.TechInfoOpen = False

                                        if self.techArrayTeam1["Weisheit"][3] == True or self.techArrayTeam1["Weisheit"][4] == True:
                                            if self.WeisheitIconVISurface.collidepoint(pos):
                                                if self.TechInfoOpen == False:
                                                    self.showInfo("WeisheitVI")
                                                elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitVI":
                                                    self.showInfo("WeisheitVI")
                                                else:
                                                    self.TechInfoOpen = False

                                if self.techArrayTeam1["Weisheit"][6] == True:
                                    if self.WeisheitIconVIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("WeisheitVIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitVIII":
                                            self.showInfo("WeisheitVIII")
                                        else:
                                            self.TechInfoOpen = False

                            elif self.yourTeam == "Team2":
                                if self.techArrayTeam2["Perfektion"][0] == True:
                                    if self.PerfektionIconIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionII":
                                            self.showInfo("PerfektionII")
                                        else:
                                            self.TechInfoOpen = False
                                    elif self.PerfektionIconIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionIII":
                                            self.showInfo("PerfektionIII")
                                        else:
                                            self.TechInfoOpen = False
                                    if self.techArrayTeam2["Perfektion"][1] == True or self.techArrayTeam2["Perfektion"][2]:
                                        if self.PerfektionIconIVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("PerfektionIV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionIV":
                                                self.showInfo("PerfektionIV")
                                            else:
                                                self.TechInfoOpen = False
                                        if self.techArrayTeam2["Perfektion"][3] == True:
                                            if self.PerfektionIconVSurface.collidepoint(pos):
                                                if self.TechInfoOpen == False:
                                                    self.showInfo("PerfektionV")
                                                elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionV":
                                                    self.showInfo("PerfektionV")
                                                else:
                                                    self.TechInfoOpen = False

                                if self.techArrayTeam2["Perfektion"][5] == True:
                                    if self.PerfektionIconVIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionVII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionVII":
                                            self.showInfo("PerfektionVII")
                                        else:
                                            self.TechInfoOpen = False

                                    elif self.PerfektionIconVIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("PerfektionVIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "PerfektionVIII":
                                            self.showInfo("PerfektionVIII")
                                        else:
                                            self.TechInfoOpen = False

                                if self.techArrayTeam2["Kraft"][0] == True:
                                    if self.KraftIconIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("KraftII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "KraftII":
                                            self.showInfo("KraftII")
                                        else:
                                            self.TechInfoOpen = False

                                    if self.techArrayTeam2["Kraft"][1] == True:
                                        if self.KraftIconIIISurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("KraftIII")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "KraftIII":
                                                self.showInfo("KraftIII")
                                            else:
                                                self.TechInfoOpen = False

                                        elif self.KraftIconIVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("KraftIV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "KraftIV":
                                                self.showInfo("KraftIV")
                                            else:
                                                self.TechInfoOpen = False

                                        elif self.KraftIconVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("KraftV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "KraftV":
                                                self.showInfo("KraftV")
                                            else:
                                                self.TechInfoOpen = False

                                        if self.techArrayTeam2["Kraft"][2] == True or self.techArrayTeam2["Kraft"][3] == True or self.techArrayTeam2["Kraft"][4]:
                                            if self.KraftIconVISurface.collidepoint(pos):
                                                if self.TechInfoOpen == False:
                                                    self.showInfo("KraftVI")
                                                elif self.TechInfoOpen == True and self.TechInfoString != "KraftVI":
                                                    self.showInfo("KraftVI")
                                                else:
                                                    self.TechInfoOpen = False

                                if self.techArrayTeam2["Kraft"][6] == True:
                                    if self.KraftIconVIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("KraftVIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "KraftVIII":
                                            self.showInfo("KraftVIII")
                                        else:
                                            self.TechInfoOpen = False

                                if self.techArrayTeam2["Weisheit"][0] == True:
                                    if self.WeisheitIconIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("WeisheitII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitII":
                                            self.showInfo("WeisheitII")
                                        else:
                                            self.TechInfoOpen = False

                                    elif self.WeisheitIconIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("WeisheitIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitIII":
                                            self.showInfo("WeisheitIII")
                                        else:
                                            self.TechInfoOpen = False

                                    if self.techArrayTeam2["Weisheit"][2] == True:
                                        if self.WeisheitIconIVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("WeisheitIV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitIV":
                                                self.showInfo("WeisheitIV")
                                            else:
                                                self.TechInfoOpen = False

                                        elif self.WeisheitIconVSurface.collidepoint(pos):
                                            if self.TechInfoOpen == False:
                                                self.showInfo("WeisheitV")
                                            elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitV":
                                                self.showInfo("WeisheitV")
                                            else:
                                                self.TechInfoOpen = False

                                        if self.techArrayTeam2["Weisheit"][3] == True or self.techArrayTeam2["Weisheit"][4] == True:
                                            if self.WeisheitIconVISurface.collidepoint(pos):
                                                if self.TechInfoOpen == False:
                                                    self.showInfo("WeisheitVI")
                                                elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitVI":
                                                    self.showInfo("WeisheitVI")
                                                else:
                                                    self.TechInfoOpen = False

                                if self.techArrayTeam2["Weisheit"][6] == True:
                                    if self.WeisheitIconVIIISurface.collidepoint(pos):
                                        if self.TechInfoOpen == False:
                                            self.showInfo("WeisheitVIII")
                                        elif self.TechInfoOpen == True and self.TechInfoString != "WeisheitVIII":
                                            self.showInfo("WeisheitVIII")
                                        else:
                                            self.TechInfoOpen = False

                            if self.TechInfoOpen == True:
                                if pos[0] > self.TechInfoSurface[0] + (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2) and pos[0] < self.TechInfoSurface[0] + (TechInfoSizeX / 2 + self.MainFontMiddle.size("Erforschen")[0] / 2) and pos[1] > self.TechInfoSurface[1] + self.TechInfoSurface[3] - 30 and pos[1] < self.TechInfoSurface[1] + self.TechInfoSurface[3] - 30 + fontSizeMiddle:
                                    #print("Erforschen geklickt ", self.TechInfoString)
                                    if self.yourTeam == "Team1":
                                        techArray = self.techArrayTeam1
                                        metalle = self.metalleTeam1
                                    else:
                                        techArray = self.techArrayTeam2
                                        metalle = self.metalleTeam2

                                    if self.TechInfoString == "PerfektionI":
                                        if metalle >= self.techcostmod * self.Perfektiontechmod * PerfektionICost and techArray["Perfektion"][0] == False:
                                            metalle = metalle - self.techcostmod * self.Perfektiontechmod * PerfektionICost
                                            self.playSFX("PerfektionTech", True, 1)
                                            techArray["Perfektion"][0] = True
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "PerfektionII":
                                        if metalle >= self.techcostmod * self.Perfektiontechmod * PerfektionIICost and techArray["Perfektion"][1] == False:
                                            metalle = metalle - self.techcostmod * self.Perfektiontechmod * PerfektionIICost
                                            techArray["Perfektion"][1] = True
                                            self.playSFX("PerfektionTech", True, 1)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "PerfektionIII":
                                        if metalle >= self.techcostmod * self.Perfektiontechmod * PerfektionIIICost and techArray["Perfektion"][2] == False:
                                            metalle = metalle - self.techcostmod * self.Perfektiontechmod * PerfektionIIICost
                                            techArray["Perfektion"][2] = True
                                            self.playSFX("PerfektionTech", True, 1)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "PerfektionIV":
                                        if metalle >= self.techcostmod * self.Perfektiontechmod * PerfektionIVCost and techArray["Perfektion"][3] == False:
                                            metalle = metalle - self.techcostmod * self.Perfektiontechmod * PerfektionIVCost
                                            techArray["Perfektion"][3] = True
                                            self.playSFX("PerfektionTech", True, 1)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "PerfektionV":
                                        if metalle >= self.techcostmod * self.Perfektiontechmod * PerfektionVCost and techArray["Perfektion"][4] == False:
                                            metalle = metalle - self.techcostmod * self.Perfektiontechmod * PerfektionVCost
                                            techArray["Perfektion"][4] = True
                                            self.playSFX("PerfektionTech", True, 1)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "PerfektionVI":
                                        if techArray["Perfektion"][5] == False and not self.Riesetechflag:
                                            self.Riesetechflag = True
                                            self.drawEvent("RieseErforschen")
                                            self.playSFX("Klick", 1, 0.8)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "PerfektionVII":
                                        if metalle >= self.techcostmod * self.Perfektiontechmod * PerfektionVIICost and techArray["Perfektion"][6] == False:
                                            metalle = metalle - self.techcostmod * self.Perfektiontechmod * PerfektionVIICost
                                            techArray["Perfektion"][6] = True
                                            self.playSFX("PerfektionTech", 1, 1)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "PerfektionVIII":
                                        if metalle >= self.techcostmod * self.Perfektiontechmod * PerfektionVIIICost and techArray["Perfektion"][7] == False:
                                            metalle = metalle - self.techcostmod * self.Perfektiontechmod * PerfektionVIIICost
                                            techArray["Perfektion"][7] = True
                                            self.playSFX("PerfektionTech", 1, 1)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "KraftI":
                                        if metalle >=self.techcostmod * self.Krafttechmod * KraftICost and techArray["Kraft"][0] == False:
                                            metalle = metalle -self.techcostmod * self.Krafttechmod * KraftICost
                                            techArray["Kraft"][0] = True
                                            self.playSFX("KraftTech", 1, 1)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "KraftII":
                                        if metalle >=self.techcostmod * self.Krafttechmod * KraftIICost and techArray["Kraft"][1] == False:
                                            metalle = metalle -self.techcostmod * self.Krafttechmod * KraftIICost
                                            techArray["Kraft"][1] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("KraftTech", 1, 1)
                                    elif self.TechInfoString == "KraftIII":
                                        if metalle >=self.techcostmod * self.Krafttechmod * KraftIIICost and techArray["Kraft"][2] == False:
                                            metalle = metalle -self.techcostmod * self.Krafttechmod * KraftIIICost
                                            techArray["Kraft"][2] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("KraftTech", 1, 1)
                                    elif self.TechInfoString == "KraftIV":
                                        if metalle >=self.techcostmod * self.Krafttechmod * KraftIVCost and techArray["Kraft"][3] == False:
                                            metalle = metalle -self.techcostmod * self.Krafttechmod * KraftIVCost
                                            techArray["Kraft"][3] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("KraftTech", 1, 1)
                                    elif self.TechInfoString == "KraftV":
                                        if metalle >=self.techcostmod * self.Krafttechmod * KraftVCost and techArray["Kraft"][4] == False:
                                            metalle = metalle -self.techcostmod * self.Krafttechmod * KraftVCost
                                            techArray["Kraft"][4] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("KraftTech", 1, 1)
                                    elif self.TechInfoString == "KraftVI":
                                        if metalle >=self.techcostmod * self.Krafttechmod * KraftVICost and techArray["Kraft"][5] == False:
                                            metalle = metalle -self.techcostmod * self.Krafttechmod * self.Krafttechmod * KraftVICost
                                            self.TechInfoOpen = False
                                            self.playSFX("KraftTech", 1, 1)
                                            techArray["Kraft"][5] = True
                                    elif self.TechInfoString == "KraftVII":
                                        if techArray["Kraft"][6] == False and not self.SchwarzesLochflag:
                                            self.SchwarzesLochflag = True
                                            self.drawEvent("SchwarzeslochErforschen")
                                            self.playSFX("Klick", 1, 0.8)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "KraftVIII":
                                        if metalle >=self.techcostmod * self.Krafttechmod * KraftVIIICost and techArray["Kraft"][7] == False:
                                            metalle = metalle -self.techcostmod * self.Krafttechmod * KraftVIIICost
                                            techArray["Kraft"][7] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("KraftTech", 1, 1)
                                    elif self.TechInfoString == "WeisheitI":
                                        if metalle >= self.techcostmod * self.Weisheittechmod * WeisheitICost and techArray["Weisheit"][0] == False:
                                            metalle = metalle - self.techcostmod * self.Weisheittechmod * WeisheitICost
                                            techArray["Weisheit"][0] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("WeisheitTech", 1, 1)
                                    elif self.TechInfoString == "WeisheitII":
                                        if metalle >= self.techcostmod * self.Weisheittechmod * WeisheitIICost and techArray["Weisheit"][1] == False:
                                            metalle = metalle - self.techcostmod * self.Weisheittechmod * WeisheitIICost
                                            techArray["Weisheit"][1] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("WeisheitTech", 1, 1)
                                    elif self.TechInfoString == "WeisheitIII":
                                        if metalle >= self.techcostmod * self.Weisheittechmod * WeisheitIIICost and techArray["Weisheit"][2] == False:
                                            metalle = metalle - self.techcostmod * self.Weisheittechmod * WeisheitIIICost
                                            techArray["Weisheit"][2] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("WeisheitTech", 1, 1)
                                    elif self.TechInfoString == "WeisheitIV":
                                        if metalle >= self.techcostmod * self.Weisheittechmod * WeisheitIVCost and techArray["Weisheit"][3] == False:
                                            metalle = metalle - self.techcostmod * self.Weisheittechmod * WeisheitIVCost
                                            techArray["Weisheit"][3] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("WeisheitTech", 1, 1)
                                    elif self.TechInfoString == "WeisheitV":
                                        if metalle >= self.techcostmod * self.Weisheittechmod * WeisheitVCost and techArray["Weisheit"][4] == False:
                                            metalle = metalle - self.techcostmod * self.Weisheittechmod * WeisheitVCost
                                            techArray["Weisheit"][4] = True
                                            if self.yourTeam == "Team1":
                                                for star in self.starArrayTeam1:
                                                    if star["cat"] == "Riese" or star["cat"] == "Hyperriese" or star["cat"] == "Überriese":
                                                        star["health"]= star["health"]*8/5
                                                message = '{"action": "starArrayTeam1", "data": ' + json.dumps(self.starArrayTeam1) + '}'
                                                message = message.encode('utf-8')
                                                self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                                            if self.yourTeam == "Team2":
                                                for star in self.starArrayTeam2:
                                                    if star["cat"] == "Riese" or star["cat"] == "Hyperriese" or star["cat"] == "Überriese":
                                                        star["health"]= star["health"]*8/5
                                                message = '{"action": "starArrayTeam2", "data": ' + json.dumps(self.starArrayTeam2) + '}'
                                                message = message.encode('utf-8')
                                                self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                                            self.TechInfoOpen = False
                                            self.playSFX("WeisheitTech", 1, 1)
                                    elif self.TechInfoString == "WeisheitVI":
                                        if metalle >= self.techcostmod * self.Weisheittechmod * WeisheitVICost and techArray["Weisheit"][5] == False:
                                            metalle = metalle - self.techcostmod * self.Weisheittechmod * WeisheitVICost
                                            techArray["Weisheit"][5] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("WeisheitTech", 1, 1)
                                    elif self.TechInfoString == "WeisheitVII":
                                        if techArray["Weisheit"][6] == False and not self.Neutronensternflag:
                                            self.Neutronensternflag = True
                                            self.drawEvent("NeutronsternErforschen")
                                            self.playSFX("Klick", 1, 0.8)
                                            self.TechInfoOpen = False
                                    elif self.TechInfoString == "WeisheitVIII":
                                        if metalle >= self.techcostmod * self.Weisheittechmod * WeisheitVIIICost and techArray["Weisheit"][7] == False:
                                            metalle = metalle - self.techcostmod * self.Weisheittechmod * WeisheitVIIICost
                                            techArray["Weisheit"][7] = True
                                            self.TechInfoOpen = False
                                            self.playSFX("WeisheitTech", 1, 1)

                                    if self.yourTeam == "Team1":
                                        self.techArrayTeam1 = techArray
                                        self.metalleTeam1 = metalle
                                    else:
                                        self.techArrayTeam2 = techArray
                                        self.metalleTeam2 = metalle

                                    v = '{"action": "techArray", "data": ' + json.dumps(techArray) + '}'
                                    v = v.encode('utf-8')
                                    #debugmode
                                    self.s.sendto(v, (self.gegnerHost, self.gegnerPort))


                            if self.TechInfoOpen and not self.TechInfoSurface.collidepoint(pos) and not self.newtechinfo:
                                self.TechInfoOpen = False
                            if self.newtechinfo:
                                self.newtechinfo = False
                                    #print(pos)
                                    #print(self.TechInfoSurface[0] + (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2))
                                    #print(self.TechInfoSurface[0] + (TechInfoSizeX / 2 + self.MainFontMiddle.size("Erforschen")[0] / 2))
                                    #print(self.TechInfoSurface[1] + self.TechInfoSurface[3] - 30 - fontSizeMiddle)
                                    #print(self.TechInfoSurface[1] + self.TechInfoSurface[3] - 30)

            for event in self.Events:
                if event["state"]:
                    for button in self.EventButtonSurfaces:
                        if button["Event"] == event:
                            star = button["star"]
                            break
                    self.drawEvent(event["name"], star)

            if self.EventButtonHover:
                pos = pygame.mouse.get_pos()
                elseflag = True
                self.EventButtonHover = False
                for button in self.EventButtonSurfaces:
                    if pos[0]>button["pos"][0]-6 and pos[0]<button["pos"][0]+self.MainFontMiddle.size(button["name"])[0]+6 and pos[1]>button["pos"][1]-15 and pos[1]<button["pos"][1]+self.MainFontMiddle.size(button["name"])[1]+15:
                        self.EventButtonHover = True
                        if button["hovertext"]!=None and button["Event"]["state"]:
                            break

                else:
                    elseflag = False
                if elseflag:
                    star = button["star"]

                    ButtonhoverWords = []
                    holder = ""
                    for char in button["hovertext"]+" ":
                        if char != " ":
                            holder+=char
                        else:
                            ButtonhoverWords.append(holder)
                            holder = ""

                    ButtonhoverWords.append(" ")

                    y = 10
                    holder = ""
                    ButtonhoverSurface = pygame.surface.Surface((200, 500), pygame.SRCALPHA, 32)
                    ButtonhoverSurface.fill((0,0,0,0))
                    k=0
                    for word in ButtonhoverWords:
                        try:
                            word = str(eval(word))
                        except:
                            pass
                        k+=1
                        if self.MainFontSmall.size(holder + " " + word)[0] < 170 and k<len(ButtonhoverWords):
                            holder = holder  + " " + word
                        else:
                            ButtonhoverSurface.blit(self.MainFontSmall.render(holder, True, yellow), (10, y))
                            y += 20
                            holder = word

                    pygame.gfxdraw.filled_polygon(self.gameDisplay, [(pos[0], pos[1]+10), (pos[0]+10, pos[1]), (pos[0]+190, pos[1]), (pos[0]+200, pos[1]+10), (pos[0]+200, pos[1]+y), (pos[0]+190, pos[1]+y+10), (pos[0]+10, pos[1]+y+10), (pos[0], pos[1]+y)], (0,0,0,255))
                    HolderSurface = pygame.surface.Surface((510, 230), pygame.SRCALPHA, 32)
                    HolderSurface.fill((0,0,0,0))
                    HolderSurface.blit(ButtonhoverSurface, (0, 0))
                    self.gameDisplay.blit(HolderSurface, pos)
                    pygame.gfxdraw.polygon(self.gameDisplay, [(pos[0], pos[1]+10), (pos[0]+10, pos[1]), (pos[0]+190, pos[1]), (pos[0]+200, pos[1]+10), (pos[0]+200, pos[1]+y), (pos[0]+190, pos[1]+y+10), (pos[0]+10, pos[1]+y+10), (pos[0], pos[1]+y)], (255, 255, 255))

            #ConnectionCheck und Abgleich der Daten

            #Alle 5 sek Connection überprüfen und Daten checken

            if "LastConnectionCheckTime" in locals():          #Wenn es nicht die erste GameLoop ist
                if LastConnectionCheckTime <= time.time() - 5000:    #Wenn letzte Abfrage mehr als 5 sek zurückliegt
                    LastConnectionCheckTime = time.time()
                    if self.WasAngekommen:      #In den letzten 5 sek ist etwas vom Anderen Team angekommen
                        self.ConnectionError = False
                    else:
                        if self.ConnectionError:
                            self.gameExit = True    #Spiel wird beendet TODO: mit GewinnerScreen ersetzen
                        else:
                            self.ConnectionError = True
                    #Senden Aller Pakete
                    if self.yourTeam == "Team1":
                        message = '{"action": "starArrayTeam1", "data": ' + json.dumps(self.starArrayTeam1) + '}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        message = '{"action": "starArraySpecial", "data": ' + json.dumps(self.starArraySpecial) + '}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        message = '{"action": "OngoingAttacks", "data": ' + json.dumps(self.Attacks) + '}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        message = '{"action": "techArray", "data": ' + json.dumps(self.techArrayTeam1) + '}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        message = '{"action": "bistDuNochDa", "data": "Filler"}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))

                    elif self.yourTeam == "Team2":
                        message = '{"action": "starArrayTeam2", "data": ' + json.dumps(self.starArrayTeam2) + '}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        message = '{"action": "techArray", "data": ' + json.dumps(self.techArrayTeam2) + '}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        message = '{"action": "OngoingAttacks", "data": ' + json.dumps(self.Attacks) + '}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))
                        message = '{"action": "binNochDa", "data": "Filler"}'
                        message = message.encode('utf-8')
                        self.s.sendto(message, (self.gegnerHost, self.gegnerPort))

                    self.WasAngekommen = False
            else:
                LastConnectionCheckTime = time.time()

            pygame.display.update()
            self.dt = self.clock.tick(FPS) #Delay für FPS anzahl


    def showInfo(self, IconString):
        self.newtechinfo = True
        self.TechInfoOpen = True
        self.TechInfoString = IconString
        if IconString == "PerfektionI":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconIDescription):
                word = PerfektionIconIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][0] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][0] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconI_X + TechInfoSpace, PerfektionIconI_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "PerfektionII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconIIDescription):
                word = PerfektionIconIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][1] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][1] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconII_X + TechInfoSpace, PerfektionIconII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "PerfektionIII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconIIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconIIIDescription):
                word = PerfektionIconIIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconIIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][2] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][2] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconIII_X + TechInfoSpace, PerfektionIconIII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "PerfektionIV":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconIVHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconIVDescription):
                word = PerfektionIconIVDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconIVDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][3] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][3] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconIV_X + TechInfoSpace, PerfektionIconIV_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "PerfektionV":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconVHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconVDescription):
                word = PerfektionIconVDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconVDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][4] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][4] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconV_X + TechInfoSpace, PerfektionIconV_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "PerfektionVI":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconVIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconVIDescription):
                word = PerfektionIconVIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconVIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][5] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][5] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconVI_X + TechInfoSpace, PerfektionIconVI_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "PerfektionVII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconVIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconVIIDescription):
                word = PerfektionIconVIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconVIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][6] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][6] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconVII_X + TechInfoSpace, PerfektionIconVII_Y - TechInfoSpace + TechIconSizeY - TechInfoSizeY, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "PerfektionVIII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(PerfektionIconVIIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(PerfektionIconVIIIDescription):
                word = PerfektionIconVIIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(PerfektionIconVIIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1
            if self.yourTeam == "Team1" and self.techArrayTeam1["Perfektion"][7] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Perfektion"][7] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (PerfektionIconVIII_X + TechInfoSpace, PerfektionIconVII_Y - TechInfoSpace + TechIconSizeY - TechInfoSizeY, TechInfoSizeX, TechInfoSizeY))



        elif IconString == "KraftI":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconIHeader, True, TechInfoHeaderTextColor)    #searchPoint
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconIDescription):
                word = KraftIconIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][0] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][0] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconI_X + TechInfoSpace, KraftIconI_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))


        elif IconString == "KraftII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconIIDescription):
                word = KraftIconIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][1] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][1] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconII_X + TechInfoSpace, KraftIconII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "KraftIII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconIIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconIIIDescription):
                word = KraftIconIIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q !=len(KraftIconIIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][2] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][2] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconIII_X + TechInfoSpace, KraftIconIII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "KraftIV":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconIVHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconIVDescription):
                word = KraftIconIVDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q !=len(KraftIconIIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][3] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][3] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconIV_X + TechInfoSpace, KraftIconIV_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "KraftV":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconVHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconVDescription):
                word = KraftIconIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][4] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][4] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconV_X + TechInfoSpace, KraftIconV_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "KraftVI":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconVIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconIIDescription):
                word = KraftIconVIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][5] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][5] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconVI_X + TechInfoSpace, KraftIconVI_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "KraftVII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconVIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconVIIDescription):
                word = KraftIconVIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][6] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][6] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconVII_X + TechInfoSpace, KraftIconVII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))


        elif IconString == "KraftVIII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(KraftIconVIIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(KraftIconVIIIDescription):
                word = KraftIconVIIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Kraft"][7] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Kraft"][7] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (KraftIconVIII_X + TechInfoSpace, KraftIconII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitI":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconIDescription):
                word =WeisheitIconIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][0] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][0] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconI_X - TechInfoSpace - TechInfoSizeX + TechIconSizeX, WeisheitIconI_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconIIDescription):
                word =WeisheitIconIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][1] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][1] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconII_X - TechInfoSpace - TechInfoSizeX + TechIconSizeX, WeisheitIconII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitIII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconIIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconIIIDescription):
                word =WeisheitIconIIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][2] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][2] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconIII_X - TechInfoSpace - TechInfoSizeX + TechIconSizeX, WeisheitIconIII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitIV":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconIVHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconIVDescription):
                word =WeisheitIconIVDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][3] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][3] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconIV_X - TechInfoSpace - TechInfoSizeX + TechIconSizeX, WeisheitIconIV_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitV":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconVHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconVDescription):
                word =WeisheitIconVDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][4] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][4] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconV_X - TechInfoSizeX - TechInfoSpace + TechIconSizeX, WeisheitIconV_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitVI":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconVIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconVIDescription):
                word =WeisheitIconVIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][5] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][5] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconVI_X - TechInfoSpace - TechInfoSizeX + TechIconSizeX, WeisheitIconVII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitVII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconVIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconVIIDescription):
                word =WeisheitIconVIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][6] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][6] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconVII_X - TechInfoSpace - TechInfoSizeX + TechIconSizeX, WeisheitIconVII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        elif IconString == "WeisheitVIII":
            self.TechInfo = pygame.Surface((TechInfoSizeX, TechInfoSizeY))
            self.TechInfo.fill(TechInfoColor)
            self.TechInfoHeaderText = self.MainFontMiddle.render(WeisheitIconVIIIHeader, True, TechInfoHeaderTextColor)
            self.TechInfoHeaderTextSurface = self.TechInfo.blit(self.TechInfoHeaderText, (TechInfoHeaderTextX, TechInfoHeaderTextY))

            lineString = ""
            i = 0
            q = 0
            while q < len(WeisheitIconIDescription):
                word =WeisheitIconVIIDescription[q]
                lineStringTemp = lineString + " " + word
                if self.MainFontSmall.size(lineStringTemp)[0] <= TechInfoSizeX - 2 * TechInfoDescriptionSpaceX and q != len(KraftIconIIDescription) - 1:
                    lineString = lineStringTemp
                else:
                    if i == 0:
                        self.TechInfoDescriptionText1 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText1Surface = self.TechInfo.blit(self.TechInfoDescriptionText1, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + TechInfoDescriptionSpaceY))
                        i += 1
                        lineString = word
                    elif i == 1:
                        self.TechInfoDescriptionText2 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText2Surface = self.TechInfo.blit(self.TechInfoDescriptionText2, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 2 * TechInfoDescriptionSpaceY + fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 2:
                        self.TechInfoDescriptionText3 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText3Surface = self.TechInfo.blit(self.TechInfoDescriptionText3, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 3 * TechInfoDescriptionSpaceY + 2 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 3:
                        self.TechInfoDescriptionText4 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText4Surface = self.TechInfo.blit(self.TechInfoDescriptionText4, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 4 * TechInfoDescriptionSpaceY + 3 * fontSizeSmall))
                        i += 1
                        lineString = word
                    elif i == 4:
                        self.TechInfoDescriptionText5 = self.MainFontSmall.render(lineString, True, TechInfoDescriptionTextColor)
                        self.TechInfoDescriptionText5Surface = self.TechInfo.blit(self.TechInfoDescriptionText5, (TechInfoDescriptionSpaceX, TechInfoHeaderTextY + fontSizeMiddle + 5 * TechInfoDescriptionSpaceY + 4 * fontSizeSmall))
                        i += 1
                        lineString = word
                q += 1

            if self.yourTeam == "Team1" and self.techArrayTeam1["Weisheit"][7] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))
            elif self.yourTeam == "Team2" and self.techArrayTeam2["Weisheit"][7] == False:
                self.TechInfoErforschenText = self.MainFontMiddle.render("Erforschen", True, TechInfoErforschenTextColor)
                self.TechInfoErforschenTextSurface = self.TechInfo.blit(self.TechInfoErforschenText, (TechInfoSizeX / 2 - self.MainFontMiddle.size("Erforschen")[0] / 2, TechInfoSizeY - 30))

            self.TechInfoSurface = self.gameDisplay.blit(self.TechInfo, (WeisheitIconVIII_X - TechInfoSpace - TechInfoSizeX, WeisheitIconVIII_Y + TechInfoSpace, TechInfoSizeX, TechInfoSizeY))

        else:
            pass
           #print("Error in showInfo: ", IconString)


    def nextLevel(self, Changestar):
        if Changestar["team"] == 1:
            starArray = self.starArrayTeam1
            techArray = self.techArrayTeam1
            metalle = self.metalleTeam1
        else:
            starArray = self.starArrayTeam2
            metalle = self.metalleTeam2
            techArray = self.techArrayTeam2
        for star in starArray:
            if star["name"] == Changestar["name"]:
                mod = 1
                if techArray['Perfektion'][6]:
                    mod = 1.3
                elif techArray['Perfektion'][6]:
                    mod = 0.8
                if star["cat"] == "Geburt":
                    if star["mass"] <= 0.05:
                        star["cat"] = "Zwerg"
                        self.playSFX("EndstadiumErreicht", 1, 1.0)
                        star["nextLevel"] = mod/(star["masse"]+1)**0.5*60/0.1  #TimeFormel [für Suche]
                    else:
                        star["cat"] = "Hauptreihe"
                        self.playSFX("ZwischenstadiumErreicht", 1, 1.0)
                        star["nextLevel"] = 2 * mod/(star["mass"]+1)**0.5*60/0.1   #TimeFormel [für Suche]
                elif star["cat"] == "Hauptreihe":
                    if star["mass"] <= 0.3:
                        star["cat"] = "Zwerg"
                        self.playSFX("EndstadiumErreicht", 1, 1.0)
                        star["nextLevel"] = mod/(star["mass"]+1)**0.5*60/0.1   #TimeFormel [für Suche]
                    elif techArray["Perfektion"][5]:
                        if techArray['Weisheit'][4]:
                            star['health']=star['health']*1.2
                        star["cat"] = "Riese"
                        if not self.ersterRieseflag:
                            self.ersterRiese = star
                        self.playSFX("ZwischenstadiumErreicht", 1, 1.0)
                        star["nextLevel"] = mod/(star["mass"]+1)**0.5*60/0.1   #TimeFormel [für Suche]
                    elif star["mass"] <= 3:
                        star["cat"] = "Zwerg"
                        self.playSFX("EndstadiumErreicht", 1, 1.0)
                        star["nextLevel"] = mod/(star["mass"]+1)**0.5*60/0.1   #TimeFormel [für Suche]
                    elif techArray["Kraft"][6] and not techArray["Weisheit"][6]:
                        star['cat'] = "Schwarzes Loch"
                        if not self.erstesSchwarzesLochflag:
                            self.erstesSchwarzesLoch = star
                    elif not techArray["Kraft"][6] and techArray["Weisheit"][6]:
                        star["cat"] = "Neutronenstern"
                        if not self.ersterNeutronensternflag:
                            self.ersterNeutronenstern = star
                    elif techArray["Kraft"][6] and techArray["Weisheit"][6]:
                        self.drawEvent("chooseCat", star=star)
                    else:
                        star["cat"] = "Zwerg"
                        self.playSFX("EndstadiumErreicht", 1, 1.0)
                        star["nextLevel"] = mod/(star["mass"]+1)**0.5*60/0.1   #TimeFormel [für Suche]

                elif star["cat"] == "Riese" or star["cat"] == "Hyperriese" or star["cat"] == "Überriese":
                    self.playSFX("EndstadiumErreicht", 1, 1.0)
                    star["nextLevel"] = mod/(star["mass"]+1)**0.5*60/0.1   #TimeFormel [für Suche]
                    if star["mass"] <= 3 or (not techArray["Kraft"][6] and not techArray["Weisheit"][6]):
                        star["cat"] = "Zwerg"
                    elif techArray["Kraft"][6] and not techArray["Weisheit"][6]:
                        star['cat'] = "Schwarzes Loch"
                        if not self.erstesSchwarzesLochflag:
                            self.erstesSchwarzesLoch = star
                    elif not techArray["Kraft"][6] and techArray["Weisheit"][6]:
                        star["cat"] = "Neutronenstern"
                        if not self.ersterNeutronensternflag:
                            self.ersterNeutronenstern = star
                    else:
                        self.drawEvent("chooseCat", star=star)
                elif star["cat"] == "Zwerg" or star["cat"] == "Neutronenstern" or star["cat"] == "Schwarzes Loch":
                    star["nextLevel"] = 3600

                for event in self.Events:
                    if event["name"] == "chooseCat":
                        choosecat = event
                        break
                if self.techArrayTeam1 and self.yourTeam=="Team1" or self.techArrayTeam2 and self.yourTeam=="Team2":
                    mod = 1.1

                if star["mass"] <= 2.3 and star["mass"] < 3 and not choosecat["state"]:
                    metalle += mod * 400*(star["mass"]-2.3)/0.7+200
                elif star["mass"] > 3 and not choosecat["state"]:
                    metalle += mod * 400*(star["mass"]-3)/17+600

        if Changestar["team"] == 1:
            self.starArrayTeam1 = starArray
            self.techArrayTeam1 = techArray
            self.metalleTeam1 = metalle
        else:
            self.starArrayTeam2 = starArray
            self.metalleTeam2 = metalle
            self.techArrayTeam2 = techArray
        for star in starArray:

                break


    def starAttack(self, starDef, starAt):
        self.chooseAttackStar = False
        self.playSFX("BattleStart", True, 1)

        self.Attacks.append({"Angreifer": starAt["name"], "Verteidiger": starDef["name"], "SchadenAng": 0, "SchadenVer": 0, "TeamAng": "Team" + str(starAt["team"]), "TeamVer": "Team" + str(starDef["team"])})

        self.OngoingAttacksMods.append({"star": starAt["name"], "time": 5})

        v='{"action": "OngoingAttacksMods", "data": '+ json.dumps(self.OngoingAttacksMods) + '}'
        v=v.encode('utf-8')
        self.s.sendto(v, (self.gegnerHost, self.gegnerPort))
        v='{"action": "NewAttack", "data": '+ json.dumps({"Angreifer": starAt["name"], "Verteidiger": starDef["name"], "SchadenAng": 0, "SchadenVer": 0, "TeamAng": "Team" + str(starAt["team"]), "TeamVer": "Team" + str(starDef["team"])}) + '}'
        v=v.encode('utf-8')
        self.s.sendto(v, (self.gegnerHost, self.gegnerPort))


    def starCaptured(self, DeinStern, Gegner, starWon):
        print("Attacks: ", self.Attacks)
        print("DeinStern: ", DeinStern)
        print("Gegner: ", Gegner)
        print("StarWon: ", starWon)
        i = 0
        x = len(self.Attacks)
        q = 0
        print("X: ", x)
        while i < x:
            print("I: ", i)
            attack = self.Attacks[i - q]
            i += 1
        #for attack in self.Attacks:
            print("Attack: ", attack)

            if attack["Verteidiger"] == DeinStern:
                print("Du bist Verteidiger")
                GegnerTeam = attack["TeamAng"]
                self.Attacks.remove(attack)
                q += 1
            elif attack["Verteidiger"] == Gegner:
                GegnerTeam = attack["TeamVer"]
                self.Attacks.remove(attack)
                q += 1

        for value in self.OngoingAttacksMods:
            if value["star"] == DeinStern or value["star"] == Gegner:
                self.OngoingAttacksMods.remove(value)

        if starWon == "DeinStern":
            if self.infoBoxStar != {} and self.infoBoxStar["name"] == Gegner:
                self.infoBoxTeam = self.yourTeam
            if self.yourTeam == "Team1":
                self.playSFX("BattleWon", 1, 1)
                if GegnerTeam == "Team2":
                    for star in self.starArrayTeam2:
                        if star["name"] == Gegner:
                            mod = 1.0
                            if self.techArrayTeam1["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * 300 * star["mass"]/2
                            star["team"] = 1
                            self.starArrayTeam2.remove(star)

                            self.starArrayTeam1.append(star)
                            break
                elif GegnerTeam == "Team3":
                    for star in self.starArrayHostileTeam1:
                        if star["name"] == Gegner:  #Oder hat man dann gewonnen wenn man das weiße Loch besiegt hat dann müsste man einfach hier die Gewinner und VerliereScreens einblenden
                            mod = 1.0
                            if self.techArrayTeam1["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * 300 * star["mass"]/2
                            star["team"] = 1
                            self.starArrayHostileTeam1.remove(star)
                            self.starArrayTeam1.append(star)
            elif self.yourTeam == "Team2":
                self.playSFX("BattleWon", 2, 1)
                self.playSFX("BattleLost", 1, 1)
                if GegnerTeam == "Team1":
                    for star in self.starArrayTeam1:
                        if star["name"] == Gegner:
                            mod = 1.0
                            if self.techArrayTeam2["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * 300 * star["mass"]/2
                            star["team"] = 2
                            self.starArrayTeam1.remove(star)
                            self.starArrayTeam2.append(star)
                            break
                elif GegnerTeam == "Team3":
                    for star in self.starArrayHostileTeam2:
                        if star["name"] == Gegner:  #Oder hat man dann gewonnen wenn man das weiße Loch besiegt hat dann müsste man einfach hier die Gewinner und VerliereScreens einblenden
                            mod = 1.0
                            if self.techArrayTeam2["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * 300 * star["mass"]/2
                            star["team"] = 2
                            self.starArrayHostileTeam2.remove(star)
                            self.starArrayTeam2.append(star)
                            break

        elif starWon == "Gegner":
            if self.infoBoxStar != {} and self.infoBoxStar["name"] == DeinStern:
                self.infoBoxTeam = GegnerTeam
            if self.yourTeam == "Team1":
                if GegnerTeam == "Team2":
                    self.playSFX("BattleWon", 2, 1)
                    self.playSFX("BattleLost", 1, 1)
                    for star in self.starArrayTeam1:
                        if star["name"] == DeinStern:
                            mod = 1.0
                            if self.techArrayTeam2["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * (star["mass"] * 300) / 2
                            star["team"] = 2
                            self.starArrayTeam1.remove(star)
                            self.starArrayTeam2.append(star)
                            break
                elif GegnerTeam == "Team3":
                    for star in self.starArrayTeam1:
                        if star["name"] == DeinStern:
                            mod = 1.0
                            if self.techArrayTeam1["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * (star["mass"] * 300) / 2
                            star["team"] = 3
                            self.starArrayTeam1.remove(star)
                            self.starArrayHostileTeam1.append(star)
                            break
            elif self.yourTeam == "Team2":
                if GegnerTeam == "Team1":
                    self.playSFX("BattleWon", 1, 1)
                    self.playSFX("BattleLost", 2, 1)
                    for star in self.starArrayTeam2:
                        if star["name"] == DeinStern:
                            mod = 1.0
                            if self.techArrayTeam1["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * (star["mass"] * 300) / 2
                            star["team"] = 2
                            self.starArrayTeam2.remove(star)

                            self.starArrayTeam1.append(star)
                            break
                elif GegnerTeam == "Team3":
                    for star in self.starArrayTeam2:
                        if star["name"] == DeinStern:
                            mod = 1.0
                            if self.techArrayTeam2["Kraft"][4]:
                                mod = 8/5
                            star["health"] = mod * (star["mass"] * 300) / 2
                            star["team"] = 3
                            self.starArrayTeam2.remove(star)
                            self.starArrayHostileTeam2.append(star)
                            break
        else:
            pass


    def generateLocation(self, array, team):
        x_good = False
        y_good = False
        if team == "Team1":
            if array != []:
                while x_good == False or not y_good:
                    if x_good == False:
                        randomX = random.randrange(0 + border_space, display_x / 2 - border_space)
                    if y_good == False:
                        randomY = random.randrange(0 + border_space, display_y - border_space)
                    for star in array:
                        if abs(randomX - star["cord_x"]) > star_space:
                            x_good = True
                            #print("X Passt:", abs(randomX - star["cord_x"]))
                        else:   #Der generierte Wert ist zu nah an einem anderen Stern
                            x_good = False  #Nochmal neue Werte generien und überprüfen
                            #print("X Passt nicht: ", abs(randomX - star["cord_x"]))
                            break
                        if abs(randomY - star["cord_y"]) > star_space:
                            y_good = True
                            #print("Y Passt: ", abs(randomY - star["cord_y"]))
                        else:   #Der generierte Wert ist zu nah an einem anderen Stern
                            y_good = False
                            #print("Y Passt nicht: ", abs(randomY) - star["cord_y"])
                            break
                    #print("Durchlauf der Überprüfungsschleife, X:", randomX, x_good, " Y: ", randomY, y_good)
                cord_x, cord_y = randomX, randomY
            else:
                cord_x = random.randrange(0 + border_space,display_x / 2 - border_space)
                cord_y = random.randrange(0 + border_space, display_y - border_space)
            #print("Cord_x: ", cord_x)
            #print("Cord_y: ", cord_y)
            return cord_x, cord_y
        elif team == "Team2":
            if array != []:
                while x_good == False or not y_good:
                    if x_good == False:
                        randomX = random.randrange(display_x/2 + border_space, display_x - border_space)
                    if y_good == False:
                        randomY = random.randrange(0 + border_space, display_y - border_space)
                    for star in array:
                        if abs(randomX - star["cord_x"]) > star_space:
                            x_good = True
                            #print("X Passt:", abs(randomX - star["cord_x"]))
                        else:   #Der generierte Wert ist zu nah an einem anderen Stern
                            x_good = False  #Nochmal neue Werte generien und überprüfen
                            #print("X Passt nicht: ", abs(randomX - star["cord_x"]))
                            break
                        if abs(randomY - star["cord_y"]) > star_space:
                            y_good = True
                            #print("Y Passt: ", abs(randomY - star["cord_y"]))
                        else:   #Der generierte Wert ist zu nah an einem anderen Stern
                            y_good = False
                            #print("Y Passt nicht: ", abs(randomY) - star["cord_y"])
                            break
                    #print("Durchlauf der Überprüfungsschleife, X:", randomX, x_good, " Y: ", randomY, y_good)
                cord_x, cord_y = randomX, randomY
            else:
                cord_x = random.randrange(display_x/2 + border_space,display_x - border_space)
                cord_y = random.randrange(0 + border_space, display_y - border_space)
            #print("Cord_x: ", cord_x)
            #print("Cord_y: ", cord_y)
            return cord_x, cord_y
        elif team == "Special":
            if array != []:
                while x_good == False or not y_good:
                    if x_good == False:
                        randomX = random.randrange(0 + border_space, display_x - border_space)
                    if y_good == False:
                        randomY = random.randrange(0 + border_space, display_y - border_space)
                    for star in array:
                        if abs(randomX - star["cord_x"]) > star_space:
                            x_good = True
                            #print("X Passt:", abs(randomX - star["cord_x"]))
                        else:   #Der generierte Wert ist zu nah an einem anderen Stern
                            x_good = False  #Nochmal neue Werte generien und überprüfen
                            #print("X Passt nicht: ", abs(randomX - star["cord_x"]))
                            break
                        if abs(randomY - star["cord_y"]) > star_space:
                            y_good = True
                            #print("Y Passt: ", abs(randomY - star["cord_y"]))
                        else:   #Der generierte Wert ist zu nah an einem anderen Stern
                            y_good = False
                            #print("Y Passt nicht: ", abs(randomY) - star["cord_y"])
                            break
                    #print("Durchlauf der Überprüfungsschleife, X:", randomX, x_good, " Y: ", randomY, y_good)
                cord_x, cord_y = randomX, randomY
            else:
                cord_x = random.randrange(0 + border_space, display_x - border_space)
                cord_y = random.randrange(0 + border_space, display_y - border_space)
            return cord_x, cord_y

        #TODO
    def QBurst(self, stern):
        if (self.yourTeam == "Team1" and not self.techArrayTeam1["Kraft"][0]) or (self.yourTeam == "Team2" and not self.techArrayTeam2["Kraft"][0]) or (self.yourTeam == "Team1" and self.strahlungTeam1<200000*stern["mass"]) or (self.yourTeam =="Team2" and self.strahlungTeam2<200000*stern["mass"]):

            return
        if self.yourTeam == "Team1":
            self.strahlungTeam1 += -200000*stern["mass"]
        else:
            self.strahlungTeam2 += -200000*stern["mass"]

        self.playSFX("QBurst", True, 1)
        starAt = stern
        for attack in self.Attacks:
            if attack["Angreifer"] == starAt["name"]:
                starDef = attack["Verteidiger"]
                break
            elif attack["Verteidiger"] == starAt["name"]:
                starDef = attack["Angreifer"]
                break
        starAtAttack = 100*2**(-starAt["mass"]/20)    #Angriff Formel

        for star in self.starArrayTeam1:
            if star["name"] == starDef:
                StarVer = star

        for star in self.starArrayTeam2:
            if star["name"] == starDef:
                StarVer = star

       #print("Stern: ", stern)
       #print("starAt: ", starAt)
       #print("starDef: ", starDef)
       #print("StarVer: ", StarVer)

        distance = ((abs(starAt["cord_x"] - StarVer["cord_x"]))** 2 + (abs(starAt["cord_y"] - StarVer["cord_y"]))** 2 )**0.5

        rangeAt = 1
        attackAt = 1
        attackDef = 1
        defenseAt = 1
        defenseDef = 1
        stackingAt = 1
        timemod = 0
        for value in self.OngoingAttacksMods:
            if value["star"] == starAt["name"]:
               #print('gibt es')
                timemod = value["time"]
                break


        if starAt['cat'] == 'Geburt':
            mod = 0
        elif starAt['cat'] == 'Hauptreihe':
            mod = 1
        elif starAt['cat'] == 'Riese' or starAt['cat'] == 'Hyperriese' or starAt['cat'] == 'Überriese':
            mod = 0.7
        elif starAt['cat'] == 'Zwerg':
            mod = 1.7
        elif starAt['cat'] == 'Neutronenstern':
            mod = 2.1
        elif starAt['cat'] == 'Schwarzes Loch':
            mod = 3

        if starAt["team"] == 1:
            starAtTech = self.techArrayTeam1
            starDefTech = self.techArrayTeam2
        else:
            starAtTech = self.techArrayTeam2
            starDefTech = self.techArrayTeam1

        if starAtTech["Kraft"][1] == True:
            rangeAt = rangeAt * 0.85
        if starDefTech['Weisheit'][2]:
            rangeAt = rangeAt * 1.3
        if starAtTech["Kraft"][8] == True:
            attackAt = attackAt * 1.1
        if starAtTech["Kraft"][3] == True:
            timepenaltyAt = (3-timemod)/3
        else:
            timepenaltyAt = (5-timemod)/5

        if starDefTech["Kraft"][3] == True:
            defenseDef = defenseDef * 0.85

        AtDamage = starAtAttack * attackAt * mod * defenseDef * 3**(-distance*rangeAt/display_x) * timepenaltyAt * (1/FPS)

        v='{"action": "Schaden", "data": {"schaden": ' + str(10 * AtDamage) + ', "stern": "' + starDef + '", "von": "' + starAt["name"] + '"}}'
        v=v.encode('utf-8')
        self.s.sendto(v, (self.gegnerHost, self.gegnerPort))

        if self.yourTeam == "Team1":
            for star in self.starArrayTeam2:
                if star["name"] == starDef:
                    star["health"] -= 10 * AtDamage
                    #print("Stern health wurde angepasst---------------------------")
                    if star["health"] <= 0:
                        self.starCaptured(starAt["name"], StarVer["name"], "DeinStern")
        elif self.yourTeam == "Team2":
            for star in self.starArrayTeam1:
                if star["name"] == starDef:
                    star["health"] -= 10 * AtDamage
                    if star["health"] <= 0:
                        self.starCaptured(starAt["name"], StarVer["name"], "DeinStern")

    def RieseErforschenStart(self):
        if self.yourTeam == "Team1":
            self.timer.append({"time": 20, "name": "Riesen Untersuchen", "effect": "self.drawEvent('RieseErforscht')", "ongoingeffect": " "})
            self.metalleTeam1 += -500
            self.strahlungTeam1 += -2000000
        elif self.yourTeam == "Team2":
            self.timer.append({"time": 20, "name": "Riesen Untersuchen", "effect": "self.drawEvent('RieseErforscht')", "ongoingeffect": " "})
            self.metalleTeam2 += -500
            self.strahlungTeam2 += -2000000


    def NeutronsternErforschenStart(self):
        if self.yourTeam == "Team1" and self.metalleTeam1>=500 and self.strahlungTeam1>=2000000:
            self.timer.append({"time": 20, "name": "Neutronenstern Untersuchen", "effect": "self.drawEvent('NeutronsternErforscht')", "ongoingeffect": " "})
            self.metalleTeam1 += -500
            self.strahlungTeam1 += -2000000
        elif self.yourTeam == "Team2" and self.metalleTeam2>=500 and self.strahlungTeam2>=2000000:
            self.timer.append({"time": 20, "name": "Neutronenstern Untersuchen", "effect": "self.drawEvent('NeutronsternErforscht')", "ongoingeffect": " "})
            self.metalleTeam2 += -500
            self.strahlungTeam2 += -2000000


    def SchwarzeslochErforschenStart(self):
        if self.yourTeam == "Team1" and self.metalleTeam1>=500 and self.strahlungTeam1>=2000000:
            self.timer.append({"time": 20, "name": "Schwarzes Loch Unteruschen", "effect": "self.drawEvent('SchwarzeslochErforscht')", "ongoingeffect": " "})
            self.metalleTeam1 += -500
            self.strahlungTeam1 += -2000000
        elif self.yourTeam == "Team2" and self.metalleTeam2>=500 and self.strahlungTeam2>=2000000:
            self.timer.append({"time": 20, "name": "Schwarzes Loch Untersuchen", "effect": "self.drawEvent('SchwarzeslochErforscht')", "ongoingeffect": " "})
            self.metalleTeam2 += -500
            self.strahlungTeam2 += -2000000

    def drawEvent(self, eventdesc, star=[]):
        for event in self.Events:
            if event["name"] == eventdesc:
                break
        event["state"] = True


        EventTextWords = []
        holder = ""
        for char in event["text"]+" ":
            if char != " ":
                holder+=char
            else:
                EventTextWords.append(holder)
                holder = ""

        EventTextWords.append(" ")

        y = 10
        holder = ""
        k = 1
        for word in EventTextWords:
            try:
                if word == ' ':
                    pass
                else:
                    word = str(eval(word))
            except:
                pass
            if self.MainFontMiddle.size(holder + " " + word)[0] < 500 and k<len(EventTextWords):
                    holder = holder  + " " + word
            else:
                y += self.MainFontMiddle.size(holder + " " + word)[1]
                holder = word
            k+=1

        EventTextSurface = pygame.surface.Surface((520, y), pygame.SRCALPHA, 32)
        locval = y
        EventTextSurface.fill((250,250,250, 140))

        y = 10
        holder = ""
        k=1
        for word in EventTextWords:
            try:
                if word == ' ':
                    pass
                else:
                    word = str(eval(word))
            except:
                pass
            if self.MainFontSmall.size(holder + " " + word)[0] < 500 and k<len(EventTextWords):
                    holder = holder  + " " + word
            else:
                EventTextSurface.blit(self.MainFontSmall.render(holder, True, black), (10, y))
                y += self.MainFontMiddle.size(holder + " " + word)[1]
                holder = word
            k+=1

        HolderSurface = pygame.surface.Surface((520, y), pygame.SRCALPHA, 32)

        HolderSurface.blit(EventTextSurface, (0, 0))


        holder = 0
        for button in event["buttons"]:
            holder+= self.MainFontMiddle.size(button["name"])[1]+30

        EventBox = pygame.Surface((eventBox_x, eventBox_y+holder))
        EventBox.blit(pygame.transform.scale(self.EventBoxBackground, (eventBox_x, eventBox_y+holder)), (0, 0))
        EventBox.blit(HolderSurface, (50, round(eventBox_y/2+holder/2-locval/2)))
        EventHeaderText = self.MainFontMiddle.render(event["Header"], True, white)
        EventBox.blit(EventHeaderText, [round(eventBox_x/2-self.MainFontMiddle.size(event["Header"])[0]/2), 10])

        EventButtons = pygame.surface.Surface((eventBox_x, round(holder+20)), pygame.SRCALPHA, 32)

        holderlist = []
        y=20
        for button in event["buttons"]:
            pos = [pygame.mouse.get_pos()[0]-round((display_x-eventBox_x)/2), pygame.mouse.get_pos()[1]-round((display_y+eventBox_y)/2)-1]
            holderlist.append({"name": button["name"], "Surface": EventButtons.blit(self.MainFontMiddle.render(button["name"], True, black), [round((eventBox_x-self.MainFontMiddle.size(button["name"])[0])/2), y]), "effect": button["effect"], "bedingung": button['bedingung'], "Event": event, "pos": (round((display_x-eventBox_x)/2)+round((eventBox_x-self.MainFontMiddle.size(button["name"])[0])/2), y+round((display_y+eventBox_y)/2)-1), "hovertext": button["hovertext"], "star": star}) #button hinzufügen
            if self.EventButtonHover and pos[0]>round((eventBox_x-self.MainFontMiddle.size(button["name"])[0])/2)-6 and pos[0]<round((eventBox_x+self.MainFontMiddle.size(button["name"])[0])/2)+6 and pos[1]>y-10 and pos[1]<y+self.MainFontMiddle.size(button["name"])[1]+10:
                localpic = pygame.transform.scale(self.Button1hover, (self.MainFontMiddle.size(button["name"])[0]+28, self.MainFontMiddle.size(button["name"])[1]+20) )
            else:
                localpic = pygame.transform.scale(self.Button1unhover, (self.MainFontMiddle.size(button["name"])[0]+28,self.MainFontMiddle.size(button["name"])[1]+20) )
            EventButtons.blit(localpic, (round((eventBox_x-self.MainFontMiddle.size(button["name"])[0])/2)-14, y-15))
            EventButtons.blit(self.MainFontMiddle.render(button["name"], True, black), [round((eventBox_x-self.MainFontMiddle.size(button["name"])[0])/2), y])
            y+= self.MainFontMiddle.size(button["name"])[1]+30

        self.EventButtonSurfaces = holderlist
        self.EventBoxSurface = self.gameDisplay.blit(EventBox, [round((display_x-eventBox_x)/2), round((display_y-eventBox_y)/2)])
        self.EventBoxButtonsSurface = self.gameDisplay.blit(EventButtons, [round((display_x-eventBox_x)/2), round((display_y+eventBox_y)/2)-1])



    def drawStarDisplay(self):

        if self.choosePlace:
            if self.yourTeam == "Team1":
                loccolor = team1_color
            else:
                loccolor = team2_color
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(self.gameDisplay, loccolor, pos, 20, 3)
            pygame.draw.line(self.gameDisplay, loccolor, (pos[0]+5, pos[1]), (pos[0]+20, pos[1]))
            pygame.draw.line(self.gameDisplay, loccolor, (pos[0]-5, pos[1]), (pos[0]-20, pos[1]))
            pygame.draw.line(self.gameDisplay, loccolor, (pos[0], pos[1]-5), (pos[0], pos[1]-20))
            pygame.draw.line(self.gameDisplay, loccolor, (pos[0], pos[1]+5), (pos[0], pos[1]+20))

        for star in self.starArrayTeam1:
            offset = round((star_size_choose - star_size)/2+1)
            if self.chooseAttackStar and self.yourTeam == "Team2":
                offset = offset * 2
            rating = round(math.log(star['mass']/0.1)/math.log(2.96))
            x = star["cord_x"]
            y = star["cord_y"]-offset
            if rating == 5:
                self.gameDisplay.blit(self.Sternabzeichen, (x-22, y-40))
            elif rating ==4:
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11-18), (x+8, y-8-18), (x+8, y-4-18), (x, y-7-18), (x-8, y-4-18), (x-8, y-8-18)])
            elif rating == 3:
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
            elif rating == 2:
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
            else:
                pygame.draw.polygon(self.gameDisplay, team1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
            mod = 1.0
            if self.techArrayTeam1["Weisheit"][4] and (star["cat"]=="Riese" or star["cat"]=="Hyperriese" or star["cat"] == "Überriese"):
                mod = 8/5
            hight = 25
            rat5offset = 0
            if rating == 5:
                rat5offset = 4
                hight += 6
            healthproz = star['health']/(mod * 300 * star["mass"] )
            if healthproz == 1.0:
                continue
            y = y + offset
            x= x+offset
            pygame.draw.polygon(self.gameDisplay, blue, [(x+12+rat5offset, y-hight), (x+rat5offset+18, y-hight), (x+rat5offset+18, y), (x+rat5offset+12, y)])
            pygame.draw.polygon(self.gameDisplay, team1_color, [(x+rat5offset+12, round(y-hight*(healthproz))), (x+rat5offset+18, round(y-hight*(healthproz))),  (x+rat5offset+18, y), (x+rat5offset+12, y)])

        for star in self.starArrayTeam2:
            offset = round((star_size_choose - star_size)/2+1)
            if self.chooseAttackStar and self.yourTeam == "Team1":
                offset = offset * 2
            rating = round(math.log(star['mass']/0.1)/math.log(2.96))
            x = star["cord_x"]
            y = star["cord_y"]-offset
            if rating == 5:
                self.gameDisplay.blit(self.Sternabzeichen, (x-20, y-45))
            elif rating ==4:
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11-18), (x+8, y-8-18), (x+8, y-4-18), (x, y-7-18), (x-8, y-4-18), (x-8, y-8-18)])
            elif rating == 3:
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
            elif rating == 2:
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
            else:
                pygame.draw.polygon(self.gameDisplay, team2_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
            mod = 1.0
            if self.techArrayTeam2["Kraft"][4]:
                mod = 8/5
            hight = 25
            rat5offset = 0
            if rating == 5:
                rat5offset = 4
                hight += 6
            healthproz = star['health']/(mod * 300 * star["mass"] )
            if healthproz == 1.0:
                continue
            y = y + offset
            x= x+offset
            pygame.draw.polygon(self.gameDisplay, blue, [(x+12+rat5offset, y-hight), (x+rat5offset+18, y-hight), (x+rat5offset+18, y), (x+rat5offset+12, y)])
            pygame.draw.polygon(self.gameDisplay, team2_color, [(x+rat5offset+12, round(y-hight*(healthproz))), (x+rat5offset+18, round(y-hight*(healthproz))),  (x+rat5offset+18, y), (x+rat5offset+12, y)])


        for star in self.starArrayHostileTeam1:
            loccolor = hostileteam1_color
            offset = round((star_size_choose - star_size)/2+1)
            if self.chooseAttackStar and self.yourTeam == "Team1":
                offset = offset * 2
            rating = round(math.log(star['mass']/0.1)/math.log(2.96))
            x = star["cord_x"]
            y = star["cord_y"]-offset
            if rating == 5:
                self.gameDisplay.blit(self.Sternabzeichen, (x-20, y-45))
            elif rating ==4:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-18), (x+8, y-8-18), (x+8, y-4-18), (x, y-7-18), (x-8, y-4-18), (x-8, y-8-18)])
            elif rating == 3:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
            elif rating == 2:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
            else:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
            hight = 25
            rat5offset = 0
            if rating == 5:
                rat5offset = 4
                hight += 6
            healthproz = star['health']/(mod * 300 * star["mass"] )
            if healthproz == 1.0:
                continue
            y = y + offset
            x= x+offset
            pygame.draw.polygon(self.gameDisplay, blue, [(x+12+rat5offset, y-hight), (x+rat5offset+18, y-hight), (x+rat5offset+18, y), (x+rat5offset+12, y)])
            pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x+rat5offset+12, round(y-hight*(healthproz))), (x+rat5offset+18, round(y-hight*(healthproz))),  (x+rat5offset+18, y), (x+rat5offset+12, y)])

        for star in self.starArrayHostileTeam2:
            loccolor = hostileteam2_color
            offset = round((star_size_choose - star_size)/2+1)
            if self.chooseAttackStar and self.yourTeam == "Team2":
                offset = offset * 2
            rating = round(math.log(star['mass']/0.1)/math.log(2.96))
            x = star["cord_x"]
            y = star["cord_y"]-offset
            if rating == 5:
                self.gameDisplay.blit(self.Sternabzeichen, (x-20, y-45))
            elif rating ==4:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-18), (x+8, y-8-18), (x+8, y-4-18), (x, y-7-18), (x-8, y-4-18), (x-8, y-8-18)])
            elif rating == 3:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-12), (x+8, y-8-12), (x+8, y-4-12), (x, y-7-12), (x-8, y-4-12), (x-8, y-8-12)])
            elif rating == 2:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11-6), (x+8, y-8-6), (x+8, y-4-6), (x, y-7-6), (x-8, y-4-6), (x-8, y-8-6)])
            else:
                pygame.draw.polygon(self.gameDisplay, hostileteam1_color, [(x, y-11), (x+8, y-8), (x+8, y-4), (x, y-7), (x-8, y-4), (x-8, y-8)])
            hight = 25
            rat5offset = 0
            if rating == 5:
                rat5offset = 4
                hight += 6
            healthproz = star['health']/(300 * star["mass"] )
            if healthproz == 1.0:
                continue
            y = y + offset
            x= x+offset
            pygame.draw.polygon(self.gameDisplay, blue, [(x+12+rat5offset, y-hight), (x+rat5offset+18, y-hight), (x+rat5offset+18, y), (x+rat5offset+12, y)])
            pygame.draw.polygon(self.gameDisplay, hostileteam2_color, [(x+rat5offset+12, round(y-hight*(healthproz))), (x+rat5offset+18, round(y-hight*(healthproz))),  (x+rat5offset+18, y), (x+rat5offset+12, y)])

    def Crisis_Dark_Matter_Create(self):
        if self.yourTeam == "Team1":
            while True:
                cord_x = random.randrange(0+border_space, display_x/2-border_space)
                cord_y = random.randrange(0+border_space, display_y - border_space)
                continueflag = False
                for star in self.starArrayTeam1:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArrayTeam2:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArraySpecial:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArrayHostileTeam1:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArrayHostileTeam2:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                if continueflag:
                    continue
                else:
                    break

            starHealth = 20 * 300 #HealthFormel [für Suche]
            self.starArrayHostileTeam1.append({"name": "X6.5 - 93 Sigma",
                                        "cord_x": cord_x,
                                        "cord_y": cord_y,
                                        "mass": 20,
                                        "age": 0,
                                        "cat": "Weißes Loch",
                                        "inAttack": False,
                                        "team": 3,
                                        "health": starHealth,
                                        "nextLevel": 60*30})
           #print("staradded")
        if self.yourTeam == "Team2":
            while True:
                cord_x = random.randrange(0+border_space, display_x/2-border_space)
                cord_y = random.randrange(0+border_space, display_y - border_space)
                continueflag = False
                for star in self.starArrayTeam1:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArrayTeam2:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArraySpecial:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArrayHostileTeam1:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                for star in self.starArrayHostileTeam2:
                    if abs(star['cord_x']-cord_x)**2 + abs(star['cord_y']-cord_y)**2 < border_space**2:
                        continueflag = True
                        break
                if continueflag:
                    continue
                else:
                    break

            starHealth = 20 * 300 #HealthFormel [für Suche]
            self.starArrayHostileTeam2.append({"name": "X6.5 - 93 Sigma",
                                        "cord_x": cord_x,
                                        "cord_y": cord_y,
                                        "mass": 20,
                                        "age": 0,
                                        "cat": "Weißes Loch",
                                        "inAttack": False,
                                        "team": 4,
                                        "health": starHealth,
                                        "nextLevel": 60*30})

    #Funktion um sound beim richtigen team zu spielen
    def playSFX(self, soundname, team, volume):
        if team:
            sound=pygame.mixer.Sound("Sounds/"+soundname+".wav")
            sound.set_volume(volume*self.SFXVolume*self.MasterVolume)
            sound.play()
        elif self.yourTeam == "Team"+str(team):
            #print("spielesound "+"Sounds/"+soundname+".wav")
            sound=pygame.mixer.Sound("Sounds/"+soundname+".wav")
            sound.set_volume(volume*self.SFXVolume*self.MasterVolume)
            sound.play()

    # Hilfsfunktion, um ein Bild zu laden:
    def loadImage(self, filename, colorkey=None, size=None):
        image = pygame.image.load(filename)
        if size is not None:
            image = pygame.transform.scale(image, size)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

if __name__ == "__main__":
    # Nynyezi().startGame(2)
    Nynyezi().MainMenu()
