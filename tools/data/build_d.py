import json

data = {
  "sports": [
    {
      "hero": True,
      "sub": "Tennis",
      "h3": "Sabalenka and Alcaraz cruise into US Open quarterfinals",
      "summary": "Defending champions Aryna Sabalenka and Carlos Alcaraz both advanced at Flushing Meadows on Sunday 6 September, setting up a heavyweight final week.",
      "body": [
        "Aryna Sabalenka beat Taylor Townsend 6-4, 6-3 on Sunday 6 September to reach the US Open quarterfinals as the defending champion and top seed. On the men's side Carlos Alcaraz needed just over two hours to see off Tommy Paul 6-4, 6-3, 6-4, continuing his bid for a second straight US Open title. Both wins came on Arthur Ashe Stadium in front of sellout crowds on the tournament's second Sunday.",
        "Elsewhere in the men's draw, Frances Tiafoe outlasted Daniil Medvedev 7-6(1), 6-4, 7-6(6) in a match that swung on two tight tiebreaks, while Ben Shelton dismissed Stefanos Tsitsipas 6-2, 6-3, 6-4 to reach his third straight US Open quarterfinal. Sabalenka now waits to see whether Wimbledon champion Linda Noskova or Marta Kostyuk will stand across the net for a semifinal spot, with the tournament running through 13 September."
      ],
      "sources": [
        ["The Washington Post", "https://www.washingtonpost.com/sports/tennis/2026/09/06/us-open-day-eight-results/fd876800-aa0b-11f1-b498-8697f35a6743_story.html"],
        ["Al Jazeera", "https://www.aljazeera.com/sports/2026/9/6/sabalenka-through-to-us-open-quarterfinals"],
        ["Bleacher Report", "https://bleacherreport.com/articles/25496817-us-open-tennis-2026-results-sundays-bracket-winners-losers-and-highlights"]
      ]
    },
    {
      "hero": False,
      "sub": "Tennis",
      "h3": "Laver Cup rosters locked in for O2 Arena return",
      "summary": "Team Europe and Team World confirmed their full six man lineups on Monday 7 September ahead of the Laver Cup running 25-27 September in London.",
      "body": [
        "Team Europe will lean on Carlos Alcaraz as its headline act, supported by Alexander Zverev, Casper Ruud, Flavio Cobolli, Jakub Mensik and Rafael Jodar, with Yannick Noah returning as captain for the ninth edition of the event. Team World counters with Alex de Minaur, Ben Shelton and Taylor Fritz leading a squad rounded out by Alexander Bublik, Learner Tien and Tommy Paul, coached by Andre Agassi.",
        "The event returns to London's O2 Arena with Team World defending the title it won in 2025, breaking Europe's long stranglehold on the trophy. Organizers expect Alcaraz's participation, fresh off his US Open run, to be the main draw for ticket sales, though his workload through the American hard court swing has raised questions about how fresh he will look by the London weekend."
      ],
      "sources": [
        ["Puntodebreak", "https://www.puntodebreak.com/en/2026/07/28/the-laver-cup-2026-officially-announces-all-the-players-who-will-participate"],
        ["LTA", "https://lta.org.uk/news/laver-cup-2026-tickets-dates-and-pre-sale"]
      ]
    },
    {
      "hero": False,
      "sub": "Tennis",
      "h3": "Davis Cup playoff ties take shape for later this month",
      "summary": "With the US Open in its final week, attention is turning to Davis Cup qualifiers and World Group playoffs scheduled for 18-19 and 19-20 September.",
      "body": [
        "The Davis Cup calendar for 2026 lists a second round of qualifiers alongside World Group I and World Group II playoff ties in the middle of September, giving national federations a narrow window to finalize squads once the US Open wraps up. Several nations are expected to lean on players who reach deep rounds in New York, creating scheduling headaches for captains balancing recovery time against team commitments.",
        "The ties carry weight for promotion and relegation within the Davis Cup's tiered format, with results feeding into who competes at the higher levels in 2027. Federations are expected to confirm final squads in the coming days once the Flushing Meadows draw is fully resolved."
      ],
      "sources": [
        ["Davis Cup", "https://www.daviscup.com/en/calendar_2026"]
      ]
    },
    {
      "hero": False,
      "sub": "Formula 1",
      "h3": "Antonelli storms from 19th to win home Italian Grand Prix",
      "summary": "Kimi Antonelli produced a stunning comeback drive to win the Italian Grand Prix at Monza on Sunday 6 September, becoming the first Italian to win there in 60 years.",
      "body": [
        "Kimi Antonelli started 19th on the grid and fought through the field to beat Mercedes teammate George Russell by 3.857 seconds, with Max Verstappen completing the podium 14.718 seconds back. It was the first time an Italian driver had won his home grand prix since Ludovico Scarfiotti's victory in 1966, and it came in front of a delirious tifosi crowd at the Tempio della Velocita.",
        "The result extended Antonelli's championship lead over Russell to 66 points, nearly three race wins clear with the season entering its final stretch. Further back, Lewis Hamilton finished sixth behind both McLarens, pole sitter Pierre Gasly came home seventh, and Charles Leclerc's home race ended in disappointment after he crashed out on just the third lap."
      ],
      "sources": [
        ["Formula1.com", "https://www.formula1.com/en/latest/article/antonelli-beats-russell-to-italian-grand-prix-win-with-stunning-comeback-drive.15WtFEBT5JEe4drdeO88t2"],
        ["The Race", "https://www.the-race.com/formula-1/f1-2026-italian-grand-prix-race-results/"]
      ]
    },
    {
      "hero": False,
      "sub": "Football",
      "h3": "PSV crush Ajax 3-1 in season's first Eredivisie classic",
      "summary": "PSV Eindhoven beat Ajax 3-1 on Saturday 5 September in the first Klassieker of the new season, sending an early title-race statement.",
      "body": [
        "The reigning champions took control of the match in Eindhoven and never let go, converting their chances while Ajax struggled to break down a well organized PSV backline. The win continued PSV's strong start to the campaign as they look to defend the title they claimed for a third straight season the previous term.",
        "Ajax will have to regroup quickly with a congested September fixture list ahead, while PSV fans left the Philips Stadion already dreaming of another title defense. The result also reopened old wounds in a rivalry that has swung heavily PSV's way over the past few seasons."
      ],
      "sources": [
        ["Total Dutch Football", "https://totaldutchfootball.com/2026/09/05/eredivisie-saturday-ajax-vs-psv-preview/"],
        ["DutchNews.nl", "https://www.dutchnews.nl/2026/04/psv-seal-eredivisie-title-after-feyenoord-draw-in-volendam/"]
      ]
    },
    {
      "hero": False,
      "sub": "Football",
      "h3": "Groningen and Twente share spoils in tight draw",
      "summary": "Groningen and Twente drew 2-2 on Sunday 6 September as the rest of the Eredivisie round played out across the country.",
      "body": [
        "The two sides traded goals throughout the match without either finding a winner, leaving both with a point apiece in a congested midtable picture. The draw came on a weekend that also featured Heerenveen hosting AZ, Telstar taking on Cambuur, and a clash between ADO Den Haag and Fortuna Sittard.",
        "With PSV pulling clear at the top after their win over Ajax, the battle for the rest of the European qualification places remains wide open through the opening weeks of the season. Neither Groningen nor Twente will be satisfied with a draw given both sides' ambitions to push into the top half of the table this term."
      ],
      "sources": [
        ["Football Web Pages", "https://www.footballwebpages.co.uk/dutch-eredivisie/fixtures-results"]
      ]
    },
    {
      "hero": False,
      "sub": "Football",
      "h3": "Oranje squad readies for final World Cup qualifying tests",
      "summary": "Already through to the 2026 World Cup, the Netherlands is preparing for qualifying fixtures against Germany on 24 September and Serbia on 27 September.",
      "body": [
        "The Dutch squad list features Jurrien Timber, Frenkie de Jong and Memphis Depay all included, while Jeremie Frimpong misses out as the squad sharpens ahead of the group's remaining matches. The Netherlands sealed its World Cup spot back in November with a 4-0 win over Lithuania, capping an unbeaten qualifying campaign in which they scored 27 goals across eight games.",
        "Even with qualification secured, coach Ronald Koeman is expected to use the September window to test combinations and fitness levels ahead of next summer's tournament in the United States, Mexico and Canada. The clash with Germany in particular carries extra edge given the historic rivalry between the two neighbors."
      ],
      "sources": [
        ["UEFA.com", "https://www.uefa.com/european-qualifiers/news/02a6-20d15935831f-d0d88d0f1da0-1000--netherlands-at-the-world-cup-2026-squad-fixtures-group-a/"],
        ["Olympics.com", "https://www.olympics.com/en/news/fifa-world-cup-2026-netherlands-players-squad-list-key-stats-schedule"]
      ]
    },
    {
      "hero": False,
      "sub": "Sailing",
      "h3": "SailGP grows to record 13 nation fleet for new season",
      "summary": "SailGP's 2026 season is underway with a record 13 national teams and a 12.8 million dollar prize purse, building toward the next stop in Saint-Tropez.",
      "body": [
        "The league's growth this season includes the debut of Artemis SailGP representing Sweden, led by Olympic veteran Iain Percy and driven by Nathan Outteridge, joining a fleet that now spans nine venues from Perth to Abu Dhabi. The Saint-Tropez stop is set for 12-13 September, giving European fans a rare close look at the F50 catamarans racing in home waters.",
        "SailGP's expansion comes as the league jostles for position alongside the America's Cup, with several top sailors now having to choose which circuit to prioritize as calendars increasingly overlap. Organizers see the bigger fleet and prize pool as key to cementing SailGP's place as a season long championship rather than a series of one-off exhibitions."
      ],
      "sources": [
        ["Yachting World", "https://www.yachtingworld.com/tag/sailgp"],
        ["US SailGP Team", "https://www.ussailgpteam.com/news"]
      ]
    },
    {
      "hero": False,
      "sub": "Sailing",
      "h3": "America's Cup challengers push on toward Naples 2027",
      "summary": "Challenger of Record GB1 Athena Racing continues its build toward the 38th America's Cup match in Naples in July 2027.",
      "body": [
        "Emirates Team New Zealand remains the defender, while Ben Ainslie's GB1 Athena Racing holds Challenger of Record status heading into a cycle that will see the Preliminary Regatta held in Cagliari, Sardinia in May, with teams racing AC40 foiling monohulls. The cycle has drawn attention for tension between the Cup and SailGP over athlete availability, a dynamic that has intensified as both events schedule more racing.",
        "Teams are using the current window to refine boat designs and sailor lineups before the pressure of the Naples match builds through 2027. The Cup's return to Italian waters is expected to draw one of the largest crowds in the event's modern history given the country's growing sailing fanbase."
      ],
      "sources": [
        ["Sail-World", "https://www.sail-world.com/news/293190/Crunch-time-for-SailGP-and-the-Cup"]
      ]
    },
    {
      "hero": False,
      "sub": "Grappling & Judo",
      "h3": "ADCC heads to Poland for biggest grappling weekend of the year",
      "summary": "The 2026 ADCC World Championship moves to Krakow's Tauron Arena on 12-13 September, marking the event's first ever visit to Poland.",
      "body": [
        "The no-gi grappling world's most prestigious title fight brings together ADCC champions, trials winners and elite invitees for two days of competition, with organizers highlighting a strong crop of rookies expected to shake up the brackets. FloSports holds exclusive streaming rights, with FloGrappling also carrying the ADCC Amateur Worlds and Fight to Win 324 across the same weekend.",
        "The move to Poland reflects ADCC's continued push to grow its footprint in Europe after years of events concentrated in the Middle East and United States. Early bouts are expected to stream free on YouTube, a move organizers hope will widen the audience beyond dedicated grappling fans."
      ],
      "sources": [
        ["FloGrappling", "https://www.flograppling.com/articles/15999460-5-things-to-know-about-the-2026-adcc-world-championship"],
        ["FloGrappling", "https://www.flograppling.com/articles/16143212-the-top-rookies-ready-to-shake-up-adcc-2026"]
      ]
    },
    {
      "hero": False,
      "sub": "Grappling & Judo",
      "h3": "Judo's Grand Slam circuit rolls into Budapest",
      "summary": "The Hungary Grand Slam runs 11-13 September in Budapest, drawing 547 judoka from 71 countries to the International Judo Federation's home city.",
      "body": [
        "The Budapest stop carries extra symbolism as the host city of the IJF's headquarters, and it forms part of a packed 2026 Grand Slam calendar that also includes Tashkent, Tbilisi, Dushanbe, Astana, Ulaanbaatar, Abu Dhabi and Tokyo. Organizers describe the entry list as one of the strongest of the season given the scale of participation.",
        "The event gives judoka a key opportunity to bank ranking points ahead of the season's championship events, with several Olympic medalists expected to compete. Hungarian fans are expected to turn out in force given judo's strong following in the country."
      ],
      "sources": [
        ["IJF.org", "https://www.ijf.org/news/show/a-packed-2026-season-ahead-for-world-judo"]
      ]
    }
  ],
  "consumer-tech": [
    {
      "hero": True,
      "sub": "Devices & Launches",
      "h3": "Apple set for foldable iPhone reveal at Surprise and Shine event",
      "summary": "Apple confirmed its September 9 event will be new CEO John Ternus's first product launch, with rumors pointing to a foldable iPhone alongside the iPhone 18 Pro line.",
      "body": [
        "Apple's Surprise and Shine event is set for Wednesday 9 September at 10am Pacific, and it doubles as John Ternus's debut as chief executive after taking over from Tim Cook on 1 September. Rumors ahead of the show point to a book style foldable iPhone, possibly branded iPhone Ultra, with a roughly 5.5 inch outer OLED display that unfolds into a display near 7.8 inches. The iPhone 18 Pro and Pro Max are also expected, alongside new Apple Watches and AirPods.",
        "Apple is skipping a standard iPhone 18 this year and will wait until spring 2027 to launch a cheaper model, according to previews circulating on Monday 7 September. The event is also expected to bring release dates for iOS 27, iPadOS 27, macOS Golden Gate, tvOS 27, watchOS 27 and visionOS 27, giving developers and users a clearer picture of the software roadmap for the year ahead."
      ],
      "sources": [
        ["MacRumors", "https://www.macrumors.com/guide/apple-september-2026-what-to-expect/"],
        ["TidBITS", "https://tidbits.com/2026/08/28/apples-surprise-and-shine-event-set-for-9-september-2026/"]
      ]
    },
    {
      "hero": False,
      "sub": "Devices & Launches",
      "h3": "IFA Berlin closes with AI appliances and first Wi-Fi 8 routers",
      "summary": "IFA Berlin 2026 wrapped up its run from 4 to 8 September with AI-heavy home appliances, new routers and toothbrushes headlining the show floor.",
      "body": [
        "Samsung expanded its Bespoke AI lineup with deeper generative features across fridges, washing machines and robot vacuums, using local neural processing so devices can manage power use without needing constant cloud access. LG's presentation leaned on energy efficient smart living and transparent OLED display technology, while TP-Link used the show to reveal the first Wi-Fi 8 routers, the Archer 8 Ultra and a companion Deco 8 Ultra mesh system.",
        "Dyson unveiled a 500 dollar electric toothbrush called the CameraJet, its first, built with an AI camera and integrated water flosser, and Anker showed off a bedside speaker called SleepLab Pro that tracks sleep, heart rate and breathing without a wearable. The 2026 IFA Innovation Awards went to Anker, Insta360 and LG Electronics as the three main prize winners, with further recognition spread across 13 additional categories."
      ],
      "sources": [
        ["Tech Digest", "https://www.techdigest.tv/2026/09/ifa-2026-key-announcements-so-far.html"],
        ["Gizmodo", "https://gizmodo.com/live-updates-from-ifa-2026-in-berlin-2000800025"]
      ]
    },
    {
      "hero": False,
      "sub": "Devices & Launches",
      "h3": "Huawei's Mate XT2 tri-fold lands two days before Apple",
      "summary": "Huawei unveiled its second generation tri-fold phone, the Mate XT2, on Monday 7 September, just ahead of Apple's own foldable reveal.",
      "body": [
        "The Mate XT2 runs Huawei's Kirin 9050 Pro chip and keeps the two hinge design of its predecessor, but now folds inward to protect the main screen when closed rather than leaving part of the display exposed. Huawei says it is the first folding phone with a hardware level anti peeping screen that blocks side viewers from reading private content, and pricing starts at 19,999 yuan, about 2,800 dollars, rising to 24,999 yuan for the 1TB version with the privacy screen. Sales begin on 12 September.",
        "Analysis firm Omdia forecasts foldable phone shipments will rise 22 percent in 2026 to more than 22 million units, a sharp jump from 2025's 6 percent growth, underlining how competitive the category has become just as Apple prepares to enter it for the first time."
      ],
      "sources": [
        ["Business Today", "https://www.businesstoday.in/technology/news/story/huawei-mate-xt2-is-here-tri-fold-phone-takes-on-apple-ahead-of-foldable-iphone-launch-553728-2026-09-07"],
        ["TechRepublic", "https://www.techrepublic.com/article/news-huawei-mate-xt2-tri-fold-apac-china/"]
      ]
    },
    {
      "hero": False,
      "sub": "Devices & Launches",
      "h3": "Sony revives budget favorite with new XM4C headphones",
      "summary": "Sony relaunched its well reviewed WH-1000XM4 as the cheaper XM4C on Monday 7 September, alongside two new budget models.",
      "body": [
        "The WH-1000XM4C arrives at 299.99 dollars in Lavender, Black and Platinum Silver, keeping the QN1 noise cancelling chip, multipoint Bluetooth and both 10 band and gaming focused EQ presets from the original. It sits below Sony's current flagship WH-1000XM6, giving budget conscious buyers a proven design at a lower price point.",
        "Sony also released the WH-CH730N at 179.99 dollars and the WH-CH530 at 69.99 dollars, both aimed at shoppers who want noise cancellation or basic wireless listening without the premium price tag. The three launches together give Sony a wider spread across price tiers heading into the holiday shopping season."
      ],
      "sources": [
        ["9to5Toys", "https://9to5toys.com/2026/09/07/sony-upgrades-1000xm4-new-xm4c-headphones/"],
        ["9to5Google", "https://9to5google.com/2026/09/07/sony-wh-1000xm4c-launch-for-299-alongside-two-more-affordable-headphones/"]
      ]
    },
    {
      "hero": False,
      "sub": "Devices & Launches",
      "h3": "iPhone 18 Pro camera leaks tease variable aperture control",
      "summary": "Code leaks published Monday 7 September point to new camera features for the iPhone 18 Pro Max just two days before Apple's event.",
      "body": [
        "The leaked code describes an exclusive variable aperture feature for the iPhone 18 Pro Max, along with a manual focus slider that lets users adjust focus distance without a third party app. iOS 27 is also said to support aperture based image correction, blending between as many as four reference points to keep photos sharp across different aperture settings.",
        "Other rumors point to a possible Dark Cherry color option and a new A20 chip, with some reports suggesting a price increase in certain markets including the UAE. With the official unveiling set for Wednesday 9 September, these leaks give the clearest picture yet of what Apple's camera team has been working on this year."
      ],
      "sources": [
        ["MacRumors", "https://www.macrumors.com/2026/09/07/five-iphone-18-pro-camera-features-seemingly-leak/"],
        ["Gulf News", "https://gulfnews.com/technology/iphone-18-pro-7-biggest-leaks-before-you-upgrade-camera-dark-cherry-design-and-more-1.500610815"]
      ]
    },
    {
      "hero": False,
      "sub": "Devices & Launches",
      "h3": "Meta previews longer-lasting Ray-Ban Gen 3 glasses",
      "summary": "Meta is teasing its Ray-Ban Meta Gen 3 glasses ahead of Meta Connect on 23 September, promising hours of continuous AI use instead of minutes.",
      "body": [
        "The Gen 3 glasses are expected to run Live AI for hours at a stretch, up from roughly 30 minutes on the current generation, turning the glasses into what Meta describes as an all day memory layer. A faster onboard chip is expected to handle more AI processing directly on the device, while wind tuned microphones aim to make outdoor calls clearer, and battery life is being built to last a full day on a single charge, addressing one of the most common complaints about the current lineup.",
        "The preview follows Meta's June launch of a cheaper 299 dollar smart glasses line built with Ray-Ban parent EssilorLuxottica but without Ray-Ban or Oakley branding, showing the company pushing on two fronts at once as it tries to make wearable AI mainstream."
      ],
      "sources": [
        ["The Gadgeteer", "https://the-gadgeteer.com/2026/05/25/smart-glasses-2026-design-strategy/"],
        ["CNBC", "https://www.cnbc.com/2026/06/23/meta-glasses-are-new-smart-glasses-starting-at-299.html"]
      ]
    },
    {
      "hero": False,
      "sub": "Software & Services",
      "h3": "Android's September drop adds Gemini memory and calmer rides",
      "summary": "Google's September 2026 Android Feature Drop, rolling out this week, adds five updates including Gemini powered item tracking and a new motion sickness aid.",
      "body": [
        "Gemini can now remember where users have placed items through Find Hub, and Gemini Live's Guided Vision feature offers spoken descriptions and reframing tips for low light or fine print situations. Google Messages picks up native Google Keep list sharing inside chats along with custom Chat Themes that match text bubble colors to a chosen design.",
        "The new Motion Assist feature displays a bubble like overlay that moves in the direction of travel, aiming to reduce motion sickness for passengers using their phones in a moving vehicle. Google also quietly added infrastructure to a Kids Auth Module meant to manage regulatory compliance notices on Android devices used by younger users."
      ],
      "sources": [
        ["9to5Google", "https://9to5google.com/2026/09/07/september-2026-google-system-updates/"],
        ["Google Blog", "https://blog.google/products-and-platforms/platforms/android/android-drop-september-2026/"]
      ]
    },
    {
      "hero": False,
      "sub": "Software & Services",
      "h3": "OpenAI ships GPT-6 Astra across ChatGPT and Codex",
      "summary": "OpenAI rolled out GPT-6 Astra on Friday 4 September, a major model upgrade for computer use, browsing and professional work that is still generating headlines this week.",
      "body": [
        "The new model targets computer use, web browsing, software engineering and science tasks, and OpenAI says it completes computer use tasks nearly twice as fast as before while preserving more context in Codex sessions. The rollout covers ChatGPT, the API, Azure and Amazon Bedrock, and adds beta plugins for Zendesk and OneNote along with the ability for eligible users to share live Sites outside their workspace.",
        "Alongside the model launch, OpenAI introduced Daybreak for Frontline Defenders, a 1 billion dollar initiative offering subsidized access to its Daybreak cyber models, training and technical support to help defenders of essential services in the United States and abroad guard against cyberattacks."
      ],
      "sources": [
        ["9to5Mac", "https://9to5mac.com/2026/09/04/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/"]
      ]
    },
    {
      "hero": False,
      "sub": "EVs & Mobility",
      "h3": "Rivian unifies its lineup with RivianOS 2 rollout",
      "summary": "Rivian began rolling out RivianOS 2 this week, the biggest software overhaul since the original R1 launched, unifying its full vehicle lineup on one platform.",
      "body": [
        "Version 2026.31 brings first and second generation R1 vehicles together with the mass market R2 on a single software foundation for the first time, featuring a rebuilt interface with context aware controls and real time police and speed camera alerts. Newer hardware gains Unreal Engine 5 rendering for onscreen visuals, and an expanded AI layer called Unified Intelligence aims to make the car's assistant more capable across daily tasks.",
        "The update lands as Rivian prepares two events this month marking the restart of construction on its 5 billion dollar EV plant in Georgia and the opening of its East Coast headquarters in Atlanta later this year, signaling the company is pushing forward on manufacturing expansion even as it refines existing vehicles."
      ],
      "sources": [
        ["Electrek", "https://electrek.co/2026/07/13/california-ev-rebate-rivian-lucid-tesla/"],
        ["WardsAuto", "https://www.wardsauto.com/news/archive-auto-rivian-supply-chain-manufacturing-scaling-r2-production/757493/"]
      ]
    },
    {
      "hero": False,
      "sub": "EVs & Mobility",
      "h3": "Tesla FSD update can now override manual driving to dodge a crash",
      "summary": "Tesla is rolling out a new Full Self-Driving Supervised version this week that can intervene even when a driver is manually controlling the car to avoid a collision.",
      "body": [
        "The update expands Tesla's crash avoidance systems beyond passive alerts, allowing the software to take corrective action in real time if it detects an imminent collision while a human is behind the wheel. The change reflects Tesla's continued push to fold more autonomous safety features into vehicles still classified as requiring driver supervision.",
        "The rollout comes as Tesla works to keep its share of the EV market steady after a rocky first half of 2026, with the company still accounting for 45 percent of new EV sales in the country despite an 8.4 percent year over year sales decline in the first quarter. Safety focused updates like this one are seen as a way to differentiate Tesla's driver assistance suite from rivals as competition intensifies."
      ],
      "sources": [
        ["Electrek", "https://electrek.co/"]
      ]
    },
    {
      "hero": False,
      "sub": "EVs & Mobility",
      "h3": "Lucid presses ahead with operational reset after big loss",
      "summary": "Lucid Motors continues implementing its operational reset this week after a 1.02 billion dollar quarterly net loss and its largest ever recall.",
      "body": [
        "Lucid identified 1.4 billion dollars in potential cash flow improvements for 2026 across operating expenses, capital spending and working capital, organizing the effort around three priorities the company calls Cash and Cost, Customer and Quality, and Culture and Team. The reset followed a recall covering 27,185 vehicles, a number that exceeds the company's total sales from the prior year, even as quarterly revenue rose 56 percent.",
        "Lucid has cut its US workforce by 18 percent, on top of an earlier 12 percent reduction, and dropped a second production shift at its Arizona plant as it works to control costs. On the brighter side, the Lucid Gravity SUV was named 2026 World Luxury Car of the Year, and Gravity robotaxi test vehicles have begun service with both Uber and Nuro."
      ],
      "sources": [
        ["Lucid Group IR", "https://ir.lucidmotors.com/news-releases/news-release-details/lucid-announces-operational-reset-and-second-quarter-2026/"],
        ["CarBuzz", "https://carbuzz.com/lucid-slashes-staff-second-time-2026/"]
      ]
    },
    {
      "hero": False,
      "sub": "EVs & Mobility",
      "h3": "US falls behind as global EV sales keep climbing",
      "summary": "A global EV outlook highlighted this week shows the United States falling behind a worldwide sales boom after the loss of federal purchase incentives.",
      "body": [
        "US EV buyers purchased around 216,000 new electric cars in the first quarter of 2026, a 27 percent drop from the year before, with EVs slipping to 5.8 percent of new vehicle sales after peaking near 10.6 percent in the third quarter of 2025. The slide followed the termination of federal tax credits for new and used EV purchases after September 2025, alongside a proposed annual 250 dollar fee for EV owners in some states.",
        "Globally the picture looks very different, with international sales continuing to climb even as the American market cools. Tesla still accounts for 45 percent of US EV sales despite its own 8.4 percent year over year decline, underscoring how much the entire domestic market has softened rather than any single automaker losing ground to rivals."
      ],
      "sources": [
        ["Rest of World", "https://restofworld.org/2026/iea-global-ev-outlook-us-sales-drop/"]
      ]
    }
  ]
}

with open("/tmp/DN/tools/data/data_d.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("written")
