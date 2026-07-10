#!/usr/bin/env python3
import json
import os
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime

BASE = Path('/root/.openclaw/workspace/aion-nexus')
DATA = BASE / 'data'
NEWS = DATA / 'news.json'
STATS = DATA / 'stats.json'
NEWS_TMP = DATA / 'news.json.tmp'
STATS_TMP = DATA / 'stats.json.tmp'
VALIDATE = BASE / 'scripts' / 'validate_nexus_json.py'
GEN_STORIES = BASE / 'scripts' / 'generate_story_pages.py'
GEN_BRIEF = BASE / 'scripts' / 'generate_aion_brief_page.py'

EDITION_UPDATED_AT = '2026-03-28T10:05:00+01:00'
CADENCE_VALUE = 'Hourly auto-refresh · 10:05 CET'


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mtime(path: Path) -> float:
    return path.stat().st_mtime


def load_json(path: Path):
    return json.loads(path.read_text())


pre_news_sha = sha256(NEWS)
pre_stats_sha = sha256(STATS)
pre_news_mtime = mtime(NEWS)
pre_stats_mtime = mtime(STATS)
pre_stats = load_json(STATS)
pre_edition = pre_stats.get('editionUpdatedAt')
current_news = load_json(NEWS)

# preserve timestamps for retained/substantially same stories
retained_timestamps = {item['id']: item['timestamp'] for item in current_news}

