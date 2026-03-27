#!/usr/bin/env python3
import hashlib
import json
import os
import subprocess
from pathlib import Path

BASE = Path('/root/.openclaw/workspace/aion-nexus/data')
NEWS = BASE / 'news.json'
STATS = BASE / 'stats.json'
NEWS_TMP = BASE / 'news.json.tmp'
STATS_TMP = BASE / 'stats.json.tmp'
VALIDATOR = Path('/root/.openclaw/workspace/aion-nexus/scripts/validate_nexus_json.py')

EDITION_TS = '2026-03-26T15:05:00+01:00'
CADENCE = 'Hourly auto-refresh · 15:05 CET'


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mtime_ns(path: Path) -> int:
    return path.stat().st_mtime_ns


pre_news_sha = sha256(NEWS)
pre_stats_sha = sha256(STATS)
pre_news_mtime = mtime_ns(NEWS)
pre_stats_mtime = mtime_ns(STATS)
pre_stats_json = json.loads(STATS.read_text(encoding='utf-8'))
pre_edition = pre_stats_json.get('editionUpdatedAt')
current_news = json.loads(NEWS.read_text(encoding='utf-8'))
current_by_id = {item['id']: item for item in current_news}


def keep_ts(item_id: str, default: str) -> str:
    return current_by_id.get(item_id, {}).get('timestamp', default)


