import inspect
import json
import os
import re
import time
from datetime import datetime


class AgenteJuridicoConformidade:
    """
    Avalia se o conteúdo pode ir ao ar ou não antes da publicação:
    - Exige criação original própria (sem copiar terceiros)
    - Protege dados e tokens/credenciais do titular
    - Evita difamação, calúnia, ofensas a terceiros reais ou incitação à violência
    - Preserva o valor das palavras sagradas, o respeito bíblico e o tom educativo
    """

    TERMOS_EXPOSICAO_DADOS = [
        r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",
        r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b",
        r"\b(senha|api_key|chave privada|cartao de credito|cartão de crédito)\b",
    ]

    TERMOS_ATAQUE_TERCEIROS = [
        r"\b(calunia|calúnia|difamacao|difamação|ameaca|ameaça|linchar|expor endereco|expor endereço)\b",
    ]

    TERMOS_SENSACIONALISMO_INDEVIDO = [
        r"\b(data exata do fim do mundo|adivinho o futuro|garantia de dinheiro facil|garantia de dinheiro fácil)\b",
    ]

    def avaliar(self, pacote_conteudo: dict) -> dict:
        motivos = []
        status = "APROVADO"

        texto_completo = " ".join([
            pacote_conteudo.get("titulo", ""),
            pacote_conteudo.get("roteiro_resumo", ""),
            pacote_conteudo.get("mensagem_biblica", ""),
            pacote_conteudo.get("legenda_postagem", ""),
        ]).strip()

        if not pacote_conteudo.get("criacao_propria", False):
            status = "BLOQUEADO"
            motivos.append("Conteúdo não marcado como criação original própria.")

        for padrao in self.TERMOS_EXPOSICAO_DADOS:
            if re.search(padrao, texto_completo, flags=re.IGNORECASE):
                status = "BLOQUEADO"
                motivos.append("Risco de exposição de dados pessoais ou credenciais do titular.")
                break

        for padrao in self.TERMOS_ATAQUE_TERCEIROS:
            if re.search(padrao, texto_completo, flags=re.IGNORECASE):
                status = "BLOQUEADO"
                motivos.append("Risco jurídico: possível ofensa, difamação ou violação de direitos de terceiros.")
                break

        for padrao in self.TERMOS_SENSACIONALISMO_INDEVIDO:
            if re.search(padrao, texto_completo, flags=re.IGNORECASE):
                if status != "BLOQUEADO":
                    status = "REVISAO_HUMANA"
                motivos.append("Aviso doutrinário/jurídico: manter firmeza bíblica sem sensacionalismo indevido.")

        if not pacote_conteudo.get("referencias_biblicas"):
            if status != "BLOQUEADO":
                status = "REVISAO_HUMANA"
            motivos.append("Informar as referências bíblicas utilizadas.")

        if not motivos:
            motivos.append(
                "Aprovado: criação própria, valor das palavras sagradas preservado, "
                "proteção ao titular e conformidade legal."
            )

        return {
            "status": status,
            "avaliado_em": datetime.now().isoformat(timespec="seconds"),
            "motivos": motivos,
        }


