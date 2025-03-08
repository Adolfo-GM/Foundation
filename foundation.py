import math
import random
import time
import string

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

class Terminal():
    def __init__(self):
        pass

    def clear(self):
        '''Clears the terminal screen'''
        print("\033[H\033[J")
    
    def clear_terminal(self):
        '''Clears the terminal screen'''
        print("\033[H\033[J")

    def render_array(self, array):
        ''' Renders a 2D array to the terminal '''
        for line in array:
            print(line)
    
    def update(self, arr):
        """Clears terminal and redraws the array"""
        self.clear()  
        self.render(arr)

    def render(self, ascii):
        ''' Renders ASCII art to the terminal '''
        print(ascii)

def random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
        "When something is important enough, you do it even if the odds are not in your favor. - Elon Musk",
        "To be, or not to be, that is the question. - William Shakespeare",
        "Imagination is more important than knowledge. - Albert Einstein",
        "The best way to predict the future is to invent it. - Alan Kay",
        "The journey is the reward. - Steve Jobs",
        "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
        "I have a dream. - Martin Luther King Jr.",
        "To conquer oneself is a greater victory than to conquer thousands in a battle. - Buddha",
        "This world shall know pain - Nagato",
        "Swear not by the moon, the inconstant moon - William Shakespeare",
        "To confuse the enemy, we must first confuse ourselves - Sun Tzu",
        "Courage needs not be remembered, for it is never forgotten - Zelda",
        "Do not go gentle into that good night. Rage, rage against the dying of the light. - Dylan Thomas",
        "The unexamined life is not worth living. - Socrates",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "What we think, we become. - Buddha",
        "He who has a why to live can bear almost any how. - Friedrich Nietzsche",
        "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "A journey of a thousand miles begins with a single step. - Lao Tzu",
        "Time is what we want most, but what we use worst. - William Penn",
        "We do not remember days, we remember moments. - Cesare Pavese",
        "The secret of getting ahead is getting started. - Mark Twain",
        "Be yourself; everyone else is already taken. - Oscar Wilde",
        "It is never too late to be what you might have been. - George Eliot",
        "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill",
        "Knowing others is intelligence; knowing yourself is true wisdom. Mastering others is strength; mastering yourself is true power. - Lao Tzu",
        "The only way to deal with this life meaningfully is to find one's passion and follow it. - Henry David Thoreau",
        "Love all, trust a few, do wrong to none. - William Shakespeare",
        "There is nothing either good or bad, but thinking makes it so. - William Shakespeare",
        "To thine own self be true, and it must follow, as the night the day, thou canst not then be false to any man. - William Shakespeare",
        "All the world's a stage, and all the men and women merely players. - William Shakespeare",
        "We are such stuff as dreams are made on, and our little life is rounded with a sleep. - William Shakespeare",
        "Tis better to have loved and lost than never to have loved at all. - Alfred Lord Tennyson",
        "Injustice anywhere is a threat to justice everywhere. - Martin Luther King Jr.",
        "You must be the change you wish to see in the world. - Mahatma Gandhi",
        "It is not the mountain we conquer, but ourselves. - Edmund Hillary",
        "A man is but the product of his thoughts. What he thinks, he becomes. - Mahatma Gandhi",
        "Our lives begin to end the day we become silent about things that matter. - Martin Luther King Jr.",
        "Those who dare to fail miserably can achieve greatly. - John F. Kennedy",
        "An eye for an eye makes the whole world blind. - Mahatma Gandhi",
        "Give me liberty, or give me death! - Patrick Henry",
        "He who is not courageous enough to take risks will accomplish nothing in life. - Muhammad Ali",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
        "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "You miss 100% of the shots you don’t take. - Wayne Gretzky",
        "It always seems impossible until it’s done. - Nelson Mandela",
        "The best revenge is massive success. - Frank Sinatra",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "The harder you work for something, the greater you’ll feel when you achieve it. - Anonymous",
        "A person who never made a mistake never tried anything new. - Albert Einstein",
        "Never let the fear of striking out keep you from playing the game. - Babe Ruth",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. - Ralph Waldo Emerson",
        "Don't cry because it's over, smile because it happened. - Dr. Seuss",
        "It is better to be hated for what you are than to be loved for what you are not. - André Gide",
        "Those who are crazy enough to think they can change the world, are the ones who do. - Steve Jobs",
        "To be great is to be misunderstood. - Ralph Waldo Emerson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
        "Life is either a daring adventure or nothing at all. - Helen Keller",
        "We may encounter many defeats, but we must not be defeated. - Maya Angelou",
        "That which does not kill us makes us stronger. - Friedrich Nietzsche",
        "Nothing in the world can take the place of Persistence. Talent will not; nothing is more common than unsuccessful men with talent. - Calvin Coolidge",
        "If you can dream it, you can do it. - Walt Disney",
        "A fool thinks himself to be wise, but a wise man knows himself to be a fool. - William Shakespeare",
        "The supreme art of war is to subdue the enemy without fighting. - Sun Tzu",
        "All warfare is based on deception. - Sun Tzu",
        "Opportunities multiply as they are seized. - Sun Tzu",
        "The greatest victory is that which requires no battle. - Sun Tzu",
        "If you know the enemy and know yourself, you need not fear the result of a hundred battles. - Sun Tzu",
        "In the midst of chaos, there is also opportunity. - Sun Tzu",
        "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win. - Sun Tzu",
        "Appear weak when you are strong, and strong when you are weak. - Sun Tzu",
        "You cannot swim for new horizons until you have courage to lose sight of the shore. - William Faulkner",
        "Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi",
        "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
        "The journey of a thousand miles begins with one step. - Lao Tzu",
        "Act as if what you do makes a difference. It does. - William James",
        "Great minds discuss ideas; average minds discuss events; small minds discuss people. - Eleanor Roosevelt",
        "To live a creative life, we must lose our fear of being wrong. - Joseph Chilton Pearce",
        "Strive not to be a success, but rather to be of value. - Albert Einstein",
        "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
        "We must let go of the life we have planned, so as to accept the one that is waiting for us. - Joseph Campbell",
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "The future belongs to those who prepare for it today. - Malcolm X",
        "You want to wake up in the morning and think the future is going to be great, and that’s what being a spacefaring civilization is all about. It’s about believing in the future and thinking that the future will be better than the past. And I can’t think of anything more exciting than going out there and being among the stars. -Elon Musk",
    ]
    return random.choice(quotes)

