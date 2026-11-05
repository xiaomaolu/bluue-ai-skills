# -*- coding: utf-8 -*-
# 汉隆剃刀 · 9:16 hand-drawn line-art explainer (violet accent)
import json, math
import helpers as H
from helpers import INK, ACC, PAPER, GREY, bubble, head, star, A
from lines import L
D = json.load(open('durs.json'))
by_scene = {}
for id_, sc, disp, sp, spd in L: by_scene.setdefault(sc, []).append((id_, disp))
LEAD = {0: 0.6, 1: 0.6, 2: 0.6, 3: 0.6, 4: 0.7, 5: 0.6, 6: 0.8}
GAP = {0: 0.45, 1: 0.45, 2: 0.4, 3: 0.4, 4: 0.45, 5: 0.4, 6: 0.8}
TAIL = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.2, 5: 1.0, 6: 4.0}
TS, SC = {}, []
t = 0.0
for sc in sorted(by_scene):
    s = t; t += LEAD[sc]
    for i, (id_, _) in enumerate(by_scene[sc]):
        if i: t += GAP[sc]
        TS[id_] = t; t += D[id_]['dur']
    t += TAIL[sc]; SC.append((s, t))
T = round(t, 2)
json.dump({'T': T, 'TS': TS}, open('timeline.json', 'w'))
def rel(id_, sc, f=0.0): return round(TS[id_] + D[id_]['dur'] * f - SC[sc][0], 3)
H.by_scene = by_scene; H.rel = rel
subs = H.subs

def frame(x, y, w, h, sw=10, col=INK):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
            f'<rect x="{x + 16}" y="{y + 16}" width="{w - 32}" height="{h - 32}" fill="none" stroke="{col}" stroke-width="{sw * 0.35:.1f}"/>')

def screen(x, y, w, h, sad=True, stand=True):
    g = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{ACC}" stroke="{INK}" stroke-width="7"/>'
    if sad:
        g += (f'<text x="{x + w * 0.12}" y="{y + h * 0.45}" class="t" style="font-size:{h * 0.32:.0f}px;font-weight:900;fill:#fff">:(</text>'
              f'<path d="M{x + w * 0.12} {y + h * 0.62} L {x + w * 0.8} {y + h * 0.62} M{x + w * 0.12} {y + h * 0.76} L {x + w * 0.6} {y + h * 0.76}" stroke="#fff" stroke-width="{max(3, h * 0.04):.0f}" opacity="0.8"/>')
    if stand:
        g += f'<path d="M{x + w / 2} {y + h} L {x + w / 2} {y + h + 30} M{x + w / 2 - 40} {y + h + 30} L {x + w / 2 + 40} {y + h + 30}" stroke="{INK}" stroke-width="7"/>'
    return g

def plane(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-90 0 C -60 -14, 60 -14, 90 0 C 60 14, -60 14, -90 0 Z" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>'
            f'<path d="M-10 -6 L -40 -60 L -10 -60 L 30 -6 M-10 6 L -40 60 L -10 60 L 30 6 M-70 -4 L -90 -36 L -74 -36 L -56 -6" fill="{PAPER}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/></g>')

def hacker(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-70 90 C -80 0, -50 -80, 0 -80 C 50 -80, 80 0, 70 90 Z" fill="{INK}"/>'
            f'<ellipse cx="0" cy="-10" rx="34" ry="40" fill="{PAPER}"/><path d="M-20 -14 L -6 -8 M20 -14 L 6 -8" stroke="{INK}" stroke-width="5"/>'
            f'<text x="0" y="30" text-anchor="middle" class="t" style="font-size:44px;font-weight:900">?</text></g>')

def razor(x, y, s=1, rot=-20):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M-160 -20 L 40 -20 C 70 -20, 80 0, 80 10 L -160 10 Z" fill="{PAPER}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
            f'<path d="M-160 10 L 60 10" stroke="{ACC}" stroke-width="5"/><circle cx="50" cy="-5" r="7" fill="{INK}"/>'
            f'<path d="M50 -5 L 220 -60 L 240 -40 L 60 6 Z" fill="{INK}"/></g>')

def ruler(x, y, s=1, rot=20):
    ticks = ''.join(f'<path d="M{-150 + k * 30} -20 L {-150 + k * 30} {-20 + (22 if k % 2 == 0 else 12)}" stroke="{INK}" stroke-width="4"/>' for k in range(11))
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><rect x="-170" y="-20" width="340" height="50" rx="6" fill="{ACC}" stroke="{INK}" stroke-width="7"/>{ticks}</g>'

