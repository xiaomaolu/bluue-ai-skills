import asyncio, sys
from playwright.async_api import async_playwright
ts=[float(x) for x in sys.argv[1:]]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        msgs=[]; pg.on("console",lambda m:msgs.append(m.text)); pg.on("pageerror",lambda e:msgs.append(str(e)))
        await pg.goto("http://localhost:8765/hr/render.html#render"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(800)
        for t in ts:
            await pg.evaluate(f"window.__seek({t})"); await pg.screenshot(path=f"snap_{t:06.1f}.jpg",type="jpeg",quality=80)
        print(msgs); await b.close()
asyncio.run(main())
