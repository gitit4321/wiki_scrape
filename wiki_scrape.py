import wikipedia
from wikipedia import exceptions

def get_wiki_summary(query):
    print('from wiki_scrape', query)
    try:
        result = wikipedia.summary(f'{query}')
        # print(result, '\n')
        # print("(If this wasn't your expected result, please revise your search query and be more specific.)")
        return f"{result} (If this wasn't your expected result, please revise your search query and be more specific.)"

    except exceptions.DisambiguationError as e:
        output = "We're sorry, your query was too vague. Here is a list of the top 5 closest results... "

        for i in range(len(e.options[:5])):
            if i != 0:
                output += ', '
            output += f"{e.options[i]}"
        # output += "\\n\\n"

        output += "... If you see your desired query in the list above, use it exactly as it appears in place of your previous query. If you don't see your desired query, please revise your search and be more specific."
        # print(output)
        return output

    except exceptions.PageError as e:
        output = 'This search yielded inconclusive results. Please revise your search and be more specific.'
        return output

