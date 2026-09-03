import json

S = "AI/HPC Stocks & Infrastructure"
F = "Foundation Models & Releases"
C = "Chinese AI Ecosystem"
A = "Agents & Automation"
E = "Enterprise & Regulation"

items = []

def add(hero, sub, h3, summary, body, sources):
    items.append({"hero": hero, "sub": sub, "h3": h3, "summary": summary, "body": body, "sources": sources})

# ---------------- AI/HPC Stocks & Infrastructure ----------------
add(True, S,
 "Broadcom posts record $29.6bn quarter but Wall Street shrugs",
 "Broadcom reported third quarter fiscal 2026 revenue of $29.6 billion, up 86% year on year on custom AI accelerator demand, and guided to roughly $34.8 billion for the current quarter.",
 ["Broadcom closed the books on its fiscal third quarter with $29.6 billion of revenue, an 86% jump from the same period a year earlier. The company said the surge was driven almost entirely by demand for the custom AI accelerators it designs for a small group of very large customers, plus the AI networking silicon that stitches those accelerators together inside data centres.",
  "Guidance was arguably the bigger number. Management pointed to approximately $34.8 billion for the fourth quarter, which would be a 93% increase on the prior year period. Broadcom has previously told investors it can see a path to more than $100 billion of AI chip revenue in fiscal 2027, a figure that would put its accelerator business within striking distance of Nvidia's data centre run rate from only two years ago.",
  "Investors were less impressed than the headline suggested. The stock came under pressure after the print, a reminder that expectations for AI semiconductor names have risen faster than the results themselves. Broadcom's custom XPU model, which builds a chip tuned to one customer's workload rather than a general purpose GPU, has attracted a roster that reportedly includes Google, Meta, Anthropic and OpenAI."],
 [["Quartz", "https://qz.com/broadcom-record-revenue-ai-chips-quarterly-earnings-090226"], ["Broadcom Investor Relations", "https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial"]])

add(False, S,
 "Nvidia doubles revenue to $96bn as Blackwell Ultra ramps",
 "Nvidia reported $96.2 billion of revenue for the quarter ended 26 July, up 106% year on year, with data centre sales of $89.0 billion beating estimates.",
 ["Nvidia's second quarter of fiscal 2027 brought $96.2 billion of revenue, an 18% sequential increase and more than double the same quarter a year earlier. Data centre revenue of $89.0 billion accounted for the overwhelming majority of that total and grew 117% year on year, comfortably ahead of the roughly $85.7 billion analysts had modelled.",
  "The company attributed the step up to the ramp of its Blackwell Ultra infrastructure. Hyperscale revenue more than doubled from a year ago and rose 13% sequentially. Gross margins held at 75% on both a GAAP and non-GAAP basis, which is notable given the memory cost pressure running through the supply chain.",
  "Chief executive Jensen Huang used the call to forecast roughly 70% revenue growth for fiscal 2028, well above the consensus view, and said demand is accelerating rather than plateauing. The guidance is the clearest signal yet that Nvidia expects the Vera Rubin generation to extend the cycle rather than mark its peak."],
 [["Nvidia Newsroom", "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027"], ["CNBC", "https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html"], ["Fortune", "https://fortune.com/2026/08/26/nvidia-results-q2-earnings/"]])

add(False, S,
 "Memory squeeze forces Nvidia to skip a gaming GPU generation",
 "A severe DRAM and HBM shortage has pushed Nvidia to shelve new gaming cards and funnel scarce memory into AI accelerators, breaking a 30-year cadence.",
 ["The memory market has become the binding constraint on AI hardware. HBM production for accelerators consumes roughly three times the wafer capacity of standard DRAM per gigabyte, and manufacturers have been reallocating lines accordingly. Industry trackers put first quarter 2026 DRAM contract price increases at around 90% sequentially, with server DRAM up 60% to 70%.",
  "SK Hynix has said its HBM, DRAM and NAND capacity is effectively sold out for 2026, and both it and Samsung have pushed HBM3E supply prices up by close to 20% for the year. Samsung lifted the price of a 32GB DDR5 module from $149 to $239, a 60% move.",
  "The knock on effect reaches consumers. Nvidia has shelved its RTX 50 Super refresh and reporting through this year indicates the RTX 60 series has slipped to 2028, meaning no new gaming GPU generation in 2026 for the first time in three decades. The memory is simply worth more attached to an AI accelerator."],
 [["Network World", "https://www.networkworld.com/article/4113772/samsung-warns-of-memory-shortages-driving-industry-wide-price-surge-in-2026.html"], ["TrendForce", "https://www.trendforce.com/news/2025/12/24/news-samsung-sk-hynix-reportedly-plan-20-hbm3e-price-hike-for-2026-as-nvidia-h200-asic-demand-rises/"]])

