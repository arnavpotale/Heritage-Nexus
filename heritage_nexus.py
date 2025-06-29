import random
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from googletrans import Translator
import folium
from folium.plugins import MarkerCluster
import webbrowser
import pandas as pd
from PIL import Image, ImageTk

#Language Translator Function
def language_translator():
    """Language Translation Functionality"""
    translator = Translator()
    languages = {
        "1": "af", "2": "ar", "3": "bn", "4": "zh-cn", "5": "de",
        "6": "es", "7": "fr", "8": "hi", "9": "it", "10": "ja",
        "11": "ko", "12": "ms", "13": "nl", "14": "pt", "15": "ru",
        "16": "sw", "17": "ta", "18": "th", "19": "tr", "20": "vi",
        "21": "mr"
    }
    language_names = {
        "1": "Afrikaans", "2": "Arabic", "3": "Bengali", "4": "Chinese (Simplified)", "5": "German",
        "6": "Spanish", "7": "French", "8": "Hindi", "9": "Italian", "10": "Japanese",
        "11": "Korean", "12": "Malay", "13": "Dutch", "14": "Portuguese", "15": "Russian",
        "16": "Swahili", "17": "Tamil", "18": "Thai", "19": "Turkish", "20": "Vietnamese",
        "21": "Marathi"
    }
    
    choice = simpledialog.askstring("Language Translator", "Enter number for language (1-21):\n" + "\n".join([f"{key}. {lang}" for key, lang in language_names.items()]))
    
    if choice not in languages:
        messagebox.showerror("Invalid Choice", "Invalid choice. Please enter a valid number between 1-21.")
        return

    target_language = languages[choice]
    text_to_translate = simpledialog.askstring("Enter Text", "Enter the text you want to translate:")
    
    try:
        translated = translator.translate(text_to_translate, dest=target_language)
        messagebox.showinfo("Translated Text", f"Translated Text ({language_names[choice]}):\n{translated.text}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during translation: {e}")

