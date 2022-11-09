import sys

from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


# Requisito 12
def actions(option, user_data=None):
    functions = [
        get_tech_news,
        search_by_title,
        search_by_date,
        search_by_tag,
        search_by_category,
        top_5_news,
        top_5_categories,
    ]
    if option == 0:
        return functions[option](int(user_data))
    return functions[option](user_data)


def choose_action(option):
    messages = {
        0: "Digite quantas notícias serão buscadas: ",
        1: "Digite o título: ",
        2: "Digite a data no formato aaaa-mm-dd: ",
        3: "Digite a tag: ",
        4: "Digite a categoria: ",
    }
    user_data = ""

    if option == 7:
        print("Encerrando script")
    elif option == 0:
        user_data = input(messages[option])
        actions(option, user_data)
    elif option in [5, 6]:
        result = actions(option)
        sys.stdout.write(str(result))
    else:
        user_data = input(messages[option])
        result = actions(option, user_data)
        sys.stdout.write(str(result))


def analyzer_menu():
    menu = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """

    try:
        option = int(input(menu))
        choose_action(option)
    except (KeyError, ValueError):
        sys.stderr.write("Opção inválida\n")
