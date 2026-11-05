import re, json, numpy as np, soundfile as sf, subprocess
SR=48000; tl=json.load(open('timeline.json')); T=tl['T']; TS=tl['TS']; D=json.load(open('durs.json'))
src=open('hr.html').read(); rng=np.random.default_rng(5); N=int((T+1)*SR)
v=np.zeros(N)
for k,t in TS.items():
    a,sr=sf.read(D[k]['wav']); a=np.interp(np.arange(0,len(a),sr/SR),np.arange(len(a)),a); i=int(t*SR); v[i:i+len(a)]+=a[:N-i]
def env(n,a,d): t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/d)
def ks(f,dur,amp=1):
    n=int(dur*SR); p=int(SR/f); b=rng.uniform(-1,1,p); out=np.zeros(n); idx=0
    for i in range(n):
        out[i]=b[idx]; nx=(idx+1)%p; b[idx]=0.994*0.5*(b[idx]+b[nx]); idx=nx
    return amp*out*env(n,0.002,0.9)
nt=lambda m:440*2**((m-69)/12)
mus=np.zeros(N)
def add(t,s,a=1.0):
    i=int(t*SR); j=min(N,i+len(s))
    if 0<=i<N: mus[i:j]+=a*s[:j-i]
BPM=88; beat=60/BPM
prog=[[48,55,60,64,67],[45,52,57,60,64],[41,48,57,60,65],[43,50,55,59,62]]  # C Am F G
cache={}
def pl(m):
    if m not in cache: cache[m]=ks(nt(m),1.6)
    return cache[m]
patt=[0,2,3,4,3,2,1,3]
bar=0; t=0.0
kick=np.sin(2*np.pi*np.cumsum(50+70*np.exp(-np.arange(int(0.3*SR))/SR/0.03))/SR)*env(int(0.3*SR),0.001,0.1)
shk=rng.standard_normal(int(0.06*SR)); shk=(shk-np.convolve(shk,np.ones(6)/6,'same'))*env(len(shk),0.004,0.015)
while t<T:
    ch=prog[bar%4]
    add(t,ks(nt(ch[0]-12),3.0),0.35)
    for k in range(8):
        tt=t+k*beat/2
        add(tt,pl(ch[patt[k]]+12),0.16 if k%2==0 else 0.1)
    for k in range(4):
        tb=t+k*beat
        if t>=6.0: add(tb,kick,0.25 if k%2==0 else 0.12)
        add(tb+beat/2,shk,0.12)
    t+=4*beat; bar+=1
sfx=np.zeros(N)
def put(t,s):
    i=int(t*SR); j=min(N,i+len(s))
    if 0<=i<N: sfx[i:j]+=s[:j-i]
n=int(0.18*SR); tt=np.arange(n)/SR
POP=0.12*np.sin(2*np.pi*(400+900*tt/0.18)*tt)*env(n,0.002,0.05)
TICK=rng.standard_normal(int(0.03*SR)); TICK=0.05*(TICK-np.convolve(TICK,np.ones(4)/4,'same'))*env(len(TICK),0.001,0.006)
pg=rng.standard_normal(int(0.4*SR)); pg=np.convolve(pg,np.ones(10)/10,'same')*np.sin(np.pi*np.arange(len(pg))/len(pg))**2*0.1
blocks=re.findall(r'<g class="scene" data-s="([\d.]+)" data-e="([\d.]+)">(.*?)\n    </g>',src,re.S)
for s0,e0,b in blocks:
    s0=float(s0)
    if s0>0: put(s0-0.05,pg)
    for m in re.finditer(r'data-at="([\d.]+)"[^>]*?data-sfx="pop"',b): put(s0+float(m.group(1)),POP)
    for m in re.finditer(r'data-anim="typedel" data-a="([\d.]+)" data-full="([^"]+)"',b):
        a=s0+float(m.group(1)); n=len(m.group(2))
        for k in range(n): put(a+1.1*(k+0.5)/n,TICK)
        for k in range(n): put(a+1.7+0.11*k,TICK*0.8)
envl=np.convolve(np.abs(v),np.ones(int(0.3*SR))/int(0.3*SR),'same'); duck=1-0.5*np.clip(envl/0.03,0,1)
end=int(T*SR); fade=np.ones(N); fo=int(3*SR); fade[end-fo:end]=np.linspace(1,0,fo); fade[end:]=0
mix=mus*0.55*duck*fade+sfx+v*0.95
sf.write('mixraw.wav',np.stack([mix,mix],1),SR)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','mixraw.wav','-af','alimiter=limit=0.95,loudnorm=I=-15:TP=-1.5:LRA=11','-ar','48000','-t',str(T),'mix.wav'],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','mix.wav','-b:a','128k','mix.mp3'],check=True)
r=lambda a:20*np.log10(np.sqrt(np.mean(a**2))+1e-9); print('mus',round(r(mus[:end]*0.55),1),'narr',round(r(v[:end]),1),'sfx',round(r(sfx[:end]),1))
