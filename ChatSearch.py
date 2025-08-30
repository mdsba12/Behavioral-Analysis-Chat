def search_chat(file_path, search_terms):
    matches = {term.lower(): [] for term in search_terms}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for term in search_terms:
                if term.lower() in line.lower():
                    matches[term.lower()].append(line.strip())

    for term, occurrences in matches.items():
        print(f"\n--- Matches for '{term}' ---")
        print(f"Total: {len(occurrences)}\n")
        for occ in occurrences:
            print(occ)

if __name__ == "__main__":
    file_path = "export.txt"
    search_terms = ["specific word"]
    search_chat(file_path, search_terms)
