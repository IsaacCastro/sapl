from django.conf.urls import url

from .apps import AppConfig
from .views import (RedirecionaAtasList, RedirecionaComissao,
                    RedirecionaComposicaoComissao,
                    RedirecionaHistoricoTramitacoesList,
                    RedirecionaMateriaLegislativaDetail,
                    RedirecionaMateriaLegislativaList,
                    RedirecionaMateriasPorAnoAutorTipo,
                    RedirecionaMateriasPorAutor, RedirecionaMesaDiretoraView,
                    RedirecionaNormasJuridicasDetail,
                    RedirecionaNormasJuridicasList,
                    RedirecionaNormasJuridicasTextoIntegral,
                    RedirecionaParlamentar, RedirecionaPautaSessao,
                    RedirecionaPresencaParlamentares,
                    RedirecionaRelatoriosList,
                    RedirecionaRelatoriosMateriasEmTramitacaoList,
                    RedirecionaSAPLIndex, RedirecionaSessaoPlenaria)

app_name = AppConfig.name
urlpatterns = [
    url(r'^default_index_html$',
        RedirecionaSAPLIndex.as_view(),
        name='redireciona_sapl_index'),
    url(r'^consultas/parlamentar/parlamentar_',
        RedirecionaParlamentar.as_view(),
        name='redireciona_parlamentar'),
    url(r'^consultas/comissao/comissao_',
        RedirecionaComissao.as_view(),
        name='redireciona_comissao'),
    url(r'^consultas/comissao/composicao/composicao_index_html',
        RedirecionaComposicaoComissao.as_view(),
        name='redireciona_composicaio_comissao'),
    url(r'^consultas/pauta_sessao/pauta_sessao_',
        RedirecionaPautaSessao.as_view(),
        name='redireciona_pauta_sessao_'),
    url(r'^consultas/mesa_diretora/mesa_diretora_index_html',
        RedirecionaMesaDiretoraView.as_view(),
        name='redireciona_mesa_diretora'),
    url(r'^consultas/mesa_diretora/parlamentar/parlamentar_',
        RedirecionaParlamentar.as_view(),
        name='redireciona_mesa_diretora_parlamentar'),
    url(r'^consultas/sessao_plenaria/',
        RedirecionaSessaoPlenaria.as_view(),
        name='redireciona_sessao_plenaria_'),
    url(r'^generico/norma_juridica_pesquisar_',
        RedirecionaNormasJuridicasList.as_view(),
        name='redireciona_norma_juridica_pesquisa'),
    url(r'^consultas/norma_juridica/norma_juridica_mostrar_proc',
        RedirecionaNormasJuridicasDetail.as_view(),
        name='redireciona_norma_juridica_detail'),
    url(r'^sapl_documentos/norma_juridica/(?P<norma_id>[0-9]+)_texto_integral',
        RedirecionaNormasJuridicasTextoIntegral.as_view(),
        name='redireciona_norma_juridica_texto_integral'),
    url(r'^relatorios_administrativos/relatorios_administrativos_index_html$',
        RedirecionaRelatoriosList.as_view(),
        name='redireciona_relatorios_list'),
    url(r'tramitacaoMaterias/tramitacaoMaterias',
        RedirecionaRelatoriosMateriasEmTramitacaoList.as_view(),
        name='redireciona_relatorio_materia_por_tramitacao'),
    url(r'tramitacaoMaterias/materia_mostrar_proc$',
        RedirecionaMateriaLegislativaDetail.as_view(),
        name='redireciona_materialegislativa_detail_tramitacao'),
    url(r'consultas/materia/materia_mostrar_proc$',
        RedirecionaMateriaLegislativaDetail.as_view(),
        name='redireciona_materialegislativa_detail'),
    url(r'^generico/materia_pesquisar_',
        RedirecionaMateriaLegislativaList.as_view(),
        name='redireciona_materialegislativa_list'),
    url(r'historicoTramitacoes/historicoTramitacoes',
        RedirecionaHistoricoTramitacoesList.as_view(),
        name='redireciona_historico_tramitacoes'),
    url(r'atasSessao',
        RedirecionaAtasList.as_view(),
        name='redireciona_atas_list'),
    url(r'presencaSessao',
        RedirecionaPresencaParlamentares.as_view(),
        name='redireciona_presencaparlamentar_list'),
    url(r'resumoPropositurasAutor',
        RedirecionaMateriasPorAutor.as_view(),
        name='redireciona_materias_por_autor_list'),
    url(r'propositurasAnoAutorTipo',
        RedirecionaMateriasPorAnoAutorTipo.as_view(),
        name='redireciona_materia_por_ano_autor_tipo_list'),
]