class TicTacToe:
    '''This class implements a console-based Tic-Tac-Toe game with an AI that plays optimally using the minimax algorithm.'''

    def __init__(self, player='X'):
        '''Initializes the game with an empty board and sets the player character.'''
        self.board = [' ' for _ in range(9)]
        self.human_player = player
        self.ai_player = 'O' if player == 'X' else 'X'
        self.current_player = 'X'

    def print_board(self):
        '''Displays the current state of the board in a human-readable format.'''
        print(f"\n{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}\n")

    def is_winner(self, board, player):
        '''Checks if a given player has won on the provided board.'''
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

    def is_full(self, board):
        '''Checks if the board is full.'''
        return ' ' not in board

    def minimax(self, board, depth, is_maximizing):
        '''The minimax algorithm for AI decision-making, evaluating hypothetical boards.'''
        if self.is_winner(board, self.ai_player):
            return 10 - depth
        if self.is_winner(board, self.human_player):
            return -10 + depth
        if self.is_full(board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.ai_player
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.human_player
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(best_score, score)
            return best_score

    def best_move(self):
        '''Calculates the best move for the AI using the minimax algorithm.'''
        best_score = float('-inf')
        move = -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.ai_player
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def get_best_move(self, board, ai_player='O', human_player='X'):
        '''Method to return the best move for the AI given a board state.'''
        self.ai_player = ai_player
        self.human_player = human_player
        temp_board = board.copy()
        best_score = float('-inf')
        move = -1
        for i in range(9):
            if temp_board[i] == ' ':
                temp_board[i] = ai_player
                score = self.minimax(temp_board, 0, False)
                temp_board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def play_move(self, position):
        '''Marks the board with the current player's move.'''
        if 0 <= position < 9 and self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        '''Switches the current player.'''
        self.current_player = self.ai_player if self.current_player == self.human_player else self.human_player

    def play_game(self):
        '''Handles the game loop where the player and AI take turns.'''
        self.print_board()
        while not self.is_full(self.board):
            if self.current_player == self.ai_player:
                print("AI's turn...")
                move = self.best_move()
                self.play_move(move)
            else:
                try:
                    move = int(input(f"Your turn ({self.human_player}). Enter a position (0-8): "))
                    if not self.play_move(move):
                        print("Invalid move. Try again.")
                        continue
                except (ValueError, IndexError):
                    print("Enter a number between 0 and 8. Try again.")
                    continue

            self.print_board()
            if self.is_winner(self.board, self.ai_player):
                print("AI wins!")
                return
            if self.is_winner(self.board, self.human_player):
                print("You win!")
                return
            self.switch_player()
        print("It's a draw!")

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation  
    return ''.join(random.choice(characters) for _ in range(length))

def distance(x1, y1, x2, y2):
    '''Returns the distance between two coordinates'''
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def midpoint(x1, y1, x2, y2):
    '''Returns the midpoint between two coordinates'''
    return ((x1 + x2) / 2, (y1 + y2) / 2)

class Printer:
    class Colors:
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        RESET = '\033[0m'
        YELLOW_GREEN = '\033[38;5;118m'

    def log(self, text, color="lime"):
        if color.lower() == "red":
            print(f"{self.Colors.RED}{text}{self.Colors.RESET}")
        elif color.lower() == "green":
            print(f"{self.Colors.GREEN}{text}{self.Colors.RESET}")
        elif color.lower() == "yellow":
            print(f"{self.Colors.YELLOW}{text}{self.Colors.RESET}")
        elif color.lower() == "blue":
            print(f"{self.Colors.BLUE}{text}{self.Colors.RESET}")
        elif color.lower() == "purple":
            print(f"{self.Colors.PURPLE}{text}{self.Colors.RESET}")
        elif color.lower() == "cyan":
            print(f"{self.Colors.CYAN}{text}{self.Colors.RESET}")
        elif color.lower() == "white":
            print(f"{self.Colors.WHITE}{text}{self.Colors.RESET}")
        elif color.lower() == "lime":
            print(f"{self.Colors.YELLOW_GREEN}{text}{self.Colors.RESET}")
        else:
            print(text) 

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

    terminal = Terminal()
    array = [
        "_|___|___|___|___|___|",
        "___|___|___|___|___|__",
        "_|___|___|___|___|___|",
        "___|___|___|___|___|__",
        "_|___|___|___|___|___|",
    ]
    terminal.render_array(array)
    ascii = '''
⠀⣤⣤⣤⣤⣤⣤⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⣤⣤⣤⣤⣤⣤⠀
⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠀
⠀⠛⠛⠛⠛⠛⠛⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠛⠛⠛⠛⠛⠛⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣉⣉⣉⣉⣉⣉⠉⣉⣉⣉⣉⣉⣉⣁⣈⣉⣉⣉⣉⣉⣉⠉⣉⣉⣉⣉⣉⣉⠀
⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠀
⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀
    '''
    terminal.render(ascii)
    print(generate_password(12))
    print(random_quote())
    print("Distance:", distance(0, 0, 3, 4))
    print("Midpoint:", midpoint(0, 0, 3, 4))
    printer = Printer()
    printer.log("Hello, World!", "green")
    printer.log("Hello, World!", "red")
    printer.log("Hello, World!", "blue")

    tic_tac_toe = TicTacToe() 
    current_board = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '] 
    best_move = tic_tac_toe.get_best_move(current_board, ai_player='O', human_player='X')
    print(f"AI's best move: {best_move}") 

    