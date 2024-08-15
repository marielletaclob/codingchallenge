def number_to_words(num):
    if num == 0:
        return "Zero"

    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    def wordify(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 11]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            return ones[n // 100] + " Hundred" + (" " + wordify(n % 100) if n % 100 != 0 else "")

    thousands = ["", " Thousand"]
    result = ""
    thousand_counter = 0

    while num > 0:
        part = num % 1000
        if part > 0:
            result = wordify(part) + thousands[thousand_counter] + (" " if result else "") + result
        num //= 1000
        thousand_counter += 1

    return result

# Main loop
while True:
    num = input("Enter an uninterrupted number without spaces or commas, or 'q' to quit): ")

    if num.lower() == 'q':
        print("Exiting program. Adieu!")
        break

    if num.isdigit() and 0 <= int(num) < 1000000:
        print("Your number is:", number_to_words(int(num)))
    else:
        print("Invalid input! Please enter a number with up to 6 digits.")
