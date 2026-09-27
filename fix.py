import glob

for page in glob.glob('/home/jeffer/proyectos/reyes-computing/*.html'):
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('fa-whatsap|', 'fa-whatsapp').replace('fa-whatsap|', 'fa-whatsapp')
    with open(page, 'w', encoding='utf-8') as f:
        f.write(c)

print('Updated all HTML files!')
