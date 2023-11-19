from random import choice

title = [
    "{adjective} Estratégias para {verb} seu {noun}",
    "O Poder do {noun} na Era {adjective}",
    "Como {verb} seu {noun} de Forma {adjective}",
    "{adjective} Dicas para {verb} um {noun} Bem-Sucedido",
    "Explorando Novas Fronteiras: {adjective} {noun}",
    "{verb} {adjective}: O Segredo do {noun} de Sucesso",
    "Desmistificando {adjective} {noun} para Iniciantes",
    "A Arte de {verb} seu {noun} com {adjective}",
    "{adjective} Maneiras de {verb} um {noun}",
    "{noun} 101: {adjective} Estratégias para {verb}",
    "Como {verb} seu {noun} de Maneira {adjective}",
    "{adjective} {noun} para Transformar sua Vida",
    "Desvendando os Mistérios de {adjective} {noun}",
    "{verb} para o Futuro: {adjective} {noun}",
    "{adjective} Estratégias para {verb} seu {noun} Diariamente",
    "{noun} Sob uma Nova Perspectiva: {adjective} Abordagens",
    "{verb} com Paixão: Transformando seu {noun} de Forma {adjective}",
    "A Jornada de {adjective} {noun}: {verb} e Desafios",
    "Como {verb} um {noun} de Maneira {adjective}",
    "{adjective} {noun}: {verb} para o Sucesso",
    "{verb} e {adjective}: A Fórmula do {noun} Ideal",
    "O Poder do {noun} {adjective}: {verb} para a Excelência",
    "{adjective} Estratégias para {verb} seu {noun} com Facilidade",
    "{verb} seu {noun} com {adjective} Determinação",
    "{adjective} {noun} para {verb} um Futuro Brilhante",
    "A Ciência por Trás de {adjective} {noun}: Como {verb} com Eficiência",
    "{adjective} Maneiras de {verb} seu {noun} a Cada Dia",
    "{noun} de Sucesso: {adjective} Estratégias para {verb}",
    "Transforme seu {noun} com {adjective} {verb}",
    "{verb} com Propósito: Desenvolvendo seu {adjective} {noun}",
    "{adjective} {noun}: A Arte de {verb} com Maestria",
    "{verb} seu {noun} de Forma {adjective} e Inovadora",
    "Os Segredos de {adjective} {noun}: Como {verb} com Sucesso",
    "{verb} para o Futuro: {adjective} Estratégias para {noun}",
    "{adjective} Maneiras de {verb} um {noun} Desafiador",
    "Explorando Novos Horizontes: {verb} seu {noun} de Forma {adjective}",
    "{noun} de Alta Performance: {adjective} Estratégias para {verb}",
    "Como {verb} seu {noun} com {adjective} Excelência",
    "{adjective} {noun} para {verb} um Futuro de Sucesso",
    "Desvendando os Mistérios de {adjective} {noun}: {verb} com Maestria",
    "{verb} seu {noun} com {adjective} Paixão",
    "{adjective} {noun} para {verb} seu {noun} de Maneira {adjective}",
    "{verb} com Eficiência: {adjective} Estratégias para {noun}",
    "{adjective} {noun}: A Chave para {verb} com Sucesso",
    "{verb} seu {noun} com {adjective} Determinação e Foco",
    "{adjective} {noun} para {verb} um Futuro Brilhante",
    "{verb} com Maestria: {adjective} Estratégias para {noun}",
    "{adjective} {noun} para {verb} com Excelência",
    "{verb} seu {noun} de Forma {adjective}: O Caminho para o Sucesso",
    "{adjective} Maneiras de {verb} seu {noun} de Maneira {adjective}",
    "{verb} seu {noun} com {adjective} Paixão e Dedicação",
    "{adjective} {noun} para {verb} um Futuro de Realizações",
    "Desmistificando {adjective} {noun}: Como {verb} com Facilidade",
    "{verb} seu {noun} com {adjective} Determinação e Foco",
    "{adjective} {noun} para {verb} seu {noun} de Forma {adjective}",
    "{verb} com Paixão: {adjective} Estratégias para {noun}",
    "{adjective} {noun}: {verb} para o Sucesso",
    "{verb} seu {noun} com {adjective} Sabedoria",
    "{adjective} {noun} para {verb} um Futuro Brilhante",
    "{verb} seu {noun} com {adjective} Excelência",
    "{adjective} Estratégias para {verb} seu {noun} de Forma {adjective}",
    "{noun} Sob uma Nova Perspectiva: {adjective} Abordagens",
    "{verb} com Determinação: Transformando seu {adjective} {noun}",
    "{adjective} {noun}: {verb} para o Sucesso",
    "{verb} e {adjective}: A Fórmula do {noun} Ideal",
    "O Poder do {noun} {adjective}: {verb} para a Excelência",
    "{adjective} Estratégias para {verb} seu {noun} com Facilidade",
    "{verb} seu {noun} com {adjective} Determinação",
    "{adjective} {noun} para {verb} um Futuro Brilhante",
    "A Ciência por Trás de {adjective} {noun}: Como {verb} com Eficiência",
    "{adjective} Maneiras de {verb} seu {noun} a Cada Dia",
    "{noun} de Sucesso: {adjective} Estratégias para {verb}",
    "Transforme seu {noun} com {adjective} {verb}",
    "{verb} com Propósito: Desenvolvendo seu {adjective} {noun}",
    "{adjective} {noun}: A Arte de {verb} com Maestria",
    "{verb} seu {noun} de Forma {adjective} e Inovadora",
    "Os Segredos de {adjective} {noun}: Como {verb} com Sucesso",
    "{verb} para o Futuro: {adjective} Estratégias para {noun}",
    "{adjective} Maneiras de {verb} um {noun} Desafiador",
    "Explorando Novos Horizontes: {verb} seu {noun} de Forma {adjective}",
    "{noun} de Alta Performance: {adjective} Estratégias para {verb}",
    "Como {verb} seu {noun} com {adjective} Excelência",
    "{adjective} {noun} para {verb} um Futuro de Sucesso",
    "Desvendando os Mistérios de {adjective} {noun}",
    "{verb} seu {noun} com {adjective} Paixão",
    "{adjective} {noun} para {verb} seu {noun} de Maneira {adjective}",
    "{verb} com Eficiência: {adjective} Estratégias para {noun}",
    "{adjective} {noun}: A Chave para {verb} com Sucesso",
    "{verb} seu {noun} com {adjective} Determinação e Foco",
    "{adjective} {noun} para {verb} um Futuro Brilhante",
    "{verb} com Maestria: {adjective} Estratégias para {noun}",
    "{adjective} {noun} para {verb} com Excelência",
    "{verb} seu {noun} de Forma {adjective}: O Caminho para o Sucesso",
    "{adjective} Maneiras de {verb} seu {noun} de Maneira {adjective}",
    "{verb} seu {noun} com {adjective} Paixão e Dedicação",
    "{adjective} {noun} para {verb} um Futuro de Realizações",
    "Desmistificando {adjective} {noun}: Como {verb} com Facilidade",
    "{verb} seu {noun} com {adjective} Determinação e Foco",
    "{adjective} {noun} para {verb} seu {noun} de Forma {adjective}",
    "{verb} com Paixão: {adjective} Estratégias para {noun}",
    "Explorando o {adjective} mundo dos {noun}",
    "Como {verb} seu {noun} de forma eficaz",
    "{adjective} estratégias para {verb} o sucesso",
    "Desvendando os mistérios do {noun} {verb}",
    "O {adjective} guia para {verb} seu {noun}",
    "{verb} o {adjective} poder do {noun}",
    "Transformando seu {noun} em uma {adjective} jornada",
    "{verb} {adjective} dicas para {noun} extraordinários",
    "Descubra como {verb} seu {noun} com facilidade",
    "Os {adjective} benefícios de {verb} um {noun}",
    "Torne-se um mestre em {verb} seu {adjective} {noun}",
    "{adjective} estratégias para {verb} seu {noun}",
    "{verb} com maestria: Seu guia para {noun} {adjective}",
    "Os segredos de {verb} um {adjective} {noun}",
    "Desfrute do {noun} {adjective} com estas {verb} dicas",
    "{adjective} maneiras de {verb} seu {noun}",
    "{adjective} truques para {verb} seu {noun} como um profissional",
    "Domine a arte de {verb} seu {adjective} {noun}",
    "{verb} com confiança: O caminho para {adjective} {noun}",
    "Os {adjective} segredos para {verb} seu {noun}",
    "A ciência por trás de {verb} seu {noun} {adjective}",
    "{adjective} estratégias para {verb} seu {noun} com sucesso",
    "{verb} seu {adjective} {noun} como um especialista",
    "Torne-se {adjective} em {verb} seu {noun}",
    "{adjective} maneiras de {verb} seu {noun} diariamente",
    "O guia definitivo para {verb} seu {adjective} {noun}",
    "{adjective} truques para {verb} seu {noun} de maneira eficiente",
    "{verb} seu {adjective} {noun} para alcançar o sucesso",
    "{adjective} dicas para {verb} seu {noun} de forma consistente",
    "{adjective} maneiras de {verb} seu {noun} com paixão",
    "Como {verb} seu {adjective} {noun} para resultados incríveis",
    "{adjective} estratégias para {verb} seu {noun} rapidamente",
    "{adjective} truques para {verb} seu {noun} com facilidade",
    "{verb} seu {adjective} {noun} com confiança",
    "Os {adjective} segredos de {verb} seu {noun} com maestria",
    "{adjective} maneiras de {verb} seu {noun} com entusiasmo",
    "Desbloqueando o {adjective} potencial de {verb} seu {noun}",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{verb} seu {adjective} {noun} para o próximo nível",
    "{adjective} estratégias para {verb} seu {adjective} {noun}",
    "{adjective} dicas para {verb} seu {noun} de forma eficaz",
    "{verb} seu {adjective} {noun} com maestria",
    "{verb} seu {noun} como um {adjective} profissional",
    "{adjective} maneiras de {verb} seu {noun} com excelência",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{verb} seu {adjective} {noun} para alcançar o sucesso",
    "{adjective} estratégias para {verb} seu {noun} com paixão",
    "{verb} seu {adjective} {noun} de maneira consistente",
    "{adjective} dicas para {verb} seu {noun} diariamente",
    "{adjective} maneiras de {verb} seu {adjective} {noun}",
    "Como {verb} seu {adjective} {noun} de forma eficiente",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{verb} seu {noun} {adjective} e alcance seus objetivos",
    "{adjective} estratégias para {verb} seu {noun} com confiança",
    "{adjective} dicas para {verb} seu {noun} com sucesso",
    "{verb} seu {noun} como um {adjective} especialista",
    "{adjective} maneiras de {verb} seu {noun} com entusiasmo",
    "{verb} seu {noun} {adjective} para o próximo nível",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{adjective} estratégias para {verb} seu {noun} de forma eficaz",
    "{verb} seu {adjective} {noun} com maestria",
    "{adjective} maneiras de {verb} seu {adjective} {noun}",
    "{verb} seu {adjective} {noun} como um profissional",
    "{adjective} truques para {verb} seu {noun} com excelência",
    "{verb} seu {adjective} {noun} para alcançar o sucesso",
    "{adjective} estratégias para {verb} seu {noun} com paixão",
    "{verb} seu {adjective} {noun} de maneira consistente",
    "{adjective} dicas para {verb} seu {noun} diariamente",
    "{adjective} maneiras de {verb} seu {noun} {adjective}",
    "Como {verb} seu {adjective} {noun} de forma eficiente",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{verb} seu {adjective} {noun} para alcançar o próximo nível",
    "{adjective} estratégias para {verb} seu {noun} com confiança",
    "{adjective} dicas para {verb} seu {noun} com sucesso",
    "{verb} seu {noun} como um {adjective} especialista",
    "{adjective} maneiras de {verb} seu {noun} com entusiasmo",
    "{verb} seu {noun} {adjective} para o próximo nível",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{adjective} estratégias para {verb} seu {noun} de forma eficaz",
    "{verb} seu {adjective} {noun} com maestria",
    "{adjective} maneiras de {verb} seu {adjective} {noun}",
    "{verb} seu {adjective} {noun} como um profissional",
    "{adjective} truques para {verb} seu {noun} com excelência",
    "{verb} seu {adjective} {noun} para alcançar o sucesso",
    "{adjective} estratégias para {verb} seu {noun} com paixão",
    "{verb} seu {adjective} {noun} de maneira consistente",
    "{adjective} dicas para {verb} seu {noun} diariamente",
    "{adjective} maneiras de {verb} seu {noun} {adjective}",
    "Como {verb} seu {adjective} {noun} de forma eficiente",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{verb} seu {adjective} {noun} para alcançar o próximo nível",
    "{adjective} estratégias para {verb} seu {noun} com confiança",
    "{adjective} dicas para {verb} seu {noun} com sucesso",
    "{verb} seu {noun} como um {adjective} especialista",
    "{adjective} maneiras de {verb} seu {noun} com entusiasmo",
    "{verb} seu {noun} {adjective} para o próximo nível",
    "{adjective} truques para {verb} seu {adjective} {noun}",
    "{adjective} estratégias para {verb} seu {noun} de forma eficaz",
    "{verb} seu {adjective} {noun} com maestria",
    "{adjective} maneiras de {verb} seu {adjective} {noun}",
]

