import gtk
prefix_path = "data/images/"

lista_simbolos = [gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "longa.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "cuadrada.png", 30, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "redonda.png", 21, 19),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "blanca.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "negra.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "corchea.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "semicorchea.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "fusa.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "semifusa.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "garrapatea.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "semigarrapatea.png", 50, 48),#
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_longa.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_cuadrada.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_redonda.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_blanca.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_negra.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_corchea.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_semicorchea.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_fusa.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_semifusa.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_garrapatea.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_semigarrapatea.png", 50, 48)]

lista_nombres = ["longa",
				  "cuadrada",
				  "redonda",
				  "blanca",
				  "negra",
				  "corchea",
				 "semicorchea",
				  "fusa",
				  "semifusa",
				  "garrapatea",
				  "semigarrapatea",#
				  "silencio_longa",
				  "silencio_cuadrada",
				  "silencio_redonda",
				  "silencio_blanca",
				  "silencio_negra",
				  "silencio_corchea",
				  "silencio_semicorchea",
				  "silencio_fusa",
				  "silencio_semifusa",
				  "silencio_garrapatea",
				  "silencio_semigarrapatea"]

lista_simbolos_selected = [gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "longa_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "cuadrada_selected.png", 30, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "redonda_selected.png", 21, 19),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "blanca_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "negra_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "corchea_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "semicorchea_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "fusa_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "semifusa_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "garrapatea_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "semigarrapatea_selected.png", 50, 48),#
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_longa_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_cuadrada_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_redonda_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_blanca_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_negra_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_corchea_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_semicorchea_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_fusa_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_semifusa_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_garrapatea_selected.png", 50, 48),
				  gtk.gdk.pixbuf_new_from_file_at_size(prefix_path + "silencio_semigarrapatea_selected.png", 50, 48)]

lista_selected = ["longa_selected",
				  "cuadrada_selected",
				  "redonda_selected",
				  "blanca_selected",
				  "negra_selected",
				  "corchea_selected",
				 "semicorchea_selected",
				  "fusa_selected",
				  "semifusa_selected",
				  "garrapatea_selected",
				  "semigarrapatea_selected",
				  "silencio_longa_selected",
				  "silencio_cuadrada_selected",
				  "silencio_redonda_selected",
				  "silencio_blanca_selected",
				  "silencio_negra_selected",
				  "silencio_corchea_selected",
				  "silencio_semicorchea_selected",
				  "silencio_fusa_selected",
				  "silencio_semifusa_selected",
				  "silencio_garrapatea_selected",
				  "silencio_semigarrapatea_selected"]