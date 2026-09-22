from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
import shutil
ROOT=Path(__file__).resolve().parent
styles={
'name':ParagraphStyle('name',fontName='Helvetica-Bold',fontSize=25,leading=29,textColor=HexColor('#202522'),spaceAfter=8),
'kicker':ParagraphStyle('kicker',fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=HexColor('#26765d'),spaceAfter=10),
'h':ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=14,leading=18,textColor=HexColor('#26765d'),spaceBefore=14,spaceAfter=8),
'role':ParagraphStyle('role',fontName='Helvetica-Bold',fontSize=10,leading=14,spaceBefore=8,spaceAfter=3),
'body':ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=13,textColor=HexColor('#424b45'),spaceAfter=5),
'small':ParagraphStyle('small',fontName='Helvetica',fontSize=8,leading=11,textColor=HexColor('#68716a'),spaceAfter=7),
'bullet':ParagraphStyle('bullet',fontName='Helvetica',fontSize=9,leading=13,textColor=HexColor('#424b45'),leftIndent=10,firstLineIndent=-8,spaceAfter=5)}
flow=[]
def add(t,style='body'):flow.append(Paragraph(t,styles[style]))
def bullet(t):add('- '+t,'bullet')
def role(title,dates,body=None):
 add(title,'role');add(dates,'small')
 if body:add(body)
add('Roberto Segura Sala','name')
add('DATA PLATFORMS / APPLIED AI / TECHNICAL LEADERSHIP','kicker')
add('Madrid, Spain · Engineering since 2011<br/><link href="https://www.linkedin.com/in/robersegsal/" color="#26765d">LinkedIn: robersegsal</link> &nbsp; | &nbsp; <link href="https://github.com/rsegura" color="#26765d">GitHub: rsegura</link> &nbsp; | &nbsp; <link href="https://x.com/Rober_Segura" color="#26765d">X: Rober_Segura</link>','small')
add('I combine platform-wide technical direction with hands-on engineering and collaboration with product teams. I enjoy continuous learning, complex problems, and turning loosely defined needs into concrete solutions with a high degree of autonomy.')
add('Professional experience','h')
role('Audiense | Backend, Big Data &amp; Real Time Engineer','Jan 2021 - Present','Technical leader for the data platform, combining architecture, implementation, cross-team adoption, and mentoring.')
for t in [
'Led the adoption of Trino and Apache Iceberg, creating and maintaining terabyte-scale tables and coordinating dozens of real-time consumers. Completed the migration to real-time enrichment.',
'Drove VEGA adoption by product teams, reducing costs and reliance on separate systems while enabling new data-driven product verticals previously constrained by scale.',
'Improved query performance through table statistics and join optimization, lowering network traffic and CPU use; introduced retries to reduce query failures.',
'Expanded interest enrichment to more profiles and improved assignment correctness through LoRA fine-tuning and reranking, with model serving on Kubernetes and vLLM.',
'Mentors engineers in AI-assisted development and supports teams in adopting the data platform.']:bullet(t)
role('TMC | Data Platform Engineer','Sep 2020 - Jan 2021')
role('Future Space | Data Platform Engineer','Sep 2019 - Sep 2020','Conceptualized and developed a production platform for fraud analysis in motor insurance claims using Scala, Kafka, Akka, and Cassandra.')
role('Earlier experience','2011 - 2019')
add('<b>everis</b> | Big Data Engineer | Feb 2018 - Sep 2019<br/>Batch and streaming systems, Kafka Streams model deployment, ELK monitoring.')
add('<b>Finect</b> | Senior Developer | Jan - Oct 2017<br/>Node.js APIs, OAuth2, and data analysis planning.')
add('<b>playthe.net</b> | Big Data Engineer | May 2014 - Dec 2016<br/>Real-time footfall analytics with Spark Streaming and Cassandra; IoT integration.')
add('<b>Primum Health IT</b> | Liferay Engineer | Aug 2013 - Apr 2014<br/><b>amaranto Consultores</b> | Senior Developer | Dec 2011 - Aug 2013<br/><b>UCLM</b> | Junior Developer | Jan - Aug 2011','small')
flow.append(PageBreak())
add('Engineering, learning &amp; exploration','name')
add('SELECTED TECHNICAL WORK','kicker')
role('Streaming data &amp; asynchronous query architecture','')
add('Iceberg data lake maintained through streaming enrichment. VEGA unifies Athena and Trino behind an asynchronous API with queue-based decoupling, execution traceability, retries, and Redis rate limiting.')
role('Applied machine learning &amp; inference','')
add('Interest classification across 444 categories using LoRA-tuned embeddings, cross-encoder reranking, and model agreement. Evaluation F1 improved from 0.255 to 0.390 after fine-tuning; strict precision rose from 36% to 52% with model agreement. Kubernetes and vLLM serving connect inference to streaming consumers; Qwen models support near-real-time enrichment.')
add('Technical expertise','h')
add('<b>Data:</b> Kafka, Redpanda, Kafka Streams, Spark, Iceberg, Trino, Athena, Parquet.<br/><b>AI:</b> Sentence Transformers, LoRA/PEFT, reranking, spaCy, vLLM, Qwen, agent harnesses.<br/><b>Backend &amp; infrastructure:</b> Python, Scala, SQL, Node.js, FastAPI, Akka HTTP, AWS, Kubernetes, Docker, Terraform, Redis, Cassandra, SQLite.<br/><b>Leadership:</b> architecture direction, platform adoption, product collaboration, technical mentoring.')
add('Personal projects &amp; research','h')
bullet('<b>Hermes Expense Tracker:</b> conversational household expense tracking with per-member Hermes assistants, a Python FastMCP domain server, SQLite, and Telegram/CLI access.')
bullet('<b>Voice Agent Architecture Prototype:</b> hands-on exploration of STT, LLM orchestration, TTS, and durable conversation state using LiveKit, Deepgram, and ElevenLabs.')
bullet('<b>Math Tutor:</b> voice-agent prototype with a validation harness and deterministic educational rules, separated from model providers and tested through offline evaluations.')
bullet('<b>AI Research Wiki:</b> Obsidian knowledge vault developed with Hermes Agent, linking sources, concepts, comparisons, and research syntheses.')
add('Education &amp; selected learning','h')
add('<b>Master in Big Data Development</b> | Hadoop Training - UCLM | 2015 - 2016<br/><b>Bachelor\'s Degree in Telecommunications</b> | UCLM')
add('Data Streaming Nanodegree - Udacity, 2021.<br/>Confluent Certified Developer for Apache Kafka - awarded 2018; expired Jan 2022.<br/>Generative AI and LLMs: Architecture and Data Preparation - IBM, 2026.','small')
add('Recent reading','h')
add('<b>Currently reading:</b> Domain-Specific Small Language Models.<br/><b>Completed:</b> Designing Data-Intensive Applications; Build a Large Language Model (From Scratch); Build an AI Agent (From Scratch).','small')
def footer(c,doc):
 c.setStrokeColor(HexColor('#e6e9e4'));c.line(42,35,A4[0]-42,35)
 c.setFont('Helvetica',8);c.setFillColor(HexColor('#68716a'));c.drawString(42,23,'Roberto Segura Sala');c.drawRightString(A4[0]-42,23,str(doc.page))
output=ROOT/'assets/roberto-segura-cv.pdf'
SimpleDocTemplate(str(output),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=46,title='Roberto Segura Sala - CV',author='Roberto Segura Sala').build(flow,onFirstPage=footer,onLaterPages=footer)
shutil.copy2(output,ROOT.parent/'output/pdf/roberto-segura-cv.pdf')
print(output)
