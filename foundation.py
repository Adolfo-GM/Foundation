import math
import random
import time

def current_time():
    '''
    Returns the current time in HH:MM:SS format
    '''
    return time.strftime('%H:%M:%S')

def current_date():
    '''
    Returns the current date in YYYY-MM-DD format
    '''
    return time.strftime('%Y-%m-%d')

def hour():
    '''
    Returns the current hour
    '''
    return int(time.strftime('%H'))

def minute():
    '''
    Returns the current minute
    '''
    return int(time.strftime('%M'))

def second():
    '''
    Returns the current second
    '''
    return int(time.strftime('%S'))

def year():
    '''
    Returns the current year
    '''
    return int(time.strftime('%Y'))

def month():
    '''
    Returns the current month
    '''
    return int(time.strftime('%m'))

def day():
    '''
    Returns the current day
    '''
    return int(time.strftime('%d'))

def weekday():
    '''
    Returns the current weekday (0 = Monday, 6 = Sunday)
    '''
    return int(time.strftime('%w'))

def weekday_text():
    '''
    Returns the current weekday as text
    '''
    return time.strftime('%A')

def month_text():
    '''
    Returns the current month as text
    '''
    return time.strftime('%B')

def millisecond():
    '''
    Returns the current milisecond
    '''
    return int((time.time() * 1000) % 1000)

class LLM:
    '''
    Lightweight Language Model with basic text manipulation and generation
    '''
    def __init__(self):
        self.name = 'LLM'

    def _split_text(self, text):
        """Helper to split text into words, handling edge cases."""
        if not isinstance(text, str) or not text.strip():
            return []
        return text.split()

    def NextWord(self, text, word):
        """Returns the word after the given word, or None if not found or last."""
        words = self._split_text(text)
        for i in range(len(words) - 1):
            if words[i] == word:
                return words[i + 1]
        return None

    def PreviousWord(self, text, word):
        """Returns the word before the given word, or None if not found or first."""
        words = self._split_text(text)
        for i in range(1, len(words)):
            if words[i] == word:
                return words[i - 1]
        return None

    def RandomWord(self, text):
        """Returns a random word from the text, or None if text is empty."""
        words = self._split_text(text)
        return random.choice(words) if words else None

    def GenerateText(self, text, length, start_word=None):
        """
        Generates text of specified length using a simple Markov-like approach.
        If start_word is None, picks a random word to begin.
        """
        words = self._split_text(text)
        if not words or length <= 0:
            return ""

        transitions = {}
        for i in range(len(words) - 1):
            current = words[i]
            next_word = words[i + 1]
            if current not in transitions:
                transitions[current] = []
            transitions[current].append(next_word)

        if start_word is None or start_word not in words:
            current = random.choice(words)
        else:
            current = start_word

        result = [current]
        for _ in range(length - 1):
            if current in transitions and transitions[current]:
                current = random.choice(transitions[current])
            else:
                current = random.choice(words)
            result.append(current)
        return " ".join(result)

def pi():
    '''Returns the value of pi'''
    return math.pi

def e():
    '''Returns the value of e'''
    return math.e

class Dice:
    '''
    Dice Rolling Simulator
    '''
    def __init__(self):
        self.name = 'Dice'

    def roll(self, sides):
        """Rolls a die with the given number of sides."""
        if not isinstance(sides, int) or sides < 1:
            raise ValueError("Sides must be a positive integer")
        return random.randint(1, sides)

class ImageGenerator:
    '''
    Simple ASCII art generator using Perlin noise concepts
    '''
    def __init__(self):
        self.palette = {
            "cloudy": " .:-=+*#%@",
            "forest": " .^~|T#%@",
            "desert": " .:~-+=*#",
            "default": " .:-=+*#%@"
        }

    def fade(self, t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(self, a, b, t):
        return a + t * (b - a)

    def grad(self, hash_val, x, y):
        h = hash_val & 15
        u = x if h < 8 else y
        v = y if h < 4 else x
        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

    def perlin_noise(self, width, height, scale=10):
        """Generates a 2D noise map using a simplified Perlin noise algorithm."""
        p = list(range(256))
        random.shuffle(p)
        p = p * 2  
        noise = []
        for y in range(height):
            row = []
            for x in range(width):
                X = int(x / scale)
                Y = int(y / scale)
                xf = (x / scale) - X
                yf = (y / scale) - Y
                u = self.fade(xf)
                v = self.fade(yf)
                aa = p[p[X] + Y]
                ab = p[p[X] + Y + 1]
                ba = p[p[X + 1] + Y]
                bb = p[p[X + 1] + Y + 1]
                x1 = self.lerp(self.grad(aa, xf, yf), self.grad(ba, xf - 1, yf), u)
                x2 = self.lerp(self.grad(ab, xf, yf - 1), self.grad(bb, xf - 1, yf - 1), u)
                value = self.lerp(x1, x2, v)
                row.append(value)
            noise.append(row)
        return noise

    def generate_ascii(self, width=40, height=20, prompt="default"):
        """Generates ASCII art based on noise and a prompt."""
        if prompt not in self.palette:
            prompt = "default"
        chars = self.palette[prompt]
        noise = self.perlin_noise(width, height)
        output = []
        for y in range(height):
            row = ""
            for x in range(width):
                value = (noise[y][x] + 1) / 2  
                idx = int(value * (len(chars) - 1))
                row += chars[idx]
            output.append(row)
        return "\n".join(output)

class Secret:
    '''
    Real randomness number generator
    '''
    def __init__(self):
        pass

    def real_random_number(self, a, b):
     '''Returns a real random number between a and b'''
     if a > b:
        a, b = b, a

     current_time = time.time()
     milliseconds = int(current_time * 1000) % 1000
     seconds = int(current_time) % 60
     minutes = (int(current_time) // 60) % 60

     random_change = (milliseconds + seconds + minutes) % (b - a)

     secret = random.uniform(a, b) + (random_change / 1000.0)

     return secret
    
    def roll(self, sides):
        """Rolls a die with the given number of sides."""
        result = self.real_random_number(1, sides)
        return round(result)



if __name__ == '__main__':
    print("Current Time:", current_time())
    print("Current Date:", current_date())
   
    ai = LLM()
    text = "Hello my name is LLM and I like to code"
    print("Next word after 'name':", ai.NextWord(text, "name"))
    print("Previous word before 'name':", ai.PreviousWord(text, "name"))
    print("Random word:", ai.RandomWord(text))
    print("Generated text:", ai.GenerateText(text, 5, "Hello"))
   
    print("Pi:", pi())
    print("Dice roll (6 sides):", Dice().roll(6))
    print("E:", e())
   
    generator = ImageGenerator()
    print("\nCloudy ASCII Art:")
    print(generator.generate_ascii(prompt="cloudy"))
    print(weekday_text())
    print(month_text())

    secret = Secret()
    print("Real Random Number:", secret.real_random_number(0, 1000))
    print(secret.roll(6))