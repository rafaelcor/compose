#!/usr/bin/env python

import gtk, os

for fname in os.listdir("."):
 if not ".png" in fname:
  continue
 pixbuf = gtk.gdk.pixbuf_new_from_file(fname)
 pixels = pixbuf.get_pixels()
 npixels = []
 for x in range(pixbuf.get_width()*pixbuf.get_height()):
  if pixels[x*4]+pixels[(x*4)+1]+pixels[(x*4)+2]+pixels[(x*4)+3] == "\x00\x00\x00@":
   npixels.append("\x00\x00\x00\x00")
  else:
   npixels.append(pixels[x*4]+pixels[(x*4)+1]+pixels[(x*4)+2]+pixels[(x*4)+3])
 npixbuf = gtk.gdk.pixbuf_new_from_data("".join(npixels), pixbuf.get_colorspace(), pixbuf.get_has_alpha(), pixbuf.get_bits_per_sample(), pixbuf.get_width(), pixbuf.get_height(), pixbuf.get_rowstride())
 npixbuf.save(fname, "png")
 print "Editado", fname
