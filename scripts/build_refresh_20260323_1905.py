import json
import hashlib
import os
from pathlib import Path
from datetime import datetime

BASE = Path('/root/.openclaw/workspace/aion-nexus/data')
NEWS = BASE / 'news.json'
STATS = BASE / 'stats.json'
NEWS_TMP = BASE / 'news.json.tmp'
STATS_TMP = BASE / 'stats.json.tmp'
VALIDATOR = Path('/root/.openclaw/workspace/aion-nexus/scripts/validate_nexus_json.py')

PRE_NEWS_SHA = 'beb4a736c81a34d33f3d61026ed24ab053d5a359d4be5c11564624472d75e826'
PRE_STATS_SHA = 'a5f280343be5e9a19f457e5fa878ea8e9b509470433305065a2c186c780a3913'
PRE_NEWS_MTIME = 1774285683.3608482
PRE_STATS_MTIME = 1774285683.3608482
PRE_EDITION = '2026-03-23T18:05:00+01:00'

EDITION_TS = '2026-03-23T19:05:00+01:00'
CADENCE = 'Hourly auto-refresh · 19:05 CET'

current_news = json.loads(NEWS.read_text(encoding='utf-8'))
current_by_id = {item['id']: item for item in current_news}


def keep_ts(item_id: str, default: str) -> str:
    return current_by_id.get(item_id, {}).get('timestamp', default)

