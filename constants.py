user_channel_list = ['https://t.me/PrateekTestingTelethon', 'https://t.me/PrateekandutkarshGroup',
                     'https://t.me/teleTestingutkarsh', 'https://t.me/GEMCALLS11', 'https://t.me/Natsucalls',
                     'https://t.me/bishopgemsx100',
                     'https://t.me/CKGEMSANN', 'https://t.me/OnePunchCallsOfficial', 'https://t.me/Joe420Calls',
                     'https://t.me/Noodles_calls', 'https://t.me/bruiserscalls', 'https://t.me/UniApes',
                     'https://t.me/doracalls', 'https://t.me/matadormoonshots', 'https://t.me/KilluaZoldyckCalls',
                     'https://t.me/REtardCEntrAl', 'https://t.me/R1C4RD0S4FUC4LLS', 'https://t.me/SapphireCalls',
                     'https://t.me/steezysgems', 'https://t.me/mommycalls', 'https://t.me/DobbysGems',
                     'https://t.me/DarenCalls', 'https://t.me/WOLFS_GEM_CALLS',
                     'https://t.me/hashiramasinju101', 'https://t.me/astrodeficalls', 'https://t.me/GRIZZLYCALLSS',
                     'https://t.me/zekecalls', 'https://t.me/karmacalls', 'https://t.me/travladdsafureviews',
                     'https://t.me/Gon_Calls', 'https://t.me/MidnightCallss',
                     'https://t.me/TheSolitaireRoom',
                     'https://t.me/CryptCallsPublic', 'https://t.me/prince_calls', 'https://t.me/escobarcalls100x',
                     'https://t.me/Owl_Calls', 'https://t.me/travladdsafucalls', 'https://t.me/CallofAngels',
                     'https://t.me/CowboyCallz', 'https://t.me/Kingdom_X100_Calls_Chat', 'https://t.me/saulsafucalls',
                     'https://t.me/MarkGems', 'https://t.me/FatApeCalls', 'https://t.me/MoonDefiiCall',
                     'https://t.me/goobygamblers', 'https://t.me/KobesCalls', 'https://t.me/thorshammergems',
                     'https://t.me/CatfishcallsbyPoe', 'https://t.me/Maestro007Joe', 'https://t.me/Kingdom_X100_CALLS',
                     'https://t.me/Rickscalls', 'https://t.me/ZizzlesTrapHouse', 'https://t.me/erics_calls',
                     'https://t.me/NINJA_CALL', 'https://t.me/gubbinscalls', 'https://t.me/Chad_Crypto',
                     'https://t.me/pj69100x', 'https://t.me/SKULLSGEMSx100', 'https://t.me/Conan_calls',
                     'https://t.me/MAGICDEFIICALLS', 'https://t.me/SKULLSGEMS', 'https://t.me/kermitcall',
                     'https://t.me/CasasReviews', 'https://t.me/cryptocuckd', 'https://t.me/rektsfamily',
                     'https://t.me/DoxxedChannel', 'https://t.me/venomcalls', 'https://t.me/gilt_calls',
                     'https://t.me/medusacalls', 'https://t.me/Village_Calls', 'https://t.me/defiangelsDEALFLOW',
                     'https://t.me/AeonsGems', 'https://t.me/bagcalls', 'https://t.me/rockefellerscalls',
                     'https://t.me/KURUKUNCALLS', 'https://t.me/DeFiWinners',
                     'https://t.me/jammas100x', 'https://t.me/mcm_tg', 'https://t.me/ValhallaCalls',
                     'https://t.me/gumballsgemcalls01', 'https://t.me/ihzanswhaleschool', 'https://t.me/Erc20Gods',
                     'https://t.me/uzumakicalls', 'https://t.me/earlyapes', 'https://t.me/Caesars_Calls',
                     'https://t.me/Ezcoinmarketcalls', 'https://t.me/gollumsgems', 'https://t.me/luffysgemscalls',
                     'https://t.me/chiroscalls', 'https://t.me/drakosmoonshotz', 'https://t.me/Lightingcalls',
                     'https://t.me/Apeology', 'https://t.me/RickandMortysCalls', 'https://t.me/SamuraiCaller',
                     'https://t.me/tryTelethon1', 'https://t.me/vegetacalls', 'https://t.me/powsdegencamp',
                     'https://t.me/DumpsterDAO', 'https://t.me/TheDonsCalls', 'https://t.me/zombiecalls1',
                     "https://t.me/shitco1nguru"]

not_working_channel_list = ["https://t.me/mrbeast6000calls/10", 'https://t.me/mrbeast6000calls/10',
                            'https://t.me/Crizalcalls', 'https://t.me/Ghilliegamble',
                            'https://t.me/+ZVqgZ6EDWlFiZGFl', "https://t.me/+Zx0NSl91_FljYjZh", 'https://t.me/croccall']

INSERT_COIN_DATA_TO_TABLE = "INSERT INTO telegram_coin_data (token_symbol, website_link, dextool_link, telegram_link, twitter_link) VALUES ('{token}', '{weblink}', '{dexlink}', '{telelink}', '{twitterlink}')"
GET_JOINING_LINKS = "SELECT channel_link FROM telegram_channels;"
INSERT_LINK_TO_TABLE = "INSERT INTO telegram_channels (channel_link, joining_status) VALUES ('{joining_link}', '{joining_status}');"
GET_TOKEN_SYMBOL = "SELECT symbol FROM uniswap_v2_pairs WHERE pair_id = '{pair_id}' LIMIT 1;"
