#!/usr/bin/env python3
import html, json, sys

DATE_ISO = "2026-06-13"
DATE_HUMAN = "Saturday, June 13, 2026"
PREV_ISO = "2026-06-12"
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
  "h3":"US and Iran said to agree wording on deal to end war",
  "summary":"Pakistan's prime minister said Washington and Tehran have settled the language of an agreement to end their war, with Trump claiming hostilities are over.",
  "body":["Nearly four months after the 2026 Iran war erupted in late February, mediators signalled the two sides had agreed on the wording of a deal to formalise the fragile April ceasefire. Trump said he had cancelled planned strikes, arguing talks were close to a result as Tehran reviewed a proposed US text.","The UN secretary-general warned that escalation continues to reverberate across borders despite the truce, and analysts cautioned that wording is not yet a signed agreement."],
  "sources":[("Al Jazeera","https://www.aljazeera.com/middle-east/"),("UN News","https://news.un.org/en/story/2026/06/1167689")]},
 {"h3":"Lebanon-Israel ceasefire holds but Hezbollah keeps pressure",
  "summary":"A US-brokered truce reached June 4 is holding loosely, though Hezbollah is expected to keep attacking Israeli forces inside Lebanon.",
  "body":["The agreement between the Lebanese government and Israel has reduced cross-border fire, but Hezbollah is likely to keep targeting Israeli positions inside Lebanon while avoiding strikes on northern Israel.","Israel, for its part, looks unlikely to scale back operations, leaving the arrangement closer to a managed standoff than a durable peace."],
  "sources":[("ACLED","https://acleddata.com/update/middle-east-overview-june-2026"),("Al Jazeera","https://www.aljazeera.com/middle-east/")]},
 {"h3":"Russian advances stall as Ukraine logs net territorial gains",
  "summary":"Open-source trackers say Russian forces lost ground over the past four weeks, a sharp reversal from earlier in 2026.",
  "body":["DeepState data for May 12 to June 9 shows Russian forces with a net loss of about one square mile, while ISW-based analysis put losses at roughly 91 square miles over a similar window.","As of June 2 the occupied area stood near 45,118 square miles. Measurements vary by source, but all point to a marked slowdown in Russian momentum."],
  "sources":[("Russia Matters","https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-june-10-2026")]},
 {"h3":"Ukrainian ground drones reshape front-line tactics",
  "summary":"Kyiv's expanding use of unmanned ground vehicles for high-risk missions is changing how both sides fight.",
  "body":["Ukraine has pushed cutting-edge drone technology beyond the air, deploying ground robots for logistics, mining and assault tasks that once cost infantry lives.","Commanders describe the systems as a force multiplier that helps offset Russia's manpower advantage along contested sectors."],
  "sources":[("NPR World","https://www.npr.org/sections/world/")]},
 {"h3":"South Korea's Yoon sentenced to 30 years over drone plot",
  "summary":"Ousted president Yoon Suk Yeol and his former defence minister received 30-year prison terms.",
  "body":["A court found that Yoon ordered drone flights over Pyongyang in 2024 to inflame tensions with North Korea and manufacture a pretext for declaring martial law at home.","The sentence marks one of the harshest reckonings for a former South Korean leader and closes a chapter that convulsed the country's politics."],
  "sources":[("Democracy Now","https://www.democracynow.org/2026/6/10/headlines")]},
 {"h3":"China detains Myanmar-focused analyst on espionage claim",
  "summary":"Beijing said Min Zin, who leads a think tank on Myanmar, was held on suspicion of espionage.",
  "body":["Chinese authorities accused the researcher of engaging in espionage and endangering national security, without releasing detailed evidence.","Rights groups linked the detention to a broader pattern of pressure on independent analysts working on sensitive regional questions."],
  "sources":[("Democracy Now","https://www.democracynow.org/2026/6/10/headlines")]},
 {"sub":"Diplomacy & Trade",
  "h3":"UN chief says Middle East shock is spilling across continents",
  "summary":"Secretary-General warned that the regional crisis is rippling through trade, travel and energy worldwide.",
  "body":["The 2026 conflict disrupted Middle East air travel, forced shipping reroutes away from the Strait of Hormuz and the Red Sea, and pushed energy prices higher.","The UN urged sustained diplomacy, calling the fragile ceasefire insufficient to contain the wider fallout."],
  "sources":[("UN News","https://news.un.org/en/story/2026/06/1167689")]},
 {"h3":"US widens AI chip export curbs to Chinese firms abroad",
  "summary":"Washington said licensing rules for advanced AI chips apply to any company headquartered in China, wherever located.",
  "body":["The Commerce Department clarified that export restrictions cover subsidiaries of Chinese companies operating outside the country, closing a perceived loophole.","Nvidia's top Blackwell GPUs remain banned for China, while a limited H200 channel stays tangled in legal and regulatory limbo."],
  "sources":[("Al Jazeera","https://www.aljazeera.com/economy/2026/6/1/us-says-ban-on-ai-chip-shipments-applies-to-chinese-firms-outside-china")]},
 {"h3":"FIFA tweaks the laws of the game ahead of the World Cup",
  "summary":"Football's governing body introduced several rule changes for the upcoming tournament.",
  "body":["FIFA confirmed adjustments to the laws of soccer designed to speed play and tighten enforcement ahead of the World Cup.","Officials framed the changes as incremental, aimed at consistency rather than wholesale reform."],
  "sources":[("US News World","https://www.usnews.com/news/world")]},
 {"sub":"Humanitarian & Climate",
  "h3":"UN warns of extreme weather as El Nino looms",
  "summary":"The WMO put the odds of an El Nino event between June and August at about 80 percent.",
  "body":["The UN climate agency told governments to brace for intensified heat, drought and flooding as a developing El Nino layers onto record warmth.","Early 2026 already brought wildfires in Chile, a cyclone in Sri Lanka and floods across Brazil, France and Kenya."],
  "sources":[("Al Jazeera","https://www.aljazeera.com/news/2026/6/2/un-tells-world-to-brace-for-extreme-weather-as-el-nino-looms")]},
 {"h3":"Heat set to remain the deadliest climate threat in 2026",
  "summary":"Forecasters expect longer, hotter heat waves across southern Europe, South Asia and the US.",
  "body":["North America has entered its May-to-October danger season with above-average temperatures forecast across much of the country.","Scientists warn the combination of El Nino and the long-term warming trend raises the risk of compounding disasters through the year."],
  "sources":[("Union of Concerned Scientists","https://blog.ucs.org/erika-spanger-siegfried/danger-season-is-here-again-with-triple-the-danger-for-2026/")]},
 {"h3":"Higher US inflation reading rattles global markets",
  "summary":"May CPI of 4.2 percent, the hottest since 2023, kept risk assets on edge.",
  "body":["Energy prices surged amid the Middle East shock, pushing headline inflation up and complicating central-bank plans worldwide.","The print fed expectations that the Federal Reserve would hold rates, with knock-on effects across equities and crypto."],
  "sources":[("Federal Reserve H.15","https://www.federalreserve.gov/releases/h15/")]},
 {"h3":"Scotland faces Haiti in friendly fixture",
  "summary":"Scotland's national team plays Haiti on June 13 as part of pre-tournament preparation.",
  "body":["The match is one of several international friendlies dotting the June calendar as squads fine-tune ahead of major competition.","Coaches are using the window to test depth and combinations before competitive fixtures resume."],
  "sources":[("US News World","https://www.usnews.com/news/world")]},
 {"h3":"Markets digest SpaceX mega-listing aftershocks",
  "summary":"The largest IPO on record reshaped sentiment across tech and risk markets.",
  "body":["SpaceX priced its offering at $135 a share and surged on debut at a valuation near $2 trillion, the biggest public offering ever.","The listing rippled into broader equities, fuelling debate about concentration of wealth and the appetite for outsized tech valuations."],
  "sources":[("Bloomberg","https://www.bloomberg.com/features/2026-spacex-ipo-elon-musk-trillionaire/")]},
 {"h3":"US military build-up in the Middle East persists post-ceasefire",
  "summary":"American forces remain heavily postured in the region despite the truce.",
  "body":["The buildup that accompanied the spring conflict has not unwound, with assets kept in place as a deterrent while talks continue.","Analysts say the footprint reflects low confidence that the ceasefire will hold without external pressure."],
  "sources":[("Wikipedia","https://en.wikipedia.org/wiki/2026_United_States_military_buildup_in_the_Middle_East")]},
 {"h3":"Warren summons Nvidia's Huang over China chip sales",
  "summary":"The senator invited Nvidia's CEO to testify on export controls and the company's China business.",
  "body":["Senator Elizabeth Warren asked Jensen Huang to appear before the Senate Banking Committee on June 11 to address advanced-chip exports.","The hearing underscores rising congressional scrutiny of how US technology reaches Chinese buyers."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/04/nvidia-ceo-jensen-huang-warren-senate-hearing-china-ai-chips.html")]},
],

"netherlands": [
 {"hero":True,"sub":"Politics & Policy",
  "h3":"New Dutch asylum system launches amid reception strain",
  "summary":"The Netherlands is rolling out a reworked asylum system while pressure builds at its main reception centre.",
  "body":["The overhaul arrives as facilities strain under arrivals, and as Italy agrees to begin taking back asylum seekers from the Netherlands under Dublin transfers.","The European Commission has separately told The Hague to drop the extra internal border controls it reintroduced, adding friction to the government's migration agenda."],
  "sources":[("DutchNews.nl","https://www.dutchnews.nl/category/politics/"),("NL Times","https://nltimes.nl/categories/politics")]},
 {"h3":"Cabinet readies new household aid as costs bite",
  "summary":"The government is preparing fresh support for households facing elevated inflation and fuel prices.",
  "body":["Ministers are assembling a package to cushion families against higher energy and living costs driven partly by the Middle East shock.","The measures come as Dutch consumers voice anxiety about purchasing power and the fragility of the international order."],
  "sources":[("DutchNews.nl","https://www.dutchnews.nl/category/politics/")]},
 {"h3":"Brussels orders Netherlands to end extra border checks",
  "summary":"The European Commission told The Hague to stop the additional border controls it imposed.",
  "body":["The Commission said the controls sit uneasily with free-movement rules in the Schengen area and should be wound down.","The instruction puts the Dutch government in a tight spot between EU obligations and its tougher domestic migration stance."],
  "sources":[("NL Times","https://nltimes.nl/categories/politics")]},
 {"h3":"All five Tiel aldermen resign amid criminal allegations",
  "summary":"The entire board of aldermen stepped down in Tiel over allegations of criminal activity.",
  "body":["The mass resignation throws the municipality into political turmoil and forces a scramble to restore governance.","Investigators are examining the allegations while the council works to fill the vacancies."],
  "sources":[("NL Times","https://nltimes.nl/")]},
 {"sub":"Economy & Housing",
  "h3":"DNB expects Dutch house prices to rise about 4 percent",
  "summary":"After an 8.6 percent jump in 2025, price growth is set to cool toward 4 percent in 2026 and 2027.",
  "body":["The central bank projects a slower but still positive trajectory for home prices, easing from last year's surge.","Affordability remains stretched, especially in the Randstad, where supply shortages keep first-time buyers and single earners under pressure."],
  "sources":[("DNB","https://www.dnb.nl/en/current-economic-issues/housing-market/"),("CBS via DutchNews","https://www.dutchnews.nl/2026/01/house-price-growth-continues-to-slow-hits-3-6-in-amsterdam/")]},
 {"h3":"House prices climbing faster in the east than the west",
  "summary":"CBS and Land Registry data show steeper gains in eastern municipalities.",
  "body":["Prices rose in nearly all municipalities, but increases were generally larger in the east of the country than the west.","The pattern points to spillover demand as buyers priced out of the Randstad look further afield."],
  "sources":[("NL Times","https://nltimes.nl/2026/02/11/dutch-home-prices-increasing-faster-east-netherlands-west")]},
 {"h3":"Mortgage lending rebounds above euro-area pace",
  "summary":"Dutch bank mortgage lending is growing robustly again after a temporary dip.",
  "body":["Lending growth has recovered and now runs above the euro-area average, signalling renewed confidence in the housing market.","Economists tie the rebound to resilient incomes and expectations of continued, if slower, price gains."],
  "sources":[("Rabobank","https://www.rabobank.com/knowledge/d011508452-dutch-housing-market-quarterly-no-signs-of-cooling-even-as-supply-grows")]},
 {"h3":"IMF sees Dutch growth slowing to 1.2 percent in 2026",
  "summary":"After 1.9 percent real GDP growth in 2025, the IMF projects a cooler 2026.",
  "body":["The Fund expects Dutch activity to moderate to 1.2 percent this year before edging up to 1.4 percent in 2027.","The economy has shown resilience, but external shocks and weaker external demand weigh on the near-term outlook."],
  "sources":[("Global Property Guide","https://www.globalpropertyguide.com/europe/netherlands/price-history")]},
 {"sub":"Society & Culture",
  "h3":"Off-peak 49-euro travel ticket launches June 24",
  "summary":"A 49-euro pass for unlimited off-peak and weekend public transport runs from June 24 to September 1.",
  "body":["The summer ticket covers trains, buses, trams and metros during off-peak hours and on weekends across the country.","Its launch could collide with a planned strike on June 24 if the cabinet fails to meet union demands, delaying services until 8am."],
  "sources":[("IamExpat","https://www.iamexpat.nl/expat-info/dutch-news/june-2026-7-things-expats-netherlands-need-know")]},
 {"h3":"Dutch voice worry over fraying international legal order",
  "summary":"Surveys show unease about global instability and the Netherlands' resilience.",
  "body":["Citizens expressed concern that the rules-based international system is weakening amid conflict and great-power friction.","The mood reflects a broader anxiety about security and the country's ability to weather external shocks."],
  "sources":[("NL Times","https://nltimes.nl/")]},
],

"ai-hpc": [
 {"hero":True,"sub":"AI/HPC Stocks & Infrastructure",
  "h3":"Texas overtakes Northern Virginia as top data center market",
  "summary":"Texas has become the world's leading primary data center market as AI build-out accelerates.",
  "body":["The shift reflects abundant land and power and a wave of mega-projects, with Nvidia partnering with IREN to deploy up to 5 GW of AI infrastructure and naming Sweetwater a flagship DSX AI-factory site.","Data center construction spending remains more than 300 percent above year-ago levels, and Jensen Huang argued AI infrastructure is now a connectivity challenge as much as a compute one."],
  "sources":[("Data Center Knowledge","https://www.datacenterknowledge.com/data-center-construction/new-data-center-developments-june-2026")]},
 {"h3":"CloudBurst breaks ground on 1.2 GW Texas campus",
  "summary":"A new flagship data center campus in Central Texas underscores the scale of AI demand.",
  "body":["CloudBurst Data Centers started construction on a 1.2 GW campus, one of several gigawatt-class projects reshaping the US power map.","Operators increasingly compete on deployment support and platform control rather than raw chip access."],
  "sources":[("Data Center Knowledge","https://www.datacenterknowledge.com/data-center-construction/new-data-center-developments-june-2026")]},
 {"h3":"Applied Digital plans $3.6B Louisiana AI campus",
  "summary":"Applied Digital will develop a 300-acre AI campus dubbed Delta Forge 1.",
  "body":["The $3.6 billion project adds to a pipeline of large AI-focused builds spreading beyond traditional hubs.","Smaller projects are advancing too, including Prime Data Centers' 18 MW SMF02 facility in Sacramento."],
  "sources":[("Data Center Knowledge","https://www.datacenterknowledge.com/data-center-construction/new-data-center-developments-june-2026")]},
 {"h3":"AI data center boom collides with US water limits",
  "summary":"Cooling demands are straining water supplies in fast-growing data center regions.",
  "body":["The rush to build is running into local water constraints, forcing operators to rethink cooling and siting.","Water availability is emerging as a binding constraint alongside power in the AI infrastructure race."],
  "sources":[("ConstructConnect","https://news.constructconnect.com/ai-data-center-boom-is-running-into-americas-water-problem")]},
 {"sub":"Foundation Models & Releases",
  "h3":"June model wave: Gemini 3.5 Pro, Claude Sonnet 4.8, Grok 5",
  "summary":"Four major model storylines are landing this month across Google, Anthropic and xAI.",
  "body":["Google's Gemini 3.5 Pro, Anthropic's Claude Mythos 1, a rumoured Claude Sonnet 4.8 and the long-delayed Grok 5 are all expected in June.","Gemini 3.5 Flash already went GA at Google I/O on May 19 and is the default in the Gemini app and AI Mode in Search."],
  "sources":[("LLM Stats","https://llm-stats.com/ai-news"),("WaveSpeed","https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/")]},
 {"h3":"Anthropic files confidentially for IPO after $65B round",
  "summary":"Anthropic submitted a draft registration statement following a valuation near $965 billion.",
  "body":["The confidential filing follows a $65 billion Series H that valued the company above OpenAI on some measures.","OpenAI is reported to be preparing its own confidential filing, with a listing possible as soon as September 2026."],
  "sources":[("LLM Stats","https://llm-stats.com/llm-updates")]},
 {"h3":"Microsoft Foundry catalog tops 11,000 models",
  "summary":"Microsoft's model catalog now spans frontier closed-weight systems from OpenAI, Anthropic and Google.",
  "body":["The catalog includes GPT-5.5, Claude Opus 4.8, Sonnet 4.5 and Haiku 4.5, and Google's Gemini lineup.","The breadth highlights how cloud platforms are positioning as neutral marketplaces for frontier and open models alike."],
  "sources":[("Build Fast with AI","https://www.buildfastwithai.com/blogs/ai-news-today-june-8-2026")]},
 {"sub":"Chinese AI Ecosystem",
  "h3":"China races to triple domestic AI chip output in 2026",
  "summary":"Chinese chipmakers aim to triple production to cut reliance on Nvidia.",
  "body":["Developers are optimising models for homegrown silicon, with MiniMax, Kimi and DeepSeek's V4 compatible with local chips rather than CUDA.","Huawei is ramping production to fill share Nvidia is ceding under tightening export rules."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/01/china-learns-to-build-without-nvidia.html"),("TipRanks","https://www.tipranks.com/news/the-fly/china-looks-to-triple-its-output-of-ai-chips-in-2026-ft-reports-thefly")]},
 {"h3":"Nvidia restarts H200 output for China amid legal limbo",
  "summary":"Nvidia has purchase orders for H200 chips from Chinese buyers but no deliveries yet.",
  "body":["Commerce cleared about 10 Chinese firms to buy H200 chips, capped at 75,000 units each, but shipments are stalled by ongoing legal and regulatory uncertainty.","The standoff leaves both Nvidia and Chinese customers in limbo as Beijing tightens its own supply-chain rules."],
  "sources":[("CNBC","https://www.cnbc.com/2026/05/14/china-ai-chips-nvidia.html")]},
 {"sub":"Agents & Automation",
  "h3":"Enterprises pivot from 'are agents real' to 'what gets agentized'",
  "summary":"June marks a shift in how companies talk about AI agents, treating them as an operating model.",
  "body":["Consultancies are framing agents as a new way to organise work rather than a side tool, legitimising them for boards.","Developer platforms are closing the gap between assistants and agents that generate, debug and refactor code."],
  "sources":[("StartupHub.ai","https://www.startuphub.ai/ai-news/insights/2026/ai-coding-agents-daily-2026")]},
 {"h3":"Coding agents move to long-running autonomous workflows",
  "summary":"The big 2026 shift is agents operating through execution loops rather than single prompts.",
  "body":["AI coding tools are progressing from autocomplete and AI IDEs to engineered agent workflows that run extended tasks.","GitHub is positioning coding agents as systems that also help with security fixes and refactors."],
  "sources":[("Pragmatic Engineer","https://newsletter.pragmaticengineer.com/p/ai-tooling-2026")]},
 {"h3":"GitHub Copilot switches to usage-based credits",
  "summary":"From June 1 Copilot moved to usage-based billing with AI credits priced at one cent each.",
  "body":["The change ties cost to consumption as agentic features run longer and consume more compute.","It signals a broader move toward metered pricing as AI workloads scale inside developer tools."],
  "sources":[("Faros AI","https://www.faros.ai/blog/best-ai-coding-agents-2026")]},
 {"h3":"Microsoft and Google challenge Anthropic and OpenAI on coding",
  "summary":"The hyperscalers are pushing their own coding-focused models into a crowded field.",
  "body":["Microsoft and Google are sharpening coding models to compete directly with Anthropic and OpenAI's developer offerings.","The contest is intensifying as coding becomes a flagship proving ground for agentic capability."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html")]},
 {"sub":"Enterprise & Regulation",
  "h3":"Apple's Gemini-powered Siri opens the iPhone to rival models",
  "summary":"Apple unveiled a revamped Siri built with Google's Gemini and a multi-AI extensions system.",
  "body":["At WWDC, Apple detailed Apple Foundation Models on Cloud, built with Google and running on Nvidia GPUs in Google's cloud, plus an extensions system that makes Claude an iPhone option for the first time.","Apple also named John Ternus to succeed Tim Cook as CEO, with Cook moving to executive chairman on September 1."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html")]},
 {"h3":"Vendors shift from chasing chips to engineering systems",
  "summary":"The data center fight is moving to full-stack platforms and operations at scale.",
  "body":["Operators are grappling with power constraints, supply-chain risk and early signs of compute-price normalisation.","Differentiation is increasingly about deployment support, infrastructure management and software services."],
  "sources":[("Data Center Knowledge","https://www.datacenterknowledge.com/next-gen-data-centers/ai-data-centers")]},
 {"h3":"BCG pitches agents as a new operating model for work",
  "summary":"Enterprise consulting is reframing AI agents as central to how companies run.",
  "body":["BCG and peers are positioning agents as a structural change rather than an add-on, aimed at business buyers and boards.","The framing helps move agents from experimentation into budgeted enterprise programs."],
  "sources":[("blog.mean.ceo","https://blog.mean.ceo/ai-agents-news-june-2026/")]},
 {"h3":"AI server market shifts to platform control",
  "summary":"Competition is moving beyond accelerators toward complete platform ownership.",
  "body":["Vendors are differentiating through full-stack AI platforms as customers seek integrated deployment and management.","The trend reflects maturing demand that values operations and software over raw chip supply."],
  "sources":[("RCRTech","https://rcrtech.com/category/ai-infrastructure-news/")]},
 {"h3":"Compute pricing shows early signs of normalising",
  "summary":"After a long squeeze, some segments of AI compute pricing are stabilising.",
  "body":["Operators report early normalisation in compute costs even as overall demand stays elevated.","The shift suggests supply is beginning to catch up in parts of the market, though power remains the gating factor."],
  "sources":[("Data Center Knowledge","https://www.datacenterknowledge.com/data-center-hardware/data-center-hardware-highlights-june-2026")]},
 {"h3":"US affirms chip rules cover Chinese firms wherever based",
  "summary":"Commerce said advanced-chip licensing applies to any China-headquartered company.",
  "body":["The guidance extends export controls to overseas subsidiaries of Chinese firms, tightening enforcement.","It adds pressure on global resellers and cloud providers to verify the ultimate ownership of buyers."],
  "sources":[("Al Jazeera","https://www.aljazeera.com/economy/2026/6/1/us-says-ban-on-ai-chip-shipments-applies-to-chinese-firms-outside-china")]},
 {"h3":"Data Center World spotlights power and cooling limits",
  "summary":"The industry's flagship event centred on the physical limits of AI scale-up.",
  "body":["Sessions focused on power availability, grid interconnects and advanced cooling as the binding constraints on growth.","Operators stressed that siting decisions now hinge as much on energy and water as on connectivity."],
  "sources":[("Data Center Knowledge","https://www.datacenterknowledge.com/build-design/data-center-world-2026-ai-pushes-infrastructure-to-new-limits")]},
 {"h3":"Apple's on-device and cloud model split takes shape",
  "summary":"Apple is splitting AI work between on-device models and a Gemini-built cloud tier.",
  "body":["The AFM Cloud Pro model handles demanding tasks in Google's cloud while lighter work stays on device.","The architecture is Apple's bid to balance privacy framing with frontier-grade capability."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html")]},
],

"crypto-macro": [
 {"hero":True,"sub":"Bitcoin & Ethereum",
  "h3":"Bitcoin and Ether rebound after Trump declares war over",
  "summary":"Crypto rallied on June 12 as Trump claimed the Middle East conflict had ended, lifting risk appetite.",
  "body":["Bitcoin opened around $63,553 on June 12, up 3.4 percent on the day, while Ether opened near $1,672, up 3.2 percent, recovering from a bruising first half of the month.","Earlier in June bitcoin had slid below $66,000 and at one point to its lowest since October 2024, pressured by ETF outflows and the geopolitical shock."],
  "sources":[("Yahoo Finance","https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-june-12-2026-prices-rebound-this-morning-after-trump-claims-war-has-ended-115949042.html")]},
 {"h3":"June sell-off wiped out bitcoin's pre-war gains",
  "summary":"Bitcoin fell nearly 11 percent in the first two weeks of June before stabilising.",
  "body":["A combination of ETF outflows, soured sentiment and rumours of large holders selling drove prices below pre-conflict levels.","The intense market focus on AI investment also drained attention and capital away from crypto."],
  "sources":[("Yahoo Finance","https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-thursday-june-4-2026-bitcoin-prices-plunge-below-pre-war-levels-114549073.html")]},
 {"h3":"Record ETF outflows underline fragile sentiment",
  "summary":"Unprecedented outflows from bitcoin ETFs marked the June downturn.",
  "body":["Bitcoin ETFs recorded more than $1.8 billion in outflows as institutions rotated away from the asset.","The exits compounded price weakness and signalled caution among professional allocators."],
  "sources":[("Investing.com","https://www.investing.com/analysis/us-crypto-regulation-sets-the-stage-for-stablecoins-to-enter-core-finance-in-2026-200672588")]},
 {"sub":"Macro & Central Banks",
  "h3":"Fed seen holding at 3.5-3.75 percent through year-end",
  "summary":"Hot inflation has cemented expectations of a prolonged Fed pause.",
  "body":["May CPI of 4.2 percent, the highest since 2023, reinforced a data-dependent hold, with the effective funds rate near 3.62 percent.","Futures price a gradual rise toward 3.8 percent by late 2026 and near 4 percent by mid-2027 as energy-driven inflation lingers."],
  "sources":[("Federal Reserve H.15","https://www.federalreserve.gov/releases/h15/"),("StreetStats","https://streetstats.finance/rates/fedfunds")]},
 {"h3":"Energy-led inflation delays expected rate cuts",
  "summary":"Geopolitical shocks pushed energy prices up, keeping core inflation above target.",
  "body":["The Middle East conflict lifted oil and gas costs, feeding through to headline inflation and complicating the Fed's path.","Officials are signalling patience, wary of easing into a fresh supply-side price shock."],
  "sources":[("AOL","https://www.aol.com/articles/budget-office-expects-federal-cut-201242760.html")]},
 {"sub":"Regulation & Policy",
  "h3":"SEC's draft plan makes digital assets a top priority",
  "summary":"A new SEC strategic plan names digital assets as its first regulatory objective.",
  "body":["The draft plan for fiscal years 2026-2030 designates digital assets and distributed ledger technology under its leading goal.","The move signals a more structured, less enforcement-first posture toward the sector."],
  "sources":[("The Block","https://www.theblock.co/post/383653/2026-crypto-regulation-outlook")]},
 {"h3":"GENIUS Act stablecoin rules due by mid-July",
  "summary":"Federal regulators must issue implementing rules for the stablecoin law by July 18.",
  "body":["The 2025 GENIUS Act was the first comprehensive US stablecoin framework, and its implementing regulations are due no later than July 18, 2026.","Stablecoins topped $250 billion in market cap by end-2025 and accounted for over 30 percent of on-chain transactions."],
  "sources":[("Latham & Watkins","https://www.lw.com/en/us-crypto-policy-tracker/regulatory-developments")]},
 {"h3":"More than 25 banks set to go live on blockchain rails",
  "summary":"SWIFT says over two dozen banks will launch blockchain-based payment processing by June 2026.",
  "body":["The rollout marks traditional banking infrastructure beginning to run on the technology underpinning crypto.","It points to deepening institutional integration even as token prices stay volatile."],
  "sources":[("OpenPR","https://www.openpr.com/news/4534237/crypto-market-news-shows-stablecoin-rules-and-fresh-regulation")]},
 {"sub":"DeFi & Altcoins",
  "h3":"XRP ETFs pass $1.4 billion in cumulative inflows",
  "summary":"Capital is rotating toward newer crypto products even as bitcoin ETFs bleed.",
  "body":["XRP ETFs crossed $1.4 billion in cumulative inflows, a contrast to heavy bitcoin ETF outflows.","The split suggests institutions are diversifying their on-chain exposure rather than exiting entirely."],
  "sources":[("Investing.com","https://www.investing.com/analysis/us-crypto-regulation-sets-the-stage-for-stablecoins-to-enter-core-finance-in-2026-200672588")]},
 {"h3":"Stablecoins push toward core finance under MiCA and GENIUS",
  "summary":"Compliant stablecoins are moving into mainstream payments across major jurisdictions.",
  "body":["The UK, Singapore and the EU's MiCA framework are driving adoption of regulated tokens alongside the US GENIUS Act.","Analysts see 2026 as the year stablecoins enter core financial plumbing rather than crypto niches."],
  "sources":[("Investing.com","https://www.investing.com/analysis/us-crypto-regulation-sets-the-stage-for-stablecoins-to-enter-core-finance-in-2026-200672588")]},
 {"h3":"Crypto regulation becomes a global power contest",
  "summary":"Jurisdictions are competing to set the rules that shape digital-asset flows.",
  "body":["Regulation has turned into a strategic lever as governments vie to attract and govern crypto activity.","The competition is reshaping where firms domicile and how cross-border tokens are treated."],
  "sources":[("Bitcoin Foundation","https://bitcoinfoundation.org/news/regulation/why-crypto-regulation-became-a-global-power-issue-in-2026/")]},
 {"h3":"Strategy-sale rumours add to bitcoin's volatility",
  "summary":"Speculation that a large corporate holder was selling rattled the market.",
  "body":["Rumours that Strategy might be trimming its bitcoin stack amplified the June downdraft.","Such chatter highlights how concentrated holdings can swing sentiment in thin conditions."],
  "sources":[("TradingKey","https://www.tradingkey.com/analysis/cryptocurrencies/btc/261945885-crypto-bitcoin-btc-price-crashing-usd-strategy-fed-tradingkey")]},
 {"h3":"Analysts map bitcoin's key support levels",
  "summary":"With prices breaking technical levels, traders are watching downside support.",
  "body":["After bitcoin sliced through several support zones in June, analysts flagged the next levels that could halt the decline.","The focus on support reflects a market unsure whether the rebound marks a bottom or a pause."],
  "sources":[("TradingKey","https://www.tradingkey.com/analysis/cryptocurrencies/btc/261945885-crypto-bitcoin-btc-price-crashing-usd-strategy-fed-tradingkey")]},
],

"mental-health": [
 {"hero":True,"sub":"Research & Studies",
  "h3":"Youth use of AI chatbots for mental-health advice surges",
  "summary":"A weighted survey estimates 19.2 percent of US youth, around 8.2 million, have sought mental-health advice from AI chatbots.",
  "body":["Use jumped from 13.1 percent in 2024, with 42.8 percent engaging at least monthly and 5.8 percent using the tools daily or near-daily; 91.7 percent found the advice helpful.","Uptake was higher among girls and young women and those aged 18-21, and among youth who had recently discussed mental health with a physician."],
  "sources":[("AJMC","https://www.ajmc.com/view/ai-chatbot-use-for-mental-health-advice-rises-sharply-among-us-youth-with-key-disparities-identified")]},
 {"h3":"Therabot trial tests fine-tuned chatbot for depression and anxiety",
  "summary":"A randomized controlled trial evaluated an expert-fine-tuned generative chatbot for mental-health treatment.",
  "body":["The study enrolled adults with clinically significant major depression, generalized anxiety, or high risk for eating disorders.","It is among the first rigorous trials of a purpose-built therapeutic chatbot, informing debate over clinical efficacy."],
  "sources":[("NEJM AI","https://ai.nejm.org/doi/full/10.1056/AIoa2400802")]},
 {"h3":"Stanford warns AI therapy bots can reinforce stigma",
  "summary":"Researchers found chatbots may be less effective than clinicians and can produce harmful responses.",
  "body":["The Stanford analysis flagged that some bots reinforce stigma toward conditions like schizophrenia and respond unsafely to crisis cues.","The authors urged caution about deploying general-purpose chatbots as substitutes for trained therapists."],
  "sources":[("Stanford HAI","https://hai.stanford.edu/news/exploring-the-dangers-of-ai-in-mental-health-care")]},
 {"h3":"Brown study details ethical risks of ChatGPT as therapist",
  "summary":"A March 2026 study catalogued serious ethical risks when general chatbots act as therapists.",
  "body":["Researchers documented failures around boundaries, confidentiality and crisis handling when general models are used for therapy.","They called for clearer guardrails and disclosure when consumer chatbots are used for emotional support."],
  "sources":[("ScienceDaily","https://www.sciencedaily.com/releases/2026/03/260302030642.htm")]},
 {"sub":"Tools & Applications",
  "h3":"JAMA review weighs millions turning to chatbots for support",
  "summary":"A JAMA piece examined the scale and stakes of AI chatbot use for mental health.",
  "body":["The review noted rapid adoption alongside uneven evidence on safety and effectiveness.","It pressed for standards, oversight and research as usage outpaces regulation."],
  "sources":[("JAMA","https://jamanetwork.com/journals/jama/fullarticle/2843812")]},
 {"h3":"Clinicians favour keeping humans in the loop",
  "summary":"Studies find patients see potential in AI agents but prefer human oversight.",
  "body":["Patients reported value in conversational agents for access and immediacy but wanted clinicians involved in care.","Providers echoed support for hybrid models that pair AI tools with human judgement."],
  "sources":[("NCBI","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11826059/")]},
 {"h3":"Clinicians balance risks and benefits of generative chatbots",
  "summary":"A survey of clinicians mapped where they see upside and danger in chatbot care.",
  "body":["Respondents saw promise in triage and between-session support but worried about accuracy, dependency and crisis response.","The findings point toward cautious, supervised integration rather than wholesale adoption."],
  "sources":[("NCBI","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12158938/")]},
 {"h3":"Qualitative work captures lived experience of chatbot support",
  "summary":"Interviews describe how some users found generative chatbots unexpectedly helpful.",
  "body":["Participants recounted moments where a chatbot felt like the right support at the right time, alongside clear limits.","The accounts add nuance to a debate often framed only around risk."],
  "sources":[("NCBI","https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11514308/")]},
 {"h3":"Access disparities shape who turns to AI for help",
  "summary":"Researchers flagged gaps in who uses chatbots and why.",
  "body":["Patterns of use varied by age, gender and prior contact with the health system, raising equity questions.","Experts cautioned that AI tools could widen or narrow gaps depending on design and access."],
  "sources":[("AJMC","https://www.ajmc.com/view/ai-chatbot-use-for-mental-health-advice-rises-sharply-among-us-youth-with-key-disparities-identified")]},
],

"sports": [
 {"hero":True,"sub":"Tennis",
  "h3":"Grass season opens at Stuttgart, 's-Hertogenbosch and Queen's",
  "summary":"The grass swing is underway as players tune up for Wimbledon across three June events.",
  "body":["The BOSS Open in Stuttgart and the Libema Open in 's-Hertogenbosch both run June 8-14, while the HSBC Championships at Queen's Club span June 6-21.","Dutch favourite Tallon Griekspoor is back on home grass, with Nick Kyrgios's return and rising Czech teen Jakub Mensik adding intrigue."],
  "sources":[("ATP Tour","https://www.atptour.com/en/news/what-is-the-2026-atp-tour-grass-season-calendar"),("Tennis Connected","https://tennisconnected.com/grass-court-season-preview-stuttgart-s-hertogenbosch-and-the-hsbc-championships-in-london/")]},
 {"h3":"Griekspoor chases momentum on Dutch grass",
  "summary":"The home favourite is looking to rediscover form at 's-Hertogenbosch.",
  "body":["Griekspoor returns to a tournament where he has thrived before, hoping the local crowd lifts him toward Wimbledon.","A deep run would steady a season that has had its ups and downs."],
  "sources":[("Tennis Connected","https://tennisconnected.com/grass-court-season-preview-stuttgart-s-hertogenbosch-and-the-hsbc-championships-in-london/")]},
 {"h3":"Mensik's first-strike game shines early on grass",
  "summary":"The young Czech is making a mark with aggressive, serve-led tennis.",
  "body":["Mensik's first-strike style has proven effective in the opening grass week, marking him as one to watch.","His emergence adds to a generational shift on the men's tour."],
  "sources":[("Tennis Connected","https://tennisconnected.com/atp-and-wta-2026-schedule-of-play-friday-june-12-for-stuttgart-s-hertogenbosch-and-the-hsbc-championships/")]},
 {"sub":"Sailing",
  "h3":"Flying Roos lead SailGP standings",
  "summary":"Tom Slingsby's BONDS Flying Roos top the 2026 season table.",
  "body":["As of June 11 the Australians led on 55 points, ahead of Emirates GBR on 44 and the US team on 36.","The championship remains tight as the fleet heads into its summer events."],
  "sources":[("SailGP","https://sailgp.com/results/all-seasons/")]},
 {"sub":"Formula 1",
  "h3":"F1 heads to Barcelona for the Catalunya Grand Prix",
  "summary":"The Spanish round runs June 12-14 at the Circuit de Barcelona-Catalunya.",
  "body":["The familiar Catalunya layout offers a stern test of car balance as teams refine upgrades.","Title contenders are watching the head-to-head battles closely as the season develops."],
  "sources":[("Sky Sports F1","https://www.skysports.com/f1/news/12433/13516662/f1-team-mate-2026-head-to-head-qualifying-race-sprint-latest-scores-results-from-formula-1-season")]},
 {"sub":"Football",
  "h3":"Ajax bring back Kasper Dolberg",
  "summary":"The Danish striker returns to Amsterdam on a deal to 2029.",
  "body":["Dolberg, who scored 45 goals in 119 games in his first spell, rejoins the club where he won three trophies in 2019.","The move adds proven Eredivisie firepower as Ajax reshape their attack."],
  "sources":[("NL Times","https://nltimes.nl/2026/01/01/january-transfer-window-opens-big-decisions-looming-psv-ajax-feyenoord")]},
 {"h3":"PSV sign Dennis Man from Parma",
  "summary":"The Romanian winger joins Eindhoven for 8.5 million euros on a four-year deal.",
  "body":["Man arrives after 142 appearances for Parma with 28 goals and 17 assists.","PSV also added Bayern's Paul Wanner and extended Noah Fernandez to 2030."],
  "sources":[("Sportsdunia","https://www.sportsdunia.com/football-transfers/psv-transfers")]},
 {"h3":"Ajax add defender Ko Itakura",
  "summary":"The Japan international signs from Borussia Monchengladbach until 2029.",
  "body":["The 28-year-old joins on a four-year contract with an option for a further year.","Itakura strengthens an Ajax backline in transition."],
  "sources":[("NL Times","https://nltimes.nl/2026/01/01/january-transfer-window-opens-big-decisions-looming-psv-ajax-feyenoord")]},
 {"sub":"Grappling",
  "h3":"ADCC 2026 World Championships set for Krakow",
  "summary":"The premier submission-grappling event lands at Tauron Arena on September 12-13.",
  "body":["Trials season is well underway, with grapplers from every continent chasing invitations to the championships.","At the West Coast Trials, Sarah Galvao dominated with three submissions to seal her spot."],
  "sources":[("MMA Mania","https://www.mmamania.com/bjj-news/438089/sarah-galvao-gianni-grippo-among-8-bjj-champs-to-win-adcc-2026-invites-at-adcc-west-coast-trials")]},
 {"h3":"UFC BJJ keeps building toward a packed June",
  "summary":"The promotion's submission-only series continues after Musumeci's latest title defence.",
  "body":["UFC BJJ 8 on May 21 in Las Vegas featured Mikey Musumeci defending his bantamweight belt for a third time.","The ADCC Dallas Open on June 20 adds another marker on a crowded grappling calendar."],
  "sources":[("Wikipedia","https://en.wikipedia.org/wiki/UFC_BJJ_8")]},
 {"h3":"ADCC trials draw thousands chasing Krakow slots",
  "summary":"Continental trials are funnelling top grapplers toward the World Championships.",
  "body":["Trials across regions are producing a steady stream of qualifiers ahead of September.","The depth of fields underscores the sport's continued growth."],
  "sources":[("ADC Combat","https://adcombat.com/adcc-events/adcc-thailand-open-2026/")]},
],

"consumer-tech": [
 {"hero":True,"sub":"Devices & Launches",
  "h3":"Apple's WWDC centres on Siri, Liquid Glass and a CEO handover",
  "summary":"Apple's developer conference led with a long-promised Siri overhaul and a leadership transition.",
  "body":["The June 8 keynote unveiled a revamped Siri, updates to the Liquid Glass design, and previews of iOS 27, macOS 27 and sibling operating systems.","Apple also named hardware chief John Ternus as Tim Cook's successor, with Cook becoming executive chairman on September 1; Mac Studio, Mac mini and iMac are lined up for M5-class refreshes."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html"),("MacRumors","https://www.macrumors.com/guide/upcoming-apple-products/")]},
 {"h3":"Siri leans on a custom Apple-Google model",
  "summary":"New Siri features use a model built with Google's Gemini team.",
  "body":["Apple's chatbot-style Siri capabilities draw on a custom model developed with Google, with heavier tasks running on Nvidia GPUs in Google's cloud.","The partnership marks a notable shift for a company that has emphasised in-house AI."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html")]},
 {"h3":"Smart glasses tipped to arrive from 2027",
  "summary":"Analysts expect Apple smart glasses among new products landing from 2027.",
  "body":["Wearables, including glasses, feature in roadmaps pointing to launches beginning next year.","The timing suggests Apple is pacing its mixed-reality ambitions after the Vision line."],
  "sources":[("Seeking Alpha","https://seekingalpha.com/news/4463563-apples-smart-glasses-among-new-products-to-hit-market-from-2027-analyst")]},
 {"sub":"Software & Services",
  "h3":"Gemini 3.5 Flash becomes the default across Google apps",
  "summary":"Google's faster model now powers the Gemini app and AI Mode in Search.",
  "body":["After going GA on May 19, Gemini 3.5 Flash is the default consumer model, with API pricing at $1.50 and $9.00 per million tokens.","Its rollout deepens AI features across Google's most-used surfaces."],
  "sources":[("WaveSpeed","https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/")]},
 {"h3":"Copilot's metered pricing reshapes developer costs",
  "summary":"GitHub Copilot's switch to usage-based credits changes how teams budget for AI.",
  "body":["From June 1, Copilot bills by consumption with AI credits at one cent each, reflecting longer agentic runs.","Teams are recalibrating workflows as costs track actual usage."],
  "sources":[("Faros AI","https://www.faros.ai/blog/best-ai-coding-agents-2026")]},
 {"sub":"EVs & Mobility",
  "h3":"Lucid ships Hands-Free Drive Assist to Gravity SUVs",
  "summary":"An over-the-air update added hands-free and lane-change assist features.",
  "body":["The June 9 update brought Hands-Free Drive Assist and Lane Change Assist to Lucid's Gravity SUVs.","The rollout underscores how EV makers keep adding capability after sale via software."],
  "sources":[("Electrek","https://electrek.co/")]},
 {"h3":"Tesla robotaxi covers Austin metro with a tiny fleet",
  "summary":"Tesla expanded coverage even as its operating fleet stayed small.",
  "body":["The service blankets the Austin metro but runs only around 20 vehicles, with the fleet shrinking rather than growing.","Musk ties a meaningful scale-up to the FSD v15 software rewrite."],
  "sources":[("Electrek","https://electrek.co/2026/06/03/tesla-robotaxi-expands-entire-austin-metro-only-20-vehicles/")]},
 {"h3":"EV startups face a make-or-break 2026",
  "summary":"Rivian, Lucid and Slate are racing toward crucial launches and profitability.",
  "body":["Rivian deliveries rose 20 percent year over year in Q1 and likely outsold Ford's EVs after the F-150 Lightning was cancelled.","Lucid has leaned on fresh Saudi and Uber investment to stay the course."],
  "sources":[("InsideEVs","https://insideevs.com/features/793324/rivian-slate-lucid-update-2026/")]},
 {"h3":"Apple lines up M5 refreshes across the Mac range",
  "summary":"Mac Studio, Mac mini and iMac are candidates for M5-class chips.",
  "body":["The Mac Studio is expected to gain M5 Max and M5 Ultra options, with the Mac mini in line for M5 and M5 Pro.","An iMac update on M5 is also anticipated as Apple refreshes its desktop lineup."],
  "sources":[("MacRumors","https://www.macrumors.com/guide/upcoming-apple-products/")]},
 {"h3":"Apple confirms device launches before its next event",
  "summary":"Apple signalled new products arriving ahead of its first scheduled 2026 launch event.",
  "body":["The company indicated some hardware would ship before the next formal event, spreading releases across the calendar.","The approach reflects a steadier cadence of smaller refreshes between marquee keynotes."],
  "sources":[("NotebookCheck","https://www.notebookcheck.net/Apple-confirms-new-device-launches-occurring-before-first-2026-launch-event.1235652.0.html")]},
],
}

MOOD = {"h3":"Sfeer vandaag","p":"Vroege zomer in Nederland: a mild, changeable Saturday with the usual mix of sun and showers as the country eases into the weekend. The national mood is unsettled beneath the warmth, with households watching prices, asylum policy back in the headlines, and quiet anxiety about a wobbling international order. Grass-court tennis in 's-Hertogenbosch and summer travel plans offer a lighter counterweight."}

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