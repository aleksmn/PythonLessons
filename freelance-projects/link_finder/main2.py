def write_links_to_file(links: list, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("\n".join(links))

def get_links_from_file(path):
    links_cleared = []
    with open(path, 'r', encoding='utf-8') as f:
        links = f.readlines()
    for line in links:
        links_cleared.append(line.replace('!', '').strip())
    return links_cleared



links1 = get_links_from_file('file1.txt')
links2 = get_links_from_file('file2.txt')

matched = set(links1).intersection(set(links2))
not_matched = set(links1).symmetric_difference(set(links2))

print(matched)
print(not_matched)

write_links_to_file(matched, "matched.txt")
write_links_to_file(not_matched, "not_matched.txt")