adjectives = [
    "alegre",
    "amigável",
    "ansioso",
    "atencioso",
    "audacioso",
    "calmo",
    "carinhoso",
    "cético",
    "colorido",
    "confiante",
    "criativo",
    "curioso",
    "dedicado",
    "delicado",
    "determinado",
    "eficiente",
    "elogioso",
    "empolgante",
    "encantador",
    "energético",
    "entusiasmado",
    "espontâneo",
    "experiente",
    "extrovertido",
    "feliz",
    "firme",
    "flexível",
    "generoso",
    "gracioso",
    "grato",
    "habilidoso",
    "harmonioso",
    "honesto",
    "humilde",
    "idealista",
    "imaginativo",
    "incansável",
    "inovador",
    "inspirador",
    "inteligente",
    "intenso",
    "intuitivo",
    "irreverente",
    "jovial",
    "justo",
    "leal",
    "lúdico",
    "luminoso",
    "maduro",
    "meticuloso",
    "motivado",
    "ousado",
    "paciente",
    "perseverante",
    "poderoso",
    "positivo",
    "proativo",
    "puro",
    "rápido",
    "realista",
    "resiliente",
    "respeitoso",
    "responsável",
    "romântico",
    "sábio",
    "sedutor",
    "sensato",
    "sensível",
    "sereno",
    "sincero",
    "sofisticado",
    "sonhador",
    "sorridente",
    "surpreendente",
    "tenaz",
    "tolerante",
    "tranquilo",
    "transparente",
    "valente",
    "verdadeiro",
    "vibrante",
    "visionário",
    "vivaz",
    "zeloso",
    "zombador",
]

