from vpython import *
import numpy as np
import random

Sun = sphere(radius=8, color=vector(1, 0.6, 0), pos=vector(0, 0, 0), emissive=True)
sun_light = local_light(pos=vector(0, 0, 0), color=vector(1, 0.9, 0.6))
label(pos=vector(0, 0, 0), text='Sun', height=16, border=0.1, font='sans')

def create_planet(name, radius, color, a, b, trail_radius=0.1, texture=None):
    planet = sphere(radius=radius, color=color, pos=vector(a, 0, 0),
                    make_trail=True, trail_type="points", trail_radius=trail_radius, texture=texture)
    label_obj = label(text=name, color=color, linecolor=color, pos=vector(0, 0, 0),
                      xoffset=20, yoffset=50, space=30,
                      height=16, border=0.1, linewidth=0.8, font='monospace')
    return {
        'object': planet,
        'label': label_obj,
        'a': a,
        'b': b,
        'theta': 0,
        'speed': 0.05 / a  
    }

planets = [
    create_planet("Mercury\nSpeed: 47.87 km/s", 1, vector(0.5, 0.5, 0.5), 12, 10, texture=textures.rock),
    create_planet("Venus\nSpeed: 35.02 km/s", 1.5, vector(0.6, 0.2, 0.3), 18, 16, texture=textures.wood),
    create_planet("Earth\nSpeed:  29.78 km/s", 2, vector(0.1, 0.3, 0.7), 24, 22, texture=textures.earth),
    create_planet("Mars\nSpeed:  24.07 km/s", 1.5, vector(0.7, 0.2, 0.1), 30, 28, texture=textures.rock),
    create_planet("Jupiter\nSpeed: 13.07 km/s", 4, vector(0.7, 0.5, 0.2), 40, 38, texture=textures.granite),
    create_planet("Saturn\nSpeed: 9.69 km/s", 3.5, vector(0.5, 0.5, 0.9), 50, 48, texture=textures.rough),
    create_planet("Uranus\nSpeed: 6.81 km/s", 2.9, vector(0.2, 0.7, 0.8), 60, 58, texture=textures.gravel),
    create_planet("Neptune\nSpeed: 5.43 km/s", 2.8, vector(0.3, 0.3, 0.9), 70, 68, texture=textures.metal),
    create_planet("Pluto\nSpeed: 4.67 km/s", 1, vector(0.9, 0.9, 0.8), 80, 78, texture=textures.stones)
]

saturn_ring = ring(pos=planets[5]['object'].pos, axis=vector(0, 1, 0), radius=4.5, thickness=0.2, color=vector(0.8, 0.8, 0.6))

