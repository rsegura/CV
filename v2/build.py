from pathlib import Path
import re,html
ROOT=Path(__file__).resolve().parent
source=(ROOT.parent/'index.html').read_text()
def section(id):
 return re.search(r'<section[^>]*id="'+id+r'".*?</section>',source,re.S)[0]
def text(s):return html.unescape(re.sub('<[^>]+>','',s)).strip()
def projects(id):
 s=section(id)
 cards=re.findall(r'      <div class="project-card".*?\n      </div>',s,re.S)
 out=[]
 for i,c in enumerate(cards):
  title=re.search(r'<h3>(.*?) <span class="arrow">',c,re.S)[1]
  domain=re.search(r'<div class="card-domain[^>]*>(.*?)</div>',c,re.S)[1]
  summary=re.search(r'<p class="card-summary">(.*?)</p>',c,re.S)[1]
  detail=c.split('<div class="card-detail">',1)[1].rsplit('</div>',2)[0]
  out.append(f'<article class="project" id="{id}-{i+1}"><p class="eyebrow">{domain}</p><h3>{title}</h3><p class="project-summary">{summary}</p><details><summary>Architecture &amp; approach <span aria-hidden="true">+</span></summary><div class="project-detail">{detail}</div></details></article>')
 return '\n'.join(out)
social='''<div class="socials"><a href="https://www.linkedin.com/in/robersegsal/" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span></a><a href="https://github.com/rsegura" target="_blank" rel="noopener noreferrer">GitHub <span aria-hidden="true">↗</span></a><a href="https://x.com/Rober_Segura" target="_blank" rel="noopener noreferrer">X <span aria-hidden="true">↗</span></a></div>'''
def page(name,title,body):
 nav=''.join(f'<a href="{path}"'+(' aria-current="page"' if name==path else '')+f'>{label}</a>' for path,label in [('index.html','About'),('experience.html','Experience'),('projects.html','Projects'),('learning.html','Learning')])
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Roberto Segura Sala — data platforms, applied AI and technical leadership. Experience, personal projects and ongoing learning."><title>{title} — Roberto Segura Sala</title><link rel="stylesheet" href="assets/style.css"></head><body>
<a class="skip" href="#main">Skip to content</a><div class="site"><header class="site-header"><a class="wordmark" href="index.html" aria-label="Roberto Segura Sala, home">rs<span>.</span></a><nav aria-label="Main navigation">{nav}</nav><a class="download" href="assets/roberto-segura-cv.pdf" download>Download CV <span aria-hidden="true">↓</span></a></header>
<main id="main">{body}</main><footer><div><a class="footer-name" href="index.html">Roberto Segura Sala</a><p>Madrid · Building, learning, sharing.</p></div>{social}<span class="copyright">© 2026</span></footer></div></body></html>'''
hero='''<section class="intro"><p class="eyebrow"><span class="dot"></span> Roberto Segura Sala · Madrid</p><h1>AI / Data Platform Engineer</h1><p class="lead">Hi, I’m Roberto. Originally from Cuenca, a curious person and proud dad of two. I’m always learning, looking for ways to improve, and finding new things to explore.</p><p class="lead">I’m passionate about AI and data: understanding how things work, experimenting with ideas, and building useful solutions. At Audiense, I work as an AI / Data Platform Engineer.</p><div class="intro-meta">Engineering since 2011</div>'''+social+'''</section>
<section class="home-work"><div class="section-heading"><div><p class="eyebrow">A few things I work on</p><h2>From architecture to everyday use.</h2></div><a class="text-link" href="projects.html">Explore the work <span aria-hidden="true">↗</span></a></div><div class="highlights">
<a class="highlight" href="projects.html#projects-1"><span class="number">01 / DATA SYSTEMS</span><h3>Streaming at scale.</h3><p>Terabyte-scale Iceberg tables and dozens of real-time consumers. Building and operating the platform behind audience enrichment.</p><span class="highlight-foot">Iceberg · Kafka · Trino <span aria-hidden="true">↗</span></span></a>
<a class="highlight" href="projects.html#projects-3"><span class="number">02 / APPLIED AI</span><h3>Models, put to work.</h3><p>LoRA fine-tuning, reranking, and inference with vLLM on Kubernetes. Reaching more profiles with more accurate interest assignments.</p><span class="highlight-foot">Embeddings · LoRA · vLLM <span aria-hidden="true">↗</span></span></a>
<a class="highlight" href="projects.html#projects-4"><span class="number">03 / PLATFORM ADOPTION</span><h3>Make data useful.</h3><p>Helping product teams adopt VEGA: fewer systems, lower costs, and new product verticals previously constrained by scale.</p><span class="highlight-foot">Architecture · Product · Collaboration <span aria-hidden="true">↗</span></span></a>
</div></section>
<section class="about-story"><div><p class="eyebrow">How I work</p><h2>Curiosity, with<br>responsibility.</h2></div><div class="prose"><p>I enjoy continuous learning and applying what I learn to complex problems. I work comfortably with a high degree of autonomy, helping give shape to needs that are not fully defined yet.</p><p>At Audiense, I combine an end-to-end view of the data platform with hands-on engineering. I connect architectural decisions with product needs, help teams adopt solutions, and share knowledge so others can work more independently.</p><p>Outside work, I explore agents through personal prototypes and maintain an AI research wiki. Building things is one of the ways I learn.</p><a class="text-link" href="projects.html#personal">Explore my personal projects <span aria-hidden="true">↗</span></a></div></section>'''
experience='''<header class="page-intro"><p class="eyebrow">Experience</p><h1>Technical depth.<br><span class="muted">A platform-wide view.</span></h1><p class="lead">From backend engineering to data platforms and applied AI, with hands-on work, cross-team collaboration, and technical mentoring.</p></header>'''+section('career')+section('skills')
proj='''<header class="page-intro"><p class="eyebrow">Selected work</p><h1>Complex problems.<br><span class="muted">Concrete solutions.</span></h1><p class="lead">The scale, decisions, and architecture behind my work. Professional systems at Audiense, followed by personal experiments.</p><div class="section-jumps"><a href="#professional">Professional work ↓</a><a href="#personal">Personal projects ↓</a></div></header><section id="professional"><div class="section-heading"><div><p class="eyebrow">Audiense · 2021–present</p><h2>Professional work</h2></div><span class="section-count">07 projects</span></div><div class="projects-list">'''+projects('projects')+'''</div></section><section id="personal"><div class="section-heading"><div><p class="eyebrow">Learning through experimentation</p><h2>Personal projects &amp; research</h2></div><span class="section-count">04 explorations</span></div><p class="section-intro">Self-directed learning projects, separate from my professional work.</p><div class="projects-list">'''+projects('personal')+'''</div></section>'''
learning='''<header class="page-intro"><p class="eyebrow">Learning</p><h1>Always a student.<br><span class="muted">Always building.</span></h1><p class="lead">Formal education, continued training, and the books shaping what I explore next.</p></header>'''+section('reading')+section('education')+section('certs')
for name,title,body in [('index.html','About',hero),('experience.html','Experience',experience),('projects.html','Projects',proj),('learning.html','Learning',learning)]:
 (ROOT/name).write_text(page(name,title,body))
print('Built four static pages from approved content.')
