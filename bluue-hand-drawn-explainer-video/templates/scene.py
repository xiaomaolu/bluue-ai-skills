W,H=1080,1920
INK='#141414'; ACC='#6c47ff'; PAPER='#fbfaf7'
def star(x,y,s=1):
    return f'<path d="M{x} {y-18*s} Q{x+3*s} {y-3*s} {x+18*s} {y} Q{x+3*s} {y+3*s} {x} {y+18*s} Q{x-3*s} {y+3*s} {x-18*s} {y} Q{x-3*s} {y-3*s} {x} {y-18*s} Z" fill="{INK}"/>'
o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'''<defs><filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="3.2"/></filter></defs>''',
f'<rect width="{W}" height="{H}" fill="{PAPER}"/>',
# header
f'<text x="90" y="170" font-family="Noto Sans CJK SC" font-weight="900" font-size="40" fill="{INK}">沉默的螺旋</text>',
f'<text x="90" y="212" font-family="Noto Sans CJK SC" font-weight="500" font-size="22" fill="#8a8a86" letter-spacing="4">THE SPIRAL OF SILENCE</text>',
f'<text x="990" y="170" text-anchor="end" font-family="Noto Sans CJK SC" font-size="24" fill="#8a8a86">蓝与蓝之间的ai差值</text>',
'<g filter="url(#rough)" stroke-linecap="round" stroke-linejoin="round">',
# window
f'<rect x="150" y="420" width="780" height="470" rx="60" fill="none" stroke="{INK}" stroke-width="8"/>',
f'<rect x="178" y="448" width="724" height="414" rx="40" fill="none" stroke="{INK}" stroke-width="3.5"/>',
# landscape outside
f'<path d="M180 760 C 300 700, 380 720, 470 690 S 660 640, 760 700 S 880 720, 900 705" fill="none" stroke="{INK}" stroke-width="4"/>',
f'<path d="M180 800 C 320 790, 520 812, 900 790" fill="none" stroke="{INK}" stroke-width="3"/>',
f'<path d="M430 700 L430 560 M400 578 L460 578 M405 604 L455 604" fill="none" stroke="{INK}" stroke-width="4"/>',
f'<path d="M240 742 l18 -50 l18 50 Z M272 736 l14 -38 l14 38 Z M500 700 l16 -44 l16 44 Z" fill="{INK}"/>',
f'<path d="M180 590 C 260 600, 360 584, 430 578 M180 616 C 260 624, 360 610, 430 604" fill="none" stroke="{INK}" stroke-width="2"/>',
f'<path d="M220 520 l40 0 M240 545 l60 0 M700 500 l50 0" stroke="#bdbdb8" stroke-width="4"/>',
]
# ---- Person A (woman, bob, left), looking right, nervous
A=[
f'<path d="M210 1300 C 215 1220, 240 1150, 300 1128 L 330 1124 L 362 1128 C 420 1150, 445 1220, 450 1300" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>',
f'<path d="M292 1072 L 292 1126 M 352 1072 L 354 1126" stroke="{INK}" stroke-width="6.5"/>',
f'<path d="M285 1126 C 300 1150, 345 1152, 362 1126" fill="none" stroke="{INK}" stroke-width="6"/>',
f'<path d="M262 1200 L 268 1300 M398 1200 L 392 1300" stroke="{INK}" stroke-width="4"/>',
f'<path d="M252 930 C 248 1000, 262 1060, 322 1086 C 382 1060, 396 1000, 392 930" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>',
f'<path d="M248 975 C 232 970, 230 1000, 252 1010 M396 975 C 412 970, 414 1000, 392 1010" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>',
f'<path d="M230 1000 C 205 880, 250 806, 330 806 C 405 808, 440 880, 418 995 C 414 1022, 406 1040, 398 1050 L 382 1042 C 392 1000, 394 960, 384 920 C 372 940, 352 948, 340 944 L 346 918 C 330 936, 300 944, 282 940 L 292 916 C 278 928, 266 934, 258 930 C 252 965, 252 1005, 258 1044 L 242 1050 C 236 1036, 232 1018, 230 1000 Z" fill="{INK}"/>',
f'<rect x="352" y="868" width="40" height="13" rx="6" transform="rotate(-18 372 874)" fill="{ACC}" stroke="{INK}" stroke-width="3"/>',
f'<path d="M270 850 C 290 832, 320 826, 345 830 M300 868 C 312 860, 330 858, 345 862" fill="none" stroke="{PAPER}" stroke-width="5"/>',
f'<path d="M272 960 Q 290 950 308 958 M 336 958 Q 354 950 372 960" fill="none" stroke="{INK}" stroke-width="6"/>',
f'<ellipse cx="298" cy="978" rx="9" ry="12" fill="{INK}"/><ellipse cx="362" cy="978" rx="9" ry="12" fill="{INK}"/>',
f'<circle cx="301" cy="973" r="3.2" fill="{PAPER}"/><circle cx="365" cy="973" r="3.2" fill="{PAPER}"/>',
f'<path d="M276 940 Q 290 934 304 938 M 344 936 Q 358 932 372 938" fill="none" stroke="{INK}" stroke-width="4.5"/>',
f'<path d="M324 1000 L 320 1018 L 328 1020" fill="none" stroke="{INK}" stroke-width="4"/>',
f'<path d="M306 1046 C 314 1042, 322 1048, 330 1044 C 336 1041, 342 1046, 346 1044" fill="none" stroke="{INK}" stroke-width="4.5"/>',
f'<path d="M268 1014 l8 -10 M280 1016 l8 -10 M358 1014 l8 -10 M370 1016 l8 -10" stroke="{INK}" stroke-width="3"/>',
f'<path d="M408 905 C 412 920, 410 935, 404 942" fill="none" stroke="#6db7ff" stroke-width="0"/>',
f'<path d="M418 900 C 426 920, 426 936, 416 942 C 406 936, 408 920, 418 900 Z" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>',
]
# ---- Person B (man, short messy hair, right), talking, confident
B=[
f'<path d="M620 1300 C 625 1215, 655 1150, 720 1128 L 760 1124 L 795 1128 C 860 1150, 890 1215, 895 1300" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>',
f'<path d="M728 1128 L 760 1190 L 792 1128" fill="none" stroke="{INK}" stroke-width="6"/>',
f'<path d="M760 1190 L 760 1300" stroke="{INK}" stroke-width="4"/>',
f'<path d="M732 1070 L 730 1128 M 790 1070 L 792 1128" stroke="{INK}" stroke-width="6.5"/>',
f'<path d="M690 925 C 686 1000, 700 1058, 760 1086 C 820 1058, 836 1000, 832 925" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>',
f'<path d="M688 970 C 670 966, 668 998, 692 1006 M834 970 C 852 966, 854 998, 830 1006" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>',
f'<path d="M676 960 C 664 880, 690 830, 720 822 L 712 800 L 745 812 L 750 786 L 775 808 L 800 790 L 805 815 L 838 812 C 862 850, 858 910, 842 962 L 830 960 C 828 930, 822 905, 806 888 L 790 905 L 776 885 L 752 906 L 740 884 L 718 905 L 704 890 C 694 910, 692 935, 690 962 Z" fill="{INK}"/>',
f'<path d="M730 840 C 748 830, 770 830, 790 838" fill="none" stroke="{PAPER}" stroke-width="5"/>',
f'<path d="M708 942 L 742 936 M 778 936 L 812 942" stroke="{INK}" stroke-width="8"/>',
f'<path d="M712 972 Q 726 964 744 970 M 776 970 Q 794 964 808 972" fill="none" stroke="{INK}" stroke-width="6"/>',
f'<ellipse cx="722" cy="980" rx="8" ry="9" fill="{INK}"/><ellipse cx="786" cy="980" rx="8" ry="9" fill="{INK}"/>',
f'<path d="M760 1000 L 756 1020 L 764 1022" fill="none" stroke="{INK}" stroke-width="4"/>',
f'<path d="M738 1040 C 750 1038, 772 1038, 784 1040 C 778 1062, 746 1062, 738 1040 Z" fill="{INK}"/>',
f'<path d="M748 1052 C 756 1046, 768 1046, 774 1052" fill="none" stroke="{ACC}" stroke-width="4"/>',
]
o+=A+B
# table + cups
o+=[f'<path d="M110 1300 L 970 1300" stroke="{INK}" stroke-width="9"/>',
f'<path d="M150 1300 L 150 1340 M 930 1300 L 930 1340" stroke="{INK}" stroke-width="7"/>',
f'<path d="M470 1240 L 476 1298 L 516 1298 L 522 1240 Z" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>',
f'<path d="M478 1258 L 514 1258" stroke="{INK}" stroke-width="3"/>',
f'<path d="M490 1222 C 484 1208, 498 1200, 492 1186 M506 1222 C 500 1208, 514 1200, 508 1186" fill="none" stroke="#9a9a96" stroke-width="3"/>']
# speech bubbles
o+=[f'<path d="M560 470 C 560 440, 590 430, 620 430 L 880 430 C 910 430, 930 448, 930 476 L 930 610 C 930 640, 910 655, 880 655 L 790 655 L 772 720 L 738 655 L 610 655 C 580 655, 560 640, 560 610 Z" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>',
f'<path d="M600 490 L 860 490 M600 540 L 890 540 M600 590 L 800 590" stroke="{ACC}" stroke-width="10"/>',
f'<path d="M250 700 C 250 684, 262 676, 278 676 L 360 676 C 376 676, 388 684, 388 700 L 388 738 C 388 754, 376 762, 360 762 L 330 762 L 318 798 L 304 762 L 278 762 C 262 762, 250 754, 250 738 Z" fill="{PAPER}" stroke="{INK}" stroke-width="6"/>',
f'<circle cx="294" cy="720" r="6" fill="{INK}"/><circle cx="319" cy="720" r="6" fill="{INK}"/><circle cx="344" cy="720" r="6" fill="{INK}"/>',
star(470,980,1.0), star(905,1010,0.75), star(560,880,0.6),
'</g>']
# caption
o+=[f'<text x="540" y="1470" text-anchor="middle" font-family="Noto Sans CJK SC" font-weight="700" font-size="50" fill="{INK}">和陌生人同坐五个小时火车，</text>',
f'<text x="540" y="1540" text-anchor="middle" font-family="Noto Sans CJK SC" font-weight="700" font-size="50" fill="{INK}">他的看法和你<tspan fill="{ACC}">相反</tspan>——你还会开口吗？</text>',
'</svg>']
open('scene_test.svg','w').write(''.join(o))