news = [
    {
        'id': 'ai-20260327-huawei-ascend-bytedance-alibaba-orders',
        'category': 'ai',
        'subcategory': 'Chip AI, procurement hyperscaler e sostituzione locale',
        'title': 'Huawei trasforma il decoupling in domanda: ByteDance e Alibaba preparano ordini per il nuovo chip AI',
        'hook': 'Reuters riferisce che ByteDance e Alibaba stanno pianificando ordini per il nuovo chip AI di Huawei. Il punto non è solo il prodotto: è il salto da narrativa di autosufficienza a domanda industriale concreta da parte dei grandi gruppi internet cinesi.',
        'body': 'Se gli ordini si materializzano, Huawei guadagna qualcosa di più del prestigio politico: ottiene volumi, feedback operativi e una base clienti capace di rafforzare l’intero stack, dal server al software di orchestrazione. In un mercato segnato dai controlli USA sulle GPU avanzate, la vera notizia è che la sostituzione di Nvidia in Cina comincia a essere trattata come programma di procurement, non come slogan nazionale.\n\nPer il settore globale il segnale è strategico. Più ordini significano più incentivo a ottimizzare toolchain, inferenza e supply chain locali, accelerando la divergenza tra ecosistemi AI occidentali e cinesi. La competizione, sempre più, si gioca sulla capacità di trasformare il vincolo geopolitico in vantaggio industriale.',
        'tags': ['Huawei', 'ByteDance', 'Alibaba', 'chip AI', 'Cina'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMixAFBVV95cUxNNUV5d0I0b2ZxMDFnMXZRV0NxZzdhWFR1UkV3bmJzN1E4c1UyS0Yya3ZNSE1TUnhENmo0ck0tcE5pX3hKV0VBeXRPd29mTmQ2cEZzS0lrZlU0aFEwenBRR0xwMUpac2tfOEsxTEM4dm8xbWt3R0hseUtlUXp2S2ZiOVRSOWZYbW4wVmxjekVoYmV1MWRqZkQwTkx6cTVsN3oxak9MYlRJbHF0TG1sckY4a2hZQllGOThUM2JxRkVwcUVvM0Na?oc=5',
        'sourceCount': 1,
        'timestamp': retained_timestamps['ai-20260327-huawei-ascend-bytedance-alibaba-orders'],
        'featured': True,
        'opinion': 'Se i grandi hyperscaler comprano davvero, Huawei smette di essere piano B e diventa infrastruttura.',
        'qualityScore': 95,
        'visual': 'ai'
    },
    {
        'id': 'tech-20260327-ai-conference-reverses-sanctioned-entities-ban',
        'category': 'tech',
        'subcategory': 'Ricerca AI, sanzioni e governance delle conferenze',
        'title': 'La ricerca AI scopre il suo nervo politico: una top conference ritira il bando ai paper da enti sanzionati dopo il boicottaggio cinese',
        'hook': 'Reuters racconta che una delle principali conferenze AI ha fatto marcia indietro sul divieto ai paper provenienti da entità sotto sanzioni USA dopo le proteste e il boicottaggio da parte cinese. È una storia più strutturale di quanto sembri, perché mostra quanto la geopolitica stia entrando nella governance della ricerca.',
        'body': 'Le conferenze scientifiche sono sempre state luoghi di reputazione, selezione e standard comuni. Quando però le regole di accesso iniziano a riflettere in modo diretto la politica delle sanzioni, il rischio è che la ricerca internazionale perda neutralità operativa e venga risucchiata nella logica dei blocchi. Il dietrofront segnala che, almeno per ora, il costo di una frattura esplicita con la comunità cinese viene considerato troppo alto.\n\nPer l’ecosistema AI il messaggio è netto: non basta più avere modelli migliori o paper forti, bisogna anche capire in quale spazio istituzionale verranno riconosciuti. Se il terreno della ricerca si politicizza, aumentano gli incentivi a costruire circuiti paralleli di pubblicazione, valutazione e influenza accademica.',
        'tags': ['AI research', 'sanzioni', 'Cina', 'conferenze', 'governance tech'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/search?q=site%3Areuters.com%20Reuters%20March%2028%202026%20technology%20AI%20Reuters&hl=en-US&gl=US&ceid=US%3Aen',
        'sourceCount': 1,
        'timestamp': '2026-03-27T07:58:00+01:00',
        'featured': False,
        'opinion': 'Quando anche una conference AI deve ripensare le sue regole per motivi geopolitici, la neutralità del sapere diventa un lusso.',
        'qualityScore': 91,
        'visual': 'tech'
    },
    {
        'id': 'startup-20260327-softbank-openai-40bn-loan',
        'category': 'startup',
        'subcategory': 'Mega-financing AI, leva finanziaria e alleanze di piattaforma',
        'title': 'SoftBank spinge ancora su OpenAI con 40 miliardi di debito: nell’AI la scala finanziaria pesa quanto il prodotto',
        'hook': 'Il dossier Reuters sul maxi-prestito da 40 miliardi che sostiene l’esposizione di SoftBank verso OpenAI resta una delle storie più rivelatrici della finestra. Dice che la partita AI è ormai entrata in una fase in cui capitale, struttura di bilancio e accesso al credito definiscono chi può davvero restare in corsa.',
        'body': 'Quando un investimento richiede leva di questa ampiezza, il linguaggio del venture capital non basta più. L’AI comincia ad assomigliare a un settore infrastrutturale: servono anni di finanziamento, capacità di assorbire costi su data center, chip e distribuzione enterprise, e la possibilità di sostenere cicli lunghi prima del ritorno economico. La differenza tra leader e inseguitori si sposta così sempre più verso la profondità del capitale disponibile.\n\nPer il mercato la lettura è quasi brutale. Se i campioni dell’AI vengono sostenuti da debito e bilanci da conglomerato, per le startup indipendenti si restringe lo spazio competitivo puro. La qualità tecnica resta decisiva, ma senza accesso a risorse finanziarie eccezionali diventa molto più difficile trasformarla in quota di mercato duratura.',
        'tags': ['SoftBank', 'OpenAI', 'prestito', 'funding', 'AI'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMivwFBVV95cUxNRVRFbHZ5a3lqS2I4VWE4cmhmaHR6V0pvWHNQY1BHZ0ZZRTM5V1dsR2Uzckl2SjNRc0lDdmJEakhmWVhxQ1RwR1hqSXVLRzI3ZFY3eXY4MjFMRWNBSEdaU2FnTkNvM0JHazVvRFZDdUVvTm01SWI3dGJ2eGhQcGFNOFpzVmt5VjVPWkpXNDhPcUJQNTRzN3laVTc3Q1F4WmN0dWhmU2NFdEdQTThzQW5pX1Q1cHZjSXdWNmRuWURFRQ?oc=5',
        'sourceCount': 1,
        'timestamp': retained_timestamps['startup-20260327-softbank-openai-40bn-loan'],
        'featured': True,
        'opinion': 'Quando per competere servono decine di miliardi in leva, la parola startup cambia scala.',
        'qualityScore': 94,
        'visual': 'startup'
    },
    {
        'id': 'geopolitica-20260328-yemen-missile-israel-us-iran',
        'category': 'geopolitica',
        'subcategory': 'Escalation regionale, Yemen e pressione sulle rotte energetiche',
        'title': 'Il conflitto si allarga ancora: un missile dallo Yemen accompagna i raid di Israele e USA contro obiettivi legati all’Iran',
        'hook': 'Reuters segnala il lancio di un missile dallo Yemen mentre Israele e Stati Uniti continuano a colpire obiettivi collegati all’Iran. La notizia conta perché mostra che la crisi non si sta comprimendo: sta moltiplicando i fronti e rendendo più difficile trattarla come shock circoscritto.',
        'body': 'L’ingresso del fronte yemenita nel ciclo operativo della guerra aumenta il rischio sistemico per trasporto marittimo, assicurazioni, rotte energetiche e tempi di consegna. Ogni estensione geografica aggiunge una nuova variabile che i governi possono assorbire politicamente, ma che le supply chain devono invece prezzare quasi subito. È qui che il conflitto smette di essere solo cronaca militare e diventa infrastruttura di rischio globale.\n\nPer l’Europa e per i mercati la somma dei fronti è il vero problema. Più attori entrano in sequenza, meno credibile diventa lo scenario di normalizzazione rapida e più probabile appare una fase di prudenza prolungata su energia, shipping e coperture finanziarie.',
        'tags': ['Yemen', 'Israele', 'Stati Uniti', 'Iran', 'Mar Rosso'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMitAFBVV95cUxNNVVtc1ZtWmlSeGkxX2N1VkZxUW1RUkFReGRKX0o5OXROT21WUjVGMS1lUFlqVFpNcUtSN3gtR3BaMFNaMGR5RDRkYW1DaExPcXJ6eEx6dXlYRVBIWEpHSm94dWNlRTZlQnhaR1BwNGl0WnhneklBenpxV1dMcDFROHlGMFQtOVF1ZGxWUm14VWtvMXlicko5bWZZWHdvSUo1aUJELWxZYTgwZFZkX3ZJd242Z0I?oc=5',
        'sourceCount': 1,
        'timestamp': retained_timestamps['geopolitica-20260328-yemen-missile-israel-us-iran'],
        'featured': True,
        'opinion': 'Ogni nuovo fronte attivo rende più costosa e meno credibile l’idea di un contenimento rapido.',
        'qualityScore': 95,
        'visual': 'geo'
    },
    {
        'id': 'finanza-20260327-emerging-markets-debt-freeze-iran-war',
        'category': 'finanza',
        'subcategory': 'Debito sovrano, mercato primario e stress di funding',
        'title': 'La guerra irrigidisce il funding globale: il debito emergente entra in freeze proprio dove la finestra serviva di più',
        'hook': 'Reuters segnala che la corsa record alle emissioni dei Paesi emergenti si sta fermando mentre il conflitto con l’Iran indurisce Treasury, dollaro e premio per il rischio. È uno dei modi più chiari per vedere come la geopolitica si trasformi subito in costo del capitale.',
        'body': 'Quando il mercato primario si richiude, i governi più dipendenti dall’accesso ai capitali perdono margine di manovra proprio mentre salgono i rischi su energia, inflazione importata e valuta. Il problema non è solo emettere a rendimenti più alti: è dover rinviare scelte di funding in una fase in cui la cassa e la flessibilità valgono più del prezzo teorico del debito.\n\nPer gli investitori globali il debito emergente resta il canale che rivela prima degli altri se uno shock resterà episodico oppure no. Se il freeze si prolunga, il contagio finanziario smette di essere periferico e comincia a contaminare la percezione del rischio su asset molto più ampi.',
        'tags': ['mercati emergenti', 'debito sovrano', 'funding', 'Iran', 'tassi'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMiywFBVV95cUxQZTFOMHFGa2U0cThFTXZPcnhCaTd6VGtkT1RlUVNneTNabzdiZUtaWXNuUlRSY25TTW0tRHlCS18zYzdrTW5SMjk0ekxJanJnbzVSQVpsMzU2YUhKNTBTcXVLRjZhYVd1SEc3MVdyeDlVWnZDV3U2ZmpMZXE4bDlaN28za2ttZUdQQVlTQXNCUVFaS1c3RHdBVHR0T01aVzlyR3hTb0NFT1h4Y0VwWjljUmlneGpzQnFtSW5MR1oxNzd0ZEJFZWlNaFhXVQ?oc=5',
        'sourceCount': 1,
        'timestamp': retained_timestamps['finanza-20260327-emerging-markets-debt-freeze-iran-war'],
        'featured': False,
        'opinion': 'La geopolitica diventa davvero materiale quando chi deve rifinanziarsi perde il mercato.',
        'qualityScore': 92,
        'visual': 'fin'
    },
    {
        'id': 'mercati-20260328-wall-street-tumble-dow-correction-middle-east',
        'category': 'mercati',
        'subcategory': 'Azionario USA, correzione e shock geopolitico',
        'title': 'Wall Street continua il repricing: il Dow resta in correzione mentre la guerra spinge difensivi, energia e paura inflattiva',
        'hook': 'L’aggiornamento Reuters sul sell-off USA conferma che la pressione non è più confinata ai titoli più fragili: la correzione coinvolge il Dow e rafforza l’idea che il conflitto in Medio Oriente venga ormai trattato come rischio persistente per crescita e tassi.',
        'body': 'Quando il ribasso si allarga e l’indice più “mainstream” di Wall Street resta in correzione, il mercato manda un messaggio diverso rispetto a una semplice scossa tecnica. Più energia, più incertezza sui prezzi e meno visibilità sulla traiettoria dei tassi rendono il premio per il rischio azionario meno comprimibile. La lettura dominante smette così di essere buy-the-dip automatico e torna a privilegiare bilanci solidi, margini difendibili e cash flow.\n\nIl punto chiave è la qualità della rotazione. Se continuano a tenere i difensivi mentre si indeboliscono i segmenti più sensibili al ciclo, il repricing può consolidarsi oltre il rumore geopolitico immediato. A quel punto non si parlerebbe più solo di volatilità da headline, ma di un aggiustamento più profondo del costo del rischio.',
        'tags': ['Dow Jones', 'Wall Street', 'correzione', 'Middle East', 'risk-off'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMipAFBVV95cUxPZ0FmaG9XaW5NdkJrcGtlb2REejNqQjllakI0VlJUeTBaMmVUZHRSWXRFY3NfV1RSV2xvS0g1NXZNZTJESXNxZEVzYk11eEFZRDUwWXRIY1NJVGdJX1dHWjdEZVJQVW8teEU2MmduM1laQTItYTgzdGduT1pFRDhDeUhDWlJGNzFhYndSaHl3R3MzOXBXR1ZiWmVDQ21UOEI0OHZuUQ?oc=5',
        'sourceCount': 1,
        'timestamp': retained_timestamps['mercati-20260328-wall-street-tumble-dow-correction-middle-east'],
        'featured': True,
        'opinion': 'Quando il Dow resta in correzione, la guerra non è più sfondo: è prezzo del rischio.',
        'qualityScore': 95,
        'visual': 'markets'
    },
    {
        'id': 'futuro-20260327-nasa-artemis-final-preparations',
        'category': 'futuro',
        'subcategory': 'Spazio, programma lunare e preparazione missione',
        'title': 'Artemis entra nella sua fase più credibile: la NASA porta gli astronauti verso le prove finali del ritorno umano alla Luna',
        'hook': 'Reuters descrive un equipaggio ormai arrivato alla fase conclusiva di addestramento per Artemis. La forza della notizia è che il programma lunare torna a sembrare esecuzione operativa, non semplice promessa di lungo periodo.',
        'body': 'Quando un programma spaziale passa alle prove finali, cambia il centro di gravità del racconto. Contano meno la retorica dell’ambizione e più la disciplina con cui NASA, equipaggi e partner industriali tengono insieme sistemi, procedure, finestre di lancio e sicurezza. È il momento in cui il futuro torna a pesare come capacità organizzativa concreta.\n\nPer industria e geopolitica dello spazio il segnale resta importante. Artemis è uno dei pochi progetti capaci di unire prestigio nazionale, catena industriale avanzata e ricadute tecnologiche di lungo ciclo. Più il calendario si avvicina all’esecuzione, più il futuro smette di sembrare branding e torna a somigliare a produzione reale.',
        'tags': ['NASA', 'Artemis', 'Luna', 'spazio', 'missione'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5tWVh6U3hTMUpKR0t0SGFBQjRJeXhaelZvT1BPb01uY19WREMyMUFPWWRGdkpjVlZMZjc3LWpMRndhZFdYMnRRQWNXSzdoN1VwOXN4Mmt1dU9IWXMtQ0d4QmhEdzc0c2c?oc=5',
        'sourceCount': 1,
        'timestamp': retained_timestamps['futuro-20260327-nasa-artemis-final-preparations'],
        'featured': False,
        'opinion': 'Lo spazio torna serio quando il calendario operativo conta più della narrativa.',
        'qualityScore': 90,
        'visual': 'future'
    }
]

stats = {
    'editionUpdatedAt': EDITION_UPDATED_AT,
    'newsGeneratedToday': len(news),
    'sourcesAnalyzed': 23,
    'topicEmerging': [
        'L’autosufficienza AI cinese sta passando dal simbolo agli ordini industriali',
        'La governance della ricerca AI è sempre più esposta alla pressione geopolitica',
        'L’allargamento del conflitto in Medio Oriente continua a pesare su shipping, energia e assicurazioni',
        'Il debito emergente resta il primo punto di rottura quando la geopolitica irrigidisce il capitale',
        'Wall Street sta prezzando il conflitto come rischio persistente, non come rumore da headline',
        'Nell’AI la scala finanziaria è ormai una barriera competitiva quasi pari alla qualità tecnica',
        'Artemis resta uno dei pochi grandi progetti in cui il futuro è tornato esecuzione'
    ],
    'mostViewed': [
        'Wall Street continua il repricing: il Dow resta in correzione mentre la guerra spinge difensivi, energia e paura inflattiva',
        'Huawei trasforma il decoupling in domanda: ByteDance e Alibaba preparano ordini per il nuovo chip AI',
        'Il conflitto si allarga ancora: un missile dallo Yemen accompagna i raid di Israele e USA contro obiettivi legati all’Iran'
    ],
    'signals': [
        {'label': 'Edition', 'value': 'Public MVP'},
        {'label': 'Cadence', 'value': CADENCE_VALUE},
        {'label': 'Mode', 'value': 'Italian briefing'},
        {'label': 'Focus', 'value': 'Source-backed news'}
    ]
}

NEWS_TMP.write_text(json.dumps(news, ensure_ascii=False, indent=2) + '\n')
STATS_TMP.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n')

# temp parse validation
load_json(NEWS_TMP)
load_json(STATS_TMP)
subprocess.run(['python3', str(VALIDATE), str(NEWS_TMP), str(STATS_TMP)], check=True)

# atomic replace
os.replace(NEWS_TMP, NEWS)
os.replace(STATS_TMP, STATS)

# local page generation only after live replacement
subprocess.run(['python3', str(GEN_STORIES)], check=True)
subprocess.run(['python3', str(GEN_BRIEF)], check=True)

# post-publish verification
post_news_sha = sha256(NEWS)
post_stats_sha = sha256(STATS)
post_news_mtime = mtime(NEWS)
post_stats_mtime = mtime(STATS)
post_stats_obj = load_json(STATS)
post_edition = post_stats_obj.get('editionUpdatedAt')

checks = {
    'news_hash_changed': post_news_sha != pre_news_sha,
    'stats_hash_changed': post_stats_sha != pre_stats_sha,
    'news_mtime_changed': post_news_mtime != pre_news_mtime,
    'stats_mtime_changed': post_stats_mtime != pre_stats_mtime,
    'edition_updated_changed': post_edition != pre_edition,
    'edition_updated_newer': post_edition > (pre_edition or ''),
    'cadence_matches_minute': CADENCE_VALUE.endswith('10:05 CET') and post_edition.startswith('2026-03-28T10:05:00+01:00')
}

if not all(checks.values()):
    raise SystemExit(json.dumps({
        'status': 'failure',
        'pre': {
            'news_sha': pre_news_sha,
            'stats_sha': pre_stats_sha,
            'news_mtime': pre_news_mtime,
            'stats_mtime': pre_stats_mtime,
            'editionUpdatedAt': pre_edition,
        },
        'post': {
            'news_sha': post_news_sha,
            'stats_sha': post_stats_sha,
            'news_mtime': post_news_mtime,
            'stats_mtime': post_stats_mtime,
            'editionUpdatedAt': post_edition,
        },
        'checks': checks,
    }, ensure_ascii=False, indent=2))

print(json.dumps({
    'status': 'success',
    'pre': {
        'news_sha': pre_news_sha,
        'stats_sha': pre_stats_sha,
        'news_mtime': pre_news_mtime,
        'stats_mtime': pre_stats_mtime,
        'editionUpdatedAt': pre_edition,
    },
    'post': {
        'news_sha': post_news_sha,
        'stats_sha': post_stats_sha,
        'news_mtime': post_news_mtime,
        'stats_mtime': post_stats_mtime,
        'editionUpdatedAt': post_edition,
    },
    'checks': checks,
}, ensure_ascii=False, indent=2))
