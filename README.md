# Numbers to Words Converter

## Description
This Python script converts a number (up to 6 digits) into its English word representation. For example, if you input `54321`, it will output `Fifty Four Thousand Three Hundred Twenty One`. The script also allows the user to keep entering numbers until they decide to quit.

## Requirements
- Python 3.x

## Installation

1. **Clone or download the repository:**

   If you have Git installed, you can clone the repository using the following command:
   ```bash
   git clone <repository_url>
   ```
Alternatively, download the repository as a ZIP file and extract it.

2. **Install Python**
Ensure Python 3.x is installed. You can download it from:
https://www.python.org/

3. **Navigate to the project directory:**
```bash
    cd path/to/your/project/directory
```
## Usage
1. **Run the script:**
```bash
python numbers_to_words.py
```
2. **Input a number:**
Enter a number with no more than 6 digits, uninterrupted by spaces or commas.

3.**Example:**
```bash
Enter an uninterrupted number without spaces or commas, or 'q' to quit): 54321
Your number is: Fifty Four Thousand Three Hundred Twenty One
```
4. **Exit the program:**
Type q to quit the program.

## Challenges

**1. Handling Different Number Ranges:**
One of the main challenges was converting numbers into words for a range from `0` to `999,999`. This required managing different ranges of numbers, like units, teens, tens, and hundreds, and combining them appropriately. I tackled this by creating `helper functions` to handle smaller chunks of the number, and then assembled these chunks together to form the final word representation.

**2. Managing Thousand Separators:**
Another challenge was correctly formatting numbers in the thousands. I had to ensure that the word representation for thousands (e.g., “Thousand”) was correctly applied only when necessary and combined with the rest of the number's words. I used an `array` to handle these thousand separators and iterated through chunks of the number to build the final result.

**3. User Input Validation:**
Validating user input to ensure it was a valid number within the specified range (0 to 999,999) and properly handling unexpected inputs like non-numeric characters or extra spaces was another key challenge. I solved this by checking the input with Python’s `string methods` and handling `edge cases` to ensure smooth operation.

## Highlights

**1. `wordify` Function:**
I’m particularly proud of the `wordify` function. It efficiently breaks down numbers into units, teens, and tens, and constructs their word equivalents. This function encapsulates much of the logic required to convert numbers into readable words and does so in a clear, modular way.

**2. Main Loop:**
The main loop is another highlight. It continuously prompts the user for input, processes the number, and provides a clear and friendly output. The loop also gracefully handles invalid inputs and provides instructions for correct usage, making the program more user-friendly.

**3. Handling Large Numbers:**
The way the program handles large numbers up to 999,999 and formats them correctly in words is something I’m proud of. It demonstrates effective use of string operations and logical checks to ensure accurate and clear output.

## Defects

**1. Non-Numeric Input Handling:**
The current implementation might not handle non-numeric characters as gracefully as it could. While it checks for digits, there are no advanced error handling or user guidance for completely invalid input formats.

**2. Input Size Limitation:**
The program is strictly limited to numbers up to 6 digits. If a user enters a number outside this range or includes invalid characters, the program will not process it correctly and might give misleading error messages.

**3. Edge Cases:**
There are a few edge cases where the formatting might not be perfect. For instance, numbers that are exactly on the boundary of thousands might not always be formatted as cleanly as possible, depending on the complexity of the number.

**4. Language and Localization:**
The program only supports English. If there was a need to support multiple languages or regional formats, additional localization would be necessary, which is not currently in place.

## Limitations

**1. Fixed Range of Input:**
The program is designed for numbers up to 999,999. Any number outside this range will not be processed correctly, and the program lacks flexibility to handle larger numbers or different formats.

**2. Lack of Advanced Error Handling:**
The program’s error handling for invalid inputs is basic. It primarily checks if the input is numeric and within range but does not handle more complex cases such as malformed input strings or unexpected characters.

**3. No User Customization:**
The program does not offer customization options for output format or language. All outputs are in a fixed format, which might not suit all user needs or preferences.

## Author
***Marielle Taclob*** |
Email: marielletaclob2@gmail.com

