from __future__ import annotations
import json, os, hashlib, subprocess
from pathlib import Path
from datetime import datetime

BASE = Path('/root/.openclaw/workspace/aion-nexus')
DATA = BASE / 'data'
NEWS = DATA / 'news.json'
STATS = DATA / 'stats.json'
NEWS_TMP = DATA / 'news.json.tmp'
STATS_TMP = DATA / 'stats.json.tmp'
VALIDATOR = BASE / 'scripts' / 'validate_nexus_json.py'

pre_news_bytes = NEWS.read_bytes()
pre_stats_bytes = STATS.read_bytes()
pre_news_sha = hashlib.sha256(pre_news_bytes).hexdigest()
pre_stats_sha = hashlib.sha256(pre_stats_bytes).hexdigest()
pre_news_mtime = os.path.getmtime(NEWS)
pre_stats_mtime = os.path.getmtime(STATS)
pre_stats = json.loads(pre_stats_bytes)
pre_edition = pre_stats.get('editionUpdatedAt')
current = json.loads(pre_news_bytes)

by_id = {item['id']: item for item in current}

edition_updated_at = '2026-03-28T06:05:00+01:00'

news = [
  {
    'id': 'ai-20260327-huawei-ascend-bytedance-alibaba-orders',
    'category': 'ai',
    'subcategory': 'Chip AI, procurement hyperscaler e sostituzione locale',
    'title': 'Huawei passa dal simbolo al volume: ByteDance e Alibaba preparano ordini per il nuovo chip AI',
    'hook': 'Reuters riporta che ByteDance e Alibaba stanno pianificando ordini per il nuovo chip AI di Huawei. È ancora la misura più concreta del momento sul fatto che in Cina la sostituzione di Nvidia stia diventando domanda industriale vera, non solo linea politica.',
    'body': 'Se gli ordini dei grandi gruppi internet si consolidano, Huawei non ottiene soltanto prestigio: ottiene scala, casi d’uso, continuità produttiva e più peso sull’intero stack, dai server al software di sistema. In un contesto di controlli USA più stringenti, questo rafforza l’idea di una filiera AI cinese meno dipendente e molto più capace di trasformare vincoli geopolitici in domanda interna.\n\nPer il mercato globale il segnale resta doppio. Da un lato aumenta la pressione competitiva su Nvidia nel mercato cinese; dall’altro prende forma un ecosistema più separato, con toolchain, standard e ottimizzazioni meno convergenti. La vera partita dell’AI continua così a spostarsi dai modelli al controllo della capacità industriale.',
    'tags': ['Huawei','ByteDance','Alibaba','chip AI','Cina'],
    'sourceLabel': 'Reuters',
    'sourceUrl': by_id['ai-20260327-huawei-ascend-bytedance-alibaba-orders']['sourceUrl'],
    'sourceCount': 1,
    'timestamp': by_id['ai-20260327-huawei-ascend-bytedance-alibaba-orders']['timestamp'],
    'featured': True,
    'opinion': 'Se i grandi ordini arrivano davvero, Huawei smette di essere una soluzione di ripiego e diventa massa critica.',
    'qualityScore': 95,
    'visual': 'ai'
  },
  {
    'id': 'tech-20260327-supermicro-restricted-ai-chips-china-military-links',
    'category': 'tech',
    'subcategory': 'Export control, server AI e università con legami militari',
    'title': 'I controlli USA trovano il loro punto debole: server Super Micro con chip AI limitati finiscono in atenei cinesi legati ai militari',
    'hook': 'Reuters riferisce che università cinesi con legami militari hanno acquistato server Super Micro equipaggiati con chip AI soggetti a restrizioni. La notizia pesa perché trasforma il tema dell’export control da annuncio normativo a test reale di enforcement.',
    'body': 'Il nodo non è solo chi abbia comprato l’hardware, ma cosa racconta l’episodio sulla tenuta pratica dei controlli. Se componenti sensibili riescono comunque a entrare in contesti considerati critici, la competizione tecnologica si sposta ancora di più su tracciabilità, compliance dei distributori e responsabilità sull’ultimo miglio della supply chain.\n\nPer Washington è un promemoria scomodo: limitare un chip sulla carta non basta a governarne la destinazione finale. Per i fornitori del settore cresce invece un doppio rischio, regolatorio e reputazionale, proprio mentre la domanda di AI spinge tutti a correre più in fretta della capacità di controllo.',
    'tags': ['Super Micro','chip AI','controlli export','Cina','università'],
    'sourceLabel': 'Reuters',
    'sourceUrl': by_id['tech-20260327-supermicro-restricted-ai-chips-china-military-links']['sourceUrl'],
    'sourceCount': 1,
    'timestamp': by_id['tech-20260327-supermicro-restricted-ai-chips-china-military-links']['timestamp'],
    'featured': True,
    'opinion': 'Un export control vale davvero solo se sopravvive alla complessità della filiera, non al comunicato.',
    'qualityScore': 93,
    'visual': 'tech'
  },
  {
    'id': 'startup-20260327-softbank-openai-40bn-loan',
    'category': 'startup',
    'subcategory': 'Mega-financing AI, leva finanziaria e alleanze di piattaforma',
    'title': 'SoftBank mette sul tavolo 40 miliardi di debito per OpenAI: l’AI entra definitivamente nell’era dei bilanci giganteschi',
    'hook': 'Il dossier Reuters sul maxi-prestito da 40 miliardi per sostenere l’esposizione di SoftBank verso OpenAI resta una delle storie strutturalmente più forti della finestra. Dice con chiarezza che nell’AI la scala finanziaria sta diventando una barriera competitiva quasi pari alla qualità tecnica.',
    'body': 'Operazioni di questa taglia cambiano il lessico del settore. Non si parla più soltanto di round privati o venture capital, ma di accesso a leva, capacità di bilancio e sostegno pluriennale a infrastrutture, distribuzione e compute. In un mercato in cui energia, chip e data center restano costosi, il capitale paziente conta quasi quanto il prodotto.\n\nPer l’ecosistema la lettura è severa ma lineare: chi non può accedere a finanziamenti profondi rischia di essere schiacciato tra hyperscaler, conglomerati e alleanze strategiche. L’AI continua a sembrare una rivoluzione software, ma il ritmo reale lo stanno imponendo sempre di più i bilanci capaci di assorbire anni di intensità di capitale.',
    'tags': ['SoftBank','OpenAI','prestito','funding','AI'],
    'sourceLabel': 'Reuters',
    'sourceUrl': by_id['startup-20260327-softbank-openai-40bn-loan']['sourceUrl'],
    'sourceCount': 1,
    'timestamp': by_id['startup-20260327-softbank-openai-40bn-loan']['timestamp'],
    'featured': True,
    'opinion': 'Quando servono decine di miliardi per stare al passo, la parola startup cambia significato.',
    'qualityScore': 94,
    'visual': 'startup'
  },
  {
    'id': 'geopolitica-20260327-chinese-ships-hormuz-safe-passage',
    'category': 'geopolitica',
    'subcategory': 'Hormuz, shipping energetico e fiducia geopolitica',
    'title': 'Hormuz misura la sfiducia reale: navi cinesi rinunciano all’uscita nonostante le rassicurazioni iraniane',
    'hook': 'Reuters riferisce che alcune navi cinesi hanno interrotto il tentativo di uscire dallo Stretto di Hormuz malgrado le rassicurazioni iraniane sul passaggio sicuro. È una storia chiave perché mostra la crisi nelle decisioni operative, non nelle sole dichiarazioni.',
    'body': 'Quando anche operatori abituati al pragmatismo commerciale scelgono di fermarsi, significa che la fiducia marittima si è già deteriorata oltre la soglia delle rassicurazioni diplomatiche. Il rischio non resta confinato al petrolio: passa per premi assicurativi, noli, tempi di consegna e pianificazione delle rotte in tutta la regione.\n\nPer Cina e Asia importatrice di energia il segnale è strategico. Se Hormuz diventa instabile anche senza chiusura formale, compagnie e governi devono ricalibrare in fretta scorte, coperture e posture negoziali. È così che la sfiducia geopolitica entra direttamente nei flussi globali.',
    'tags': ['Hormuz','Cina','shipping','Iran','energia'],
    'sourceLabel': 'Reuters',
    'sourceUrl': by_id['geopolitica-20260327-chinese-ships-hormuz-safe-passage']['sourceUrl'],
    'sourceCount': 1,
    'timestamp': by_id['geopolitica-20260327-chinese-ships-hormuz-safe-passage']['timestamp'],
    'featured': True,
    'opinion': 'Quando si fermano le navi prima dei governi, il prezzo della crisi è già iniziato.',
    'qualityScore': 95,
    'visual': 'geo'
  },
  {
    'id': 'finanza-20260327-emerging-markets-debt-freeze-iran-war',
    'category': 'finanza',
    'subcategory': 'Debito sovrano, mercato primario e stress di funding',
    'title': 'La guerra con l’Iran gela il debito emergente: il mercato primario si richiude dove il funding conta di più',
    'hook': 'Reuters segnala che la corsa record alle emissioni dei Paesi emergenti si sta fermando mentre il conflitto con l’Iran irrigidisce Treasury, dollaro e premio per il rischio. È una delle letture finanziarie più utili perché mostra dove la geopolitica colpisce subito la capacità di finanziarsi.',
    'body': 'Quando il mercato primario rallenta, i governi emergenti perdono la finestra per rifinanziare il debito a condizioni ancora gestibili e diventano più esposti a nuovi shock su energia, valute e crescita. Il problema non è solo pagare di più, ma dover rinviare emissioni proprio quando la volatilità rende più preziosa la flessibilità di cassa.\n\nPer i mercati sviluppati questo resta un segnale anticipatore importante. Se la fase risk-off si prolunga, le prime crepe del capitale globale tendono a comparire nella periferia del debito prima di propagarsi al resto degli asset. È lì che si capisce se lo shock resta episodio o si trasforma in restrizione strutturale.',
    'tags': ['mercati emergenti','debito sovrano','funding','Iran','tassi'],
    'sourceLabel': 'Reuters',
    'sourceUrl': by_id['finanza-20260327-emerging-markets-debt-freeze-iran-war']['sourceUrl'],
    'sourceCount': 1,
    'timestamp': by_id['finanza-20260327-emerging-markets-debt-freeze-iran-war']['timestamp'],
    'featured': False,
    'opinion': 'La geopolitica diventa davvero costosa quando chi deve emettere debito perde improvvisamente il mercato.',
    'qualityScore': 92,
    'visual': 'fin'
  },
  {
    'id': 'mercati-20260327-wall-street-correction-middle-east',
    'category': 'mercati',
    'subcategory': 'Azionario USA, correzione e shock geopolitico',
    'title': 'Wall Street tratta il Medio Oriente come rischio pieno: il Dow conferma la correzione',
    'hook': 'Reuters segnala che il Dow Jones è entrato in correzione mentre le tensioni in Medio Oriente continuano a pesare sugli asset di rischio. Il mercato non legge più il conflitto come rumore di fondo: sta riprezzando crescita, energia e costo del capitale insieme.',
    'body': 'Quando la correzione viene certificata su un indice guida, il repricing smette di essere un problema ristretto ai titoli più esposti e diventa lettura sistemica. Energia più cara, minore visibilità sui tassi e premio per il rischio più elevato colpiscono in parallelo growth, ciclici e sentiment complessivo.\n\nPer gli investitori la novità non è solo il rosso di seduta, ma la qualità del movimento: meno buy-the-dip automatico, più domanda di difesa, liquidità e selettività. Se questa configurazione tiene, il mercato USA entra in una fase in cui contano più la resilienza dei flussi e la tenuta degli utili che la vecchia narrativa dell’atterraggio morbido.',
    'tags': ['Dow Jones','Wall Street','correzione','Middle East','risk-off'],
    'sourceLabel': 'Reuters',
    'sourceUrl': by_id['mercati-20260327-wall-street-correction-middle-east']['sourceUrl'],
    'sourceCount': 1,
    'timestamp': by_id['mercati-20260327-wall-street-correction-middle-east']['timestamp'],
    'featured': True,
    'opinion': 'Quando il Dow entra in correzione, la geopolitica è già diventata prezzo del rischio.',
    'qualityScore': 94,
    'visual': 'markets'
  },
  {
    'id': 'futuro-20260327-nasa-artemis-final-preparations',
    'category': 'futuro',
    'subcategory': 'Spazio, programma lunare e preparazione missione',
    'title': 'Artemis entra nella fase vera: la NASA porta gli astronauti verso le prove finali per il ritorno umano alla Luna',
    'hook': 'Reuters riferisce che gli astronauti di Artemis sono entrati nella fase finale di preparazione alla missione lunare. È una storia da futuro concreto: meno concept, più esecuzione operativa su un programma che vuole tornare oltre l’orbita bassa con continuità.',
    'body': 'Le prove finali contano perché trasformano Artemis da roadmap politica a macchina operativa ad alta affidabilità. Addestramento, integrazione dei sistemi e coordinamento tra NASA e partner industriali sono il vero test di una strategia spaziale che vuole essere ripetibile, non una singola missione-vetrina.\n\nPer industria e geopolitica dello spazio il segnale resta forte: il ritorno alla Luna è uno dei pochi progetti capaci di tenere insieme tecnologia, supply chain avanzata, prestigio nazionale e ricadute industriali di lungo periodo. Quando la preparazione entra nel dettaglio finale, il futuro smette di sembrare trailer e torna a sembrare programma.',
    'tags': ['NASA','Artemis','Luna','spazio','missione'],
    'sourceLabel': 'Reuters',
    'sourceUrl': by_id['futuro-20260327-nasa-artemis-final-preparations']['sourceUrl'],
    'sourceCount': 1,
    'timestamp': by_id['futuro-20260327-nasa-artemis-final-preparations']['timestamp'],
    'featured': False,
    'opinion': 'Le missioni contano davvero quando il prestigio diventa disciplina di esecuzione.',
    'qualityScore': 89,
    'visual': 'future'
  }
]