class GeradorHistoriaSemFim:
    """
    Gera episódios contínuos baseados em fatos reais do cotidiano ou perguntas do público,
    trabalhando Curiosidade, Empatia, Justiça (respeito pelos mais velhos), Nostalgia e Superação,
    junto ao valor da Bíblia e das palavras sagradas, hábito constante e volta de Cristo.
    """

    PILARES_FACEBOOK = {
        "Curiosidade": "Despertar atenção com situações reais do dia a dia.",
        "Empatia": "Usar empatia e valores familiares para gerar identificação.",
        "Justica": "Despertar senso de justiça e respeito pelos mais velhos.",
        "Nostalgia": "Resgatar lembranças e raízes que despertam emoção genuína.",
        "Superacao": "Entregar superação, esperança e desfecho construtivo.",
    }

    ESCALA_VALOR_PALAVRAS_SAGRADAS = {
        "1_a_3_vezes_sem_habito": (
            "Apenas olhar ou abrir de vez em quando sem constância não cria raiz profunda "
            "nem transforma o rumo do dia a dia."
        ),
        "4_a_5_dias_com_dedicacao": (
            "Quando a pessoa se dedica de verdade quatro, cinco dias ou mais, a vida começa "
            "a mudar, brigas e desconfianças perdem força e a fidelidade abre portas."
        ),
        "habito_firme_e_luz": (
            "Quando as palavras sagradas viram hábito firme e constante, iluminam como luz, "
            "ensinam a ouvir e dão palavra e firmeza para falar da verdade de Deus."
        ),
    }

    CATALOGO_EPISODIOS = [
        {
            "titulo": "O Valor da Bíblia e das Palavras Sagradas: Quando a Luz Entra na Vida",
            "origem": "Fato real, valor das palavras sagradas e hábito constante vs. confusão do dia a dia",
            "cenario_real": "Comércio de bairro, rua e casa da família",
            "referencias_biblicas": [
                "Josué 1:8 (Meditar na Palavra com constância e fidelidade)",
                "Salmos 119:105 (As palavras sagradas como lâmpada e luz para o caminho)",
                "Tiago 1:19 (Parar para ouvir com calma e evitar confusão precipitada)",
                "Mateus 24 (Sinais dos tempos, arrependimento e volta de Cristo)",
                "Gênesis 6–7 (Noé), Gênesis 5:22-24 (Enoque) e 1 Reis 18 (Elias)"
            ],
            "roteiro_resumo": (
                "Mostra o valor real da Bíblia e das palavras sagradas deixadas por Deus e por Cristo "
                "através dos profetas e escolhidos: abrir uma, duas ou três vezes sem constância não cria "
                "raiz, mas dedicar-se quatro ou cinco dias até virar hábito ilumina a família, reduz "
                "confusão, ensina a ouvir e aponta para o arrependimento e a volta de Cristo."
            ),
            "mensagem_biblica": (
                "As palavras sagradas da Bíblia têm imenso valor quando deixam de ser leitura passageira "
                "e viram hábito constante, luz na vida diária e chamado ao arrependimento diante da volta de Cristo."
            ),
            "cenas": [
                {
                    "cena": 1,
                    "pilar": "Curiosidade",
                    "duracao_seg": 15,
                    "movimento": "Dois personagens discutem no comércio enquanto um terceiro para, ouve com calma e chama atenção para o que está por trás da briga.",
                    "fala": "Por que tanta discussão sem ouvir? Parar e buscar o sentido real muda a conversa."
                },
                {
                    "cena": 2,
                    "pilar": "Justica",
                    "duracao_seg": 15,
                    "movimento": "Um morador mais velho entra na cena com firmeza respeitosa, pede respeito mútuo e lembra o valor de honrar quem veio antes.",
                    "fala": "Justiça e respeito pelos mais velhos mantêm a ordem onde a pressa só causa estrago."
                },
                {
                    "cena": 3,
                    "pilar": "Empatia e Nostalgia",
                    "duracao_seg": 20,
                    "movimento": "Na casa da família, as gerações se reúnem à mesa, fazem oração e abrem as palavras sagradas com constância.",
                    "fala": "Abrir a Bíblia uma, duas ou três vezes sem constância não firma a raiz; mas de quatro a cinco dias e virando hábito, a luz aparece."
                },
                {
                    "cena": 4,
                    "pilar": "Superacao",
                    "duracao_seg": 20,
                    "movimento": "Cristo surge com firmeza e compaixão, apontando para o arrependimento, a volta do Senhor e o exemplo de Noé, Enoque e Elias.",
                    "fala": "Cristo está voltando: arrependam-se, façam das palavras sagradas hábito firme e sigam para os próximos capítulos em primeira mão."
                }
            ],
            "legenda_postagem": (
                "Qual é o verdadeiro valor da Bíblia quando você deixa de olhar só de passagem e faz das "
                "palavras sagradas um hábito vivo? Acompanhe essa história sem fim e siga a página para "
                "receber os próximos capítulos em primeira mão."
            )
        }
    ]

    PERGUNTAS_PUBLICO_PADRAO = [
        "Qual é o verdadeiro valor da Bíblia quando ela vira hábito e não apenas leitura de vez em quando?",
        "Por que tantas famílias perdem a paciência e entram em confusão por motivos pequenos?",
        "Como ensinar a oração, as palavras sagradas e o respeito pelos mais velhos hoje em dia?",
        "O que a Bíblia diz sobre arrependimento e a volta de Cristo nos dias atuais?"
    ]

    def gerar_episodio(self, numero_episodio: int, pergunta_publico: str | None = None) -> dict:
        base = self.CATALOGO_EPISODIOS[(numero_episodio - 1) % len(self.CATALOGO_EPISODIOS)].copy()
        base["episodio"] = numero_episodio
        base["criacao_propria"] = True
        base["pilares_facebook"] = self.PILARES_FACEBOOK
        base["escala_valor_palavras_sagradas"] = self.ESCALA_VALOR_PALAVRAS_SAGRADAS

        if pergunta_publico:
            base["origem"] = f"Pergunta do público: {pergunta_publico}"
            base["titulo"] = f"Ep. {numero_episodio} — {pergunta_publico}"

        return base

    def preparar_proximo_ciclo(self, episodio_atual: int) -> dict:
        proximo_num = episodio_atual + 1
        pergunta = self.PERGUNTAS_PUBLICO_PADRAO[(episodio_atual - 1) % len(self.PERGUNTAS_PUBLICO_PADRAO)]
        return self.gerar_episodio(proximo_num, pergunta_publico=pergunta)


