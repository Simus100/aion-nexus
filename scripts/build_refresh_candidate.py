#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path('/root/.openclaw/workspace/aion-nexus')
LIVE_NEWS = ROOT / 'data' / 'news.json'
NEWS_TMP = ROOT / 'data' / 'news.json.tmp'
STATS_TMP = ROOT / 'data' / 'stats.json.tmp'

current = json.loads(LIVE_NEWS.read_text(encoding='utf-8'))
current_by_id = {item['id']: item for item in current}

def ts(item_id: str, fallback: str) -> str:
    return current_by_id.get(item_id, {}).get('timestamp', fallback)

news = [
    {
        'id': 'ai-20260329-alibaba-agents-strategy-shift',
        'category': 'ai',
        'subcategory': 'Agenti AI, orchestrazione software e monetizzazione enterprise',
        'title': 'Alibaba alza la posta sugli agenti AI: la prossima battaglia non è il modello, ma il flusso di lavoro',
        'hook': 'Reuters segnala che la strategia AI di Alibaba sta prendendo forma attorno a scommesse più nette sugli agenti. Il punto non è solo tecnico: il mercato sta cercando chi riesce a trasformare l’AI da feature a sistema operativo del lavoro digitale.',
        'body': 'Negli ultimi trimestri l’attenzione si è concentrata soprattutto sulla corsa ai foundation model, ma la mossa di Alibaba riporta il focus su un livello più vicino alla monetizzazione: software che coordina task, strumenti e decisioni lungo processi reali. Se la traiettoria si consolida, il vantaggio competitivo non dipenderà solo dalla qualità del modello, ma da integrazione, distribuzione e capacità di entrare nelle abitudini operative di imprese e piattaforme.\n\nPer il settore questo è un segnale utile anche fuori dalla Cina. La fase che si apre sembra premiare meno i demo spettacolari e più i prodotti che riducono attrito, orchestrano sistemi e difendono ricavi ricorrenti. In altre parole, l’era degli agenti conta davvero solo se riesce a spostare produttività e budget, non soltanto attenzione.',
        'tags': ['Alibaba', 'agenti AI', 'enterprise software', 'orchestrazione', 'monetizzazione'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMisgFBVV95cUxOOEl1RjY5TXpZZ3FXWEl3TFJqb1pFUTVDXzNtVzJOUTlDclZEdURYZWRqazVyRVJURkxiMUxYcnFObkFhRE5rZDNJN0VMWER1S2FsM2NqWEZlb2tzSTZzaTNyWEpzSmltVTR1RDJHMTRaTWhVNTJMX3JZTHNHRnNqX0l4dFBhY1VfMDc4TGRJZG9KTzlNV0VvakJSeWFnRzBncnU4Qmlnckl0UDJncE1LR2NR?oc=5',
        'sourceCount': 1,
        'timestamp': '2026-03-18T08:00:00+01:00',
        'featured': True,
        'opinion': 'Gli agenti contano solo quando smettono di sembrare una demo e diventano infrastruttura del lavoro.',
        'qualityScore': 91,
        'visual': 'ai',
    },
    {
        'id': 'tech-20260327-huawei-ai-chip-bytedance-alibaba-orders',
        'category': 'tech',
        'subcategory': 'Semiconduttori AI, catene cinesi di approvvigionamento e concorrenza a Nvidia',
        'title': 'Il nuovo chip AI di Huawei convince ByteDance e Alibaba: la Cina passa dagli annunci agli ordini',
        'hook': 'Reuters riferisce che il nuovo chip AI di Huawei sta convincendo ByteDance e Alibaba, entrambe orientate a ordinare. Il segnale è industriale prima ancora che geopolitico: la Cina sta costruendo domanda domestica vera per alternative a Nvidia.',
        'body': 'Quando due gruppi di questa scala si muovono verso ordini concreti, il tema esce dalla retorica dell’autosufficienza e diventa test di capacità produttiva. Per Huawei conta meno il confronto astratto sulle performance assolute e molto di più la possibilità di inserirsi nel flusso reale di training e inference dei grandi campioni digitali cinesi. È lì che si misura se un ecosistema domestico può reggere davvero.\n\nPer il mercato globale dei semiconduttori, la implicazione è chiara: anche con Nvidia ancora dominante, la presenza di una seconda catena di approvvigionamento abbastanza credibile può modificare scelte di procurement, roadmap software e posture strategiche. Gli annunci contano, ma gli ordini contano molto di più.',
        'tags': ['Huawei', 'AI chip', 'ByteDance', 'Alibaba', 'Cina', 'semiconduttori'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMixAFBVV95cUxNNUV5d0I0b2ZxMDFnMXZRV0NxZzdhWFR1UkV3bmJzN1E4c1UyS0Yya3ZNSE1TUnhENmo0ck0tcE5pX3hKV0VBeXRPd29mTmQ2cEZzS0lrZlU0aFEwenBRR0xwMUpac2tfOEsxTEM4dm8xbWt3R0hseUtlUXp2S2ZiOVRSOWZYbW4wVmxjekVoYmV1MWRqZkQwTkx6cTVsN3oxak9MYlRJbHF0TG1sckY4a2hZQllGOThUM2JxRkVwcUVvM0Na?oc=5',
        'sourceCount': 1,
        'timestamp': ts('tech-20260327-huawei-ai-chip-bytedance-alibaba-orders', '2026-03-28T07:53:00+01:00'),
        'featured': True,
        'opinion': 'Quando arrivano gli ordini, la sovranità tecnologica smette di essere slogan e comincia a pesare nei bilanci.',
        'qualityScore': 94,
        'visual': 'tech',
    },
    {
        'id': 'geopolitica-20260329-houthis-enter-iran-war-us-marines-region',
        'category': 'geopolitica',
        'subcategory': 'Allargamento regionale del conflitto, Mar Rosso e postura militare USA',
        'title': 'Gli Houthi entrano apertamente nella guerra con l’Iran: il fronte si allarga mentre Washington rafforza la presenza',
        'hook': 'Reuters riferisce che gli Houthi yemeniti sono entrati nel conflitto con attacchi contro Israele, mentre Marines statunitensi arrivano nella regione. Il passaggio è cruciale perché trasforma una guerra già pesante in un rischio ancora più distribuito su rotte, deterrenza e tempi di uscita.',
        'body': 'Quando un attore come gli Houthi entra più direttamente nel teatro, la crisi smette di essere soltanto confronto tra grandi capitali regionali e assume una forma più reticolare. Significa più punti di pressione possibili su traffico commerciale, difese aeree, assicurazioni marittime e gestione politica degli alleati. Per Washington, il rafforzamento della postura militare segnala che il dossier non viene più trattato come episodio da contenere in fretta.\n\nPer Europa e mercati l’effetto non è solo militare ma logistico. Un conflitto che si allarga nel quadrante tra Golfo, Israele e Mar Rosso aumenta il rischio di shock più lunghi su energia, shipping e costo del capitale. È il tipo di sviluppo che rende più difficile raccontare il conflitto come una fiammata: qui il problema è la durata moltiplicata per i nodi geografici coinvolti.',
        'tags': ['Houthi', 'Iran', 'Israele', 'Mar Rosso', 'US Marines', 'shipping'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMi0AFBVV95cUxNbGZJMUdyVUtHd0VTaE5QTnhITmJGNE5EMDdwMVZsV2h5UFdDenF6bGpMdVBPdUN0MkZMM1RwOThuVTgxV1dLY0Zsbmdyck5oUUZYd3JSVExjNy1lR0dMZE5KVTdBTjJXeVhWS0J1RlVBOGlReTdpUmJlTThLaEdmVld5S2JYOHB1eTkxSEU0aVNneWlBaVg5RkNFUlprR1I3em41bWtDdXFWUDJZV3czX1hZSktrRDhMWHE5OW03N0pWYUtSX0sxblZPM0lvakZS?oc=5',
        'sourceCount': 1,
        'timestamp': '2026-03-29T00:14:00+01:00',
        'featured': True,
        'opinion': 'Quando il fronte si allarga a nuovi attori armati, il vero rischio diventa la persistenza del disordine regionale.',
        'qualityScore': 96,
        'visual': 'geo',
    },
    {
        'id': 'finanza-20260328-india-central-bank-rupee-curbs-unwinding',
        'category': 'finanza',
        'subcategory': 'Valute emergenti, arbitraggio e difesa della stabilità finanziaria',
        'title': 'La banca centrale indiana stringe sulla rupia: le nuove regole forzano il disinnesco di scommesse speculative',
        'hook': 'Reuters segnala che le misure della banca centrale indiana sul mercato della rupia stanno costringendo gli operatori a chiudere posizioni di arbitraggio. Il messaggio è netto: quando la pressione esterna cresce, la difesa della valuta diventa un tema di stabilità sistemica, non di fine tuning.',
        'body': 'La storia conta perché mostra quanto rapidamente uno shock esterno possa trasferirsi dai prezzi dell’energia e dal risk-off globale alla microstruttura dei mercati. Se le autorità arrivano a intervenire in modo da forzare l’unwinding delle scommesse, significa che il problema non è soltanto il livello del cambio, ma la dinamica con cui si accumulano vulnerabilità nel sistema. La rupia diventa così un termometro della fragilità dei grandi importatori emergenti.\n\nPer gli investitori internazionali, il caso India è un avvertimento più ampio. In una fase di petrolio alto e geopolitica instabile, i Paesi con forti necessità di import energetico possono vedere stress combinati su valuta, obbligazionario e flussi. È lì che il costo del capitale risale e che le allocazioni iniziano a cambiare davvero.',
        'tags': ['India', 'rupia', 'banca centrale', 'arbitraggio', 'mercati emergenti'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMivgFBVV95cUxObFU4OVdzcTFFTEktcGhuTEdJckpfYTExcGZaQ1ExanVPT3prMTZRN29wU1N4cTVYcE8xSktZLVowakswWGQ5OENjcm10XzRsa3NKT055UF9QNUMwN1FIbk8yYUFyTm9ESEtBMHFESnlRWkQ2Z0t0SGxmdDBraC1vT1hOelFNMmtDT2FmcV9waHFPdFc5UG96UDJGVk9DbDVGdzdDa21YdFNPVWRfTnVVczdMNzhmQkZsYUFaeHlR?oc=5',
        'sourceCount': 1,
        'timestamp': '2026-03-28T14:03:43+01:00',
        'featured': True,
        'opinion': 'Quando una banca centrale forza l’unwinding, il mercato sta già dicendo che la tensione non è cosmetica.',
        'qualityScore': 92,
        'visual': 'fin',
    },
    {
        'id': 'mercati-20260327-dow-correction-middle-east-tensions',
        'category': 'mercati',
        'subcategory': 'Azionario USA, allargamento della correzione e repricing del rischio geopolitico',
        'title': 'Anche il Dow entra in correzione: il risk-off da Medio Oriente non è più confinato al tech',
        'hook': 'Reuters riferisce che anche il Dow Jones è entrato in territorio di correzione mentre le tensioni in Medio Oriente continuano a trascinare il sentiment. Il messaggio per il mercato è chiaro: il repricing del rischio si sta allargando oltre il Nasdaq e oltre le sole megacap tecnologiche.',
        'body': 'Quando corregge anche il listino più esposto all’economia reale e ai grandi industriali, Wall Street sta dicendo che il problema non è più una semplice compressione dei multipli growth. Petrolio più alto, minore visibilità macro e premio geopolitico più persistente cominciano a toccare l’intero spettro del rischio, dalle cicliche ai finanziari. È il passaggio da una correzione di stile a una correzione di ampiezza.\n\nQuesto cambia anche la lettura tattica. Se la debolezza si estende agli indici più larghi, gli investitori non stanno solo prendendo profitto sui vincitori del rally AI: stanno rivalutando il contesto complessivo di crescita, inflazione e costo del capitale. È molto più difficile chiamarlo rumore quando il sell-off smette di avere un solo bersaglio.',
        'tags': ['Dow Jones', 'Wall Street', 'correzione', 'Middle East', 'risk-off', 'petrolio'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMipAFBVV95cUxPZ0FmaG9XaW5NdkJrcGtlb2REejNqQjllakI0VlJUeTBaMmVUZHRSWXRFY3NfV1RSV2xvS0g1NXZNZTJESXNxZEVzYk11eEFZRDUwWXRIY1NJVGdJX1dHWjdEZVJQVW8teEU2MmduM1laQTItYTgzdGduT1pFRDhDeUhDWlJGNzFhYndSaHl3R3MzOXBXR1ZiWmVDQ21UOEI0OHZuUQ?oc=5',
        'sourceCount': 1,
        'timestamp': ts('mercati-20260327-dow-correction-middle-east-tensions', '2026-03-27T21:52:58+01:00'),
        'featured': True,
        'opinion': 'Quando corregge anche il Dow, la geopolitica smette di colpire un settore e comincia a ridisegnare il mercato intero.',
        'qualityScore': 94,
        'visual': 'markets',
    },
    {
        'id': 'startup-20260326-rebellions-korea-ai-chip-investment',
        'category': 'startup',
        'subcategory': 'AI chip startup, politica industriale e capitale pubblico strategico',
        'title': 'Seoul mette 166 milioni su Rebellions: la corsa ai chip AI entra nella politica industriale asiatica',
        'hook': 'Reuters riferisce che la Corea del Sud investirà 166 milioni di dollari nella startup di chip AI Rebellions. Non è solo un round: è un segnale che i governi asiatici vogliono coltivare campioni domestici nei semiconduttori per non lasciare tutta la catena del valore a Stati Uniti e Cina.',
        'body': 'Quando il capitale pubblico entra con questa scala in una startup di chip, il messaggio supera il venture tradizionale. Rebellions viene trattata come asset industriale da far crescere dentro una strategia nazionale che tiene insieme sovranità tecnologica, manifattura avanzata e posizionamento nelle infrastrutture AI. Per Seoul conta costruire una filiera che possa reggere sia sul lato dei data center sia su quello delle applicazioni enterprise ed edge.\n\nPer l’ecosistema startup è una notizia più pesante di quanto sembri. In un mercato in cui il costo di competere sui semiconduttori è enorme, sopravvive chi riesce ad agganciarsi a clienti strategici, fabs, supporto statale e domanda locale credibile. La corsa ai chip AI non è più solo una storia di performance: è sempre più politica industriale con nomi propri.',
        'tags': ['Rebellions', 'Corea del Sud', 'AI chip', 'politica industriale', 'startup', 'semiconduttori'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMisgFBVV95cUxNX1UwU2JaM3BaZVlpNjU4ZmNjcnNMSEdydTY3NDA2T1ZvODl3YVI4ZEtidzNBQVVEXzBmTTYzd2hkMldlUlhQVU1tc1pRRDJIcFlMbnU3elFoTEpfaUNnb210ckdONnFDRFdZNlVQV1B2NzFOU2tyNlhZaXhlTGI0YkxEUTYwazBSdEVaLUw2aDVWWkRQWlFMSlh1TGRiWGxhRlFQb3ZxamljcWo1SUlxNXlR?oc=5',
        'sourceCount': 1,
        'timestamp': ts('startup-20260326-rebellions-korea-ai-chip-investment', '2026-03-26T10:01:43+01:00'),
        'featured': False,
        'opinion': 'Quando lo Stato finanzia chip startup, il venture diventa geostrategia applicata.',
        'qualityScore': 90,
        'visual': 'startup',
    },
    {
        'id': 'futuro-20260328-ai-deepfakes-midterm-campaigns',
        'category': 'futuro',
        'subcategory': 'Disinformazione sintetica, campagne elettorali e fiducia pubblica',
        'title': 'I deepfake AI sfumano il confine del reale nella campagna di midterm USA',
        'hook': 'Reuters segnala che i deepfake stanno rendendo sempre più poroso il confine tra contenuto autentico e contenuto sintetico nella campagna americana del 2026. È una storia di futuro molto presente: la tecnologia è già dentro il processo democratico.',
        'body': 'La questione non è solo quanti falsi circolano, ma quanto rapidamente abbassano il costo del dubbio. Quando ogni video, audio o frammento visivo può essere contestato o imitato con strumenti sempre più accessibili, la verifica non riesce a scalare allo stesso ritmo della manipolazione. In politica questo produce un doppio effetto tossico: più spazio per l’inganno e più facilità nel liquidare come falso anche il materiale autentico.\n\nPer questo la storia pesa oltre la cronaca elettorale statunitense. I deepfake stanno diventando un problema infrastrutturale dell’informazione pubblica: piattaforme, media, staff politici e cittadini vengono costretti a spendere più energia per distinguere il vero dal plausibile. È il tipo di slittamento che cambia le regole del dibattito prima ancora delle norme.',
        'tags': ['deepfake', 'AI', 'elezioni USA', 'disinformazione', 'media'],
        'sourceLabel': 'Reuters',
        'sourceUrl': 'https://news.google.com/rss/articles/CBMirwFBVV95cUxNT2hiN2thZG9SM1NGU3FoeVRxTlFnQUdYb0tkUXM4WU1sRk1xbklrNGNzT1ZQbUw5bDdZeEhEMGl5bUNUenJVMXBOUWRORkw4SzR0MlNwanc0SEV3UnBXWEx3cXZIMjNpeUN0UVhZR1VWOGhmZDFCZE41U2RCaHoyQmhMNkkxS3FzYXJaQ2JzNUlWRENsMk9kZ3l3VE1IS0ZIMG5uNUM1WThOX0xhd25Z?oc=5',
        'sourceCount': 1,
        'timestamp': ts('futuro-20260328-ai-deepfakes-midterm-campaigns', '2026-03-28T14:32:08+01:00'),
        'featured': False,
        'opinion': 'Il punto non è più se i deepfake arrivano nella politica: è che ci sono già, e abbassano il costo della sfiducia.',
        'qualityScore': 90,
        'visual': 'future',
    },
]

stats = {
    'editionUpdatedAt': '2026-03-29T06:05:00+02:00',
    'newsGeneratedToday': len(news),
    'sourcesAnalyzed': 23,
    'topicEmerging': [
        'Gli agenti AI stanno diventando un test di integrazione e monetizzazione, non solo di modello',
        'La Cina prova a trasformare l’alternativa a Nvidia in ordini industriali reali',
        'L’allargamento del conflitto in Medio Oriente aumenta il rischio su shipping ed energia',
        'Le valute emergenti restano il punto in cui la geopolitica si scarica più rapidamente',
        'La correzione di Wall Street si allarga oltre il tech e rafforza il repricing del rischio',
        'La politica industriale asiatica entra più direttamente nel venture dei chip AI',
        'I deepfake stanno trasformando la fiducia pubblica in un problema infrastrutturale'
    ],
    'mostViewed': [
        'Gli Houthi entrano apertamente nella guerra con l’Iran: il fronte si allarga mentre Washington rafforza la presenza',
        'Il nuovo chip AI di Huawei convince ByteDance e Alibaba: la Cina passa dagli annunci agli ordini',
        'Anche il Dow entra in correzione: il risk-off da Medio Oriente non è più confinato al tech'
    ],
    'signals': [
        {'label': 'Edition', 'value': 'Public MVP'},
        {'label': 'Cadence', 'value': 'Hourly auto-refresh · 06:05 CEST'},
        {'label': 'Mode', 'value': 'Italian briefing'},
        {'label': 'Focus', 'value': 'Source-backed news'}
    ]
}

NEWS_TMP.write_text(json.dumps(news, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
STATS_TMP.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('wrote temp candidates')
