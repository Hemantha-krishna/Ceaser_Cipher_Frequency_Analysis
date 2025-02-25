Decrypt the ciphertext C by using the φ(i) correlation model explained in detail below.

Following lists the monogram English statistics where p(c) represents the frequency of character c in English texts.

c	p(c)	c	p(c)	c	p(c)	c	p(c)

Figure 1. Monogram English Statistics.
Let φ(i) be the correlation of the frequency of each letter in the ciphertext with the character frequencies in English obtained from Figure 1. Let f(c) be the frequency of character c (expressed as a fraction). The formula for the correlation for each ciphertext (with all arithmetic being mod 26) is

φ(i) = Σ0 ≤ c ≤ 25 f(c) x p(c – i)
where f(c) is the ciphertext character frequency and p(c-i) is obtained from Figure 1. This correlation φ(i) should be a maximum when the key k translates the ciphertext into
English. Trying the most likely key first, i.e. the i value that yields the largest φ(i), we obtain plaintext alternatives. Out of these, the alternative that is a meaningful English text is decided to be the plaintext.

As an example, assume that ciphertext “KHOOR ZRUOG” is given. To solve it using the φ(i) model, we first compute the frequency (as a fraction) of each letter in the ciphertext as follows:
G	0.1
H	0.1
K	0.1
O	0.3
R	0.2
U	0.1
Z	0.1

where ciphertext frequencies sum up to 1.0. Then, we compute φ(i) as follows:

φ(i) = Σ0 ≤ c ≤ 25 f(c) x p(c – i) = 0.1 x p(6 – i) + 0.1 x p(7 – i) + 0.1 x p(10 – i) + 0.3 x p(14 – i) +
0.2 x p(17 – i) + 0.1 x p(20 – i) + 0.1p(25 – i)

For example, for i=0, the φ(i) is computed as:

φ(0) = 0.1 x p(6) + 0.1 x p(7) + 0.1 x p(10) + 0.3 x p(14) + 0.2 x p(17) + 0.1 x p(20) + 0.1 x p(25)
= 0.1 x 0.015 + 0.1 x 0.06 + 0.1 x 0.005 + 0.3 x 0.08 + 0.2 x 0.065 + 0.1 x 0.03 + 0.1 x 0.002
= 0.0482

Therefore, we obtain the table below:

Figure 2. The value of φ(i) for 0 ≤ i ≤ 25


The most likely keys (represented as i) that yield the largest φ(i) value are highlighted in Figure 2: They are 6, 10, 3, and 14 in decreasing order of φ(i) value.


Trying the most likely key first, we obtain as plaintext “EBIIL TLOIA” when i = 6, “AXEEH PHKEW” when i = 10, “HELLO WORLD” when i = 3, and “WTAAD LDGAS” when i = 14. The statistics indicated that the key was most likely 6, when in fact the correct key was 3. So the attacker must test the results. The statistics simply reduce the number of trials in most cases. Only three trials were needed.