add(False, S,
 "Microsoft lifts 2026 capex plan to $190bn and adds 1GW a quarter",
 "Microsoft has raised calendar 2026 capital spending to roughly $190 billion and is on pace to double its global data centre footprint within two years.",
 ["Microsoft's finance chief put calendar 2026 capital expenditure at about $190 billion, with roughly $40 billion falling in the fourth quarter of fiscal 2026 alone. The company added approximately one gigawatt of data centre capacity in a single quarter and says it is on track to double its worldwide footprint inside two years.",
  "The spending sits alongside a commitment from OpenAI to buy an incremental $250 billion of Azure capacity. Microsoft is also starting to disclose quarterly revenue for the Azure cloud business separately for the first time, having reported 42% year on year growth to $29.42 billion in its most recent quarter.",
  "Microsoft is not alone. The five largest US cloud and AI infrastructure providers have collectively signalled between $660 billion and $690 billion of capital expenditure for 2026, a figure that has become the central exhibit in the argument over whether AI revenue can catch up with AI capex."],
 [["The Next Platform", "https://www.nextplatform.com/cloud/2026/05/04/microsoft-committed-to-doubling-ai-infrastructure-in-two-years/5219208"], ["Futurum Group", "https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/"]])

add(False, S,
 "Anthropic plans $50bn US data centre build with Fluidstack",
 "Anthropic is committing around $50 billion to American data centre capacity, beginning with Fluidstack developed sites in Texas and New York.",
 ["Anthropic has laid out a roughly $50 billion domestic data centre programme, with the first sites being developed alongside Fluidstack in Texas and New York. The move takes the company from a pure model developer that rents compute into one that is directly underwriting the physical build.",
  "The commitment lands as the company courts enterprise customers ahead of a widely reported public listing. Google has separately committed up to $40 billion and multi gigawatt cloud capacity over five years, giving Anthropic two very large compute pipelines running in parallel.",
  "Vertical integration into power and buildings has become the default posture for frontier labs. OpenAI has its Stargate campuses with Oracle and SoftBank, Meta has established a dedicated Meta Compute organisation for gigawatt scale sites, and KKR has launched Helix Digital Infrastructure with a budget above $10 billion for hyperscale assets with secured power."],
 [["Data Center Dynamics", "https://www.datacenterdynamics.com/en/news/anthropic-plans-50bn-us-data-center-spend-starting-with-fluidstack-sites-in-texas-and-new-york/"], ["Data Center Dynamics", "https://www.datacenterdynamics.com/en/news/kkr-launches-helix-digital-infrastructure-to-deliver-hyperscale-data-centers-with-secured-power/"]])

add(False, S,
 "Bitcoin miners book over $70bn of AI hosting contracts",
 "Public miners have signed more than $70 billion of AI and high performance computing deals, with some expected to draw most of their revenue from compute rather than mining.",
 ["The conversion of bitcoin mining estates into AI data centres has moved from thesis to balance sheet. Publicly listed miners have now secured more than $70 billion in AI and high performance computing contracts, and analysts expect some operators to take up to 70% of revenue from compute hosting by the end of this year.",
  "The individual deals are large. IREN signed a $9.7 billion arrangement with Microsoft covering 76,000 Nvidia GB300 GPUs across 200 megawatts at its Childress campus in Texas. Hut 8 agreed a 15 year, $7 billion lease with Google backed Fluidstack. Bitfarms is converting a Washington state mine to HPC hosting under a $128 million deal for 18 megawatts, targeting completion in December, and plans to wind down mining entirely by 2027.",
  "The economics behind the pivot are unforgiving. Miners have been losing roughly $19,000 per coin produced at current difficulty and power costs, while interconnect queues have made an existing grid connection one of the scarcest assets in the AI buildout."],
 [["Data Center Dynamics", "https://www.datacenterdynamics.com/en/news/bitfarms-to-convert-washington-cryptomine-to-hpcai-hosting/"], ["CoinDesk", "https://www.coindesk.com/markets/2026/03/27/bitcoin-miners-are-becoming-ai-companies-and-selling-their-btc-to-fund-the-transition"]])

add(False, S,
 "Software stocks slide as investors question the AI capex return",
 "The S&P software and services index is down close to 20% this year even as Azure and Nvidia data centre revenue keep compounding, sharpening the bubble debate.",
 ["The AI trade has split in two. The S&P Software and Services index has fallen nearly 20% in 2026 while the broader Nasdaq is down a more modest 2.4%, a gap that reflects worry about monetisation rather than about demand for chips.",
  "The bear case rests on three points: falling token prices compressing revenue per unit of intelligence, cheaper Chinese open weight models capturing a growing share of usage, and hyperscaler capital expenditure running at roughly $700 billion for the year against uncertain cash returns.",
  "The counterargument is that the underlying numbers keep accelerating. Azure grew 43% and Nvidia's data centre revenue rose 92% in their latest reported quarters. The unresolved question is whether AI generated cash flow catches capex, which would make this year's drawdown a valuation reset inside an intact boom rather than the start of something worse."],
 [["Fortune", "https://fortune.com/2026/07/17/tech-stocks-global-selloff-as-investors-ai-semiconductor-chips/"], ["Investing.com", "https://www.investing.com/analysis/big-tech-will-spend-600b-on-ai-in-2026-5-stocks-cashing-the-checks-200674615"]])