verbs = [
    "aceitar",
    "agir",
    "ajudar",
    "amar",
    "analisar",
    "aprender",
    "apresentar",
    "aprovar",
    "argumentar",
    "avaliar",
    "brilhar",
    "buscar",
    "calcular",
    "celebrar",
    "comandar",
    "começar",
    "compartilhar",
    "competir",
    "compreender",
    "concluir",
    "conectar",
    "conquistar",
    "construir",
    "consumir",
    "contribuir",
    "conversar",
    "convencer",
    "cooperar",
    "criar",
    "cultivar",
    "decidir",
    "definir",
    "descobrir",
    "desenvolver",
    "dialogar",
    "dirigir",
    "discutir",
    "divertir",
    "dominar",
    "educar",
    "elogiar",
    "encontrar",
    "energizar",
    "engajar",
    "entender",
    "entusiasmar",
    "enxergar",
    "equilibrar",
    "escutar",
    "escrever",
    "esperar",
    "estudar",
    "evoluir",
    "exercitar",
    "experimentar",
    "explorar",
    "expressar",
    "falar",
    "fascinar",
    "fazer",
    "festejar",
    "focar",
    "fortalecer",
    "gerar",
    "harmonizar",
    "identificar",
    "iluminar",
    "imaginar",
    "implementar",
    "inovar",
    "inspirar",
    "interpretar",
    "jogar",
    "lamentar",
    "lançar",
    "liderar",
    "lutar",
    "manter",
    "melhorar",
    "movimentar",
    "motivar",
    "namorar",
    "navegar",
    "observar",
    "oferecer",
    "organizar",
    "ousar",
    "pensar",
    "perceber",
    "planejar",
    "praticar",
    "preparar",
    "proclamar",
    "produzir",
    "programar",
    "proteger",
    "provocar",
    "questionar",
    "realizar",
    "refletir",
    "resolver",
    "respeitar",
    "revolucionar",
    "saber",
    "saudar",
    "seguir",
    "sentir",
    "sorrir",
    "sugerir",
    "transformar",
    "trabalhar",
    "utilizar",
    "valorizar",
    "vencer",
    "visualizar",
]

