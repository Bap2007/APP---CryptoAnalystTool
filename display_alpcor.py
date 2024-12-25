def display_letter_indices():
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    indices = list(range(26))
    
    print("| Lettre | Index | Lettre | Index | Lettre | Index | Lettre | Index | Lettre | Index | Lettre | Index |")
    print("|--------|-------|--------|-------|--------|-------|--------|-------|--------|-------|--------|-------|")
    for i in range(0, 26, 5):
        row = "".join(f"| {alphabet[j]:<6} | {indices[j]:<5} " for j in range(i, min(i + 5, 26)))
        print(row + "|")

# Appel de la fonction pour afficher le tableau
display_letter_indices()