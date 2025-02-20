english_freq = {
    'a': 0.080, 'b': 0.015, 'c': 0.030, 'd': 0.040, 'e': 0.130,
    'f': 0.020, 'g': 0.015, 'h': 0.060, 'i': 0.065, 'j': 0.005,
    'k': 0.005, 'l': 0.035, 'm': 0.030, 'n': 0.070, 'o': 0.080,
    'p': 0.020, 'q': 0.002, 'r': 0.065, 's': 0.060, 't': 0.090,
    'u': 0.030, 'v': 0.010, 'w': 0.015, 'x': 0.005, 'y': 0.020,
    'z': 0.002
}

ciphertext = "TEBKFKQEBZLROPBLCERJXKBSBKQP"
ciphertext = ciphertext.lower()

# Computing ciphertext letter frequencies
ciphertext_freq = {}
total_letters = len(ciphertext)

for letter in ciphertext:
    if letter in ciphertext_freq:
        ciphertext_freq[letter] += 1
    else:
        ciphertext_freq[letter] = 1

# Converting counts to fractions
for letter in ciphertext_freq:
    ciphertext_freq[letter] /= total_letters

# Computing φ(i) for each shift
def compute_phi(shift):
    phi = 0.0
    for c in ciphertext_freq:
        plaintext_letter = chr(((ord(c) - ord('a') - shift) % 26) + ord('a'))
        if plaintext_letter in english_freq:
            phi += ciphertext_freq[c] * english_freq[plaintext_letter]
    return phi

# Computing φ(i) for all shifts
phi_values = []
for shift in range(26):
    phi = compute_phi(shift)
    phi_values.append((shift, phi))

#Finding the shift with the highest φ(i)
best_shift, best_phi = max(phi_values, key=lambda x: x[1])

#Decrypting the ciphertext using the best shift
def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for c in ciphertext:
        if c in english_freq:  
            plaintext += chr(((ord(c) - ord('a') - shift) % 26) + ord('a'))
        else:
            plaintext += c  
    return plaintext

plaintext = decrypt_caesar(ciphertext, best_shift)

# Results
print("φ(i) values for all shifts:")
for shift, phi in phi_values:
    print(f"Shift = {shift:2d}, φ(i) = {phi:.4f}")

print(f"\nBest shift: {best_shift} (φ(i) = {best_phi:.4f})")
print(f"Decrypted plaintext: {plaintext}")