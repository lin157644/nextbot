from PIL import Image

i=0
while i<7770:
    i = i + 24
    img = Image.open(f'newframes/frame{i}.png')
    img = img.resize((70,20)).convert('L')
    img.save(f'newframes/frame{i}.png')