nouns = [
    "amor",
    "tempo",
    "vida",
    "casa",
    "pessoa",
    "dia",
    "mundo",
    "ano",
    "trabalho",
    "parte",
    "forma",
    "caminho",
    "palavra",
    "história",
    "ponto",
    "exemplo",
    "questão",
    "família",
    "governo",
    "país",
    "grupo",
    "problema",
    "empresa",
    "chance",
    "momento",
    "razão",
    "meio",
    "objetivo",
    "situação",
    "condição",
    "senso",
    "sentido",
    "valor",
    "arte",
    "beleza",
    "ideia",
    "caso",
    "fato",
    "resultado",
    "efeito",
    "lugar",
    "cidade",
    "região",
    "bairro",
    "espaço",
    "mês",
    "noite",
    "manhã",
    "tarde",
    "hora",
    "minuto",
    "segundo",
    "produto",
    "projeto",
    "programa",
    "recurso",
    "instrumento",
    "meio",
    "modo",
    "método",
    "número",
    "grupo",
    "categoria",
    "variável",
    "objeto",
    "evento",
    "situação",
    "relação",
    "conexão",
    "diferença",
    "semelhança",
    "experiência",
    "memória",
    "desejo",
    "sonho",
    "ideia",
    "pensamento",
    "conceito",
    "conhecimento",
    "informação",
    "comunicação",
    "linguagem",
    "expressão",
    "sentimento",
    "emoção",
    "ação",
    "reação",
    "movimento",
    "desenvolvimento",
    "progresso",
    "cultura",
    "educação",
    "ciência",
    "arte",
    "tecnologia",
    "natureza",
    "ambiente",
    "clima",
    "sistema",
    "estrutura",
    "organização",
    "instituição",
    "empresa",
    "mercado",
    "comércio",
    "produto",
    "serviço",
    "preço",
    "valor",
    "qualidade",
]