# World Heritage Map Generator Function
def world_heritage_map():
    """Generate World Heritage Map"""
    
    sites = [
        {"site": "Taj Mahal", "description": "A white marble mausoleum in India.", "latitude": 27.1751, "longitude": 78.0421},
        {"site": "Machu Picchu", "description": "An ancient Incan city in Peru.", "latitude": -13.1631, "longitude": -72.5450},
         {"site": "Great Wall of China", "description": "A series of fortifications in China.", "latitude": 40.4319, "longitude": 116.5704},
        {"site": "Statue of Liberty", "description": "A symbol of freedom in the USA.", "latitude": 40.6892, "longitude": -74.0445},
        {"site": "Eiffel Tower", "description": "An iconic iron tower in Paris, France.", "latitude": 48.8584, "longitude": 2.2945},
        {"site": "Sydney Opera House", "description": "A famous performing arts center in Australia.", "latitude": -33.8568, "longitude": 151.2153},
        {"site": "Colosseum", "description": "An ancient amphitheater in Rome, Italy.", "latitude": 41.8902, "longitude": 12.4922},
        {"site": "Pyramids of Giza", "description": "Ancient pyramids in Egypt.", "latitude": 29.9792, "longitude": 31.1342},
        {"site": "Angkor Wat", "description": "A massive temple complex in Cambodia.", "latitude": 13.4125, "longitude": 103.8670},
        {"site": "Mount Fuji", "description": "A sacred mountain and symbol of Japan.", "latitude": 35.3606, "longitude": 138.7274},
        {"site": "Stonehenge", "description": "A prehistoric monument in England.", "latitude": 51.1789, "longitude": -1.8262},
        {"site": "Christ the Redeemer", "description": "A famous statue in Rio de Janeiro, Brazil.", "latitude": -22.9519, "longitude": -43.2105},
        {"site": "Petra", "description": "An archaeological site in Jordan.", "latitude": 30.3285, "longitude": 35.4444},
        {"site": "Banff National Park", "description": "A stunning park in Canada known for its Rocky Mountains.", "latitude": 51.4968, "longitude": -115.9281},
        {"site": "Santorini", "description": "A beautiful island in Greece with iconic white and blue architecture.", "latitude": 36.3932, "longitude": 25.4615},
        {"site": "Grand Canyon", "description": "A natural wonder in the USA.", "latitude": 36.1069, "longitude": -112.1129},
        {"site": "Galápagos Islands", "description": "An archipelago in Ecuador known for unique wildlife.", "latitude": -0.9538, "longitude": -89.6104},
        {"site": "Uluru", "description": "A massive sandstone monolith in Australia.", "latitude": -25.3444, "longitude": 131.0369},
        {"site": "Yellowstone National Park", "description": "The first national park in the USA.", "latitude": 44.4280, "longitude": -110.5885},
        {"site": "Neuschwanstein Castle", "description": "A fairy-tale castle in Germany.", "latitude": 47.5576, "longitude": 10.7498},
        {"site": "Alhambra", "description": "A palace and fortress complex in Spain.", "latitude": 37.1761, "longitude": -3.5881},
        {"site": "Tower of London", "description": "A historic castle on the River Thames in England.", "latitude": 51.5081, "longitude": -0.0759},
        {"site": "Chichén Itzá", "description": "A large Mayan archaeological site in Mexico.", "latitude": 20.6843, "longitude": -88.5678},
        {"site": "Victoria Falls", "description": "One of the largest waterfalls, located on the Zambia-Zimbabwe border.", "latitude": -17.9243, "longitude": 25.8572},
        {"site": "Louvre Museum", "description": "The world's largest art museum in Paris, France.", "latitude": 48.8606, "longitude": 2.3376},
        {"site": "Ha Long Bay", "description": "A bay in Vietnam known for emerald waters and limestone islands.", "latitude": 20.9101, "longitude": 107.1839},
        {"site": "Acropolis of Athens", "description": "An ancient citadel in Greece.", "latitude": 37.9715, "longitude": 23.7257},
        {"site": "Mount Kilimanjaro", "description": "The highest mountain in Africa.", "latitude": -3.0674, "longitude": 37.3556},
        {"site": "Giza Pyramids", "description": "The ancient pyramids of Egypt.", "latitude": 29.9792, "longitude": 31.1342},
        {"site": "Mount Rushmore", "description": "A monumental granite sculpture in South Dakota, USA.", "latitude": 43.8791, "longitude": -103.4591},
        {"site": "Sagrada Familia", "description": "A Roman Catholic basilica in Barcelona, Spain.", "latitude": 41.4036, "longitude": 2.1744},
        {"site": "Versailles Palace", "description": "A former royal residence in France.", "latitude": 48.8049, "longitude": 2.1204},
        {"site": "Giza Necropolis", "description": "An ancient burial ground in Egypt.", "latitude": 29.9753, "longitude": 31.1325},
        {"site": "The Louvre", "description": "A world-famous museum located in Paris, France.", "latitude": 48.8606, "longitude": 2.3376},
        {"site": "Moai Statues of Easter Island", "description": "Ancient stone statues located on Easter Island.", "latitude": -27.1127, "longitude": -109.3497},
        {"site": "Auschwitz Concentration Camp", "description": "A site of historical significance in Poland.", "latitude": 50.0359, "longitude": 19.1783},
        {"site": "Berlin Wall", "description": "A historical landmark in Germany.", "latitude": 52.5163, "longitude": 13.3777},
        {"site": "Palace of Versailles", "description": "A former royal residence in France.", "latitude": 48.8049, "longitude": 2.1204},
        {"site": "Shwedagon Pagoda", "description": "A famous pagoda in Myanmar.", "latitude": 16.7843, "longitude": 96.1595},
        {"site": "Mount Etna", "description": "A highly active volcano in Sicily, Italy.", "latitude": 37.7510, "longitude": 15.0047},
        {"site": "Pompeii", "description": "An ancient city preserved by volcanic ash in Italy.", "latitude": 40.7487, "longitude": 14.4847},
        {"site": "Iguazu Falls", "description": "A massive waterfall system in South America.", "latitude": -25.6953, "longitude": -54.4367},
        {"site": "Sultan Ahmed Mosque", "description": "A historic mosque in Istanbul, Turkey.", "latitude": 41.0053, "longitude": 28.9760},
        {"site": "Chernobyl Exclusion Zone", "description": "The site of the 1986 nuclear disaster in Ukraine.", "latitude": 51.2760, "longitude": 30.2211},
        {"site": "Kremlin", "description": "A fortified complex in Moscow, Russia.", "latitude": 55.7558, "longitude": 37.6176},
        {"site": "Red Fort", "description": "A historic fort in Delhi, India.", "latitude": 28.6562, "longitude": 77.2410},
        {"site": "Qutub Minar", "description": "A towering minaret in Delhi, India.", "latitude": 28.5244, "longitude": 77.1855},
        {"site": "Bodh Gaya", "description": "The site of Buddha's enlightenment in Bihar, India.", "latitude": 24.6955, "longitude": 84.9915},
        {"site": "Fatehpur Sikri", "description": "A city built by the Mughal emperor Akbar in India.", "latitude": 27.1000, "longitude": 77.6755},
        {"site": "Humayun's Tomb", "description": "The tomb of the Mughal emperor Humayun in Delhi, India.", "latitude": 28.5922, "longitude": 77.2500},
        {"site": "Khajuraho Temples", "description": "Famous for their intricate erotic sculptures in Madhya Pradesh, India.", "latitude": 24.8473, "longitude": 79.9195},
        {"site": "Sanchi Stupa", "description": "A Buddhist complex in Madhya Pradesh, India.", "latitude": 23.4902, "longitude": 77.7490},
        {"site": "Elephanta Caves", "description": "Ancient rock-cut temples on Elephanta Island in Mumbai, India.", "latitude": 18.9275, "longitude": 72.9286},
        {"site": "Ajanta and Ellora Caves", "description": "Buddhist rock-cut cave complexes in Maharashtra, India.", "latitude": 20.5292, "longitude": 75.7069},
        {"site": "Meghalaya Living Root Bridges", "description": "Unique natural bridges formed by the roots of trees in Meghalaya, India.", "latitude": 25.2900, "longitude": 91.5863},
        {"site": "Jantar Mantar", "description": "An astronomical observatory in Jaipur, India.", "latitude": 26.9196, "longitude": 75.8260},
        {"site": "Rani-ki-Vav", "description": "A stepwell in Patan, Gujarat, India.", "latitude": 23.8528, "longitude": 72.1333},
        {"site": "Sundarbans Mangrove Forests", "description": "The world's largest tidal halophytic mangrove forest in West Bengal, India.", "latitude": 21.9494, "longitude": 88.1692},
        {"site": "Kaziranga National Park", "description": "A UNESCO World Heritage Site and home to the Indian one-horned rhinoceros.", "latitude": 26.6525, "longitude": 93.1700},
        {"site": "Brihadeeswarar Temple", "description": "A grand temple in Thanjavur, Tamil Nadu, India.", "latitude": 10.7869, "longitude": 79.1316},
        {"site": "Rock Shelters of Bhimbetka", "description": "Caves in Madhya Pradesh with prehistoric rock paintings.", "latitude": 22.6948, "longitude": 77.4377},
        {"site": "Giant's Causeway", "description": "An area of interlocking basalt columns in Northern Ireland.", "latitude": 55.2400, "longitude": -6.5111},
        {"site": "Cahokia Mounds", "description": "A pre-Columbian Native American city in Illinois, USA.", "latitude": 38.6466, "longitude": -90.0687},
        {"site": "Easter Island", "description": "An island in the southeastern Pacific Ocean, known for its Moai statues.", "latitude": -27.1127, "longitude": -109.3497},
        {"site": "Mount Vesuvius", "description": "An active volcano near Naples, Italy.", "latitude": 40.8222, "longitude": 14.4269},
        {"site": "Mount Sinai", "description": "A mountain in Egypt, traditionally associated with the Biblical Mount Sinai.", "latitude": 28.5392, "longitude": 33.9735},
        {"site": "Banaue Rice Terraces", "description": "A 2,000-year-old terrace system in the Philippines.", "latitude": 16.9269, "longitude": 121.0516},
        {"site": "Ischigualasto Provincial Park", "description": "A fossil-rich park in Argentina.", "latitude": -30.9510, "longitude": -67.6141},
        {"site": "Arenal Volcano", "description": "An active volcano in Costa Rica.", "latitude": 10.4634, "longitude": -84.7037}
    ]
    
    world_map = folium.Map(location=[0, 0], zoom_start=2)
    marker_cluster = MarkerCluster().add_to(world_map)

    for site in sites:
        folium.Marker(
            location=[site["latitude"], site["longitude"]],
            popup=f"<b>{site['site']}</b><br>{site['description']}",
        ).add_to(marker_cluster)

   
    output_file = os.path.abspath("world_heritage_map.html")
    print("Saving map to:", output_file)

    world_map.save(output_file)
    webbrowser.open(output_file)
    messagebox.showinfo("Map Generated", f"World Heritage Map has been generated. Opened in your browser.")