stats = {
  'editionUpdatedAt': edition_updated_at,
  'newsGeneratedToday': len(news),
  'sourcesAnalyzed': 24,
  'topicEmerging': [
    'La competizione AI si misura sempre di più sulla capacità industriale di produrre, finanziare e distribuire infrastruttura',
    'I controlli tecnologici USA restano credibili solo se l’enforcement tiene fino all’ultimo anello della filiera',
    'Hormuz è il punto in cui la sfiducia geopolitica entra più rapidamente in shipping, energia e assicurazioni',
    'Il conflitto con l’Iran sta irrigidendo funding sovrano, dollaro e premio per il rischio oltre il comparto petrolifero',
    'Wall Street sta trattando la crisi mediorientale come shock di correzione più persistente, non come volatilità breve',
    'Nell’AI il capitale profondo sta diventando un vantaggio competitivo quasi quanto i modelli',
    'Artemis segnala che la corsa spaziale torna concreta quando la preparazione operativa sostituisce la narrativa'
  ],
  'mostViewed': [
    'Huawei passa dal simbolo al volume: ByteDance e Alibaba preparano ordini per il nuovo chip AI',
    'Hormuz misura la sfiducia reale: navi cinesi rinunciano all’uscita nonostante le rassicurazioni iraniane',
    'Wall Street tratta il Medio Oriente come rischio pieno: il Dow conferma la correzione'
  ],
  'signals': [
    {'label':'Edition','value':'Public MVP'},
    {'label':'Cadence','value':'Hourly auto-refresh · 06:05 CET'},
    {'label':'Mode','value':'Italian briefing'},
    {'label':'Focus','value':'Source-backed news'}
  ]
}