class MotorProducaoVideoReal:
    """
    Estrutura de produção real para transformar cada cena em comando/job de vídeo em movimento
    e voz/narração quando conectado a um motor/API externo na nuvem (via variáveis de ambiente).
    Não grava chaves nem tokens em arquivos de log.
    """

    VAR_API_VIDEO = "API_VIDEO_KEY"
    VAR_API_VOZ = "API_VOZ_KEY"

    def __init__(self):
        self._chave_video_configurada = bool((os.getenv(self.VAR_API_VIDEO) or "").strip())
        self._chave_voz_configurada = bool((os.getenv(self.VAR_API_VOZ) or "").strip())

    def montar_jobs_cenas(self, episodio: dict, decisao_juridica: dict) -> dict:
        if decisao_juridica["status"] != "APROVADO":
            return {
                "status_producao": "BLOQUEADO_PELO_AGENTE_JURIDICO",
                "chave_video_configurada": self._chave_video_configurada,
                "chave_voz_configurada": self._chave_voz_configurada,
                "jobs_cenas": [],
            }

        jobs = []
        for cena in episodio["cenas"]:
            jobs.append({
                "episodio": episodio["episodio"],
                "cena": cena["cena"],
                "pilar": cena["pilar"],
                "duracao_seg": cena["duracao_seg"],
                "cenario": episodio["cenario_real"],
                "prompt_movimento_atuacao": (
                    f"Cena realista em movimento no cenário '{episodio['cenario_real']}': "
                    f"{cena['movimento']} Expressões naturais, postura humana e continuidade visual."
                ),
                "texto_fala_voz": cena["fala"],
                "formato_video": "1080x1920",
                "estado_execucao": (
                    "PRONTO_PARA_ENVIAR_API_REAL"
                    if (self._chave_video_configurada and self._chave_voz_configurada)
                    else "ENFILEIRADO_AGUARDANDO_CHAVES_VIDEO_E_VOZ"
                ),
            })

        # >>> PONTO EXATO DE INTEGRACAO COM MOTOR DE VIDEO E VOZ NA NUVEM <<<
        # Quando você configurar API_VIDEO_KEY e API_VOZ_KEY no ambiente da nuvem,
        # este bloco pode chamar o serviço real de geração de vídeo/voz para cada item em `jobs`.

        return {
            "status_producao": (
                "PRONTO_PARA_RENDERIZACAO_REAL"
                if (self._chave_video_configurada and self._chave_voz_configurada)
                else "MODO_PREPARACAO_DE_JOBS_SEM_CHAVES_EXTERNAS"
            ),
            "chave_video_configurada": self._chave_video_configurada,
            "chave_voz_configurada": self._chave_voz_configurada,
            "total_jobs": len(jobs),
            "jobs_cenas": jobs,
        }

    def salvar_fila_producao(self, producao: dict, arquivo_fila: str = "fila_producao_video.json") -> str:
        historico = []
        if os.path.exists(arquivo_fila):
            with open(arquivo_fila, "r", encoding="utf-8") as f:
                try:
                    historico = json.load(f)
                except json.JSONDecodeError:
                    historico = []
        historico.append({
            "registrado_em": datetime.now().isoformat(timespec="seconds"),
            "producao": producao,
        })
        with open(arquivo_fila, "w", encoding="utf-8") as f:
            json.dump(historico, f, ensure_ascii=False, indent=2)
        return os.path.abspath(arquivo_fila)


class TresAgentesOperacionais:
    NOME_VARIAVEL_TOKEN = "TOKEN_PUBLICACAO"

    def __init__(self):
        self._token_em_memoria = os.getenv(self.NOME_VARIAVEL_TOKEN)
        self._origem_token = "VARIAVEL_AMBIENTE" if self._token_em_memoria else "NENHUMA"

    def agente_distribuicao(self, episodio: dict, decisao_juridica: dict) -> dict:
        if decisao_juridica["status"] != "APROVADO":
            return {
                "acao": "BLOQUEADO_PELO_AGENTE_JURIDICO",
                "motivos": decisao_juridica["motivos"],
                "token_disponivel": bool(self._token_em_memoria),
                "origem_token": self._origem_token,
            }

        token_ok = bool(self._token_em_memoria and self._token_em_memoria.strip())
        return {
            "acao": "VALIDACAO_OK_MODO_TESTE_SEM_POSTAR",
            "token_disponivel": token_ok,
            "origem_token": self._origem_token,
            "titulo_sugerido": f"{episodio['titulo']} | Siga Para Receber em Primeira Mão",
            "meta_acompanhamento": "40.000 a 50.000 seguidores",
        }

    def agente_logs(self, registro: dict, arquivo_log: str = "log_historia_sem_fim.json") -> str:
        registro_seguro = json.loads(json.dumps(registro))
        if "distribuicao" in registro_seguro:
            registro_seguro["distribuicao"].pop("token", None)
            registro_seguro["distribuicao"].pop("token_publicacao", None)

        historico = []
        if os.path.exists(arquivo_log):
            with open(arquivo_log, "r", encoding="utf-8") as f:
                try:
                    historico = json.load(f)
                except json.JSONDecodeError:
                    historico = []
        historico.append(registro_seguro)
        with open(arquivo_log, "w", encoding="utf-8") as f:
            json.dump(historico, f, ensure_ascii=False, indent=2)
        return os.path.abspath(arquivo_log)


