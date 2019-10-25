# Mining Text: Simplificação de Texto
Trabalho da faculdade.

A simplificação de texto é um tópico que vem se demonstrando uma ferramenta importante tanto como pre processamento de texto, quanto em tornar textos complexos, em textos mais simples para que pessoas com algumas dificuldades possam ter acesso a determinados conteúdos. A diferença entre a simplificação de texto como um passo para um projeto e a simplificação de texto como produto final é o tratamento para tornar o texto legível de novo. Para muitos projetos se retiram as palavras que têm pouco significado para o texto, as stopwords, apesar de isso também ser um passo possível para a simplificação de texto, um texto legível precisa ter essas stopwords. Afinal o que seria o mundo sem por que?

O primeiro artigo Text Simplification for Children de 	Jan De Belder e Marie Francine Moens divide o processo em simplificação lexica, simplificação sintática, otimização de escolhas e avaliação. Há a denúncia de falta de base de dados, mas isso foi suprido com a wikipedia e a simple.wikipedia, se supõe que um texto na wikipedia que possui uma versão mais simples na simple wikipedia sempre será um texto mais simples. O texto também sugere usar um classificador para detectar se um texto é simples ou não.

O segundo artigo Using Lexical Chains to Identify Text Difficulty: A Corpus Statistics and Classification Study de Partha Mukherjee, Gondy Leroy e David Kauchak propõe um as características usadas para classificar um texto como fácil ou difícil. Propõe usar cadeias de palavras para melhorar a tarefa de encontrar esse padrão, as cadeias não são mais que grupos de palavras organizadas por um determinado critério. Eles também criam sua base de dados com o material disponível na wikipedia.

## Update 1

Apesar do uso do _stemming_ e do 