# ---------------- Foundation Models & Releases ----------------
add(False, F,
 "Anthropic ships Claude Fable 5.1 and Mythos 5.1",
 "Anthropic released Fable 5.1 and Mythos 5.1 at the same headline price as Fable 5, cutting cache read costs by 75% and claiming a large jump in scientific research work.",
 ["Anthropic released Claude Fable 5.1 and the limited access Claude Mythos 5.1, positioning both as its strongest models for coding and knowledge work. Input and output pricing is unchanged at $10 and $50 per million tokens, but cache reads fall 75% from $1.00 to $0.25 per million, which the company estimates cuts typical workload costs by around 25% and highly agentic ones by up to 45%.",
  "The benchmark story is heavily weighted toward research. Anthropic reports 52.6% on Terminal-Bench-Science 0.1, more than double Fable 5, alongside 55.8% on Terminal-Bench 4.0 against 42.0% for the previous model, 77.9% on OSWorld and 73.4% on CursorBench. Artificial Analysis, which ran pre-release evaluations, placed the model at the top of its intelligence index at maximum effort while noting cost per task is still about 20% higher than Fable 5 because output token counts rose.",
  "Anthropic also disclosed that Fable and Mythos 5.1 share the same weights, with an escalating classifier stack that falls back to Opus 4.8 for requests judged dangerous. The company says cybersecurity safeguards now flag benign requests roughly 60% less often and that fallback on basic biology and medical questions is down about 85%.",
  "The release landed a day before OpenAI published its Astra safety preview, and several observers read the timing as deliberate. Anthropic also confirmed the model watermarks its outputs, a requirement it took on when it signed the EU AI Act transparency code of practice in July."],
 [["VentureBeat", "https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads"], ["The New Stack", "https://thenewstack.io/anthropic-fable-5-1-launch/"], ["Bloomberg", "https://www.bloomberg.com/news/articles/2026-09-01/anthropic-says-new-fable-5-1-ai-model-is-cheaper-better-at-coding"]])

add(False, F,
 "OpenAI says Astra is its first Critical cyber capability model",
 "OpenAI confirmed its forthcoming Astra model crosses the Critical cybersecurity threshold in its Preparedness Framework and will ship with restricted access to its strongest offensive capabilities.",
 ["OpenAI published a preview of Astra ahead of release, stating the model is the first to reach the Critical cybersecurity capability threshold under its Preparedness Framework. Astra scored 100% on the public ExploitBench, which forced the company to build a contamination free internal port using V8 vulnerabilities disclosed after the model's knowledge cutoff. On that refreshed set it remained roughly four times more capable than GPT-5.6 Sol while using far fewer tokens.",
  "In expert assessments the model found and chained two zero days in modified tests, compromised a hardened browser, escaped its sandbox and executed commands on the host with limited human help. OpenAI said it will release Astra soon but will restrict the most advanced cyber capabilities to a group of testers first, expanding through its Daybreak Blue defensive programme.",
  "Sam Altman framed the delay in unusually direct terms, saying the company has been slowing work on models after Astra to keep safety and alignment progress in step with capability. The Verge reported that development was pushed back following the Hugging Face breach.",
  "Reaction split predictably. Some researchers welcomed a defender first rollout that mirrors Anthropic's approach, while critics argued the framing is as much marketing as caution."],
 [["Wired", "https://www.wired.com/story/openai-astra-first-ai-model-with-critical-cyber-abilities/"], ["OpenAI", "https://openai.com/index/path-to-astra"], ["Reuters", "https://www.reuters.com/business/openai-says-upcoming-model-is-so-capable-it-requires-stronger-guardrails-2026-09-01/"]])

add(False, F,
 "Astra's recurrent depth design sparks a monitorability fight",
 "The Information reported that Astra uses a recurrent depth architecture that shifts reasoning into activations, prompting safety researchers to warn about unmonitorable chains of thought.",
 ["The Information reported that OpenAI's Astra uses a technique described as recurrent depth, which improves cost and performance but pushes more of the model's reasoning into internal activations rather than readable natural language. The claim set off one of the sharpest public safety arguments of the year.",
  "Redwood Research's Ryan Greenblatt called it potentially the worst development for AI safety to date, and Apollo researcher Mikita Balesni argued that all labs should commit to limiting opaque serial depth. Others countered that chain of thought legibility was always an artefact of current training methods rather than a durable guarantee.",
  "OpenAI research chief Jakub Pachocki pushed back publicly, saying the computation graph depth of current frontier models including Astra is within a factor of two of GPT-4 and that the company has worked to preserve chain of thought monitoring since its first reasoning models. The Information's Amir Efrati noted OpenAI stated on the same day that Astra's chain of thought can be monitored.",
  "The episode is a useful preview of how architecture choices now double as governance choices, since a design that improves inference economics can simultaneously erode the main interpretability tool regulators and evaluators rely on."],
 [["The Information", "https://www.theinformation.com/articles/secret-technique-behind-openais-astra-model-sparks-security-concerns"], ["Marcus on AI", "https://garymarcus.substack.com/p/red-alert-openai-is-poised-to-cross"]])