S = []
# ---------- 0 · cover + global blue screen ----------
a = lambda i, f=0: rel(i, 0, f)
screens = ''.join(f'<g class="pop" data-at="{a("a1", .15 + k * 0.08):.2f}" data-c="{x + 90},{y + 60}">{screen(x, y, 180, 120)}</g>' for k, (x, y) in enumerate([(150, 900), (450, 880), (750, 900), (300, 1080), (600, 1080)]))
S.append(f'''<g class="rough">
<g class="fade" data-at="0">
  {frame(150, 300, 780, 300, 12)}
  <text x="540" y="498" text-anchor="middle" class="t" style="font-size:150px;font-weight:900;letter-spacing:8px">汉隆<tspan fill="{ACC}">剃刀</tspan></text>
  <text x="540" y="560" text-anchor="middle" class="t" style="font-size:24px;fill:{GREY};letter-spacing:8px">HANLON'S RAZOR</text>
  <text x="540" y="710" text-anchor="middle" class="t" style="font-size:54px;font-weight:900">全世界同时蓝屏</text>
  <text x="540" y="788" text-anchor="middle" class="t" style="font-size:54px;font-weight:900">是谁在<tspan fill="{ACC}">搞鬼</tspan>？</text>
</g>
<g class="fade" data-at="0" data-out="{a('a1', .12)}">{screen(390, 900, 300, 190)}</g>
<g class="fade" data-at="{a('a1', .1)}" data-out="{a('a3') - 0.3}">{screens}</g>
<g class="slide" data-at="{a('a2', .1)}" data-out="{a('a3') - 0.3}" data-from="0,20">{plane(540, 1300, .8)}<path d="M430 1350 L 650 1350" stroke="{INK}" stroke-width="6"/><text x="700" y="1320" class="t" style="font-size:30px;font-weight:900;fill:{ACC}">停飞</text></g>
<g class="pop" data-at="{a('a2', .45)}" data-out="{a('a3') + 1.0}" data-c="860,760" data-sfx="pop">{bubble(740, 640, 240, 220, 700, 900, 'none', sw=6)}{hacker(860, 740, .9)}</g>
<g class="pop" data-at="{a('a3', .15)}" data-out="{a('a3') + 1.0}" data-c="860,750"><path d="M760 660 L 960 840 M960 660 L 760 840" stroke="{ACC}" stroke-width="12"/></g>
<g class="fade" data-at="{a('a3', .3)}">
  <rect x="150" y="900" width="360" height="200" rx="16" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>
  <text x="330" y="975" text-anchor="middle" class="t" style="font-size:40px;font-weight:900">安全软件更新</text>
  <rect x="200" y="1010" width="260" height="30" rx="8" fill="none" stroke="{INK}" stroke-width="5"/><g data-anim="fill" data-a="{a('a3', .3)}" data-b="{a('a3', .9)}"><rect x="204" y="1014" width="0" height="22" fill="{ACC}"/></g>
  <text x="330" y="1084" text-anchor="middle" class="t" style="font-size:26px;fill:{GREY}">有缺陷的一行配置</text></g>
<g class="slide" data-at="{a('a4', .1)}" data-from="0,30" data-sfx="pop"><text x="760" y="1040" text-anchor="middle" class="t" style="font-size:110px;font-weight:900;fill:{ACC}">850万</text><text x="760" y="1100" text-anchor="middle" class="t" style="font-size:32px;font-weight:700">台电脑崩溃（估计）</text></g>
<text class="foot fade" data-at="{a('a3', .3)}" x="540" y="1380" text-anchor="middle">2024 年 7 月 19 日 · 已隐去公司名称</text>
</g>
{subs(0)}''')

