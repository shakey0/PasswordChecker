import re

class PasswordChecker():
    def check(self, password):
        if len(password) < 20:
            return "Password must be at least 20 characters."
        elif len([char for char in password if char.isnumeric()]) == 0:
            return "Password must contain numbers."
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return "Password must contain symbols."
        elif len([char for char in password if char.isupper()]) == 0 or \
            len([char for char in password if char.islower()]) == 0:
            return "Password must contain uppercase and lowercase characters."
        elif len([animal for animal in self.get_animals_list() if animal in password.lower()]) == 0:
            return "Password must contain an animal."
        elif sum([int(char) for char in password if char.isnumeric()]) < 60:
            return "Password must contain digits that add up to 60."
        elif len([word for word in self.get_question_start_words() if word in password.lower()]) == 0:
            return "Password must contain a word to start a question."
        elif self.check_consecutive_sum(password) == False:
            return "Password must not contain consecutive digits adding to more than 16."
        elif len([word for word in self.english_monarchs() if word.lower() in password.lower()]) == 0:
            return "Password must contain the first name of an English monarch."
        else:
            return True


    def get_animals_list(self):
        animals_list = [
            "aardvark", "albatross", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo",
            "baboon", "badger", "barracuda", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly",
            "camel", "capybara", "caribou", "cassowary", "cat", "caterpillar", "cattle", "chameleon", "chamois", "cheetah",
            "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "cormorant", "coyote",
            "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "dotterel",
            "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant", "elk",
            "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur", "gazelle", "gerbil",
            "giant panda", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", 
            "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "herring", 
            "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", 
            "jay", "jellyfish", "kangaroo", "kingfisher", "koala", "kookaburra", "kouprey", "kudu", "lapwing", "lark",
            "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard",
            "manatee", "mandrill", "mantis", "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose",
            "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx",
            "ostrich", "otter", "owl", "oyster", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin",
            "pheasant", "pig", "pigeon", "platypus", "polar bear", "pony", "porcupine", "porpoise", "prairie dog",
            "quail", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red deer", "red panda", "reindeer",
            "rhinoceros", "rook", "salamander", "salmon", "sand dollar", "sandpiper", "sardine", "scorpion", "seahorse",
            "seal", "shark", "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid",
            "squirrel", "starling", "stingray", "stinkbug", "stork", "swallow", "swan", "tapir", "tarsier", "termite",
            "tiger", "toad", "trout", "turkey", "turtle", "vulture", "wallaby", "walrus", "wasp", "water buffalo",
            "weasel", "whale", "wildcat", "wildebeest", "wolf", "wombat", "woodpecker", "worm", "wren", "yak", "zebra"
        ]
        return animals_list
    
    def get_question_start_words(self):
        question_starts = [
            "what", "which", "who", "whom", "whose", 
            "when", "where", "why", "how", "is", 
            "are", "was", "were", "do", "does", 
            "did", "have", "has", "had", "can", 
            "could", "will", "would", "should", "shall",
            "may", "might", "must"
        ]
        return question_starts
    
    def check_consecutive_sum(self, s):
        numbers = []
        num = 0
        for char in s:
            if char.isdigit():
                num += int(char)
            else:
                if num:
                    numbers.append(num)
                    num = 0
        if num:
            numbers.append(int(num))

        if len([no for no in numbers if no > 16]) > 0:
            return False
        return True

    def english_monarchs(self):
        list_of_monarchs = [
            "Egbert", "Aethelwulf", "Aethelbald", "Aethelbert", "Aethelred", "Alfred", "Edward", "Aethelstan",
            "Edmund", "Eadred", "Eadwig", "Edgar", "Edward", "Harold", "William", "Henry", "Stephen", "Matilda",
            "Richard", "John", "Henry", "Edward", "Mary", "Elizabeth", "James", "Charles", "Oliver", "Richard",
            "Anne", "George", "Victoria", "Edward", "George", "Elizabeth"
        ]
        return list_of_monarchs
