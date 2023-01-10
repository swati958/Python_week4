with open('index.html','r') as webpage:
    with open('output.txt','a') as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quote = line.find('\"',pos)
                second_quote = line.find('\"',first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(url+ '\n')