news = [
    {
        'id': 'ai-20260325-manus-meta-china-exit-restrictions',
        'category': 'ai',
        'subcategory': 'Sovranità tecnologica, M&A transfrontaliera e controllo dei founder',
        'title': 'Manus-Meta, la Cina trasforma i founder AI in leva strategica',
        'hook': 'Reuters riferisce che due cofondatori di Manus non possono lasciare la Cina mentre Pechino riesamina la vendita a Meta. Il punto non è più solo il prezzo del deal: è il controllo sul talento che rende operativi agenti e know-how.',
        'body': 'Quando la review regolatoria tocca direttamente la mobilità dei fondatori, il mercato capisce che l’AI non viene più trattata come semplice software. Team, competenze e capacità di esecuzione diventano asset sensibili quasi quanto chip, dati e infrastrutture, e ogni acquisizione transfrontaliera inizia a portarsi dietro un premio politico stabile.\n\nPer Meta questo dossier vale più di una singola operazione: è un test su quanto sarà ancora praticabile comprare all’estero piattaforme agentiche complete, con persone chiave incluse. Se Pechino consolida questo approccio, l’M&A globale sull’AI dovrà convivere con diligence più dure, tempi più lunghi e clausole costruite attorno alla sovranità tecnologica.',
        'tags': ['Manus', 'Meta', 'Cina', 'AI agents', 'M&A'],
        'sourceLabel': 'Reuters / FT',
        'sourceUrl': 'https://whtc.com/2026/03/25/china-bars-manus-co-founders-from-leaving-country-as-it-reviews-sale-to-meta-ft-reports/',
        'sourceCount': 2,
        'timestamp': keep_ts('ai-20260325-manus-meta-china-exit-restrictions', '2026-03-25T08:05:00+01:00'),
        'featured': True,
        'opinion': 'Se la review blocca i founder, la geopolitica dell’AI è già dentro il term sheet.',
        'qualityScore': 96,
        'visual': 'ai'
    },
    {
        'id': 'tech-20260326-microsoft-copilot-wave3-frontier-seoul',
        'category': 'tech',
        'subcategory': 'Enterprise software, agenti e diffusione operativa dell’AI',
        'title': 'Microsoft alza la posta su Copilot: da assistente a layer operativo per l’impresa',
        'hook': 'Al Microsoft AI Tour Seoul l’azienda rilancia Wave 3 di Microsoft 365 Copilot, Copilot Cowork e il nuovo piano Microsoft 365 E7. Il messaggio è chiaro: la fase delle demo generative lascia spazio a stack agentici più profondi dentro i workflow aziendali.',
        'body': 'La novità pesa perché sposta Copilot dal supporto occasionale all’orchestrazione di attività multi-step con più contesto su posta, calendari, documenti e identità aziendale. Se questa promessa regge nell’uso reale, Microsoft rafforza il vantaggio distributivo della suite produttiva già installata nelle grandi organizzazioni e rende più costoso per i concorrenti entrare a valle.\n\nIl segnale più forte è commerciale e infrastrutturale insieme: gli agenti vengono impacchettati con sicurezza, governance e amministrazione enterprise. In pratica Microsoft sta dicendo ai CIO che la prossima ondata AI non si compra come funzione accessoria, ma come livello operativo integrato con controllo, compliance e rollout su larga scala.',
        'tags': ['Microsoft', 'Copilot', 'agenti AI', 'enterprise software', 'Corea'],
        'sourceLabel': 'Microsoft',
        'sourceUrl': 'https://news.microsoft.com/source/asia/2026/03/26/microsoft-positions-korea-as-a-global-ai-hub-moving-beyond-experimentation-to-full-scale-frontier-transformation/?lang=ko',
        'sourceCount': 1,
        'timestamp': keep_ts('tech-20260326-microsoft-copilot-wave3-frontier-seoul', '2026-03-26T07:00:00+01:00'),
        'featured': True,
        'opinion': 'Chi controlla la suite di lavoro prova ora a controllare anche il layer degli agenti.',
        'qualityScore': 91,
        'visual': 'tech'
    },
    {
        'id': 'geopolitica-20260326-iran-us-proposal-negative-response',
        'category': 'geopolitica',
        'subcategory': 'Medio Oriente, diplomazia coercitiva e rischio di allargamento del conflitto',
        'title': 'Iran-USA, la risposta fredda di Teheran tiene aperta solo una tregua di carta',
        'hook': 'Un alto funzionario iraniano dice a Reuters che la prima risposta di Teheran alla proposta USA per fermare la guerra non è stata positiva. La finestra diplomatica non è chiusa, ma resta troppo stretta per comprimere davvero il premio geopolitico.',
        'body': 'Il punto chiave non è soltanto il rifiuto iniziale, ma la zona grigia in cui resta la trattativa: non un no definitivo, non un sì operativo. Questo lascia mercati, alleati occidentali e operatori energetici sospesi tra una possibile de-escalation e il rischio concreto che il conflitto continui a contagiare energia, trasporti e postura militare regionale.\n\nPer Europa e G7 significa lavorare su deterrenza, catene logistiche e canali diplomatici nello stesso momento, senza poter contare su una soluzione rapida. Finché Teheran segnala freddezza e Washington continua a testare una via negoziale, la variabile dominante non è la tregua ma la durata dell’incertezza.',
        'tags': ['Iran', 'USA', 'Medio Oriente', 'diplomazia', 'guerra'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://www.tbsnews.net/world/irans-initial-response-us-proposal-not-positive-senior-iranian-official-tells-reuters-1394161',
        'sourceCount': 1,
        'timestamp': keep_ts('geopolitica-20260326-iran-us-proposal-negative-response', '2026-03-26T08:45:00+01:00'),
        'featured': True,
        'opinion': 'Con Teheran fredda, il mercato continua a prezzare più durata del conflitto che compromesso.',
        'qualityScore': 94,
        'visual': 'geo'
    },
    {
        'id': 'finanza-20260326-ecb-nagel-april-hike-option',
        'category': 'finanza',
        'subcategory': 'Banche centrali, shock energetico e rischio di secondo round inflazionistico',
        'title': 'Nagel riapre il dossier rialzi BCE: l’energia rimette aprile sul tavolo',
        'hook': 'In un’intervista a Reuters, Joachim Nagel dice che un rialzo dei tassi BCE ad aprile è un’opzione se la guerra in Medio Oriente alimenta un nuovo shock inflazionistico. I mercati tornano a guardare non solo alla crescita, ma anche al rischio di trasmissione dell’energia ai prezzi interni.',
        'body': 'Il passaggio più importante non è solo il tono da falco del governatore tedesco, ma l’idea che Francoforte possa muoversi già al prossimo meeting se vedrà rincari oltre l’energia e pressioni salariali più persistenti. Dopo una fase in cui la traiettoria sembrava più leggibile, il conflitto in Medio Oriente riporta l’eurozona in uno scenario da banca centrale in allerta permanente.\n\nPer l’Europa il problema resta asimmetrico: importare energia cara significa importare anche fragilità macro e politica. Se petrolio, gas e chimica rimangono sotto stress, la BCE rischia di tornare difensiva proprio mentre l’economia avrebbe bisogno di respiro per investimenti, domanda e adozione tecnologica.',
        'tags': ['BCE', 'Joachim Nagel', 'inflazione', 'energia', 'tassi'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://wkzo.com/2026/03/26/ecbs-nagel-says-april-rate-hike-an-option/',
        'sourceCount': 1,
        'timestamp': keep_ts('finanza-20260326-ecb-nagel-april-hike-option', '2026-03-26T09:05:00+01:00'),
        'featured': False,
        'opinion': 'Se il petrolio detta il tono della BCE, la tregua monetaria europea è molto meno stabile del previsto.',
        'qualityScore': 93,
        'visual': 'fin'
    },
    {
        'id': 'mercati-20260325-russia-oil-export-capacity-halted',
        'category': 'mercati',
        'subcategory': 'Energia, supply shock e repricing del rischio globale',
        'title': 'Petrolio, il mercato deve assorbire anche il colpo alla capacità export russa',
        'hook': 'Secondo calcoli Reuters, almeno il 40% della capacità russa di esportazione di greggio è ferma tra attacchi ucraini, danni a pipeline e sequestri di tanker. In un mercato già teso dalla guerra con l’Iran, l’offerta perde un altro cuscinetto critico.',
        'body': 'Non è il classico episodio tattico su un singolo terminale: la combinazione di porti colpiti, Druzhba danneggiata e navi bloccate tocca circa 2 milioni di barili al giorno di capacità. In un contesto con il Brent sopra i 100 dollari e lo Stretto di Hormuz ancora sotto pressione, ogni interruzione aggiuntiva rende molto più fragile il quadro energetico globale.\n\nPer i mercati il nodo è che il premio geopolitico non dipende più da un solo fronte. Se Medio Oriente e infrastruttura energetica russa restano simultaneamente sotto stress, il repricing può trasmettersi a inflazione, tassi, valute e asset rischiosi con intensità superiore a quella delle normali fasi di risk-off.',
        'tags': ['Russia', 'petrolio', 'Ucraina', 'supply shock', 'Hormuz'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://economictimes.indiatimes.com/news/international/business/at-least-40-of-russias-oil-export-capacity-halted-reuters-calculations-show/articleshow/129814011.cms?from=mdr',
        'sourceCount': 1,
        'timestamp': keep_ts('mercati-20260325-russia-oil-export-capacity-halted', '2026-03-26T05:20:00+01:00'),
        'featured': True,
        'opinion': 'Quando saltano insieme il cuscinetto iraniano e quello russo, l’energia torna a essere il prezzo politico del mondo.',
        'qualityScore': 94,
        'visual': 'markets'
    },
    {
        'id': 'scienza-20260326-cern-alice-primordial-plasma-small-systems',
        'category': 'scienza',
        'subcategory': 'Fisica delle particelle, plasma primordiale e piccoli sistemi',
        'title': 'ALICE sposta il confine del plasma primordiale anche nelle collisioni tra protoni',
        'hook': 'Il CERN riferisce che una nuova analisi di ALICE trova, anche nei sistemi piccoli, un pattern di flusso anisotropo coerente con la formazione di quark-gluon plasma. Se il segnale regge, la fisica del plasma primordiale non resta più confinata alle collisioni pesanti.',
        'body': 'La novità conta perché avvicina protoni e ioni pesanti dentro la stessa domanda: quanto piccolo può essere un sistema che mostra comportamento collettivo da materia primordiale? L’osservazione di un flusso più forte nei barioni rispetto ai mesoni su un ampio intervallo di momento rafforza proprio l’ipotesi che anche nei sistemi piccoli emerga un mezzo di quark in espansione.\n\nPer la comunità scientifica non è un dettaglio tecnico ma una revisione di cornice. Se segnali tipici del quark-gluon plasma compaiono anche dove per anni si pensava non potessero formarsi, cambiano sia i modelli con cui leggiamo le collisioni al LHC sia il modo in cui ricostruiamo i primi istanti dell’universo.',
        'tags': ['CERN', 'ALICE', 'LHC', 'quark-gluon plasma', 'fisica'],
        'sourceLabel': 'CERN / Nature Communications',
        'sourceUrl': 'https://home.cern/news/news/physics/alice-sees-new-sign-primordial-plasma-proton-collisions',
        'sourceCount': 2,
        'timestamp': keep_ts('scienza-20260326-cern-alice-primordial-plasma-small-systems', '2026-03-26T12:10:00+01:00'),
        'featured': False,
        'opinion': 'Quando un segnale dei sistemi grandi riappare nei protoni, cambia l’ipotesi di partenza più del dettaglio sperimentale.',
        'qualityScore': 89,
        'visual': 'science'
    },
    {
        'id': 'futuro-20260326-nsf-ai-ready-america-coordination-hubs',
        'category': 'futuro',
        'subcategory': 'Adozione diffusa, workforce e infrastruttura istituzionale dell’AI',
        'title': 'Gli Stati Uniti provano a industrializzare l’adozione: l’AI-ready economy passa dai territori',
        'hook': 'La nuova iniziativa NSF “AI-Ready America” punta a creare hub di coordinamento in ogni stato e territorio per diffondere strumenti, competenze e progetti AI oltre la scuola. Il bersaglio non è il laboratorio d’élite, ma la capacità di portare adozione pratica dentro imprese e organizzazioni pubbliche.',
        'body': 'È un passaggio rilevante perché sposta l’attenzione dalla sola frontiera dei modelli all’infrastruttura sociale dell’adozione. Se ogni stato costruisce nodi di coordinamento, competenze e sperimentazione, l’AI diventa meno dipendente da poche coste e più simile a una politica industriale distribuita, con effetti su lavoro, formazione e competitività locale.\n\nPer il resto del mondo il messaggio è chiaro: non basta avere campioni tecnologici. Chi costruisce meccanismi permanenti di diffusione, upskilling e assistenza tecnica può trasformare molto meglio la capacità di ricerca in produttività diffusa. È lì che si giocherà una parte del divario dei prossimi anni.',
        'tags': ['NSF', 'AI Ready America', 'workforce', 'adozione AI', 'policy'],
        'sourceLabel': 'NSF',
        'sourceUrl': 'https://www.nsf.gov/funding/opportunities/techaccess-ai-ready-america',
        'sourceCount': 1,
        'timestamp': '2026-03-26T05:50:00+01:00',
        'featured': False,
        'opinion': 'La prossima gara sull’AI non sarà solo tra modelli, ma tra Paesi che sanno diffonderla davvero.',
        'qualityScore': 88,
        'visual': 'future'
    }
]

stats = {
    'editionUpdatedAt': EDITION_TS,
    'newsGeneratedToday': len(news),
    'sourcesAnalyzed': 10,
    'topicEmerging': [
        'La sovranità AI entra nei deal attraverso founder, mobilità e controllo regolatorio',
        'Gli agenti enterprise si spostano dal copilota al layer operativo delle suite di lavoro',
        'La finestra negoziale su Iran resta aperta ma insufficiente a calmare il premio geopolitico',
        'Energia e logistica continuano a guidare insieme inflazione, tassi e risk pricing',
        'La diffusione dell’AI diventa tema di coordinamento territoriale e workforce, non solo di ricerca',
        'La fisica del plasma primordiale si apre sempre più ai sistemi piccoli'
    ],
    'mostViewed': [
        'Manus-Meta, la Cina trasforma i founder AI in leva strategica',
        'Iran-USA, la risposta fredda di Teheran tiene aperta solo una tregua di carta',
        'Petrolio, il mercato deve assorbire anche il colpo alla capacità export russa'
    ],
    'signals': [
        {'label': 'Edition', 'value': 'Public MVP'},
        {'label': 'Cadence', 'value': CADENCE},
        {'label': 'Mode', 'value': 'Italian briefing'},
        {'label': 'Focus', 'value': 'Source-backed news'}
    ]
}

NEWS_TMP.write_text(json.dumps(news, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
STATS_TMP.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

parsed_news = json.loads(NEWS_TMP.read_text(encoding='utf-8'))
parsed_stats = json.loads(STATS_TMP.read_text(encoding='utf-8'))
if not isinstance(parsed_news, list):
    raise SystemExit('temp news did not parse as list')
if not isinstance(parsed_stats, dict):
    raise SystemExit('temp stats did not parse as object')

subprocess.run(['python3', str(VALIDATOR), str(NEWS_TMP), str(STATS_TMP)], check=True)

os.replace(NEWS_TMP, NEWS)
os.replace(STATS_TMP, STATS)

post_news_sha = sha256(NEWS)
post_stats_sha = sha256(STATS)
post_news_mtime = mtime_ns(NEWS)
post_stats_mtime = mtime_ns(STATS)
post_news_json = json.loads(NEWS.read_text(encoding='utf-8'))
post_stats_json = json.loads(STATS.read_text(encoding='utf-8'))

news_hash_changed = post_news_sha != pre_news_sha
stats_hash_changed = post_stats_sha != pre_stats_sha
news_mtime_changed = post_news_mtime != pre_news_mtime
stats_mtime_changed = post_stats_mtime != pre_stats_mtime

if not (news_hash_changed or news_mtime_changed):
    raise SystemExit('news live file did not change')
if not (stats_hash_changed or stats_mtime_changed):
    raise SystemExit('stats live file did not change')
if post_stats_json.get('editionUpdatedAt') != EDITION_TS:
    raise SystemExit('editionUpdatedAt mismatch after publish')
if pre_edition is not None and post_stats_json.get('editionUpdatedAt') <= pre_edition:
    raise SystemExit('editionUpdatedAt did not advance')
if not any(s.get('label') == 'Cadence' and s.get('value') == CADENCE for s in post_stats_json.get('signals', [])):
    raise SystemExit('cadence does not match edition minute')
if len(post_news_json) != len(news):
    raise SystemExit('published news length mismatch')

print(json.dumps({
    'pre': {
        'news_sha': pre_news_sha,
        'stats_sha': pre_stats_sha,
        'news_mtime_ns': pre_news_mtime,
        'stats_mtime_ns': pre_stats_mtime,
        'editionUpdatedAt': pre_edition,
    },
    'post': {
        'news_sha': post_news_sha,
        'stats_sha': post_stats_sha,
        'news_mtime_ns': post_news_mtime,
        'stats_mtime_ns': post_stats_mtime,
        'editionUpdatedAt': post_stats_json.get('editionUpdatedAt'),
    },
    'changed': {
        'news_hash_changed': news_hash_changed,
        'stats_hash_changed': stats_hash_changed,
        'news_mtime_changed': news_mtime_changed,
        'stats_mtime_changed': stats_mtime_changed,
    }
}, ensure_ascii=False, indent=2))
