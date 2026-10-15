"""Dựng trang web chính sách quyền riêng tư từ PRIVACY.md vào thư mục _site (chạy tự động khi push, hoặc chạy tay: python build.py)."""
import pathlib
import re

import markdown

root = pathlib.Path(__file__).parent
text = (root / "PRIVACY.md").read_text(encoding="utf-8")
body = markdown.markdown(text, extensions=["extra", "sane_lists", "toc"])
title = "Privacy Policy — Moodle Super Manager"

page = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Chính sách quyền riêng tư / Privacy policy of the Moodle Super Manager browser extension.">
<style>
  :root {{ --fg:#1d2125; --muted:#5f6b76; --bg:#ffffff; --accent:#0f6cbf; --line:#dee2e6; --code:#f1f3f5; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --fg:#e6e9ec; --muted:#9aa5b1; --bg:#14181c; --accent:#6db3f2; --line:#2c333a; --code:#1e252b; }} }}
  body {{ margin:0; background:var(--bg); color:var(--fg); font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }}
  main {{ max-width:820px; margin:0 auto; padding:32px 16px 64px; }}
  h1 {{ font-size:1.7rem; line-height:1.3; margin:1.6em 0 .4em; }}
  h1:first-of-type {{ margin-top:0; }}
  h2 {{ font-size:1.35rem; margin:1.8em 0 .5em; padding-bottom:.25em; border-bottom:1px solid var(--line); }}
  h3 {{ font-size:1.05rem; margin:1.4em 0 .4em; }}
  a {{ color:var(--accent); }}
  code {{ background:var(--code); padding:.1em .35em; border-radius:4px; font-size:.92em; }}
  hr {{ border:0; border-top:1px solid var(--line); margin:2em 0; }}
  li {{ margin:.3em 0; }}
  p, li {{ color:var(--fg); }}
</style>
</head>
<body>
<main>
{body}
</main>
</body>
</html>
"""

out = root / "_site"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
print("Đã dựng", out / "index.html", f"({len(page)} ký tự)", "| tiêu đề:", re.findall(r"<h1[^>]*>(.*?)</h1>", body)[:1])
