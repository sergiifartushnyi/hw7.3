def second_index(search_string, substring):
    if not search_string or not substring:
        return None

    first_index = search_string.find(substring)
    if first_index == -1:
        return None

    second_index = search_string.find(substring, first_index + len(substring))

    return second_index if second_index != -1 else None

print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello, hello", "lo"))
print('ok')