def global_festivals_game():
    """Trivia Game Functionality"""
    def get_questions():
        return [
            {
                "question": "Which festival is known as the 'Festival of Colors' in India?",
                "choices": ["A) Diwali", "B) Holi", "C) Eid", "D) Navratri"],
                "answer": "B"
            }, {"question": "Which festival is known as the 'Festival of Colors' in India?", "choices": ["A) Diwali", "B) Holi", "C) Eid", "D) Navratri"], "answer": "B"},
        {"question": "In which country is the ancient city of Petra located?", "choices": ["A) Greece", "B) Jordan", "C) Egypt", "D) Iraq"], "answer": "B"},
        {"question": "What is the traditional Japanese art of folding paper called?", "choices": ["A) Origami", "B) Ikebana", "C) Karate", "D) Sumi-e"], "answer": "A"},
        {"question": "Which famous landmark is located in Paris, France?", "choices": ["A) Eiffel Tower", "B) Colosseum", "C) Great Wall of China", "D) Machu Picchu"], "answer": "A"},
        {"question": "The Taj Mahal is located in which city?", "choices": ["A) Delhi", "B) Jaipur", "C) Agra", "D) Mumbai"], "answer": "C"},
        {"question": "Which country is home to the Great Barrier Reef?", "choices": ["A) New Zealand", "B) Australia", "C) South Africa", "D) United States"], "answer": "B"},
        {"question": "What is the name of the famous ancient Mayan city in Mexico?", "choices": ["A) Teotihuacan", "B) Chichen Itza", "C) Tulum", "D) Machu Picchu"], "answer": "B"},
        {"question": "Which ancient civilization built the pyramids of Egypt?", "choices": ["A) Romans", "B) Egyptians", "C) Mayans", "D) Greeks"], "answer": "B"},
        {"question": "What is the traditional dress of Scotland?", "choices": ["A) Kimono", "B) Kilt", "C) Sari", "D) Toga"], "answer": "B"},
        {"question": "Which festival is celebrated by lighting lamps and fireworks in India?", "choices": ["A) Holi", "B) Diwali", "C) Eid", "D) Christmas"], "answer": "B"},
        {"question": "What is the national dance of Spain?", "choices": ["A) Tango", "B) Flamenco", "C) Waltz", "D) Salsa"], "answer": "B"},
        {"question": "In which country would you find the iconic Machu Picchu?", "choices": ["A) Peru", "B) Bolivia", "C) Brazil", "D) Ecuador"], "answer": "A"},
        {"question": "Which African country is known for its pyramids and ancient tombs?", "choices": ["A) Egypt", "B) Kenya", "C) South Africa", "D) Nigeria"], "answer": "A"},
        {"question": "Which ancient site is known as the ‘Lost City of the Incas’?", "choices": ["A) Petra", "B) Machu Picchu", "C) Colosseum", "D) Stonehenge"], "answer": "B"},
        {"question": "Which Asian country celebrates Songkran, the traditional New Year festival?", "choices": ["A) Thailand", "B) Japan", "C) China", "D) India"], "answer": "A"},
        {"question": "Which famous structure is located in China?", "choices": ["A) The Colosseum", "B) Great Wall", "C) Petra", "D) Pyramids"], "answer": "B"},
        {"question": "Which country is home to the famous landmark, the Colosseum?", "choices": ["A) Spain", "B) Greece", "C) Italy", "D) France"], "answer": "C"},
        {"question": "What is the traditional Chinese philosophy and practice of creating harmony with nature?", "choices": ["A) Buddhism", "B) Taoism", "C) Confucianism", "D) Shinto"], "answer": "B"},
        {"question": "Which iconic landmark is located in Rio de Janeiro, Brazil?", "choices": ["A) Christ the Redeemer", "B) Eiffel Tower", "C) Statue of Liberty", "D) Big Ben"], "answer": "A"},
        {"question": "What was the famous festival of the Aztecs dedicated to the sun god?", "choices": ["A) Day of the Dead", "B) Sun Festival", "C) Quetzalcoatl", "D) Tlachtli"], "answer": "B"},
        {"question": "Which country is home to the world-renowned ancient site of the Acropolis?", "choices": ["A) Italy", "B) Greece", "C) Turkey", "D) Egypt"], "answer": "B"},
        {"question": "What is the name of the traditional Japanese flower arranging art?", "choices": ["A) Sumi-e", "B) Ikebana", "C) Origami", "D) Karate"], "answer": "B"},
        {"question": "Which Indian festival celebrates the harvest season and is known for flying kites?", "choices": ["A) Pongal", "B) Diwali", "C) Makar Sankranti", "D) Onam"], "answer": "C"},
        {"question": "Which Italian city is famous for its canals and gondola rides?", "choices": ["A) Rome", "B) Venice", "C) Milan", "D) Florence"], "answer": "B"},
        {"question": "Which cultural festival in Brazil involves colorful parades and samba dancing?", "choices": ["A) Carnival", "B) Oktoberfest", "C) Holi", "D) St. Patrick's Day"], "answer": "A"},
        {"question": "In which country would you find the ancient city of Pompeii?", "choices": ["A) France", "B) Italy", "C) Greece", "D) Turkey"], "answer": "B"},
        {"question": "Which city is known as the 'City of Love'?", "choices": ["A) Paris", "B) Rome", "C) Madrid", "D) Vienna"], "answer": "A"},
        {"question": "Which country is home to the iconic site, the Eiffel Tower?", "choices": ["A) Germany", "B) France", "C) Italy", "D) Spain"], "answer": "B"},
        {"question": "What is the name of the sacred river in India, worshipped as a goddess?", "choices": ["A) Ganges", "B) Nile", "C) Yangtze", "D) Danube"], "answer": "A"},
        {"question": "Which city is home to the famous landmark, the Sydney Opera House?", "choices": ["A) Sydney", "B) Melbourne", "C) Brisbane", "D) Perth"], "answer": "A"},
        {"question": "Which American landmark is known as the 'Statue of Liberty'?", "choices": ["A) Washington Monument", "B) Statue of Liberty", "C) Lincoln Memorial", "D) Golden Gate Bridge"], "answer": "B"},
        {"question": "Which ancient civilization is known for building pyramids in Egypt?", "choices": ["A) Greeks", "B) Egyptians", "C) Romans", "D) Sumerians"], "answer": "B"},
        {"question": "Which festival in India marks the victory of good over evil and is celebrated by burning effigies?", "choices": ["A) Diwali", "B) Dussehra", "C) Holi", "D) Navratri"], "answer": "B"},
        {"question": "The famous Blue Mosque is located in which city?", "choices": ["A) Cairo", "B) Istanbul", "C) Mecca", "D) Tehran"], "answer": "B"},
        {"question": "Which is the largest religious monument in the world, located in Cambodia?", "choices": ["A) Borobudur", "B) Angkor Wat", "C) Notre-Dame Cathedral", "D) St. Peter's Basilica"], "answer": "B"},
        {"question": "Which UNESCO World Heritage Site is located in the country of Turkey?", "choices": ["A) Hagia Sophia", "B) Christ the Redeemer", "C) Petra", "D) Mount Fuji"], "answer": "A"},
        {"question": "In which country is the cultural practice of Flamenco dancing popular?", "choices": ["A) Italy", "B) Spain", "C) France", "D) Mexico"], "answer": "B"},
        {"question": "Which ancient wonder was located in the city of Babylon, Iraq?", "choices": ["A) Hanging Gardens", "B) Great Pyramid of Giza", "C) Statue of Zeus", "D) Lighthouse of Alexandria"], "answer": "A"},
        {"question": "Which city is known for its famous landmarks, the Big Ben and London Eye?", "choices": ["A) London", "B) Paris", "C) Rome", "D) New York"], "answer": "A"},
        {"question": "Which is the largest man-made structure on Earth?", "choices": ["A) Great Wall of China", "B) Colosseum", "C) The Louvre", "D) Christ the Redeemer"], "answer": "A"},
        {"question": "Which country is famous for the traditional dance called the Tango?", "choices": ["A) Brazil", "B) Argentina", "C) Spain", "D) Italy"], "answer": "B"},
        {"question": "Which country is known for its Mount Fuji and tea ceremonies?", "choices": ["A) China", "B) Japan", "C) India", "D) South Korea"], "answer": "B"},
          
        ]
    
    questions = get_questions()

    
    num_questions = simpledialog.askinteger("Number of Questions", "How many questions would you like to answer?", minvalue=1, maxvalue=len(questions))

   
    selected_questions = random.sample(questions, num_questions)
    
    score = 0

   
    for question in selected_questions:
        answer = simpledialog.askstring("Question", f"{question['question']}\n" + "\n".join(question["choices"]))
        if answer.strip().upper() == question["answer"]:
            score += 1
        else:
        
            correct_choice = question['choices'][ord(question["answer"]) - 65]
            messagebox.showinfo("Incorrect", f"Incorrect! The correct answer was: {correct_choice}")
    
    messagebox.showinfo("Game Over", f"Game Over! Your score: {score}/{num_questions}")