add(False, F,
 "Google ships Gemini 3.8 Flash weeks after 3.7 Flash",
 "Google released Gemini 3.8 Flash on 2 September, continuing a release cadence that has produced four Flash generations since July.",
 ["Google pushed Gemini 3.8 Flash into general availability on 2 September, the latest step in an unusually compressed release schedule. Gemini 3.7 Flash reached general availability on 13 August, only three weeks after 3.6 Flash, which itself followed the 21 July launch of 3.6 Flash and 3.5 Flash-Lite.",
  "Google has positioned the Flash line as its workhorse tier for coding and agent workloads rather than a cut down variant, with each release claiming improvements in software engineering, knowledge work and web development. The company has also been shipping specialised models alongside the main line, including Gemini Omni Flash for conversational video generation and editing and Gemini 3.5 Transcribe.",
  "Pricing has been used as a lever as much as capability. Google's developer changelog listed Gemini 3.7 Flash at an introductory rate through the end of December, part of a broader price war in which Anthropic cut cache reads 75% and Chinese labs continue to undercut both."],
 [["Google AI for Developers", "https://ai.google.dev/gemini-api/docs/changelog"], ["Google Blog", "https://blog.google/innovation-and-ai/technology/google-ai-updates-august-2026/"]])

add(False, F,
 "Grok 4.6 lands third on Artificial Analysis intelligence index",
 "xAI released Grok 4.6 in August, a 1.5 trillion parameter model with a 500K context aimed at long running agents and interactive work.",
 ["xAI shipped Grok 4.6 on 12 August, describing it as a direct upgrade to Grok 4.5 in the same 500,000 token context class. Elon Musk characterised it as a 1.5 trillion parameter model whose gains come mainly from improved supervised fine tuning and reinforcement learning rather than a larger pretraining run.",
  "The stated focus is long horizon work: researching and analysing information, operating across a codebase and turning a product idea into a running application. Pricing starts at $2 per million input tokens and $6 per million output tokens below 200K prompt tokens, doubling above that threshold.",
  "Independent evaluators placed the model third on the Artificial Analysis intelligence index, overtaking Moonshot's Kimi K3 and matching GPT-5.6 Sol. It is available through the xAI API, Cursor, Grok Build and partners including OpenRouter, Vercel and Cloudflare."],
 [["VentureBeat", "https://venturebeat.com/technology/spacexai-debuts-grok-4-6-overtaking-kimi-k3s-performance-and-matching-gpt-5-6-sol-for-worlds-third-best-on-artificial-analysis"], ["LLM Stats", "https://llm-stats.com/blog/research/grok-4.6-launch"]])

# ---------------- Chinese AI Ecosystem ----------------
add(False, C,
 "Alibaba open weights a 125B Qwen model aimed at Anthropic",
 "Alibaba released Qwen3.8-Flash with 125 billion parameters and published weights, following with a Qwen3.8-Max checkpoint on 2 September.",
 ["Alibaba made Qwen3.8-Flash downloadable on 26 August and released its weights, a 125 billion parameter model the company positions as competitive with Anthropic's Opus 4.6 and DeepSeek's V4-Flash at a fraction of the cost. A Qwen3.8-Max-0902 checkpoint followed on 2 September.",
  "The strategic point is distribution rather than raw capability. Qwen has recorded more than three billion downloads over six months, dwarfing Google's 418 million and Meta's 227 million for all of 2026, and has claimed the top spot globally among open weight model families.",
  "The scale gap between Chinese and American open releases has become structural. In almost every month of 2026 the largest and most performant open model published by a Chinese lab has exceeded anything released openly by an American one, with China's monthly ceiling ranging from 754 billion to 2.78 trillion parameters."],
 [["Bloomberg", "https://www.bloomberg.com/news/articles/2026-08-26/alibaba-releases-smaller-cost-effective-qwen-ai-model"], ["South China Morning Post", "https://www.scmp.com/tech/tech-trends/article/3364404/alibabas-lightweight-qwen-model-takes-larger-ai-systems-openai-deepseek-zhipu"]])

