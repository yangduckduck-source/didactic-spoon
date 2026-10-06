"""app.html(아티팩트용 본문)을 GitHub Pages용 완전한 index.html로 감싼다.

app.html 은 claude.ai 아티팩트에 그대로 올리는 원본이라 <html>/<head> 없이
<title>·<link>·<style> 로 시작한다. 이 스크립트는 그 머리 부분을 <head> 로 옮기고
아티팩트가 깔아 주던 최소 초기화 CSS 를 붙여 독립 실행 페이지를 만든다.

    python3 scripts/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "app.html").read_text(encoding="utf-8")

marker = '<div class="app">'
head_part, body_part = src.split(marker, 1)

page = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<!-- 이 파일은 scripts/build.py 가 app.html 에서 만든다. 직접 고치지 말 것. -->
<style>:root{{color-scheme:light}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{head_part.strip()}
</head>
<body>
{marker}{body_part.rstrip()}
</body>
</html>
"""
(ROOT / "index.html").write_text(page, encoding="utf-8")
print("index.html written")