news = [
    {
        'id': 'geopolitica-20260322-hormuz-ultimatum-shipping-pressure',
        'category': 'geopolitica',
        'subcategory': 'Hormuz, libertà di navigazione e risposta multilaterale',
        'title': 'Hormuz diventa un test di governance globale: l’IMO chiede un corridoio operativo per il traffico civile',
        'hook': 'La notizia non è solo la tensione nello stretto, ma il salto istituzionale: l’agenzia marittima ONU parla ormai di quadro urgente e coordinato per mettere in sicurezza equipaggi e navi commerciali.',
        'body': 'Nel resoconto della sessione straordinaria del 18-19 marzo, il Consiglio dell’IMO condanna gli attacchi alle navi mercantili, richiama il rispetto delle libertà di navigazione e sollecita una risposta internazionale coordinata per proteggere la navigazione civile nello Stretto di Hormuz. Il testo lega la crisi non solo ai rischi militari, ma anche alla continuità operativa dello shipping, ai rifornimenti essenziali per le navi bloccate e ai pericoli aggiuntivi generati da jamming e spoofing dei sistemi GNSS.\n\nIl punto editoriale è che Hormuz sta uscendo dalla categoria delle crisi regionali per entrare in quella delle infrastrutture strategiche globali. Quando l’organismo di riferimento del commercio marittimo parla di safe maritime framework urgente, il mercato deve leggere il problema come sistemico: logistica, energia, assicurazioni e credibilità della libertà di navigazione sono ormai nello stesso dossier.',
        'tags': ['Iran', 'Hormuz', 'IMO', 'shipping', 'sicurezza marittima'],
        'sourceLabel': 'IMO / sviluppi internazionali',
        'sourceUrl': 'https://www.imo.org/en/mediacentre/pressbriefings/pages/imo-calls-for-safe-passage-framework-in-strait-of-hormuz.aspx',
        'sourceCount': 2,
        'timestamp': keep_ts('geopolitica-20260322-hormuz-ultimatum-shipping-pressure', '2026-03-22T07:05:00+00:00'),
        'featured': True,
        'opinion': 'Quando la libertà di navigazione richiede un framework umanitario e operativo, la crisi è già oltre la dimensione locale.',
        'qualityScore': 96,
        'visual': 'geo'
    },
    {
        'id': 'mercati-20260322-oil-shipping-insurance-hormuz',
        'category': 'mercati',
        'subcategory': 'petrolio, war-risk e costo della catena fisica',
        'title': 'Il premio di rischio non è solo sul Brent: Hormuz rialza assicurazioni, noli e costo del capitale operativo',
        'hook': 'Il prezzo del greggio resta il termometro più visibile, ma il mercato sta cominciando a prezzare soprattutto l’inaffidabilità della rotta e la frizione sulla logistica reale.',
        'body': 'Il richiamo dell’IMO a un safe-passage framework conferma che il dossier Hormuz non pesa soltanto sui future energetici. Quando una via marittima critica richiede protezione straordinaria, salgono i premi war-risk, si irrigidiscono i noli, aumenta il capitale circolante immobilizzato e diventa meno lineare la programmazione dei flussi commerciali anche per chi non compra direttamente petrolio.\n\nPer i mercati il rischio più persistente non è necessariamente il picco del barile, ma l’erosione di affidabilità della catena fisica. Se il traffico resta esposto a incidenti, ritardi e costi assicurativi più alti, la normalizzazione del greggio non basterà da sola a cancellare il premio infrastrutturale che oggi si sta formando.',
        'tags': ['petrolio', 'shipping', 'assicurazioni', 'noli', 'mercati'],
        'sourceLabel': 'IMO / lettura di mercato',
        'sourceUrl': 'https://www.imo.org/en/mediacentre/pressbriefings/pages/imo-calls-for-safe-passage-framework-in-strait-of-hormuz.aspx',
        'sourceCount': 2,
        'timestamp': keep_ts('mercati-20260322-oil-shipping-insurance-hormuz', '2026-03-22T07:05:00+00:00'),
        'featured': True,
        'opinion': 'I mercati assorbono uno spike del petrolio più facilmente di una rotta strategica che smette di essere affidabile.',
        'qualityScore': 94,
        'visual': 'markets'
    },
    {
        'id': 'finanza-20260321-ecb-inflation-risk-iran-energy',
        'category': 'finanza',
        'subcategory': 'BCE, shock energetico e margine sui tassi',
        'title': 'La BCE difende l’opzionalità: con guerra ed energia nel quadro, Francoforte evita promesse premature sui tassi',
        'hook': 'Luis de Guindos lega apertamente il conflitto in Medio Oriente a crescita e inflazione dell’area euro. Il messaggio al mercato è semplice: oggi la flessibilità vale quasi quanto il livello dei tassi.',
        'body': 'Nell’intervista pubblicata il 23 marzo, il vicepresidente della BCE Luis de Guindos spiega che la guerra in Medio Oriente avrà un forte impatto sia sulla crescita sia sull’inflazione dell’area euro. La banca centrale ribadisce quindi un approccio data-dependent: osservare headline e core inflation, aspettative, prezzi dell’energia, fertilizzanti e alimentari, senza pre-impegnarsi su una traiettoria predeterminata dei tassi nelle prossime riunioni.\n\nLa sostanza è che Francoforte vuole preservare margine di manovra mentre lo shock esterno resta mobile. Se il rischio sono i second-round effects, la credibilità non passa da una promessa rapida di rialzo o taglio, ma dalla capacità di restare pronta a intervenire senza irrigidire troppo presto la guidance.',
        'tags': ['BCE', 'inflazione', 'energia', 'tassi', 'Europa'],
        'sourceLabel': 'ECB',
        'sourceUrl': 'https://www.ecb.europa.eu/press/inter/date/2026/html/ecb.in260323~b893c61107.en.html',
        'sourceCount': 1,
        'timestamp': keep_ts('finanza-20260321-ecb-inflation-risk-iran-energy', '2026-03-21T15:05:00+01:00'),
        'featured': True,
        'opinion': 'Nel rumore geopolitico, la banca centrale più credibile è quella che non si lascia inchiodare a uno script troppo rigido.',
        'qualityScore': 93,
        'visual': 'fin'
    },
    {
        'id': 'ai-20260321-openai-chatgpt-ads-us-rollout',
        'category': 'ai',
        'subcategory': 'monetizzazione, accesso e fiducia nell’AI consumer',
        'title': 'OpenAI porta ChatGPT Go su scala più ampia e prepara i test advertising: la monetizzazione entra senza toccare le risposte',
        'hook': 'La mossa conta perché prova a finanziare l’AI consumer di massa senza confondere utilità, privacy e promozione. È uno stress test sul modello economico, non solo sul prodotto.',
        'body': 'OpenAI ha annunciato l’estensione di ChatGPT Go agli Stati Uniti e più in generale ai mercati in cui ChatGPT è disponibile, aggiungendo più messaggi, immagini, upload di file e memoria a un prezzo contenuto. Nelle prossime settimane partiranno inoltre test pubblicitari negli Stati Uniti per i tier Free e Go, con una linea dichiarata netta: annunci separati e chiaramente etichettati, senza influenza sulle risposte e senza vendita delle conversazioni agli inserzionisti.\n\nQuesta storia resta centrale perché fotografa il passaggio di fase dell’AI consumer. Dopo la corsa alla qualità del modello arriva la domanda più scomoda: come si finanzia l’accesso di massa senza erodere la fiducia? Da qui in avanti la competizione non sarà solo sulla potenza, ma sulla tenuta del patto economico con gli utenti.',
        'tags': ['OpenAI', 'ChatGPT', 'advertising', 'ricavi', 'AI consumer'],
        'sourceLabel': 'OpenAI',
        'sourceUrl': 'https://openai.com/index/our-approach-to-advertising-and-expanding-access/',
        'sourceCount': 1,
        'timestamp': keep_ts('ai-20260321-openai-chatgpt-ads-us-rollout', '2026-03-21T20:00:00+00:00'),
        'featured': True,
        'opinion': 'L’AI consumer diventa adulta quando deve spiegare come monetizza senza intaccare la fiducia.',
        'qualityScore': 92,
        'visual': 'ai'
    },
    {
        'id': 'tech-20260323-google-cloud-nvidia-gtc-ai-infrastructure',
        'category': 'tech',
        'subcategory': 'cloud, GPU e stack per agentic AI',
        'title': 'Google Cloud e Nvidia accelerano la fase infrastrutturale dell’AI: Rubin, G4 e inference stack sempre più integrati',
        'hook': 'Dal GTC 2026 arriva un segnale netto: l’era degli agenti si giocherà sullo stack completo, non soltanto sul modello più brillante.',
        'body': 'Nel blog pubblicato in occasione di NVIDIA GTC 2026, Google Cloud presenta l’espansione della partnership con Nvidia come risposta ai carichi dell’agentic AI e delle architetture mixture-of-experts. Gli annunci includono il supporto in arrivo per Vera Rubin NVL72, il rafforzamento delle G4 VM con Blackwell, una preview di configurazioni frazionate via vGPU e l’integrazione di NVIDIA Dynamo con GKE Inference Gateway, oltre a un supporto più ampio su Vertex AI e Model Garden.\n\nLa lettura industriale è sempre più chiara: throughput, latenza, efficienza di inferenza e co-progettazione software-hardware stanno diventando la vera barriera competitiva dell’AI enterprise. Meno demo isolate, più controllo dell’infrastruttura che rende scalabili agenti, modelli multimodali e deployment continuativi.',
        'tags': ['Google Cloud', 'Nvidia', 'GTC', 'inference', 'data center'],
        'sourceLabel': 'Google Cloud',
        'sourceUrl': 'https://cloud.google.com/blog/products/compute/google-cloud-ai-infrastructure-at-nvidia-gtc-2026',
        'sourceCount': 1,
        'timestamp': keep_ts('tech-20260323-google-cloud-nvidia-gtc-ai-infrastructure', '2026-03-23T07:06:49+00:00'),
        'featured': False,
        'opinion': 'Nel 2026 l’AI enterprise premia chi controlla il sistema, non solo il modello.',
        'qualityScore': 91,
        'visual': 'tech'
    },
    {
        'id': 'startup-20260323-airstreet-fund-iii-ai-first',
        'category': 'startup',
        'subcategory': 'venture capital, AI-first e capacità strategiche',
        'title': 'Air Street chiude un terzo fondo da 232 milioni: il venture AI europeo alza il peso di software, science e defense',
        'hook': 'Non è soltanto un nuovo veicolo. È un segnale su dove il capitale vuole restare rilevante nell’economia AI del 2026.',
        'body': 'Con il lancio del Fund III, Air Street Capital annuncia 232,323,232 dollari per sostenere startup AI-first dal seed alle prime fasi growth in Nord America ed Europa, con assegni da 500 mila a 15 milioni e puntate selettive fino a 25 milioni. La tesi dichiarata attraversa software, developer tools e infrastruttura, techbio e scienza, oltre a difesa e sicurezza.\n\nLa notizia pesa perché descrive un venture meno dipendente dalla sola narrativa consumer e più orientato a capacità strategiche. In Europa, soprattutto, vedere software, science e defense nello stesso perimetro segnala un mercato che prova a finanziare competenze industriali dure, non soltanto applicazioni di moda.',
        'tags': ['Air Street Capital', 'venture capital', 'AI-first', 'difesa', 'startup'],
        'sourceLabel': 'Air Street Capital',
        'sourceUrl': 'https://press.airstreet.com/p/fund-iii',
        'sourceCount': 1,
        'timestamp': keep_ts('startup-20260323-airstreet-fund-iii-ai-first', '2026-03-23T09:05:00+01:00'),
        'featured': False,
        'opinion': 'Quando il venture unisce AI, science e defense, sta finanziando capacità prima ancora che storytelling.',
        'qualityScore': 89,
        'visual': 'startup'
    },
    {
        'id': 'scienza-20260320-cern-alice-primordial-plasma-small-systems',
        'category': 'scienza',
        'subcategory': 'fisica delle particelle, plasma primordiale e piccoli sistemi',
        'title': 'ALICE sposta il confine del plasma primordiale: un segnale robusto emerge anche nelle collisioni tra protoni',
        'hook': 'Il risultato accorcia la distanza concettuale tra collisioni pesanti e sistemi piccoli. Se il pattern regge, cambia il modo in cui leggiamo l’emergere della materia quark-gluoni.',
        'body': 'In uno studio pubblicato su Nature Communications e presentato dal CERN, la collaborazione ALICE riferisce di aver osservato un pattern comune tra collisioni protone-protone, protone-piombo e piombo-piombo al Large Hadron Collider. Il dato chiave riguarda l’anisotropic flow: in un ampio intervallo di momento, i barioni mostrano un flusso più forte dei mesoni, in linea con modelli che includono formazione ed evoluzione di quark-gluon plasma anche in sistemi molto piccoli.\n\nLa portata scientifica è doppia. Da un lato il risultato rafforza l’idea che il plasma primordiale non sia confinato agli eventi più massicci; dall’altro costringe a una lettura più raffinata dei meccanismi con cui emergono struttura collettiva e materia nei primi istanti dell’universo.',
        'tags': ['CERN', 'ALICE', 'LHC', 'quark-gluon plasma', 'fisica'],
        'sourceLabel': 'CERN / Nature Communications',
        'sourceUrl': 'https://home.cern/news/news/physics/alice-sees-new-sign-primordial-plasma-proton-collisions',
        'sourceCount': 2,
        'timestamp': keep_ts('scienza-20260320-cern-alice-primordial-plasma-small-systems', '2026-03-20T12:00:00+01:00'),
        'featured': False,
        'opinion': 'Quando un segnale tipico dei sistemi grandi riappare nei protoni, non cambia un dettaglio: cambia l’ipotesi di partenza.',
        'qualityScore': 88,
        'visual': 'science'
    },
    {
        'id': 'futuro-20260323-nvidia-emerald-ai-factories-grid-assets',
        'category': 'futuro',
        'subcategory': 'AI factories, energia flessibile e rete elettrica',
        'title': 'Nvidia ed Emerald AI trattano i data center come asset di rete: l’AI factory entra nell’economia dell’energia',
        'hook': 'La novità non è solo tecnica. Se i carichi AI diventano flessibili e coordinati con generazione, storage e interconnessione, il futuro dei modelli passa sempre più dal sistema elettrico.',
        'body': 'A CERAWeek 2026, Nvidia ed Emerald AI annunciano una collaborazione con AES, Constellation, Invenergy, NextEra Energy, Nscale Energy & Power e Vistra per sviluppare una nuova classe di AI factories progettate per connettersi più rapidamente alla rete e operare come asset energetici flessibili. Il riferimento è l’architettura Vera Rubin DSX e il software DSX Flex, che puntano a coordinare calcolo, storage e risorse behind-the-meter per ridurre i tempi di time-to-power e aiutare la stabilità della rete.\n\nLa lettura strategica è forte: il collo di bottiglia dell’AI non è più soltanto computazionale ma elettrico, regolatorio e infrastrutturale. Quando i data center vengono pensati come carichi negoziabili e non come domanda rigida, il futuro dell’AI smette di essere una storia solo da chip e diventa una storia da utility, interconnessioni e politica industriale.',
        'tags': ['AI factories', 'energia', 'data center', 'rete elettrica', 'CERAWeek'],
        'sourceLabel': 'NVIDIA Newsroom',
        'sourceUrl': 'https://nvidianews.nvidia.com/news/nvidia-and-emerald-ai-join-leading-energy-companies-to-pioneer-flexible-ai-factories-as-grid-assets',
        'sourceCount': 1,
        'timestamp': '2026-03-23T12:00:00-05:00',
        'featured': False,
        'opinion': 'La scarsità decisiva dell’AI sta diventando sempre più elettrica, negoziata e gestita come infrastruttura critica.',
        'qualityScore': 90,
        'visual': 'future'
    }
]

