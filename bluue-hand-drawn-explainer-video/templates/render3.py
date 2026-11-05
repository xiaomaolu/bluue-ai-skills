import asyncio, subprocess, sys, time
from playwright.async_api import async_playwright
FPS=30; A=int(sys.argv[1]); B=int(sys.argv[2]); OUT=sys.argv[3]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1080,"height":1920},device_scale_factor=1)
        await pg.goto("http://localhost:8765/hr/render.html#render")
        await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(1000)
        ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
            "-c:v","libx264","-pix_fmt","yuv420p","-crf","17","-preset","medium","-r",str(FPS),OUT],stdin=subprocess.PIPE)
        t0=time.time()
        for i in range(A,B):
            await pg.evaluate(f"window.__seek({i/FPS})")
            ff.stdin.write(await pg.screenshot(type="jpeg",quality=93))
            if (i-A)%300==0: print(i,B,round(time.time()-t0,1),flush=True)
        ff.stdin.close(); ff.wait(); await b.close(); print("done",flush=True)
asyncio.run(main())
