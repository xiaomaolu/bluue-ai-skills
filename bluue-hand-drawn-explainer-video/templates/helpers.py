import re, math, json
import scene as SCN
from lines import L
INK, ACC, PAPER, GREY = SCN.INK, SCN.ACC, SCN.PAPER, '#9a9a96'
def hl(s): return re.sub(r'【(.*?)】', r'<tspan class="o">\1</tspan>', s)
def wrap(s, n=18):
    plain = re.sub(r'[【】]', '', s)
    if len(plain) <= n: return [s]
    best = None
    for m in re.finditer(r'[，：；、—]', plain):
        k = m.end(); sc_ = abs(k - len(plain) / 2)
        if k <= n + 2 and len(plain) - k <= n + 2 and (best is None or sc_ < best[0]): best = (sc_, k)
    if not best:
        cands = [m.end() for m in re.finditer(r'[，：；、—]', plain) if 4 < m.end() < len(plain) - 3]
        k = min(cands, key=lambda q: abs(q - len(plain) / 2)) if cands else math.ceil(len(plain) / 2)
    else: k = best[1]
    j = c = 0
    while c < k:
        if s[j] in '【】': j += 1; continue
        j += 1; c += 1
    while j < len(s) and s[j] in '—': j += 1
    a, b = s[:j], s[j:]
    if a.count('【') > a.count('】'): a += '】'; b = '【' + b
    return [a, b]
def subs(sc):
    ids = [i for i, _ in by_scene[sc]]; out = []
    for k, id_ in enumerate(ids):
        disp = [x[2] for x in L if x[0] == id_][0]
        at = rel(id_, sc); o = f' data-out="{rel(ids[k+1], sc) - 0.2}"' if k + 1 < len(ids) else ''
        ls = wrap(disp); y0 = 1480 if len(ls) == 1 else 1450
        fs = min(50, int(930 / max(len(re.sub(r'[【】]', '', l)) for l in ls)))
        out += [f'<text class="sub fade" data-at="{at}"{o} data-d="0.2" x="540" y="{y0 + i * 68}" style="font-size:{fs}px">{hl(l)}</text>' for i, l in enumerate(ls)]
    return ''.join(out)

# ---------- drawing helpers ----------
def star(x, y, s=1): return SCN.star(x, y, s)
def bubble(x, y, w, h, tx, ty, kind='talk', lines=3, sw=6):
    """rounded bubble with a tail pointing to (tx,ty)."""
    r = min(30, h / 2.5); bx = min(max(tx, x + r + 20), x + w - r - 40)
    tail = f'L {bx + 34} {y + h} L {tx} {ty} L {bx} {y + h}' if ty > y else f'L {bx} {y} L {tx} {ty} L {bx + 34} {y}'
    if ty > y:
        d = f'M{x + r} {y} L {x + w - r} {y} Q {x + w} {y} {x + w} {y + r} L {x + w} {y + h - r} Q {x + w} {y + h} {x + w - r} {y + h} {tail} L {x + r} {y + h} Q {x} {y + h} {x} {y + h - r} L {x} {y + r} Q {x} {y} {x + r} {y} Z'
    else:
        d = f'M{x + r} {y} {tail} L {x + w - r} {y} Q {x + w} {y} {x + w} {y + r} L {x + w} {y + h - r} Q {x + w} {y + h} {x + w - r} {y + h} L {x + r} {y + h} Q {x} {y + h} {x} {y + h - r} L {x} {y + r} Q {x} {y} {x + r} {y} Z'
    g = f'<path d="{d}" fill="{PAPER}" stroke="{INK}" stroke-width="{sw}"/>'
    if kind == 'talk':
        pad = 22; lh = (h - 2 * pad) / lines
        for i in range(lines):
            ww = (w - 2 * pad) * (1 if i < lines - 1 else 0.6)
            yy = y + pad + lh * (i + 0.5)
            g += f'<path d="M{x + pad} {yy:.0f} L {x + pad + ww:.0f} {yy:.0f}" stroke="{ACC}" stroke-width="{max(5, lh * 0.32):.0f}"/>'
    elif kind == 'dots':
        for i in range(3): g += f'<circle cx="{x + w / 2 + (i - 1) * w * 0.2:.0f}" cy="{y + h / 2:.0f}" r="{max(3, h * 0.07):.1f}" fill="{INK}"/>'
    elif kind == 'grey':
        pad = 20
        for i in range(2):
            yy = y + h * (0.36 + i * 0.3)
            g += f'<path d="M{x + pad} {yy:.0f} L {x + w - pad - i * w * 0.3:.0f} {yy:.0f}" stroke="{GREY}" stroke-width="7"/>'
    return g

