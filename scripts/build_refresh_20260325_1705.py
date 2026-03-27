from pathlib import Path
import json

news = [
  {
    "id": "ai-20260325-manus-meta-china-exit-restrictions",
    "category": "ai",
    "subcategory": "M&A transfrontaliera, controllo export del talento e agenti general purpose",
    "title": "Pechino blocca i founder di Manus e trasforma il dossier Meta in un test di sovranità AI",
    "hook": "Reuters e Financial Times riferiscono che due cofondatori di Manus non possono lasciare la Cina mentre le autorità riesaminano la cessione a Meta. Non è più solo un deal: è un caso scuola di controllo politico sugli asset AI strategici.",
    "body": "Il punto di rottura è che nella review non entra soltanto il capitale, ma anche la mobilità dei founder e il trasferimento implicito di know-how. Se un'uscita cross-border può essere rallentata fino a limitare gli spostamenti dei dirigenti, il mercato deve leggere l'AI come industria soggetta a filtri sovrani molto più duri rispetto al software tradizionale.\n\nPer Meta il rischio non è soltanto l'esito di questa operazione, ma il precedente che si crea per tutte le future acquisizioni in aree come agenti, automazione e foundation models. Il premio regolatorio sulle operazioni internazionali sale, e con lui il valore strategico della localizzazione di talenti e proprietà intellettuale.",
    "tags": ["Manus", "Meta", "Cina", "AI agents", "M&A"],
    "sourceLabel": "Reuters / FT",
    "sourceUrl": "https://whtc.com/2026/03/25/china-bars-manus-co-founders-from-leaving-country-as-it-reviews-sale-to-meta-ft-reports/",
    "sourceCount": 2,
    "timestamp": "2026-03-25T08:05:00+01:00",
    "featured": True,
    "opinion": "Quando i founder diventano parte della review, la sovranità tecnologica è già entrata nel term sheet.",
    "qualityScore": 96,
    "visual": "ai"
  },
  {
    "id": "tech-20260325-china-chip-growth-ai-supply-chain",
    "category": "tech",
    "subcategory": "Semiconduttori, colli di bottiglia industriali e infrastruttura AI",
    "title": "La corsa ai datacenter AI allunga la filiera dei chip cinesi ben oltre il wafer",
    "hook": "Da Semicon China 2026 Reuters raccoglie un messaggio netto: la domanda AI sta accelerando capex, backlog e capacità produttiva in tutta la filiera. Packaging, test e interconnessioni ottiche diventano il vero stress point del ciclo.",
    "body": "L'aspetto più importante è che la pressione non si concentra più solo sulla produzione dei chip, ma su tutti i livelli necessari a far scalare i carichi AI: test avanzato, optical interconnect, moduli e materiali. Quando i fornitori parlano di ordini già impegnati fino al prossimo anno, significa che il collo di bottiglia si sta distribuendo lungo l'intera architettura industriale.\n\nPer il mercato globale è anche un segnale sulla profondità della risposta cinese. Nelle fasce dove può eseguire più rapidamente, Pechino continua ad aumentare massa produttiva e capacità di assorbire domanda; questo non elimina il vantaggio estero nei segmenti più avanzati, ma rende la competizione molto più lunga e manifatturiera di quanto suggerisca la sola narrativa sui nodi di frontiera.",
    "tags": ["Cina", "chip", "AI infrastructure", "supply chain", "Semicon China"],
    "sourceLabel": "Reuters",
    "sourceUrl": "https://whtc.com/2026/03/25/ai-boom-accelerates-chinas-chip-industry-growth-as-demand-strains-supply-chain/",
    "sourceCount": 1,
    "timestamp": "2026-03-25T15:05:00+01:00",
    "featured": True,
    "opinion": "Il prossimo squeeze dell'AI non riguarda solo i chip: riguarda tutto ciò che li collega, li testa e li confeziona.",
    "qualityScore": 94,
    "visual": "tech"
  },
  {
    "id": "geopolitica-20260325-germany-army-ai-wartime-decisions",
    "category": "geopolitica",
    "subcategory": "Difesa europea, dottrina NATO e AI per il command loop",
    "title": "La Bundeswehr porta l'AI nel ciclo decisionale di guerra e alza il tono europeo sulla difesa",
    "hook": "Reuters riferisce che l'esercito tedesco vuole usare strumenti AI per leggere più rapidamente i dati di campo, prendendo lezione dall'esperienza ucraina. Il passaggio è importante perché sposta il tema dall'innovazione alla dottrina operativa.",
    "body": "Se l'obiettivo dichiarato è comprimere il tempo necessario a interpretare sensori, immagini e pattern nemici, allora l'AI non è più un accessorio di analisi ma un moltiplicatore diretto del comando e controllo. Berlino sta dicendo apertamente che il vantaggio decisionale in guerra dipenderà sempre di più dalla capacità di trattare flussi informativi che gli esseri umani da soli non riescono più a governare in tempo utile.\n\nResta il presidio umano sulle decisioni finali, ma la traiettoria è chiara: interoperabilità con gli standard NATO, urgenza di implementazione e tensione costante tra sovranità dei dati e soluzioni statunitensi già più mature. In pratica, la cautela europea lascia spazio alla necessità di schierare capacità reali.",
    "tags": ["Germania", "Bundeswehr", "AI militare", "NATO", "Ucraina"],
    "sourceLabel": "Reuters",
    "sourceUrl": "https://whtc.com/2026/03/25/german-army-eyes-ai-tools-to-expedite-wartime-decision-making/",
    "sourceCount": 1,
    "timestamp": "2026-03-25T15:05:00+01:00",
    "featured": True,
    "opinion": "Quando anche Berlino parla di battlefield AI in termini operativi, il dibattito europeo è già uscito dal laboratorio.",
    "qualityScore": 95,
    "visual": "geo"
  },
  {
    "id": "finanza-20260325-ecb-inflation-forecast-energy-costs",
    "category": "finanza",
    "subcategory": "BCE, shock energetico e funzione di reazione sui tassi",
    "title": "Lagarde irrigidisce il tono della BCE: l'energia torna a contare più del conforto del mercato",
    "hook": "La BCE ha rivisto al rialzo le stime sull'inflazione energetica e Christine Lagarde ha segnalato meno tolleranza verso rincari anche non troppo persistenti. Per gli investitori il cambio vero è nella funzione di reazione, non nel dato isolato.",
    "body": "Quando Francoforte suggerisce di essere pronta ad agire anche di fronte a pressioni sui prezzi meno durature del previsto, il mercato capisce che la soglia politica per una risposta si è abbassata. Questo modifica immediatamente il pricing di bond, credito e azionario europeo, perché il capitale torna a scontare una banca centrale più guardinga e meno paziente.\n\nL'effetto pratico è un eurozona rate path più nervoso anche senza una stretta istantanea. Basta l'idea di una BCE meno accomodante davanti a uno shock energetico per rimettere in moto volatilità, repricing e domande sulla resilienza della crescita sotto costo del denaro più alto.",
    "tags": ["BCE", "Lagarde", "inflazione", "energia", "tassi"],
    "sourceLabel": "Reuters",
    "sourceUrl": "https://news.google.com/rss/articles/CBMitAFBVV95cUxPcm9mNG8xc2lRUGJoOUpkRWRnREYzc3EyNGpNalRRdUVKYWsyUmdfWnpSbmlFOTF1d0FDSFE1bGdvYXlwNUgzX0VLSGt2Vm1jU1g3VFo0MWNxb3dlV2JwZkYwMEF3Y2dqaVdLNVVkeHRDLUVSYkdHMy1tMnJjWFpqU0hyUG81OE4yaFlTRG9TLXNRelY3SGwtN1pVVnNwcjFFMUpnX3NTcjR0STA1dDRwamN5bVY?oc=5",
    "sourceCount": 2,
    "timestamp": "2026-03-25T13:05:00+01:00",
    "featured": False,
    "opinion": "Più del tasso di oggi, pesa una BCE che abbassa la soglia di allarme sui prezzi energetici.",
    "qualityScore": 93,
    "visual": "fin"
  },
  {
    "id": "mercati-20260325-oil-falls-ceasefire-hopes-middle-east",
    "category": "mercati",
    "subcategory": "Greggio, rischio geopolitico e de-escalation sulle rotte energetiche",
    "title": "Il greggio scarica premio di guerra: la tregua mediorientale entra nel pricing più dei fondamentali",
    "hook": "Il petrolio arretra dopo le indiscrezioni su una proposta di cessate il fuoco in 15 punti in Medio Oriente. Il movimento segnala che il mercato sta sgonfiando soprattutto il premio di rischio logistico e geopolitico.",
    "body": "In questi passaggi il greggio smette di riflettere solo domanda e offerta corrente e diventa un termometro della probabilità assegnata a una de-escalation credibile. Se gli operatori iniziano a prezzare rotte più sicure e minore rischio di interruzioni, il repricing può essere veloce anche in assenza di un cambiamento immediato dei fondamentali fisici.\n\nPer i portafogli conta perché riduce temporaneamente una delle fonti di pressione inflattiva globale più difficili da governare. Ma la fragilità resta alta: basta un segnale contrario sul terreno per far rientrare nel prezzo quel premio di guerra che oggi il mercato prova a scaricare.",
    "tags": ["petrolio", "Middle East", "ceasefire", "greggio", "risk premium"],
    "sourceLabel": "Reuters",
    "sourceUrl": "https://news.google.com/rss/articles/CBMixAFBVV95cUxQNVU5QWgzLWc3VmJ3VS1jcUNrcklMYXFiNG8yeE1wcmdqZTJHZDBxd1ZLS0hYSEdMQTlzQUJTa0FHcjdyeHQ4Ry0yQXN0OXI4QWsxVmJXbjJvNTBGM1FYMUtNZUNDM01PSmxRay1IcG9XQTFQc045bkZxbHZJeE94VC1zaHJVTmlVaWx6b21sTmlqZGxkRHdQQ0hwOEphLWVTQ29KbUNtdkprQXZ4QWVUMGVvamZUVVh1blUwcGt3TFlaTkhG?oc=5",
    "sourceCount": 1,
    "timestamp": "2026-03-25T13:48:00+01:00",
    "featured": True,
    "opinion": "Se il greggio scende su una bozza di tregua, vuol dire che il rischio di supply disruption era già fortemente nel prezzo.",
    "qualityScore": 92,
    "visual": "markets"
  },
  {
    "id": "startup-20260325-mastercard-bvnk-stablecoin-acquisition",
    "category": "startup",
    "subcategory": "Fintech, stablecoin e consolidamento dei rails di pagamento",
    "title": "Mastercard compra BVNK e tratta le stablecoin come plumbing da enterprise",
    "hook": "L'acquisizione di BVNK da parte di Mastercard segnala che le stablecoin stanno scivolando dalla narrativa crypto verso l'infrastruttura dei pagamenti. Quando un incumbent compra execution, vuol dire che vede domanda operativa e non solo optionalità.",
    "body": "BVNK porta in dote un layer costruito per uso aziendale, compliance e regolamento, cioè esattamente le parti che separano un esperimento fintech da un'infrastruttura utile su scala. Per Mastercard l'operazione è un modo per presidiare i rails programmabili senza aspettare che il mercato maturi da solo tramite partnership leggere.\n\nPer l'ecosistema startup il messaggio è pragmatico: il valore si concentra su chi rende gli asset digitali utilizzabili dentro vincoli reali di regolazione, tesoreria e integrazione con sistemi esistenti. Meno ideologia crypto, più software finanziario industriale.",
    "tags": ["Mastercard", "BVNK", "stablecoin", "fintech", "pagamenti"],
    "sourceLabel": "Reuters",
    "sourceUrl": "https://news.google.com/rss/articles/CBMiogFBVV95cUxNbDd0WElvQW9xWHJrVW5KTjlBUjgxRXNQM2o2V21RNkk1cV9lc2RfLVkxdVlBbEdrdEFqM3RwQXBfcGZkd1hSWGlWNGpYcFpieG0xUWplWHY4NEpMYXBSV1gwbGRvY29ZOVBoNHRVNTVac3g1bkUydG9OeGxaNkJEdFFvSlhnOWV3Y09NYlN2WEd2UDFCNWFjNm9tOHBLaWpWenc?oc=5",
    "sourceCount": 1,
    "timestamp": "2026-03-25T13:05:00+01:00",
    "featured": False,
    "opinion": "Quando un incumbent compra rails stablecoin, sta comprando meno narrativa e più infrastruttura.",
    "qualityScore": 91,
    "visual": "startup"
  }
]