add(False, C,
 "DeepSeek V4 family reaches general availability under MIT licence",
 "DeepSeek's V4-Pro hit general availability in August, completing a two model family with open weights, a one million token context and a sparse attention redesign.",
 ["DeepSeek launched V4 and V4-Pro in late April and brought V4-Pro to general availability on 13 August with the V4-Pro-0813 checkpoint. The family splits into V4-Pro at 1.6 trillion total parameters with 49 billion active and V4-Flash at 284 billion total with 13 billion active, the latter released with open weights on Hugging Face under an MIT licence on 31 July.",
  "Both models share a one million token context and a new architecture the lab calls Compressed Sparse Attention combined with Heavily Compressed Attention, a design aimed squarely at reducing the cost of long context agentic work rather than at benchmark peaks.",
  "V4 was China's first trillion parameter frontier model and set a template others followed. Xiaomi and Alibaba have since shipped trillion parameter systems of their own, with domestic developers moving away from the billion parameter general models that dominated 2023 and 2024 toward larger architectures tuned to Chinese chip stacks."],
 [["DeepSeek", "https://deepseek.ai/deepseek-v4"], ["South China Morning Post", "https://www.scmp.com/tech/big-tech/article/3357449/chinas-trillion-parameter-ai-race-how-developers-strive-narrow-gap-us-rivals"]])

add(False, C,
 "Zhipu and MiniMax turn Hong Kong listings into war chests",
 "Zhipu listed in Hong Kong in January and has since risen roughly 1,500%, with MiniMax following a day later as both push open source flagship models.",
 ["Zhipu listed on the Hong Kong Stock Exchange on 8 January, raising about $560 million and becoming the first of China's so called Six AI Tigers to go public. MiniMax followed a day later with a raise of up to $539 million. Both books were heavily oversubscribed, with MiniMax closing institutional orders a day early.",
  "The aftermarket performance has been extraordinary. Zhipu's shares have climbed roughly 1,500%, briefly pushing its market value past $160 billion in June before settling above $100 billion, a valuation that gives it real capacity to fund training runs without foreign capital.",
  "Both companies have leaned into open weights as a distribution strategy, releasing new flagship models within hours of each other. Zhipu's GLM-4.7 narrowed the coding agent gap with Google DeepMind and Anthropic, and its Z.ai arm has since shipped a desktop agentic development environment built around GLM-5.2."],
 [["South China Morning Post", "https://www.scmp.com/tech/tech-trends/article/3339301/minimax-and-zhipus-stellar-hong-kong-ipos-supercharge-chinas-ai-ambitions"], ["Rest of World", "https://restofworld.org/2026/zhipu-ai-minimax-ipo/"]])

add(False, C,
 "Huawei doubles Ascend output and maps a chip a year to 2028",
 "Huawei plans roughly 600,000 Ascend 910C chips this year and has published a roadmap of Ascend 950, 960 and 970 parts that each double compute.",
 ["Huawei is on course to produce around 600,000 Ascend 910C accelerators in 2026, roughly double last year's output, and to expand the wider Ascend line to as many as 1.6 million dies. The company has also laid out a three year cadence with the Ascend 950 this year, the 960 in 2027 and the 970 in 2028, each generation doubling compute capacity.",
  "The Ascend 950PR reached market in the first quarter in card and SuperPoD server formats, rated at 1.56 PFLOPS in FP4 with Huawei's proprietary HiBL 1.0 memory delivering 1.4 TB per second of bandwidth. That works out to roughly 2.8 times the FP4 throughput of the export restricted H20.",
  "Taken with SMIC capacity gains, the ramp suggests export controls have slowed rather than stopped domestic accelerator supply. It also gives Chinese labs a credible reason to tune trillion parameter architectures for a non Nvidia stack."],
 [["RCR Wireless", "https://www.rcrwireless.com/20250922/ai-infrastructure/huawei-ai-chips"], ["Huawei Central", "https://www.huaweicentral.com/huawei-to-announce-new-ascend-ai-chip-solutions-at-waic-2026/"]])

add(False, C,
 "H200 sales to China resume with a 25% cut to the US Treasury",
 "Washington cleared Nvidia H200 exports to China with a 25% revenue share, but Beijing has capped fulfilment near 200,000 units and restricted their use.",
 ["The Trump administration reversed course on H200 exports, clearing sales to China on condition that recipients are vetted and that 25% of the revenue goes to the US Treasury. Commerce approved roughly ten Chinese firms including Alibaba, Tencent, ByteDance and JD.com to buy up to 75,000 units each, plus distributors.",
  "Actual volumes have lagged the paperwork. Commerce official Jeffrey Kessler told Congress in July that shipments had been very few despite around $10 billion in approved licences. Nvidia has since prepared a batch of roughly 82,000 GPUs for the market.",
  "Beijing has applied its own limits, permitting only about 200,000 H200 chips to be fulfilled and restricting the hardware to AI training on public data rather than inference or sensitive workloads. Nvidia's share of the Chinese accelerator market has continued to shrink even as the legal channel reopened."],
 [["CNBC", "https://www.cnbc.com/2026/01/14/trump-nvidia-h200-china-ai-chips.html"], ["Tom's Hardware", "https://www.tomshardware.com/tech-industry/semiconductors/nvidia-prepares-h200-shipments-to-china-as-chip-war-lines-blur"]])

