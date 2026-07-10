from pathlib import Path
import json

base = Path('/root/.openclaw/workspace/aion-nexus')
news_path = base / 'data/news.json'
stats_path = base / 'data/stats.json'
news_tmp = base / 'data/news.json.tmp'
stats_tmp = base / 'data/stats.json.tmp'

current_news = json.loads(news_path.read_text())
old_ts = {item['id']: item['timestamp'] for item in current_news}

edition_updated_at = '2026-03-28T14:05:00+01:00'
cadence_value = 'Hourly auto-refresh · 14:05 CET'

items = [
  {
    'id': 'ai-20260328-nvidia-inference-trillion-opportunity',
    'category': 'ai',
    'subcategory': 'Inference economics, domanda enterprise e nuova gamba dei ricavi AI',
    'title': 'Nvidia vede nell’inference il vero moltiplicatore: il mercato dei chip AI può spingersi verso la soglia del trilione',
    'hook': 'Reuters racconta il cambio di baricentro: non è più solo training, ma inference su larga scala. Se il grosso della domanda AI si sposta nell’uso quotidiano dei modelli, il ciclo degli investimenti hardware diventa molto più esteso e meno episodico.',
    'body': 'La tesi di Nvidia è semplice ma pesante: quando l’AI entra davvero nei prodotti e nei flussi aziendali, servono acceleratori non soltanto per addestrare modelli giganteschi ma per farli girare in produzione, con latenze, costi e affidabilità accettabili. Questo allarga il mercato indirizzabile e rende la spesa AI meno legata ai soli laboratori di frontiera e più alla diffusione industriale dell’infrastruttura.\n\nPer il settore è un passaggio strategico. Se l’inference diventa la voce dominante, cambiano i vincitori lungo la catena del valore: chip, networking, memoria, data center e software di ottimizzazione entrano tutti nello stesso ciclo di spesa. L’AI smette ancora di più di essere una corsa a pochi modelli e somiglia sempre più a una piattaforma industriale diffusa.',
    'tags': ['Nvidia', 'AI inference', 'chip', 'data center', 'enterprise AI'],
    'sourceLabel': 'Reuters',
    'sourceUrl': 'https://news.google.com/rss/articles/CBMiuAFBVV95cUxNdzZqLTZuMnJNcm0wVG9VTFpSSnlZZTJvX3NXRTczU21sSFh1QU5rZUd0MDk3dE9xYWFOak8xblh4ZV9ONEstbTNzNDdyeXNsUzA1UktZMmR6YnJvTzdhVUMyOFFOaVVPdG1kY0lhVm5CdzJkV2Z3Q0hSRHYyWmZ6Rl9DZFduVURFcTVLTkdaYnR4TWxsa0JGV3F5V3Q3QzItTFVBZWVvajZOZzdiYW5MSk1iYnFvdDFN?oc=5',
    'sourceCount': 1,
    'timestamp': '2026-03-28T14:05:00+01:00',
    'featured': True,
    'opinion': 'Se l’inference scala davvero, Nvidia allunga il ciclo AI oltre l’hype del training.',
    'qualityScore': 95,
    'visual': 'ai'
  },
  {
    'id': 'tech-20260328-china-approval-nvidia-h200-big-tech',
    'category': 'tech',
    'subcategory': 'Export controls, procurement hyperscaler e ambiguità del decoupling',
    'title': 'Pechino apre agli H200 di Nvidia: ByteDance, Alibaba e Tencent tornano a fare shopping nel cuore della corsa AI',
    'hook': 'Reuters riferisce che la Cina ha dato il via libera a ByteDance, Alibaba e Tencent per acquistare chip H200 di Nvidia. È la fotografia più nitida del momento: il decoupling resta reale, ma la domanda per hardware di punta continua a forzare zone grigie e accomodamenti pratici.',
    'body': 'La notizia pesa perché riguarda tre gruppi che fanno scala vera in cloud, advertising, consumer internet e servizi AI. Se possono approvvigionarsi di H200, la competizione cinese sui modelli e sull’inference non dipende soltanto da sostituti domestici ma torna ad appoggiarsi, almeno in parte, alla catena tecnologica globale. Questo attenua l’idea di una separazione già compiuta e mostra quanto sia difficile chiudere davvero il rubinetto ai chip più desiderati.\n\nPer Washington e per l’industria il segnale è scomodo. Ogni eccezione o finestra regolatoria complica l’enforcement e rende il quadro meno lineare per i vendor. Ma per il mercato conta soprattutto altro: la fame di capacità AI dei grandi gruppi cinesi resta intatta, e continua a tradursi in ordini concreti.',
    'tags': ['Nvidia', 'H200', 'ByteDance', 'Alibaba', 'Tencent', 'Cina'],
    'sourceLabel': 'Reuters',
    'sourceUrl': 'https://news.google.com/rss/articles/CBMixgFBVV95cUxQeGZWV3pRRDlNMGl5UGI2bFNDSGFjYzJ5TlVteGJWSzJpTHdlaE4yWDFTQVBKc1dDMHA4WFNPUzVwSHJQb1E4OGI3ZnZrc2ZMbzEzcG1rdlItcFZjWGMwVVZQWmJ2ZjhTQmdQczlBY2xWeFU5RVFENHpOUzFFX2RKV3VqZGNxTDhqVWhjT2kxVUF0WHZ5NmJRUHlkVElDR1BrTnN1aXY0WDItUWxxLUZZbk4xN1ByaEtwY2dVbHRrRmlUUmd3WlE?oc=5',
    'sourceCount': 1,
    'timestamp': '2026-03-28T14:05:00+01:00',
    'featured': True,
    'opinion': 'Il decoupling vale meno degli ordini reali quando il bisogno di chip torna industriale.',
    'qualityScore': 94,
    'visual': 'tech'
  },
  {
    'id': 'geopolitica-20260328-yemen-missile-israel-us-iran',
    'category': 'geopolitica',
    'subcategory': 'Escalation regionale, Yemen e pressione sulle rotte energetiche',
    'title': 'Lo Yemen entra più apertamente nel conflitto: gli Houthi colpiscono Israele mentre proseguono i raid su obiettivi legati all’Iran',
    'hook': 'Reuters segnala che gli Houthi hanno colpito Israele nell’attuale ciclo di guerra mentre Israele e Stati Uniti continuano gli attacchi contro obiettivi collegati all’Iran. La crisi non si comprime: aggiunge fronti e rende meno credibile uno scenario di normalizzazione rapida.',
    'body': 'L’ingresso più esplicito del fronte yemenita aumenta il rischio sistemico per trasporto marittimo, assicurazioni, rotte energetiche e tempi di consegna. Ogni estensione geografica aggiunge una variabile che i governi possono assorbire politicamente, ma che le supply chain devono prezzare quasi subito. È qui che il conflitto smette di essere solo cronaca militare e diventa infrastruttura di rischio globale.\n\nPer l’Europa e per i mercati, la somma dei fronti è il vero problema. Più attori entrano in sequenza, meno credibile diventa lo scenario di raffreddamento rapido e più probabile appare una fase di prudenza prolungata su energia, shipping e coperture finanziarie.',
    'tags': ['Yemen', 'Houthi', 'Israele', 'Stati Uniti', 'Iran', 'Mar Rosso'],
    'sourceLabel': 'Reuters',
    'sourceUrl': 'https://news.google.com/rss/articles/CBMitAFBVV95cUxNNVVtc1ZtWmlSeGkxX2N1VkZxUW1RUkFReGRKX0o5OXROT21WUjVGMS1lUFlqVFpNcUtSN3gtR3BaMFNaMGR5RDRkYW1DaExPcXJ6eEx6dXlYRVBIWEpHSm94dWNlRTZlQnhaR1BwNGl0WnhneklBenpxV1dMcDFROHlGMFQtOVF1ZGxWUm14VWtvMXlicko5bWZZWHdvSUo1aUJELWxZYTgwZFZkX3ZJd242Z0I?oc=5',
    'sourceCount': 1,
    'timestamp': old_ts['geopolitica-20260328-yemen-missile-israel-us-iran'],
    'featured': True,
    'opinion': 'Ogni nuovo fronte attivo rende più costosa e meno credibile l’idea di un contenimento rapido.',
    'qualityScore': 96,
    'visual': 'geo'
  },
  {
    'id': 'mercati-20260328-wall-street-tumble-dow-correction-middle-east',
    'category': 'mercati',
    'subcategory': 'Azionario USA, correzione e shock geopolitico',
    'title': 'Wall Street continua il repricing: il Dow resta in correzione mentre la guerra spinge difensivi, energia e paura inflattiva',
    'hook': 'L’aggiornamento Reuters sul sell-off USA conferma che la pressione non è più confinata ai titoli più fragili: la correzione coinvolge il Dow e consolida l’idea che il conflitto in Medio Oriente venga trattato come rischio persistente per crescita e tassi.',
    'body': 'Quando il ribasso si allarga e l’indice più mainstream di Wall Street resta in correzione, il mercato manda un messaggio diverso rispetto a una semplice scossa tecnica. Più energia, più incertezza sui prezzi e meno visibilità sulla traiettoria dei tassi rendono il premio per il rischio azionario meno comprimibile. La lettura dominante smette così di essere buy-the-dip automatico e torna a privilegiare bilanci solidi, margini difendibili e cash flow.\n\nIl punto chiave è la qualità della rotazione. Se continuano a reggere i difensivi mentre si indeboliscono i segmenti più sensibili al ciclo, il repricing può consolidarsi oltre il rumore geopolitico immediato. A quel punto non si parlerebbe più solo di volatilità da headline, ma di un aggiustamento più profondo del costo del rischio.',
    'tags': ['Dow Jones', 'Wall Street', 'correzione', 'Middle East', 'risk-off'],
    'sourceLabel': 'Reuters',
    'sourceUrl': 'https://news.google.com/rss/articles/CBMirgFBVV95cUxQb09zaXpJQWtLeTJUeG82MC1qTks1Y2t4TnlhMk56bEpIT2JwQzJVWEx5eFQ3RFdVbG0wQUt2WGNxY3VzdG1xcVVuWUo2MUpMNVhXU2dRWEtwTW9PRHRRcV9HaUhFYXZzeE44Zjhnc2Mxdkw3VUh0TkhTTXlzTmNMTGVrZmV6b1c4NnU4SUJ4bDFSSWdGZkxtaDl0X1hFeE84UFhwUkM5VC1wLUp2c0E?oc=5',
    'sourceCount': 1,
    'timestamp': old_ts['mercati-20260328-wall-street-tumble-dow-correction-middle-east'],
    'featured': True,
    'opinion': 'Quando il Dow resta in correzione, la guerra non è più sfondo: entra direttamente nel prezzo del rischio.',
    'qualityScore': 95,
    'visual': 'markets'
  },
  {
    'id': 'finanza-20260328-india-assets-oil-shock-rupee-outflows',
    'category': 'finanza',
    'subcategory': 'Flussi globali, petrolio e stress sul capitale nei mercati emergenti',
    'title': 'Il petrolio accelera la fuga dal rischio: gli investitori esteri scaricano l’India e la rupia prende il colpo',
    'hook': 'Reuters segnala deflussi record dagli asset indiani mentre lo shock petrolifero rialza i timori su inflazione, partite correnti e margine di politica economica. È un promemoria duro: quando l’energia sale per guerra, i Paesi importatori pagano quasi subito in valuta e multipli.',
    'body': 'L’India è un caso rilevante perché non parliamo di un mercato periferico, ma di uno dei grandi barometri del rischio emergente. Se i capitali esteri arretrano con questa velocità, significa che il prezzo del petrolio non viene più letto come disturbo temporaneo ma come variabile capace di cambiare utili, inflazione e stabilità macro in tempi stretti. La pressione sulla rupia rende tutto più visibile.\n\nPer i portafogli globali il messaggio è ampio. Se il greggio resta alto e la guerra allunga la sua ombra su shipping e assicurazioni, i mercati emergenti importatori di energia tornano a essere il punto dove lo shock geopolitico si trasforma prima in stress finanziario.',
    'tags': ['India', 'rupia', 'petrolio', 'mercati emergenti', 'deflussi'],
    'sourceLabel': 'Reuters',
    'sourceUrl': 'https://news.google.com/rss/articles/CBMiuwFBVV95cUxOenVMQ25wc2dPNk42VXVPTDg5d0ozcmNLVUYxelNaVVlQZi1jdVQwanY5OGNCWVY2eDlnaEJYUmFTd21pYUNBYURGSlhiUTN5aDk0b25aSGliUWxTWXltcG9GSmx4UVNJaDdiTHEwelNhQk9kV01jTFhubkhjdTVzZW9wMFpQT3FSLXkyZmY0aWgxYkVqMlg0UU1FVmFUNXQ1RHVYRnVNaGxsZGoyUktWRzVXMldrMkdXa21R?oc=5',
    'sourceCount': 1,
    'timestamp': '2026-03-28T14:05:00+01:00',
    'featured': False,
    'opinion': 'La geopolitica pesa davvero quando trasforma il petrolio in fuga di capitali.',
    'qualityScore': 92,
    'visual': 'fin'
  },
  {
    'id': 'startup-20260328-openai-60bn-strategic-investors',
    'category': 'startup',
    'subcategory': 'Mega-funding AI, capitale strategico e consolidamento di ecosistema',
    'title': 'OpenAI alza ancora la scala: Nvidia, Microsoft e Amazon discutono un round fino a 60 miliardi',
    'hook': 'Reuters rilancia le indiscrezioni di The Information su un possibile investimento fino a 60 miliardi in OpenAI da parte di partner strategici come Nvidia, Microsoft e Amazon. Più che una raccolta, sembra un riassetto di potere attorno al centro di gravità dell’AI generativa.',
    'body': 'Se numeri di questa taglia entrano davvero sul tavolo, la distanza tra startup leader e resto del mercato smette quasi del tutto di essere colmabile con il solo prodotto. Capitale, compute, distribuzione cloud e accesso enterprise diventano parti dello stesso pacchetto. OpenAI verrebbe così trattata sempre meno come promessa ad altissima crescita e sempre più come infrastruttura privata di prima fascia.\n\nPer l’ecosistema il segnale è doppio. Da un lato conferma che i vincitori dell’AI stanno attirando risorse quasi sovrane; dall’altro rafforza l’idea che i grandi incumbents preferiscano comprare esposizione al futuro invece di restarne spettatori. La scala finanziaria continua a selezionare il campo di gioco.',
    'tags': ['OpenAI', 'Microsoft', 'Amazon', 'Nvidia', 'funding', 'AI'],
    'sourceLabel': 'Reuters',
    'sourceUrl': 'https://news.google.com/rss/articles/CBMi1AFBVV95cUxNc2F4bHlTMVBzSHAyOC1fYWpFTk5oRDZyS05TTU05MDBtOXkzOGktNXZnVDF2RzdxbGJqUW1oMTdHa19MbW96MV9Tb29qSWFvQmFUWk9sbWhjaFIyN05NMmdKLWM5d3NlQVlYN0NCbGVZbXA3REhiTUhXaXlySjNJV2RxRkpObzlTZmNzaXM0X1pIZG1rS1Q1RHEyTTVnNGNKNG1iaEV5T0VyZFp4aV9fVGd3d3BYLUZxajhpeF90NHczMjNob01NQmFMUmNSX1NhNEtFag?oc=5',
    'sourceCount': 1,
    'timestamp': '2026-03-28T14:05:00+01:00',
    'featured': False,
    'opinion': 'Quando i round sembrano politica industriale, il termine startup diventa quasi simbolico.',
    'qualityScore': 93,
    'visual': 'startup'
  },
  {
    'id': 'futuro-20260327-nasa-artemis-final-preparations',
    'category': 'futuro',
    'subcategory': 'Spazio, programma lunare e preparazione missione',
    'title': 'Artemis entra nella sua fase più credibile: la NASA porta gli astronauti verso le prove finali del ritorno umano alla Luna',
    'hook': 'Reuters descrive un equipaggio ormai arrivato alla fase conclusiva di preparazione per Artemis. La forza della notizia è che il programma lunare torna a sembrare esecuzione operativa, non semplice promessa di lungo periodo.',
    'body': 'Quando un programma spaziale passa alle prove finali, cambia il centro di gravità del racconto. Contano meno la retorica dell’ambizione e più la disciplina con cui NASA, equipaggi e partner industriali tengono insieme sistemi, procedure, finestre di lancio e sicurezza. È il momento in cui il futuro torna a pesare come capacità organizzativa concreta.\n\nPer industria e geopolitica dello spazio il segnale resta importante. Artemis è uno dei pochi progetti capaci di unire prestigio nazionale, catena industriale avanzata e ricadute tecnologiche di lungo ciclo. Più il calendario si avvicina all’esecuzione, più il futuro smette di sembrare branding e torna a somigliare a produzione reale.',
    'tags': ['NASA', 'Artemis', 'Luna', 'spazio', 'missione'],
    'sourceLabel': 'Reuters',
    'sourceUrl': 'https://news.google.com/rss/articles/CBMiZ0FVX3lxTE5tWVh6U3hTMUpKR0t0SGFBQjRJeXhaelZvT1BPb01uY19WREMyMUFPWWRGdkpjVlZMZjc3LWpMRndhZFdYMnRRQWNXSzdoN1VwOXN4Mmt1dU9IWXMtQ0d4QmhEdzc0c2c?oc=5',
    'sourceCount': 1,
    'timestamp': old_ts['futuro-20260327-nasa-artemis-final-preparations'],
    'featured': False,
    'opinion': 'Lo spazio torna serio quando il calendario operativo conta più della narrativa.',
    'qualityScore': 90,
    'visual': 'future'
  }
]

