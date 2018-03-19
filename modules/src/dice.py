import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import modules
from templates.attachment import AttachmentTemplate
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {
    1: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-one/256/0/e74c3c_none.png',
    2: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-two/256/0/e74c3c_none.png',
    3: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-three/256/0/e74c3c_none.png',
    4: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-four/256/0/e74c3c_none.png',
    5: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-five/256/0/e74c3c_none.png',
    6: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-six/256/0/e74c3c_none.png'
}
# def text2png(text, fullpath, color = "#000", bgcolor = "#FFF", fontfullpath = None, fontsize = 13, leftpadding = 3, rightpadding = 3, width = 200):
#     REPLACEMENT_CHARACTER = u'\uFFFD'
#     NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '

#     #prepare linkback
#     # linkback = "created via http://ourdomain.com"
#     fontlinkback = ImageFont.truetype('FreeMono.ttf', 8)
#     linkbackx = fontlinkback.getsize(linkback)[0]
#     linkback_height = fontlinkback.getsize(linkback)[1]
#     #end of linkback

#     font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(fontfullpath, fontsize)
#     text = text.replace('\n', NEWLINE_REPLACEMENT_STRING)

#     lines = []
#     line = u""

#     for word in text.split():
#         print word
#         if word == REPLACEMENT_CHARACTER: #give a blank line
#             lines.append( line[1:] ) #slice the white space in the begining of the line
#             line = u""
#             lines.append( u"" ) #the blank line
#         elif font.getsize( line + ' ' + word )[0] <= (width - rightpadding - leftpadding):
#             line += ' ' + word
#         else: #start a new line
#             lines.append( line[1:] ) #slice the white space in the begining of the line
#             line = u""

#             #TODO: handle too long words at this point
#             line += ' ' + word #for now, assume no word alone can exceed the line width

#     if len(line) != 0:
#         lines.append( line[1:] ) #add the last line

#     line_height = font.getsize(text)[1]
#     img_height = line_height * (len(lines) + 1)

#     img = Image.new("RGBA", (width, img_height), bgcolor)
#     draw = ImageDraw.Draw(img)

#     y = 0
#     for line in lines:
#         draw.text( (leftpadding, y), line, color, font=font)
#         y += line_height

#     # add linkback at the bottom
#     # draw.text( (width - linkbackx, img_height - linkback_height), linkback, color, font=fontlinkback)

#     img.save(fullpath)

def process(input, entities=None):
    # message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
    # message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
    # message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
    # message=input
    upperLimit = input.split(' ')
    # message=int(upperLimit[1])
    if upperLimit[1].isdigit():
        msg=random.randint(1,int(upperLimit[1]))
        # img = Image.new('RGB', (200, 100))
        # d = ImageDraw.Draw(img)
        # d.text((20, 20),str(message), fill=(255, 0, 0))
        
        #try 2
        # i = Image.new("RGB", (255,255))
        # d = ImageDraw.Draw(i)
        # f = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28)
        # d.text((0,0), str(message), font=f)
        # i.save(open("result.png", "wb"), "PNG")
        #try 2 end


        # try 3
        # text2png(str(msg), 'test.png', fontfullpath = "FreeMono.ttf")
        # message = AttachmentTemplate('test.png', type='image').get_message()
        # try 3 end

        # img = Image.open('test.png')
        # img.show()
        # message = img
        message=TextTemplate(str(msg)).get_message()
        # path = "../../../../../../home/snehith/Desktop/JARVIS-on-Messenger/images/"
        # valid_images = [".jpg",".gif",".png",".tga"]
        # if f in os.listdir(path):
        #     ext = os.path.splitext(f)[1]
        #     if ext.lower() not in valid_images:
        #         continue
        #     else:
        #         images = map(Image.open(os.path.join(path,f), ['powered_by_tmdb.png', 'powered_by_tmdb.png'])
        #         widths, heights = zip(*(i.size for i in images))

        #         total_width = sum(widths)
        #         max_height = max(heights)

        #         new_im = Image.new('RGB', (total_width, max_height))

        #         x_offset = 0

        #         for im in images:
        #           new_im.paste(im, (x_offset,0))
        #           x_offset += im.size[0]

        #         new_im.save('test.jpg')
    else:
        message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
        message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
        message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