# ---------- 1 · concept ----------
b = lambda i, f=0: rel(i, 1, f)
S.append(f'''<g class="rough">
<g class="fade" data-at="0.1" data-out="{b('b3') - 0.3}">{head(540, 900, 90, 0, 'flat', 0)}
  {bubble(640, 560, 300, 200, 600, 820, 'none', sw=6)}
  <g data-anim="shave" data-a="{b('b2', .2)}" data-b="{b('b2', .55)}"><path d="M720 600 L 750 540 L 770 610 M840 610 L 860 540 L 890 600" fill="{ACC}" stroke="{INK}" stroke-width="5"/></g>
  <text x="790" y="690" text-anchor="middle" class="t" style="font-size:40px;font-weight:900">他故意的</text>
  <path d="M700 676 L 880 676" class="fade" data-at="{b('b2', .6)}" stroke="{ACC}" stroke-width="9"/></g>
<g class="slide" data-at="{b('b2', .15)}" data-out="{b('b3') - 0.3}" data-from="200,-80" data-sfx="pop">{razor(690, 520, 1.0, -15)}</g>
<g class="slide" data-at="{b('b2', .05)}" data-from="0,20"><text x="540" y="400" text-anchor="middle" class="t" style="font-size:100px;font-weight:900">汉隆<tspan fill="{ACC}">剃刀</tspan></text></g>
<g class="slide" data-at="{b('b3', .2)}" data-from="0,30" data-sfx="pop">
  <rect x="140" y="1110" width="380" height="200" rx="20" fill="{PAPER}" stroke="{GREY}" stroke-width="6" stroke-dasharray="14 10"/>
  <text x="330" y="1200" text-anchor="middle" class="t" style="font-size:48px;font-weight:900;fill:{GREY}">恶意</text><text x="330" y="1260" text-anchor="middle" class="t" style="font-size:28px;fill:{GREY}">先放一放</text>
  <rect x="560" y="1110" width="380" height="200" rx="20" fill="{ACC}" stroke="{INK}" stroke-width="6"/>
  <text x="750" y="1190" text-anchor="middle" class="t" style="font-size:38px;font-weight:900;fill:#fff">疏忽 · 误会</text><text x="750" y="1250" text-anchor="middle" class="t" style="font-size:38px;font-weight:900;fill:#fff">系统问题</text></g>
</g>
{subs(1)}''')

# ---------- 2 · Jones & Harris ----------
c = lambda i, f=0: rel(i, 2, f)
S.append(f'''<g class="rough">
<g class="slide" data-at="{c('c1', .3)}" data-from="-40,0" data-sfx="pop">
  <rect x="140" y="380" width="320" height="400" rx="12" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>
  <text x="300" y="450" text-anchor="middle" class="t" style="font-size:36px;font-weight:900">支持卡斯特罗</text>
  {''.join(f'<path d="M180 {500 + k * 46} L {420 - (k % 3) * 40} {500 + k * 46}" stroke="{GREY}" stroke-width="6"/>' for k in range(6))}</g>
<g class="slide" data-at="{c('c2', .2)}" data-from="0,-30" data-sfx="pop">
  <path d="M470 560 C 540 520, 580 520, 640 560" stroke="{INK}" stroke-width="6" fill="none"/><path d="M620 540 L 642 562 L 614 574" stroke="{INK}" stroke-width="6" fill="none"/>
  <rect x="560" y="400" width="380" height="90" rx="45" fill="{ACC}" stroke="{INK}" stroke-width="6"/><text x="750" y="458" text-anchor="middle" class="t" style="font-size:34px;font-weight:900;fill:#fff">作者是被指定写的</text></g>
<g class="slide" data-at="{c('c3', .1)}" data-from="40,0" data-sfx="pop">{head(780, 720, 70, 3, 'flat', -0.6)}
  {bubble(560, 830, 420, 120, 760, 820, 'none', sw=6)}<text x="770" y="905" text-anchor="middle" class="t" style="font-size:36px;font-weight:900">他就是这么想的</text></g>
<g class="fade" data-at="{c('c4')}">
  <path d="M540 1050 L 540 1300 M440 1300 L 640 1300" stroke="{INK}" stroke-width="7"/>
  <g data-anim="tilt" data-a="{c('c4', .1)}" data-b="{c('c4', .5)}" data-cx="540" data-cy="1060">
    <path d="M300 1060 L 780 1060" stroke="{INK}" stroke-width="7"/>
    <path d="M300 1060 L 260 1140 L 340 1140 Z M780 1060 L 740 1140 L 820 1140 Z" fill="none" stroke="{INK}" stroke-width="5"/>
    <rect x="240" y="1140" width="120" height="70" rx="8" fill="{ACC}" stroke="{INK}" stroke-width="5"/><text x="300" y="1187" text-anchor="middle" class="t" style="font-size:32px;font-weight:900;fill:#fff">动机</text>
    <rect x="740" y="1140" width="80" height="50" rx="8" fill="{PAPER}" stroke="{INK}" stroke-width="5"/><text x="780" y="1174" text-anchor="middle" class="t" style="font-size:26px;font-weight:700">处境</text>
  </g></g>
<text class="foot fade" data-at="{c('c1', .3)}" x="540" y="1380" text-anchor="middle">Jones &amp; Harris, 1967 · 归因实验</text>
</g>
{subs(2)}''')

