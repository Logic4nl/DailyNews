import html, json, sys

DATE_ISO = "2026-06-18"
DATE_HUMAN = "Thursday, June 18, 2026"
PREV_ISO = "2026-06-17"
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

MOOD = {"h3":"Sfeer vandaag","p":"Het is bloedheet in Amsterdam en de rest van het land, met temperaturen die richting de 35 graden kruipen en een code geel van het KNMI. Het nationale hitteplan is van kracht en veel mensen zoeken verkoeling langs de grachten en in de parken. Onder de zomerse drukte hangt een serieuze ondertoon, met het verdriet om het ongeluk in Zeeland en de aanhoudende spanning rond de asielopvang."}

DATA = {
"global": [
{"hero":True,"sub":"Conflicts & Security",
 "h3":"US releases 14-point Iran deal text as ceasefire holds",
 "summary":"Washington published the official memorandum with Tehran, easing some financial curbs and setting a path for nuclear talks after a months-long war.",
 "body":["The United States released the text of the so-called Islamabad Memorandum of Understanding with Iran on June 17, a 14-point document that loosens certain financial restrictions and lays out expectations for addressing Tehran's nuclear program in future technical talks. The agreement was formally signed in Switzerland and triggers a 60-day window to negotiate a final deal endorsed by the UN.","The final text added a methodology for neutralizing Iran's stockpile of highly enriched uranium by down-blending it under IAEA supervision. It also specified that Iran will let commercial vessels transit the Strait of Hormuz at no charge for 60 days, reopening a chokepoint whose closure had hit global growth projections."],
 "sources":[("CNN","https://www.cnn.com/2026/06/17/middleeast/us-iran-war-mou-text-intl"),("NPR","https://www.npr.org/2026/06/15/nx-s1-5858590/us-iran-deal-updates")]},
{"h3":"Russia pounds Ukrainian cities as war grinds on",
 "summary":"Fresh Russian strikes killed civilians in Kyiv and damaged a revered religious landmark while Ukraine kept hitting Russian oil infrastructure.",
 "body":["A wave of Russian strikes on Kyiv killed at least five people and wounded dozens, with missiles slamming into the Shevchenkivskyi district in under 30 minutes and setting an apartment tower and shops ablaze. Smoke rose around the golden domes of the Kyiv-Pechersk Lavra after its roof caught fire, an image Zelensky later showed Trump at the G7.","Ukraine kept up its own pressure, with drones striking the Russian port of Ust-Luga for the fifth time in ten days and complicating Moscow's crude oil exports. Russia's ground advance has stalled, a shift credited to Kyiv steadily strengthening its drone capabilities."],
 "sources":[("PBS NewsHour","https://www.pbs.org/newshour/world/russia-unleashes-an-overnight-barrage-on-ukraine-killing-11-people-and-damaging-a-religious-landmark-officials-say"),("Kyiv Independent","https://kyivindependent.com/explosions-rock-kyiv-amid-intelligence-warnings-of-russian-mass-attack/")]},
{"h3":"UN deploys gang-suppression force as Guterres visits Haiti",
 "summary":"The UN chief toured Port-au-Prince as a new multinational force takes shape against gangs that have displaced 1.5 million people.",
 "body":["Secretary-General Antonio Guterres visited Haiti on June 16 as gang violence pushed displacement to a record 1.5 million people, more than one in ten Haitians. UN figures show 2,300 people killed across the country so far this year, with more than 18,000 fleeing the Cite Soleil slum in May alone.","A new UN-approved gang-suppression force is being stood up to replace the underfunded Kenyan-led police mission. Jamaica, Chad, El Salvador and Guatemala have so far deployed fewer than 1,000 troops to the growing force."],
 "sources":[("UN News","https://news.un.org/en/story/2026/06/1167732"),("Euronews","https://www.euronews.com/2026/06/16/un-chief-visits-haiti-as-gang-violence-soars-and-number-of-displaced-hits-15-million")]},
{"h3":"Hezbollah and Israel trade strikes as Lebanon disarms",
 "summary":"Cross-border exchanges flared even as the Lebanese army said it had completed the first phase of a disarmament plan.",
 "body":["Israel and Hezbollah exchanged strikes as the wider regional conflict simmered, with the group framing its rocket fire as a defensive response to more than a year of Israeli attacks despite a 2024 truce. Hezbollah said it acted to force Israel to halt aggression and leave seized Lebanese territory.","At the same time the Lebanese army announced it had completed the first phase of a plan to disarm armed groups, a step closely watched by mediators trying to stabilize the country's south and prevent a slide back into full-scale war."],
 "sources":[("CNN","https://www.cnn.com/2026/06/07/world/live-news/iran-war-trump-israel-lebanon")]},
{"h3":"Congo and M23 set to resume peace talks in Switzerland",
 "summary":"Mediators prepared a new round of negotiations as clashes continued across North and South Kivu.",
 "body":["The Congolese government and the M23 rebel group are expected to resume peace talks in Switzerland soon, building on a framework agreement signed in November to end their conflict in eastern DRC. US and Swiss mediators have focused talks on implementation, including the contested Rubaya mining site.","On the ground the fighting has not stopped, with Kinshasa building up troops in North and South Kivu and pro-government forces clashing with M23-aligned militias near the Masisi-Walikale border and in the South Kivu highlands."],
 "sources":[("International Crisis Group","https://www.crisisgroup.org/rpt/africa/democratic-republic-congo-rwanda/320-m23-offensive-elusive-peace-great-lakes")]},
{"sub":"Diplomacy & Trade",
 "h3":"G7 leaders vow unwavering support for Ukraine",
 "summary":"At the Evian summit the G7 pledged more air defenses for Kyiv and tougher sanctions on Russian oil and gas.",
 "body":["G7 leaders meeting in Evian, France declared unwavering support for Ukraine, agreeing to step up air defense deliveries and increase economic pressure on Moscow. Their joint statement committed to strengthening Russian sanctions, including measures targeting the oil and gas sectors.","Zelensky met Trump and Macron on the sidelines for about 30 minutes, showing Trump photographs of damage to the Kyiv-Pechersk Lavra. Zelensky said partners had agreed on both air defense systems and missiles to bolster Ukraine's protection."],
 "sources":[("CNN","https://www.cnn.com/2026/06/16/world/live-news/iran-war-g7-summit"),("Kyiv Independent","https://kyivindependent.com/zelensky-trump-macron-hold-behind-the-scenes-meeting-at-g7-summit/")]},
{"h3":"Trump signals new tariffs on autos, drugs and aluminum",
 "summary":"The president said fresh duties were coming soon, framing them as a national security necessity for wartime supply chains.",
 "body":["Trump said the US would impose tariffs on autos, pharmaceuticals and aluminum in the near future, arguing the country would need to make all those products in the event of wars or other crises. The remarks extend a tariff push that already includes 25 percent duties on foreign cars and parts.","The administration has separately layered duties of up to 100 percent on patented pharmaceutical imports and 50 percent on goods made entirely of aluminum. Officials have ranked auto tariffs as their top trade priority for 2026."],
 "sources":[("The White House","https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-updates-tariffs-on-steel-aluminum-and-copper-imports/")]},
{"h3":"EU and US complete tariff deal capping duties at 15 percent",
 "summary":"Brussels moved to ratify rules implementing the transatlantic trade pact, scrapping most EU duties on American goods.",
 "body":["The EU finalized the legal machinery for its trade deal with Washington, with the Council and Parliament agreeing on regulations to implement the tariff elements of the joint statement. The pact eliminates EU tariffs on most US industrial and agricultural goods while the US caps tariffs on European imports at 15 percent.","Lawmakers strengthened the package with a safeguard mechanism, a reinforced suspension clause and a sunset clause. Washington must cut derivative tariffs to 15 percent or less by the end of 2026 or the EU can suspend concessions on targeted American products."],
 "sources":[("Consilium","https://www.consilium.europa.eu/en/press/press-releases/2026/05/20/eu-us-trade-council-and-parliament-strike-a-deal-to-implement-the-tariff-elements-of-the-joint-statement/")]},
{"h3":"Egypt presses Israel to drop plan to hold most of Gaza",
 "summary":"Cairo urged Israel to abandon a push to control 70 percent of the enclave as the fragile ceasefire frayed.",
 "body":["Egyptian President Abdel-Fattah el-Sissi urged Israel on June 17 to abandon its plan to take control of 70 percent of Gaza, as witnesses reported Israeli forces pushing forward the Yellow Line dividing the territory. The October 2025 ceasefire has grown increasingly fragile.","Talks to disarm armed groups have not produced an agreement, raising the risk of renewed fighting. Hamas has rejected a sequenced disarmament plan, conditioning any move on Israel halting operations, allowing full humanitarian aid and providing international guarantees."],
 "sources":[("UN","https://press.un.org/en/2026/sc16284.doc.htm")]},
{"h3":"Xi meets Taiwanese politician in rare cross-strait outreach",
 "summary":"Beijing courted amenable Taiwanese figures while conducting maritime law enforcement drills east of the island.",
 "body":["Xi Jinping held a meeting with a Taiwanese politician, the first such encounter since 2016, as Beijing sought to present cross-strait engagement positively to Taiwan's public ahead of November local elections. The visitor voiced support for the 1992 consensus as a path to cross-strait peace.","Even while courting sympathetic politicians, Beijing flexed its muscles, with the PRC Ministry of Transport conducting a maritime law enforcement operation east of Taiwan to assert its territorial claims."],
 "sources":[("AEI","https://www.aei.org/articles/china-taiwan-update-june-12-2026/")]},
{"sub":"Humanitarian & Climate",
 "h3":"UN says 239 million people need aid in 2026",
 "summary":"The Global Humanitarian Overview warns a quarter of a billion people need help as funding hits a decade low.",
 "body":["The UN's Global Humanitarian Overview for 2026 estimates 239 million people need urgent assistance, following a 2025 marked by deep cuts to aid operations and a record number of deadly attacks on aid workers. Funding has fallen to its lowest level in a decade even as needs climb.","The UN says it needs 23 billion dollars to meet the most urgent needs and aims to save 87 million lives across 50 countries. Crises are intensifying as protracted conflicts, climate shocks and economic fragility drive record displacement and a growing hunger emergency."],
 "sources":[("OCHA","https://www.unocha.org/publications/report/world/global-humanitarian-overview-2026-enesfr")]},
{"h3":"Sudan famine deepens as war enters fourth year",
 "summary":"Aid agencies warn 33.7 million Sudanese will need help in 2026 with famine declared and El Fasher cut off.",
 "body":["The World Food Programme projects 33.7 million Sudanese will require humanitarian aid in 2026 as the civil war grinds into its fourth year and aid dwindles. Famine has been declared in two states with 20 more facing severe threats, including El Fasher and Kadugli.","A UN Fact-Finding Mission found the Rapid Support Forces acted with intent to destroy the Zaghawa and Fur communities in El Fasher, evidence bearing the hallmarks of genocide. The city remains largely cut off from humanitarian access after its fall to the RSF."],
 "sources":[("Health Policy Watch","https://healthpolicy-watch.news/sudans-catastrophic-civil-war-enters-fourth-year/")]},
{"h3":"Europe swelters under record-breaking early heatwave",
 "summary":"An exceptionally early heat dome smashed temperature records and triggered wildfires across the continent.",
 "body":["An unusually early and intense heatwave has gripped much of Europe since late May, shattering records in Spain, the UK, Germany, France and Ireland with temperatures running 10 to 15 degrees Celsius above normal. France's weather service said a heat dome pushed readings more than 10 degrees above average, while Portugal hit 40.3 degrees.","Scientists link the early onset to climate change, noting that breaking May temperature records has shifted from a roughly 1-in-100-year event to about 1-in-33. The heat has been tied to at least 12 deaths in the UK and sparked wildfires, including near Arthur's Seat in Edinburgh."],
 "sources":[("Carbon Brief","https://www.carbonbrief.org/cited-9-june-2026-europes-exceptional-heatwave-warming-forecast-amoc-observations-at-risk/")]},
{"h3":"Myanmar crisis leaves 16 million needing aid",
 "summary":"The UN warns of an almost invisible crisis as war and last year's earthquake keep millions in urgent need.",
 "body":["More than 16.2 million people in Myanmar, including 4.9 million children, remain in urgent need of humanitarian support as the country reels from expanding armed conflict and recovery from the deadly March 2025 earthquake that killed more than 3,800 people. The 2026 response plan spans two-thirds of the country's townships.","Aid delivery is repeatedly blocked by fighting, checkpoints and administrative delays, and in 2025 only about a quarter of the required funds arrived. The UN has prioritized 2.6 million people with the most severe needs at a cost of 521 million dollars."],
 "sources":[("UN News","https://news.un.org/en/story/2025/12/1166618")]},
{"h3":"Climate-driven needs surge in humanitarian appeals",
 "summary":"The UN reports a steep rise in climate-related needs as intensifying shocks compound conflict and displacement.",
 "body":["UN agencies report an 800 percent increase in climate-related needs within humanitarian appeals since 2000, as intensifying climate shocks compound conflict and economic fragility. More than 117 million people remain forcibly displaced worldwide.","The 2026 appeals reflect the strain, with 2.8 billion dollars sought for 20 million people in Sudan and 1.4 billion to reach nearly five million people affected by the Myanmar crisis."],
 "sources":[("ReliefWeb","https://reliefweb.int/topics/climate-change-and-humanitarian-assistance")]},
],
"netherlands": [
{"hero":True,"sub":"Politics & Policy",
 "h3":"Netherlands pledges 500 million euros in new arms for Ukraine",
 "summary":"The Dutch cabinet unveiled a fresh military aid package for Ukraine focused on drones and air defence, lifting its total PURL contribution to 1 billion euros.",
 "body":["Defence Minister Dilan Yesilgoz announced the 500 million euro package on June 17 during talks with her Ukrainian counterpart Mykhailo Fedorov. Half the money will buy drones from Dutch manufacturers, while the other half flows into the US-led PURL program that funds American-made weapons for Kyiv.","The pledge brings the Netherlands' total commitment to the PURL initiative to 1 billion euros. The country signed a ten-year security partnership with Ukraine in 2024 and has stayed among Kyiv's most consistent backers through more than four years of war."],
 "sources":[("NL Times","https://nltimes.nl/2026/06/17/netherlands-announces-eu500-million-military-aid-package-ukraine")]},
{"h3":"Senate clears ban on gay conversion therapy",
 "summary":"A broad majority of senators backed a law criminalising attempts to change a person's sexual orientation, with penalties of up to two years in prison.",
 "body":["The Senate approved the bill on June 16 with 57 of 75 senators in favour, after a coalition including D66, VVD and the Partij voor de Dieren pushed it forward. The law targets practices aimed at minors and adults in vulnerable situations.","Violators face fines of up to 27,500 euros or as much as two years behind bars, and professionals involved could lose their right to practise. Supporters cited research linking conversion practices to depression and suicidal thoughts. The measure takes effect once the king grants royal assent."],
 "sources":[("NL Times","https://nltimes.nl/2026/06/16/netherlands-bans-gay-conversion-therapy-senate-majority-backs-new-law")]},
{"h3":"Solvinity appeals block on US takeover of DigiD operator",
 "summary":"The firm behind the DigiD login platform is challenging the cabinet's decision to bar its sale to US cloud company Kyndryl on national security grounds.",
 "body":["Junior digital sovereignty minister Willemijn Aerdts blocked the 100 million euro takeover last month after the investment-vetting agency flagged risks tied to US data law. Solvinity and its majority owner, British firm Vitruvian Partners, have now filed an appeal seeking clarity on the legal basis.","Officials feared the US CLOUD Act could let Washington demand access to DigiD data after an acquisition. The US ambassador criticised the ban, suggesting it amounted to a non-tariff barrier of the kind Donald Trump has used to justify retaliatory tariffs."],
 "sources":[("NL Times","https://nltimes.nl/2026/06/17/solvinity-company-behind-digid-appeals-government-ban-us-takeover")]},
{"h3":"Jetten set to apologise to Moluccan community at new monument",
 "summary":"The prime minister is expected to apologise for the state's treatment of Moluccan migrants when he unveils a monument in Rotterdam this weekend.",
 "body":["The monument stands at the former Lloyd Yard docks, where nearly 13,000 Moluccan soldiers and their families first arrived in the early 1950s after fighting alongside the Dutch in Indonesia. They expected a temporary stay and a promised homeland that never came.","Demobilised soldiers were housed in camps, including the former wartime sites at Westerbork and Vught, and dismissed from the army regardless of years served. A majority of MPs this week backed a motion calling for an appropriate gesture and an investigation into their treatment."],
 "sources":[("DutchNews.nl","https://www.dutchnews.nl/2026/06/jetten-likely-to-apologise-to-moluccans-at-unveiling-of-monument/")]},
{"sub":"Economy & Housing",
 "h3":"House price rises finally slow as supply climbs",
 "summary":"Fresh CBS and NVM figures point to month-on-month stabilisation in home prices, though regional gaps remain wide.",
 "body":["The national statistics agency CBS and estate agent association NVM both report that price growth is cooling, with the annual index easing to around 5 percent in March from above 8 percent in 2025. NVM noted fewer viewings and bids per home as buyers turn cautious.","More homes are reaching the market as landlords offload smaller properties under rent caps and higher taxes. Even so, a persistent structural shortage continues to keep prices elevated."],
 "sources":[("DutchNews.nl","https://www.dutchnews.nl/2026/06/dutch-housing-update-tips-tests-and-the-latest-news/")]},
{"h3":"Inflation jumps to 3.5 percent, highest in a year",
 "summary":"Dutch annual inflation accelerated in May, driven mainly by sharply higher transport and flight costs.",
 "body":["CBS data show consumer prices rose 3.5 percent year on year in May, up from 2.8 percent in April and the highest reading since the previous spring. Transport inflation led the way at 9.9 percent, fuelled by costlier international flights.","Forecasters expect inflation to average above 3 percent across 2026 as energy prices climb. The pickup complicates the picture for households already squeezed by housing costs."],
 "sources":[("CBS","https://www.cbs.nl/en-gb/visualisations/economy-dashboard/inflation")]},
{"h3":"Quarter-million young workers stuck with too few hours",
 "summary":"A new study finds many under-30s want more work than their contracts allow, exposing a mismatch in the labour market.",
 "body":["Nearly 250,000 young people would prefer to work more hours than they are currently contracted, according to research published on June 17. More than two-thirds of employees under 30 would rather work full-time, yet only just over half actually do.","The gap is especially acute for those juggling jobs with study. Researchers say the findings highlight how flexible and part-time arrangements leave many young workers short of the income and stability they want."],
 "sources":[("NL Times","https://nltimes.nl/2026/06/17/quarter-million-young-workers-stuck-contracts-hours-study-finds")]},
{"sub":"Society & Culture",
 "h3":"Heat plan activated nationwide as temperatures near 35C",
 "summary":"Public health authorities triggered the national heat plan from Thursday, with KNMI issuing a code yellow warning across most of the country.",
 "body":["The RIVM activated the plan after consulting the KNMI, which forecasts highs of up to 35 degrees on Friday and again on Monday. A code yellow warning covers the whole country except the Wadden Islands, citing warm nights and high humidity.","The plan kicks in when at least four straight days above 27 degrees are expected. Officials warned that prolonged heat raises the risk of fatigue, dehydration and heatstroke, especially for vulnerable groups."],
 "sources":[("NL Times","https://nltimes.nl/2026/06/17/nationwide-heat-plan-effect-thursday-temperatures-soar-netherlands")]},
{"h3":"Teen driver faces negligence charge in deadly Zeeland crash",
 "summary":"Prosecutors allege negligence after a car ploughed into a school cycling group near Vogelwaarde, killing three children and a school principal.",
 "body":["The crash on June 11 hit a group of 14 pupils and two supervisors from a primary school in Axel during a school camp trip. The principal of school De Warande was among the four people killed and several others were injured.","A 19-year-old man from Hulst has been formally charged with causing a fatal crash through negligence. Investigators are examining the vehicle's speed and whether alcohol, drugs or distraction played a role."],
 "sources":[("NL Times","https://nltimes.nl/2026/06/16/negligence-alleged-crash-killed-3-kids-school-principal-biking-zeeland")]},
{"h3":"Over a million Dutch now rely only on social media for news",
 "summary":"A new report finds a growing slice of the population gets news solely from social platforms despite low trust in what they see there.",
 "body":["More than a million people, about 7 percent of adults, now use no news sites, television or radio and depend entirely on social media, up from 2 percent in 2018. Yet only 12 percent say they trust the news they encounter on those platforms.","The trend raises concerns about misinformation and the erosion of shared facts. Researchers warn the shift is especially pronounced among younger audiences."],
 "sources":[("DutchNews.nl","https://www.dutchnews.nl/2026/06/over-a-million-dutch-now-rely-only-on-social-media-for-news/")]},
{"h3":"Small group blamed for surge in violent anti-asylum protests",
 "summary":"An analysis concludes that a limited core of agitators is behind a nationwide wave of violent demonstrations against asylum reception.",
 "body":["Recent protests have turned destructive, including an incident in Loosdrecht where demonstrators set fire to shrubs around a reception building and obstructed firefighters. Prime Minister Rob Jetten condemned the acts as utterly scandalous.","The findings come as refugee agency COA scrambles to house tens of thousands of people this year amid a large shortfall in available places. Officials say the violence is driven by a small but determined group rather than broad public sentiment."],
 "sources":[("DutchNews.nl","https://www.dutchnews.nl/2026/05/arson-and-arrests-as-anti-asylum-protests-escalate/")]},
],
"ai-hpc": [
{"hero":True,"sub":"AI/HPC Stocks & Infrastructure",
 "h3":"AI lab CEOs meet G7 leaders, push US-led AI coalition",
 "summary":"Altman, Amodei and Hassabis sat down with world leaders at the G7 summit in France, the first time the three rival lab chiefs appeared together before heads of state.",
 "body":["At the G7 summit in Evian, the heads of OpenAI, Anthropic and Google DeepMind discussed frontier model risks and global standards with President Trump, Emmanuel Macron, Keir Starmer and Friedrich Merz. Amodei and Hassabis called for a US-led coalition that would coordinate chip trade and structured access to advanced models while excluding China.","Altman floated the idea of an international forum, potentially helmed by the US, to set standards for the most capable systems. The leaders also raised cooperation on cyber, bioterrorism and intelligence risks tied to increasingly autonomous AI."],
 "sources":[("CNBC","https://www.cnbc.com/2026/06/17/anthropic-amodei-google-hassabis-us-ai-coalition-g7.html"),("Semafor","https://www.semafor.com/article/06/17/2026/ai-ceos-talk-global-standards-at-g7")]},
{"h3":"Anthropic hits 965B valuation, files confidentially for IPO",
 "summary":"Anthropic closed a financing round valuing it at 965 billion dollars, eclipsing OpenAI, with run-rate revenue past 30 billion and a confidential IPO filing.",
 "body":["The new round vaults Anthropic ahead of OpenAI on paper as its annualized revenue climbed from roughly 9 billion dollars at the end of 2025 to over 30 billion. The number of customers spending more than 1 million dollars a year topped 1,000, doubling in under two months.","Google made a 40 billion dollar investment as part of a deepening relationship spanning Google Cloud TPU capacity and a Broadcom partnership for multiple gigawatts of next-generation compute. Anthropic has confidentially filed paperwork for a public listing."],
 "sources":[("Anthropic","https://www.anthropic.com/news/google-broadcom-partnership-compute")]},
{"h3":"Apollo leads 35B financing for Broadcom AI compute platform",
 "summary":"Apollo, Blackstone and a bank syndicate assembled a 35 billion dollar asset-backed package for Broadcom's new XPV platform targeting more than 20GW of frontier-lab compute.",
 "body":["The structure bundles custom chips, networking, power infrastructure and long-duration customer commitments into a single asset-backed mechanism aimed at frontier AI labs through 2028. It reflects how financing for AI buildouts has moved toward project-finance style vehicles rather than pure equity.","The deal lands as a full gigawatt of AI data center capacity now runs around 100 billion dollars to build, and US data center electricity demand has jumped from 23GW in 2023 to 42GW in 2026."],
 "sources":[("NextBigFuture","https://www.nextbigfuture.com/2026/06/power-is-everything-in-ai-100-billion-per-gigawatt-of-data-center.html")]},
{"h3":"CoreWeave and Nebius join Nasdaq-100 amid neocloud surge",
 "summary":"The two neocloud providers were added to the Nasdaq-100 in June, capping a run of multibillion-dollar capacity deals with Meta and OpenAI.",
 "body":["CoreWeave expects 12 to 13 billion dollars in 2026 revenue, lifted by an additional 21 billion dollar Meta capacity deal running through 2032 plus its OpenAI work. Nebius plans to scale connected capacity from 170MW to between 800MW and 1GW by year end.","Meta separately signed a five-year, 27 billion dollar agreement with Nebius that includes one of the first large-scale deployments of Nvidia's Vera Rubin platform. The index addition signals how central these specialist GPU clouds have become to AI infrastructure."],
 "sources":[("TIKR","https://www.tikr.com/blog/nebius-and-coreweave-nasdaq-nbis-crwv-stocks-surge-following-announcement-of-nasdaq-100-addition")]},
{"h3":"Nvidia ships Spectrum-X photonics for Vera Rubin AI factories",
 "summary":"Nvidia said its Spectrum-X Ethernet photonics built on co-packaged optics has entered full production for scale-out deployments on the Vera Rubin platform.",
 "body":["The new switching generation targets scale-out and scale-across connectivity in the large AI factories now being built around Vera Rubin. CoreWeave plans to integrate Rubin-based systems into its cloud in the second half of 2026 for training, inference and agentic workloads.","Anthropic, OpenAI and SpaceX are among the first users of Nvidia's Vera CPU, which enters full production in the third quarter. The first gigawatt of the OpenAI partnership deploys on Vera Rubin later this year."],
 "sources":[("Nvidia","https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/")]},
{"sub":"Foundation Models & Releases",
 "h3":"OpenAI eyes late-June GPT-5.6 as a meaningful leap",
 "summary":"Chief scientist Jakub Pachocki told staff GPT-5.6 will be a meaningful improvement over GPT-5.5, with a launch expected in late June.",
 "body":["Sources point to gains centered on agentic workflows and a further 10 to 15 percent token-efficiency improvement rather than single-turn chat, alongside a context window expanding toward 1.5 million tokens. The cadence follows GPT-5.4 in March and GPT-5.5 in April, putting 5.6 roughly six to seven weeks later.","Prediction markets priced the June 22 to 28 window at over 80 percent probability, with Polymarket volume exceeding 1 million dollars. OpenAI had not confirmed an official date as of June 16."],
 "sources":[("TechTimes","https://www.techtimes.com/articles/318492/20260616/gpt-56-openai-chief-scientist-calls-it-meaningful-leap-june-launch-nears.htm")]},
{"h3":"Nvidia opens Cosmos 3 world model for physical AI",
 "summary":"Nvidia launched Cosmos 3, an open frontier foundation model that unifies vision reasoning, world generation and action prediction for robotics and autonomous vehicles.",
 "body":["Built on a mixture-of-transformers architecture, Cosmos 3 natively understands and generates text, image, video, ambient sound and actions, cutting physical AI training and evaluation cycles from months to days. Variants include Cosmos 3 Super for high-accuracy robotics, Nano for fast video and action reasoning, and an upcoming Edge tier.","Nvidia also formed a Cosmos Coalition with labs and robotics firms including Black Forest Labs, Runway, Skild AI and Generalist to push open world models forward."],
 "sources":[("HPCwire","https://www.hpcwire.com/aiwire/2026/06/01/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai/")]},
{"h3":"Microsoft launches seven in-house MAI models",
 "summary":"Microsoft unveiled a family of seven home-grown MAI models, including its first reasoning model, as it reduces reliance on OpenAI and cuts developer costs.",
 "body":["The lineup includes MAI-Thinking-1 for reasoning and software engineering, MAI-Code-1-Flash for turning descriptions into application code, MAI-Voice-2 with emotional control across 15 languages, and MAI-Image-2.5, which scored well on image-editing leaderboards.","The release, tied to Microsoft Build, signals a strategy to diversify model options inside Foundry beyond its OpenAI partnership while lowering costs for developers."],
 "sources":[("Microsoft AI","https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/")]},
{"h3":"Anthropic ships Claude Fable 5",
 "summary":"Anthropic released Claude Fable 5 on June 9, the latest entry in a fast-moving stretch of frontier model launches across the major labs.",
 "body":["The release lands amid an unusually dense run of model drops, with Microsoft, Nvidia and Chinese labs all pushing new systems within days of each other. It extends Anthropic's lineup as the company leans into enterprise demand that has driven revenue past a 30 billion dollar run rate.","Anthropic is simultaneously locking in compute through expanded Google Cloud TPU capacity and a Broadcom partnership covering multiple gigawatts."],
 "sources":[("LLM-Stats","https://llm-stats.com/llm-updates")]},
{"sub":"Chinese AI Ecosystem",
 "h3":"DeepSeek V4 sparks scramble for Huawei Ascend chips",
 "summary":"DeepSeek's V4 release, optimized for Huawei's Ascend processors rather than Nvidia, triggered a procurement rush among ByteDance, Tencent and Alibaba.",
 "body":["DeepSeek shipped V4-Pro, which it says rivals top closed models, and a cheaper V4-Flash, both tuned for Huawei's Ascend 950. The shift away from Nvidia hardware marks a notable departure for the Hangzhou startup and sent SMIC shares up 10 percent in Hong Kong.","US restrictions on advanced chipmaking tools are now constraining Huawei's ability to meet the very demand it helped create. DeepSeek expects supply to stay tight until Ascend production ramps later in 2026."],
 "sources":[("Capacity","https://capacityglobal.com/news/deepseek-v4-triggers-scramble/")]},
{"h3":"Chinese open models capture 45 percent of OpenRouter traffic",
 "summary":"Combined Chinese AI providers crossed 45 percent of OpenRouter traffic, up from under 2 percent a year earlier, as open models from DeepSeek and Qwen surge globally.",
 "body":["Chinese open-source models such as DeepSeek and Alibaba's Qwen now account for around 30 percent of all AI model downloads worldwide, surpassing the United States. Labs close to the frontier now include Qwen, ByteDance's Doubao, Moonshot's Kimi, MiniMax and Zhipu's Z.ai.","The momentum follows a year of accelerated releases since the original DeepSeek shock, with Chinese firms racing to ship cheaper, openly licensed systems."],
 "sources":[("Digital Applied","https://www.digitalapplied.com/blog/chinese-ai-models-q2-2026-market-share-report")]},
{"h3":"Alibaba pushes Qwen toward trillion-parameter multimodal era",
 "summary":"Alibaba is scaling its Qwen line toward a fully multimodal Qwen 4 spanning 100B to trillion-class parameters after shipping a 1M-token agentic-coding update.",
 "body":["Qwen 3.6 Plus brought a default 1M-token context window and stronger agentic coding earlier this year, with Qwen 4 expected across the second and third quarters. Alibaba also revealed a text-to-video model that topped blind-test rankings for video generation.","The roadmap underscores Alibaba's bid to stay at the open-model frontier as Chinese labs collectively gain share against US incumbents."],
 "sources":[("CNBC","https://www.cnbc.com/2026/01/28/chinese-tech-companies-accelerate-ai-model-rollouts-us-rivals-deepseek-moonshot-kimi.html")]},
{"sub":"Agents & Automation",
 "h3":"OpenAI debuts Deployment Simulation to catch model drift",
 "summary":"OpenAI introduced Deployment Simulation, replaying real past conversations with a new candidate model to predict undesired behaviors before release.",
 "body":["The privacy-preserving method replays exactly the contexts users brought to prior models instead of synthetic prompts, surfacing how a candidate might behave in the wild. OpenAI validated it across roughly 1.3 million de-identified conversations spanning GPT-5 Thinking through GPT-5.4.","The company says the technique beats baselines at predicting whether a behavior will rise or fall after launch, addressing the evaluation gap flagged in the International AI Safety Report 2026."],
 "sources":[("OpenAI","https://openai.com/index/deployment-simulation/")]},
{"h3":"Nvidia launches open platform to agentize knowledge work",
 "summary":"Nvidia rolled out an open agent development platform aimed at building autonomous systems for knowledge work across enterprises.",
 "body":["The platform packages tools for agents with goals, memory, planning and tool use, slotting into a market where AWS, Google Cloud, Microsoft, GitHub and Databricks now describe agents in similar terms. It arrives as the Model Context Protocol gains traction as an open standard for connecting agents to enterprise data.","Gartner expects 40 percent of enterprise applications to embed task-specific agents in 2026, though fewer than 10 percent of enterprises have yet scaled agents to real production value."],
 "sources":[("Nvidia","https://nvidianews.nvidia.com/news/ai-agents")]},
{"h3":"GitHub Copilot moves to usage-based AI Credits billing",
 "summary":"GitHub switched Copilot to usage-based AI Credits on June 1 and added a 100 dollar Copilot Max tier, unsettling power users of agentic coding.",
 "body":["Sticker prices held across Pro, Pro+, Business and Enterprise plans, but each now functions as a monthly credit allowance, with Copilot Max offering 20,000 credits for heavy workloads. Agentic coding makes consumption harder to predict, fueling cost anxiety among the heaviest users.","Copilot still leads on share with roughly 42 percent of paid tools and 20 million users, even as Cursor scaled from 100 million to 1 billion dollars in annual recurring revenue in a year."],
 "sources":[("New Market Pitch","https://newmarketpitch.com/blogs/news/ai-code-assistant-cursor-vs-github-copilot")]},
{"sub":"Enterprise & Regulation",
 "h3":"EU publishes AI content-labelling code before August deadline",
 "summary":"The European Commission released a Code of Practice on marking AI-generated content on June 10, a key milestone ahead of the AI Act becoming fully applicable in August.",
 "body":["The code arrives as companies brace for August 2 transparency and high-risk obligations covering systems used in critical infrastructure, employment, essential services and law enforcement. Persistent uncertainty over possible delays is forcing firms to decide whether to pause or rush compliance work.","Pre-launch legal reviews have become standard for EU-facing AI releases, with technical documentation now built into product development rather than written after the fact."],
 "sources":[("European Commission","https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai")]},
{"h3":"OpenAI spins up a Deployment Company for enterprises",
 "summary":"OpenAI launched a dedicated Deployment Company to help businesses build production systems around its models.",
 "body":["The new unit targets enterprises struggling to move from pilots to scaled value, packaging integration and operational support around OpenAI's models. It dovetails with the broader market shift in which implementation and tuning costs dwarf raw license spend.","The move positions OpenAI to capture more of the services layer as agentic deployments become the main driver of enterprise AI value."],
 "sources":[("OpenAI","https://openai.com/index/openai-launches-the-deployment-company/")]},
{"h3":"Colorado AI Act takes effect as state rules multiply",
 "summary":"Colorado's AI Act takes effect June 30, part of a fast-moving patchwork of US state AI laws layered atop federal direction.",
 "body":["California, New York, Utah, Nevada, Maine and Illinois have all enacted significant AI legislation, leaving the US landscape multi-layered across executive direction, agency memos, procurement rules and state statutes. Colorado's law is among the most closely watched for its high-risk system obligations.","The fragmentation pushes enterprises toward standardized governance frameworks to manage compliance across overlapping jurisdictions."],
 "sources":[("Gunderson Dettmer","https://www.gunder.com/en/news-insights/insights/2026-ai-laws-update-key-regulations-and-practical-guidance")]},
{"sub":"AI/HPC Stocks & Infrastructure",
 "h3":"Meta forms Meta Compute unit for gigawatt-scale data centers",
 "summary":"Meta established a dedicated Meta Compute organization and laid out plans for multiple gigawatt-plus AI data centers.",
 "body":["The new unit centralizes Meta's sprawling compute buildout as it commits tens of billions to neocloud partners including CoreWeave and Nebius. Its Nebius agreement features one of the first large-scale Vera Rubin deployments.","The reorganization underscores how hyperscalers are treating compute as a distinct strategic pillar amid surging demand and record capital spending."],
 "sources":[("Data Center Dynamics","https://www.datacenterdynamics.com/en/news/meta-establishes-meta-compute-plans-multiple-gigawatt-plus-scale-ai-data-centers/")]},
{"h3":"TSMC lifts 2026 outlook as 2nm node ramps",
 "summary":"TSMC raised its 2026 outlook on durable AI demand, with May revenue up 30 percent year over year as its N2 process begins contributing.",
 "body":["The foundry's 2nm node started generating revenue in March, opening one of the most consequential transitions in chip history, with Apple expected first and Nvidia and AMD set to follow for next-generation accelerators. Revenue for January through May rose 30 percent from a year earlier.","Deloitte projects global semiconductor sales to hit a record 975 billion dollars in 2026, with the AI boom still dominating the industry narrative despite a brief June sector sell-off."],
 "sources":[("CNBC","https://www.cnbc.com/2026/04/16/tsmc-q1-profit-58-percent-ai-chip-demand-record.html")]},
{"h3":"Google to power next Siri and ships Gemini Enterprise agents",
 "summary":"Google confirmed the next Apple Siri will run on Gemini and launched its Gemini Enterprise Agent Platform as it deepens enterprise AI reach.",
 "body":["The Siri deal hands Google a marquee placement on hundreds of millions of devices, while the Gemini Enterprise Agent Platform targets businesses building agentic workflows. Both moves accompany Google's 40 billion dollar investment in Anthropic.","Together they show Google pressing on consumer distribution and enterprise tooling at once, even as it remains a major compute supplier to a rival lab."],
 "sources":[("AI Weekly","https://aiweekly.co/ai-news-today/google-ai-news")]},
],
"crypto-macro": [
{"hero":True,"sub":"Macro & Central Banks",
 "h3":"Fed holds rates but flags 2026 hike in Warsh's first meeting",
 "summary":"The Federal Reserve kept rates at 3.5 to 3.75 percent on June 17 but lifted its dot plot sharply, with nine of 18 officials projecting a hike before year end.",
 "body":["In Kevin Warsh's first meeting as chair the FOMC voted 12-0 to hold the federal funds target at 3.5 to 3.75 percent, but the updated projections turned notably hawkish. The median end-2026 rate rose to 3.8 percent from 3.4 percent in March, and nine of the eighteen members now pencil in at least one rate hike this year.","Officials cited inflation still running above the 2 percent goal, partly driven by energy and supply shocks tied to the Middle East conflict. The 10-year Treasury yield erased earlier losses to sit near 4.46 percent, while markets began pricing in a possible hike later in 2026."],
 "sources":[("Federal Reserve","https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm"),("CNBC","https://www.cnbc.com/2026/06/17/fed-interest-rate-decision-june-2026.html")]},
{"h3":"ECB raises rates for first time in three years on Iran shock",
 "summary":"The ECB lifted its three key rates by 25bps effective June 17, pushing the deposit rate to 2.25 percent as Middle East conflict fuels eurozone price pressures.",
 "body":["The European Central Bank delivered its first rate increase since its tightening cycle ended in September 2023, raising the deposit facility rate to 2.25 percent, the main refinancing rate to 2.40 percent and the marginal lending rate to 2.65 percent. The bank framed the move as robust across scenarios for how the Middle East shock might evolve.","Flash eurozone inflation hit 3.2 percent in May, the highest since September 2023, with core inflation climbing to 2.5 percent. New staff projections see headline inflation averaging 3.0 percent in 2026 before easing toward target by 2028."],
 "sources":[("European Central Bank","https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html")]},
{"h3":"US retail sales jump 0.9 percent in May",
 "summary":"American consumers spent a stronger than expected 763.7 billion dollars in May, with broad gains that fed into a 2.8 percent Q2 GDP tracker reading.",
 "body":["Retail and food services sales rose 0.9 percent in May to 763.7 billion dollars, nearly double what economists had penciled in. Online sales climbed 1.5 percent and clothing and furniture stores posted gains, though electronics and department stores slipped.","Tax refunds in April and May boosted spending, though economists warn that cushion is fading. The Atlanta Fed GDP tracker showed the economy growing at a 2.8 percent annualized pace in the second quarter, reinforcing the Fed's view that activity remains solid."],
 "sources":[("US News","https://money.usnews.com/investing/news/articles/2026-06-17/us-retail-sales-beat-expectations-in-may")]},
{"h3":"Oil holds below 100 dollars as Iran war keeps markets on edge",
 "summary":"Crude stayed under 100 dollars a barrel through mid-June as traders priced a long grind in the Middle East rather than a full supply shock.",
 "body":["Oil traded up about 2 percent in mid-June but stayed below 100 dollars, with traders judging there were enough supply buffers to avoid a full-blown shock. Reports of an interim US-Iran peace deal eased some of the pressure on energy and risk assets.","Investors have shifted from treating the conflict as a temporary inflation spike to pricing a prolonged standoff. Fitch warned the war could weaken global growth, lift inflation and bond yields, and raise the odds of higher rates for longer."],
 "sources":[("Morgan Stanley","https://www.morganstanley.com/insights/articles/iran-war-oil-inflation-stock-market-2026")]},
{"sub":"Bitcoin & Ethereum",
 "h3":"Bitcoin holds near 65K as traders weigh Fed and Iran deal",
 "summary":"Bitcoin traded around 64,900 dollars on June 17 after briefly topping 66,000, caught between a hawkish Fed and easing Middle East tensions.",
 "body":["Bitcoin changed hands near 64,940 dollars on the morning of June 17, down roughly 1,500 from the prior day as traders parsed the FOMC outcome. Earlier in the week BTC pushed above 66,000, helped by a US-Iran deal narrative and corporate buying, before pulling back.","The token has had a rough 2026, sitting nearly 40,000 dollars below year-ago levels. Polymarket traders saw a 57 percent chance BTC would settle in the 64,000 to 66,000 band on June 18."],
 "sources":[("Fortune","https://fortune.com/article/price-of-bitcoin-06-17-2026/")]},
{"h3":"Ethereum slips toward 1,750 as bearish signals mount",
 "summary":"ETH traded around 1,756 dollars on June 17, down on the day, with technical indicators tilting bearish and the token off about 755 over the past year.",
 "body":["Ethereum changed hands near 1,756 dollars on June 17, down close to 60 from the prior session, keeping it the second-largest crypto with a market cap around 233 billion dollars. Technical screens leaned bearish, with 25 indicators flashing sell against just 5 buys.","Early 2026 brought a steep ETH selloff blamed on recession fears and on co-founder Vitalik Buterin offloading millions of dollars of the token. The asset remains well below year-ago levels despite the maturing staking ETF market."],
 "sources":[("Fortune","https://fortune.com/article/price-of-ethereum-06-17-2026/")]},
{"h3":"Bitcoin ETFs swing from record outflows back to inflows",
 "summary":"After a record 3.4 billion dollar weekly outflow earlier in June, US spot Bitcoin ETFs returned to modest inflows by June 16.",
 "body":["US spot Bitcoin ETFs bled a record 3.4 billion dollars in a single week earlier in June, the largest withdrawal since their 2024 launch, driven by rising Treasury yields, shifting Fed expectations and profit-taking. Analysts argued the bleed looked more cyclical than structural.","By June 16 sentiment had turned, with Bitcoin products drawing about 10 million dollars in net inflows and Ethereum funds adding roughly 9.6 million. The reversal suggested institutional buyers were stepping back in at lower levels."],
 "sources":[("KuCoin","https://www.kucoin.com/news/flash/crypto-etf-inflows-rise-for-btc-eth-sol-xrp-on-june-16")]},
{"h3":"Strategy buys back Bitcoin two weeks after first-ever sale",
 "summary":"Michael Saylor's Strategy bought 1,550 BTC for about 101 million dollars, lifting its hoard to 845,256 coins just two weeks after selling for the first time since 2022.",
 "body":["Strategy scooped up 1,550 Bitcoin for roughly 101 million dollars between June 1 and June 7 at an average price of 65,332, pushing its treasury to 845,256 BTC. The buy landed two weeks after the firm sold 32 BTC at about 77,135, its first sale since 2022.","The company paid roughly 11,800 dollars less per coin than its exit price, while also lifting its cash reserve by 100 million to 1 billion. Rival miner Marathon Digital separately bought 66.7 million dollars of Bitcoin on June 16."],
 "sources":[("Yahoo Finance","https://finance.yahoo.com/markets/crypto/articles/microstrategy-buys-bitcoin-2-weeks-122701010.html")]},
{"sub":"DeFi & Altcoins",
 "h3":"Uniswap's UNI surges over 20 percent on Standard Chartered call",
 "summary":"UNI jumped more than 22 percent to around 3.64 dollars after Standard Chartered initiated coverage with a 100 dollar long-term target, the week's top large-cap performer.",
 "body":["Uniswap's token spiked roughly 23 percent in 24 hours to about 3.64 dollars, with weekly gains near 50 percent, leading the 100 largest cryptocurrencies. The move followed Standard Chartered Global Research initiating coverage on June 15 with a 100 dollar target by end-2030, a near 40x call.","The bank argued Uniswap is uniquely placed to capture growth in tokenized assets active in DeFi, which it expects to expand 37x by 2030. Its path runs through 6.50 this year, 20 in 2027 and 40 in 2028."],
 "sources":[("CoinDesk","https://www.coindesk.com/markets/2026/06/17/uni-token-surges-while-rest-of-crypto-market-looks-to-fed-s-warsh-for-guidance")]},
{"h3":"Hyperliquid's HYPE hits record as it tops Solana per token",
 "summary":"HYPE surged 11.6 percent to an all-time high of 76.90 dollars on June 16, briefly trading above SOL's per-token price for the first time.",
 "body":["Hyperliquid's HYPE token rallied 11.6 percent to a record 76.90 dollars on June 16, rebounding from a 53 low earlier in the month and triggering about 11.5 million dollars in short liquidations. It briefly traded above Solana's per-token price, a first in market history.","The surge was supported by roughly 1.16 billion dollars in monthly token repurchases and open interest near 3.3 billion. The flip was per token only, as Solana's 41 billion dollar market cap still dwarfs Hyperliquid's 16.5 billion."],
 "sources":[("FinanceFeeds","https://financefeeds.com/hyperliquid-eyes-a-bold-upset-over-solana/")]},
{"h3":"Altcoin Season Index climbs to 51 as capital rotates",
 "summary":"With Bitcoin stalling, the Altcoin Season Index rose to 51, signaling gradual rotation into UNI, HYPE, Solana and other large caps.",
 "body":["The Altcoin Season Index climbed to 51 in mid-June as Bitcoin stalled and money rotated into the broader market. UNI led the daily and weekly gainers while HYPE and Solana drove a broad altcoin bid.","Analysts flagged a coming overhang, with roughly 5 billion dollars of insider-held tokens set to unlock across smart contract, AI and DeFi projects over the next six months. That supply pressure could cap any sustained altcoin run."],
 "sources":[("Coinpedia","https://coinpedia.org/news/altcoin-season-news-why-next-six-months-are-important/")]},
{"sub":"Regulation & Policy",
 "h3":"CLARITY Act eligible for Senate floor but faces tight clock",
 "summary":"The digital asset market structure bill cleared committee 15-9 and reached the Senate calendar, but faces a narrow window and unresolved ethics provisions.",
 "body":["The Digital Asset Market Clarity Act advanced out of the Senate Banking Committee on a 15-9 vote in May and by June 1 was placed on the Senate Legislative Calendar, making it eligible for floor consideration. Two Democrats joined all Republicans, though they withheld guaranteed floor support.","The bill still must reconcile with the Senate Agriculture version, clear a 60-vote floor threshold and merge with the House-passed text. Senator Lummis warned that missing this year could push any market structure law out to roughly 2030."],
 "sources":[("CoinDesk","https://www.coindesk.com/policy/2026/06/04/crypto-clarity-act-in-spotlight-for-bad-actor-provisions-as-senate-process-grinds-forward")]},
{"h3":"SEC names digital assets its top objective in 2026-2030 plan",
 "summary":"The SEC's draft strategic plan published June 2 lists digital assets and distributed ledger tech as its first regulatory objective for the next five years.",
 "body":["The SEC published a draft strategic plan for fiscal 2026 through 2030 that designates digital assets and distributed ledger technology as its first regulatory objective under Goal 1. The framing marks a sharp shift toward proactive crypto rulemaking.","The plan builds on a March joint SEC and CFTC interpretation clarifying when crypto assets count as securities, plus a memorandum of understanding between the two agencies to coordinate oversight and provide fair notice to market participants."],
 "sources":[("SEC","https://www.sec.gov/newsroom/press-releases/2026-30-sec-clarifies-application-federal-securities-laws-crypto-assets")]},
{"h3":"GENIUS Act rules near as USDC cements institutional lead",
 "summary":"With GENIUS Act implementing rules due by July 2026, Circle's USDC has become the default stablecoin for new US institutional integrations.",
 "body":["The GENIUS Act, the first US federal stablecoin framework, has its implementing regulations due by July 2026 and enforcement beginning no later than January 2027. USDC was already substantively compliant, helping it become the default choice for new US institutional integrations.","Tether responded with USA-T, a US-regulated stablecoin issued through a nationally chartered bank, though its flagship USDT remains outside the GENIUS framework. USDC grew 73 percent in 2025 to 75 billion dollars while USDT added 36 percent to 186.6 billion."],
 "sources":[("Circle","https://www.circle.com/genius-act")]},
],
"mental-health": [
{"hero":True,"sub":"Research & Studies",
 "h3":"Chatbots become a top source of talk therapy as evidence lags",
 "summary":"A JAMA analysis finds AI chatbots are now among the most common providers of talk therapy in the US, even as research shows humans still outperform them on serious cases.",
 "body":["A wide-ranging JAMA piece reports that AI chatbots have quietly become one of the most common sources of talk therapy in the US, driven largely by gaps in access to human clinicians. Every study comparing chatbots to therapists for moderate-to-severe anxiety or depression still shows licensed humans producing significantly better outcomes.","Most supporting trials run only two to eight weeks, leaving long-term maintenance of gains untested. Researchers warn that millions are leaning on tools that were never built or validated as primary mental health treatment."],
 "sources":[("JAMA","https://jamanetwork.com/journals/jama/fullarticle/2843812"),("Fortune","https://fortune.com/2026/05/12/chatbots-are-becoming-mental-health-tools-before-they-are-ready/")]},
{"h3":"Meta-analysis of 48 trials finds modest benefit from chat agents",
 "summary":"A new npj Digital Medicine meta-analysis of 48 randomized trials covering 28,071 people finds small-to-moderate but real reductions in depression, anxiety and stress.",
 "body":["Researchers pooled 48 randomized controlled trials spanning more than 28,000 participants to weigh how much conversational agents actually help. The analysis found statistically significant small-to-moderate reductions in symptoms of depression, anxiety and stress across both AI and rule-based bots.","Effects were larger in clinical and subclinical groups than in healthy users, a pattern echoed in a parallel npj review of 39 chatbot studies. The authors stress these tools work best as complements to care rather than standalone treatment."],
 "sources":[("npj Digital Medicine","https://www.nature.com/articles/s41746-026-02820-1")]},
{"h3":"Stanford warns AI therapy bots show stigma and crisis failures",
 "summary":"Stanford HAI researchers found popular AI therapy chatbots can express stigma toward certain conditions and give dangerous answers in crisis scenarios.",
 "body":["A Stanford HAI evaluation tested how leading therapy-style chatbots respond to common mental health situations and found troubling patterns. Some models displayed stigma toward conditions like schizophrenia and alcohol dependence and gave responses that could be dangerous when a user was in crisis.","The team argues these failures stem from training that rewards agreeable, flowing conversation rather than clinical accuracy. They caution against deploying such systems as therapist replacements without strong human oversight."],
 "sources":[("Stanford HAI","https://hai.stanford.edu/news/exploring-the-dangers-of-ai-in-mental-health-care")]},
{"h3":"Survey maps how US adults really use AI for mental health",
 "summary":"A JMIR Mental Health cross-sectional survey finds many US adults now turn to AI for support, though most still prefer human professionals.",
 "body":["Researchers surveyed US adults on whether and how they use AI tools for mental health, finding a meaningful subset relying on chatbots for support comparable to what they might seek from a person. Most respondents still preferred human professionals, especially for serious concerns.","The authors call for ongoing monitoring and ethical guidelines so AI expands access without quietly substituting for clinical care. They frame help-seeking in the AI age as a shifting landscape that regulators have yet to fully grasp."],
 "sources":[("JMIR Mental Health","https://mental.jmir.org/2026/1/e88196")]},
{"h3":"New tool automatically audits AI chats for safety failures",
 "summary":"A JMIR Mental Health validation study introduces ASTRA, a system that scans entire AI conversations for mental health risk behaviors.",
 "body":["A development-and-validation paper describes ASTRA, an automated safety testing and reporting application built to flag risky behavior across full AI mental health conversations rather than single replies. In initial testing it reliably identified several forms of clinically relevant risk.","A companion JMIR commentary argues that safety should be judged across the trajectory of a conversation, not at isolated end points, since harm often builds gradually. Together the papers push for conversation-level safety auditing as a standard."],
 "sources":[("JMIR Mental Health","https://mental.jmir.org/2026/1/e91367")]},
{"sub":"Tools & Applications",
 "h3":"FDA panel weighs guardrails as zero GenAI mental health tools cleared",
 "summary":"After a November advisory meeting, the FDA still has not authorized any generative AI mental health device despite clearing over 1,200 other AI tools.",
 "body":["The FDA's Digital Health Advisory Committee convened to debate how to oversee generative AI mental health devices, stressing the need for physician oversight and intervention. Despite authorizing more than 1,200 AI-enabled devices overall, the agency has cleared zero generative AI tools for mental health use.","Legal analysts note the FDA plans to focus enforcement on higher-harm use cases while updating its quality system rules in 2026. The result is a widening gap between fast-moving products and slow regulatory clearance."],
 "sources":[("Psychiatric Times","https://www.psychiatrictimes.com/view/fda-committee-meets-on-generative-ai-digital-mental-health-devices")]},
{"h3":"OpenAI rebuilds ChatGPT responses for distress and self-harm",
 "summary":"OpenAI says working with 170 mental health experts cut undesired responses in sensitive chats by 65 to 80 percent and added a trusted contact feature.",
 "body":["OpenAI detailed a major overhaul of how ChatGPT handles psychosis, mania, self-harm and emotional reliance, saying it collaborated with more than 170 mental health experts. The company reports reducing responses that fall short of its goals by 65 to 80 percent and improving safe-response rates by about 50 percent in suicide and self-harm scenarios.","New mechanisms include time-limited safety summaries that track risk across a conversation and a trusted contact feature letting adults designate someone to be notified. OpenAI is also adding emotional reliance to its baseline safety testing."],
 "sources":[("OpenAI","https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/")]},
{"h3":"Woebot retires its app as AI therapy pioneers exit",
 "summary":"Woebot Health is shutting down its pioneering mental health chatbot app as of June 30, including its teen-focused version.",
 "body":["Woebot Health emailed users that it will retire its AI-powered mental health chatbot app on June 30, including the teen-focused product it had been building. Once a flagship of the digital therapeutics movement, Woebot leaned on scripted cognitive behavioral techniques rather than open-ended generative AI.","The shutdown lands as newer generative AI rivals and tighter regulation reshape the field. It marks a symbolic end for one of the first companies to bring chatbot therapy into the mainstream."],
 "sources":[("MobiHealthNews","https://www.mobihealthnews.com/news/woebot-health-shutting-down-its-app")]},
{"h3":"Tony Robbins-backed AI coach The Path raises 14.3M",
 "summary":"The Path, an AI mental wellness startup cofounded by Tony Robbins and former Calm leaders, raised 14.3 million dollars in seed funding.",
 "body":["The Path closed a 14.3 million dollar seed round for an AI platform cofounded by Tony Robbins alongside former Calm data science and engineering leaders. The product is pitched as a coach built to challenge users rather than simply agree with them, drawing on CBT, ACT, DBT and solution-focused techniques.","The raise continues a wave of AI behavioral health funding that also saw Jimini Health pull in 17 million dollars for its AI agent platform. Investors are betting on structured, clinically framed coaching over open-ended chat."],
 "sources":[("MobiHealthNews","https://www.mobihealthnews.com/news/tony-robbins-ai-mental-health-startup-path-raises-143m")]},
{"h3":"States rush to regulate AI therapy after chatbot-linked harms",
 "summary":"With Illinois banning AI therapists and California's chatbot safeguards now law, lawmakers are racing to set rules after reports of AI-linked harms.",
 "body":["A growing patchwork of state laws is targeting AI in mental health, led by Illinois, which became the first state to ban AI from delivering therapy without licensed oversight, with fines up to 10,000 dollars. California's chatbot safeguard law took effect January 1, and Senator Markey introduced a Youth AI Privacy Act in March.","The push follows documented cases of so-called AI psychosis and teen harms linked to chatbot interactions, with one project logging nearly 300 instances of delusional spiraling. Researchers count roughly 20 meaningful state laws now governing AI mental health interactions."],
 "sources":[("Stateline","https://stateline.org/2026/01/15/ai-therapy-chatbots-draw-new-oversight-as-suicides-raise-alarm/")]},
{"h3":"Utah emerges as model for pragmatic AI mental health rules",
 "summary":"An npj Digital Medicine paper profiles Utah's regulatory framework as a national template balancing AI innovation with patient safety.",
 "body":["Researchers from the University of Utah and the state's Office of Artificial Intelligence Policy describe how Utah built a pragmatic regulatory framework as generative AI floods into mental health care. The approach aims to let innovation proceed while requiring transparency and patient safeguards rather than outright bans.","The authors position Utah as a national leader offering a middle path between prohibition and a regulatory vacuum. They argue forward-looking rules can channel AI's reach into underserved areas without abandoning safety."],
 "sources":[("npj Digital Medicine","https://www.nature.com/articles/s41746-026-02580-y")]},
],
"sports": [
{"hero":True,"sub":"Football",
 "h3":"England crush Croatia 4-2 as Kane bags brace in World Cup opener",
 "summary":"Harry Kane scored twice as England beat Croatia 4-2 in Dallas to open their 2026 World Cup campaign in Group L.",
 "body":["England opened their World Cup at the Dallas stadium with a 4-2 win over Croatia on June 17. Kane struck twice inside the first 42 minutes before Petar Musa and Martin Baturina hit back to level the match before the break.","England regained control after half time with goals from Jude Bellingham and Marcus Rashford sealing the result. The win gave Thomas Tuchel's side a strong start in a group they are expected to win comfortably."],
 "sources":[("ESPN","https://www.espn.com/soccer/match/_/gameId/760437/croatia-england")]},
{"h3":"Netherlands held 2-2 by Japan as Kamada strikes late",
 "summary":"A late Daichi Kamada equaliser denied the Dutch a winning World Cup start in their Group F opener.",
 "body":["The Netherlands twice led against Japan in Arlington but had to settle for a 2-2 draw in their opening Group F fixture. Virgil van Dijk and Crysencio Summerville put the Dutch ahead each time, only for Japan to respond through Nakamura and a late Kamada strike.","Kamada's 89th-minute deflected effort from a corner snatched a point for Japan and left Ronald Koeman's side frustrated. The Netherlands turn next to a meeting with Sweden in Houston as the group tightens."],
 "sources":[("Sky Sports","https://www.skysports.com/football/news/12098/13552697/world-cup-2026-netherlands-2-2-japan-daichi-kamadas-89th-minute-equaliser-denies-the-dutch-in-dallas")]},
{"h3":"Co-hosts headline packed second round of World Cup fixtures",
 "summary":"Mexico, Canada and a clutch of favourites took the field on June 18 as the expanded group stage rolled on.",
 "body":["June 18 served up a packed slate of second-round group games across the three host nations. Mexico hosted Korea Republic at Estadio Akron in Guadalajara while Czechia met South Africa in Atlanta in Group A action.","Group B also featured Switzerland against Bosnia and Herzegovina at SoFi Stadium and co-hosts Canada facing Qatar at BC Place in Vancouver. The expanded 48-team format has kept the schedule dense through the opening fortnight."],
 "sources":[("ESPN","https://www.espn.com/soccer/story/_/id/48939282/2026-fifa-world-cup-fixtures-results-match-schedule-group-stage-knockout-rounds-bracket")]},
{"h3":"France and Argentina open campaigns with statement wins",
 "summary":"France beat Senegal 3-1 and Argentina downed Algeria 3-0 as the tournament favourites made strong starts.",
 "body":["The World Cup's leading contenders flexed their muscle in the opening round of fixtures. France saw off Senegal 3-1 in Group I while Argentina cruised past Algeria 3-0 in Group J.","Norway also impressed with a 4-1 win over Iraq and Austria edged Jordan 3-1. The expanded field has produced lopsided results as the heavyweights settle into the group phase."],
 "sources":[("CBS Sports","https://www.cbssports.com/soccer/news/world-cup-group-standings-table-results/")]},
{"sub":"Tennis",
 "h3":"Sinner survives Struff scare in Halle ahead of Wimbledon",
 "summary":"World No.1 Jannik Sinner edged past Jan-Lennard Struff in three sets at the Halle Open as he sharpens his grass game.",
 "body":["Defending Wimbledon champion Jannik Sinner came through a tough test in Halle, beating home favourite Jan-Lennard Struff 6-2, 6-7(1), 7-6(3). It was the second straight match Sinner needed three sets to win as he builds form on grass.","The Terra Wortmann Open is a key tune-up before Wimbledon, where Sinner is the top seed. Alexander Zverev, fresh off his Roland Garros title, advanced on the other side of the draw."],
 "sources":[("ATP Tour","https://www.atptour.com/en/news/halle-2026-results")]},
{"h3":"Vekic denies Raducanu to claim Queen's title on grass",
 "summary":"Donna Vekic beat Emma Raducanu 6-0, 7-6(6) in the HSBC Championships final at Queen's Club for her fifth career title.",
 "body":["Croatia's Donna Vekic spoiled the home party at Queen's Club, beating British No.1 Emma Raducanu 6-0, 7-6(6) in the final. The win was Vekic's fifth WTA title and her first at the 500 level.","Raducanu had stormed into the final with a straight-sets win over Iva Jovic but could not contain Vekic in the opening set. The run still lifts Raducanu toward a Wimbledon seeding in a strong grass season for the Brit."],
 "sources":[("Sky Sports","https://www.skysports.com/tennis/news/32461/13553975/emma-raducanu-loses-queens-final-to-donna-vekic-despite-battling-display-by-british-no-1")]},
{"h3":"Alcaraz withdrawal reshapes Wimbledon as Zverev rises to No.2",
 "summary":"Carlos Alcaraz has pulled out of Wimbledon 2026 with injury, opening the men's draw and lifting Zverev to the No.2 seed.",
 "body":["Carlos Alcaraz's injury withdrawal from Wimbledon has thrown the men's draw open with Jannik Sinner installed as top seed and defending champion. Roland Garros winner Alexander Zverev moves up to the No.2 seed and is now a leading contender.","The grass swing through Halle, Queen's and Berlin has been the proving ground as players chase seedings. Alcaraz's absence removes one of the title favourites and shifts the balance toward Sinner and Zverev."],
 "sources":[("Crush and Rush News","https://www.crushrushnews.com/2026/05/20/2026-wimbledon-mens-entry-list-sinner-alcaraz-withdrawal/")]},
{"sub":"F1",
 "h3":"Hamilton wins first Ferrari race in dramatic Barcelona GP",
 "summary":"Lewis Hamilton claimed his maiden Ferrari victory in Barcelona as championship leader Kimi Antonelli retired late.",
 "body":["Lewis Hamilton finally delivered his first win for Ferrari at the Barcelona-Catalunya Grand Prix, leading home George Russell and Lando Norris. A flawless three-stop strategy aided by a virtual safety car handed Hamilton a free pit stop and control of the race.","The result produced the first all-British podium since 1968. Championship leader Antonelli suffered an electrical failure with three laps left, denting his points haul as the title fight tightens."],
 "sources":[("Formula 1","https://www.formula1.com/en/latest/article/hamilton-claims-stellar-maiden-grand-prix-victory-for-ferrari-in-barcelona-as-antonelli-suffers-shock-retirement.4yCXiPLHUdcnl2BwNpqUIa")]},
{"sub":"Sailing",
 "h3":"SailGP heads to Halifax with Australia leading Season 6",
 "summary":"SailGP's Season 6 reaches its seventh event in Halifax on June 20-21 with Tom Slingsby's Australia out front.",
 "body":["SailGP's high-speed fleet arrives in Halifax for the seventh event of Season 6 on June 20-21. After six rounds Australia lead the standings on 55 points, ahead of Great Britain on 44 and the United States on 36.","Each event winner banks 400,000 dollars from a total purse of 12.8 million dollars across the 2026 season. Tom Slingsby's Australian crew have been the team to beat after recent wins in New York and Bermuda."],
 "sources":[("Scuttlebutt Sailing News","https://www.sailingscuttlebutt.com/2026/06/11/race-against-time-for-sailgp-halifax/")]},
{"sub":"Grappling",
 "h3":"Final ADCC qualifying trials loom in Australia for 2026 Worlds",
 "summary":"The last spots for the 2026 ADCC World Championship are on the line at the Asia and Oceania Trials in Australia on June 20-21.",
 "body":["The final qualifying event on the 2026 ADCC calendar takes place on Australia's Gold Coast, with the North American, EMEA and South American trials already complete. The Asia and Oceania bracket is the last route into the World Championship.","The region produced history last cycle when Adele Fornarino won gold in both the under-55kg and absolute divisions. FloGrappling carries the trials live as the qualified field fills out ahead of Worlds."],
 "sources":[("FloGrappling","https://www.flograppling.com/articles/15972853-2026-adcc-asia-oceania-trials-entries-whos-in-for-the-final-trials")]},
{"h3":"Dalpra completes perfect IBJJF season as new rankings drop",
 "summary":"Tainan Dalpra's fourth middleweight world title headlines fresh June rankings after a clean sweep of 2026's major IBJJF events.",
 "body":["Tainan Dalpra capped a dominant year with his fourth IBJJF middleweight world title, finishing as one of only two athletes to win gold at every major IBJJF event in 2026. His all-submission run drew wide attention across the grappling world.","FloGrappling published updated world rankings in June reflecting the results from the Long Beach Worlds. Dalpra and Gabi Pessanha stood out as the season's standout performers heading into the no-gi calendar."],
 "sources":[("FloGrappling","https://www.flograppling.com/articles/15951418-ibjjf-worlds-2026-results-heres-every-division-winner")]},
],
"consumer-tech": [
{"hero":True,"sub":"Software & Services",
 "h3":"Google ships Android 17 stable alongside June Pixel Drop",
 "summary":"Google released Android 17 to Pixel phones and the Pixel Watch on June 16, bundled with a feature-packed quarterly drop.",
 "body":["Google began rolling out the stable build of Android 17 on June 16, timed to land with the June 2026 Pixel Feature Drop across phones, folds and the Pixel Watch. The release headlines floating app Bubbles that turn the browser, calendar and Gemini into windows over your main screen, plus Screen Reactions that overlay selfie video onto screen recordings.","The drop also folds in Gemini Omni for Gemini Pro users and the Lyria 3 music model that generates audio from text or images. Google extended several emergency safety features to more phones and countries and added an Emergency Detection update for the Pixel Watch."],
 "sources":[("9to5Google","https://9to5google.com/2026/06/16/google-android-17-pixel-launch/")]},
{"h3":"Apple seeds iOS 26.6 beta 2 with little new on show",
 "summary":"Apple pushed iOS 26.6 public beta 2 on June 16, a low-key update focused on fixes as iOS 27 takes the spotlight.",
 "body":["Apple released iOS 26.6 public beta 2 on June 16, but testers found almost nothing new to discover. The 26.6 cycle is expected to center on bug and security fixes rather than headline features.","The few additions in the works include a notification warning users as they near their blocked-call limit and a feature that automatically locks an iPhone if it is yanked from your hand. Apple's attention has largely shifted to iOS 27, unveiled at WWDC and due in September."],
 "sources":[("9to5Mac","https://9to5mac.com/2026/06/16/apple-releases-ios-26-6-beta-2-for-iphone-heres-what-to-expect/")]},
{"h3":"Netflix to stream Spotify video podcasts including Bill Simmons",
 "summary":"Netflix and Spotify struck a deal to bring 16 video podcasts, including The Ringer's lineup, to the streamer in 2026.",
 "body":["Netflix and Spotify confirmed a partnership to bring a selection of Spotify Studios and The Ringer video podcasts to Netflix, starting in the US in early 2026 before expanding to other markets. The deal blurs the line between podcasting and traditional streaming.","The initial slate of 16 titles includes The Bill Simmons Podcast, The Zach Lowe Show, The McShay Show, The Rewatchables and Conspiracy Theories. The move gives Spotify's video shows a new home and hands Netflix a fresh stream of talk content."],
 "sources":[("The Hollywood Reporter","https://www.hollywoodreporter.com/business/business-news/netflix-spotify-video-podcasts-1236400404/")]},
{"h3":"YouTube Premium prices climb across every tier",
 "summary":"Google quietly raised YouTube Premium prices for all plan tiers in the US, lifting the individual plan to 15.99 dollars.",
 "body":["Google increased the cost of every YouTube Premium plan in the United States, with the individual plan rising to 15.99 dollars a month from 13.99. The family plan jumped to 26.99 dollars from 22.99, hitting households the hardest.","The hikes arrived with little advance warning, adding to a year of rising subscription costs across streaming. The changes apply to new and existing subscribers as YouTube leans on Premium revenue."],
 "sources":[("Artvoice","https://artvoice.com/youtube-premium-price-increases-just-went-live-with-no-warning-and-here-is-every-new-price/")]},
{"sub":"EVs & Mobility",
 "h3":"Jaguar goes all-electric as JLR unveils Range Rover Electric",
 "summary":"At its June 17 Investor Day, JLR confirmed Jaguar becomes a fully electric brand and showed the production Range Rover Electric.",
 "body":["Jaguar Land Rover used its Gaydon Investor Day on June 17 to confirm Jaguar's transformation into an all-electric marque and to debut the long-awaited Range Rover Electric. Press testing points to a 118kWh battery delivering roughly 300 miles of range and a dual-motor setup making around 542 horsepower.","JLR also laid out a plan to cut 1.7 billion pounds in costs over the next two years and lower its breakeven point to 300,000 units. Every JLR brand is set to offer a pure-electric model before the end of the decade."],
 "sources":[("Electric Drives","https://electricdrives.tv/range-rover-electric-everything-we-know-about-the-brands-upcoming-first-ev/")]},
{"h3":"Tesla robotaxi blankets Austin as Cybercab specs surface",
 "summary":"Tesla expanded its unsupervised robotaxi zone to the entire Austin metro just as EPA filings revealed the production Cybercab's specs.",
 "body":["Tesla widened its geofenced unsupervised robotaxi service to cover the whole Austin metro area, though the active fleet still numbers only around 20 vehicles serving that vast zone. The expansion continues the company's cautious public rollout of driverless rides.","Separately, newly released EPA certification documents exposed the production Cybercab's full technical profile for the first time. The two-seat robotaxi carries a 3,113-pound curb weight, a 219 horsepower motor and a 48kWh battery pack."],
 "sources":[("Electrek","https://electrek.co/guides/tesla/")]},
{"h3":"Ford takes 19.5 billion charge in retreat from pricey EVs",
 "summary":"Ford booked a multi-billion-dollar charge as it pivots from high-end electric vehicles back toward hybrids amid weak demand.",
 "body":["Ford disclosed it will absorb a charge of about 19.5 billion dollars over the next two years as it scales back full-electric ambitions and leans into hybrids. The automaker pointed to a market unwilling to buy premium EVs in the 50,000 to 80,000 dollar range.","The move underscores a turbulent stretch for the US EV market, where slower adoption, shrinking incentives and trade tensions have forced carmakers to rethink product plans. Rivals like Rivian and Lucid are pressing on with cheaper models to chase mainstream buyers."],
 "sources":[("Yahoo Finance","https://finance.yahoo.com/news/ford-rivian-announce-big-developments-192600717.html")]},
{"h3":"Rivian locks in R2 pricing as mass-market push begins",
 "summary":"Rivian confirmed final specs and pricing for its R2 SUV, starting near 45,000 dollars as it chases mainstream buyers.",
 "body":["Rivian firmed up production specifications and pricing for its R2 SUV and R3 crossover, the affordable models aimed squarely at mainstream American drivers. The R2 starts at 45,000 dollars before incentives, with deliveries slated to begin in early 2026.","The company expects to deliver 62,000 to 67,000 vehicles this year, close to 50 percent growth over 2025. The mass-market launch arrives as struggling EV startups including Rivian, Lucid and Slate navigate their most pivotal year yet."],
 "sources":[("InsideEVs","https://insideevs.com/features/793324/rivian-slate-lucid-update-2026/")]},
{"sub":"Devices & Launches",
 "h3":"Samsung pushes One UI 9 Beta 3 to Galaxy S26 in six countries",
 "summary":"Samsung released its third One UI 9 beta for the Galaxy S26 series on June 17 with privacy and camera fixes.",
 "body":["Samsung rolled out the third One UI 9 Beta build to Galaxy S26 owners across six countries on June 17, advancing its Android 17-based software ahead of a stable release. The update bundles nine changes, including two improvements and seven bug fixes.","Most of the fixes target Privacy Display and camera behavior. One UI 9 is expected to ship in finished form on the Galaxy Z Fold 8 and Z Flip 8, which are tipped to launch at a London Unpacked event on July 22."],
 "sources":[("Android Central","https://www.androidcentral.com/phones/samsung-galaxy/samsung-galaxy-unpacked-summer-2026-how-to-watch-and-what-to-expect")]},
{"h3":"iPhone 18 Pro tipped for a 35 percent smaller Dynamic Island",
 "summary":"Fresh leaks point to a much narrower Dynamic Island and a RAM bump for Apple's 2026 iPhone lineup.",
 "body":["MacRumors reports the iPhone 18 Pro and Pro Max will shrink the Dynamic Island by roughly 35 percent, narrowing it from about 20.7mm to around 13.5mm by moving Face ID components beneath the display. The base iPhone 18 is also said to jump to 12GB of RAM to power Apple's heavier on-device AI and Siri features.","Color leaks point to Dark Cherry, Light Blue, Dark Gray and Silver for the Pro models, with the wine-red Dark Cherry as the signature shade. The phones are expected in September alongside Apple's first foldable iPhone."],
 "sources":[("MacRumors","https://www.macrumors.com/")]},
{"h3":"Meta preps two new Ray-Ban glasses with hidden NameTag code",
 "summary":"FCC filings reveal two unreleased Ray-Ban Meta glasses while researchers found dormant facial-recognition code in Meta's AI app.",
 "body":["FCC filings surfaced two new Ray-Ban Meta models codenamed Blazer and Scriber, with fresh model numbers suggesting a new hardware generation built around a Snapdragon AR chipset and upgraded mics. The disclosures point to Meta's next push in face-worn computing.","Separately, Wired found code for an unreleased facial-recognition feature dubbed NameTag buried in Meta's AI app, capable of capturing faces via the glasses and alerting the wearer on later recognition. The code is not enabled or available to customers, but it has reignited privacy concerns."],
 "sources":[("Engadget","https://www.engadget.com/2187824/wired-found-code-for-an-unreleased-facial-recognition-feature-in-meta-s-ai-app/")]},
{"h3":"Sony's anniversary 1000X headphones disappoint reviewers",
 "summary":"Sony's 10th-anniversary flagship headphones get a premium leather-and-metal redesign but step back on sound and noise cancelling.",
 "body":["Sony marked a decade of its 1000X line with a refined model dressed in leather and metal, but reviewers found both the sound quality and active noise cancelling fell short of last year's WH-1000XM6. The anniversary edition trades performance gains for a more luxurious build.","The flagship lands in a crowded high-end market where Sennheiser's latest flagship has narrowed the gap to Bose and Sony with better sound and more effective ANC. Marshall also entered the fray with a model blending its Major and Monitor designs."],
 "sources":[("Engadget","https://www.engadget.com/reviews/headphones/")]},
{"h3":"Lexus prices ES Electric for the US from 48,795 dollars",
 "summary":"Lexus confirmed US pricing for its ES Electric sedan, offered in single-motor and dual-motor trims.",
 "body":["Lexus set US pricing for its ES Electric, offering a 350e single-motor front-wheel-drive version and a 500e dual-motor all-wheel-drive variant. Prices run from 48,795 to 60,195 dollars, slotting the luxury sedan into a competitive EV field.","The launch is part of a wave of roughly 32 new electric models reaching US showrooms this year, even as the broader market wrestles with softer demand and reduced incentives. Genesis, Acura and others are also bringing fresh EVs to dealers."],
 "sources":[("InsideEVs","https://insideevs.com/features/783999/every-new-electric-car-ev-2026/")]},
],
}
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
