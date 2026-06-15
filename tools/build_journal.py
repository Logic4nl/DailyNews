#!/usr/bin/env python3
import html, json, sys

DATE_ISO = "2026-06-16"
DATE_HUMAN = "Tuesday, June 16, 2026"
PREV_ISO = "2026-06-15"
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
  "h3":"Iran sets July funeral for Khamenei as fragile US truce holds",
  "summary":"Iranian state media said the funeral and burial of late supreme leader Ali Khamenei will run July 4 to 9, while mediators keep trying to turn the April ceasefire into a lasting deal.",
  "body":["State outlets confirmed an extended series of memorial rites for Khamenei, killed in the opening strikes of the 2026 war in late February, signalling Tehran is consolidating its post-leadership transition even as the conflict with the US and Israel remains formally unresolved.","A Pakistan-mediated ceasefire agreed April 8 has been extended repeatedly. Negotiators say they have settled wording for a fuller agreement, but Tehran remains wary, and Iranian officials warned operations could resume if Israeli strikes in southern Lebanon continue."],
  "sources":[("Euronews","https://www.euronews.com/news/international"),("House of Commons Library","https://commonslibrary.parliament.uk/research-briefings/cbp-10637/")]},
 {"h3":"Lebanon-Israel truce loosely holds as Hezbollah keeps firing",
  "summary":"A US-brokered ceasefire is reducing cross-border fire, but Hezbollah is expected to keep targeting Israeli positions inside Lebanon.",
  "body":["The arrangement between Beirut and Israel has cut the volume of exchanges, yet analysts describe it as a managed standoff rather than peace, with Hezbollah likely to keep hitting Israeli forces on Lebanese soil while avoiding strikes on northern Israel.","Israel has shown little sign of pulling back, leaving the southern front a persistent flashpoint that could reignite the wider regional conflict."],
  "sources":[("ACLED","https://acleddata.com/update/middle-east-overview-june-2026")]},
 {"h3":"Russian advance slows as trackers log Ukrainian net gains",
  "summary":"Open-source monitors say Russian forces lost ground over recent weeks, reversing earlier 2026 momentum.",
  "body":["DeepState data for early June shows fluctuating lines, with Russia making a net gain of about six square miles in the June 2 to 9 window after a net loss of 93 square miles in the prior four weeks.","Total occupied territory stood near 45,118 square miles as of June 2. Measurements vary by source, but the trend points to a marked slowdown in Russian gains compared with early 2026."],
  "sources":[("Russia Matters","https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-june-10-2026")]},
 {"h3":"Israel expands Gaza footprint toward 70 percent control",
  "summary":"Satellite imagery shows new Israeli military posts as control rises from 60 percent, with Netanyahu signalling further expansion.",
  "body":["ACLED logged more than 40 Israeli attacks on Hamas and allied groups in May, the highest monthly total since the October 2025 ceasefire, with strikes killing several senior commanders including military chief Izz al-Din Haddad.","Imagery shows outposts expanding east of Gaza City and a new base built atop the bulldozed Eastern Cemetery in Khan Younis, as Israel presses pressure while shifting focus to Lebanon and Iran."],
  "sources":[("Al Jazeera","https://www.aljazeera.com/news/2026/6/3/israel-is-building-more-military-posts-in-gaza-satellite-imagery-shows"),("ACLED","https://acleddata.com/update/middle-east-overview-june-2026")]},
 {"h3":"Strait of Hormuz disruption keeps rattling global trade",
  "summary":"Shipping reroutes and energy spikes from the spring conflict continue to reverberate well beyond the Gulf.",
  "body":["The closure of the Strait of Hormuz during the height of the war forced tankers onto longer routes and pushed Brent crude sharply higher, with knock-on effects on insurance, freight and inflation worldwide.","The Netherlands signalled openness to helping secure the strait if a US-Iran peace deal is reached, underscoring how widely the fallout has spread across European policy debates."],
  "sources":[("NL Times","https://nltimes.nl/top-stories"),("EIA","https://www.eia.gov/outlooks/steo/")]},
 {"sub":"Diplomacy & Trade",
  "h3":"US orders Anthropic to cut foreign-national access to top models",
  "summary":"A government directive told the AI company to suspend access to its most capable models for foreign nationals, a striking national-security move.",
  "body":["The order marks an escalation in Washington's effort to treat frontier AI as a controlled strategic capability, extending export-style thinking from chips to the models themselves.","It lands amid broader curbs on advanced AI chips, which the Commerce Department says now cover Chinese-headquartered firms wherever they operate."],
  "sources":[("Euronews","https://www.euronews.com/news/international")]},
 {"h3":"China tightens travel curbs on its AI researchers",
  "summary":"Researchers at Alibaba and DeepSeek now need Beijing approval before overseas trips, a control once reserved for nuclear scientists.",
  "body":["The restrictions aim to stop talent poaching and outward transfer of know-how as China's AI capability approaches parity with the US, with Stanford's 2026 AI Index putting the gap at just 2.7 percent.","The move mirrors tightening on the US side and signals that both powers increasingly treat AI talent as a national-security asset."],
  "sources":[("TechTimes","https://www.techtimes.com/articles/317325/20260528/china-ai-travel-curbs-reach-alibaba-deepseek-private-sector-researchers-need-beijing-approval.htm")]},
 {"h3":"London opera marks World Cup kickoff",
  "summary":"Covent Garden staged a Nessun dorma performance to mark the start of the 2026 World Cup.",
  "body":["SeokJong Baek and the Royal Opera Chorus performed the Puccini aria long associated with football tournaments, a cultural curtain-raiser as the expanded 48-team event got under way across North America.","The tournament, running June 11 to July 19, is the first hosted jointly by the US, Canada and Mexico."],
  "sources":[("Euronews","https://www.euronews.com/news/international")]},
 {"sub":"Humanitarian & Climate",
  "h3":"Elevated oil keeps pressure on import-dependent economies",
  "summary":"With Brent averaging near $105 in June, energy-importing and lower-income economies face renewed strain.",
  "body":["The EIA expects falling inventories to keep Brent elevated through the summer if Hormuz traffic stays constrained, raising costs for fuel, fertiliser and food across vulnerable economies.","Forecasters warn that sustained high energy prices could slow global growth and complicate central-bank efforts to ease policy."],
  "sources":[("EIA","https://www.eia.gov/outlooks/steo/report/global_oil.php")]},
 {"h3":"South Korea closes chapter on Yoon martial-law saga",
  "summary":"Aftershocks from the 2024 to 2025 political crisis continue to shape Seoul's institutions.",
  "body":["The reckoning over the martial-law episode has reordered South Korean politics, with courts and parliament asserting authority after one of the country's gravest constitutional tests in decades.","Analysts say the saga has reinforced guardrails against executive overreach even as it leaves a polarised electorate."],
  "sources":[("Euronews","https://www.euronews.com/tag/world-news")]},
],
"netherlands": [
 {"hero":True,"sub":"Politics & Policy",
  "h3":"Jetten minority cabinet navigates first months in office",
  "summary":"D66 leader Rob Jetten leads the Netherlands' first minority government in decades, governing with VVD and CDA on 66 of 150 seats.",
  "body":["After D66 and PVV each won 26 seats in October 2025, Jetten formed a three-party coalition presented on January 30, ten seats short of a majority and reliant on shifting parliamentary support to pass legislation.","The arrangement followed the collapse of the Schoof cabinet in February, leaving the government to balance housing, asylum and budget pressures without a fixed majority."],
  "sources":[("DutchReview","https://dutchreview.com/news/new-dutch-cabinet-unveils-coalition-plans/"),("IamExpat","https://www.iamexpat.nl/expat-info/dutch-news/whats-next-dutch-government-after-collapse-schoof-i")]},
 {"h3":"Coalition keeps mortgage relief, plans housing investment",
  "summary":"The government will leave the mortgage interest deduction unchanged and pledges a billion euros a year for affordable housing from 2029.",
  "body":["Ministers framed the unchanged deduction as protecting housing-market stability, while introducing annual income checks for rent increases and wealth tests for new social-housing tenants.","From 2029 the state plans to invest one billion euros a year in affordable housing, a long-dated response to a shortage that continues to dominate domestic politics."],
  "sources":[("DutchReview","https://dutchreview.com/news/new-dutch-cabinet-unveils-coalition-plans/")]},
 {"h3":"Cabinet scraps national tax on China parcels",
  "summary":"The Netherlands dropped plans for its own levy on low-value packages from China, waiting instead for an EU-wide import tax.",
  "body":["Officials said a unilateral charge risked complexity and friction, and that an EU import tax now in the works would be a cleaner route to address the flood of cheap e-commerce parcels.","The decision aligns Dutch policy with a broader European push to tighten rules on platforms shipping directly to consumers."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
 {"h3":"Netherlands open to helping secure Strait of Hormuz",
  "summary":"The Hague signalled willingness to contribute to securing the strait should a US-Iran peace deal take hold.",
  "body":["The statement reflects Dutch concern over the trade and energy fallout from the spring conflict, and a readiness to back maritime-security efforts within an allied framework.","Any contribution would likely be modest and conditional on a durable agreement rather than the current fragile truce."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
 {"sub":"Economy & Housing",
  "h3":"NS 49-euro summer pass overwhelms website",
  "summary":"Demand for the national rail operator's discounted summer ticket crashed the site, with sales topping 20,000.",
  "body":["The 49-euro pass drew a rush of buyers as households look to stretch travel budgets over the holidays, briefly overwhelming NS systems at launch.","The scramble highlighted both the appeal of cheaper rail travel and the strain on booking infrastructure during peak demand."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
 {"h3":"Benefits scandal redress hits new snag",
  "summary":"Roughly 20,000 parents were wrongly compensated as victims in the long-running childcare benefits affair.",
  "body":["The error is the latest stumble in a redress programme that has repeatedly struggled to fairly identify and pay the families harmed by the tax authority's wrongful fraud accusations.","The scandal remains a defining stain on Dutch governance and a recurring test of the state's ability to make amends."],
  "sources":[("DutchNews.nl","https://www.dutchnews.nl/")]},
 {"sub":"Society & Culture",
  "h3":"Hague court hands Syrian ex-interrogator 26 years",
  "summary":"A Dutch court convicted a former Syrian interrogator of crimes including torture and rape, sentencing him to 26 years.",
  "body":["The verdict reflects the Netherlands' active use of universal-jurisdiction prosecutions to pursue grave international crimes committed abroad.","Rights advocates welcomed the ruling as a measure of accountability for victims of the Syrian conflict."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
 {"h3":"Police seize 100 km/h fatbike in safety crackdown",
  "summary":"Officers impounded a souped-up fatbike capable of reaching 100 km/h amid concern over illegally fast e-bikes.",
  "body":["The seizure underlines a growing enforcement push against modified electric bikes that far exceed legal speed limits and endanger riders and pedestrians.","Dutch authorities have flagged fatbikes as a rising road-safety problem, particularly among younger riders."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
 {"h3":"PSV sells Saibari to Bayern for record 55 million euros",
  "summary":"Eindhoven cashed in on midfielder Ismael Saibari in a club-record sale to Bayern Munich.",
  "body":["The 55-million-euro transfer marks one of the largest fees ever received by PSV and reflects strong demand for Eredivisie talent from Europe's biggest clubs.","The sale strengthens PSV's finances while leaving the squad to rebuild around the departure of a key creative player."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
 {"h3":"Heat and storm risk build toward the weekend",
  "summary":"Temperatures could reach 33C in parts of the country by Friday, with rising thunderstorm risk.",
  "body":["Forecasters expect an early-summer warm spell followed by an increasing chance of storms, a familiar Dutch pattern of heat broken by unsettled weather.","Authorities urged caution around heat and sudden downpours as outdoor activity picks up."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
],
"ai-hpc": [
 {"hero":True,"sub":"Foundation Models & Releases",
  "h3":"June model flood: GPT-5.6, Gemini 3.5 Pro and Claude 4.8 land",
  "summary":"The industry is calling June 2026 the most concentrated month of frontier model releases yet, with all three leading labs shipping or teasing major upgrades.",
  "body":["Anthropic shipped Claude Opus 4.8 on May 28 with agentic upgrades, and by early June it topped the LLM Stats overall score at 67.9, ahead of GPT-5.5. Google held Gemini 3.5 Pro for a June release after announcing 3.5 Flash at I/O, while references to an OpenAI model codenamed iris-alpha, widely read as GPT-5.6, leaked from Codex logs.","On user-preference rankings Gemini 3 Pro leads LMArena, while the Artificial Analysis Intelligence Index v4.0 places GPT-5.2 with extended reasoning at the top on benchmarks, underscoring how crowded the frontier has become."],
  "sources":[("LLM Stats","https://llm-stats.com/llm-updates"),("Essa Mamdani","https://www.essamamdani.com/blog/june-2026-ai-model-flood-gpt-gemini-claude")]},
 {"h3":"Anthropic warns its own models may outpace control",
  "summary":"The company issued a rare public caution that frontier systems could soon be too powerful to reliably steer.",
  "body":["The warning, paired with a new model line and rapid agentic gains, signals that even leading developers see safety margins narrowing as capability climbs.","It arrives alongside reports that Anthropic has confidentially filed for an IPO after a $65 billion round valuing it near $965 billion."],
  "sources":[("Build Fast with AI","https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026")]},
 {"h3":"DeepSeek previews long-awaited V4 model",
  "summary":"China's DeepSeek showed a preview of V4, promising upgrades in reasoning and agentic ability to rival US labs.",
  "body":["The release lands a year after R1 reset expectations for Chinese open models, into a far more competitive home market where Alibaba and ByteDance are shipping aggressively.","Huawei confirmed its latest Ascend-powered cluster can support V4, an important signal for domestic compute self-sufficiency."],
  "sources":[("CNBC","https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html")]},
 {"sub":"AI/HPC Stocks & Infrastructure",
  "h3":"Nvidia puts Vera CPU into full production",
  "summary":"Jensen Huang said the data-center Vera CPU is in full production, with OpenAI, Anthropic and SpaceX among early adopters.",
  "body":["At Computex in Taipei, Nvidia detailed its Rubin platform spanning six co-designed chips, with Vera Rubin instances due from AWS, Google Cloud, Microsoft, Oracle and neoclouds including CoreWeave, Lambda, Nebius and Nscale in the second half of 2026.","The push aims to cut training time and inference token costs as hyperscalers race to expand capacity."],
  "sources":[("NVIDIA Newsroom","https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer"),("Data Center Knowledge","https://www.datacenterknowledge.com/data-center-chips/ces-2026-nvidia-launches-rubin-to-maintain-data-center-stronghold")]},
 {"h3":"Microsoft guides to 190 billion dollars of 2026 capex",
  "summary":"Microsoft said total capital spending this year should reach about $190 billion, with surging memory prices adding to the bill.",
  "body":["Roughly $25 billion of the increase is attributed to higher memory and storage costs driven by AI infrastructure demand, a sign of how component inflation is rippling through hyperscaler budgets.","The figure cements the scale of the buildout even as investors question how quickly AI revenue will catch up to spend."],
  "sources":[("Build Fast with AI","https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026")]},
 {"h3":"Oracle leans into Stargate and AI data centers",
  "summary":"Oracle is redirecting spending toward massive AI data-center projects, including the $500 billion Stargate effort with OpenAI and SoftBank.",
  "body":["The pivot positions Oracle as a core capacity provider in the AI buildout, betting that long-duration compute contracts will anchor growth.","It reflects a wider shift in which infrastructure, not models, increasingly drives the economics of the AI boom."],
  "sources":[("Build Fast with AI","https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026")]},
 {"h3":"Amazon custom silicon passes 20 billion dollar run rate",
  "summary":"Amazon's in-house chip business surpassed a $20 billion annual run rate with multi-year commitments from major AI customers.",
  "body":["Commitments from OpenAI, Anthropic, Meta and Uber underline how hyperscalers are diversifying away from sole reliance on Nvidia for training and inference.","The scale signals that custom accelerators are becoming a durable second pillar of AI compute supply."],
  "sources":[("Build Fast with AI","https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026")]},
 {"sub":"Agents & Automation",
  "h3":"Coding agents become team infrastructure",
  "summary":"A wave of June launches reframes AI coding tools as shared team systems rather than solo assistants.",
  "body":["Z.ai launched GLM-5.2 across its coding plans on June 13 with a one-million-token context window, while Augment Code rolled out Cosmos to every team plan and Microsoft introduced Rayfin at Build 2026.","GitHub Copilot scrapped premium-request billing for usage-based credits on June 1, and surveys suggest 57 percent of organisations now run AI agents in production workflows."],
  "sources":[("The New Stack","https://thenewstack.io/coding-agents-team-infrastructure/"),("MarkTechPost","https://www.marktechpost.com/2026/06/10/ai-coding-agents-development-platforms-2026/")]},
 {"h3":"Microsoft and Google push deeper into AI coding models",
  "summary":"The two giants are challenging Anthropic and OpenAI directly on code generation.",
  "body":["Both companies are positioning proprietary coding models as a strategic battleground, betting that developer workflows are among the stickiest enterprise use cases.","The contest is accelerating feature parity and price competition across the coding-agent market."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html")]},
 {"sub":"Enterprise & Regulation",
  "h3":"OpenAI updates life-sciences model and biodefense push",
  "summary":"OpenAI refreshed its life-sciences model and launched a new biodefense initiative while preparing IPO paperwork.",
  "body":["The biodefense effort signals growing attention to dual-use risk as models gain capability in scientific domains.","It coincides with reports that OpenAI is finalising Wall Street IPO documents, mirroring Anthropic's move toward public markets."],
  "sources":[("Build Fast with AI","https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026")]},
 {"h3":"Apple licenses custom Gemini model from Google",
  "summary":"Apple is paying roughly $1 billion a year to license a 1.2-trillion-parameter custom Gemini model from Google.",
  "body":["The deal, confirmed jointly earlier in the year, underpins a revamped Siri and signals Apple's pragmatic choice to buy frontier capability rather than build it alone.","It deepens an unusual partnership between two longtime rivals at the center of the mobile ecosystem."],
  "sources":[("AI Business","https://aibusiness.com/generative-ai/openai-vs-anthropic-vs-google-model-isn-t-the-point")]},
 {"sub":"Chinese AI Ecosystem",
  "h3":"DeepSeek weighs outside funding for the first time",
  "summary":"The Chinese lab is considering external capital, drawing interest from Alibaba and state funds.",
  "body":["The move would mark a shift for a company that built its reputation on lean, self-funded development, and points to the capital intensity now required to stay at the frontier.","Alibaba's interest also reflects consolidation pressures across China's crowded model landscape."],
  "sources":[("TipRanks","https://www.tipranks.com/news/deepseek-draws-interest-from-alibaba-baba-as-it-considers-outside-funding")]},
],
"crypto-macro": [
 {"hero":True,"sub":"Macro & Central Banks",
  "h3":"Fed expected to hold as two-day meeting opens",
  "summary":"The FOMC began its June 16 to 17 meeting with markets pricing near-certain odds of no change to the 3.5 to 3.75 percent range.",
  "body":["Market-implied odds put a hold at roughly 99.6 percent, leaving attention on the statement and Chair Powell's press conference for any signal on the path of cuts later in 2026.","The April meeting held rates on an 8-4 vote, the most divided since 1992, and elevated oil prices from the spring conflict complicate the inflation picture the committee must weigh."],
  "sources":[("Polymarket","https://polymarket.com/event/fed-decision-in-june-825"),("Federal Reserve","https://www.federalreserve.gov/monetarypolicy/fomcminutes20260429.htm")]},
 {"h3":"S&P 500 forecasts split as oil and earnings tug",
  "summary":"Year-end targets range widely, from JPMorgan's cautious 7,200 to Goldman's 8,000.",
  "body":["Reuters' median year-end forecast sits near 7,620, with UBS at 7,900 and Goldman at 8,000, while JPMorgan trimmed to 7,200 and flagged downside toward 6,000 if headwinds intensify.","AI-related earnings are supporting tech-heavy indices, but elevated oil and softer guidance are the main risks cited by bears."],
  "sources":[("AOL/JPMorgan","https://www.aol.com/jp-morgan-resets-p-500-150018412.html"),("Capital.com","https://capital.com/en-int/market-updates/us-index-forecast-10-06-2026")]},
 {"h3":"Brent holds near 105 dollars on Hormuz risk",
  "summary":"The EIA expects falling inventories to keep Brent elevated through summer if shipping stays constrained.",
  "body":["Brent averaged $107 in May and is projected near $105 in June and July under the assumption that Hormuz traffic remains limited.","Sustained high energy prices risk slowing growth and keeping inflation sticky, potentially delaying Fed easing."],
  "sources":[("EIA","https://www.eia.gov/outlooks/steo/report/global_oil.php")]},
 {"sub":"Bitcoin & Ethereum",
  "h3":"Bitcoin rebounds above 65,000 dollars on truce relief",
  "summary":"Bitcoin hit a two-week high after a weekend peace deal sent oil lower and lifted risk assets.",
  "body":["Bitcoin pushed above $65,500 as easing Middle East tensions improved sentiment, after opening near $63,553 on June 12, up over 3 percent that day. Ethereum traded near $1,672, also up around 3 percent.","Traders are watching the Fed meeting as the main near-term catalyst after a volatile start to June."],
  "sources":[("Yahoo Finance","https://finance.yahoo.com/personal-finance/investing/article/bitcoin-and-ethereum-prices-today-friday-june-12-2026-bitcoin-rebound-this-morning-after-trump-claims-war-has-ended-115949042.html")]},
 {"h3":"Spot Bitcoin ETFs nurse heavy outflows",
  "summary":"US spot Bitcoin ETFs recorded outflows exceeding 3.75 billion dollars since mid-May.",
  "body":["The sustained redemptions reflect risk-off positioning during the spring conflict and a broader rotation, even as prices recovered on the ceasefire.","Whether inflows return likely hinges on the Fed's tone and the durability of the Middle East truce."],
  "sources":[("Intellectia","https://intellectia.ai/blog/bitcoin-price-recovery-june-2026")]},
 {"sub":"Regulation & Policy",
  "h3":"SEC puts digital assets atop its strategic plan",
  "summary":"A draft SEC strategic plan for 2026 to 2030 names digital assets and distributed ledger tech as its first regulatory objective.",
  "body":["Published June 2, the plan signals a marked shift toward a clearer, more structured approach to crypto oversight after years of enforcement-led policy.","It positions the SEC at the center of implementing the new federal framework taking shape across digital-asset markets."],
  "sources":[("The Block","https://www.theblock.co/post/383653/2026-crypto-regulation-outlook")]},
 {"h3":"Stablecoin rules near finalisation under GENIUS Act",
  "summary":"Regulators are expected to finalise licensing, custody and capital rules for payment stablecoins by mid-2026.",
  "body":["The 2025 GENIUS Act restricts issuance to regulated banks, credit unions and licensed non-banks under OCC oversight, but key details await follow-up rulemaking.","Banks are pressing regulators to close a loophole letting stablecoin issuers offer yield, which they fear could erode deposits."],
  "sources":[("DL News","https://www.dlnews.com/articles/regulation/key-dates-for-us-crypto-regulation-in-2026/"),("BVNK","https://bvnk.com/blog/global-stablecoin-regulations-2026")]},
 {"sub":"DeFi & Altcoins",
  "h3":"Risk appetite returns to majors after ceasefire",
  "summary":"Futures positioning showed a renewed taste for risk as crypto markets steadied.",
  "body":["After a red start to June, derivatives data pointed to traders cautiously rebuilding long exposure in major tokens as geopolitical fear ebbed.","Altcoin leadership remained narrow, with the broader market still anchored to macro signals and the Fed.",],
  "sources":[("CoinDesk","https://www.coindesk.com/markets/2026/06/01/bitcoin-ether-start-june-in-the-red-while-futures-show-taste-for-risk-xlm-hype-gain")]},
],
"mental-health": [
 {"hero":True,"sub":"Research & Studies",
  "h3":"Landmark trial shows generative AI chatbot eased clinical symptoms",
  "summary":"A randomized controlled trial of the fine-tuned Therabot chatbot reported meaningful improvements in depression, anxiety and eating-disorder risk.",
  "body":["Published in NEJM AI, the trial is described as the first RCT to demonstrate effectiveness of a fully generative AI therapy chatbot for clinical-level symptoms, with strong engagement and high user ratings among adults with MDD, GAD or high risk for feeding and eating disorders.","Researchers cautioned that results need replication and that generative chatbots require careful guardrails before broad clinical deployment."],
  "sources":[("NEJM AI","https://ai.nejm.org/doi/full/10.1056/AIoa2400802")]},
 {"h3":"Stanford flags dangers of AI therapy chatbots",
  "summary":"A Stanford study warns that therapy chatbots can introduce bias and fail in ways that risk harm.",
  "body":["Researchers found that some systems lacked effectiveness compared with human therapists and could respond inappropriately to signs of crisis, raising safety concerns.","The work adds to calls for clear standards and oversight before chatbots are used in higher-risk mental-health contexts."],
  "sources":[("Stanford HAI","https://hai.stanford.edu/news/exploring-the-dangers-of-ai-in-mental-health-care")]},
 {"h3":"New study details ethical risks of ChatGPT as therapist",
  "summary":"Researchers documented serious ethical risks when general-purpose chatbots are used for therapy.",
  "body":["The analysis highlighted issues around privacy, inconsistent responses and the absence of clinical accountability when people lean on consumer chatbots for mental-health support.","Authors urged users and clinicians to treat general models as unvalidated for treatment rather than as substitutes for care."],
  "sources":[("ScienceDaily","https://www.sciencedaily.com/releases/2026/03/260302030642.htm")]},
 {"h3":"Qualitative study centers lived experience of chatbot use",
  "summary":"A JMIR Mental Health study explored how people with depression actually experience an LLM-based self-management chatbot.",
  "body":["Researchers built a GPT-4o-based chatbot named Zenny and interviewed 17 people with lived experience of depression, surfacing both comfort and concern in day-to-day use.","Participants valued availability and non-judgment but flagged limits around depth, trust and crisis handling."],
  "sources":[("JMIR Mental Health","https://mental.jmir.org/2026/1/e78288")]},
 {"h3":"Science review maps AI across mental-health research and care",
  "summary":"A Science paper surveys how AI could reshape diagnosis, treatment and access in mental health.",
  "body":["The review weighs opportunities to extend support beyond clinics against risks of bias, over-reliance and weak evidence, calling for rigorous evaluation.","It frames AI as a complement to, not a replacement for, human clinicians."],
  "sources":[("Science","https://www.science.org/doi/10.1126/science.adz9193")]},
 {"sub":"Tools & Applications",
  "h3":"Digital mental-health market accelerates toward 2035",
  "summary":"The US digital mental-health market is projected to grow from about 8.97 billion dollars in 2026 at a 20 percent CAGR.",
  "body":["Analysts expect the market to expand toward roughly 47 billion dollars by 2035, propelled by teletherapy adoption and FDA-cleared digital therapeutics.","Reimbursement progress, including Medicare coverage of some approved apps, is helping move tools into mainstream care."],
  "sources":[("Towards Healthcare","https://www.towardshealthcare.com/insights/us-digital-mental-health-market-sizing")]},
 {"h3":"Big Health raises 23.7 million to expand FDA-cleared treatments",
  "summary":"The digital therapeutics firm secured new funding to scale reimbursable insomnia and anxiety treatments.",
  "body":["The capital supports broader access to SleepioRx for insomnia and DaylightRx for generalized anxiety, both FDA-cleared and built for integration with teletherapy.","The round reflects investor confidence that evidence-based, reimbursable digital treatments can reach scale."],
  "sources":[("Business Wire","https://www.businesswire.com/news/home/20260212541697/en/Big-Health-Secures-Funding-to-Accelerate-Adoption-of-Digital-Mental-Health-Treatments")]},
 {"h3":"Reviews stress CBT and DBT grounding for chatbots",
  "summary":"New reviews argue mental-health chatbots work best when anchored in established psychological frameworks.",
  "body":["Analyses of NLP-driven systems point to better outcomes when tools draw on cognitive behavioral therapy, dialectical behavior therapy and mindfulness rather than open-ended chat.","The findings reinforce a move toward structured, evidence-based design over generic conversational agents."],
  "sources":[("Wiley/CAPR","https://onlinelibrary.wiley.com/doi/10.1002/capr.70095")]},
],
"sports": [
 {"hero":True,"sub":"Football / World Cup",
  "h3":"World Cup rolls on with Iran-New Zealand and France-Senegal",
  "summary":"The expanded 48-team tournament continues June 16 with group-stage fixtures including France against Senegal.",
  "body":["The opening days delivered upsets and tight margins: Australia beat Turkiye 2-0, Brazil and Morocco drew 1-1, Scotland edged Haiti 1-0, and Qatar snatched a late 1-1 draw with Switzerland.","The Netherlands opened with a 2-2 draw against Japan, setting up a congested race in their group as play continues across North American host cities."],
  "sources":[("Yahoo Sports","https://sports.yahoo.com/soccer/live/2026-world-cup-scores-results.html"),("Al Jazeera","https://www.aljazeera.com/sports/liveblog/2026/6/14/netherlands-vs-japan-live-world-cup-2026")]},
 {"h3":"PSV record sale ripples through Eredivisie market",
  "summary":"Bayern's 55-million-euro move for Ismael Saibari sets a marker for Dutch transfer values.",
  "body":["The club-record fee underscores the Eredivisie's role as a feeder to Europe's elite and gives PSV resources to reshape its squad.","It also raises expectations for further summer departures from the Dutch top flight."],
  "sources":[("NL Times","https://nltimes.nl/top-stories")]},
 {"sub":"Tennis",
  "h3":"Grass swing heats up before Wimbledon",
  "summary":"Queen's Club and Nottingham headline the men's grass season from June 15, with the women's tour also in full swing.",
  "body":["The ATP 500 men's event at Queen's runs June 15 to 21, while the Nottingham Open hosts tour-level play the same week as players sharpen form on grass.","The combined HSBC Championships format keeps both tours in London across the swing toward Wimbledon."],
  "sources":[("ATP Tour","https://www.atptour.com/en/news/what-is-the-2026-atp-tour-grass-season-calendar"),("WTA","https://www.wtatennis.com/news/4512314/grass-court-swing-411-2026-dates-draws-prize-money-and-everything-you-need-to-know")]},
 {"h3":"Libema Open caps Dutch grass week",
  "summary":"The 's-Hertogenbosch event wrapped its joint ATP and WTA week on home grass.",
  "body":["Elise Mertens went in as defending women's champion in a field featuring Alexandrova and Navarro, with the tournament a key tune-up on the Dutch calendar.","The week offered local fans top-tier grass-court tennis ahead of the season's Grand Slam."],
  "sources":[("Tennis Up To Date","https://tennisuptodate.com/wta/libema-open-s-hertogenbosch-wta-2026-entry-list-when-is-the-draw-confirmed-prize-money-history-and-predictions")]},
 {"sub":"Motorsport & Sailing",
  "h3":"Antonelli extends Mercedes grip on the F1 season",
  "summary":"Kimi Antonelli won in Montreal for his fourth victory of 2026, with Hamilton second and Verstappen third.",
  "body":["The Canadian Grand Prix result tightened Mercedes' hold on the championship, while Verstappen's first podium of the year offered Red Bull a glimmer of recovery.","Hamilton's runner-up finish kept Ferrari in the mix as the calendar moves on."],
  "sources":[("Bleacher Report","https://bleacherreport.com/articles/25430668-canadian-f1-grand-prix-2026-results-winner-standings-highlights-reaction")]},
 {"h3":"SailGP heads to Canada as Roos lead",
  "summary":"The Canada Sail Grand Prix is set for June 20 to 21 with the Australian team in front.",
  "body":["Tom Slingsby's Australia extended its SailGP championship lead with a strong showing in Bermuda, carrying momentum into the Canadian event.","The foiling circuit continues to draw growing audiences as it tours global venues."],
  "sources":[("Sail-World","https://www.sail-world.com/news/295980/Apex-Group-Bermuda-Sail-Grand-Prix-Overall")]},
 {"sub":"Grappling",
  "h3":"Grappling calendar packed as ADCC worlds loom",
  "summary":"June features the ADCC Dallas Open and Pan American championships, with the ADCC World Championships set for Krakow in September.",
  "body":["The biennial ADCC worlds will be held at Tauron Arena in Krakow on September 12 to 13, with a record total payout of $362,000, up from $230,600 previously.","ONE Championship also lined up Kade Ruotolo defending his lightweight submission grappling title against Fabricio Andrey on June 26."],
  "sources":[("FloGrappling","https://www.flograppling.com/articles/14526784-every-athlete-invited-to-adcc-world-championship-2026"),("MMA Mania","https://www.mmamania.com/bjj-news/405991/adcc-2026-fight-card-list-of-confirmed-bjj-stars-invited-to-the-adcc-world-championships")]},
],
"consumer-tech": [
 {"hero":True,"sub":"Software & Services",
  "h3":"Apple bets WWDC on a Gemini-powered Siri",
  "summary":"At WWDC 2026 Apple unveiled an AI strategy centered on a revamped Siri and practical features across iOS 27 and its other platforms.",
  "body":["The keynote, which opened June 8, emphasised everyday usefulness over flashy demos, with a much-anticipated Siri overhaul drawing on a custom Gemini model licensed from Google.","Apple spread updates across iOS 27, iPadOS 27, macOS 27, watchOS 27 and visionOS 27, framing the year as a steady rollout of AI capabilities people will actually use."],
  "sources":[("Bloomberg","https://www.bloomberg.com/news/articles/2026-06-09/apple-wwdc-2026-recap-everything-coming-to-iphone-mac-apple-watch-and-more"),("Tom's Guide","https://www.tomsguide.com/tech-events/apples-wwdc-2026-conference-kicks-off-in-june-heres-what-we-expect-to-see")]},
 {"h3":"iPhone Fold and iPhone 18 Pro line up for September",
  "summary":"Apple is set to reveal its first foldable and a new Pro flagship at its fall event.",
  "body":["Reports point to an iPhone Fold with a 7.6-inch interior screen and a rumored $2,500 price, alongside the iPhone 18 Pro, a new HomePod mini and an updated Apple TV 4K.","Combined with refreshes across AirPods, Apple Watch and iPad mini, 2026 is shaping up as Apple's most product-dense year in recent memory."],
  "sources":[("MacRumors","https://www.macrumors.com/roundup/wwdc/"),("Memeburn","https://memeburn.com/apples-15-new-product-leaks-ahead-of-wwdc-2026/")]},
 {"sub":"Devices & Launches",
  "h3":"Nvidia jumps into PCs with Arm-based laptop chip",
  "summary":"Nvidia unveiled an Arm-based PC chip, the RTX Spark Superchip, to power Windows laptops from Dell, HP and Microsoft.",
  "body":["The move extends Nvidia's ambition to win at every layer of the AI stack, taking it beyond data-center GPUs into consumer computing.","Devices using the new silicon are slated to debut as the company pushes AI features down to the laptop."],
  "sources":[("CNBC","https://www.cnbc.com/2026/06/02/nvidias-new-pc-chips-are-ceos-bid-to-own-every-part-of-ai-stack.html")]},
 {"h3":"Computex showcases liquid-cooled AI hardware",
  "summary":"Vendors at Computex 2026 leaned heavily into liquid cooling and Nvidia's MGX and DGX Station platforms.",
  "body":["MSI and Giga Computing showed next-generation AI infrastructure designs as thermal management becomes a defining constraint for dense compute.","The show underlined how AI demand is reshaping the entire hardware supply chain, from racks to cooling."],
  "sources":[("EQS News","https://www.eqs-news.com/news/corporate/msi-showcases-liquid-cooled-ai-infrastructure-nvidia-mgx-nvidia-dgx-station-and-dc-mhs-platforms-at-computex-2026/ed406797-7249-4f96-bf4b-4b1f93b7d7ff_en")]},
 {"sub":"EVs & Mobility",
  "h3":"Tesla retakes top EV spot as BYD sales slump",
  "summary":"Tesla delivered 358,023 EVs in Q1 2026, up 6.5 percent, while BYD's pure-EV sales fell 25 percent.",
  "body":["The swing handed Tesla back the global EV crown for the quarter, even as it faces pressure across valuation, demand and its robotaxi bets.","BYD's sharp decline highlighted how quickly competitive positions can shift in the EV market."],
  "sources":[("InsideEVs","https://insideevs.com/news/792143/tesla-no1-ev-maker-q1-2026/")]},
 {"h3":"Tesla Model 3 RWD named most efficient EV",
  "summary":"Edmunds testing crowned the 2026 Model 3 Rear-Wheel Drive the most efficient EV in production.",
  "body":["The test car traveled 393 miles on a charge against a 363-mile EPA rating, beating its official figure by 30 miles in real-world conditions.","Tesla also touts the upcoming Cybercab as its most efficient certified vehicle yet."],
  "sources":[("Not a Tesla App","https://www.notateslaapp.com/news/4290/tesla-model-3-named-most-efficient-ev-by-edmunds")]},
 {"h3":"Tesla develops smaller, cheaper EV after Model 2 shelved",
  "summary":"Tesla is reportedly working on a new compact, lower-cost model following the cancellation of the Model 2.",
  "body":["The effort signals Tesla's continued search for a volume-driving affordable car amid intensifying competition and slowing growth in some markets.","Details remain thin, but the project underscores pressure to broaden the lineup below current price points."],
  "sources":[("Electrek","https://electrek.co/2026/04/09/tesla-reportedly-developing-new-smaller-cheaper-ev-after-killing-model-2/")]},
],
}

MOOD = {"h3":"Sfeer vandaag","p":"Vroege zomer met spanning eronder: a warm Tuesday building toward 33C and weekend storms, the country easing into holiday mode while the Jetten minority cabinet juggles housing, asylum and a jittery world order. World Cup fever and grass-court tennis lift the mood, even as households keep one eye on prices and a fragile Middle East truce."}

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
