marks = {
    "Rayyan": 100,
    "Sumit" : 101,
    "Parth" : 75
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Sumit":99})
# print(marks)

# print(marks.get("Rayyan2")) # Prints NONE
# print(marks["Rayyan2"]) # Run Error

marks.pop("Parth") # Removes the selected item form the dictionary
print(marks)