def manuscripts_library_sites():
    """Manuscripts or Library Sites Menu"""
    sites = [
        
    {"name": "Perseus Digital Library", "url": "https://www.perseus.tufts.edu/hopper/"},
    {"name": "Project Gutenberg", "url": "https://www.gutenberg.org/"},
    {"name": "Internet Archive", "url": "https://archive.org/"},
    {"name": "Digital Bodleian", "url": "https://digital.bodleian.ox.ac.uk/"},
    {"name": "World Digital Library", "url": "https://www.wdl.org/en/"},
    {"name": "Sanskrit Manuscripts in the South Asian Rare Books Collection", "url": "https://blogs.loc.gov/international-collections/2018/01/sanskrit-manuscripts-in-the-south-asian-rare-books-collection/"},
    {"name": "Indian Manuscripts", "url": "https://indianmanuscripts.com/"},
    {"name": "National Mission for Manuscripts (India)", "url": "https://www.namami.gov.in/major-manuscript-repositories-india"},
    {"name": "Sanskrit Documents", "url": "https://sanskritdocuments.org/"},
    {"name": "The British Library - Ancient Manuscripts", "url": "https://www.bl.uk/medieval-literature"},
    {"name": "The Vatican Library", "url": "https://www.vaticanlibrary.va/"},
    {"name": "HathiTrust Digital Library", "url": "https://www.hathitrust.org/"},
    {"name": "The Huntington Library", "url": "https://www.huntington.org/library"},
    {"name": "The Royal Library of Belgium - Digital Library", "url": "https://www.kbr.be/en/digital-library/"},
    {"name": "The Oriental Institute of the University of Chicago - Digital Collections", "url": "https://oi.uchicago.edu/collections"},
    {"name": "National Archives (UK) - Digital Resources", "url": "https://www.nationalarchives.gov.uk/"},
    {"name": "The Islamic Manuscripts Collection at Harvard University", "url": "https://library.harvard.edu/collections/islamic-manuscripts"},
    {"name": "The National Library of China", "url": "http://www.nlc.cn/"},
    {"name": "Internet Sacred Text Archive", "url": "https://www.sacred-texts.com/"},
    {"name": "Digital Scriptorium", "url": "https://www.digitalscriptorium.org/"},
    {"name": "The Asia Minor & Black Sea Digital Library", "url": "https://www.accordancesoftware.com/"},
    {"name": "The Digital Public Library of America", "url": "https://dp.la/"}


    ]

    site_list = "\n".join([f"{i + 1}. {site['name']}" for i, site in enumerate(sites)])
    site_choice = simpledialog.askstring("Manuscripts Library Sites", f"Available Manuscripts or Library Sites:\n{site_list}\nEnter the number of your choice (or 0 to exit):")
    
    try:
        site_choice = int(site_choice)
        if 0 < site_choice <= len(sites):
            selected_site = sites[site_choice - 1]
            webbrowser.open(selected_site['url'])
            messagebox.showinfo("Opening Site", f"You selected: {selected_site['name']}\nOpening in browser.")
        elif site_choice == 0:
            messagebox.showinfo("Exit", "Returning to the main menu.")
        else:
            messagebox.showerror("Invalid Choice", "Invalid choice. Try again.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Tkinter UI for Main Menu
root = tk.Tk()
root.title("HERITAGE NEXUS")


root.state('zoomed')


def resize_bg(event):
    new_width = event.width
    new_height = event.height
    resized_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_photo_resized = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(bg_image_id, image=bg_photo_resized)
    canvas.bg_photo_resized = bg_photo_resized  


def resize_bg(event):
    
    new_width = event.width
    new_height = event.height
    resized_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_photo_resized = ImageTk.PhotoImage(resized_image)
    

    canvas.itemconfig(bg_image_id, image=bg_photo_resized)
    canvas.bg_photo_resized = bg_photo_resized  


bg_image = Image.open("bgg2.jpeg")
bg_photo = ImageTk.PhotoImage(bg_image)


canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both", expand=True)


bg_image_id = canvas.create_image(0, 0, image=bg_photo, anchor="nw")


root.bind("<Configure>", resize_bg)

menu_label = tk.Label(root, text="Cultural Explorer", font=("Arial", 24, "bold"), bg="#ffffff", fg="black")
menu_label_window = canvas.create_window(1000,1000 , window=menu_label)

buttons = [
    {"text": "Language Translator", "command": language_translator},
    {"text": "World Heritage Map Generator", "command": world_heritage_map },
    {"text": "Global Festivals Trivia Game", "command": global_festivals_game},
    {"text": "Manuscripts or Library Sites", "command": manuscripts_library_sites},
]


button_images = {
    "Language Translator": "speak.jpeg",
    "World Heritage Map Generator": "location.jpeg",
    "Global Festivals Trivia Game": "pen.jpeg",
    "Manuscripts or Library Sites": "book.jpeg",
}


button_icons = {}
for key, path in button_images.items():
    img = Image.open(path).resize((50, 50), Image.Resampling.LANCZOS)  
    button_icons[key] = ImageTk.PhotoImage(img)


buttons = [
    {"text": "Language Translator", "command": language_translator, "icon": button_icons["Language Translator"]},
    {"text": "World Heritage Map ", "command": world_heritage_map, "icon": button_icons["World Heritage Map Generator"]},
    {"text": "Cultural Trivia Game", "command": global_festivals_game, "icon": button_icons["Global Festivals Trivia Game"]},
    {"text": "Manuscripts and Library Sites", "command": manuscripts_library_sites, "icon": button_icons["Manuscripts or Library Sites"]},
]

for i, button_info in enumerate(buttons):
    button = tk.Button(
        root,
        text=button_info["text"],
        image=button_info["icon"],
        compound="left", 
        command=button_info["command"],
        font=("Arial", 14),
        bg="light yellow",
        fg="black",
        width=300,
        height=80
    )
    

    
    button_window = canvas.create_window(750, 240 + i * 130, window=button)

exit_button = tk.Button(
    root,
    text="Exit",
 
    compound="left",
    command=root.quit,
    font=("Arial", 14),
    bg="red",
    fg="white",
    width=15,
    height=2
)
exit_button_window = canvas.create_window(750, 440 + len(buttons) * 70, window=exit_button)
root.mainloop()