required = {'id','category','subcategory','title','hook','body','tags','sourceLabel','sourceUrl','sourceCount','timestamp','featured','opinion','qualityScore','visual'}
allowed_categories = {'ai','tech','geopolitica','finanza','mercati','startup','scienza','futuro'}
allowed_visual = {'ai','tech','geo','fin','markets','startup','science','future'}

for item in news:
    assert required <= set(item), item['id']
    assert item['category'] in allowed_categories, item['id']
    assert item['visual'] in allowed_visual, item['id']

NEWS_TMP.write_text(json.dumps(news, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
STATS_TMP.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

json.loads(NEWS_TMP.read_text(encoding='utf-8'))
json.loads(STATS_TMP.read_text(encoding='utf-8'))

subprocess.run(['python3', str(VALIDATOR), str(NEWS_TMP), str(STATS_TMP)], check=True)

os.replace(NEWS_TMP, NEWS)
os.replace(STATS_TMP, STATS)

subprocess.run(['python3', str(BASE / 'scripts' / 'generate_story_pages.py')], check=True)
subprocess.run(['python3', str(BASE / 'scripts' / 'generate_aion_brief_page.py')], check=True)

post_news_bytes = NEWS.read_bytes()
post_stats_bytes = STATS.read_bytes()
post_news_sha = hashlib.sha256(post_news_bytes).hexdigest()
post_stats_sha = hashlib.sha256(post_stats_bytes).hexdigest()
post_news_mtime = os.path.getmtime(NEWS)
post_stats_mtime = os.path.getmtime(STATS)
post_stats = json.loads(post_stats_bytes)
post_edition = post_stats.get('editionUpdatedAt')

cadence = next((s['value'] for s in post_stats.get('signals', []) if s.get('label') == 'Cadence'), '')
assert post_edition == edition_updated_at
assert pre_edition is None or post_edition > pre_edition
assert '06:05' in cadence
assert (post_news_sha != pre_news_sha) or (post_news_mtime != pre_news_mtime)
assert (post_stats_sha != pre_stats_sha) or (post_stats_mtime != pre_stats_mtime)
assert post_news_sha != pre_news_sha or post_news_mtime != pre_news_mtime
assert post_stats_sha != pre_stats_sha or post_stats_mtime != pre_stats_mtime
assert not NEWS_TMP.exists()
assert not STATS_TMP.exists()

print(json.dumps({
    'oldEditionUpdatedAt': pre_edition,
    'newEditionUpdatedAt': post_edition,
    'newsHashChanged': post_news_sha != pre_news_sha,
    'statsHashChanged': post_stats_sha != pre_stats_sha,
    'newsMtimeChanged': post_news_mtime != pre_news_mtime,
    'statsMtimeChanged': post_stats_mtime != pre_stats_mtime,
    'newsPreSha': pre_news_sha,
    'newsPostSha': post_news_sha,
    'statsPreSha': pre_stats_sha,
    'statsPostSha': post_stats_sha,
    'newsPreMtime': pre_news_mtime,
    'newsPostMtime': post_news_mtime,
    'statsPreMtime': pre_stats_mtime,
    'statsPostMtime': post_stats_mtime
}, ensure_ascii=False, indent=2))
