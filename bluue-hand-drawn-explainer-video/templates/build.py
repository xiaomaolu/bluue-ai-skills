import re, base64, os
src=open('hr.html').read()
r=re.sub(r'<link rel="preconnect"[^>]*>\n','',src); r=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>','<meta charset="utf-8">',r)
open('render.html','w').write(r)
web=src
if os.path.exists('mix.mp3'):
    b=base64.b64encode(open('mix.mp3','rb').read()).decode()
    web=web.replace('<!--AUDIO-->',f'<audio id="narr" preload="auto" src="data:audio/mpeg;base64,{b}"></audio>')
open('hr_web.html','w').write(web); print('built')
