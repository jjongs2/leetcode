UNITS = {
    2: "Hundred",
    3: "Thousand",
    6: "Million",
    9: "Billion",
}

UNDER_20 = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}

TENS = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def token_to_words(token, words):
            hundred, digit_00 = token // 100, token % 100
            if digit_00 in UNDER_20:
                words.append(UNDER_20[digit_00])
            elif digit_00 != 0:
                ten, digit_0 = digit_00 // 10, digit_00 % 10
                if digit_0 > 0:
                    words.append(UNDER_20[digit_0])
                words.append(TENS[ten])
            if hundred > 0:
                words.append(UNITS[2])
                words.append(UNDER_20[hundred])

        words = []
        exp = 0
        while num > 0:
            if (token := num % 1000) > 0:
                if exp in UNITS:
                    words.append(UNITS[exp])
                token_to_words(token, words)
            exp += 3
            num //= 1000
        return " ".join(reversed(words))
