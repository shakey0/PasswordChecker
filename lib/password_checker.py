import re

class PasswordChecker():
    def check(self, password):
        if len(password) < 20:
            return "Password must be at least 20 characters."
        elif len([char for char in password if char.isnumeric()]) == 0:
            return "Password must contain numbers."
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>£€¥₹₽₣₢¢₦₡₧₪₸₫₩₭₮₯₶₲₴₺₥₰₠₣₤₧₨₩₪₫₭₮₯₰₠₡₢₣₤₥₦₧₨₩₪₫₭₮₯₶₷₸₹₺₻₼₽₾₿]', password):
            return "Password must contain symbols."
        elif len([char for char in password if char.isupper()]) == 0 or \
            len([char for char in password if char.islower()]) == 0:
            return "Password must contain uppercase and lowercase characters."
        elif len([animal for animal in self.get_animals_list() if animal in password.lower()]) == 0:
            return "Password must contain an animal."
        elif sum([int(char) for char in password if char.isnumeric()]) < 60:
            return "Password must contain digits that add up to at least 60."
        elif len([word for word in self.get_question_start_words() if word in password.lower()]) == 0:
            return "Password must contain a word to start a question."
        elif self.check_consecutive_sum(password) == False:
            return "Password must not contain consecutive digits adding to more than 16."
        elif len([word for word in self.english_monarchs() if word.lower() in password.lower()]) == 0:
            return "Password must contain the first name of an English monarch."
        else:
            return True


    def get_animals_list(self):
        animals_list = ['aardvark', 'adder', 'agouti', 'akita', 'albatross', 'alligator', 'alpaca',
                        'amphibian', 'anaconda', 'angelfish', 'anole', 'ant', 'anteater', 'antelope',
                        'antlion', 'aoudad', 'ape', 'aphid', 'arachnid', 'argali', 'armadillo', 'armet',
                        'avocet', 'axolotl', 'babirusa', 'baboon', 'badelfish', 'badger', 'barbet',
                        'barracuda', 'basilisk', 'bass', 'bat', 'batfish', 'bear', 'beast', 'beaver',
                        'bee', 'beetle', 'beluga', 'betta', 'bichon', 'binturong', 'bird', 'bison',
                        'bluefish', 'bluejay', 'boa', 'boar', 'booby', 'boto', 'boxer', 'bream', 'buck',
                        'budgerigar', 'buffalo', 'bug', 'bulbul', 'bullfrog', 'bumblebee', 'bunting',
                        'bushbaby', 'butterfly', 'buzzard', 'caiman', 'camel', 'canary', 'capybara',
                        'caracal', 'cardinal', 'caribou', 'carp', 'cassowary', 'cat', 'catbird',
                        'caterpillar', 'catfish', 'cattle', 'centipede', 'chameleon', 'chamois',
                        'chaparral', 'cheetah', 'chickadee', 'chicken', 'chihuahua', 'chimpanzee',
                        'chinchbug', 'chinchilla', 'chipmunk', 'chital', 'chough', 'chow', 'cicada',
                        'civet', 'clam', 'coati', 'cobra', 'cockatiel', 'cockatoo', 'cockroach', 'cod',
                        'codfish', 'collie', 'conch', 'condor', 'conure', 'coot', 'copperhead', 'coral',
                        'cormorant', 'cottonmouth', 'cougar', 'cowbird', 'coyote', 'crab', 'crane',
                        'crappie', 'cricket', 'crocodile', 'crossbill', 'crow', 'cuckoo', 'cur',
                        'curassow', 'curlew', 'cuscus', 'cuttlefish', 'dachshund', 'dalmatian',
                        'damselfly', 'danio', 'dartfish', 'deer', 'dhole', 'dingo', 'dinosaur',
                        'doberman', 'dodo', 'dog', 'dolphin', 'donkey', 'dormouse', 'dotterel', 'dove',
                        'dovekie', 'dragon', 'dragonfly', 'drongo', 'drum', 'duck', 'dugong', 'dunlin',
                        'dunnock', 'eagle', 'earthworm', 'earwig', 'echidna', 'eel', 'egret', 'eider',
                        'eland', 'elephant', 'elk', 'elver', 'emu', 'enhydra', 'ermine',
                        'falcon', 'ferret', 'finch', 'firefly', 'fish', 'flamingo', 'flatfish', 'flea',
                        'flicker', 'fly', 'flycatcher', 'flyingfish', 'fossa', 'fox', 'frigatebird',
                        'frog', 'fulmar', 'galago', 'gallinule', 'gander', 'gar', 'garpike',
                        'gaur', 'gazelle', 'gecko', 'gelada', 'gerbil', 'gharial', 'gibbon', 'giraffe',
                        'glaucous', 'gnat', 'gnatcatcher', 'gnu', 'goat', 'goatfish', 'goby', 'goldeneye',
                        'goldfinch', 'goldfish', 'goosander', 'goose', 'goosefish', 'gopher', 'gorilla',
                        'goshawk', 'grackle', 'grasshopper', 'grayling', 'greenfinch', 'greenshank',
                        'grouse', 'grub', 'guan', 'guanaco', 'guenon', 'gull', 'guppy', 'haddock',
                        'halcyon', 'halibut', 'hamster', 'hare', 'harrier', 'hartebeest', 'hawk',
                        'hedgehog', 'heron', 'herring', 'hippopotamus', 'honeyeater', 'hookworm', 'hoopoe',
                        'hornbill', 'hornet', 'horse', 'horsefly', 'hound', 'housefly', 'hoverfly',
                        'human', 'hummingbird', 'hyena', 'ibex', 'ibis', 'ichneumon', 'iguana', 'impala',
                        'indigo', 'indris', 'insect', 'jackal', 'jackrabbit', 'jaguar', 'jaguarundi',
                        'jay', 'jellyfish', 'jennet', 'jerboa', 'junglefowl', 'kagu', 'kakapo', 'kangaroo',
                        'karakul', 'keeshond', 'kelpie', 'kennet', 'kentish', 'kestrel', 'killdeer',
                        'kingbird', 'kingfisher', 'koala', 'koi', 'dragon', 'kookaburra', 'kouprey',
                        'kudu', 'labrador', 'lapwing', 'lark', 'lemming', 'lemur', 'leopard', 'limpet',
                        'linnet', 'lion', 'lionfish', 'lizard', 'llama', 'lobster', 'locust', 'loon',
                        'loris', 'louse', 'lynx', 'lyrebird', 'macaque', 'macaw', 'mackerel', 'magpie',
                        'mallard', 'mammal', 'mammoth', 'manatee', 'mandrill', 'ray', 'mantis', 'marlin',
                        'marmoset', 'marten', 'mastiff', 'mayfly', 'meadowlark', 'meerkat', 'millipede',
                        'mink', 'minnow', 'mockingbird', 'mole', 'mongoose', 'mongrel', 'monkey', 'moorhen',
                        'moose', 'moray', 'mosquito', 'moth', 'mouflon', 'mouse',
                        'mousebird', 'mudskipper', 'mule', 'narwhal', 'nase', 'newfoundland', 'newt',
                        'nightcrawler', 'nightfish', 'nightingale', 'nuthatch', 'nyala', 'oakworm',
                        'ocelot', 'octopus', 'okapi', 'olm', 'opossum', 'orangutan', 'oriole', 'osprey',
                        'ostrich', 'otter', 'ouzel', 'ovenbird', 'owl', 'ox', 'oxpecker', 'oyster', 'paca',
                        'packrat', 'pademelon', 'panda', 'panther', 'parakeet', 'parrot', 'parrotfish',
                        'partridge', 'peacock', 'peafowl', 'peccary', 'pelican', 'penguin', 'perch',
                        'pheasant', 'pig', 'pigeon', 'pika', 'pike', 'pilchard', 'pinniped', 'piranha',
                        'plankton', 'platyfish', 'platypus', 'plover', 'polecat', 'polliwog',
                        'pony', 'pooch', 'poodle', 'porcupine', 'porgy', 'porpoise', 'possum', 'potto',
                        'prawn', 'pufferfish', 'puffin', 'puma', 'quail', 'quelea', 'quetzal', 'quokka',
                        'quoll', 'rabbit', 'raccoon', 'ragworm', 'rail', 'ram', 'rat', 'ratfish',
                        'rattlesnake', 'raven', 'reindeer', 'reptile', 'rhino', 'rhinoceros', 'robin',
                        'rockfish', 'rodent', 'roller', 'rook', 'rooster', 'rottweiler', 'sable',
                        'salamander', 'salmon', 'dollar', 'sandpiper', 'sardine', 'scallop', 'scarab',
                        'scorpion', 'seagull', 'seahawk', 'seahorse', 'seal', 'serpent', 'setter', 'shark',
                        'shearwater', 'sheep', 'shelduck', 'shrew', 'shrimp', 'siamang', 'siamese',
                        'silverfish', 'skate', 'skimmer', 'skink', 'skipjack', 'skunk', 'sloth', 'slug',
                        'snail', 'snake', 'snapper', 'sparrow', 'spider', 'spoonbill',
                        'springbok', 'squid', 'squirrel', 'starfish', 'starling', 'stingray', 'stinkbug',
                        'stoat', 'stork', 'sunfish', 'swallow', 'swan', 'tamarin', 'tanager', 'tapeworm',
                        'tapir', 'tarantula', 'tarpon', 'tarsier', 'teal', 'termite', 'tetra', 'tiger',
                        'tigerfish', 'toad', 'toucan', 'trout', 'tuna', 'turbot', 'turkey', 'turtle',
                        'uakari', 'uguisu', 'urchin', 'vulture', 'wallaby', 'walleye',
                        'walrus', 'warbler', 'warthog', 'wasp', 'weasel', 'whale', 'whippet', 'whitefish',
                        'wildcat', 'wildebeest', 'wolf', 'wombat', 'woodchuck', 'woodcock', 'woodpecker',
                        'worm', 'wrasse', 'wren', 'yabby', 'yak', 'yellowjacket', 'zebra', 'zebu', 'zonkey',
                        'zooplankton']
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
            "Egbert", "Aethelwulf", "Aethelbald", "Aethelbert", "Aethelred", "Ethelred", "Alfred", "Æthelred",
            "Edward", "Aethelstan", "Edmund", "Eadred", "Eadwig", "Edgar", "Edward", "Harold", "William",
            "Henry", "Stephen", "Matilda", "Richard", "John", "Henry", "Edward", "Mary", "Elizabeth", "James",
            "Charles", "Oliver", "Richard", "Anne", "George", "Victoria", "Edward", "George", "Elizabeth"
        ]
        return list_of_monarchs