# ---------- 3 · everyday ----------
d = lambda i, f=0: rel(i, 3, f)
def pair(y, left, right, at, at2):
    return (f'<g class="slide" data-at="{at}" data-from="-30,0" data-sfx="pop"><rect x="120" y="{y}" width="400" height="150" rx="18" fill="{PAPER}" stroke="{GREY}" stroke-width="6" stroke-dasharray="14 10"/>'
            f'<text x="320" y="{y + 70}" text-anchor="middle" class="t" style="font-size:30px;fill:{GREY}">你以为</text><text x="320" y="{y + 120}" text-anchor="middle" class="t" style="font-size:38px;font-weight:900;fill:{GREY}">{left}</text></g>'
            f'<g class="slide" data-at="{at2}" data-from="30,0" data-sfx="pop"><rect x="560" y="{y}" width="400" height="150" rx="18" fill="{PAPER}" stroke="{ACC}" stroke-width="7"/>'
            f'<text x="760" y="{y + 70}" text-anchor="middle" class="t" style="font-size:30px;fill:{ACC}">更可能</text><text x="760" y="{y + 120}" text-anchor="middle" class="t" style="font-size:38px;font-weight:900">{right}</text></g>')
S.append(f'''<g class="rough">
<text class="t slide" data-at="0.1" data-from="0,20" x="540" y="400" text-anchor="middle" style="font-size:60px;font-weight:900">生活里的“剃刀时刻”</text>
{pair(500, '商家故意的', '系统派错了单', d('d1', .1), d('d3', .3))}
{pair(720, '领导折腾人', '没人负责改', d('d2', .1), d('d3', .45))}
{pair(940, '他针对我', '他没看到', d('d3', .05), d('d3', .6))}
</g>
{subs(3)}''')

# ---------- 4 · reversal: malice hiding as error ----------
e = lambda i, f=0: rel(i, 4, f)
mask = (f'<path d="M380 620 C 380 500, 700 500, 700 620 C 700 760, 620 840, 540 840 C 460 840, 380 760, 380 620 Z" fill="{PAPER}" stroke="{INK}" stroke-width="8"/>'
        f'<path d="M440 640 Q 470 610 500 640 M580 640 Q 610 610 640 640" fill="none" stroke="{INK}" stroke-width="7"/><path d="M480 740 Q 540 790 600 740" fill="none" stroke="{INK}" stroke-width="7"/>'
        f'<path d="M380 620 L 300 600 M700 620 L 780 600" stroke="{INK}" stroke-width="5"/>')
S.append(f'''<g class="rough">
<g class="pop" data-at="{e('e1', .2)}" data-c="540,400" data-sfx="pop"><rect x="390" y="330" width="300" height="120" rx="16" fill="{ACC}" stroke="{INK}" stroke-width="7" transform="rotate(-4 540 390)"/><text x="540" y="420" text-anchor="middle" class="t" style="font-size:80px;font-weight:900;fill:#fff" transform="rotate(-4 540 390)">反转</text></g>
<g class="fade" data-at="{e('e2')}" data-out="{e('e4') - 0.3}">
  {head(380, 700, 70, 2, 'open', 0.4)}
  <rect x="250" y="840" width="580" height="60" rx="8" fill="{PAPER}" stroke="{INK}" stroke-width="7"/><path d="M500 840 L 470 760 M470 760 L 440 740" stroke="{INK}" stroke-width="6"/><circle cx="440" cy="740" r="14" fill="{INK}"/>
  <g class="slide" data-at="{e('e2', .4)}" data-from="40,0">{bubble(520, 520, 420, 150, 470, 700, 'none', sw=6)}<text x="730" y="580" text-anchor="middle" class="t" style="font-size:32px;font-weight:900">“是几个软件工程师</text><text x="730" y="630" text-anchor="middle" class="t" style="font-size:32px;font-weight:900">装的”</text></g>
  <g class="slide" data-at="{e('e3', .3)}" data-from="0,30" data-sfx="pop"><rect x="200" y="960" width="680" height="200" rx="18" fill="{PAPER}" stroke="{ACC}" stroke-width="8"/>
    <text x="540" y="1040" text-anchor="middle" class="t" style="font-size:40px;font-weight:900">后来：公司在美国认罪</text>
    <text x="540" y="1120" text-anchor="middle" class="t" style="font-size:64px;font-weight:900;fill:{ACC}">罚款 43 亿美元</text></g>
  <text class="foot" x="540" y="1220" text-anchor="middle">2015 年国会听证 · 2017 年认罪协议 · 已隐去公司名称</text>
</g>
<g class="scale" data-at="{e('e4', .05)}" data-c="540,680" data-sx0="0.8" data-sy0="0.8">{mask}<text x="540" y="1000" text-anchor="middle" class="t" style="font-size:60px;font-weight:900;fill:{ACC}">“我只是不小心”</text></g>
</g>
{subs(4)}''')