planetary_details = {
    "Mercury": {
        "info": "Smallest Planet: Mercury is the smallest planet in the solar system and the closest one to the Sun. \nExtreme Temperatures: Daytime temperatures can exceed 400°C (750°F), while nighttime temperatures drop to -180°C (-290°F) due to the lack of an atmosphere. \nNo Moons or Rings: Mercury has no moons and no ring system. \nShort Year: It completes one orbit around the Sun in just 88 Earth days, making its year very short. \nCraters Everywhere: Mercury’s surface is heavily cratered, resembling the Moon's surface. \nHard to Observe: Its small size and proximity to the Sun make it difficult to see from Earth without a telescope. \nSolar Wind Effects: Mercury doesn’t have weather, but solar winds constantly strike its surface, blowing away particles. \nUninhabitable: Despite being a rocky planet, its extreme temperatures, lack of atmosphere, and absence of breathable air make it impossible for humans to live there. \n",
        "image": ["mercury.jpg","mercury1.jpg","mercury2.jpg"],
        "quiz": [
            {"question": "What is the size of Mercury?", "options": ["Small", "Medium", "Large", "Very large"], "answer": "Small"},
            {"question": "How long is a year on Mercury?", "options": ["88 days", "365 days", "2 years", "1 year"], "answer": "88 days"},
            {"question": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"},
            {"question": "What is the surface temperature of Mercury?", "options": ["Very hot", "Very cold", "Moderate", "Freezing"], "answer": "Very hot"},
            {"question": "How many moons does Mercury have?", "options": ["0", "1", "2", "3"], "answer": "0"},
            {"question": "What is Mercury's primary atmosphere made of?", "options": ["Oxygen", "Carbon Dioxide", "No atmosphere", "Nitrogen"], "answer": "No atmosphere"},
            {"question": "Which planet has no moons and no rings?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"},
            {"question": "How long does it take Mercury to complete one rotation?", "options": ["59 Earth days", "24 hours", "365 days", "30 Earth days"], "answer": "59 Earth days"},
            {"question": "What is Mercury’s most notable feature?", "options": ["Craters", "Rings", "Water", "Mountains"], "answer": "Craters"},
            {"question": "What makes Mercury hard to see from Earth?", "options": ["Its size", "Its distance", "Its lack of atmosphere", "Its brightness"], "answer": "Its lack of atmosphere"}
        ]
    },
    "Venus": {
        "info": "Earth's Twin: Venus is similar in size and composition to Earth but has vastly different conditions. \nBright Appearance: Known as the Morning Star or Evening Star, Venus shines brilliantly in the sky. \nExtreme Heat: Its thick carbon dioxide atmosphere creates a runaway greenhouse effect, making it the hottest planet, with surface temperatures around 475°C (900°F). \nCrushing Pressure: The surface pressure is over 90 times that of Earth’s, equivalent to being 900 meters underwater. \nSlow Rotation: Venus takes 243 Earth days to rotate once, longer than its 225-day orbit around the Sun. \nRetrograde Spin: Venus rotates backward compared to most planets, causing the Sun to rise in the west and set in the east. \nGeological Features: The surface includes vast plains, volcanoes, and lava flows but no liquid water due to extreme heat. \nScientific Exploration: Missions like Magellan and Venus Express have studied its geology and atmosphere, suggesting potential past habitability. \n",
        "image": ["venus.jpg","venus1.jpg","venus2.jpg"],
        "quiz": [
            {"question": "Venus is the second planet from the Sun. True or False?", "options": ["True", "False"], "answer": "True"},
            {"question": "What is the main component of Venus's atmosphere?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"question": "Which planet is called Earth's twin?", "options": ["Mars", "Venus", "Saturn", "Jupiter"], "answer": "Venus"},
            {"question": "How many moons does Venus have?", "options": ["0", "1", "2", "3"], "answer": "0"},
            {"question": "What is the average temperature on Venus?", "options": ["350°C", "100°C", "500°C", "25°C"], "answer": "500°C"},
            {"question": "What is the surface of Venus mostly made of?", "options": ["Rock", "Clouds", "Water", "Ice"], "answer": "Rock"},
            {"question": "Which planet has the hottest surface temperature?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Venus"},
            {"question": "What is the name of Venus' brightest feature?", "options": ["The Great Red Spot", "The Evening Star", "The Ring", "The Dust Storm"], "answer": "The Evening Star"},
            {"question": "Which of these planets rotates in the opposite direction to most other planets?", "options": ["Venus", "Earth", "Jupiter", "Saturn"], "answer": "Venus"},
            {"question": "Venus has a thick atmosphere made up mostly of which gas?", "options": ["Carbon Dioxide", "Methane", "Nitrogen", "Oxygen"], "answer": "Carbon Dioxide"}
        ]
    },
    "Earth": {
        "info": "Life-Supporting Planet: Earth is the only known planet to support life, thanks to its liquid water, breathable atmosphere, and moderate climate. \nUnique Atmosphere: Its atmosphere, rich in nitrogen (78%) and oxygen (21%), protects life from harmful radiation and regulates temperature. \nSurface Composition: Around 71% of Earth's surface is covered by water, earning it the nickname Blue Planet. \nPlate Tectonics: Earth's crust is divided into tectonic plates that move, causing earthquakes, volcanic activity, and shaping landscapes. \nDistance from the Sun: Positioned at an average of 93 million miles (150 million km) from the Sun, it resides in the Goldilocks Zone, ideal for life. \nDynamic Seasons: Earth's axial tilt (23.5°) causes seasonal changes as it orbits the Sun over 365.25 days. \nNatural Satellite: The Moon stabilizes Earth's axial tilt and affects tides, playing a crucial role in Earth's ecosystem. \nDiverse Ecosystems: Earth boasts a wide range of environments, from deserts to rainforests, supporting millions of species. \n",
        "image": ["earth.jpg","earth1.jpg","earth2.jpg"],
        "quiz": [
            {"question": "What percentage of Earth's surface is covered by water?", "options": ["70%", "50%", "30%", "90%"], "answer": "70%"},
            {"question": "Which is the largest continent on Earth?", "options": ["Asia", "Africa", "Europe", "Antarctica"], "answer": "Asia"},
            {"question": "What is Earth's atmosphere made mostly of?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Nitrogen"},
            {"question": "How long does it take for Earth to complete one orbit around the Sun?", "options": ["365 days", "1 year", "24 hours", "30 days"], "answer": "365 days"},
            {"question": "How many moons does Earth have?", "options": ["1", "2", "3", "None"], "answer": "1"},
            {"question": "Which layer of the Earth is the hottest?", "options": ["Core", "Mantle", "Crust", "Lithosphere"], "answer": "Core"},
            {"question": "Which element is most abundant in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": "Nitrogen"},
            {"question": "What is the average temperature of Earth?", "options": ["15°C", "30°C", "0°C", "25°C"], "answer": "15°C"},
            {"question": "Earth's magnetic field is created by what?", "options": ["Earth's atmosphere", "Earth's core", "The Sun", "The Moon"], "answer": "Earth's core"},
            {"question": "Which type of rock is most abundant on Earth?", "options": ["Sedimentary", "Metamorphic", "Igneous", "None"], "answer": "Igneous"}
        ]
    },
    "Mars": {
        "info": "The Red Planet: Mars gets its nickname from its reddish appearance, caused by iron oxide (rust) on its surface. \nSmaller and Colder: Mars is about half the size of Earth, with surface temperatures ranging from -140°C to 20°C (-220°F to 70°F). \nThin Atmosphere: Composed mostly of carbon dioxide, the atmosphere is 100 times thinner than Earth’s, making it unable to support liquid water on the surface. \nDust Storms: Mars experiences massive dust storms that can envelop the entire planet, lasting for weeks. \nPotential for Life: Evidence of ancient river valleys, lake beds, and water ice suggests that Mars may have had conditions suitable for life in the past. \nTwo Small Moons: Mars has two irregularly shaped moons, Phobos and Deimos, believed to be captured asteroids. \nOlympus Mons: It is home to Olympus Mons, the tallest volcano in the solar system, standing about 22 km (13.6 miles) high. \nExploration Efforts: Robotic missions like NASA’s Perseverance and Curiosity rovers, along with orbiters, continue to study Mars' geology, climate, and potential for future human colonization. \n",
        "image": ["mars.jpg","mars1.jpg","mars2.jpg"],
        "quiz": [
            {"question": "What is the color of Mars?", "options": ["Red", "Blue", "Green", "White"], "answer": "Red"},
            {"question": "Which is the largest volcano in the solar system?", "options": ["Olympus Mons", "Mount Everest", "Kilimanjaro", "Mount Fuji"], "answer": "Olympus Mons"},
            {"question": "Mars has two moons. True or False?", "options": ["True", "False"], "answer": "True"},
            {"question": "What is the primary element that makes Mars appear red?", "options": ["Oxygen", "Carbon", "Iron oxide", "Sulfur"], "answer": "Iron oxide"},
            {"question": "What was discovered beneath the surface of Mars?", "options": ["Water", "Diamonds", "Oil", "Gold"], "answer": "Water"},
            {"question": "How many days does it take Mars to complete one rotation?", "options": ["24 hours", "687 days", "687 hours", "24.6 hours"], "answer": "24.6 hours"},
            {"question": "Which NASA rover landed on Mars in 2021?", "options": ["Curiosity", "Perseverance", "Spirit", "Opportunity"], "answer": "Perseverance"},
            {"question": "What gas is abundant in Mars's thin atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"question": "What kind of landscape is common on Mars?", "options": ["Desert", "Tropical rainforest", "Ocean", "Mountains"], "answer": "Desert"},
            {"question": "Mars is known as the Red Planet due to which mineral?", "options": ["Iron oxide", "Copper", "Magnesium", "Calcium"], "answer": "Iron oxide"}
        ]
    },
    "Jupiter": {
        "info": "Largest Planet: Jupiter is the biggest planet in the solar system, with a diameter 11 times that of Earth and a mass more than 300 times greater. \nGas Giant: Composed mostly of hydrogen and helium, Jupiter lacks a solid surface, with its atmosphere transitioning into a dense liquid interior. \nGreat Red Spot: A massive storm larger than Earth has been raging for at least 300 years, making it a defining feature of Jupiter. \nPowerful Magnetic Field: Jupiter’s magnetic field is the strongest in the solar system, 20,000 times more powerful than Earth's. \nFast Rotation: Despite its size, Jupiter has the shortest day of any planet, completing one rotation in just under 10 hours. \nNumerous Moons: Jupiter has at least 92 moons, including the four largest—Io, Europa, Ganymede, and Callisto—known as the Galilean moons. \nEuropa’s Potential: Europa, one of its moons, is a prime candidate for extraterrestrial life due to its subsurface ocean beneath an icy crust. \nExploration Missions: Spacecraft like Juno and Galileo have provided valuable data on Jupiter’s atmosphere, magnetic field, and moons. \n",
        "image": ["jupiter.jpg","jupiter1.jpg","jupiter2.jpg"],
        "quiz": [
            {"question": "What is the largest planet in the solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
            {"question": "What is Jupiter's famous storm called?", "options": ["The Great Red Spot", "The Big White Spot", "The Black Hole", "The Blue Storm"], "answer": "The Great Red Spot"},
            {"question": "How many moons does Jupiter have?", "options": ["50", "30", "79", "10"], "answer": "79"},
            {"question": "What is the primary gas in Jupiter's atmosphere?", "options": ["Oxygen", "Hydrogen", "Helium", "Nitrogen"], "answer": "Hydrogen"},
            {"question": "How many rings does Jupiter have?", "options": ["1", "2", "3", "None"], "answer": "None"},
            {"question": "What is Jupiter's diameter?", "options": ["139,822 km", "50,000 km", "100,000 km", "80,000 km"], "answer": "139,822 km"},
            {"question": "Jupiter's magnetic field is how many times stronger than Earth's?", "options": ["2 times", "20 times", "10 times", "100 times"], "answer": "20 times"},
            {"question": "What is Jupiter's main source of energy?", "options": ["The Sun", "Internal heat", "Electricity", "Wind"], "answer": "Internal heat"},
            {"question": "Which spacecraft visited Jupiter in 2016?", "options": ["Cassini", "Juno", "Voyager", "Parker"], "answer": "Juno"},
            {"question": "What is the largest moon of Jupiter?", "options": ["Ganymede", "Europa", "Io", "Callisto"], "answer": "Ganymede"}
        ]
    },
    "Saturn": {
        "info": "The Ringed Planet: Saturn is renowned for its stunning ring system, made of ice, rock, and dust particles. \nGas Giant: Like Jupiter, Saturn is mostly hydrogen and helium, with no solid surface. \nSize and Mass: It is the second-largest planet in the solar system, about 9.5 times Earth's diameter, but much less dense—so light it would float in water. \nComplex Ring System: Saturn's rings are divided into several distinct sections, with the main rings spanning up to 175,000 miles (282,000 km) in diameter. \nMany Moons: Saturn has at least 145 moons, including Titan, the second-largest moon in the solar system and the only one with a thick atmosphere. \nTitan's Potential: Titan is of particular interest because its lakes and rivers of liquid methane and ethane could harbor exotic forms of life. \nFast Rotation: Saturn completes a day in about 10.7 hours, leading to its oblate shape (flattened at the poles). \nExploration Missions: The Cassini-Huygens mission provided unprecedented insights into Saturn's rings, atmosphere, and moons, especially Titan and Enceladus. \n",
        "image": ["saturn.jpg","saturn1.jpg","saturn2.jpg"],
        "quiz": [
            {"question": "What planet is famous for its rings?", "options": ["Jupiter", "Saturn", "Mars", "Uranus"], "answer": "Saturn"},
            {"question": "What is the composition of Saturn's rings?", "options": ["Ice and rock", "Gas", "Dust", "Molten metal"], "answer": "Ice and rock"},
            {"question": "How many moons does Saturn have?", "options": ["82", "50", "30", "10"], "answer": "82"},
            {"question": "What is Saturn's most well-known moon?", "options": ["Titan", "Europa", "Ganymede", "Io"], "answer": "Titan"},
            {"question": "What is Saturn's primary atmosphere made of?", "options": ["Hydrogen", "Oxygen", "Carbon Dioxide", "Methane"], "answer": "Hydrogen"},
            {"question": "How long is a day on Saturn?", "options": ["10 hours", "24 hours", "12 hours", "30 hours"], "answer": "10 hours"},
            {"question": "What is the name of the spacecraft that explored Saturn's rings?", "options": ["Cassini", "Voyager", "Parker", "New Horizons"], "answer": "Cassini"},
            {"question": "Which planet has the most moons in the solar system?", "options": ["Saturn", "Jupiter", "Mars", "Uranus"], "answer": "Saturn"},
            {"question": "Saturn is the _ largest planet in the solar system?", "options": ["1st", "2nd", "3rd", "4th"], "answer": "2nd"},
            {"question": "Saturn's rings are primarily made of what?", "options": ["Rock", "Ice", "Gas", "Dust"], "answer": "Ice"}
        ]
    },
    "Uranus": {
        "info": "Ice Giant: Uranus is classified as an ice giant, composed of hydrogen, helium, and significant amounts of water, ammonia, and methane, which give it a pale blue color. \nTilted Axis: Uranus rotates on its side, with an axial tilt of 98 degrees, leading to extreme seasons that last over 20 Earth years each. \nColdest Planet: Despite being farther from the Sun, Neptune is warmer; Uranus holds the title of the coldest planet, with temperatures dropping to -224°C (-371°F). \nFaint Rings: Uranus has a system of faint, dark rings composed mostly of ice and rock particles. \nMany Moons: Uranus has 27 known moons, named after characters from Shakespearean and Alexander Pope's works, such as Titania, Oberon, and Miranda. \nSlow Orbit: It takes Uranus 84 Earth years to complete one orbit around the Sun. \nAtmospheric Composition: The methane in its atmosphere absorbs red light, giving the planet its bluish hue. \nLimited Exploration: Uranus has only been visited once, by NASA’s Voyager 2 in 1986, which provided valuable data about its atmosphere, moons, and rings. \n",
        "image": ["uranus.jpg","uranus1.jpg","uranus2.png"],
        "quiz": [
            {"question": "Which planet rotates on its side?", "options": ["Earth", "Venus", "Uranus", "Mars"], "answer": "Uranus"},
            {"question": "What is Uranus primarily composed of?", "options": ["Iron", "Water", "Gas", "Ice and gas"], "answer": "Ice and gas"},
            {"question": "What is the tilt of Uranus' axis?", "options": ["98 degrees", "90 degrees", "180 degrees", "45 degrees"], "answer": "98 degrees"},
            {"question": "What color is Uranus due to the methane in its atmosphere?", "options": ["Blue", "Green", "Yellow", "Red"], "answer": "Blue"},
            {"question": "How many moons does Uranus have?", "options": ["13", "27", "60", "5"], "answer": "27"},
            {"question": "Which of these planets is known for its extreme tilt?", "options": ["Uranus", "Saturn", "Neptune", "Jupiter"], "answer": "Uranus"},
            {"question": "What is Uranus's primary atmosphere composed of?", "options": ["Nitrogen", "Hydrogen", "Methane", "Oxygen"], "answer": "Methane"},
            {"question": "Uranus is the _ largest planet in the solar system?", "options": ["2nd", "3rd", "4th", "7th"], "answer": "3rd"},
            {"question": "Uranus has a total of how many rings?", "options": ["13", "1", "11", "3"], "answer": "13"},
            {"question": "What year did Voyager 2 fly by Uranus?", "options": ["1986", "2000", "1997", "1979"], "answer": "1986"}
        ]
    },
    "Neptune": {
        "info": "Farthest Planet: Neptune is the eighth and farthest planet from the Sun, located about 4.5 billion kilometers (2.8 billion miles) away. \nIce Giant: Like Uranus, it is an ice giant composed of hydrogen, helium, water, ammonia, and methane, which gives it a striking deep blue color. \nFast Winds: Neptune has the fastest winds in the solar system, reaching speeds of up to 2,100 km/h (1,300 mph). \nGreat Dark Spot: This storm, similar to Jupiter’s Great Red Spot, was first observed by Voyager 2 in 1989 but has since disappeared. \nFaint Rings: Neptune has six faint and incomplete rings made of dust and ice particles. \nMany Moons: It has 14 known moons, with Triton being the largest and most intriguing due to its retrograde orbit and potential subsurface ocean. \nLong Orbit: Neptune takes 165 Earth years to complete one orbit around the Sun; it was discovered in 1846 and completed its first full orbit in 2011. \nExploration Mission: NASA’s Voyager 2 is the only spacecraft to have visited Neptune, providing valuable insights into its atmosphere, rings, and moons. \n",
        "image": ["neptune.jpg","neptune1.jpg","neptune2.jpg"],
        "quiz": [
            {"question": "Which planet is known for its strong winds?", "options": ["Saturn", "Neptune", "Jupiter", "Uranus"], "answer": "Neptune"},
            {"question": "What is the primary gas in Neptune's atmosphere?", "options": ["Oxygen", "Hydrogen", "Methane", "Helium"], "answer": "Methane"},
            {"question": "What is Neptune's most famous feature?", "options": ["The Great Red Spot", "The Great Dark Spot", "Titan", "The Rings"], "answer": "The Great Dark Spot"},
            {"question": "How many moons does Neptune have?", "options": ["14", "3", "5", "13"], "answer": "14"},
            {"question": "Neptune has a striking blue color because of which gas?", "options": ["Oxygen", "Methane", "Nitrogen", "Carbon Dioxide"], "answer": "Methane"},
            {"question": "Which spacecraft visited Neptune?", "options": ["Voyager 1", "Voyager 2", "Parker", "New Horizons"], "answer": "Voyager 2"},
            {"question": "What year did Voyager 2 fly by Neptune?", "options": ["1989", "1987", "1999", "1978"], "answer": "1989"},
            {"question": "Neptune has the strongest winds in the solar system. True or False?", "options": ["True", "False"], "answer": "True"},
            {"question": "How long is a day on Neptune?", "options": ["16 hours", "24 hours", "12 hours", "30 hours"], "answer": "16 hours"},
            {"question": "Which of the following is Neptune's largest moon?", "options": ["Triton", "Titan", "Ganymede", "Europa"], "answer": "Triton"}
        ]
    },
    "Pluto": {
        "info": "Dwarf Planet: Pluto was classified as the ninth planet until 2006, when it was redefined as a dwarf planet by the International Astronomical Union. \nSmall Size: It is much smaller than Earth's Moon, with a diameter of about 2,377 km (1,477 miles). \nIcy Surface: Pluto’s surface is composed of nitrogen, methane, and carbon monoxide ice, giving it a reflective and patchy appearance. \nCold and Distant: Located in the Kuiper Belt, Pluto has surface temperatures averaging -229°C (-380°F). \nLong Orbit: Pluto takes 248 Earth years to complete one orbit around the Sun and has an elliptical orbit, bringing it closer to the Sun than Neptune at times. \nLarge Moon: Charon, its largest moon, is almost half the size of Pluto, and the two are often considered a double-dwarf-planet system. \nThin Atmosphere: Pluto has a tenuous atmosphere made of nitrogen, methane, and carbon monoxide that expands when it is closer to the Sun and freezes when it moves farther away. \nExploration Mission: NASA’s New Horizons spacecraft flew by Pluto in 2015, revealing detailed images of its icy mountains, plains, and complex geology. \n",
        "image": ["pluto.jpg","pluto1.jpg","pluto2.jpg"],
        "quiz": [
            {"question": "What type of planet is Pluto classified as?", "options": ["Dwarf planet", "Gas giant", "Terrestrial planet", "Ice giant"], "answer": "Dwarf planet"},
            {"question": "When was Pluto discovered?", "options": ["1930", "1950", "1920", "1900"], "answer": "1930"},
            {"question": "Who discovered Pluto?", "options": ["Edwin Hubble", "Clyde Tombaugh", "Johann Gottfried", "William Herschel"], "answer": "Clyde Tombaugh"},
            {"question": "What is Pluto's largest moon?", "options": ["Charon", "Titan", "Io", "Ganymede"], "answer": "Charon"},
            {"question": "What is Pluto's atmosphere made of?", "options": ["Methane", "Hydrogen", "Oxygen", "Nitrogen"], "answer": "Methane"},
            {"question": "Pluto is the __ planet in the solar system?", "options": ["First", "Eighth", "Ninth", "Seventh"], "answer": "Ninth"},
            {"question": "Which spacecraft visited Pluto in 2015?", "options": ["Parker", "Cassini", "New Horizons", "Voyager"], "answer": "New Horizons"},
            {"question": "How long does it take Pluto to orbit the Sun?", "options": ["200 years", "150 years", "248 years", "100 years"], "answer": "248 years"},
            {"question": "What is Pluto's surface made of?", "options": ["Rock and ice", "Gas", "Metal", "Liquid water"], "answer": "Rock and ice"},
            {"question": "Which planet was Pluto once considered a part of?", "options": ["Neptune", "Uranus", "Earth", "Jupiter"], "answer": "Neptune"}
        ]
    },
}

info_label = text(text="Planet Information and Images", align='center', pos=vector(-150, (len(planets) + 1) * 10, 0),
                  height=5, color=color.white)
Quiz_label = text(text="Quiz on planets", align='center', pos=vector(150, (len(planets) + 1) * 10, 0),
                  height=5, color=color.white)

info_buttons = []
for i, planet in enumerate(planets):
    button_y = (len(planets) - i) * 10
    button = box(pos=vector(-150, button_y, 0), size=vector(25, 8, 1), color=vector(0.2, 0.6, 0.2))
    button_label = text(text=f"{planet['label'].text.split()[0]}", align='center',
                        pos=button.pos + vector(0, 0, 1), height=5, color=color.white)
    info_buttons.append({'button': button, 'label': button_label, 'planet': planet})

quiz_buttons = []
for i, planet in enumerate(planets):
    button_y = (len(planets) - i) * 10
    button = box(pos=vector(150, button_y, 0), size=vector(25, 8, 1), color=vector(0.7, 0.5, 0.2))
    button_label = text(text=f"{planet['label'].text.split()[0]}", align='center',
                        pos=button.pos + vector(0, 0, 1), height=5, color=color.white)
    quiz_buttons.append({'button': button, 'label': button_label, 'planet': planet})
    
def display_info(planet_name, detailed_info, image):
     image_html = "".join([f"<img src='{img}' width='200' height='200' style='margin:5px;'>" for img in image])
     scene.caption = f"<b>{planet_name}:</b>\n\n{detailed_info}\n\n{image_html}>"
     
def check_info_button_click():
    for btn in info_buttons:
        button_pos_2d = vector(btn['button'].pos.x, btn['button'].pos.y, 0)
        if mag(scene.mouse.pos - button_pos_2d) < btn['button'].size.x / 2:
            btn['button'].color = vector(0.2, 0.8, 0.2)  
            planet_name = btn['label'].text.split()[0]  
            planet_info = planetary_details.get(planet_name, {})
            if planet_info:
                display_info(planet_name, planet_info['info'], planet_info.get('image', []))
                
#Code for the entire quiz process
                
def start_quiz(planet_name):
    quiz_data = planetary_details.get(planet_name, {}).get('quiz', [])
    selected_quizzes = random.sample(quiz_data, 5)
    scene.caption = "" 
    user_answers = [] 
    scene.events = []
    for i, quiz in enumerate(selected_quizzes, start=1):
        question = quiz['question']
        options = "\n".join([f"{j + 1}. {opt}" for j, opt in enumerate(quiz['options'])])
        display_questions(i, question, options)
        selected_answer = None
        while selected_answer is None:
            rate(10)  
            for event in scene.events:
                if event.key in ['1', '2', '3', '4']:  
                    selected_answer = int(event.key) - 1  
                    user_answers.append({
                        "question": question,
                        "selected_answer": quiz['options'][selected_answer],
                        "correct_answer": quiz['answer']
                    })
                    scene.events = [] 
                    break 
        while selected_answer is None:
            rate(10)
    display_results(user_answers)
    
def check_quiz_button_click():
    for btn in quiz_buttons:
        button_pos_2d = vector(btn['button'].pos.x, btn['button'].pos.y, 0) 
        if mag(scene.mouse.pos - button_pos_2d) < btn['button'].size.x / 2:
            btn['button'].color = vector(0.2, 0.8, 0.2)  
            planet_name = btn['label'].text.split()[0] 
            planet_info = planetary_details.get(planet_name, {})
            start_quiz(planet_name)
            
def display_questions(question_number, question, options):
    scene.caption = ""
    scene.caption += f"<b>Question {question_number}:</b>\n\n{question}\n\n"
    scene.caption += f"<b>Options:</b>\n{options}\n\n"
                
def display_results(user_answers):
    correct_answers = sum(1 for ans in user_answers if ans['selected_answer'] == ans['correct_answer'])
    total_questions = len(user_answers)
    result_caption = f"<b>Your Results:</b>\n\n"
    result_caption += f"Correct Answers: {correct_answers} / {total_questions}\n\n"
    for ans in user_answers:
        result_caption += f"<b>{ans['question']}</b>\nYour Answer: {ans['selected_answer']}\n"
        result_caption += f"Correct Answer: {ans['correct_answer']}\n\n"
    scene.caption = result_caption

def handle_keypress(evt):
    if evt.key in ['1', '2', '3', '4']:
        scene.events.append(evt)

scene.bind('keydown', handle_keypress) 

moon_orbit_radius = 4  
moon_orbit_speed = 0.02 
moon = sphere(radius=0.5, color=vector(0.7, 0.7, 0.7), make_trail=False, trail_type='points', trail_radius=0.05)
moon_theta = 0  

while True:
    rate(100)
    for planet in planets:
        planet['theta'] += planet['speed']
        x = planet['a'] * np.cos(planet['theta'])
        z = planet['b'] * np.sin(planet['theta'])
        planet['object'].pos = vector(x, 0, z)
        planet['label'].pos = planet['object'].pos
        if planet['object'] == planets[5]['object']:
            saturn_ring.pos = planet['object'].pos
            
    check_info_button_click()
    check_quiz_button_click()
    
    #Code to create Moon
    
    earth_pos = planets[2]['object'].pos
    moon_orbit_inclination = np.radians(30) 
    moon_theta += moon_orbit_speed
    moon_x = earth_pos.x + moon_orbit_radius * np.cos(moon_theta)
    moon_z = earth_pos.z + moon_orbit_radius * np.sin(moon_theta) * np.cos(moon_orbit_inclination)
    moon_y = earth_pos.y + moon_orbit_radius * np.sin(moon_orbit_inclination) * np.sin(moon_theta)
    moon.pos = vector(moon_x, moon_y, moon_z)