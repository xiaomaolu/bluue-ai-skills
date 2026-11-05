import re, os, json, hashlib, numpy as np, soundfile as sf, sherpa_onnx
from lines import L
d='../tts/kokoro-multi-lang-v1_1/'
cfg=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(kokoro=sherpa_onnx.OfflineTtsKokoroModelConfig(model=d+'model.onnx',voices=d+'voices.bin',tokens=d+'tokens.txt',
  data_dir=d+'espeak-ng-data',dict_dir=d+'dict',lexicon=d+'lexicon-us-en.txt,'+d+'lexicon-zh.txt'),num_threads=2),rule_fsts=f'{d}date-zh.fst,{d}phone-zh.fst,{d}number-zh.fst')
tts=None; os.makedirs('sent',exist_ok=True); out={}
for id_,sc,disp,sp,spd in L:
    text=sp or re.sub(r'[【】“”]','',disp)
    text=text.replace('：','，')
    h=hashlib.md5(f'{text}{spd}'.encode()).hexdigest()[:10]; fn=f'sent/{h}.wav'
    if not os.path.exists(fn):
        if tts is None: tts=sherpa_onnx.OfflineTts(cfg)
        g=tts.generate(text,sid=3,speed=spd); a=np.array(g.samples); idx=np.where(np.abs(a)>0.01)[0]
        a=a[max(0,idx[0]-240):idx[-1]+1200]; sf.write(fn,a,g.sample_rate)
    a,sr=sf.read(fn); out[id_]=dict(wav=fn,dur=len(a)/sr)
    print(id_,round(len(a)/sr,2),text,flush=True)
json.dump(out,open('durs.json','w'),ensure_ascii=False,indent=0)
