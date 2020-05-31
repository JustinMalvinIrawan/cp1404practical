import wikipedia


def main():
    title = input("Please enter the title you want to search")
    page = wikipedia.page(title)
    print(page.title)
    print(page.summary)
    print(page.url)
    while title != "":
        try:
            title = input("Please enter the title you want to search")
            page = wikipedia.page(title)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)



main()
