def last_occurrence_index(string, substring):
    index = string.rfind(substring)
    return index

# Example usage:
main_string = "hello world hello"
substring = "world"
index = last_occurrence_index(main_string, substring)
print("Index of last occurrence:", index)
