def title_case(title, minor_words=None):
    t = title.capitalize().split()
    array = []
    if minor_words:
        m = minor_words.lower().split()
        for i in t:
            if i not in m:
                array.append(i.title())
            else:
                array.append(i)
        return ' '.join(array)
    else:
        return title.title()
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('ola i michal'))



