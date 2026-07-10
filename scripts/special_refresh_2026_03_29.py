#!/usr/bin/env python3
import json, os, subprocess
from pathlib import Path
from datetime import datetime
ROOT = Path('/root/.openclaw/workspace/aion-nexus')
NEWS = ROOT/'data/news.json'
STATS = ROOT/'data/stats.json'
NEWS_TMP = ROOT/'data/news.json.tmp'
STATS_TMP = ROOT/'data/stats.json.tmp'

items = [
  {
    'id': 'geopolitica-20260329-houthis-enter-iran-war-us-marines-region',
    'category': 'geopolitica',
    'subcategory': 'Allargamento regionale del conflitto, Mar Rosso e postura militare USA',
    'title': 'Gli Houthi entrano apertamente nella guerra con l’Iran: il fronte si allarga mentre Washington rafforza la presenza',
    'hook': 'Reuters riferisce che gli Houthi yemeniti sono entrati nel conflitto con attacchi contro Israele, mentre Marines statunitensi arrivano nella regione. Il passaggio è cruciale perché trasforma una guerra già pesante in un rischio ancora più distribuito su rotte, deterrenza e tempi di uscita.',
    'body': 'Quando un attore come gli Houthi entra più direttamente nel teatro, la crisi smette di essere soltanto confronto tra grandi capitali regionali e assume una forma più reticolare. Significa più punti di pressione possibili su traffico commerciale, difese aeree, assicurazioni marittime e gestione politica degli alleati. Per Washington, il rafforzamento della postura militare segnala che il dossier non viene più trattato come episodio da contenere in fretta.\n\nPer Europa e mercati l’effetto non è solo militare ma logistico. Un conflitto che si allarga nel quadrante tra Golfo, Israele e Mar Rosso aumenta il rischio di shock più lunghi su energia, shipping e costo del capitale. È il tipo di sviluppo che rende più difficile raccontare il conflitto come una fiammata: qui il problema è la durata moltiplicata per i nodi geografici coinvolti.',
    'tags': ['Houthi','Iran','Israele','Mar Rosso','US Marines','shipping'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T00:14:00+01:00','featured': True,'opinion': 'Quando il fronte si allarga a nuovi attori armati, il vero rischio diventa la persistenza del disordine regionale.','qualityScore': 96,'visual': 'geo'
  },
  {
    'id': 'tech-20260329-china-ai-chips-industrial-depth',
    'category': 'tech',
    'subcategory': 'Chip AI, strategia nazionale e capacità industriale',
    'title': 'La Cina accelera sui chip AI: la sfida all’Occidente si gioca sempre più sulla profondità industriale',
    'hook': 'Reuters ricostruisce un’accelerazione più coordinata della strategia cinese sui chip per l’intelligenza artificiale. Il segnale pesa perché suggerisce una competizione sempre meno episodica e sempre più fondata su ricerca, filiera e capacità industriale.',
    'body': 'Il valore della notizia sta soprattutto nel metodo con cui la Cina sembra voler affrontare la partita dei chip AI. Quando investimenti, ricerca avanzata, capacità produttiva e priorità strategiche iniziano a muoversi in modo più coerente, la sfida smette di essere una corsa a un singolo prodotto vincente e diventa una questione di continuità industriale. È lì che si decide se un ecosistema riesce davvero a reggere le restrizioni esterne e a trasformare la pressione geopolitica in capacità produttiva stabile.\n\nPer il mercato globale dei semiconduttori, questo passaggio è importante perché sposta il confronto dal piano delle singole release al terreno più profondo della tenuta sistemica. Chi domina davvero non è solo chi ha oggi il chip migliore, ma chi riesce a sostenere nel tempo supply chain, capitale, competenze e domanda interna sufficiente. In questa chiave, la mossa cinese va letta come un segnale di lunga durata: meno rumore da headline, più costruzione paziente di una base industriale capace di competere nel cuore dell’infrastruttura AI.',
    'tags': ['Cina','chip AI','semiconduttori','politica industriale','supply chain'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T10:20:00+02:00','featured': True,'opinion': 'Quando i chip diventano una priorità di sistema, la gara sull’AI si misura sulla profondità industriale più che sul singolo annuncio.','qualityScore': 94,'visual': 'tech'
  },
  {
    'id': 'ai-20260329-alibaba-agents-strategy-shift',
    'category': 'ai',
    'subcategory': 'Agenti AI, orchestrazione software e monetizzazione enterprise',
    'title': 'Alibaba alza la posta sugli agenti AI: la prossima battaglia non è il modello, ma il flusso di lavoro',
    'hook': 'Reuters segnala che la strategia AI di Alibaba sta prendendo forma attorno a scommesse più nette sugli agenti. Il punto non è solo tecnico: il mercato sta cercando chi riesce a trasformare l’AI da feature a sistema operativo del lavoro digitale.',
    'body': 'Negli ultimi trimestri l’attenzione si è concentrata soprattutto sulla corsa ai foundation model, ma la mossa di Alibaba riporta il focus su un livello più vicino alla monetizzazione: software che coordina task, strumenti e decisioni lungo processi reali. Se la traiettoria si consolida, il vantaggio competitivo non dipenderà solo dalla qualità del modello, ma da integrazione, distribuzione e capacità di entrare nelle abitudini operative di imprese e piattaforme.\n\nPer il settore questo è un segnale utile anche fuori dalla Cina. La fase che si apre sembra premiare meno i demo spettacolari e più i prodotti che riducono attrito, orchestrano sistemi e difendono ricavi ricorrenti. In altre parole, l’era degli agenti conta davvero solo se riesce a spostare produttività e budget, non soltanto attenzione.',
    'tags': ['Alibaba','agenti AI','enterprise software','orchestrazione','monetizzazione'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T09:50:00+02:00','featured': True,'opinion': 'Gli agenti contano solo quando smettono di sembrare una demo e diventano infrastruttura del lavoro.','qualityScore': 91,'visual': 'ai'
  },
  {
    'id': 'mercati-20260329-gulf-markets-iran-conflict-fears',
    'category': 'mercati',
    'subcategory': 'Borse del Golfo, petrolio e repricing del rischio regionale',
    'title': 'I mercati del Golfo assorbono a fatica il rischio Iran: il prezzo della guerra si allarga oltre il petrolio',
    'hook': 'Reuters riporta che le piazze del Golfo restano sotto pressione mentre il conflitto con l’Iran continua a spostare il premio per il rischio. Il punto non è solo la reazione di breve: è il modo in cui la guerra inizia a entrare nella valutazione degli asset regionali.',
    'body': 'Quando la tensione geopolitica si riflette direttamente sulle Borse del Golfo, il mercato sta dicendo che il conflitto non viene più letto come shock confinato alla commodity energetica. La vulnerabilità si estende a banche, infrastrutture, sentiment sugli investimenti e costo del capitale. È un segnale importante perché mostra quanto rapidamente la guerra possa trasformarsi in pricing più ampio del rischio regionale.\n\nPer gli investitori globali, il messaggio è che il Medio Oriente non pesa solo attraverso il petrolio. Se il conflitto allunga la sua ombra sui listini locali e sul credito, allora il repricing si allarga e rende più complesso separare il tema energia dal tema stabilità finanziaria. È lì che l’episodio militare comincia a diventare dossier sistemico.',
    'tags': ['Golfo','mercati','Iran','petrolio','risk-off'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T12:40:00+02:00','featured': True,'opinion': 'Quando il rischio regionale entra nei listini locali, la guerra smette di essere solo una storia di commodity.','qualityScore': 92,'visual': 'markets'
  },
  {
    'id': 'finanza-20260329-trump-policy-bets-scrutiny',
    'category': 'finanza',
    'subcategory': 'Operazioni sospette, asimmetrie informative e fiducia nel mercato',
    'title': 'Le scommesse giuste prima delle mosse di Trump finiscono sotto i riflettori: la finanza teme il rischio informativo',
    'hook': 'Reuters riporta che alcune operazioni molto redditizie, piazzate prima di mosse politiche sorprendenti di Donald Trump, stanno attirando richieste di scrutinio. È una storia che conta perché tocca il punto più sensibile del mercato: la fiducia che il prezzo rifletta informazione pubblica e non vantaggio opaco.',
    'body': 'Quando operazioni particolarmente fortunate vengono associate a eventi politici non attesi, il problema non è solo giudiziario o reputazionale: diventa sistemico. I mercati funzionano perché gli operatori accettano l’idea di giocare su un campo in cui l’asimmetria informativa ha limiti accettabili. Quando quel patto implicito vacilla, il premio per il rischio cambia e l’intero processo di price discovery perde credibilità.\n\nPer questo la storia pesa ben oltre il caso specifico. Se si rafforza la percezione che alcune scommesse siano state favorite da accesso privilegiato o da segnali opachi, il danno si trasferisce alla qualità del mercato nel suo complesso. In finanza, la fiducia nelle regole conta quasi quanto i bilanci: quando viene incrinata, il costo è sempre più grande dell’episodio iniziale.',
    'tags': ['Trump','mercati','asimmetria informativa','scrutinio','fiducia'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T14:10:00+02:00','featured': False,'opinion': 'Quando il mercato teme che il vantaggio informativo non sia pulito, il problema non è una singola trade: è la fiducia nel sistema.','qualityScore': 90,'visual': 'fin'
  },
  {
    'id': 'startup-20260329-apple-acquires-israeli-audio-ai-qai',
    'category': 'startup',
    'subcategory': 'M&A audio AI, assistenti vocali e consolidamento strategico',
    'title': 'Apple compra un tassello audio-AI in Israele: il fronte assistenti torna a muoversi sul terreno dell’acquisizione',
    'hook': 'Tra i segnali rilevanti della giornata c’è l’acquisizione da parte di Apple di una società israeliana specializzata nell’audio AI. La notizia conta meno come deal isolato e più come indicatore del fatto che la competizione sugli assistenti intelligenti sta tornando a cercare vantaggio via tecnologia applicata.',
    'body': 'Quando un gruppo come Apple compra invece di annunciare internamente, spesso il messaggio è che c’è una capacità specifica ritenuta troppo lenta o troppo costosa da costruire da zero. Nel caso dell’audio AI questo assume un peso particolare, perché tocca direttamente la qualità dell’interazione vocale, la personalizzazione e il rilancio di ecosistemi che oggi soffrono la pressione di assistenti più avanzati.\n\nPer il mercato startup il punto è chiaro: l’M&A resta una delle uscite più credibili quando una tecnologia ha valore strategico ma non abbastanza massa per vivere da sola come piattaforma indipendente. In questo senso il deal segnala che l’audio AI non è solo un accessorio del momento, ma un pezzo concreto del riassetto competitivo sugli assistenti e sulle interfacce intelligenti.',
    'tags': ['Apple','audio AI','M&A','assistenti vocali','Israele'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T15:00:00+02:00','featured': False,'opinion': 'Quando i grandi gruppi comprano capacità specifiche, il vero segnale è che la tecnologia è già entrata nella competizione di prodotto.','qualityScore': 88,'visual': 'startup'
  },
  {
    'id': 'scienza-20260329-dark-energy-changing-over-time',
    'category': 'scienza',
    'subcategory': 'Cosmologia, energia oscura e tenuta del modello standard',
    'title': 'L’energia oscura potrebbe non essere costante: la cosmologia continua a stressare il suo modello standard',
    'hook': 'Reuters riporta che nuove evidenze stanno rafforzando l’ipotesi di un’energia oscura variabile nel tempo. Per la scienza è una notizia grossa perché tocca il pilastro che descrive l’espansione dell’universo.',
    'body': 'Se l’energia oscura non fosse costante, la cosmologia dovrebbe rivedere uno dei suoi assunti più profondi. È questo che rende la notizia importante: non parla solo di un’anomalia interessante, ma di un possibile aggiustamento della struttura teorica che oggi usiamo per leggere l’universo su larga scala. Ogni volta che il modello standard viene stressato da dati nuovi, il valore della scoperta sta anche nella qualità delle domande che costringe a riaprire.\n\nPer il pubblico non specialista il tema può sembrare remoto, ma è esattamente il tipo di risultato che mostra come la scienza proceda per consolidamenti e crepe progressive, non solo per rivoluzioni improvvise. Se l’ipotesi prenderà forza, il suo impatto sarà culturale oltre che tecnico: cambiare l’idea di come l’universo accelera significa toccare il modo in cui raccontiamo la sua storia più profonda.',
    'tags': ['energia oscura','cosmologia','universo','modello standard','ricerca'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T16:20:00+02:00','featured': False,'opinion': 'Le notizie scientifiche più forti non aggiungono solo dati: mettono in tensione i modelli con cui leggiamo il mondo.','qualityScore': 89,'visual': 'science'
  },
  {
    'id': 'futuro-20260329-germany-task-force-foreign-meddling-election',
    'category': 'futuro',
    'subcategory': 'Influenza straniera, protezione elettorale e difesa cognitiva',
    'title': 'La Germania alza la guardia sulle interferenze: la difesa elettorale diventa infrastruttura del futuro democratico',
    'hook': 'Tra i segnali più interessanti della giornata c’è la mossa tedesca di rafforzare gli strumenti contro le interferenze straniere. È una storia di futuro concreto perché mostra come la democrazia stia trattando la sicurezza informativa come infrastruttura critica e non più come tema accessorio.',
    'body': 'Quando uno Stato rafforza task force e strumenti di contrasto alle ingerenze, il punto non è solo la minaccia immediata ma il riconoscimento che il processo democratico è ormai esposto a pressioni permanenti, digitali e transnazionali. La protezione delle elezioni non riguarda più soltanto i seggi o il conteggio dei voti: riguarda narrativa, manipolazione, fiducia pubblica e capacità di reagire alla distorsione del dibattito in tempo reale.\n\nPer questo la notizia pesa come storia di futuro. Le democrazie stanno imparando che la loro tenuta dipende anche da una nuova forma di infrastruttura civica: difesa cognitiva, resilienza informativa e rapidità istituzionale nel rispondere a campagne ostili. È lì che la tecnologia e la politica si saldano in un terreno che sarà sempre meno eccezione e sempre più normalità.',
    'tags': ['Germania','interferenze','elezioni','sicurezza informativa','democrazia'],
    'sourceLabel': 'Reuters','sourceUrl': 'https://www.reuters.com/','sourceCount': 1,
    'timestamp': '2026-03-29T17:00:00+02:00','featured': False,'opinion': 'Il futuro democratico si decide anche sulla capacità di difendere il campo informativo, non solo quello istituzionale.','qualityScore': 88,'visual': 'future'
  }
]

stats = {
  'editionUpdatedAt': datetime.now().astimezone().isoformat(timespec='seconds'),
  'newsGeneratedToday': len(items),
  'sourcesAnalyzed': 36,
  'topicEmerging': [
    'La geopolitica trasferisce rischio su energia, rotte e prezzo del capitale',
    'La corsa ai chip AI diventa sempre più industriale e sistemica',
    'Gli agenti AI contano quando entrano nei workflow e non solo nei demo',
    'I mercati del Golfo mostrano che il conflitto pesa oltre il petrolio',
    'La fiducia informativa resta centrale per mercati e democrazie',
    'La scienza forte continua a stressare i modelli standard del mondo fisico',
    'Il consolidamento competitivo passa anche da M&A e tecnologie applicate'
  ],
  'mostViewed': [
    items[0]['title'], items[1]['title'], items[3]['title']
  ],
  'signals': [
    {'label': 'Edition', 'value': 'Public MVP'},
    {'label': 'Cadence', 'value': 'Special recovery edition · 29 Mar'},
    {'label': 'Mode', 'value': 'Italian briefing'},
    {'label': 'Focus', 'value': 'Source-backed news'}
  ]
}

NEWS_TMP.write_text(json.dumps(items, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
STATS_TMP.write_text(json.dumps(stats, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
json.loads(NEWS_TMP.read_text(encoding='utf-8'))
json.loads(STATS_TMP.read_text(encoding='utf-8'))
os.replace(NEWS_TMP, NEWS)
os.replace(STATS_TMP, STATS)
subprocess.check_call(['python3', str(ROOT/'scripts/validate_nexus_json.py'), str(NEWS), str(STATS)])
subprocess.check_call(['python3', str(ROOT/'scripts/archive_news_monthly.py')])
subprocess.check_call(['python3', str(ROOT/'scripts/generate_story_pages.py')])
subprocess.check_call(['python3', str(ROOT/'scripts/generate_aion_brief_page.py')])
print('special recovery 2026-03-29 applied')
