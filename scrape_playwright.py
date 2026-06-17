"""
Uses Playwright to fully render each CLAD doc page and extract:
- Every img src, alt text
- The text of the nearest heading and paragraph before/after the image
- For GIFs, note that they are animated
"""
import asyncio
import json
from playwright.async_api import async_playwright

PAGES = [
    ('overview',           'https://developers.specs.com/docs/clad'),
    ('how-clad-works',     'https://developers.specs.com/docs/clad/overview-section/how-clad-works'),
    ('agents-and-skills',  'https://developers.specs.com/docs/clad/overview-section/agents-and-skills'),
    ('setup-lens-studio',  'https://developers.specs.com/docs/clad/setup/setup-lens-studio'),
    ('claude-code-setup',  'https://developers.specs.com/docs/clad/setup/setup-ai/claude-code-setup'),
    ('codex-setup',        'https://developers.specs.com/docs/clad/setup/setup-ai/codex-setup'),
    ('cursor-setup',       'https://developers.specs.com/docs/clad/setup/setup-ai/cursor-setup'),
    ('javascript-debugger','https://developers.specs.com/docs/clad/tools/javascript-debugger'),
    ('test-leaf',          'https://developers.specs.com/docs/clad/tools/test-your-lens-with-leaf'),
    ('troubleshoot-mcp',   'https://developers.specs.com/docs/clad/troubleshooting/troubleshoot-lens-studio-mcp'),
    ('troubleshoot-plugin','https://developers.specs.com/docs/clad/troubleshooting/troubleshoot-lens-studio-plugin'),
    ('setup-specs-project','https://developers.specs.com/docs/clad/additional-guides/setup-specs-project'),
    ('refresh-logger',     'https://developers.specs.com/docs/clad/additional-guides/refresh-logger'),
    ('open-project-cli',   'https://developers.specs.com/docs/clad/additional-guides/open-project-in-cli'),
]

JS_EXTRACT = """
() => {
    const results = [];
    const imgs = document.querySelectorAll('img');
    imgs.forEach(img => {
        const src = img.src || img.getAttribute('src') || '';
        const alt = img.alt || '';
        
        // Walk up to find enclosing figure or div
        let container = img.parentElement;
        for (let i = 0; i < 5; i++) {
            if (!container) break;
            if (['FIGURE','SECTION','ARTICLE','DIV'].includes(container.tagName)) break;
            container = container.parentElement;
        }
        
        // Get text before and after img in the document
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        const allText = [];
        let node;
        while (node = walker.nextNode()) {
            allText.push({text: node.textContent.trim(), node});
        }
        
        // Find nearest heading before the image
        let prevHeading = '';
        let prevPara = '';
        let el = img;
        let limit = 20;
        while (el && limit-- > 0) {
            el = el.previousElementSibling || el.parentElement?.previousElementSibling;
            if (!el) break;
            if (/^H[1-6]$/.test(el.tagName) && !prevHeading) {
                prevHeading = el.textContent.trim();
            }
            if (['P','LI'].includes(el.tagName) && !prevPara) {
                prevPara = el.textContent.trim().substring(0, 200);
            }
            if (prevHeading && prevPara) break;
        }
        
        // Get caption / figcaption
        let caption = '';
        let figParent = img.closest('figure');
        if (figParent) {
            const cap = figParent.querySelector('figcaption');
            if (cap) caption = cap.textContent.trim();
        }
        
        // Check if it's a GIF
        const isGif = src.toLowerCase().includes('.gif');
        
        results.push({
            src: src,
            alt: alt,
            caption: caption,
            prevHeading: prevHeading,
            prevPara: prevPara,
            isGif: isGif,
            naturalWidth: img.naturalWidth,
            naturalHeight: img.naturalHeight
        });
    });
    return results;
}
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        all_results = {}
        
        for name, url in PAGES:
            print(f"Fetching {name}...", flush=True)
            try:
                await page.goto(url, wait_until='networkidle', timeout=30000)
                # Scroll to trigger lazy loading
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.sleep(2)
                await page.evaluate("window.scrollTo(0, 0)")
                await asyncio.sleep(1)
                
                images = await page.evaluate(JS_EXTRACT)
                # Filter to only CLAD doc images
                images = [i for i in images if 'docs-static' in i['src'] or 'clad' in i['src'].lower()]
                all_results[name] = images
                print(f"  Found {len(images)} images", flush=True)
            except Exception as e:
                print(f"  ERROR: {e}", flush=True)
                all_results[name] = []
        
        await browser.close()
        
        # Write results
        with open(r'D:\SNAPCHAT\Snapchat-CLAD\image_data.json', 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
        
        print("\n=== RESULTS ===")
        for name, images in all_results.items():
            print(f"\n--- {name} ---")
            for img in images:
                print(f"  src: {img['src']}")
                print(f"  alt: {img['alt']}")
                print(f"  caption: {img['caption']}")
                print(f"  heading: {img['prevHeading']}")
                print(f"  para: {img['prevPara'][:150]}")
                print(f"  gif: {img['isGif']}")
                print()

asyncio.run(main())
