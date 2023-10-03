# Projeto Restaurant Orders

Neste projeto, foi implementado estruturas de dados de Hashmap, implementadas em Python através das classes Dict e Set, para criar uma ferramenta de construção de cardápios para o Restaurante 🍝 🦐 Chapa Quente 🍛 🥘. O restaurante precisa desta ferramenta para simplificar a geração de cardápios, considerando restrições alimentares e a disponibilidade de ingredientes em estoque. Atualmente, a gestão das receitas e do estoque é feita de forma ineficiente usando arquivos CSV, e o objetivo é melhorar essa gestão.

<br/>

# Funcionalidades

* Geração de cardápios personalizados com base nas preferências do cliente e na disponibilidade de ingredientes em estoque.
* Manipulação eficiente de configurações e parâmetros do sistema usando estruturas de dados Dict.
* Gerenciamento de receitas e estoque de forma organizada e eficaz.
* Implementação de testes de software para garantir a qualidade do código.

# Tecnologias Utilizadas

* Python
* Pandas
* Estruturas de dados: Dict e Set
* Testes de software

# Requisitos do Projeto

1. Implemente testes para a classe `Ingredient`, que se encontra no módulo `src/models/ingredient.py`.
2. Implemente testes para a classe `Dish`, que se encontra no módulo `src/models/dish.py`.
3. Implemente a classe `MenuData` que fará todo o mapeamento de pratos e ingredientes baseado nos arquivo csv disponibilizado. Ela se encontra no módulo `src/services/menu_data.py`.
4. Implemente o método `get_main_menu` dentro da classe `MenuBuilder`, que gera um `DataFrame` com os cardápios. Ele se encontra no arquivo `src/services/menu_builder.py`.
5. Complemente a implementação do método `get_main_menu` para que só sejam exibidos pratos que possam ser feitos com os ingredientes disponíveis no estoque.

# Agradecimentos

Agradecemos à Trybe por proporcionar a oportunidade de desenvolver este projeto e aprender novas tecnologias. Também agradecemos à comunidade de desenvolvedores que contribui para o desenvolvimento do React e outras tecnologias utilizadas neste projeto. E, é claro, agradecemos a George Lucas por criar um universo tão incrível que inspira tantas pessoas até hoje.