# ---------------- Agents & Automation ----------------
add(False, A,
 "DeepSeek opens an agent harness to rival Claude Code",
 "DeepSeek released Harness v0.1 as an open source coding agent framework alongside V4-Pro, giving developers an alternative to closed agentic environments.",
 ["DeepSeek paired its V4-Pro API release with Harness v0.1, an open source agent harness aimed directly at developers who would otherwise reach for an integrated environment such as Claude Code. The move follows the lab's usual pattern of giving away the scaffolding and charging for the model.",
  "V4-Pro itself was tuned heavily for agentic workloads, with pricing raised above the previous flagship, an unusual step for a lab that built its reputation on undercutting Western APIs. The combination signals that DeepSeek sees long horizon tool use rather than chat as the product.",
  "The harness lands in a crowded field. Anthropic has Claude Code, OpenAI has a Codex desktop app for macOS that runs multiple agents in parallel, Meta has Muse Code for large repositories and Z.ai has ZCode. What differentiates DeepSeek's entry is that the orchestration layer itself is free to fork."],
 [["VentureBeat", "https://venturebeat.com/technology/deepseek-harness-launches-as-open-source-rival-to-claude-code-alongside-v4-pro-on-api-with-higher-prices"]])

add(False, A,
 "Z.ai launches ZCode as a free agentic development environment",
 "Zhipu's Z.ai released ZCode, a free desktop agent environment built around its GLM-5.2 model and aimed at Cursor, Claude Code and GitHub Copilot.",
 ["Z.ai, the international arm of newly listed Zhipu, released ZCode as a free desktop application it describes as an agentic development environment purpose built for its GLM-5.2 flagship. The pitch is a full local agent workspace rather than an editor plugin.",
  "Giving the tool away is consistent with the broader Chinese strategy of using open weights and free tooling to build developer share while Western rivals monetise the same layer. GLM-5.2 sits behind it, the successor to the GLM-4.7 model that narrowed the coding agent gap with Anthropic and Google DeepMind earlier this year.",
  "For Western incumbents the competitive pressure is on price rather than capability. Cursor charges for its Automations feature, GitHub Copilot is a subscription and Claude Code bills against API usage, all against a free alternative running a competent open model."],
 [["VentureBeat", "https://venturebeat.com/technology/z-ai-launches-zcode-to-challenge-cursor-claude-code-and-github-copilot-in-ai-coding"]])

add(False, A,
 "Meta ships Muse Code for whole repository engineering tasks",
 "Meta launched Muse Code, an agent built to complete software engineering tasks across large codebases, extending its Muse model family into developer tooling.",
 ["Meta launched Muse Code in early August, describing it as an agent that can accomplish complete software engineering tasks across large repositories rather than answering questions about individual files. It is the developer facing entry in the Muse family that Meta Superintelligence Labs began with Muse Spark in April and Muse Image in July.",
  "The launch fits a wider reorganisation under chief AI officer Alexandr Wang, who has pushed the group toward shipping discrete products after a period of expensive hiring and internal restructuring.",
  "Internally Meta has been recalibrating how it measures AI adoption. Wired reported that the company has softened review language around AI driven impact and token usage, easing off what employees had taken to calling tokenmaxxing, while continuing to promote its internal agent Hatch."],
 [["TechCrunch", "https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/"], ["Techmeme", "https://www.techmeme.com/260902/p49"]])

add(False, A,
 "Model Context Protocol gets its largest update since launch",
 "MCP finalised a move to a fully stateless architecture and adopted a formal 12-month deprecation policy in its biggest revision in twenty months.",
 ["The Model Context Protocol received its largest revision since it was published twenty months ago. The update completes the transition to a fully stateless architecture and introduces a formal twelve month deprecation policy, both aimed at making the standard safe to build production agent infrastructure on.",
  "Statelessness matters because it removes the requirement for a server to hold session context between calls, which simplifies horizontal scaling and makes agent tooling far easier to run behind load balancers. The deprecation policy addresses the other enterprise complaint, which was that the specification moved too fast to depend on.",
  "MCP has become the de facto integration layer for agent tooling across vendors, so changes to it ripple through Anthropic, OpenAI, Google and the long tail of startups building connectors. Salesforce, for example, shipped a plugin for Claude Cowork on 1 September carrying 37 prebuilt sales skills."],
 [["VentureBeat", "https://venturebeat.com/orchestration/mcp-just-got-its-biggest-update-ever-heres-what-changes-for-ai-agents"], ["VentureBeat", "https://venturebeat.com/technology/salesforce-launches-headless-360-to-turn-its-entire-platform-into-infrastructure-for-ai-agents"]])

