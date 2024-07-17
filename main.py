def main():
    text = get_boot_text()
    lowered_string = text.lower()   
    words = text.split() 
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    sorted_list = []
    for ch in chars:
        sorted_list.append({"char": ch, "num": chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(len(words), "words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_boot_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def sort_on(d):
    return d["num"]

main()