def mostrar_funcao_python(nome_funcao: str = "executar_teste_python") -> None:
    """
    Exibe diretamente no terminal o código-fonte em Python da função escolhida.
    """
    mapa_funcoes = {
        "executar_teste_python": executar_teste_python,
        "montar_jobs_cenas": MotorProducaoVideoReal.montar_jobs_cenas,
        "gerar_episodio": GeradorHistoriaSemFim.gerar_episodio,
        "avaliar": AgenteJuridicoConformidade.avaliar,
        "agente_distribuicao": TresAgentesOperacionais.agente_distribuicao,
    }
    alvo = mapa_funcoes.get(nome_funcao)
    print(f"\n--- CÓDIGO PYTHON DA FUNÇÃO: {nome_funcao} ---")
    if alvo is None:
        print(f"Função '{nome_funcao}' não encontrada. Disponíveis: {', '.join(mapa_funcoes.keys())}")
        return
    print(inspect.getsource(alvo))
    print("--- FIM DO CÓDIGO PYTHON ---\n")


def executar_teste_python(quantidade_ciclos: int = 1, passo_a_passo_seg: float = 0.0, exibir_funcao: bool = False) -> None:
    """
    Executa o teste em Python puro no Prompt de Comando mostrando movimento, fala,
    pilares, preparação dos jobs de vídeo/voz, validação jurídica e registro em log.
    """
    gerador = GeradorHistoriaSemFim()
    motor_video = MotorProducaoVideoReal()
    agentes = TresAgentesOperacionais()
    juridico = AgenteJuridicoConformidade()

    for ep in range(1, quantidade_ciclos + 1):
        episodio = gerador.gerar_episodio(ep)
        decisao = juridico.avaliar(episodio)
        producao = motor_video.montar_jobs_cenas(episodio, decisao)
        distribuicao = agentes.agente_distribuicao(episodio, decisao)
        proxima = gerador.preparar_proximo_ciclo(ep)

        print(f"\n================ EPISÓDIO {ep} (PYTHON PURO) ================")
        print(f"Título : {episodio['titulo']}")
        print(f"Cenário: {episodio['cenario_real']}")
        print(f"Jurídico: {decisao['status']} | Distribuição: {distribuicao['acao']}")
        print(f"Produção Vídeo/Voz: {producao['status_producao']} ({producao['total_jobs']} cenas/jobs)")

        for cena in episodio["cenas"]:
            print(f"\n  [Cena {cena['cena']} | Pilar: {cena['pilar']} | {cena['duracao_seg']}s]")
            print(f"  Movimento/Ação: {cena['movimento']}")
            print(f"  Fala          : \"{cena['fala']}\"")
            if passo_a_passo_seg > 0:
                time.sleep(passo_a_passo_seg)

        caminho_fila = motor_video.salvar_fila_producao(producao)
        registro = {
            "episodio": ep,
            "executado_em": datetime.now().isoformat(timespec="seconds"),
            "titulo": episodio["titulo"],
            "decisao_juridica": decisao,
            "producao_video_voz": {
                "status_producao": producao["status_producao"],
                "total_jobs": producao["total_jobs"],
                "chave_video_configurada": producao["chave_video_configurada"],
                "chave_voz_configurada": producao["chave_voz_configurada"],
                "arquivo_fila": caminho_fila,
            },
            "distribuicao": distribuicao,
            "proximo_episodio_gerado": {
                "episodio": proxima["episodio"],
                "titulo": proxima["titulo"],
            },
        }
        caminho_log = agentes.agente_logs(registro)
        print(f"\nPróximo episódio preparado: Ep. {proxima['episodio']} — {proxima['titulo']}")
        print(f"Fila de produção salva em: {caminho_fila}")
        print(f"Log salvo em: {caminho_log}")

    if exibir_funcao:
        mostrar_funcao_python("executar_teste_python")


if __name__ == "__main__":
    executar_teste_python(quantidade_ciclos=1, passo_a_passo_seg=0.0, exibir_funcao=True)