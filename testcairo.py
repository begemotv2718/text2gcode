import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
ctx = cairo.Context(surface)
ctx.set_line_width(1)
ctx.set_source_rgb(1,1,1)
scale=50.0
xoffset=50.0*scale
ctx.move_to(56.015625*scale-xoffset, 2.0*scale)
#ctx.curve_to(54.47265625*scale-xoffset, 2.0*scale, 53.25*scale-xoffset, 2.49609375*scale, 52.34375*scale-xoffset, 3.484375*scale)
for p in [(54.47265625, 2.0, 53.25, 2.49609375, 52.34375, 3.484375),(51.4453125, 4.46484375, 51.0, 5.8046875, 51.0, 7.5),(51.0, 9.19921875, 51.4453125, 10.54296875, 52.34375, 11.53125),(53.25, 12.51171875, 54.47265625, 13.0, 56.015625, 13.0),(57.546875, 13.0, 58.7578125, 12.51171875, 59.65625, 11.53125), (60.55078125, 10.54296875, 61.0, 9.19921875, 61.0, 7.5),(61.0, 5.8046875, 60.55078125, 4.46484375, 59.65625, 3.484375),(58.7578125, 2.49609375, 57.546875, 2.0, 56.015625, 2.0)]:
    ctx.curve_to(p[0]*scale-xoffset,p[1]*scale,p[2]*scale-xoffset,p[3]*scale,p[4]*scale-xoffset,p[5]*scale)
ctx.stroke()
ctx.set_source_rgb(0,1,0)
ctx.move_to(56.015625*scale-xoffset, 2.0*scale)
for p in [(54.47265625, 2.0, 53.25, 2.49609375, 52.34375, 3.484375),(51.4453125, 4.46484375, 51.0, 5.8046875, 51.0, 7.5),(51.0, 9.19921875, 51.4453125, 10.54296875, 52.34375, 11.53125),(53.25, 12.51171875, 54.47265625, 13.0, 56.015625, 13.0),(57.546875, 13.0, 58.7578125, 12.51171875, 59.65625, 11.53125), (60.55078125, 10.54296875, 61.0, 9.19921875, 61.0, 7.5),(61.0, 5.8046875, 60.55078125, 4.46484375, 59.65625, 3.484375)]:
    ctx.line_to(p[0]*scale-xoffset,p[1]*scale)
    ctx.line_to(p[2]*scale-xoffset,p[3]*scale)
    ctx.line_to(p[4]*scale-xoffset,p[5]*scale)
ctx.stroke()

surface.write_to_png("/tmp/test.png")
'''
(0, (56.015625, 2.0))
(2, (54.47265625, 2.0, 53.25, 2.49609375, 52.34375, 3.484375))
(2, (51.4453125, 4.46484375, 51.0, 5.8046875, 51.0, 7.5))
(2, (51.0, 9.19921875, 51.4453125, 10.54296875, 52.34375, 11.53125))
(2, (53.25, 12.51171875, 54.47265625, 13.0, 56.015625, 13.0))
(2, (57.546875, 13.0, 58.7578125, 12.51171875, 59.65625, 11.53125))
(2, (60.55078125, 10.54296875, 61.0, 9.19921875, 61.0, 7.5))
(2, (61.0, 5.8046875, 60.55078125, 4.46484375, 59.65625, 3.484375))
(2, (58.7578125, 2.49609375, 57.546875, 2.0, 56.015625, 2.0))
(3, ())
'''
