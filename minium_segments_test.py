#!/usr/bin/env python

import gtk

class DrawingAreaExample:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Drawing Area Example")
        window.connect("destroy", lambda w: gtk.main_quit())
        self.area = gtk.DrawingArea()
        self.area.set_size_request(400, 300)
        #self.pangolayout = self.area.create_pango_layout("")


        self.area.set_events(gtk.gdk.POINTER_MOTION_MASK |
                             gtk.gdk.POINTER_MOTION_HINT_MASK )
        self.area.connect("expose-event", self.area_expose_cb)

        window.add(self.area)
        self.area.show()
        window.show()

    def area_expose_cb(self, area, event):
        self.style = self.area.get_style()
        self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
        self.draw_segments(10, 100)

        return True



    def draw_segments(self, x, y):
        segments = ((x+20,y+10, x+20,y+70), (x+60,y+10, x+60,y+70),
            (x+10,y+30 , x+70,y+30), (x+10, y+50 , x+70, y+50))
        self.area.window.draw_segments(self.gc, segments)
        #self.pangolayout.set_text("Segments")
        #self.area.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)
        return



def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    DrawingAreaExample()
    main()
