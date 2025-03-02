import foundation

LLM = foundation.LLM()
text = 'The quick brown fox jumps over the lazy dog'
print(LLM.NextWord(text, 'quick'))  
print(LLM.PreviousWord(text, 'quick'))


Dice = foundation.Dice()
print(Dice.roll(6))

