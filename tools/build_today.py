# -*- coding: utf-8 -*-
import html, json, sys
from today_data import MOOD, GLOBAL, NETHERLANDS, AI_HPC, CRYPTO, MENTAL, SPORTS, CONSUMER

DATE_ISO = "2026-06-24"
DATE_HUMAN = "Wednesday, June 24, 2026"
MIN_ISO = "2026-03-19"

SECTIONS = [
    ("global", "Global News", "#1B998B"),
    ("netherlands", "Netherlands", "#E8703A"),
    ("ai-hpc", "AI & HPC", "#7B2D8E"),
    ("crypto-macro", "Crypto & Macro", "#E8B130"),
    ("mental-health", "AI & Mental Health", "#D63B47"),
    ("sports", "Sports", "#2478A0"),
    ("consumer-tech", "Consumer Tech", "#3D5A80"),
]
DATA = {
    "global": GLOBAL, "netherlands": NETHERLANDS, "ai-hpc": AI_HPC,
    "crypto-macro": CRYPTO, "mental-health": MENTAL, "sports": SPORTS, "consumer-tech": CONSUMER,
}


# Normalize: only the first hero per section stays a hero (one hero-card per section)
for _sid,_items in DATA.items():
    _seen=False
    for _it in _items:
        if _it.get("hero"):
            if _seen:
                _it.pop("hero",None)
            else:
                _seen=True

def esc_attr(s):
    return html.escape(s, quote=True)

def render_card(item):
    body = [p for p in item["body"] if p.strip() not in ("Sources:", "Sources", "")]
    body_html = "".join("<p>%s</p>" % html.escape(p) for p in body)
    sources_json = json.dumps([{"name":n,"url":u} for n,u in item["sources"]])
    pills = "".join('<span class="source-pill">%s</span>' % html.escape(n) for n,_ in item["sources"])
    cls = "hero-card" if item.get("hero") else "card"
    inner = "hero-body" if item.get("hero") else "card-body"
    return ('<div class="%s" data-title="%s" data-body="%s" data-sources="%s">'
            '<div class="%s"><h3>%s</h3><p>%s</p><div class="meta">%s</div></div></div>') % (
        cls, esc_attr(item["h3"]), esc_attr(body_html), esc_attr(sources_json),
        inner, html.escape(item["h3"]), html.escape(item["summary"]), pills)

def render_section(sid, name, accent):
    items = DATA[sid]
    parts = []
    last_sub = None
    for it in items:
        if it.get("sub") and it["sub"] != last_sub:
            parts.append('<div class="subsection-label">%s</div>' % html.escape(it["sub"]))
            last_sub = it["sub"]
        parts.append(render_card(it))
    grid = "".join(parts)
    if sid == "netherlands":
        mood = '<div class="mood-box"><h3>%s</h3><p>%s</p></div>' % (html.escape(MOOD["h3"]), html.escape(MOOD["p"]))
        grid = mood + grid
    header = ('<div class="section-header"><div class="accent" style="background:%s"></div>'
              '<h2>%s</h2><span class="count">%d stories</span></div>') % (accent, html.escape(name), len(items))
    return '<section class="section" id="%s">%s<div class="news-grid">%s</div></section>' % (sid, header, grid)

