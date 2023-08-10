class Adventure:

    def __init__(self, name, tagline, blurb, description, link, pictures, tier):
        self.name = name
        self.tagline = tagline 
        self.blurb = blurb
        self.description = description
        self.link = link
        self.pictures = pictures
        self.tier = tier

    def __str__(self):
        return self.name
    

adventures = {
    'red_wizards_of_thay': Adventure('Red Wizards of Thay',
                                        'As seen in Dungeons & Dragons: Honor Amongst Thieves!',
                                        'Infiltrate the ranks of the Red Wizards, uncover their dark secrets, and stop their schemes in this magical adventure of intrigue.',
                                        'The Red Wizards of Thay are a powerful cabal of wizards who have been plotting to take over the Sword Coast for centuries. Now, they have finally found a way to do it. They have discovered a way to create a powerful magical item that will allow them to control the minds of the people of the Sword Coast. They have sent a team of spies to the Sword Coast to gather information about the item and to find a way to get it. You have been hired to infiltrate the Red Wizards and stop them before they can complete their plans.',
                                        'https://outschool.com/classes/dungeons-and-dragons-red-wizards-of-thay-or-as-seen-in-the-new-dandd-movie-nxFS5Fv8?usid=z05zHVoS&signup=true&utm_campaign=share_activity_link'
                                        'rwot',
                                        3),
    'tomb_of_annihilation': Adventure('Tomb of Annihilation',
                                        'Discover the Deadly Secrets of the Lost City!',
                                        'Explore the treacherous jungles of Chult, overcome lethal traps, and solve the mystery of the Soulmonger in this thrilling adventure.',
                                        'The Tomb of the Nine Gods is a tomb that was built by the ancient Chultan civilization. It is located in the jungles of Chult, and it is said to contain the remains of the Nine Gods. The tomb is protected by a powerful magical barrier that prevents anyone from entering. The cult of the Reptile God has discovered a way to break the barrier and enter the tomb. They have sent a team of spies to Chult to gather information about the tomb and to find a way to break the barrier. You have been hired to infiltrate the cult and stop them before they can complete their plans.',
                                        'https://outschool.com/classes/dungeons-and-dragons-tomb-of-annihilation-or-jungle-dinosaur-adventure-10cP1Aiq?usid=z05zHVoS&signup=true&utm_campaign=share_activity_link'
                                        'toa',
                                        2),
    'ghosts_of_saltmarsh': Adventure('Ghosts of Saltmarsh',
                                        'Uncover the Mysteries of the Haunted Coast!',
                                        'Brave the shores of Saltmarsh, confront terrifying monsters, and navigate coastal politics in this chilling, nautical adventure.',
                                        "Along the haunted coast of Saltmarsh, strange occurrences and ancient secrets abound. Called upon to investigate these mysteries, you and your fellow adventurers must brave the treacherous shores, navigate the dangerous politics of the coastal town, and face terrifying monsters from the deep. As you delve deeper into the shadows, you'll uncover a sinister plot that threatens the entire region. In this chilling nautical adventure, only your courage and wits can save the day and bring peace to the beleaguered coast.",
                                        'https://outschool.com/classes/dungeons-and-dragons-ghosts-of-saltmarsh-beginner-pirate-sea-adventure-srGx42LE?usid=z05zHVoS&signup=true&utm_campaign=share_activity_link'
                                        'gos',
                                        2),
    'waterdeep_dragon_heist': Adventure('Waterdeep: Dragon Heist',
                                        'Find Treasure in the City of Splendors!',
                                        'Dive into the treacherous politics and factions of Waterdeep to discover the secret of the Dragon Heist and claim your fortune.',
                                        "In the bustling City of Splendors, the legendary Dragon Heist offers the promise of untold riches and power. Amidst the treacherous politics and factions of Waterdeep, you and your fellow adventurers must uncover the secret behind the hoard, outwit your rivals, and claim your fortune. As you delve into the city's underbelly, you'll encounter dangerous foes, forge unlikely alliances, and unravel a mystery that reaches to the highest echelons of power. Will you seize the opportunity to change your destiny, or will you fall victim to the machinations of Waterdeep's shadowy denizens?",
                                        'https://outschool.com/classes/dungeons-and-dragons-waterdeep-dragon-heist-beginner-fantasy-campaign-KDkVZ3l2?usid=z05zHVoS&signup=true&utm_campaign=share_activity_link'
                                        'wdh',
                                        1),
    'lost_mine_of_phandelver': Adventure('Lost Mine of Phandelver',
                                        'Unearth the Secrets of the Forgotten Mine!',
                                        'Embark on a perilous journey to uncover the location of the legendary Lost Mine of Phandelver, battle fearsome foes, and unlock hidden treasures in this classic adventure.',
                                        "The fabled Lost Mine of Phandelver, once a prosperous source of precious ores, has been hidden for centuries, its location lost to time. Now, whispers of the mine's rediscovery have sparked a thrilling race to uncover its secrets. As brave adventurers, you must journey through treacherous lands, overcome formidable foes, and piece together the clues that will lead you to the lost mine. Along the way, you'll unravel a sinister plot that threatens the very fabric of the realm. Can you unlock the hidden treasures of Phandelver before it's too late?",
                                        'https://outschool.com/classes/dungeons-and-dragons-lost-mine-of-phandelver-beginner-starter-adventure-i3wfid6L?usid=z05zHVoS&signup=true&utm_campaign=share_activity_link'
                                        'lmop',
                                        1),
    'Wild Beyond the Witchlight': Adventure('Wild Beyond the Witchlight',Enter the Enchanted Carnival and Discover a Hidden World!
                                        'Enter the Enchanted Carnival and Discover a Hidden World!',
                                        'Step into the magical realm of the Feywild, navigate through the mysterious Witchlight Carnival, and unravel the secrets of a lost domain in this whimsical and enchanting adventure.',
                                        "The Witchlight Carnival, a wondrous and enchanted event, serves as a gateway to the magical realm of the Feywild. As intrepid adventurers, you are drawn to the carnival's myriad attractions and soon find yourselves embroiled in a fantastical journey through a lost domain. Along the way, you'll encounter whimsical creatures, solve riddles, and navigate the ever-changing landscape of the Feywild, all while uncovering a hidden truth that could alter the very nature of reality. In this enchanting and whimsical adventure, your wits, courage, and heart will be put to the test as you strive to unravel the secrets of the Wild Beyond the Witchlight.",
                                        'https://outschool.com/classes/dungeons-and-dragons-the-wild-beyond-a-magical-campaign-for-beginners-Dj7Mm6Qx?usid=z05zHVoS&signup=true&utm_campaign=share_activity_link'
                                        'wbtw',
                                        1)
}

