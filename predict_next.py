import numpy as np

def predict_next_number(numbers):
    """
    Προβλέπει τον επόμενο αριθμό μιας ακολουθίας με γραμμική παλινδρόμηση.
    numbers: λίστα από αριθμούς (int ή float)
    επιστρέφει: predicted_next (float)
    """
    n = len(numbers)
    if n < 2:
        raise ValueError("Χρειάζονται τουλάχιστον 2 αριθμοί για πρόβλεψη.")
    
    # Δημιουργία των x: 0, 1, 2, ..., n-1
    x = np.arange(n)
    y = np.array(numbers)
    
    # Υπολογισμός συντελεστών γραμμής (κλίση a, τεταγμένη b)
    # y = a*x + b
    a, b = np.polyfit(x, y, 1)
    
    # Πρόβλεψη για το επόμενο x = n
    next_x = n
    prediction = a * next_x + b
    return prediction

def main():
    print("=== Πρόγραμμα πρόβλεψης επόμενου αριθμού ===")
    print("Δώσε μια ακολουθία αριθμών χωρισμένους με κόμμα ή κενό (π.χ. 1,2,3,4 ή 1 2 3 4)")
    user_input = input("Αριθμοί: ")
    
    # Αντικατάσταση κόμματος με κενό και διάσπαση
    user_input = user_input.replace(',', ' ')
    parts = user_input.split()
    
    try:
        numbers = [float(part) for part in parts]
    except ValueError:
        print("Λάθος: Βεβαιώσου ότι δίνεις μόνο αριθμούς.")
        return
    
    if len(numbers) < 2:
        print("Λάθος: Δώσε τουλάχιστον 2 αριθμούς για να γίνει πρόβλεψη.")
        return
    
    try:
        next_num = predict_next_number(numbers)
        print(f"\nΑκολουθία: {numbers}")
        print(f"Πρόβλεψη επόμενου αριθμού: {next_num:.4f}")
    except Exception as e:
        print(f"Σφάλμα: {e}")

if __name__ == "__main__":
    main()