HAIRS = [
 lambda x, y, r: f'M{x - r * 1.02} {y + r * 0.1} C {x - r * 1.1} {y - r * 1.2}, {x + r * 1.1} {y - r * 1.2}, {x + r * 1.02} {y + r * 0.1} C {x + r * 0.7} {y - r * 0.35}, {x - r * 0.4} {y - r * 0.25}, {x - r * 1.02} {y + r * 0.1} Z',
 lambda x, y, r: f'M{x - r * 1.05} {y + r * 0.6} C {x - r * 1.25} {y - r * 1.2}, {x + r * 1.25} {y - r * 1.2}, {x + r * 1.05} {y + r * 0.6} L {x + r * 0.82} {y + r * 0.6} C {x + r * 0.85} {y}, {x + r * 0.5} {y - r * 0.45}, {x} {y - r * 0.42} C {x - r * 0.5} {y - r * 0.45}, {x - r * 0.85} {y}, {x - r * 0.82} {y + r * 0.6} Z',
 lambda x, y, r: f'M{x - r} {y - r * 0.1} L {x - r * 0.75} {y - r * 1.1} L {x - r * 0.35} {y - r * 0.85} L {x} {y - r * 1.2} L {x + r * 0.35} {y - r * 0.85} L {x + r * 0.78} {y - r * 1.08} L {x + r} {y - r * 0.1} C {x + r * 0.5} {y - r * 0.5}, {x - r * 0.5} {y - r * 0.5}, {x - r} {y - r * 0.1} Z',
 lambda x, y, r: f'M{x - r * 1.0} {y} C {x - r * 1.05} {y - r * 1.15}, {x + r * 1.05} {y - r * 1.15}, {x + r * 1.0} {y} C {x + r * 0.3} {y - r * 0.55}, {x - r * 0.2} {y - r * 0.2}, {x - r * 1.0} {y} Z',
]
def head(x, y, r=46, v=0, mouth='closed', look=0, extra=''):
    g = f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PAPER}" stroke="{INK}" stroke-width="{max(4, r * 0.12):.1f}"/>'
    g += f'<path d="{HAIRS[v % 4](x, y, r)}" fill="{INK}"/>'
    ex = r * 0.36; ey = y + r * 0.12; lk = look * r * 0.1
    g += f'<ellipse cx="{x - ex + lk:.1f}" cy="{ey:.1f}" rx="{r * 0.09:.1f}" ry="{r * 0.13:.1f}" fill="{INK}"/><ellipse cx="{x + ex + lk:.1f}" cy="{ey:.1f}" rx="{r * 0.09:.1f}" ry="{r * 0.13:.1f}" fill="{INK}"/>'
    my = y + r * 0.55
    if mouth == 'open':
        g += f'<path d="M{x - r * 0.2 + lk:.1f} {my:.1f} Q {x + lk:.1f} {my + r * 0.32:.1f} {x + r * 0.2 + lk:.1f} {my:.1f} Z" fill="{INK}"/>'
    elif mouth == 'flat':
        g += f'<path d="M{x - r * 0.14 + lk:.1f} {my:.1f} L {x + r * 0.14 + lk:.1f} {my:.1f}" stroke="{INK}" stroke-width="{max(3, r * 0.08):.1f}"/>'
    else:
        g += f'<path d="M{x - r * 0.16 + lk:.1f} {my:.1f} Q {x + lk:.1f} {my + r * 0.1:.1f} {x + r * 0.16 + lk:.1f} {my:.1f}" fill="none" stroke="{INK}" stroke-width="{max(3, r * 0.08):.1f}"/>'
    # shoulders
    g += f'<path d="M{x - r * 1.25} {y + r * 2.3} C {x - r * 1.2} {y + r * 1.5}, {x - r * 0.6} {y + r * 1.2}, {x} {y + r * 1.2} C {x + r * 0.6} {y + r * 1.2}, {x + r * 1.2} {y + r * 1.5}, {x + r * 1.25} {y + r * 2.3}" fill="{PAPER}" stroke="{INK}" stroke-width="{max(4, r * 0.12):.1f}"/>'
    return g + extra