stats = {
  "editionUpdatedAt": "2026-03-25T17:05:00+01:00",
  "newsGeneratedToday": len(news),
  "sourcesAnalyzed": 12,
  "topicEmerging": [
    "La sovranità tecnologica sta entrando direttamente nelle operazioni di M&A AI",
    "L'infrastruttura AI sposta i colli di bottiglia da wafer a test, packaging e ottica",
    "La difesa europea accelera sull'AI come leva di superiorità decisionale",
    "La BCE torna più sensibile ai rincari energetici nella lettura dell'inflazione",
    "Sul greggio il premio geopolitico si muove più in fretta dei fondamentali fisici",
    "Le stablecoin diventano interessanti quando funzionano come rails enterprise"
  ],
  "mostViewed": [
    "Pechino blocca i founder di Manus e trasforma il dossier Meta in un test di sovranità AI",
    "La Bundeswehr porta l'AI nel ciclo decisionale di guerra e alza il tono europeo sulla difesa",
    "La corsa ai datacenter AI allunga la filiera dei chip cinesi ben oltre il wafer"
  ],
  "signals": [
    {"label": "Edition", "value": "Public MVP"},
    {"label": "Cadence", "value": "Hourly auto-refresh · 17:05 CET"},
    {"label": "Mode", "value": "Italian briefing"},
    {"label": "Focus", "value": "Source-backed news"}
  ]
}

Path('/root/.openclaw/workspace/aion-nexus/data/news.json.tmp').write_text(json.dumps(news, ensure_ascii=False, indent=2) + '\n')
Path('/root/.openclaw/workspace/aion-nexus/data/stats.json.tmp').write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n')
