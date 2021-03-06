#!/usr/bin/env python
#padsp
#el c3 va a ser la nota de referencia 78  coord y,  clave sol 
#import gtk
import random
import math
import gobject
import pysynth
import os
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#import menu_desplegable
prefix_path = "data/images/"
######
negra = QImage(prefix_path+"negra.png",'PNG')
negra = QImage(prefix_path+"negra_selected.png",'PNG')

#blanca = gtk.gdk.pixbuf_new_from_file_at_size(prefix_path+"blanca.png", 50, 48)
#blanca_selected = gtk.gdk.pixbuf_new_from_file_at_size(prefix_path+"blanca_selected.png", 50, 48)

notas = ["c", "d", "e", "f", "g", "a", "b"]
class Compose:
    def movsym(self, widget, event):
        print event.keyval
        #self.area.grab_focus()
        #65362 flechita arriba
        #65364 flechita abajo
        for elemento in self.lista:
            if elemento[2] == "negra_selected":
                if event.keyval == 65362:
                    elemento[1] -= 6
        #self.draw_notes()
        #self.area.modify_bg(2, gtk.gdk.Color(red=1000, green=0, blue=0, pixel=25))
        self.draw_notes()
        return True
    def add_symbol(self, widget):
        print "test"
        self.new("negra",self.lista[-1][0]+20,78)
        self.draw_notes()
        return True
    def addnota(self, nota, num):
     anota = nota[0]
     anum = int(nota.replace(anota, ""))
     if num >= 7-notas.index(anota):
      anum += 1
      anum += (num-(7-notas.index(anota)))/7
     anota = notas[(notas.index(anota)+num)%7]
     return "%s%d" % (anota, anum)
     
    def play_function(self, w, data):
        print "clicked"
        to_play = []
        for elemento in self.lista:
            #elemento[1] es y
            #y de c3 do central es 78
            #6 y entre nota
            to_play.append((self.addnota("c3", (78-elemento[1])/6),3))
        #print to_play
        pysynth.make_wav(to_play, fn="./notas.wav")
        os.system("padsp python player.py notas.wav")
        os.remove("notas.wav")
        #print self.lista
            
            

    def get_main_menu(self, window):
        accel_group = gtk.AccelGroup()
        item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)
        item_factory.create_items(self.menu_items)
        window.add_accel_group(accel_group)
        self.item_factory = item_factory
        return item_factory.get_widget("<main>")

    def detect_click(self, widget, event):
        for elemento in self.lista:
            if elemento[3] == "no_volteada" and elemento[2] == "negra":   
                if event.x-10 >= elemento[0]:
                    if event.x-10 <= elemento[0]+13:
                        if event.y-100 >= elemento[1]:#despues ver con las no volteadas
                            if event.y-28 <= elemento[1]+120:#despues ver con las no volteadas
                                #print elemento
                                for elemento2 in self.lista:
                                 elemento2[2] = elemento2[2].replace("_selected", "")
                                elemento[2] = "negra_selected"
                                print self.lista.index(elemento)
                                if elemento != -1:
                                   self.lista[(self.lista.index(elemento)-1)][2] = "negra"
                                if elemento < len(self.lista):
                                    self.lista[(self.lista.index(elemento)+1)][2] = "negra"
                                self.draw_notes()
                                
                                    
            else:#volteados
                if event.x-10 >= elemento[0]:
                    if event.x-10 <= elemento[0]+29:
                        if event.y-135 >= elemento[1]:
                            if event.y-136 <= elemento[1]+92:
                                print 'nota'  
        return
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.menu_items = (
            ( "/_File",         None,         None, 0, "<Branch>" ),
            ( "/File/_New",     "<control>N", None, 0, None ),
            ( "/File/_Open",    "<control>O", None, 0, None ),
            ( "/File/_Save",    "<control>S", None, 0, None ),
            ( "/File/Save _As", None,         None, 0, None ),
            ( "/File/sep1",     None,         None, 0, "<Separator>" ), #separador
            ("/File/Export as PDF", None, None, 0, None),
            ( "/File/Quit",     "<control>Q", QtCore.QCoreApplication.instance().quit, 0, None ),
            ( "/_Options",      None,         None, 0, "<Branch>" ),
            ( "/Options/Play",  None,         self.play_function, 0, None ),
            ( "/_Help",         None,         None, 0, "<LastBranch>" ),
            ( "/_Help/About",   None,         None, 0, None ),
            ( "/_Help/Update",  None,         None, 0, None ),
            )
        self.cursor = -1
        self.lista = []
        app = QtGui.QApplication(sys.argv)
        window = QtGui.QWidget()
        window.setWindowTitle("Compose 0.0.1.0")
        window.connect(window, SIGNAL('triggered()'), lambda q: QtCore.QCoreApplication.instance().quit)
        #no olvidar pasar#window.add_events(gtk.gdk.MOTION_NOTIFY | gtk.gdk.BUTTON_PRESS)
        vbox = QVBoxLayout()
        self.area = QPainter()
        tile = QPixmap(QSize(400, 300))
        self.area.fillRect(0, 0, tile.width(), tile.height())
        self.area.set_events(gtk.gdk.POINTER_MOTION_MASK |
                             gtk.gdk.POINTER_MOTION_HINT_MASK |
                             gtk.gdk.EXPOSURE_MASK|
                             gtk.gdk.LEAVE_NOTIFY_MASK|
                             gtk.gdk.BUTTON_PRESS_MASK|
                             gtk.gdk.KEY_PRESS_MASK | 
                             gtk.gdk.KEY_RELEASE_MASK 
                             )
        self.area.connect("expose-event", self.area_expose_cb)
        self.area.connect("button-press-event", self.detect_click)
        self.area.connect("key-press-event", self.movsym)
        self.area.set_flags(gtk.CAN_FOCUS)
        

        self.new("negra", 70, 48)#dif 6 
        #36
        self.new("negra", 90, 66)
        self.new("negra", 110, 78)#do central(c3)
        
        menubar = self.get_main_menu(window)
        toolbar = gtk.Toolbar()
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        
        saveb = gtk.ToolButton(gtk.STOCK_SAVE)
        saveb.set_tooltip_text("Save the current proyect")
        openb = gtk.ToolButton(gtk.STOCK_OPEN)
        openb.set_tooltip_text("Open a proyect")
        playb = gtk.ToolButton("gtk-media-play")
        playb.set_tooltip_text("Play the current proyect")
        addsb = gtk.ToolButton(gtk.STOCK_ADD)
        selectm = gtk.ToolItem()
        selectm.add(menu_desplegable.combo)
        toolbar.insert(saveb, 0)
        toolbar.insert(openb, 1)
        toolbar.insert(playb, 2)
        toolbar.insert(selectm, 3)
        toolbar.insert(addsb, 4)
        
        vbox.pack_start(menubar, False, True, 0)
        vbox.pack_start(toolbar, False, False, 1)
        vbox.pack_start(self.area, False, True, 2)
        
        addsb.connect("clicked", self.add_symbol)
        playb.connect("clicked", self.play_function)
        
        window.add(vbox)
        menubar.show()
        toolbar.show_all()
        vbox.show()
        self.area.show()
        window.show()
        self.area.grab_focus()
        return 

    def area_expose_cb(self, area, event):
        self.style = self.area.get_style()
        self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
        self.gc.line_width = 1
        #9 arriba linea adicional
        self.draw(10, 100)
        self.draw_notes()
        return True

    def draw(self, x, y):
        segmentssol = ((x+10,y+60 , x+320,y+60), 
                    (x+10, y+72 , x+320, y+72),
                    (x+10, y+84 , x+320, y+84),
                    (x+10, y+96 , x+320, y+96),
                    (x+10, y+108 , x+320, y+108),
                    (x+320, y+60 , x+320, y+108))
        self.area.window.draw_segments(self.gc, segmentssol)
        pixbuf = gtk.gdk.pixbuf_new_from_file(prefix_path+"clave_sol.png") #one way to load a pixbuf
        self.area.window.draw_pixbuf(self.gc, pixbuf, 0, 0, x+10, y+42, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
        
    def draw_notes(self):
        for elemento in self.lista:
            if elemento[3] == "no_volteada":
                if elemento[2] == "negra_selected":
                    self.area.window.draw_pixbuf(self.gc, negra_selected, 0, 0, 10+elemento[0], 100+elemento[1], -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                    if elemento[1] <= 43:
                        self.area.window.draw_pixbuf(self.gc, negra_selected.rotate_simple(180), 0, 0, 10+elemento[0], 100+elemento[1]+36, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                        self.area.modify_bg(2, gtk.gdk.Color(red=1000, green=0, blue=0, pixel=25))
                else:
                    if elemento[1] <= 43:
                        self.area.window.draw_pixbuf(self.gc, negra.rotate_simple(180), 0, 0, 10+elemento[0], 100+elemento[1]+36, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                        self.area.modify_bg(2, gtk.gdk.Color(red=1000, green=0, blue=0, pixel=25))
                        
                    elif elemento[1] == 78:
                        self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+142, elemento[0]+27, elemento[1]+142)
                        self.area.window.draw_pixbuf(self.gc, negra, 0, 0, 10+elemento[0], 100+elemento[1], -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                    elif elemento[1] == 90:
                        self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+142, elemento[0]+27, elemento[1]+142)
                        self.area.window.draw_pixbuf(self.gc, negra, 0, 0, 10+elemento[0], 100+elemento[1], -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                    elif elemento[1] == 102:
                        self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+142, elemento[0]+27, elemento[1]+142)
                        self.area.window.draw_pixbuf(self.gc, negra, 0, 0, 10+elemento[0], 100+elemento[1], -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                    elif elemento[1] == 114:
                        self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+142, elemento[0]+27, elemento[1]+142)
                        self.area.window.draw_pixbuf(self.gc, negra, 0, 0, 10+elemento[0], 100+elemento[1], -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                    else:
                        self.area.window.draw_pixbuf(self.gc, negra, 0, 0, 10+elemento[0], 100+elemento[1], -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
            elif elemento[3] == "volteada":
                if elemento[1] == 6:
                    self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+142, elemento[0]+27, elemento[1]+142)
                    self.area.window.draw_pixbuf(self.gc, negra.rotate_simple(180), 0, 0, 10+elemento[0], 100+elemento[1]+36, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                elif elemento[1] == -6:
                    self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+142, elemento[0]+27, elemento[1]+142)
                    self.area.window.draw_pixbuf(self.gc, negra.rotate_simple(180), 0, 0, 10+elemento[0], 100+elemento[1]+36, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                elif elemento[1] == -18:
                    self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+142, elemento[0]+27, elemento[1]+142)
                    self.area.window.draw_pixbuf(self.gc, negra.rotate_simple(180), 0, 0, 10+elemento[0], 100+elemento[1]+36, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                elif elemento[1] == 15:
                    self.area.window.draw_line(self.gc, elemento[0]+5, elemento[1]+144, elemento[0]+27, elemento[1]+144)
                    self.area.window.draw_pixbuf(self.gc, negra.rotate_simple(180), 0, 0, 10+elemento[0], 100+elemento[1]+36, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
                else:
                    self.area.window.draw_pixbuf(self.gc, negra.rotate_simple(180), 0, 0, 10+elemento[0], 100+elemento[1]+36, -1, -1, gtk.gdk.RGB_DITHER_NONE, 0, 0)
        return True

    def new(self, what_type, posx, posy):
        if what_type == "negra":
            if posy <= 43:
                self.lista.append([posx, posy, "negra", "volteada"])
            else:
                self.lista.append([posx, posy, "negra", "no_volteada"])
        if what_type == "blanca":
            if posy <= 43:
                self.lista.append([posx, posy, "blanca", "volteada"])
            else:
                self.lista.append([posx, posy, "blanca", "no_volteada"])
        if what_type == "redonda":
            if posy <= 43:
                self.lista.append([posx, posy, "redonda", "volteada"])
            else:
                self.lista.append([posx, posy, "redonda", "no_volteada"])
        if what_type == "longa":
            if posy <= 43:
                self.lista.append([posx, posy, "longa", "volteada"])
            else:
                self.lista.append([posx, posy, "longa", "no_volteada"])
        if what_type == "cuadrada":
            if posy <= 43:
                self.lista.append([posx, posy, "cuadrada", "volteada"])
            else:
                self.lista.append([posx, posy, "cuadrada", "no_volteada"])
        if what_type == "corchea":
            if posy <= 43:
                self.lista.append([posx, posy, "corchea", "volteada"])
            else:
                self.lista.append([posx, posy, "corchea", "no_volteada"])
        if what_type == "semi_corchea":
            if posy <= 43:
                self.lista.append([posx, posy, "semi_corchea", "volteada"])
            else:
                self.lista.append([posx, posy, "semi_corchea", "no_volteada"])
        if what_type == "fusa":
            if posy <= 43:
                self.lista.append([posx, posy, "fusa", "volteada"])
            else:
                self.lista.append([posx, posy, "fusa", "no_volteada"])
        if what_type == "semi_fusa":
            if posy <= 43:
                self.lista.append([posx, posy, "semi_fusa", "volteada"])
            else:
                self.lista.append([posx, posy, "semi_fusa", "no_volteada"])
        if what_type == "garrapatea":
            if posy <= 43:
                self.lista.append([posx, posy, "garrapatea", "volteada"])
            else:
                self.lista.append([posx, posy, "garrapatea", "no_volteada"])
        if what_type == "semi_garrapatea":
            if posy <= 43:
                self.lista.append([posx, posy, "semi_garrapatea", "volteada"])
            else:
                self.lista.append([posx, posy, "semi_garrapatea", "no_volteada"])
        return

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    Compose()
    main()