tags = [
    "Inovação",
    "Tecnologia",
    "Empreendedorismo",
    "Marketing Digital",
    "Desenvolvimento Pessoal",
    "Gestão de Projetos",
    "Crescimento Profissional",
    "Educação",
    "Negócios",
    "Produtividade",
    "Sustentabilidade",
    "Saúde Mental",
    "Finanças Pessoais",
    "Carreira",
    "Transformação Digital",
    "Dicas Práticas",
    "Motivação",
    "Cultura Organizacional",
    "Trabalho Remoto",
    "Inovação Tecnológica",
    "Futuro do Trabalho",
    "Estratégia Empresarial",
    "Liderança",
    "Autoaperfeiçoamento",
    "Criatividade",
    "Economia",
    "Educação Financeira",
    "Tendências de Mercado",
    "Ferramentas Digitais",
    "Networking",
    "Comunicação",
    "Inspiração",
    "Ferramentas de Produtividade",
    "Sustentabilidade Empresarial",
    "Gestão do Tempo",
    "Estratégias de Vendas",
    "Tecnologias Emergentes",
    "Aprendizado Contínuo",
    "Gestão de Equipes",
    "Startups",
    "E-commerce",
    "Estratégias de Marketing",
    "Inteligência Artificial",
    "Automação",
    "Cibersegurança",
    "Futuro da Educação",
    "Empoderamento Feminino",
    "Mindfulness",
    "Inclusão e Diversidade",
    "Saúde e Bem-estar",
    "Comportamento do Consumidor",
    "Gestão de Mudanças",
    "Inovações Tecnológicas",
    "Estratégias de Sucesso",
    "Transformação Pessoal",
    "Gestão de Recursos",
    "Economia Circular",
    "Liderança Transformadora",
    "Crescimento de Startups",
    "Estratégias de Crescimento",
    "Gestão de Projetos Ágeis",
    "Desenvolvimento Profissional",
    "Inteligência Emocional",
    "Cultura Empresarial",
    "Tecnologias Disruptivas",
    "Ferramentas Colaborativas",
    "Criação de Conteúdo",
    "Gestão de Riscos",
    "Inovação em Negócios",
    "Marketing de Conteúdo",
    "Estratégias de Inovação",
    "Negócios Sustentáveis",
    "Desenvolvimento de Habilidades",
    "Empreendedorismo Social",
    "Estratégias de Networking",
    "Empreendedorismo Digital",
    "Gestão de Finanças",
    "Estratégias de Empreendedorismo",
    "Gestão de Pequenas Empresas",
    "Desenvolvimento de Carreira",
    "Tecnologias do Futuro",
    "Estratégias de Autoaperfeiçoamento",
    "Gestão de Inovação",
    "Desenvolvimento Sustentável",
    "Gestão de Talentos",
    "Estratégias de Automação",
    "Tecnologia na Educação",
    "Ferramentas para Empreendedores",
    "Inovação em Gestão",
    "Estratégias de Produtividade",
    "Estratégias de Trabalho Remoto",
    "Tecnologias de Comunicação",
    "Desenvolvimento de Liderança",
    "Gestão de Projetos Inovadores",
    "Estratégias de Economia Circular",
    "Estratégias de Cibersegurança",
    "Gestão da Mudança Organizacional",
    "Gestão de Startups",
    "Tecnologias de Inteligência Artificial",
    "Gestão de Equipes de Alta Performance",
    "Estratégias de Transformação Digital",
]

