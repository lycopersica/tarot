import random
import pyinputplus as pyip
import art

# List of major arcana tarot cards and their meanings
major_arcana = [
    {"name": "The Fool", "meaning": "Spontaneity, leap of faith, naivete"},
    {"name": "The Magician", "meaning": "Boundless energy, action, chaos"},
    {"name": "The High Priestess", "meaning": "Intuition, secrets, hidden knowledge"},
    {"name": "The Empress", "meaning": "The Mother, creation, nature, smothering"},
    {"name": "The Emperor", "meaning": "The Father, protection, stability, withholding"},
    {"name": "The Hierophant", "meaning": "Seeking knowledge, mentorship, ceremony, bureaucracy"},
    {"name": "The Lovers", "meaning": "Union, sex, love, joy"},
    {"name": "The Chariot", "meaning": "Will, triumph, perseverance"},
    {"name": "Strength", "meaning": "Mastery of emotions, self control, courage"},
    {"name": "The Hermit", "meaning": "Solitude, meditation, stillness, self-awareness"},
    {"name": "Wheel of Fortune", "meaning": "Destiny, changing of course, the will of the universe"},
    {"name": "Justice", "meaning": "Karma, difficult decisions, balance of choice"},
    {"name": "The Hanged Man", "meaning": "Sacrifice, letting go, disentanglement"},
    {"name": "Death", "meaning": "Transformation, closing a chapter, struggle to be born"},
    {"name": "Temperance", "meaning": "Healing, renewal, moderation"},
    {"name": "The Devil", "meaning": "Addiction, bondage, destructive cycles"},
    {"name": "The Tower", "meaning": "Unexpected upheaval, personal breakthrough"},
    {"name": "The Star", "meaning": "Hope, peacefulness, childlike wonder"},
    {"name": "The Moon", "meaning": "Vivid imagination, the inner self, shadows"},
    {"name": "The Sun", "meaning": "Vitality, enlightenment, rebirth again and again"},
    {"name": "Judgement", "meaning": "Forgiveness, moving on, closure"},
    {"name": "The World", "meaning": "Wholeness, completion, harmony"},

]

