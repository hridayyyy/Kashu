pip install transformers torch

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random

model_name = "gpt2"  
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
prompts = [
    "Picnic in the park with homemade sandwiches and fresh fruit", "Stargazing at a local observatory or in your backyard", "Wine or whiskey tasting at a vineyard or distillery", "Go-kart racing at a local track", "Attend a live concert or music festival", "Hot air balloon ride over a scenic area", "Take a cooking class together and learn a new recipe", "Outdoor movie night with a projector and blankets", "Day trip to a nearby town you've never visited before", "Volunteer together at a local charity or animal shelter", "Horseback riding along a trail", "Take a pottery class and create your own mugs or vases", "Drive-in movie at an old-fashioned theater", "Go to an escape room and solve puzzles together", "Visit an art museum or gallery exhibit", "Kayaking or canoeing down a river or lake", "Attend a stand-up comedy show at a local club", "Have a DIY pizza night with toppings of your choice", "Go hiking and enjoy a scenic picnic at the top", "Go roller skating at an indoor or outdoor rink", "Attend a food truck festival and try different cuisines", "Watch the sunrise or sunset from a scenic location", "Take a dance class like salsa, tango, or ballroom", "Visit a botanical garden or flower show", "Go apple or berry picking at a local farm", "Attend a theater performance or musical", "Make homemade ice cream or bake cookies together", "Tour a historic site or local landmark", "Go rock climbing at an indoor or outdoor climbing gym", "Bike through a scenic trail or city tour", "Rent paddle boats at a nearby lake", "Try a new restaurant or cafe in town", "Visit a farmer's market and shop for fresh produce", "Go mini-golfing or putt-putt golf", "Go bowling for a casual and fun evening", "Paint and sip at a wine and painting class", "Attend a sports game or local sporting event", "Take a pottery painting class at a local studio", "Go ice skating indoors or at a seasonal outdoor rink", "Visit a zoo or wildlife sanctuary", "Go to a planetarium and learn about the stars", "Take a scenic train ride through the countryside", "Host a game night with board games and snacks", "Attend a trivia night at a local bar or cafe", "Take a scenic drive along a coastal or mountain road", "Go to a science museum or interactive exhibit", "Visit an amusement park and ride roller coasters", "Take a photography walk and capture the beauty of your city", "Attend a local festival or street fair", "Take a yoga or meditation class for relaxation", "Plan a backyard camping night with a tent and campfire", "Do a food tour of your city, trying bites from different restaurants", "Rent scooters or bikes and explore a new neighborhood", "Try indoor skydiving for a thrilling experience", "Watch a foreign film and cook a meal from that culture", "Do a bookstore crawl and buy each other a favorite book", "Attend a flower arranging class and make bouquets", "Do a mystery dinner party with friends and solve a crime together", "Go karting or visit an arcade for a nostalgic night", "Watch a classic movie marathon with themed snacks", "Visit a lighthouse or scenic coastal point", "Go to a paint-your-own ceramics studio", "Attend a themed costume party or make one yourselves", "Visit a dog park (if you have pets) and enjoy some time outdoors", "Go on a food truck adventure, trying different street foods", "Take a trapeze class or aerial yoga for something adventurous", "Take a ferry ride and enjoy the view from the water", "Visit an aquarium and watch the marine life", "Have a rooftop dinner at a scenic rooftop bar or restaurant", "Take a self-defense class together", "Explore a nearby cave or cavern", "Do a themed photoshoot with costumes or a certain style", "Visit a chocolate factory or candy-making class", "Fly kites in the park on a breezy day", "Go for a nature walk and identify plants or birds", "Rent a cabin for the weekend and have a cozy getaway", "Take a day trip to the beach and build sandcastles", "Try archery or axe throwing at a local range", "Visit a local brewery for a beer-tasting tour", "Go for a scenic motorcycle or scooter ride", "Take a woodworking or DIY craft class", "Try paddleboarding at a local lake or beach", "Attend a car show or vintage car exhibition", "Go to a jazz or blues club and listen to live music", "Visit a butterfly conservatory or aviary", "Attend a lantern festival and release lanterns into the sky", "Try glassblowing at a local studio", "Go foraging in the woods and learn about edible plants", "Visit a haunted house or go on a ghost tour", "Take a pottery wheel class and make something unique", "Go on a historical walking tour of your city", "Do a DIY craft night and make something creative together", "Visit a natural hot spring for a relaxing soak", "Attend a murder mystery dinner theater", "Explore a flea market or antique shop", "Go fly fishing or regular fishing at a lake or river", "Do a home spa night with face masks and massages", "Take a scenic flight in a small plane or helicopter", "Go to a renaissance fair and enjoy medieval activities", "Create a time capsule together with meaningful items and bury it"
]

def generate_love_message(prompt):

    inputs = tokenizer.encode(prompt, return_tensors="pt")


    outputs = model.generate(inputs, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2, 
                             top_p=0.95, temperature=0.7)


    message = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return message

random_prompt = random.choice(prompts)
love_message = generate_love_message(random_prompt)

print(f"Prompt: {random_prompt}\nToday's Date Idea: {love_message}")