categories = [
    "Ciência",
    "Tecnologia",
    "Saúde",
    "Educação",
    "Cultura",
    "Entretenimento",
    "Negócios",
    "Desenvolvimento Pessoal",
    "Meio Ambiente",
    "Finanças",
    "Moda",
    "Esportes",
    "Gastronomia",
    "Viagens",
    "Arte",
    "História",
    "Política",
    "Religião",
    "Família",
    "Bem-estar",
    "Comportamento",
    "Economia",
    "Sustentabilidade",
    "Inovação",
    "Empreendedorismo",
    "Psicologia",
    "Autoajuda",
    "Literatura",
    "Tendências",
    "Marketing",
    "Digital",
    "Gestão",
    "Carreira",
    "Liderança",
    "Design",
    "Futuro",
    "Cinema",
    "Música",
    "Arquitetura",
    "Fotografia",
    "Comunicação",
    "Redes Sociais",
    "Internet",
    "Games",
    "Ciência da Computação",
    "Inteligência Artificial",
    "Robótica",
    "Educação Digital",
    "Saúde Mental",
    "Nutrição",
    "Fitness",
    "Medicina",
    "Biotecnologia",
    "Ensino",
    "Aprendizado",
    "Culinária",
    "Receitas",
    "Vinhos",
    "Turismo",
    "Aventuras",
    "Artes Plásticas",
    "Teatro",
    "Dança",
    "Literatura",
    "Poesia",
    "Biografias",
    "Notícias",
    "Análise de Mercado",
    "Investimentos",
    "Gestão Financeira",
    "Tecnologia Verde",
    "Energias Renováveis",
    "Reciclagem",
    "Educação Financeira",
    "Mercado de Trabalho",
    "Empregabilidade",
    "Recursos Humanos",
    "Comportamento Empresarial",
    "Estratégias de Negócios",
    "Startups",
    "Empresas Familiares",
    "Gestão de Projetos",
    "Produtividade",
    "Empreendedorismo Social",
    "Marketing de Conteúdo",
    "SEO",
    "Publicidade",
    "Design Thinking",
    "Criatividade",
    "Inovação Tecnológica",
    "Transformação Digital",
    "Indústria 4.0",
    "Big Data",
    "Cibersegurança",
    "Cloud Computing",
    "Teletrabalho",
    "Gestão Remota",
    "Futuro do Trabalho",
    "Autoaperfeiçoamento",
    "Desenvolvimento de Habilidades",
    "Liderança Transformadora",
]


def make_title() -> str:
    noun = choice(nouns)
    adjective = choice(adjectives)
    verb = choice(verbs)
    template = choice(title)

    return template.format(verb=verb, noun=noun, adjective=adjective).title()