stats = {
    'editionUpdatedAt': EDITION_TS,
    'newsGeneratedToday': len(news),
    'sourcesAnalyzed': 9,
    'topicEmerging': [
        'Hormuz come test globale sulla libertà di navigazione',
        'Premio di rischio logistico oltre il prezzo del petrolio',
        'BCE più prudente davanti allo shock energetico',
        'AI consumer tra accesso, ads e fiducia dell’utente',
        'Stack AI integrato tra cloud, GPU e inference',
        'Venture europeo più esposto a science, defense e sistemi fisici',
        'AI factories trattate come asset energetici flessibili'
    ],
    'mostViewed': [
        'Hormuz diventa un test di governance globale: l’IMO chiede un corridoio operativo per il traffico civile',
        'La BCE difende l’opzionalità: con guerra ed energia nel quadro, Francoforte evita promesse premature sui tassi',
        'OpenAI porta ChatGPT Go su scala più ampia e prepara i test advertising: la monetizzazione entra senza toccare le risposte'
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

os.system(f'python3 {VALIDATOR} {NEWS_TMP} {STATS_TMP}') == 0 or (_ for _ in ()).throw(SystemExit('validation failed'))

NEWS_TMP.replace(NEWS)
STATS_TMP.replace(STATS)

post_news = NEWS.read_bytes()
post_stats = STATS.read_bytes()
post_news_sha = hashlib.sha256(post_news).hexdigest()
post_stats_sha = hashlib.sha256(post_stats).hexdigest()
post_news_mtime = NEWS.stat().st_mtime
post_stats_mtime = STATS.stat().st_mtime
post_stats_json = json.loads(post_stats.decode('utf-8'))

if post_news_sha == PRE_NEWS_SHA and post_news_mtime == PRE_NEWS_MTIME:
    raise SystemExit('news live file did not change')
if post_stats_sha == PRE_STATS_SHA and post_stats_mtime == PRE_STATS_MTIME:
    raise SystemExit('stats live file did not change')
if post_stats_json.get('editionUpdatedAt') != EDITION_TS:
    raise SystemExit('editionUpdatedAt mismatch after publish')
if post_stats_json.get('editionUpdatedAt') <= PRE_EDITION:
    raise SystemExit('editionUpdatedAt did not advance')
if not any(s.get('label') == 'Cadence' and s.get('value') == CADENCE for s in post_stats_json.get('signals', [])):
    raise SystemExit('cadence does not match edition minute')

print(json.dumps({
    'pre': {
        'news_sha': PRE_NEWS_SHA,
        'stats_sha': PRE_STATS_SHA,
        'news_mtime': PRE_NEWS_MTIME,
        'stats_mtime': PRE_STATS_MTIME,
        'editionUpdatedAt': PRE_EDITION,
    },
    'post': {
        'news_sha': post_news_sha,
        'stats_sha': post_stats_sha,
        'news_mtime': post_news_mtime,
        'stats_mtime': post_stats_mtime,
        'editionUpdatedAt': post_stats_json.get('editionUpdatedAt'),
    }
}, ensure_ascii=False, indent=2))