add(False, A,
 "Uber cuts 3,300 jobs to fund a $10bn robotaxi pivot",
 "Uber is eliminating roughly 10% of its global workforce while committing more than $10 billion to autonomous vehicle partnerships and hiring 500 engineers.",
 ["Uber announced on 2 September that it will cut about 3,300 jobs, roughly 10% of its global workforce and its largest reduction since 2020. Chief executive Dara Khosrowshahi told staff the company had become too complex after years of rapid growth and that the restructuring will remove management layers, merge teams and cut the number of managers by 20%.",
  "This is a reallocation rather than a retrenchment. Uber has committed more than $10 billion to robotaxi partnerships and is keeping more than 500 open roles, nearly all engineering positions tied to autonomy. The company also withdrew from Nigeria and Uganda as part of the same review.",
  "The strategic bet is that Uber does not need to own the vehicles. If it supplies the app, the demand, the routing, payments and fleet management, it can sit above whichever autonomous stack wins. The risk is that the operators of those stacks reach the same conclusion in reverse."],
 [["Transport Topics", "https://www.ttnews.com/articles/uber-cut-3300-jobs-management"], ["Benzinga", "https://www.benzinga.com/markets/tech/26/09/61574935/uber-axes-3300-jobs-to-build-its-autonomous-future"]])

# ---------------- Enterprise & Regulation ----------------
add(False, E,
 "US government backs OpenAI in New York Times copyright case",
 "The Justice Department filed a brief in Manhattan federal court arguing that training large language models on copyrighted text is generally fair use.",
 ["The Trump administration filed a brief in Manhattan federal court siding with OpenAI in its copyright dispute with The New York Times, arguing that training large language models on copyrighted material generally qualifies as fair use. It is the first time the federal government has intervened in the wave of AI training copyright litigation.",
  "The filing states that the United States has a strong interest in the court rejecting any argument that training on copyrighted texts violates copyright law, citing scientific advancement and national security. The Times sued OpenAI and Microsoft in 2023 alleging that millions of its articles were ingested without permission to build ChatGPT.",
  "The intervention reaches well beyond one case. Authors, publishers, music labels and news outlets have brought parallel suits against OpenAI, Anthropic and Meta, and nearly all of them turn on the same fair use question. A government position carries no binding weight but gives defendants a powerful amicus to cite."],
 [["Quartz", "https://qz.com/trump-administration-openai-new-york-times-copyright-lawsuit-090226"], ["US News", "https://www.usnews.com/news/top-news/articles/2026-09-02/us-government-backs-openai-in-new-york-times-copyright-case"]])

add(False, E,
 "Sony and Warner Chappell sue Anthropic over song lyrics",
 "Two of the largest music publishers accuse Anthropic of a brazen campaign of intellectual property theft involving tens of thousands of copyrighted works.",
 ["Sony Music Publishing and Warner Chappell Music filed suit against Anthropic in the Northern District of California, alleging the company used tens of thousands of copyrighted songs to train Claude without permission. The complaint also names chief executive Dario Amodei and co-founder Benjamin Mann as defendants.",
  "The publishers allege Anthropic obtained lyrics and sheet music from pirate sources including Library Genesis and the Pirate Library Mirror and scraped licensed lyric sites such as Musixmatch and LyricFind. They seek statutory damages of up to $150,000 per wilfully infringed work plus up to $25,000 for each alleged removal of copyright management information.",
  "Anthropic said it disagrees with the claims and intends to defend itself robustly. The suit follows the $1.5 billion settlement the company reached with authors and publishers a year ago, evidence that the earlier resolution did not close the book on its training data provenance.",
  "Round Hill Music has separately sued Anthropic and Suno seeking up to $1 billion, and the timing is awkward given reporting that Anthropic is preparing a listing."],
 [["TechCrunch", "https://techcrunch.com/2026/08/29/sony-music-warner-sue-anthropic-alleging-a-brazen-campaign-of-intellectual-property-theft/"], ["Fortune", "https://fortune.com/2026/09/01/anthropic-warner-sony-music-songs-lawsuit/"]])

add(False, E,
 "Lutnick says Anthropic is back on the right side with Washington",
 "The Commerce Secretary said Anthropic has repaired relations with the Trump administration after months of conflict over military use and export controls.",
 ["Commerce Secretary Howard Lutnick said Anthropic is back on the right side with the Trump administration, signalling an end to months of open conflict between the company and Washington. He indicated the administration now trusts the firm after it complied with government requests.",
  "The dispute had been unusually public. Defence Secretary Pete Hegseth had blocked Anthropic from certain military contracts after the company insisted on guardrails including prohibitions on mass surveillance of Americans and autonomous weaponry, and in February the President directed every federal agency to phase out use of Anthropic technology over six months.",
  "The timing matters commercially. Anthropic is reported to be weighing a listing in September or October, and an unresolved standoff with the federal government would have been a difficult item to carry into a prospectus. Bloomberg reported the reconciliation followed the lifting of export controls affecting the company."],
 [["Bloomberg", "https://www.bloomberg.com/news/articles/2026-09-02/lutnick-says-anthropic-has-patched-relations-with-us-government"], ["Quartz", "https://qz.com/anthropic-trump-administration-good-standing-commerce-secretary-090226"]])

