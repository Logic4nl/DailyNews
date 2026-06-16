#!/usr/bin/env python3
import html, json, sys

DATE_ISO = "2026-06-17"
DATE_HUMAN = "Wednesday, June 17, 2026"
PREV_ISO = "2026-06-16"
MIN_ISO = "2026-03-19"

SECTIONS = [
    ("global", "Global News", "#1B998B"),
    ("netherlands", "Netherlands", "#E8703A"),
    ("ai-hpc", "AI & HPC", "#7B2D8E"),
    ("crypto-macro", "Crypto & Macro", "#E8B130"),
    ("mental-health", "AI & Mental Health", "#D63B47"),
    ("sports", "Sports", "#2478A0"),
    ("consumer-tech", "Consumer Tech", "#3D5A80"),
]

DATA = {
"global": [
 {"hero":True,"sub":"Conflicts & Security",
  "h3":"US and Iran sign ceasefire memorandum, agree to reopen Hormuz",
  "summary":"Washington and Tehran signed a Pakistan-brokered memorandum to firm up the spring truce, reopen the Strait of Hormuz and open a 60-day window of talks.",
  "body":["The understanding aims to convert the fragile April ceasefire into a durable arrangement, reopening the Strait of Hormuz to tanker traffic and setting a 60-day period for negotiations on Iran's nuclear programme and broader regional security.","Markets read the deal as a clear de-escalation. Oil slid on the prospect of restored Gulf flows, easing one of the main inflation pressures hanging over the global economy since the spring conflict."],
  "sources":[("Bloomberg","https://www.bloomberg.com/news/articles/2026-06-15/oil-holds-losses-after-iran-deal-spurs-stock-rally-markets-wrap"),("TheStreet","https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-16-2026")]},
 {"h3":"Ukraine and Russia trade fire as European leaders push direct talks",
  "summary":"Leaders of the UK, France and Germany backed Zelenskyy's call for direct ceasefire negotiations even as both sides kept up deadly strikes.",
  "body":["After a London meeting, the three European leaders endorsed Ukraine's push for direct talks with Moscow. The diplomatic effort came as Russia and Ukraine kept trading air attacks, with a Russian strike killing five and wounding more than a dozen in the Zaporizhzhia region.","Earlier short truces around Orthodox Easter and Victory Day failed to hold, leaving mediators trying again to broker a lasting pause in the fighting."],
  "sources":[("Al Jazeera","https://www.aljazeera.com/news/2026/6/8/ukraine-russia-trade-fire-as-zelenskyy-allies-back-call-for-direct-talks")]},
 {"h3":"Trackers say Russian advance has slowed sharply",
  "summary":"Open-source monitors report fluctuating front lines, a marked slowdown from early-2026 Russian momentum.",
  "body":["Battlefield trackers logged only small net Russian gains in early June after losing ground in the preceding weeks, with occupied territory holding near 45,000 square miles.","The trend points to a stalemate rather than breakthrough, strengthening the case some European capitals are making for a negotiated pause."],
  "sources":[("Russia Matters","https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-june-10-2026")]},
 {"h3":"Israel keeps pressure on Gaza as Lebanon front simmers",
  "summary":"Satellite imagery shows expanding Israeli posts in Gaza while a separate truce with Lebanon only loosely holds.",
  "body":["Monitors recorded the highest monthly tally of Israeli strikes since the October 2025 ceasefire, with new outposts visible east of Gaza City. A US-brokered arrangement with Lebanon has reduced cross-border fire without ending it.","Analysts describe both fronts as managed standoffs that could reignite, even as attention shifts to the wider Iran track."],
  "sources":[("Al Jazeera","https://www.aljazeera.com/news/2026/6/3/israel-is-building-more-military-posts-in-gaza-satellite-imagery-shows"),("ACLED","https://acleddata.com/update/middle-east-overview-june-2026")]},
 {"sub":"Diplomacy & Trade",
  "h3":"China tightens overseas travel rules for its AI researchers",
  "summary":"Researchers at Alibaba and DeepSeek now need Beijing's approval before foreign trips, a control once reserved for nuclear scientists.",
  "body":["The curbs aim to stop talent poaching and the outward transfer of know-how as Chinese AI nears parity with the US. Stanford's 2026 AI Index puts the capability gap at about 2.7 percent.","The move mirrors tightening on the US side and signals that both powers now treat AI expertise as a controlled strategic asset."],
  "sources":[("TechTimes","https://www.techtimes.com/articles/317325/20260528/china-ai-travel-curbs-reach-alibaba-deepseek-private-sector-researchers-need-beijing-approval.htm")]},
 {"h3":"Strait of Hormuz reopening ripples through shipping and energy",
  "summary":"Restored Gulf traffic is expected to unwind months of rerouting and elevated freight and insurance costs.",
  "body":["The earlier closure forced tankers onto longer routes and pushed crude and shipping costs higher worldwide. A reopening should gradually ease those pressures if the truce holds.","Forecasters caution that any renewed disruption would quickly reverse the relief, keeping energy a key swing factor for global inflation."],
  "sources":[("EIA","https://www.eia.gov/outlooks/steo/"),("Bloomberg","https://www.bloomberg.com/news/articles/2026-06-15/oil-holds-losses-after-iran-deal-spurs-stock-rally-markets-wrap")]},
 {"sub":"Humanitarian & Climate",
  "h3":"Europe swelters through an exceptionally early heatwave",
  "summary":"May and early June records fell across western Europe, with high readings in Portugal, France and the UK.",
  "body":["Temperatures touched 40.3C in Portugal, 36C in France and above 35C in the UK in an unusually early heat episode. Scientists link the intensity to a warming climate.","Health agencies warned of risks to vulnerable groups as cities brace for more frequent and earlier extreme heat."],
  "sources":[("Carbon Brief","https://www.carbonbrief.org/cited-9-june-2026-europes-exceptional-heatwave-warming-forecast-amoc-observations-at-risk/")]},
 {"h3":"WMO forecasts near-record global temperatures through 2030",
  "summary":"A WMO and Met Office outlook projects yearly averages of 1.3 to 1.9C above pre-industrial levels over the next five years.",
  "body":["The forecast points to a sustained run of near-record warmth, with a real chance of individual years breaching the 1.5C mark that anchors international climate goals.","Officials say the trajectory underscores the need for both rapid emissions cuts and stronger adaptation against heat, flooding and fire."],
  "sources":[("WMO","https://wmo.int/media/news/extreme-heat-cold-precipitation-and-fires-mark-start-of-2026")]},
 {"h3":"Floods and extreme heat deepen humanitarian strain in Africa",
  "summary":"Severe flooding in Southern Africa has killed more than 200 since late 2025 while extreme heat hits South Sudan.",
  "body":["Aid agencies report mounting displacement from flooding across Southern Africa alongside dangerous heat affecting outdoor workers and people in poor housing in South Sudan.","Researchers warn many urban areas are nearing conditions that threaten health and infrastructure, widening the humanitarian challenge from compounding climate shocks."],
  "sources":[("World Weather Attribution","https://www.worldweatherattribution.org/location/africa/")]},
 {"h3":"Expanded World Cup opens across North America",
  "summary":"The first 48-team World Cup is under way across the US, Canada and Mexico, running through mid-July.",
  "body":["The tournament marks the largest edition yet and the first hosted jointly by three nations, with matches spread across stadiums in all three countries.","Organisers are managing heat, travel and logistics at unprecedented scale as the group stage gets going."],
  "sources":[("Olympics.com","https://www.olympics.com/en/news/fifa-world-cup-2026-every-match-group-result-tuesday-16-june-live-scores")]},
],
"netherlands": [
 {"hero":True,"sub":"Politics & Policy",
  "h3":"Jetten cabinet revives bill to criminalise undocumented stay",
  "summary":"The D66-led minority cabinet wants to reintroduce a measure penalising illegal residence after parliament rejected an earlier hardline package.",
  "body":["Asylum minister Bart van den Brink is seeking to restore measures left out of the EU migration pact through separate legislation, with the cabinet pressing again on criminalising undocumented stay.","The push tests the minority coalition of D66, VVD and CDA, which must find parliamentary support for a contested agenda on a politically charged issue."],
  "sources":[("NL Times","https://nltimes.nl/2026/05/07/dutch-cabinet-pushes-new-law-criminalize-undocumented-stay"),("DutchNews.nl","https://www.dutchnews.nl/2026/02/rob-jettens-team-who-is-who-in-the-new-dutch-cabinet/")]},
 {"h3":"EU migration pact takes effect, reshaping Dutch asylum rules",
  "summary":"The bloc's migration and asylum pact came into force on June 12, covering part of the policy the cabinet had sought nationally.",
  "body":["The pact standardises parts of asylum processing across member states and absorbs several measures the Dutch government wanted, prompting it to pursue the remainder through domestic law.","Officials are now mapping which national proposals are still needed and which are superseded by the EU framework."],
  "sources":[("InfoMigrants","https://www.infomigrants.net/en/post/71031/dutch-lawmakers-reject-proposed-hardline-asylum-bill")]},
 {"h3":"Anti-asylum protests flare with arson and arrests",
  "summary":"Arrivals at a Loosdrecht site were met by protesters who set fire to surrounding shrubs, drawing riot police.",
  "body":["Demonstrators obstructed firefighters and several people were detained for arson and disorder as tensions over reception centres escalated.","The unrest highlights the volatile local politics around housing asylum seekers as the cabinet tightens national policy."],
  "sources":[("DutchNews.nl","https://www.dutchnews.nl/2026/05/arson-and-arrests-as-anti-asylum-protests-escalate/")]},
 {"sub":"Economy & Housing",
  "h3":"DNB projects house prices rising 3 to 4 percent a year to 2028",
  "summary":"The central bank's spring projections see cooler but still positive price growth after last year's surge.",
  "body":["DNB expects annual house-price gains of 3 to 4 percent between 2026 and 2028, well below the pace seen in 2025 as higher mortgage rates and softer confidence weigh on demand.","Prices remain well above the 2022 peak in nominal terms, leaving affordability a central political pressure point."],
  "sources":[("De Nederlandsche Bank","https://www.dnb.nl/en/current-economic-issues/housing-market/")]},
 {"h3":"Dutch inflation eased to 3.4 percent in May",
  "summary":"Consumer price growth slowed but stayed above the euro-area average.",
  "body":["May inflation came in at 3.4 percent, continuing a gradual cooling from prior years while remaining elevated relative to the ECB target.","Energy swings tied to the spring conflict remain a wildcard for the path of Dutch prices through the summer."],
  "sources":[("De Nederlandsche Bank","https://www.dnb.nl/en/the-euro-and-europe/inflation/")]},
 {"h3":"Housing shortage near 400,000 homes keeps a floor under prices",
  "summary":"Rabobank says the market shows no real signs of cooling even as supply slowly grows.",
  "body":["The structural shortfall of roughly 400,000 homes continues to support demand, making a meaningful price drop unlikely despite weaker affordability.","Economists expect supply gains to chip only slowly at the gap, keeping pressure on first-time buyers and renters."],
  "sources":[("Rabobank","https://www.rabobank.com/knowledge/d011508452-dutch-housing-market-quarterly-no-signs-of-cooling-even-as-supply-grows")]},
 {"h3":"IMF trims Dutch growth forecast to 1.2 percent for 2026",
  "summary":"After 1.9 percent real growth in 2025, the Fund sees slower expansion this year.",
  "body":["The IMF projects 1.2 percent growth in 2026 and 1.4 percent in 2027, a step down that reflects softer global demand and tighter financial conditions.","The Dutch economy proved resilient last year but faces a more challenging external backdrop."],
  "sources":[("Global Property Guide","https://www.globalpropertyguide.com/europe/netherlands/price-history")]},
 {"sub":"Society & Culture",
  "h3":"The Hague signals readiness to help secure the Strait of Hormuz",
  "summary":"Dutch officials said they would consider contributing to securing the strait if a US-Iran peace deal holds.",
  "body":["The stance shows how widely the spring conflict reverberated through European policy, with the Netherlands weighing a role in protecting a waterway vital to global trade.","Any contribution would hinge on the durability of the new US-Iran understanding."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
],
"ai-hpc": [
 {"hero":True,"sub":"Foundation Models & Releases",
  "h3":"OpenAI launches GPT-5.5, its most capable model yet",
  "summary":"The release posts state-of-the-art results in agentic coding, computer use and knowledge work, served on Nvidia GB200 NVL72 systems.",
  "body":["GPT-5.5 leads benchmarks including Terminal-Bench 2.0 and OSWorld-Verified, with OpenAI citing strong early internal results. The model is priced at roughly twice GPT-5.4 and the public API is not yet open.","The launch sharpens the frontier race just as compute and power constraints dominate the industry's planning."],
  "sources":[("llm-stats","https://llm-stats.com/llm-updates"),("unrot.co","https://unrot.co/blogs/ai-news-today-june-15-2026")]},
 {"h3":"OpenAI stands up DeployCo and buys consultancy Tomoro",
  "summary":"A majority-owned deployment subsidiary launches with over $4bn to help enterprises build and run AI systems.",
  "body":["OpenAI created DeployCo to package enterprise rollout work, folding in Tomoro's roughly 150 engineers and partnering with firms including TPG, Bain Capital and Brookfield.","The move pushes OpenAI deeper into services as it tries to convert model leadership into enterprise revenue."],
  "sources":[("unrot.co","https://unrot.co/blogs/ai-news-today-june-15-2026")]},
 {"h3":"Nvidia names Anthropic and OpenAI among Vera chip users",
  "summary":"Nvidia said leading labs are big early customers of its new Vera processor.",
  "body":["The disclosure underscores how tightly the top model developers are tied to Nvidia's roadmap as they scale training and inference.","Demand for the latest accelerators remains a gating factor for frontier progress."],
  "sources":[("Bloomberg","https://www.bloomberg.com/news/articles/2026-06-01/nvidia-says-anthropic-openai-among-big-users-of-new-vera-chip")]},
 {"h3":"Anthropic files for a trillion-dollar IPO, publishes AI pause proposal",
  "summary":"The company moved toward a landmark listing the same week it floated a proposal for a global pause on the most advanced AI.",
  "body":["The juxtaposition drew attention to the tension between commercial scale and safety advocacy, with Anthropic also extending Claude access in Japan under its Mythos line.","The filing would mark one of the largest tech listings ever if it proceeds at the mooted valuation."],
  "sources":[("dentro.de","https://dentro.de/ai/news/"),("unrot.co","https://unrot.co/blogs/ai-news-today-june-15-2026")]},
 {"sub":"AI/HPC Stocks & Infrastructure",
  "h3":"Nvidia takes option to invest up to $2.1bn in IREN",
  "summary":"The chipmaker deepened ties with the data-centre operator through a sizeable investment option.",
  "body":["The arrangement aligns Nvidia with a miner-to-HPC operator building out AI compute capacity, part of a wave of chip-and-infrastructure tie-ups.","It signals continued appetite to lock in power and siting for AI workloads."],
  "sources":[("HL","https://www.hl.co.uk/shares/stock-market-news/company--news/openai,-nvidia-expected-to-announce-major-uk-data-centre-investments")]},
 {"h3":"Mistral secures $830m to build its first data centre near Paris",
  "summary":"The French lab will house 13,800 Nvidia GB300 GPUs at a 44 MW site and is exploring custom silicon.",
  "body":["The Bruyeres-le-Chatel facility is slated to come online this year as Mistral pushes toward 200 MW of European compute by 2027. The company has not named a chip partner or architecture.","The financing marks one of Europe's larger sovereign-AI infrastructure bets to date."],
  "sources":[("Phemex","https://phemex.com/news/article/mistral-ai-secures-830m-debt-financing-for-data-center-and-chip-development-86685"),("Techzine","https://www.techzine.eu/news/applications/140079/mistral-raises-e723m-to-expand-its-ai-infrastructure/")]},
 {"h3":"Mistral joins 1.4 GW Paris-region AI campus venture",
  "summary":"A joint venture with Bpifrance, UAE fund MGX and Nvidia plans a vast campus near Paris.",
  "body":["Construction is set to begin in the second half of 2026 with operations by 2028, supporting the full AI lifecycle from training to inference.","The project anchors France's bid to host frontier-scale compute on home soil."],
  "sources":[("Techzine","https://www.techzine.eu/news/applications/140079/mistral-raises-e723m-to-expand-its-ai-infrastructure/")]},
 {"h3":"Alphabet to raise about $85bn for AI data centres",
  "summary":"The equity raise includes a reported $10bn commitment from Berkshire Hathaway.",
  "body":["The capital targets a sweeping build-out of AI compute as hyperscaler spending escalates. Collective Big Tech AI infrastructure outlays may top $650bn in 2026.","The scale of financing highlights how capital-intensive the AI race has become."],
  "sources":[("Crypto Briefing","https://cryptobriefing.com/google-ai-delay-chip-stocks-data-centers/")]},
 {"h3":"Google AI project delay rattles chip stocks",
  "summary":"A reported slip in a Google AI effort knocked semiconductor names even as data-centre spending kept climbing.",
  "body":["The reaction showed how sensitive chip valuations have grown to single hyperscaler decisions, though underlying buildout momentum remained intact.","Investors are parsing each delay for signals on the durability of AI capex."],
  "sources":[("Crypto Briefing","https://cryptobriefing.com/google-ai-delay-chip-stocks-data-centers/")]},
 {"h3":"UAE 5 GW data-centre project reportedly draws OpenAI, Nvidia and Cisco",
  "summary":"Reports tie major US tech names to a large new Gulf compute project.",
  "body":["The plan would add significant capacity in the region as sovereign-AI ambitions and US partnerships expand across the Gulf.","Power, cooling and chip supply remain the binding constraints on such projects."],
  "sources":[("Seeking Alpha","https://seekingalpha.com/news/4449713-openai-may-be-part-of-new-5gw-data-center-project-in-uae-report")]},
 {"h3":"Meta unveils new in-house AI chips",
  "summary":"Meta announced fresh custom silicon to cut its reliance on third-party accelerators.",
  "body":["The chips target Meta's training and inference needs as it scales models and infrastructure spending.","Custom silicon is increasingly central to hyperscaler cost and supply strategies."],
  "sources":[("Yahoo Finance","https://finance.yahoo.com/news/live/tech-stocks-today-anthropic-says-pentagon-ban-could-cost-it-billions-meta-announces-new-ai-chips-134456659.html")]},
 {"sub":"Agents & Automation",
  "h3":"SpaceX to acquire AI coding startup Cursor in $60bn deal",
  "summary":"The acquisition vaulted SpaceX's valuation 20 percent higher, past Amazon.",
  "body":["The deal folds a fast-growing AI coding tool into SpaceX and reset its valuation to a record. It signals how aggressively cash-rich firms are buying AI capability.","Integration plans and rationale beyond talent remain to be detailed."],
  "sources":[("TheStreet","https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-16-2026")]},
 {"h3":"GPT-5.5 raises the bar on agentic coding and computer use",
  "summary":"The model posts leading scores on agent benchmarks, intensifying competition in automation.",
  "body":["Stronger tool use and multi-step task performance push the frontier of what coding and computer-use agents can do reliably.","Rivals are expected to respond quickly as enterprises evaluate agentic workflows."],
  "sources":[("unrot.co","https://unrot.co/blogs/ai-news-today-june-15-2026")]},
 {"sub":"Chinese AI Ecosystem",
  "h3":"Beijing requires approval for Alibaba and DeepSeek researcher travel",
  "summary":"China extended a nuclear-era control to its top AI talent.",
  "body":["Researchers at leading firms now need state sign-off before overseas trips, aimed at preventing talent and know-how outflow.","The step reflects how strategic Beijing now views frontier AI capability."],
  "sources":[("TechTimes","https://www.techtimes.com/articles/317325/20260528/china-ai-travel-curbs-reach-alibaba-deepseek-private-sector-researchers-need-beijing-approval.htm")]},
 {"h3":"Stanford AI Index puts US-China capability gap at 2.7 percent",
  "summary":"The 2026 edition shows the gap narrowing to near parity on key measures.",
  "body":["The slim margin underscores how quickly Chinese labs have closed ground, sharpening the strategic stakes for both governments.","The finding frames much of the current export-control and talent policy on both sides."],
  "sources":[("TechTimes","https://www.techtimes.com/articles/317325/20260528/china-ai-travel-curbs-reach-alibaba-deepseek-private-sector-researchers-need-beijing-approval.htm")]},
 {"sub":"Enterprise & Regulation",
  "h3":"US orders Anthropic to cut foreign-national access to top models",
  "summary":"A government directive told the company to suspend its most capable models for foreign nationals.",
  "body":["The order treats frontier models as controlled strategic capabilities, extending export-style thinking from chips to software.","It lands amid broader curbs on advanced AI chips reaching Chinese-headquartered firms."],
  "sources":[("Euronews","https://www.euronews.com/news/international")]},
 {"h3":"Anthropic warns a Pentagon ban could cost it billions",
  "summary":"The company flagged material revenue at risk from a potential defence-sector restriction.",
  "body":["The disclosure highlights how dependent leading labs are becoming on large government and enterprise contracts.","It also shows the regulatory crosscurrents facing firms that straddle commercial and national-security work."],
  "sources":[("Yahoo Finance","https://finance.yahoo.com/news/live/tech-stocks-today-anthropic-says-pentagon-ban-could-cost-it-billions-meta-announces-new-ai-chips-134456659.html")]},
],
"crypto-macro": [
 {"hero":True,"sub":"Macro & Central Banks",
  "h3":"Fed set to hold as Warsh chairs his first meeting, decision today",
  "summary":"Markets price a near-certain hold at 3.50 to 3.75 percent, with the decision and new projections at 2pm ET.",
  "body":["The FOMC is widely expected to keep rates unchanged in Kevin Warsh's debut as chair, with traders watching the dot plot and his first press conference for signals on the timing of any 2026 cut.","Sticky inflation and a resilient labour market have kept the committee in wait-and-see mode since late 2025."],
  "sources":[("StockTitan","https://www.stocktitan.net/articles/fed-rate-decision-june-17-2026"),("CBS News","https://www.cbsnews.com/news/federal-reserve-interest-rates-kevin-warsh-june-2026/")]},
 {"h3":"May CPI at 4.2 percent keeps the Fed cautious",
  "summary":"Energy-driven price pressure lifted headline inflation, reinforcing the case for no cut.",
  "body":["Consumer prices rose 4.2 percent year over year in May, pushed up by energy costs tied to the spring conflict, with unemployment near 4.4 percent.","The combination has cemented expectations that policymakers will wait for clearer disinflation before easing."],
  "sources":[("IndexBox","https://www.indexbox.io/blog/fed-holds-rates-as-inflation-hits-42-warshs-first-fomc-press-conference-in-focus/")]},
 {"h3":"Oil sinks below $80 after the US-Iran deal",
  "summary":"Crude fell sharply on expectations of restored Gulf supply, easing inflation pressure.",
  "body":["The memorandum to reopen the Strait of Hormuz pulled oil down on supply-relief bets, improving the macro backdrop for risk assets.","Lower energy costs feed through to softer headline inflation, a tailwind the Fed will weigh against still-firm core readings."],
  "sources":[("TheStreet","https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-16-2026")]},
 {"h3":"US stocks mixed as tech drags into the Fed decision",
  "summary":"The Dow rose while the Nasdaq and S&P 500 wavered ahead of the rate call.",
  "body":["Investors trimmed risk in megacap tech while cyclicals held up, leaving the major indexes little changed before the FOMC.","Positioning stayed cautious with the dot plot and Warsh's tone set to drive the next move."],
  "sources":[("TheStreet","https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-16-2026")]},
 {"sub":"Bitcoin & Ethereum",
  "h3":"Bitcoin holds near $66k into Fed day",
  "summary":"BTC traded around $66,000, steadying after a volatile June.",
  "body":["The market is treating the FOMC as the key near-term catalyst, with a dovish tone seen opening room toward $68,500 and a hawkish surprise risking a slide to the low $60,000s.","Improved geopolitics and softer oil offered some support."],
  "sources":[("blockchainreporter","https://blockchainreporter.net/bitcoin-price-today-btc-holds-66k-as-the-feds-big-day-arrives-and-warsh-takes-over/")]},
 {"h3":"Ethereum near $1,790 and the year's only major in the green",
  "summary":"ETH traded up about 1.8 percent and is up roughly 44 percent in 2026, bucking a broad sell-off.",
  "body":["Ether's relative strength stands out against double-digit declines elsewhere, with bitcoin down about 26 percent and XRP down nearly 38 percent year to date.","Traders point to staking and ETF flows as part of the divergence."],
  "sources":[("Yahoo Finance","https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-tuesday-june-16-2026-highest-opening-values-in-two-weeks-113313567.html")]},
 {"h3":"Key bitcoin support sits at $64,350 then $60,630",
  "summary":"Analysts flag those levels as the line in the sand on a hawkish Fed.",
  "body":["A break of $64,350 would put the low-$60,000s region in play, while a hold and dovish signal could push price back above $67,000.","Volatility is expected to spike around the decision and press conference."],
  "sources":[("blockchainreporter","https://blockchainreporter.net/crypto-market-today-june-16-2026-bitcoin-66340-fomc-xrp-etf-hyperliquid/")]},
 {"sub":"DeFi & Altcoins",
  "h3":"XRP ETF chatter and Hyperliquid activity in focus",
  "summary":"Product speculation and on-chain venue activity featured in the day's altcoin scan.",
  "body":["Market notes flagged renewed interest around an XRP exchange-traded product and continued attention on Hyperliquid as traders position around the macro event.","Altcoin breadth stayed weak with most majors negative on the year."],
  "sources":[("blockchainreporter","https://blockchainreporter.net/crypto-market-today-june-16-2026-bitcoin-66340-fomc-xrp-etf-hyperliquid/")]},
 {"sub":"Regulation & Policy",
  "h3":"Geopolitics framed June's crypto swings",
  "summary":"Analysts tie the month's pullback and recovery to the Fed, Iran and large holders.",
  "body":["The June drawdown was attributed to Fed uncertainty, the Iran conflict and selling pressure from big holders, with the subsequent steadying linked to de-escalation and easing oil.","Direction from here hinges heavily on the rate path Warsh signals."],
  "sources":[("Bitget","https://www.bitget.com/news/detail/12560605448772")]},
 {"h3":"Warsh debut watched for the 2026 rate-cut timeline",
  "summary":"Investors want to know whether the first cut slips into 2027 or a September window stays open.",
  "body":["The new chair's framing of the inflation and labour balance will shape expectations across rates, equities and crypto.","A repricing of cut odds in either direction would ripple quickly through risk assets."],
  "sources":[("Mitrade","https://www.mitrade.com/au/insights/others/cfd-trading/fed-interest-rate-decision-2026")]},
],
"mental-health": [
 {"hero":True,"sub":"Research & Studies",
  "h3":"APA survey: 77 percent of psychologists say patients report using AI",
  "summary":"More than a third say patients are using AI as an additional mental health provider.",
  "body":["The APA 2026 Chatbots and Mental Health Survey found near-ubiquitous patient AI use, with a sizeable share treating chatbots as a supplementary source of support alongside human care.","Clinicians are urged to ask about AI use directly and help patients use it safely."],
  "sources":[("APA","https://www.apa.org/topics/artificial-intelligence-machine-learning/discussing-ai-use-therapy")]},
 {"h3":"Randomised trial tests Therabot for depression and anxiety",
  "summary":"An expert fine-tuned chatbot was studied in adults with significant symptoms.",
  "body":["The trial enrolled adults with major depressive disorder, generalised anxiety or high eating-disorder risk to assess whether a purpose-built chatbot can deliver measurable benefit.","Results add to a thin but growing evidence base on clinical-grade conversational tools."],
  "sources":[("NEJM AI","https://ai.nejm.org/doi/full/10.1056/AIoa2400802")]},
 {"h3":"Early data flags potential harms among psychiatric patients",
  "summary":"A large service-system study reports concerning outcomes from chatbot use in vulnerable patients.",
  "body":["Researchers describe cases where general chatbots missed context or reinforced unhealthy coping, underscoring risks for people with serious mental illness.","The authors call for guardrails and clinician oversight rather than unsupervised use."],
  "sources":[("medRxiv","https://www.medrxiv.org/content/10.1101/2025.11.19.25340580.full.pdf")]},
 {"h3":"Clinicians weigh the risks and benefits of generative AI",
  "summary":"A qualitative study captures mixed clinician views on chatbots in care.",
  "body":["Practitioners see promise for access and between-session support but worry about safety, accuracy and over-reliance.","Most favour AI as an adjunct under human supervision rather than a replacement."],
  "sources":[("PMC","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12158938/")]},
 {"h3":"Patients see potential but prefer humans in the loop",
  "summary":"Survey work finds openness to AI agents paired with a clear preference for human oversight.",
  "body":["Respondents value convenience and lowered barriers but want a clinician involved, especially for higher-risk situations.","The findings point to hybrid models rather than fully autonomous tools."],
  "sources":[("PMC","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11826059/")]},
 {"sub":"Tools & Applications",
  "h3":"General chatbots may now be the largest source of emotional support",
  "summary":"A clinical psychologist argues mainstream assistants are widely used for mental health.",
  "body":["Tools like ChatGPT, Gemini and Claude are reportedly used by huge numbers of people for anxiety, stress, loss and relationships, often outside any clinical setting.","Experts warn the scale outpaces the evidence and the safeguards."],
  "sources":[("JAMA","https://jamanetwork.com/journals/jama/fullarticle/2843812")]},
 {"h3":"Fortune: chatbots are becoming mental health tools before they are ready",
  "summary":"Reporting highlights the gap between rapid adoption and clinical validation.",
  "body":["The piece documents how quickly people lean on chatbots for support while regulation and evidence lag behind.","It echoes clinician calls for clearer standards and crisis safeguards."],
  "sources":[("Fortune","https://fortune.com/2026/05/12/chatbots-are-becoming-mental-health-tools-before-they-are-ready/")]},
 {"h3":"APA issues guidance on discussing AI use in therapy",
  "summary":"The association published advice for clinicians on talking with patients about chatbots.",
  "body":["The guidance encourages open, nonjudgemental conversations about how and why patients use AI, and how to keep that use safe.","It positions clinicians to steer rather than ignore a now-common behaviour."],
  "sources":[("APA","https://www.apa.org/topics/artificial-intelligence-machine-learning/discussing-ai-use-therapy")]},
],
"sports": [
 {"hero":True,"sub":"Football",
  "h3":"World Cup: France beat Senegal 3-1 in the group stage",
  "summary":"France opened strongly as the expanded tournament's group games rolled on.",
  "body":["Les Bleus controlled the match to take three points, one of the headline results on a packed June 16 schedule across North American venues.","The win sets an early marker as favourites navigate the longer group phase."],
  "sources":[("Olympics.com","https://www.olympics.com/en/news/fifa-world-cup-2026-every-match-group-result-tuesday-16-june-live-scores")]},
 {"h3":"Argentina, Austria and Iraq feature in June 16 fixtures",
  "summary":"A full slate included Argentina against Algeria and Austria against Jordan.",
  "body":["The day's later kickoffs added to a dense early-tournament calendar as more groups got under way.","Holders and contenders alike began feeling out the expanded format."],
  "sources":[("Yahoo Sports","https://sports.yahoo.com/soccer/article/2026-world-cup-winners-schedule-teams-fixtures-results-how-to-watch-050724826.html")]},
 {"sub":"Tennis",
  "h3":"Queen's Club: De Minaur top seed as Draper and Alcaraz withdraw",
  "summary":"The grass ATP 500 lost two marquee names before play.",
  "body":["Alex de Minaur headlines the field with Jiri Lehecka and Tommy Paul among the seeds, after home favourite Jack Draper and Carlos Alcaraz pulled out.","The draw reshapes the pre-Wimbledon pecking order on grass."],
  "sources":[("khelnow","https://khelnow.com/tennis/schedule-queens-club-championships-202606-2")]},
 {"h3":"Halle Open: Zverev and Medvedev advance",
  "summary":"The top seed and a former major champion moved into the second round.",
  "body":["Home favourite Alexander Zverev progressed alongside Daniil Medvedev at the German grass 500, keeping the headliners on track.","Both eye momentum ahead of Wimbledon."],
  "sources":[("ATP Tour","https://www.atptour.com/en/news/halle-2026-results")]},
 {"h3":"Grass swing sets the stage for Wimbledon",
  "summary":"Queen's, Halle, Berlin and Nottingham frame the run-in to the Championships.",
  "body":["The cluster of grass events gives players limited time to adapt before the year's third major.","Form on the surface often reshuffles seeding expectations quickly."],
  "sources":[("Tennis Connected","https://tennisconnected.com/atp-wta-grass-court-swing-preview-2026-queens-club-halle-berlin-nottingham-set-the-stage-for-wimbledon/")]},
 {"sub":"Formula 1",
  "h3":"Antonelli leads the title race after winning in Canada",
  "summary":"Kimi Antonelli holds the championship lead following a dramatic Montreal victory.",
  "body":["Antonelli won a chaotic Canadian Grand Prix ahead of Lewis Hamilton and Max Verstappen, while George Russell retired with a power-unit issue.","The result extended Antonelli's advantage as the season moved on."],
  "sources":[("Formula1.com","https://www.formula1.com/en/latest/article/antonelli-wins-dramatic-canadian-grand-prix-as-russell-retires-amid-thrilling-mercedes-battle.MzvclJaqCidlYMUXonuDq")]},
 {"sub":"Sailing",
  "h3":"SailGP heads to Halifax for the Canada Grand Prix",
  "summary":"The foiling championship races at Halifax on June 20 and 21.",
  "body":["The fleet of national teams continues its global series on Canada's Atlantic coast in the next round.","Points remain tight near the top of the season standings."],
  "sources":[("World Sailing","https://www.sailing.org/2025/06/27/sailgp-2026-season-dates-and-venues-confirmed/")]},
 {"sub":"Eredivisie",
  "h3":"Paul Wanner joins PSV from Bayern Munich",
  "summary":"The 19-year-old attacking midfielder moves to Eindhoven.",
  "body":["Wanner's transfer adds a highly rated young creator to PSV as Dutch clubs reshape squads for next season.","It marks a notable arrival in the Eredivisie's summer market."],
  "sources":[("Tribuna","https://tribuna.com/en/league/eredivisie/transfers/")]},
 {"h3":"Marko Pjaca signs for Twente",
  "summary":"The winger joined on a two-year deal after leaving Dinamo Zagreb.",
  "body":["Pjaca arrives in Enschede on a free after terminating his Zagreb contract, adding experience to Twente's attack.","The deal is part of an active early window for Dutch sides."],
  "sources":[("Tribuna","https://tribuna.com/en/league/eredivisie/transfers/")]},
],
"consumer-tech": [
 {"hero":True,"sub":"Software & Services",
  "h3":"WWDC 2026: Apple previews iOS 27 and a Gemini-powered Siri",
  "summary":"Apple unveiled new software platforms and a more conversational Siri built on Google's Gemini.",
  "body":["At its developer conference Apple previewed iOS 27, macOS 27 and companion platform updates due in the autumn, headlined by a revamped, more capable Siri.","The Gemini partnership signals Apple leaning on a partner model to close its assistant gap."],
  "sources":[("TechRadar","https://www.techradar.com/news/live/apple-wwdc-2026-live"),("Tom's Guide","https://www.tomsguide.com/tech-events/apples-wwdc-2026-conference-kicks-off-in-june-heres-what-we-expect-to-see")]},
 {"h3":"Siri turns more conversational under the hood",
  "summary":"The assistant is set to become more detailed and engaging across devices.",
  "body":["Apple framed the new Siri as a major step up in natural interaction, integrated across its operating systems.","Wider Apple Intelligence features expand alongside it."],
  "sources":[("Tom's Guide","https://www.tomsguide.com/tech-events/apples-wwdc-2026-conference-kicks-off-in-june-heres-what-we-expect-to-see")]},
 {"h3":"New Apple operating systems arrive in the autumn",
  "summary":"iOS 27, macOS 27 and the rest preview now and ship later this year.",
  "body":["Following the developer-conference reveal, public releases of the platform updates are expected in September.","Developers get the summer to adapt apps to the new features."],
  "sources":[("MacRumors","https://www.macrumors.com/roundup/wwdc/")]},
 {"sub":"Devices & Launches",
  "h3":"iPhone 18 Pro, a foldable iPhone and camera AirPods due in September",
  "summary":"Apple's hardware wave is set for the autumn rather than WWDC.",
  "body":["Reports point to an iPhone 18 Pro, Apple's first foldable iPhone and AirPods with cameras arriving later in the year.","WWDC stayed a software-focused event as expected."],
  "sources":[("MacRumors","https://www.macrumors.com/guide/upcoming-apple-products/")]},
 {"h3":"Samsung's Galaxy S26 line is already shipping",
  "summary":"The flagship S26 series and midrange A-series launched earlier this year.",
  "body":["Samsung's 2026 flagship lineup is on shelves, with attention now turning to its summer foldables.","The S26 Ultra carries Qualcomm's latest mobile silicon."],
  "sources":[("SammyGuru","https://sammyguru.com/samsung-2026-roadmap-upcoming-galaxy-devices/")]},
 {"h3":"Galaxy Z Fold 8 and Flip 8 expected in late July",
  "summary":"Samsung's next foldables are tipped for an event around July 22 in London.",
  "body":["Leaks point to a wider-body Galaxy Z Fold 8 and a Flip 8 powered by Qualcomm's newest chip.","The launch would line them up against Google's foldable."],
  "sources":[("SamMobile","https://www.sammobile.com/news/samsung-galaxy-z-fold-8-everything-to-know/")]},
 {"h3":"Google Pixel foldable lines up against Samsung",
  "summary":"The Pixel 11 Pro Fold is set to challenge the Galaxy Z Fold 8 this year.",
  "body":["Google's 2026 foldable strategy aims to push harder in a maturing premium segment.","The head-to-head sharpens competition in big-screen phones."],
  "sources":[("Tom's Guide","https://www.tomsguide.com/phones/samsung-galaxy-z-fold-8-vs-google-pixel-11-pro-fold-which-android-foldable-will-win-in-2026")]},
 {"h3":"Meta announces new in-house AI chips",
  "summary":"Custom silicon aims to power Meta's AI features and cut accelerator costs.",
  "body":["The chips target Meta's growing on-device and data-centre AI needs.","It is the latest move by a big platform to control its own silicon stack."],
  "sources":[("Yahoo Finance","https://finance.yahoo.com/news/live/tech-stocks-today-anthropic-says-pentagon-ban-could-cost-it-billions-meta-announces-new-ai-chips-134456659.html")]},
 {"sub":"EVs & Mobility",
  "h3":"Tesla develops a smaller, cheaper EV after shelving the Model 2",
  "summary":"Tesla is reportedly working on a new compact, lower-cost car.",
  "body":["The effort signals a renewed search for a volume-driving affordable model amid intensifying competition.","Details remain thin but the project underscores pressure to broaden the lineup."],
  "sources":[("Electrek","https://electrek.co/2026/04/09/tesla-reportedly-developing-new-smaller-cheaper-ev-after-killing-model-2/")]},
 {"h3":"Tesla Model 3 named the most efficient EV",
  "summary":"The Model 3 topped an efficiency ranking, reinforcing its value case.",
  "body":["Strong efficiency keeps the Model 3 competitive on running costs as rivals expand their ranges.","Efficiency is an increasingly central selling point as buyers watch energy prices."],
  "sources":[("Not a Tesla App","https://www.notateslaapp.com/news/4290/tesla-model-3-named-most-efficient-ev-by-edmunds")]},
],
}

MOOD = {"h3":"Sfeer vandaag","p":"Vroege zomer met een zucht verlichting: an early summer that swings between an exceptional heatwave and the relief of cooler air, while the Jetten minority cabinet juggles asylum, housing and the new EU migration pact. Markets and households exhale as oil eases and a US-Iran deal holds, and World Cup nights plus grass-court tennis lift the mood even as inflation near 3.4 percent keeps one eye on prices."}

def esc_attr(s):
    return html.escape(s, quote=True)

def render_card(item):
    body_html = "".join("<p>%s</p>" % html.escape(p) for p in item["body"])
    sources_json = json.dumps([{"name":n,"url":u} for n,u in item["sources"]])
    pills = "".join('<span class="source-pill">%s</span>' % html.escape(n) for n,_ in item["sources"])
    cls = "hero-card" if item.get("hero") else "card"
    inner = "hero-body" if item.get("hero") else "card-body"
    return ('<div class="%s" data-title="%s" data-body="%s" data-sources="%s">'
            '<div class="%s"><h3>%s</h3><p>%s</p><div class="meta">%s</div></div></div>') % (
        cls, esc_attr(item["h3"]), esc_attr(body_html), esc_attr(sources_json),
        inner, html.escape(item["h3"]), html.escape(item["summary"]), pills)

def render_section(sid, name, accent):
    items = DATA[sid]
    parts = []
    last_sub = None
    for it in items:
        if it.get("sub") and it["sub"] != last_sub:
            parts.append('<div class="subsection-label">%s</div>' % html.escape(it["sub"]))
            last_sub = it["sub"]
        parts.append(render_card(it))
    grid = "".join(parts)
    if sid == "netherlands":
        mood = '<div class="mood-box"><h3>%s</h3><p>%s</p></div>' % (html.escape(MOOD["h3"]), html.escape(MOOD["p"]))
        grid = mood + grid
    header = ('<div class="section-header"><div class="accent" style="background:%s"></div>'
              '<h2>%s</h2><span class="count">%d stories</span></div>') % (accent, html.escape(name), len(items))
    return '<section class="section" id="%s">%s<div class="news-grid">%s</div></section>' % (sid, header, grid)

sidebar = "".join('<a href="#%s">%s</a>' % (sid, html.escape(name)) for sid,name,_ in SECTIONS)
sections_html = "".join(render_section(sid, name, accent) for sid,name,accent in SECTIONS)

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>The Daily Brief - %s</title>
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%%3E%%3Crect width='32' height='32' rx='6' fill='%%231a1a1a'/%%3E%%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='14' font-weight='bold' fill='%%23fff' text-anchor='middle'%%3EDB%%3C/text%%3E%%3C/svg%%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#faf9f6;color:#1a1a1a;line-height:1.6}
.masthead{position:relative;text-align:center;padding:2.5rem 1.2rem 1.5rem;border-bottom:3px solid #1a1a1a;margin-bottom:0}
.masthead h1{font-family:'Newsreader',serif;font-size:3rem;letter-spacing:0.15em;font-weight:700}
.masthead .date{font-size:0.95rem;color:#555;margin-top:0.3rem}
.masthead .tagline{font-family:'Newsreader',serif;font-style:italic;color:#777;margin-top:0.2rem;font-size:1rem}
.date-nav{position:absolute;left:1.2rem;top:50%%;transform:translateY(-50%%);display:flex;align-items:center;gap:0.4rem}
.date-nav button{background:none;border:1px solid #ccc;border-radius:6px;width:32px;height:32px;cursor:pointer;font-size:1rem;color:#555;display:flex;align-items:center;justify-content:center;transition:all 0.2s}
.date-nav button:hover{background:#f0eeea;border-color:#999}
.date-nav button:disabled{opacity:0.3;cursor:default}
.date-nav input[type='date']{font-family:'Inter',sans-serif;font-size:0.82rem;border:1px solid #ccc;border-radius:6px;padding:0.3rem 0.5rem;background:#fff;color:#333;cursor:pointer}
@media(max-width:768px){.date-nav{position:static;transform:none;justify-content:center;margin-bottom:0.5rem}}
.tab-bar{display:flex;justify-content:center;gap:0;border-bottom:3px solid #1a1a1a;background:#f5f4f0}
.tab-bar a{display:inline-block;padding:0.7rem 2rem;font-family:'Inter',sans-serif;font-size:0.9rem;font-weight:600;color:#777;text-decoration:none;border-bottom:3px solid transparent;margin-bottom:-3px;transition:all 0.2s}
.tab-bar a:hover{color:#1a1a1a;background:#eae8e3}
.tab-bar a.active{color:#1a1a1a;border-bottom-color:#1a1a1a}
.layout{display:flex;max-width:1400px;margin:0 auto;padding:0 1rem}
.sidebar{position:sticky;top:1rem;height:fit-content;width:220px;min-width:220px;padding-right:1.5rem;display:none}
@media(min-width:1200px){.sidebar{display:block}}
.sidebar nav a{display:block;padding:0.45rem 0.8rem;color:#555;text-decoration:none;font-size:0.82rem;border-left:3px solid transparent;transition:all 0.2s;margin-bottom:0.15rem;border-radius:0 4px 4px 0}
.sidebar nav a:hover{color:#1a1a1a;background:#f0eeea;border-left-color:#999}
.sidebar nav a.active{color:#1a1a1a;font-weight:600;border-left-color:#1a1a1a}
.main{flex:1;min-width:0;padding-bottom:4rem}
.content{flex:1;min-width:0;padding-bottom:4rem}
.section{margin-bottom:3rem}
.section-header{display:flex;align-items:center;gap:0.8rem;margin-bottom:1.5rem;padding-bottom:0.6rem;border-bottom:3px solid #1a1a1a}
.section-header .accent{width:6px;height:36px;border-radius:3px}
.section-header h2{font-family:'Newsreader',serif;font-size:1.7rem;font-weight:700}
.section-header .count{font-size:0.75rem;color:#888;margin-left:auto;white-space:nowrap}
.news-grid{column-count:3;column-gap:1.1rem}
@media(max-width:1024px){.news-grid{column-count:2}}
@media(max-width:640px){.news-grid{column-count:1}}
.subsection-label{column-span:all;font-family:'Newsreader',serif;font-size:1.15rem;font-weight:600;color:#444;margin:1.2rem 0 0.8rem;padding-bottom:0.3rem;border-bottom:1px solid #ddd}
.subsection-label:first-child{margin-top:0}
.card,.hero-card{break-inside:avoid;display:inline-block;width:100%%;background:#fff;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,0.06);margin-bottom:1.1rem;overflow:hidden;cursor:pointer;transition:all 0.2s;border:1px solid #eee}
.card:hover,.hero-card:hover{box-shadow:0 4px 16px rgba(0,0,0,0.1);transform:translateY(-2px)}
.hero-card{column-span:all}
.hero-card .hero-body{padding:1.2rem 1.5rem}
.hero-card .hero-body h3{font-family:'Newsreader',serif;font-size:1.5rem;margin-bottom:0.4rem}
.hero-card .hero-body p{color:#555;font-size:0.92rem;line-height:1.55}
.hero-card .hero-body .meta{display:flex;align-items:center;gap:0.5rem;margin-top:0.6rem;font-size:0.75rem;color:#888}
.card .card-body{padding:1rem 1.1rem}
.card .card-body h3{font-family:'Newsreader',serif;font-size:1.1rem;margin-bottom:0.3rem;line-height:1.3}
.card .card-body p{color:#555;font-size:0.85rem;line-height:1.5}
.card .card-body .meta{display:flex;align-items:center;gap:0.5rem;margin-top:0.5rem;font-size:0.72rem;color:#888}
.source-pill{display:inline-block;padding:0.15rem 0.5rem;background:#f0eeea;border-radius:12px;color:#555;text-decoration:none;font-size:0.7rem;transition:background 0.2s}
.source-pill:hover{background:#e0ddd8}
.mood-box{column-span:all;background:linear-gradient(135deg,#ffecd2,#fcb69f);border-radius:10px;padding:1.2rem 1.5rem;margin-bottom:1.1rem;border:none;box-shadow:0 1px 4px rgba(0,0,0,0.06)}
.mood-box h3{font-family:'Newsreader',serif;font-size:1.1rem;margin-bottom:0.3rem}
.mood-box p{font-size:0.88rem;color:#444}
.modal-overlay{display:none;position:fixed;top:0;left:0;width:100%%;height:100%%;background:rgba(0,0,0,0.6);z-index:1000;justify-content:center;align-items:center;padding:1rem}
.modal-overlay.active{display:flex}
.modal-content{background:#fff;border-radius:12px;max-width:680px;width:100%%;max-height:85vh;overflow-y:auto;padding:2rem;position:relative}
.modal-content h2{font-family:'Newsreader',serif;font-size:1.6rem;margin-bottom:0.8rem;line-height:1.3}
.modal-content .modal-body{font-size:0.92rem;color:#333;line-height:1.7}
.modal-content .modal-body p{margin-bottom:0.8rem}
.modal-content .modal-sources{margin-top:1.2rem;padding-top:0.8rem;border-top:1px solid #eee}
.modal-content .modal-sources a{display:inline-block;margin:0.2rem 0.3rem 0.2rem 0;padding:0.25rem 0.7rem;background:#f0eeea;border-radius:14px;color:#555;text-decoration:none;font-size:0.78rem;transition:background 0.2s}
.modal-content .modal-sources a:hover{background:#e0ddd8;color:#333}
.modal-close{position:absolute;top:1rem;right:1rem;width:36px;height:36px;border-radius:50%%;border:none;background:#f0eeea;cursor:pointer;font-size:1.2rem;display:flex;align-items:center;justify-content:center;color:#555}
.modal-close:hover{background:#ddd}
.footer{text-align:center;padding:2rem;color:#aaa;font-size:0.75rem;border-top:1px solid #eee}
</style>
</head>
<body>
<div class="masthead">
<div class="date-nav">
<button id="prev-day" aria-label="Previous day">&larr;</button>
<input type="date" id="date-picker" value="%s" min="%s" max="%s">
<button id="next-day" aria-label="Next day" disabled>&rarr;</button>
</div>
<h1>The Daily Brief</h1>
<div class="date">%s</div>
<div class="tagline">A handpicked digest of the day's signal</div>
</div>
<div class="tab-bar">
<a href="index.html" class="active">News</a>
<a href="miner-analytics.html">AI / HPC Analytics</a>
</div>
<div class="layout">
<aside class="sidebar">
<nav>
%s
</nav>
</aside>
<main class="content">
''' % (DATE_HUMAN, DATE_ISO, MIN_ISO, DATE_ISO, DATE_HUMAN, sidebar)

TAIL = '''</main>
</div>
<footer style="text-align:center;padding:2rem 1rem;color:#777;font-size:0.85rem;border-top:1px solid #eee;margin-top:2rem">The Daily Brief - daily news journal - generated automatically</footer>
<script>
const overlay=document.createElement('div');overlay.className='modal-overlay';
overlay.innerHTML='<div class="modal-content"><button class="modal-close" aria-label="Close">&times;</button><h2 id="modal-title"></h2><div class="modal-body" id="modal-body"></div><div class="modal-sources" id="modal-sources"></div></div>';
document.body.appendChild(overlay);
const modalTitle=document.getElementById('modal-title');
const modalBody=document.getElementById('modal-body');
const modalSources=document.getElementById('modal-sources');
function openModal(card){
  modalTitle.textContent=card.dataset.title;
  modalBody.innerHTML=card.dataset.body;
  const sources=JSON.parse(card.dataset.sources||'[]');
  modalSources.innerHTML='<strong style="font-size:0.85rem;color:#444">Sources:</strong><br>'+sources.map(s=>'<a href="'+s.url+'" target="_blank" rel="noopener">'+s.name+'</a>').join(' ');
  overlay.classList.add('active');
}
function closeModal(){overlay.classList.remove('active');}
document.querySelectorAll('.card,.hero-card').forEach(c=>c.addEventListener('click',()=>openModal(c)));
overlay.addEventListener('click',e=>{if(e.target===overlay)closeModal();});
overlay.querySelector('.modal-close').addEventListener('click',closeModal);
document.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal();});
const sections=document.querySelectorAll('.section');
const sideLinks=document.querySelectorAll('.sidebar nav a');
const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){const id=e.target.id;sideLinks.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+id));}});},{rootMargin:'-30%% 0px -60%% 0px'});
sections.forEach(s=>observer.observe(s));
const datePicker=document.getElementById('date-picker');
const prevBtn=document.getElementById('prev-day');
const nextBtn=document.getElementById('next-day');
function navigate(date){window.location.href='journal-'+date+'.html';}
datePicker.addEventListener('change',e=>{navigate(e.target.value);});
prevBtn.addEventListener('click',()=>{
  const d=new Date(datePicker.value);
  d.setDate(d.getDate()-1);
  const iso=d.toISOString().slice(0,10);
  if(iso>='%s')navigate(iso);
});
nextBtn.addEventListener('click',()=>{
  const d=new Date(datePicker.value);
  d.setDate(d.getDate()+1);
  const iso=d.toISOString().slice(0,10);
  if(iso<='%s')navigate(iso);
});
</script>
</body>
</html>''' % (MIN_ISO, DATE_ISO)

out = HEAD + sections_html + TAIL
with open(sys.argv[1] if len(sys.argv)>1 else ("journal-%s.html"%DATE_ISO), "w", encoding="utf-8") as f:
    f.write(out)
total = sum(len(v) for v in DATA.values())
print("wrote %d bytes, %d stories" % (len(out), total))
for sid,name,_ in SECTIONS:
    print("  %s: %d" % (name, len(DATA[sid])))
