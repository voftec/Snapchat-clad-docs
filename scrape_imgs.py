import urllib.request
import re

pages = [
    ('overview', 'https://developers.specs.com/docs/clad'),
    ('how-clad-works', 'https://developers.specs.com/docs/clad/overview-section/how-clad-works'),
    ('setup-lens-studio', 'https://developers.specs.com/docs/clad/setup/setup-lens-studio'),
    ('claude-code-setup', 'https://developers.specs.com/docs/clad/setup/setup-ai/claude-code-setup'),
    ('codex-setup', 'https://developers.specs.com/docs/clad/setup/setup-ai/codex-setup'),
    ('cursor-setup', 'https://developers.specs.com/docs/clad/setup/setup-ai/cursor-setup'),
    ('javascript-debugger', 'https://developers.specs.com/docs/clad/tools/javascript-debugger'),
    ('test-leaf', 'https://developers.specs.com/docs/clad/tools/test-your-lens-with-leaf'),
    ('troubleshoot-mcp', 'https://developers.specs.com/docs/clad/troubleshooting/troubleshoot-lens-studio-mcp'),
    ('troubleshoot-plugin', 'https://developers.specs.com/docs/clad/troubleshooting/troubleshoot-lens-studio-plugin'),
    ('setup-specs-project', 'https://developers.specs.com/docs/clad/additional-guides/setup-specs-project'),
    ('refresh-logger', 'https://developers.specs.com/docs/clad/additional-guides/refresh-logger'),
    ('open-project-cli', 'https://developers.specs.com/docs/clad/additional-guides/open-project-in-cli'),
]

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

for name, url in pages:
    try:
        with opener.open(url) as r:
            html = r.read().decode('utf-8', errors='ignore')
        # Find all img tags with surrounding context
        imgs = re.findall(r'(?s).{0,300}<img[^>]+>.{0,300}', html)
        print(f'\n=== {name} ===')
        for img in imgs:
            src_m = re.search(r'src="([^"]+)"', img)
            alt_m = re.search(r'alt="([^"]*)"', img)
            src = src_m.group(1) if src_m else 'NO_SRC'
            alt = alt_m.group(1) if alt_m else 'NO_ALT'
            # Get clean text around the img tag
            clean = re.sub(r'<[^>]+>', ' ', img)
            clean = re.sub(r'\s+', ' ', clean).strip()
            print(f'  SRC: {src}')
            print(f'  ALT: {alt}')
            print(f'  CTX: {clean[:300]}')
            print()
    except Exception as e:
        print(f'FAIL {name}: {e}')
