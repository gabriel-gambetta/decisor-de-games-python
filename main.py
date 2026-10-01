import games, user

jogos_teste = [

    games.Game(
        'Baldur\'s Gate 3',
        'Primário',
        ['Adventure', 'RPG', 'Strategy'],
        [
            'RPG', 'Character Customization', 'Choices Matter',
            'Turn-Based Combat', 'Story Rich', 'Sexual Content',
            'CRPG', 'Fantasy', 'Adventure', 'Romance',
            'Online Co-Op', 'Multiplayer', 'Nudity', 'Strategy',
            'Singleplayer', 'Co-op Campaign', 'Class-Based',
            'Dark Fantasy', 'Combat', 'LGBTQ+'
        ]
    ),

    games.Game(
        'Total War: WARHAMMER III',
        'Secundário',
        ['Action', 'Strategy'],
        [
            'Strategy', 'Turn-Based Strategy', 'Grand Strategy',
            'RTS', 'Fantasy', 'Real Time Tactics', 'War',
            'Dark Fantasy', 'Dwarves', 'Action', 'Tactical',
            'Multiplayer', 'Atmospheric', 'Co-op', 'Colorful',
            'PvP', 'Singleplayer', 'Online Co-Op',
            'Story Rich', 'Tower Defense'
        ]
    ),

    games.Game(
        'Warhammer 40,000: Rogue Trader',
        None,
        ['Action', 'Adventure', 'Indie', 'RPG', 'Strategy'],
        [
            'RPG', 'Choices Matter', 'CRPG', 'Character Customization',
            'Turn-Based Strategy', 'Turn-Based Combat', 'Strategy',
            'Co-op', 'Tactical RPG', 'Adventure', 'Atmospheric',
            'Fantasy', 'Dark Fantasy', 'Action', 'Multiplayer',
            'Story Rich', 'Sci-fi', 'Singleplayer', 'Space', 'Romance'
        ]
    ),

    games.Game(
        'Dragon Age™: The Veilguard',
        'Primário',
        ['Action', 'RPG'],
        [
            'LGBTQ+', 'Fantasy', 'Singleplayer', 'RPG', 'Action RPG',
            'Strategy', 'CRPG', 'Turn-Based', 'Tactics',
            'Character Customization', 'Third Person', 'Action',
            'Romance', 'Adventure', 'Dragons', 'Magic', 'Story Rich',
            'Multiple Endings', 'Lore-Rich', 'Choices Matter',
            'Psychological Horror'
        ]
    ),

    games.Game(
        'Kingdom Come: Deliverance II',
        None,
        ['Action', 'Adventure', 'RPG'],
        [
            'RPG', 'Medieval', 'Open World', 'Singleplayer',
            'Story Rich', 'First-Person', 'Realistic', 'Adventure',
            'Action', 'Historical', 'Swordplay', 'Combat',
            'Immersive', 'Choices Matter', 'Atmospheric',
            'Alternate History', 'Action-Adventure', '3D',
            'LGBTQ+', 'Sexual Content'
        ]
    ),

    games.Game(
        'Mount & Blade II: Bannerlord',
        'Secundário',
        ['Action', 'Indie', 'RPG', 'Simulation', 'Strategy'],
        [
            'Medieval', 'Strategy', 'Open World', 'RPG', 'War',
            'Multiplayer', 'Sandbox', 'Singleplayer', 'Action',
            'Character Customization', 'Simulation', 'Moddable',
            'Adventure', 'Horses', 'Realistic', 'Third Person',
            'Historical', 'First-Person', 'Great Soundtrack',
            'Early Access'
        ]
    ),

    games.Game(
        'XCOM® 2',
        'Primário',
        ['Strategy'],
        [
            'Strategy', 'Turn-Based Combat', 'Tactical',
            'Character Customization', 'RPG', 'Singleplayer',
            'Turn-Based Tactics', 'Sci-fi', 'War', 'Military',
            'PvE', 'Isometric', 'Post-apocalyptic', 'Perma Death',
            'Turn-Based Strategy', 'Turn-Based', 'Alternate History',
            'Grid-Based Movement', 'Top-Down', 'Logic'
        ]
    ),

    games.Game(
        'Sid Meier’s Civilization® VI',
        'Secundário',
        ['Strategy'],
        [
            'Strategy', 'Turn-Based Strategy', 'Multiplayer',
            'Historical', 'Grand Strategy', 'Singleplayer',
            'Turn-Based', '4X', 'City Builder', 'War', 'Simulation',
            'Tactical', 'Management', 'Building', 'Online Co-Op',
            'Moddable', 'Great Soundtrack', 'Co-op', 'Hex Grid',
            'Atmospheric'
        ]
    ),

    games.Game(
        'Hearts of Iron IV',
        None,
        ['Simulation', 'Strategy'],
        [
            'Strategy', 'World War II', 'Grand Strategy', 'War',
            'Historical', 'Military', 'Alternate History',
            'Multiplayer', 'Simulation', 'Tactical', 'Singleplayer',
            'RTS', 'Real-Time with Pause', 'Diplomacy', 'Sandbox',
            'Co-op', 'Strategy RPG', 'Open World', 'Competitive',
            'Action'
        ]
    ),

    games.Game(
        'Europa Universalis IV',
        'Primário',
        ['Simulation', 'Strategy'],
        [
            'Grand Strategy', 'Strategy', 'Historical', 'Simulation',
            '4X', 'Alternate History', 'Wargame', 'Military',
            'Diplomacy', 'Economy', 'Replay Value', 'Sandbox',
            'Real-Time with Pause', 'Moddable', 'Nonlinear',
            'Co-op', 'Singleplayer', 'Management', 'Multiplayer',
            'War'
        ]
    ),

    games.Game(
        'Stellaris',
        'Secundário',
        ['Simulation', 'Strategy'],
        [
            'Space', 'Strategy', 'Grand Strategy', 'Sci-fi', '4X',
            'Exploration', 'Sandbox', 'Simulation', 'Multiplayer',
            'Real-Time with Pause', 'Singleplayer', 'Moddable',
            'Management', 'Diplomacy', 'Military', 'Futuristic',
            'Replay Value', 'Great Soundtrack',
            'Procedural Generation', 'Atmospheric'
        ]
    ),

    games.Game(
        'Crusader Kings III',
        None,
        ['Simulation', 'Strategy'],
        [
            'Strategy', 'Medieval', 'Grand Strategy', 'Simulation',
            'RPG', 'Historical', 'Management', 'Character Customization',
            'Life Sim', 'Sandbox', 'Choices Matter', 'RTS', 'War',
            'Singleplayer', 'Economy', 'Multiplayer', 'Moddable',
            '4X', 'Real-Time with Pause', 'Sexual Content'
        ]
    ),

    games.Game(
        'Red Dead Redemption 2',
        'Primário',
        ['Action', 'Adventure'],
        [
            'Open World', 'Story Rich', 'Western', 'Multiplayer',
            'Adventure', 'Action', 'Realistic', 'Singleplayer',
            'Shooter', 'Horses', 'Beautiful', 'Atmospheric',
            'Third-Person Shooter', 'Great Soundtrack', 'Third Person',
            'Gore', 'Sandbox', 'First-Person', 'FPS', 'Sexual Content'
        ]
    ),

    games.Game(
        'Starfield',
        None,
        ['RPG'],
        [
            'Space', 'Open World', 'Singleplayer', 'RPG', 'Sci-fi',
            'Exploration', 'Character Customization', 'First-Person',
            'Story Rich', 'Action-Adventure', 'Third Person',
            'Adventure', 'Action RPG', 'Space Sim', 'Atmospheric',
            'Moddable', 'Action', 'Cinematic', 'Realistic',
            'Great Soundtrack'
        ]
    ),

    games.Game(
        'Hades',
        'Secundário',
        ['Action', 'Indie', 'RPG'],
        [
            'Action', 'Roguelike', 'Roguelite', 'Hack and Slash',
            'Indie', 'Mythology', 'Action Roguelike', 'Singleplayer',
            'Great Soundtrack', 'Story Rich', 'Dungeon Crawler',
            'RPG', 'Replay Value', 'Isometric', 'Difficult',
            'Hand-drawn', 'Action RPG', 'Atmospheric', 'LGBTQ+',
            'Perma Death'
        ]
    ),

    games.Game(
        'Hollow Knight',
        'Primário',
        ['Action', 'Adventure', 'Indie'],
        [
            'Metroidvania', 'Platformer', 'Souls-like', 'Difficult',
            'Great Soundtrack', '2D', 'Indie', 'Singleplayer',
            'Exploration', 'Atmospheric', 'Adventure', 'Story Rich',
            'Hand-drawn', 'Multiple Endings', 'Action',
            'Dark Fantasy', 'Open World', 'Cute', 'Controller',
            'Side Scroller'
        ]
    ),

    games.Game(
        'Portal 2',
        None,
        ['Action', 'Adventure'],
        [
            'Singleplayer', 'Platformer', 'Puzzle', 'First-Person',
            'Dark Humor', 'Story Rich', 'Puzzle Platformer', 'Funny',
            'Female Protagonist', '3D Platformer', 'Co-op',
            'Action-Adventure', 'Action', 'FPS', 'Physics', 'Sci-fi',
            'Level Editor', 'Science', 'Comedy', 'Atmospheric'
        ]
    ),

    games.Game(
        'Stardew Valley',
        'Secundário',
        ['Indie', 'RPG', 'Simulation'],
        [
            'Farming Sim', 'Pixel Graphics', 'Multiplayer', 'Life Sim',
            'RPG', 'Relaxing', 'Simulation', 'Agriculture', 'Crafting',
            'Sandbox', 'Indie', 'Building', 'Open World', 'Casual',
            'Singleplayer', '2D', 'Dating Sim', 'Cute',
            'Great Soundtrack', 'Fishing'
        ]
    ),

    games.Game(
        'Project Zomboid',
        'Primário',
        ['Indie', 'RPG', 'Simulation', 'Early Access'],
        [
            'Survival', 'Zombies', 'Open World', 'Multiplayer',
            'Open World Survival Craft', 'Sandbox', 'Crafting',
            'Building', 'Indie', 'Simulation', 'RPG', 'Survival Horror',
            'Realistic', 'Isometric', 'Singleplayer', '2D',
            'Adventure', 'Early Access'
        ]
    ),

    games.Game(
        'Rust',
        None,
        ['Action', 'Adventure', 'Indie', 'Massively Multiplayer', 'RPG'],
        [
            'Survival', 'Crafting', 'Multiplayer', 'Open World',
            'Open World Survival Craft', 'Building', 'PvP', 'Sandbox',
            'Adventure', 'First-Person', 'Nudity', 'Action', 'FPS',
            'Shooter', 'Co-op', 'Online Co-Op', 'Indie',
            'Post-apocalyptic', 'Early Access', 'Simulation'
        ]
    ),

    games.Game(
        'Satisfactory',
        'Secundário',
        ['Adventure', 'Indie', 'Simulation', 'Strategy'],
        [
            'Base Building', 'Automation', 'Open World', 'Crafting',
            'Multiplayer', 'Co-op', 'Building', 'Resource Management',
            'Sandbox', 'Exploration', 'Open World Survival Craft',
            'Adventure', 'Survival', 'First-Person', 'Simulation',
            'Strategy', 'Sci-fi', 'Singleplayer', 'Indie',
            'Early Access'
        ]
    ),

    games.Game(
        'Warframe',
        'Primário',
        ['Action', 'RPG', 'Free To Play'],
        [
            'Free to Play', 'Looter Shooter', 'Action RPG',
            'Third-Person Shooter', 'Action', 'RPG', 'Third Person',
            'Massively Multiplayer', 'Online Co-Op',
            'Character Customization', 'Co-op', 'PvE', 'Sci-fi',
            'Singleplayer', 'Space', 'Lore-Rich', 'Shooter',
            'Hack and Slash', 'Parkour', 'Ninja'
        ]
    ),

    games.Game(
        'Counter-Strike 2',
        None,
        ['Action', 'Free To Play'],
        [
            'FPS', 'Shooter', 'Multiplayer', 'Competitive', 'Action',
            'Team-Based', 'eSports', 'Tactical', 'First-Person', 'PvP',
            'Online Co-Op', 'Co-op', 'Strategy', 'Military', 'War',
            'Trading', 'Difficult', 'Realistic', 'Fast-Paced',
            'Moddable'
        ]
    ),

    games.Game(
        'Half-Life',
        'Secundário',
        ['Action'],
        [
            'FPS', 'Classic', '1990\'s', 'Sci-fi', 'Singleplayer',
            'Multiplayer', 'Shooter', 'Action', 'First-Person',
            'Aliens', 'Silent Protagonist', 'Story Rich', 'Atmospheric',
            'Gore', 'Retro', 'Moddable', 'Adventure',
            'Action-Adventure', 'Difficult', 'PvP'
        ]
    ),
]


gabriel_teste = user.Usuário(
    [
        'RPG',
        'Strategy',
        'Action'
    ],
    [
        'Character Customization',
        'War',
        'Military',
        'Open World',
        'Story Rich',
        'Fantasy',
        'Singleplayer'
    ]
)


print(games.decidir_game(jogos_teste, gabriel_teste))
