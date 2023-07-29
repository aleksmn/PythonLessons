def read_links_from_file(filename):
    with open(filename, 'r') as file:
        links = set(file.read().splitlines())
    return links

def write_links_to_file(links, filename):
    with open(filename, 'w') as file:
        file.write("\n".join(links))

def find_matching_links(file1_links, file2_links):
    matching_links = set()
    non_matching_links = set()

    for link in file1_links:
        if link in file2_links or link.rstrip('!') in file2_links:
            matching_links.add(link)
        else:
            non_matching_links.add(link)

    for link in file2_links:
        if link not in file1_links and link.rstrip('!') not in file1_links:
            non_matching_links.add(link)

    return matching_links, non_matching_links

if __name__ == "__main__":
    file1_links = read_links_from_file("file1.txt")
    file2_links = read_links_from_file("file2.txt")

    matching_links, non_matching_links = find_matching_links(file1_links, file2_links)

    write_links_to_file(matching_links, "совпадающие ссылки.txt")
    write_links_to_file(non_matching_links, "несовпадающие ссылки.txt")