from .models import Filme

def lista_filmes_recentes(requests):
    lista_filmes_recentes = Filme.objects.order_by('-data_criacao')[0:8]
    if lista_filmes_recentes:
        filme_destaque = lista_filmes_recentes[0]
    else:
        filme_destaque = None
    return {'lista_filmes_recentes': lista_filmes_recentes, 'filme_destaque': filme_destaque}


def lista_filmes_emalta(requests):
    lista_filmes_emalta = Filme.objects.order_by('-visualizacoes')[0:8]
    return {'lista_filmes_emalta': lista_filmes_emalta}