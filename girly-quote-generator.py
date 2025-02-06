import random

def girly_quote_generator():
    quotes = [
        "I'm a girly girl",
        "Always say yes to lipstick"
        "Think girly, act girly",
        "Be happy, be girly"
    ]

    return random.choice(quotes)

if __name__ == "__main__":
    print(girly_quote_generator()) 