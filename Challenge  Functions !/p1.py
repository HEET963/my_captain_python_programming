def most_frequent(str):
    frequency = {}

    
    for x in str:
        if x.isalpha():
            x = x.lower()
            frequency[x] = frequency.get(x, 0) + 1

    
    sorted_frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: item[1], reverse=True)}

    
    for x, frequency in sorted_frequency.items():
        print(f"{x}: {frequency}")



str = "Mississippi"
print("Letter frequencies in the input string:")
most_frequent(str)