sidebar = "".join('<a href="#%s">%s</a>' % (sid, html.escape(name)) for sid,name,_ in SECTIONS)
sections_html = "".join(render_section(sid, name, accent) for sid,name,accent in SECTIONS)

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>The Daily Brief - %s</title>
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%%3E%%3Crect width='32' height='32' rx='6' fill='%%231a1a1a'/%%3E%%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='14' font-weight='bold' fill='%%23fff' text-anchor='middle'%%3EDB%%3C/text%%3E%%3C/svg%%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#faf9f6;color:#1a1a1a;line-height:1.6}
.masthead{position:relative;text-align:center;padding:2.5rem 1.2rem 1.5rem;border-bottom:3px solid #1a1a1a;margin-bottom:0}
.masthead h1{font-family:'Newsreader',serif;font-size:3rem;letter-spacing:0.15em;font-weight:700}
.masthead .date{font-size:0.95rem;color:#555;margin-top:0.3rem}
.masthead .tagline{font-family:'Newsreader',serif;font-style:italic;color:#777;margin-top:0.2rem;font-size:1rem}
.date-nav{position:absolute;left:1.2rem;top:50%%;transform:translateY(-50%%);display:flex;align-items:center;gap:0.4rem}
.date-nav button{background:none;border:1px solid #ccc;border-radius:6px;width:32px;height:32px;cursor:pointer;font-size:1rem;color:#555;display:flex;align-items:center;justify-content:center;transition:all 0.2s}
.date-nav button:hover{background:#f0eeea;border-color:#999}
.date-nav button:disabled{opacity:0.3;cursor:default}
.date-nav input[type='date']{font-family:'Inter',sans-serif;font-size:0.82rem;border:1px solid #ccc;border-radius:6px;padding:0.3rem 0.5rem;background:#fff;color:#333;cursor:pointer}
@media(max-width:768px){.date-nav{position:static;transform:none;justify-content:center;margin-bottom:0.5rem}}
.tab-bar{display:flex;justify-content:center;gap:0;border-bottom:3px solid #1a1a1a;background:#f5f4f0}
.tab-bar a{display:inline-block;padding:0.7rem 2rem;font-family:'Inter',sans-serif;font-size:0.9rem;font-weight:600;color:#777;text-decoration:none;border-bottom:3px solid transparent;margin-bottom:-3px;transition:all 0.2s}
.tab-bar a:hover{color:#1a1a1a;background:#eae8e3}
.tab-bar a.active{color:#1a1a1a;border-bottom-color:#1a1a1a}
.layout{display:flex;max-width:1400px;margin:0 auto;padding:0 1rem}
.sidebar{position:sticky;top:1rem;height:fit-content;width:220px;min-width:220px;padding-right:1.5rem;display:none}
@media(min-width:1200px){.sidebar{display:block}}
.sidebar nav a{display:block;padding:0.45rem 0.8rem;color:#555;text-decoration:none;font-size:0.82rem;border-left:3px solid transparent;transition:all 0.2s;margin-bottom:0.15rem;border-radius:0 4px 4px 0}
.sidebar nav a:hover{color:#1a1a1a;background:#f0eeea;border-left-color:#999}
.sidebar nav a.active{color:#1a1a1a;font-weight:600;border-left-color:#1a1a1a}
.main{flex:1;min-width:0;padding-bottom:4rem}
.content{flex:1;min-width:0;padding-bottom:4rem}
.section{margin-bottom:3rem}
.section-header{display:flex;align-items:center;gap:0.8rem;margin-bottom:1.5rem;padding-bottom:0.6rem;border-bottom:3px solid #1a1a1a}
.section-header .accent{width:6px;height:36px;border-radius:3px}
.section-header h2{font-family:'Newsreader',serif;font-size:1.7rem;font-weight:700}
.section-header .count{font-size:0.75rem;color:#888;margin-left:auto;white-space:nowrap}
.news-grid{column-count:3;column-gap:1.1rem}
@media(max-width:1024px){.news-grid{column-count:2}}
@media(max-width:640px){.news-grid{column-count:1}}
.subsection-label{column-span:all;font-family:'Newsreader',serif;font-size:1.15rem;font-weight:600;color:#444;margin:1.2rem 0 0.8rem;padding-bottom:0.3rem;border-bottom:1px solid #ddd}
.subsection-label:first-child{margin-top:0}
.card,.hero-card{break-inside:avoid;display:inline-block;width:100%%;background:#fff;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,0.06);margin-bottom:1.1rem;overflow:hidden;cursor:pointer;transition:all 0.2s;border:1px solid #eee}
.card:hover,.hero-card:hover{box-shadow:0 4px 16px rgba(0,0,0,0.1);transform:translateY(-2px)}
.hero-card{column-span:all}
.hero-card .hero-body{padding:1.2rem 1.5rem}
.hero-card .hero-body h3{font-family:'Newsreader',serif;font-size:1.5rem;margin-bottom:0.4rem}
.hero-card .hero-body p{color:#555;font-size:0.92rem;line-height:1.55}
.hero-card .hero-body .meta{display:flex;align-items:center;gap:0.5rem;margin-top:0.6rem;font-size:0.75rem;color:#888}
.card .card-body{padding:1rem 1.1rem}
.card .card-body h3{font-family:'Newsreader',serif;font-size:1.1rem;margin-bottom:0.3rem;line-height:1.3}
.card .card-body p{color:#555;font-size:0.85rem;line-height:1.5}
.card .card-body .meta{display:flex;align-items:center;gap:0.5rem;margin-top:0.5rem;font-size:0.72rem;color:#888}
.source-pill{display:inline-block;padding:0.15rem 0.5rem;background:#f0eeea;border-radius:12px;color:#555;text-decoration:none;font-size:0.7rem;transition:background 0.2s}
.source-pill:hover{background:#e0ddd8}
.mood-box{column-span:all;background:linear-gradient(135deg,#ffecd2,#fcb69f);border-radius:10px;padding:1.2rem 1.5rem;margin-bottom:1.1rem;border:none;box-shadow:0 1px 4px rgba(0,0,0,0.06)}
.mood-box h3{font-family:'Newsreader',serif;font-size:1.1rem;margin-bottom:0.3rem}
.mood-box p{font-size:0.88rem;color:#444}
.modal-overlay{display:none;position:fixed;top:0;left:0;width:100%%;height:100%%;background:rgba(0,0,0,0.6);z-index:1000;justify-content:center;align-items:center;padding:1rem}
.modal-overlay.active{display:flex}
.modal-content{background:#fff;border-radius:12px;max-width:680px;width:100%%;max-height:85vh;overflow-y:auto;padding:2rem;position:relative}
.modal-content h2{font-family:'Newsreader',serif;font-size:1.6rem;margin-bottom:0.8rem;line-height:1.3}
.modal-content .modal-body{font-size:0.92rem;color:#333;line-height:1.7}
.modal-content .modal-body p{margin-bottom:0.8rem}
.modal-content .modal-sources{margin-top:1.2rem;padding-top:0.8rem;border-top:1px solid #eee}
.modal-content .modal-sources a{display:inline-block;margin:0.2rem 0.3rem 0.2rem 0;padding:0.25rem 0.7rem;background:#f0eeea;border-radius:14px;color:#555;text-decoration:none;font-size:0.78rem;transition:background 0.2s}
.modal-content .modal-sources a:hover{background:#e0ddd8;color:#333}
.modal-close{position:absolute;top:1rem;right:1rem;width:36px;height:36px;border-radius:50%%;border:none;background:#f0eeea;cursor:pointer;font-size:1.2rem;display:flex;align-items:center;justify-content:center;color:#555}
.modal-close:hover{background:#ddd}
.footer{text-align:center;padding:2rem;color:#aaa;font-size:0.75rem;border-top:1px solid #eee}
</style>
</head>
<body>
<div class="masthead">
<div class="date-nav">
<button id="prev-day" aria-label="Previous day">&larr;</button>
<input type="date" id="date-picker" value="%s" min="%s" max="%s">
<button id="next-day" aria-label="Next day" disabled>&rarr;</button>
</div>
<h1>The Daily Brief</h1>
<div class="date">%s</div>
<div class="tagline">A handpicked digest of the day's signal</div>
</div>
<div class="tab-bar">
<a href="index.html" class="active">News</a>
<a href="miner-analytics.html">AI / HPC Analytics</a>
</div>
<div class="layout">
<aside class="sidebar">
<nav>
%s
</nav>
</aside>
<main class="content">
''' % (DATE_HUMAN, DATE_ISO, MIN_ISO, DATE_ISO, DATE_HUMAN, sidebar)

TAIL = '''</main>
</div>
<footer style="text-align:center;padding:2rem 1rem;color:#777;font-size:0.85rem;border-top:1px solid #eee;margin-top:2rem">The Daily Brief - daily news journal - generated automatically</footer>
<script>
const overlay=document.createElement('div');overlay.className='modal-overlay';
overlay.innerHTML='<div class="modal-content"><button class="modal-close" aria-label="Close">&times;</button><h2 id="modal-title"></h2><div class="modal-body" id="modal-body"></div><div class="modal-sources" id="modal-sources"></div></div>';
document.body.appendChild(overlay);
const modalTitle=document.getElementById('modal-title');
const modalBody=document.getElementById('modal-body');
const modalSources=document.getElementById('modal-sources');
function openModal(card){
  modalTitle.textContent=card.dataset.title;
  modalBody.innerHTML=card.dataset.body;
  const sources=JSON.parse(card.dataset.sources||'[]');
  modalSources.innerHTML='<strong style="font-size:0.85rem;color:#444">Sources:</strong><br>'+sources.map(s=>'<a href="'+s.url+'" target="_blank" rel="noopener">'+s.name+'</a>').join(' ');
  overlay.classList.add('active');
}
function closeModal(){overlay.classList.remove('active');}
document.querySelectorAll('.card,.hero-card').forEach(c=>c.addEventListener('click',()=>openModal(c)));
overlay.addEventListener('click',e=>{if(e.target===overlay)closeModal();});
overlay.querySelector('.modal-close').addEventListener('click',closeModal);
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal();});
const sections=document.querySelectorAll('.section');
const sideLinks=document.querySelectorAll('.sidebar nav a');
const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){const id=e.target.id;sideLinks.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+id));}});},{rootMargin:'-30%% 0px -60%% 0px'});
sections.forEach(s=>observer.observe(s));
const datePicker=document.getElementById('date-picker');
const prevBtn=document.getElementById('prev-day');
const nextBtn=document.getElementById('next-day');
function navigate(date){window.location.href='journal-'+date+'.html';}
datePicker.addEventListener('change',e=>{navigate(e.target.value);});
prevBtn.addEventListener('click',()=>{
  const d=new Date(datePicker.value);
  d.setDate(d.getDate()-1);
  const iso=d.toISOString().slice(0,10);
  if(iso>='%s')navigate(iso);
});
nextBtn.addEventListener('click',()=>{
  const d=new Date(datePicker.value);
  d.setDate(d.getDate()+1);
  const iso=d.toISOString().slice(0,10);
  if(iso<='%s')navigate(iso);
});
</script>
</body>
</html>''' % (MIN_ISO, DATE_ISO)

out = HEAD + sections_html + TAIL
with open(sys.argv[1] if len(sys.argv)>1 else ("journal-%s.html"%DATE_ISO), "w", encoding="utf-8") as f:
    f.write(out)
total = sum(len(v) for v in DATA.values())
print("wrote %d bytes, %d stories" % (len(out), total))
for sid,name,_ in SECTIONS:
    print("  %s: %d" % (name, len(DATA[sid])))
