import wikipediaapi

def get_article(article):

    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(article)
    print(page_py)

    # check if the page exists
    page_py = wiki_wiki.page(article)
    print("Page - Exists: %s" % page_py.exists())

    if(not page_py.exists()):
        txt = "The page does not exists. Try something else"
        return txt

    # Else get full page sections
    sections = page_py.sections
    level = 0
    for s in sections:
        print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
        print_sections(s.sections, level + 1)

    return str(page_py.sections[0])

def print_sections(sections, level=0):
        for s in sections:
                print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
                print_sections(s.sections, level + 1)
