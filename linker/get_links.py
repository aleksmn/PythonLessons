
def get_links() -> str:

    links = ''

    while True:
        link_input = input("Введите ссылку:\n").strip()

        if link_input == '':
            break

        links += '\n' + link_input

    links = links.strip()


    return links


if __name__ == "__main__":
    print(get_links())