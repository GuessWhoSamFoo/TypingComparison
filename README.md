# TypingComparison

This is a first attempt at comparing gesture typing on a QWERTY vs DVORAK layout on a stock Google Android keyboard.

The idea originated from reading about how to consistently type over 100+wpm. DVORAK layout seems to be the quick answer. However on mobile devices where gesture typing using one finger is more common, the benefits are not as clear.

The center from each key is on a 720x1280 resolution screen was mapped to assign_layout.py

main.py calculates the total distance in px needed by user input for a list of 10000 most frequent words.

Although the scatter plot does show DVORAK has an advantage in the sense of requiring less movement to input words, it is not clear that this is a meaning comparison at words with 10+ letters as the frequency is much lower.

# Resources

https://github.com/first20hours/google-10000-english

https://www.nayuki.io/page/i-type-in-dvorak
