from performance_test import run_test

# Instance files:
I_random = "random.txt"
I_high_first = "high-first-not-enough-later.txt"
I_cheaper_later = "high-first-cheaper-later.txt"
I_const_hotel = "constant-hotel-price.txt"
I_0dot8_ratio_adversary = "ratio-0dot8-adversary.txt"

if __name__ == '__main__':
    # run_test(I_random)
    run_test(I_0dot8_ratio_adversary)

    # run_test(I_cheaper_later)
