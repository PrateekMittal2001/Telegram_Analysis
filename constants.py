user_channel_list = ["https://t.me/teleTestingutkarsh", "https://t.me/PrateekTestingTelethon",
                     "https://t.me/Chad_Crypto", "https://t.me/R1C4RD0S4FUC4LLS", "https://t.me/pj69100x",
                     "https://t.me/erics_calls", "https://t.me/steezysgems", "https://t.me/KobesCalls",
                     'https://t.me/Owl_Calls', 'https://t.me/Maestro007Joe',
                     'https://t.me/prince_calls', 'https://t.me/ZizzlesTrapHouse',
                     'https://t.me/venomcalls', 'https://t.me/Caesars_Calls',
                     'https://t.me/medusacalls', 'https://t.me/CowboyCallz', 'https://t.me/Kingdom_X100_CALLS',
                     'https://t.me/MarkGems',
                     'https://t.me/gollumsgems', 'https://t.me/SapphireCalls', 'https://t.me/DoxxedChannel',
                     'https://t.me/bruiserscalls', 'https://t.me/FatApeCalls', 'https://t.me/gubbinscalls',
                     'https://t.me/ValhallaCalls', 'https://t.me/TheSolitaireRoom',
                     'https://t.me/steezysgems', 'https://t.me/KobesCalls',
                     'https://t.me/Chad_Crypto',  'https://t.me/erics_calls',
                     'https://t.me/R1C4RD0S4FUC4LLS', 'https://t.me/Owl_Calls',
                     'https://t.me/gumballsgemcalls01', 'https://t.me/gilt_calls', 'https://t.me/MAGICDEFIICALLS',
                     'https://t.me/TheDonsCalls', 'https://t.me/venomcalls', 'https://t.me/medusacalls',
                     'https://t.me/DarenCalls', 'https://t.me/Erc20Gods', 'https://t.me/CasasReviews',
                     'https://t.me/KURUKUNCALLS', 'https://t.me/CallofAngels', 'https://t.me/CallofAngels',
                     'https://t.me/GEMCALLS11',  'https://t.me/Natsucalls',
                     'https://t.me/CallofAngels', 'https://t.me/kermitcall', 'https://t.me/MoonDefiiCall',
                     'https://t.me/ValhallaCalls', 'https://t.me/zombiecalls1',
                     'https://t.me/Gon_Calls', 'https://t.me/MidnightCallss', 'https://t.me/Conan_calls',
                     'https://t.me/NINJA_CALL', 'https://t.me/escobarcalls100x', 'https://t.me/GRIZZLYCALLSS',
                     'https://t.me/ihzanswhaleschool', 'https://t.me/Lightingcalls', 'https://t.me/Apeology',
                     'https://t.me/mommycalls', 'https://t.me/SamuraiCaller', 'https://t.me/karmacalls',
                     'https://t.me/astrodeficalls', 'https://t.me/Village_Calls', 'https://t.me/hashiramasinju101',
                     'https://t.me/Ezcoinmarketcalls', 'https://t.me/croccall', 'https://t.me/uzumakicalls',
                     'https://t.me/Village_Calls']


not_working_channel_list = ["https://t.me/mrbeast6000calls/10", 'https://t.me/mrbeast6000calls/10',
                            'https://t.me/Crizalcalls', 'https://t.me/Ghilliegamble',
                            'https://t.me/+ZVqgZ6EDWlFiZGFl', "https://t.me/+Zx0NSl91_FljYjZh",]


INSERT_COIN_DATA_TO_TABLE = "INSERT INTO telegram_coin_data (token_name, website_link, dextool_link, telegram_link, twitter_link) VALUES ('{token}', '{weblink}', '{dexlink}', '{telelink}', '{twitterlink}')"
GET_JOINING_LINKS = "SELECT * FROM telegram_channels;"
INSERT_LINK_TO_TABLE = "INSERT INTO telegram_channels (channel_link, joining_status) VALUES ('{joining_link}', '{joining_status}');"