add(False, E,
 "EU AI Act enforcement begins with fines up to 3% of turnover",
 "The Commission started enforcing general purpose AI and transparency rules on 2 August, with the AI Office able to demand documentation and levy penalties.",
 ["The European Commission began enforcing the AI Act's general purpose model and transparency obligations on 2 August. Providers now face fines of up to 15 million euros or 3% of worldwide annual turnover, whichever is higher, for ignoring transparency duties.",
  "The substantive requirements are practical rather than abstract. Chatbots must identify themselves as automated systems, deepfakes must be labelled, and machine generated or edited content must carry machine readable marks so it can be detected automatically. That last obligation is why Anthropic now watermarks Claude outputs.",
  "Enforcement is split. The AI Office handles general purpose models directly with power to request technical documentation, run evaluations, demand corrective steps and issue fines, while national competent authorities supervise other AI systems in their own markets.",
  "The contrast with the United States is sharpening. Federal preemption provisions were stripped from both the One Big Beautiful Bill Act and the defence authorisation, leaving a patchwork in which California's AI Transparency Act became operative on the same day as the EU rules."],
 [["European Commission", "https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august"], ["Help Net Security", "https://www.helpnetsecurity.com/2026/08/04/eu-ai-act-enforcement-ai-models/"]])

add(False, E,
 "Anthropic retreats on data retention with Enterprise Frontier Safeguards",
 "After customer pushback Anthropic will let enterprises keep Claude monitoring logs in their own cloud and run human reviews themselves.",
 ["Anthropic announced Enterprise Frontier Safeguards, walking back a contested data retention policy after what the company described as a lot of feedback from business customers. The scheme gives enterprises privacy equivalent to zero data retention while preserving cross session misuse detection.",
  "The compromise is structural rather than cosmetic. Data is still retained, but customers control where it is hosted, and when human review is required they can conduct that review themselves rather than handing transcripts to Anthropic. Salesforce security teams worked with Anthropic on the design.",
  "The Register noted the practical catch, which is that customers must verify for themselves that the arrangement worked as promised. Rollout begins in phases this autumn.",
  "The policy sits at the centre of the enterprise adoption question. Regulated industries have been reluctant to route sensitive work through frontier models without guarantees about logs, and Anthropic has been open that data retention terms were suppressing usage of its most capable tier."],
 [["CNBC", "https://www.cnbc.com/2026/09/01/anthropic-data-retention.html"], ["Anthropic", "https://www.anthropic.com/news/enterprise-frontier-safeguards"], ["The Register", "https://www.theregister.com/ai-and-ml/2026/09/02/anthropic-promises-zero-data-retention-but-customers-must-check-it_worked/5293789"]])

add(False, E,
 "Substack turns AI detection into a reader facing feature",
 "Pangram raised $9 million and now powers a Substack tool that lets readers scan posts, notes and comments for AI generated text.",
 ["Pangram raised $9 million led by Menlo Ventures, taking total funding to roughly $14 million, and released Pangram 4 for text alongside an image detection model in research preview. The company claims better than 99% accuracy on AI assisted and mixed human machine writing.",
  "Substack integrated the technology in late July so readers can scan posts and Notes published from 21 July onward, along with individual comments and replies, through its Reader and iOS apps. The bet is that a meaningful share of subscribers will pay a premium for writing they can verify was written by a person.",
  "Detection has become a commercial category rather than an academic curiosity, driven partly by the EU AI Act's machine readable marking requirements and partly by publishing scandals in which established writers were found to have shipped model generated copy. The unresolved problem is that detectors and generators improve against each other, so accuracy claims age quickly."],
 [["TechCrunch", "https://techcrunch.com/2026/07/29/as-ai-content-floods-the-internet-pangram-raises-9m-to-detect-it/"], ["The AI Insider", "https://theaiinsider.tech/2026/08/07/ai-detection-startup-pangram-announces-9m-in-funding-launches-new-text-and-image-detection-models/"]])

data = {"ai-hpc": items}

# validation
assert sum(1 for i in items if i["hero"]) == 1, "hero count"
assert items[0]["hero"] is True
for i in items:
    assert len(i["h3"]) < 80, i["h3"]
    assert 2 <= len(i["body"]) <= 4, i["h3"]
    assert len(i["sources"]) >= 1
    for f in ("hero","sub","h3","summary","body","sources"):
        assert f in i
    blob = i["h3"] + i["summary"] + "".join(i["body"])
    assert "—" not in blob, i["h3"]

order = [i["sub"] for i in items]
seen = []
for s in order:
    if not seen or seen[-1] != s:
        assert s not in seen, "subsection not grouped: " + s
        seen.append(s)
print("subsections:", seen)

with open("/tmp/DailyNews/tools/data/data_b.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

with open("/tmp/DailyNews/tools/data/data_b.json", encoding="utf-8") as f:
    d = json.load(f)
print("stories:", len(d["ai-hpc"]))
