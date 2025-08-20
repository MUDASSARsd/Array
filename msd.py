import array
arr = array.array('i', [1, 2, 3, 4, 5])
print("Original array:", arr)

search_value = int(input("enter a num"))
new_value = int(input("enter a num"))


found = False
for i in range(len(arr)):
    if arr[i] == search_value:
        print(f"Value {search_value} found at index {i}")
        arr[i] = new_value
        found = True
        break

if not found:
    print(f"Value {search_value} not found in array.")


print("Modified array:", arr)