stats = {
  'editionUpdatedAt': edition_updated_at,
  'newsGeneratedToday': len(items),
  'sourcesAnalyzed': 24,
  'topicEmerging': [
    'L’inference sta diventando il vero motore economico della domanda AI',
    'Il decoupling sui chip resta poroso quando gli hyperscaler tornano a comprare',
    'L’allargamento del conflitto in Medio Oriente continua a pesare su shipping ed energia',
    'Il petrolio alto si scarica subito su valute e flussi dei grandi importatori emergenti',
    'Wall Street tratta guerra e tassi come un unico pacchetto di repricing',
    'Nell’AI il capitale strategico conta sempre più quanto la qualità tecnica',
    'I grandi programmi spaziali tornano credibili solo quando entrano in disciplina operativa'
  ],
  'mostViewed': [
    'Lo Yemen entra più apertamente nel conflitto: gli Houthi colpiscono Israele mentre proseguono i raid su obiettivi legati all’Iran',
    'Wall Street continua il repricing: il Dow resta in correzione mentre la guerra spinge difensivi, energia e paura inflattiva',
    'Nvidia vede nell’inference il vero moltiplicatore: il mercato dei chip AI può spingersi verso la soglia del trilione'
  ],
  'signals': [
    {'label': 'Edition', 'value': 'Public MVP'},
    {'label': 'Cadence', 'value': cadence_value},
    {'label': 'Mode', 'value': 'Italian briefing'},
    {'label': 'Focus', 'value': 'Source-backed news'}
  ]
}

news_tmp.write_text(json.dumps(items, ensure_ascii=False, indent=2) + '\n')
stats_tmp.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n')
json.loads(news_tmp.read_text())
json.loads(stats_tmp.read_text())
print('wrote temp files')