# ---------- 5 · how to use ----------
f_ = lambda i, f=0: rel(i, 5, f)
S.append(f'''<g class="rough">
<text class="t slide" data-at="0.1" data-from="0,20" x="540" y="400" text-anchor="middle" style="font-size:60px;font-weight:900">两步用剃刀</text>
<g class="slide" data-at="{f_('f1', .1)}" data-from="0,30" data-sfx="pop"><rect x="160" y="500" width="760" height="170" rx="24" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>
  <circle cx="240" cy="585" r="44" fill="{ACC}" stroke="{INK}" stroke-width="5"/><text x="240" y="603" text-anchor="middle" class="t" style="font-size:48px;font-weight:900;fill:#fff">1</text>
  <text x="320" y="575" class="t" style="font-size:42px;font-weight:900">先假设是疏忽</text><text x="320" y="630" class="t" style="font-size:32px;fill:{GREY}">去问一句</text></g>
<path class="draw" data-at="{f_('f2', .05)}" d="M540 690 L 540 760" stroke="{INK}" stroke-width="7"/>
<g class="slide" data-at="{f_('f2', .15)}" data-from="0,30" data-sfx="pop"><rect x="160" y="780" width="760" height="230" rx="24" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>
  <circle cx="240" cy="895" r="44" fill="{ACC}" stroke="{INK}" stroke-width="5"/><text x="240" y="913" text-anchor="middle" class="t" style="font-size:48px;font-weight:900;fill:#fff">2</text>
  <text x="320" y="860" class="t" style="font-size:38px;font-weight:900">反复出现？</text><text x="320" y="915" class="t" style="font-size:38px;font-weight:900">总对同一方有利？</text>
  <text x="320" y="975" class="t" style="font-size:32px;font-weight:700;fill:{ACC}">→ 再考虑恶意</text></g>
</g>
{subs(5)}''')

# ---------- 6 · ending ----------
g = lambda i, f=0: rel(i, 6, f)
S.append(f'''<g class="rough">
<g class="slide" data-at="0.2" data-from="-60,0">{razor(470, 820, 1.2, -25)}</g>
<g class="slide" data-at="{g('g1', .45)}" data-from="60,0" data-sfx="pop">{ruler(600, 1000, 1.3, 15)}</g>
{star(850, 700, 1.1)}{star(200, 1080, .8)}
<g class="fade" data-at="{g('g1', .05)}"><text x="540" y="560" text-anchor="middle" class="t" style="font-size:50px;font-weight:900">对人，先用剃刀</text></g>
<g class="fade" data-at="{g('g1', .55)}"><text x="540" y="1220" text-anchor="middle" class="t" style="font-size:50px;font-weight:900">对事，留一把<tspan fill="{ACC}">尺</tspan></text></g>
<g class="fade" data-at="{g('g2', 1.0) + 0.4}"><text class="t" x="540" y="380" text-anchor="middle" style="font-size:56px;font-weight:900">汉隆<tspan fill="{ACC}">剃刀</tspan></text><text class="t" x="540" y="430" text-anchor="middle" style="font-size:24px;fill:{GREY};letter-spacing:3px">HANLON'S RAZOR</text></g>
</g>
{subs(6)}''')

assert len(S) == len(SC)
body = '\n'.join(f'    <g class="scene" data-s="{s:.2f}" data-e="{e_:.2f}">{b_}\n    </g>' for (s, e_), b_ in zip(SC, S))
html = open('head.part').read().replace('<!--SCENES-->', body).replace('__T__', str(T)) + open('tail.part').read().replace('__T__', str(T))
html = (html.replace('<title>沉默的螺旋</title>', '<title>汉隆剃刀</title>').replace('沉默的螺旋</text>', '汉隆剃刀</text>', 1)
        .replace('THE SPIRAL OF SILENCE', "HANLON'S RAZOR").replace('手绘动画：沉默的螺旋', '手绘动画：汉隆剃刀'))
open('hr.html', 'w').write(html)
print('T', T, [(round(x, 1), round(y, 1)) for x, y in SC])