# List of minor arcana tarot cards and their meanings
minor_arcana = [
    {"name": "Ace of Wands", "meaning": "New beginnings, inspiration, creativity"},
    {"name": "Two of Wands", "meaning": "Determination, direction, success"},
    {"name": "Three of Wands", "meaning": "Envisioning the future, self-sufficiency"},
    {"name": "Four of Wands", "meaning": "Completion, celebration, reward"},
    {"name": "Five of Wands", "meaning": "Conflict, lack of focus, loss"},
    {"name": "Six of Wands", "meaning": "Victory, success, rising up"},
    {"name": "Seven of Wands", "meaning": "Courage, inner strength, self reliance"},
    {"name": "Eight of Wands", "meaning": "Insight, sudden change, movement"},
    {"name": "Nine of Wands", "meaning": "Strength, stamina, courage"},
    {"name": "Ten of Wands", "meaning": "Burdens, blockage, difficulty"},
    {"name": "Page of Wands", "meaning": "Visionary, inspirational, potential"},
    {"name": "Knight of Wands", "meaning": "Charming, adventurous, illusory"},
    {"name": "Queen of Wands", "meaning": "Vibrant, protective, forceful"},
    {"name": "King of Wands", "meaning": "Charismatic, creative, compassionate"},
    {"name": "Ace of Cups", "meaning": "New phases, revitalization, love"},
    {"name": "Two of Cups", "meaning": "Connection, romance, anticipation"},
    {"name": "Three of Cups", "meaning": "Friendship, joy, bounty"},
    {"name": "Four of Cups", "meaning": "Greed, discontent, longing"},
    {"name": "Five of Cups", "meaning": "Grief, disappointment, sorrow"},
    {"name": "Six of Cups", "meaning": "Memories, childhood, joy"},
    {"name": "Seven of Cups", "meaning": "Illusion, deception, temptation"},
    {"name": "Eight of Cups", "meaning": "Stagnation, illness, departure"},
    {"name": "Nine of Cups", "meaning": "Harmony, bliss, wishes coming true"},
    {"name": "Ten of Cups", "meaning": "Energy, positivity, actualization"},
    {"name": "Page of Cups", "meaning": "Creative, emotional, unstable"},
    {"name": "Knight of Cups", "meaning": "Artistic, introspective, unreadable"},
    {"name": "Queen of Cups", "meaning": "Insightful, tranquil, psychic"},
    {"name": "King of Cups", "meaning": "Diplomatic, open minded, dignified"},
    {"name": "Ace of Swords", "meaning": "Truth, mental clarity, decisiveness"},
    {"name": "Two of Swords", "meaning": "Opposing forces, blockage, stagnation"},
    {"name": "Three of Swords", "meaning": "Betrayal, heartbreak, turmoil"},
    {"name": "Four of Swords", "meaning": "Stillness, fearlessness, internal focus"},
    {"name": "Five of Swords", "meaning": "Self-destruction, hubris, discord"},
    {"name": "Six of Swords", "meaning": "Hope, recovery, travel"},
    {"name": "Seven of Swords", "meaning": "Secrecy, self-interest, deceit"},
    {"name": "Eight of Swords", "meaning": "Powerlessness, feeling trapped, limited perceptions"},
    {"name": "Nine of Swords", "meaning": "Dark visions, shadow self, depression"},
    {"name": "Ten of Swords", "meaning": "Ruin, self-pity, rock bottom"},
    {"name": "Page of Swords", "meaning": "Honest, keenly observant, judgemental"},
    {"name": "Knight of Swords", "meaning": "Determined, dynamic, exhausting"},
    {"name": "Queen of Swords", "meaning": "Sharp, perceptive, critical"},
    {"name": "King of Swords", "meaning": "Fair, analytical, removed"},
    {"name": "Ace of Coins", "meaning": "Prosperity, windfall, seedlings"},
    {"name": "Two of Coins", "meaning": "Balance, material change, metamorphosis"},
    {"name": "Three of Coins", "meaning": "Teamwork, determination, focus"},
    {"name": "Four of Coins", "meaning": "Material gain, possessiveness, rigid control"},
    {"name": "Five of Coins", "meaning": "Sadness, anxiety, illness"},
    {"name": "Six of Coins", "meaning": "Growth, generosity, prosperous harvest"},
    {"name": "Seven of Coins", "meaning": "Uncertainty, avoidance, contemplation"},
    {"name": "Eight of Coins", "meaning": "Craftsmanship, skill, mastery"},
    {"name": "Nine of Coins", "meaning": "Newfound stability, work paying off, luxury"},
    {"name": "Ten of Coins", "meaning": "Abundance, completion, caretaking"},
    {"name": "Page of Coins", "meaning": "Hard-working, responsible, avoidant"},
    {"name": "Knight of Coins", "meaning": "Loyal, dedicated, stubborn"},
    {"name": "Queen of Coins", "meaning": "Domestic, healing, needy"},
    {"name": "King of Coins", "meaning": "Calm, dedicated, stable"},

]


# Function to perform tarot reading
def tarot_reading():
    art.tprint("TAROT", "wizard")
    arcana_choice = input("Enter 'major' for major arcana cards only or 'minor' for all cards: ")
    number_of_cards = input("Enter 1 for one card pull or 3 for three card past-present-future spread: ")
    input("Focus on your question and press enter to draw the cards")
    if arcana_choice == 'major':
        cards = major_arcana
    elif arcana_choice == 'minor':
        cards = major_arcana + minor_arcana
    else:
        print("Invalid input")
        return

    if number_of_cards == '1':
        # Select one random card
        card = random.choice(cards)
        print("Your tarot card is: " + card["name"])
        print("Interpretation: " + card["meaning"])
    elif number_of_cards == '3':
        # Select 3 random cards
        reading = random.sample(cards, 3)

        print("Your tarot reading:")
        print("Past: " + reading[0]["name"] + " - " + reading[0]["meaning"])
        print("Present: " + reading[1]["name"] + " - " + reading[1]["meaning"])
        print("Future: " + reading[2]["name"] + " - " + reading[2]["meaning"])
    else:
        print("Invalid input")


# Perform the reading
tarot_reading()
while True:
    continue_choice = pyip.inputYesNo(prompt="Do you want to continue? (yes/no)")
    if continue_choice.lower() == "yes":
        tarot_reading()
    else:
        break

# example of how to add more stuff to the card dictionary
# cards = [
#     {"name": "The Fool", "meaning": "New beginnings, taking a leap of faith, spontaneity", "description": "The Fool represents the beginning of a new journey, taking a leap of faith and embracing the unknown. It suggests a sense of spontaneity and carefree attitude.", "image": "https://www.example.com/fool.jpg"},
#     {"name": "The Magician", "meaning": "Manipulation, creativity, power", "description": "The Magician is a card of manipulation, creativity, and power. It suggests the ability to take control of a situation and turn it to your advantage.", "image": "https://www.example.com/magician.jpg"},
#     # Add more cards here
# ]
