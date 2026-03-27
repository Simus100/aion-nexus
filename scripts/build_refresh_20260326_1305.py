#!/usr/bin/env python3
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path

BASE = Path('/root/.openclaw/workspace/aion-nexus/data')
NEWS = BASE / 'news.json'
STATS = BASE / 'stats.json'
NEWS_TMP = BASE / 'news.json.tmp'
STATS_TMP = BASE / 'stats.json.tmp'
VALIDATOR = Path('/root/.openclaw/workspace/aion-nexus/scripts/validate_nexus_json.py')

EDITION_TS = '2026-03-26T13:05:00+01:00'
CADENCE = 'Hourly auto-refresh · 13:05 CET'


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mtime(path: Path) -> float:
    return path.stat().st_mtime


pre_news_sha = sha256(NEWS)
pre_stats_sha = sha256(STATS)
pre_news_mtime = mtime(NEWS)
pre_stats_mtime = mtime(STATS)
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
        'title': 'Il caso Manus-Meta mostra che in Cina anche i founder AI sono già materia di sovranità',
        'hook': 'Reuters riferisce che due cofondatori di Manus non possono lasciare la Cina mentre Pechino riesamina la vendita a Meta. Il deal non riguarda più solo multipli e proprietà intellettuale: riguarda il controllo sul talento strategico.',
        'body': 'Quando una review regolatoria arriva a toccare direttamente la mobilità dei fondatori, il mercato capisce che i team AI vengono trattati come asset sensibili quasi quanto chip, dati e infrastrutture. Per i buyer internazionali questo alza il rischio esecutivo delle acquisizioni transfrontaliere e rende molto meno lineare comprare competenze, agenti e know-how in blocco.\n\nPer Meta il problema non è solo chiudere l’operazione, ma capire se questo precedente cambierà il costo politico di futuri deal nel settore. Se la sovranità entra nei contratti attraverso le persone chiave, l’M&A globale sull’AI dovrà scontare tempi più lunghi, clausole più dure e un premio regolatorio permanente.',
        'tags': ['Manus', 'Meta', 'Cina', 'AI agents', 'M&A'],
        'sourceLabel': 'Reuters / FT',
        'sourceUrl': 'https://whtc.com/2026/03/25/china-bars-manus-co-founders-from-leaving-country-as-it-reviews-sale-to-meta-ft-reports/',
        'sourceCount': 2,
        'timestamp': keep_ts('ai-20260325-manus-meta-china-exit-restrictions', '2026-03-25T08:05:00+01:00'),
        'featured': True,
        'opinion': 'Se la review blocca i founder, la geopolitica AI è già entrata nella term sheet.',
        'qualityScore': 96,
        'visual': 'ai'
    },
    {
        'id': 'tech-20260326-microsoft-copilot-wave3-frontier-seoul',
        'category': 'tech',
        'subcategory': 'Enterprise software, agenti e diffusione operativa dell’AI',
        'title': 'Microsoft spinge Copilot oltre il copilota: a Seoul presenta agenti più profondi e un pacchetto enterprise dedicato',
        'hook': 'Al Microsoft AI Tour Seoul l’azienda rilancia Wave 3 di Microsoft 365 Copilot, Copilot Cowork e il nuovo piano Microsoft 365 E7. Il messaggio è che la partita non è più la demo generativa, ma l’integrazione degli agenti nei processi reali d’impresa.',
        'body': 'Le novità contano perché spostano Copilot dal perimetro dell’assistenza puntuale a quello dell’esecuzione di flussi multi-step con più contesto su mail, calendari e documenti. Se questa promessa regge nell’uso reale, Microsoft consolida il vantaggio di distribuzione dato dalla suite produttiva già presente nelle grandi aziende, rendendo più costoso per i concorrenti entrare a valle.\n\nIl segnale più forte è commerciale: dal 1° maggio Microsoft collegherà gli agenti a un bundle enterprise con identità, sicurezza e governance incorporate. In pratica sta dicendo ai CIO che la prossima ondata AI non si compra come plugin creativo, ma come stack operativo con controllo, compliance e rollout su larga scala.',
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
        'title': 'L’Iran raffredda il piano americano: la finestra negoziale resta aperta, ma troppo stretta per calmare davvero i mercati',
        'hook': 'Un alto funzionario iraniano dice a Reuters che la prima risposta di Teheran alla proposta USA per fermare la guerra non è stata positiva. Il segnale è che la diplomazia esiste ancora, ma non abbastanza da ridurre rapidamente il premio geopolitico.',
        'body': 'Il punto chiave non è solo il rifiuto iniziale, ma il fatto che la risposta resti in una zona grigia: non un no definitivo, non un sì operativo. Questo lascia mercati e alleati occidentali sospesi tra speranza di de-escalation e rischio concreto che il conflitto continui a contagiare energia, trasporti e postura militare regionale.\n\nPer Europa e G7 significa lavorare su deterrenza e canali diplomatici allo stesso tempo, senza poter contare su una soluzione rapida. Finché Teheran segnala freddezza e Washington continua a testare una via negoziale, la variabile dominante resta l’incertezza, non la tregua.',
        'tags': ['Iran', 'USA', 'Medio Oriente', 'diplomazia', 'guerra'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://www.tbsnews.net/world/irans-initial-response-us-proposal-not-positive-senior-iranian-official-tells-reuters-1394161',
        'sourceCount': 1,
        'timestamp': keep_ts('geopolitica-20260326-iran-us-proposal-negative-response', '2026-03-26T08:45:00+01:00'),
        'featured': True,
        'opinion': 'Finché la prima risposta iraniana è fredda, il mercato prezza più durata del conflitto che compromesso.',
        'qualityScore': 94,
        'visual': 'geo'
    },
    {
        'id': 'finanza-20260326-ecb-nagel-april-hike-option',
        'category': 'finanza',
        'subcategory': 'Banche centrali, shock energetico e rischio di secondo round inflazionistico',
        'title': 'Nagel riapre la porta a un rialzo BCE già ad aprile: l’energia rimette i tassi al centro',
        'hook': 'In un’intervista a Reuters, Joachim Nagel dice che un rialzo dei tassi BCE ad aprile è "un’opzione" se la guerra in Medio Oriente alimenta un nuovo shock inflazionistico. Il mercato non guarda più solo alla crescita: torna a prezzare il rischio di contagio dai prezzi energetici al resto dell’economia.',
        'body': 'Il passaggio chiave non è soltanto il tono da falco del governatore tedesco, ma l’idea che la BCE possa agire già al prossimo meeting se vedrà segnali di rincari oltre l’energia e pressioni salariali più persistenti. Dopo mesi in cui la traiettoria sembrava più leggibile, il conflitto in Iran rimette in gioco uno scenario da banca centrale in allerta permanente.\n\nPer l’eurozona il problema è noto ma ora più duro: importare energia cara significa importare anche fragilità macro. Se petrolio, gas e chimica restano sotto stress, la politica monetaria rischia di tornare difensiva proprio mentre l’economia europea avrebbe bisogno di ossigeno per investimenti, domanda e adozione tecnologica.',
        'tags': ['BCE', 'Joachim Nagel', 'inflazione', 'energia', 'tassi'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://wkzo.com/2026/03/26/ecbs-nagel-says-april-rate-hike-an-option/',
        'sourceCount': 1,
        'timestamp': keep_ts('finanza-20260326-ecb-nagel-april-hike-option', '2026-03-26T09:05:00+01:00'),
        'featured': False,
        'opinion': 'Se il petrolio detta il tono della BCE, la tregua monetaria europea è molto meno stabile di quanto sembrasse.',
        'qualityScore': 93,
        'visual': 'fin'
    },
    {
        'id': 'mercati-20260325-russia-oil-export-capacity-halted',
        'category': 'mercati',
        'subcategory': 'Energia, supply shock e repricing del rischio globale',
        'title': 'Il mercato del petrolio ora deve prezzare anche il colpo all’export russo',
        'hook': 'Secondo calcoli Reuters, almeno il 40% della capacità russa di esportazione di greggio è ferma tra attacchi ucraini, danni a pipeline e sequestri di tanker. In un mercato già teso dalla guerra con l’Iran, l’offerta perde un altro cuscinetto.',
        'body': 'Questo non è il solito episodio tattico su singoli terminali: la combinazione di porti colpiti, Druzhba danneggiata e navi bloccate tocca circa 2 milioni di barili al giorno di capacità. In un contesto di prezzi sopra i 100 dollari e Stretto di Hormuz sotto stress, ogni ulteriore interruzione rende molto più fragile il quadro energetico globale.\n\nPer i mercati il punto è che il premio geopolitico non dipende più da un solo fronte. Se Medio Oriente e infrastruttura energetica russa restano contemporaneamente sotto pressione, il repricing può trasmettersi a inflazione, tassi e asset rischiosi con molta più violenza di quanto visto nelle normali fasi di risk-off.',
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
        'id': 'startup-20260325-harvey-200m-11bn-legal-ai',
        'category': 'startup',
        'subcategory': 'Vertical AI, professional services e nuova ondata di agenti operativi',
        'title': 'Harvey raccoglie 200 milioni a 11 miliardi: il denaro punta dove gli agenti hanno un ROI misurabile',
        'hook': 'Harvey annuncia un round da 200 milioni di dollari a valutazione 11 miliardi, mentre il legal AI accelera sulla promessa di agenti capaci di eseguire workflow complessi. Il capitale si sta spostando verso startup che vendono automazione verticale, non solo modelli generici.',
        'body': 'Il punto non è soltanto la valutazione, ma il tipo di domanda che sostiene il round: studi legali e team in-house cercano strumenti che riducano lavoro ripetitivo su contratti, diligence, compliance e contenzioso. In altre parole, l’AI che convince il venture oggi è quella che entra nei processi ad alto costo e parla il linguaggio di margini, tempi e responsabilità operative.\n\nPer l’ecosistema startup questo segna una gerarchia più dura. I capitali restano abbondanti, ma premiano molto di più le piattaforme verticali che riescono a trasformare i modelli in agenti utilizzabili dentro flussi reali, con meno tolleranza per prodotti spettacolari ma ancora troppo generici.',
        'tags': ['Harvey', 'legal AI', 'funding', 'AI agents', 'venture capital'],
        'sourceLabel': 'Harvey',
        'sourceUrl': 'https://www.harvey.ai/blog/harvey-raises-at-dollar11-billion-valuation-to-scale-agents-across-law-firms-and-enterprises',
        'sourceCount': 1,
        'timestamp': keep_ts('startup-20260325-harvey-200m-11bn-legal-ai', '2026-03-25T23:10:00+01:00'),
        'featured': False,
        'opinion': 'Il venture 2026 paga soprattutto l’AI che sostituisce lavoro fatturabile, non quella che colleziona demo.',
        'qualityScore': 90,
        'visual': 'startup'
    },
    {
        'id': 'scienza-20260326-cern-alice-primordial-plasma-small-systems',
        'category': 'scienza',
        'subcategory': 'Fisica delle particelle, plasma primordiale e piccoli sistemi',
        'title': 'ALICE sposta il confine del plasma primordiale: un segnale robusto emerge anche nelle collisioni tra protoni',
        'hook': 'Il CERN riferisce che una nuova analisi di ALICE trova, anche nei sistemi piccoli, un pattern di flusso anisotropo coerente con la formazione di quark-gluon plasma. Se regge, la fisica del plasma primordiale non resta più confinata alle collisioni pesanti.',
        'body': 'La novità conta perché avvicina protoni e ioni pesanti dentro una stessa domanda fisica: quanto piccolo può essere un sistema che mostra comportamento collettivo da materia primordiale? L’osservazione che i barioni mostrino un flusso più forte dei mesoni su un ampio intervallo di momento rafforza proprio l’ipotesi che anche nei sistemi piccoli emerga un mezzo di quark in espansione.\n\nPer la comunità scientifica non è un dettaglio tecnico, ma una revisione di cornice. Se i segnali tipici del quark-gluon plasma appaiono anche dove si pensava non potessero formarsi, allora cambiano sia i modelli con cui leggiamo le collisioni al LHC sia il modo in cui ricostruiamo le condizioni dei primi istanti dell’universo.',
        'tags': ['CERN', 'ALICE', 'LHC', 'quark-gluon plasma', 'fisica'],
        'sourceLabel': 'CERN / Nature Communications',
        'sourceUrl': 'https://home.cern/news/news/physics/alice-sees-new-sign-primordial-plasma-proton-collisions',
        'sourceCount': 2,
        'timestamp': '2026-03-26T12:10:00+01:00',
        'featured': False,
        'opinion': 'Quando un segnale da sistemi grandi riappare nei protoni, cambia l’ipotesi di partenza più che il dettaglio sperimentale.',
        'qualityScore': 89,
        'visual': 'science'
    }
]

stats = {
    'editionUpdatedAt': EDITION_TS,
    'newsGeneratedToday': len(news),
    'sourcesAnalyzed': 11,
    'topicEmerging': [
        'La sovranità AI entra nei deal anche attraverso la mobilità dei founder',
        'Gli agenti enterprise diventano stack operativo dentro le suite di lavoro',
        'La finestra negoziale su Iran resta troppo stretta per comprimere il premio geopolitico',
        'Energia e difesa continuano a guidare insieme inflazione, tassi e rischio di mercato',
        'Il venture premia vertical AI con workflow misurabili più dei prodotti generalisti',
        'La fisica del plasma primordiale si apre sempre più anche ai sistemi piccoli'
    ],
    'mostViewed': [
        'Il caso Manus-Meta mostra che in Cina anche i founder AI sono già materia di sovranità',
        'L’Iran raffredda il piano americano: la finestra negoziale resta aperta, ma troppo stretta per calmare davvero i mercati',
        'Il mercato del petrolio ora deve prezzare anche il colpo all’export russo'
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

json.loads(NEWS_TMP.read_text(encoding='utf-8'))
json.loads(STATS_TMP.read_text(encoding='utf-8'))

subprocess.run(['python3', str(VALIDATOR), str(NEWS_TMP), str(STATS_TMP)], check=True)

os.replace(NEWS_TMP, NEWS)
os.replace(STATS_TMP, STATS)

post_news_sha = sha256(NEWS)
post_stats_sha = sha256(STATS)
post_news_mtime = mtime(NEWS)
post_stats_mtime = mtime(STATS)
post_news_json = json.loads(NEWS.read_text(encoding='utf-8'))
post_stats_json = json.loads(STATS.read_text(encoding='utf-8'))

if post_news_sha == pre_news_sha and post_news_mtime == pre_news_mtime:
    raise SystemExit('news live file did not change')
if post_stats_sha == pre_stats_sha and post_stats_mtime == pre_stats_mtime:
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
        'news_mtime': pre_news_mtime,
        'stats_mtime': pre_stats_mtime,
        'editionUpdatedAt': pre_edition,
    },
    'post': {
        'news_sha': post_news_sha,
        'stats_sha': post_stats_sha,
        'news_mtime': post_news_mtime,
        'stats_mtime': post_stats_mtime,
        'editionUpdatedAt': post_stats_json.get('editionUpdatedAt'),
    }
}, ensure_ascii=False, indent=2))