# Character A / B from the approved sample
A_ALL = SCN.A; B_ALL = SCN.B
def A(shout=False, calm=False):
    parts = []
    for p in A_ALL:
        if (shout or calm) and ('M418 900' in p or 'M268 1014' in p): continue
        if shout and 'M306 1046' in p:
            p = f'<path d="M300 1036 Q 324 1030 348 1036 Q 340 1068 324 1068 Q 308 1068 300 1036 Z" fill="{INK}"/>'
        parts.append(p)
    return ''.join(parts)
def B(listen=False):
    parts = []
    for p in B_ALL:
        if listen and 'M738 1040' in p: p = f'<path d="M742 1044 Q 760 1050 780 1044" fill="none" stroke="{INK}" stroke-width="5"/>'
        if listen and 'M748 1052' in p: continue
        parts.append(p)
    return ''.join(parts)

WINDOW = ''.join(SCN.o[7:9]) if False else ''
def train(bubbles=''):
    win = (f'<rect x="150" y="420" width="780" height="470" rx="60" fill="{PAPER}" stroke="{INK}" stroke-width="8"/>'
           f'<rect x="178" y="448" width="724" height="414" rx="40" fill="none" stroke="{INK}" stroke-width="3.5"/>')
    land = (f'<g clip-path="url(#win)"><g data-anim="scroll">'
            + ''.join(f'<g transform="translate({k * 760} 0)">'
                      f'<path d="M140 760 C 300 700, 380 720, 470 690 S 660 640, 760 700 S 880 720, 920 705" fill="none" stroke="{INK}" stroke-width="4"/>'
                      f'<path d="M430 700 L430 560 M400 578 L460 578 M405 604 L455 604" fill="none" stroke="{INK}" stroke-width="4"/>'
                      f'<path d="M240 742 l18 -50 l18 50 Z M272 736 l14 -38 l14 38 Z M560 690 l16 -44 l16 44 Z" fill="{INK}"/>'
                      f'<path d="M-330 590 C -200 600, 300 584, 430 578 M-330 616 C -200 624, 300 610, 430 604" fill="none" stroke="{INK}" stroke-width="2"/>'
                      f'</g>' for k in range(-1, 3))
            + f'</g><path d="M140 800 C 320 790, 520 812, 940 790" fill="none" stroke="{INK}" stroke-width="3"/>'
            f'<path d="M220 520 l40 0 M240 545 l60 0 M700 500 l50 0" stroke="#bdbdb8" stroke-width="4"/></g>')
    table = ''.join(SCN.o[i] for i in range(len(SCN.o)) if False) + (
        f'<path d="M110 1300 L 970 1300" stroke="{INK}" stroke-width="9"/>'
        f'<path d="M150 1300 L 150 1340 M 930 1300 L 930 1340" stroke="{INK}" stroke-width="7"/>'
        f'<path d="M470 1240 L 476 1298 L 516 1298 L 522 1240 Z" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>'
        f'<path d="M478 1258 L 514 1258" stroke="{INK}" stroke-width="3"/>'
        f'<path d="M490 1222 C 484 1208, 498 1200, 492 1186 M506 1222 C 500 1208, 514 1200, 508 1186" fill="none" stroke="#9a9a96" stroke-width="3"/>')
    return win + land, table

