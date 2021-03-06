# -*- coding: utf-8 -*-
import cairo


text=u'HELLO HS'
font="Sans"
font_size=20.0
font_args=[cairo.FONT_SLANT_NORMAL]

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
ctx = cairo.Context(surface)
ctx.select_font_face(font, *font_args)
ctx.set_font_size(font_size)
x_bearing,y_bearing,text_width,text_height,x_advance,y_advance=ctx.text_extents(text)
ctx.move_to(-x_bearing, -y_bearing)
ctx.text_path(text)
pts=ctx.copy_path_flat()
#pts=ctx.copy_path()
cur_segment_start=(0.0,0.0)
feed=""
g_code=['G21 G90 G64 G40','G0 Z3.0','M3 S10000']
for p in pts:
  if p[0] == 0:
    g_code.append('G0 Z3.0')
    g_code.append('G0 X%2.5f Y%2.5f' % (p[1][0],text_height-p[1][1]))
    g_code.append('G1 F100.0 Z-2.0')
    cur_segment_start=(p[1][0],text_height-p[1][1])
    feed="F400.0"
  elif(p[0] == 1):
    g_code.append('G1 %s X%2.5f Y%2.5f' % (feed,p[1][0],text_height-p[1][1]))
    feed=""
  elif(p[0] == 2):
    start=(p[1][0],p[1][1])
    middle=(p[1][2],p[1][3])
    end=(p[1][4],p[1][5])
    g_code.append('G2 X%2.5f Y%2.5f I%2.5f J%2.5f' % (start[0],start[1],0.0,0.0))
  elif(p[0] == 3):
    g_code.append('G1 X%2.5f Y%2.5f' % cur_segment_start)

g_code.append('G0 Z3.0')
g_code.append('M5')
g_code.append('M2')
#for p in pts:
#  print p

for l in g_code:
  print l
