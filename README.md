🔁 Array Search & Replace in Python
This project demonstrates how to use Python's built-in array module to search for a value in an array and replace it with a new one based on user input.
📌 Description
The script:
- Initializes an array of integers using array.array
- Prompts the user to enter a value to search for
- Replaces the found value with a new one
- Displays the original and modified array
- Handles cases where the value is not found
🧪 Example:
arr = array.array('i', [1, 2, 3, 4, 5])
# User inputs:
#   search_value = 3
#   new_value = 99
# Output:
#   Value 3 found at index 2
#   Modified array: array('i', [1, 2, 99, 4, 5])


🚀 How to Run:
- Make sure Python is installed on your system.
- Clone this repository:
git clone https://github.com/your-username/array-search-replace.git
cd array-search-replace
- Run the script:
python array_search_replace.py


📂 File Structure
array-search-replace/
├── array_search_replace.py
└── README.md


🛠️ Requirements
- Python 3.x
- No external libraries required
🙌 Contributing
Feel free to fork the repo, improve the code, or add new features like:
- Support for other data types
- Multiple replacements
- GUI interface

