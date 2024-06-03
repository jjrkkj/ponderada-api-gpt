# Documentação

## 1. Como rodar a API?

#### 1. Instale as dependêcias

Execute o comando no terminal: `pip install fastapi uvicorn pydantic`

#### 2. Navegue até o diretório correto

Certifique-se que está na raiz do projeto.
Execute o comando no terminal: `cd src/backend`

#### 3. Inicie o servidor

Execute o comando no terminal: `uvicorn app:app --reload`

---

## 2. Endpoints

### 2.1 Endpoints para Histórias

#### 2.1.1 Criar História

- POST /story/

Cria uma nova história.

#### Corpo da Requisição:

- **title (string)**: O título da história.
- **description (string)**: A descrição da história.
- **category (string)**: A categoria da história.

#### Resposta:

Retorna a história criada.

#### Exemplo:

```json
{
  "title": "Nova História",
  "description": "Esta é uma nova história.",
  "category": "Aventura"
}
```

#### 2.1.2 Ler História por ID

- GET /story/{story_id}

Busca uma história pelo seu ID.

#### Parâmetros:

story_id (int): O ID da história a ser buscada.

#### Resposta:

- Se a história for encontrada, retorna a história com title, description e category.
- Se a história não for encontrada, retorna uma mensagem indicando "História não encontrada".

#### Exemplo:

```json
{
  "title": "Nova História",
  "description": "Esta é uma nova história.",
  "category": "Aventura"
}
```

#### 2.1.3 Atualizar História

- PUT /story/{story_id}

Atualiza uma história pelo seu ID.

#### Parâmetros:

- **story_id (int)**: O ID da história a ser atualizada.

#### Corpo da Requisição:

- **title (string)**: O novo título da história.
- **description (string)**: A nova descrição da história.
- **category (string)**: A nova categoria da história.

#### Resposta:

Retorna uma mensagem indicando "História atualizada com sucesso".

#### Exemplo:

```json
{
  "title": "História Atualizada",
  "description": "Esta é uma história atualizada.",
  "category": "Mistério"
}
```

#### 2.1.4 Deletar História

- DELETE /story/{story_id}

Deleta uma história pelo seu ID.

#### Parâmetros:

- **story_id (int)**: O ID da história a ser deletada.

#### Resposta:

Retorna uma mensagem indicando "História deletada com sucesso".

#### Exemplo:

```json
{
  "message": "História deletada com sucesso"
}
```

### 2.2 Endpoints para Usuários

#### 2.2.1 Criar Usuário

- POST /user/

Cria um novo usuário.

#### Corpo da Requisição:

- **name (string)**: O nome do usuário.
- **username (string)**: O nome de usuário do usuário.
- **password (string)**: A senha do usuário.

#### Resposta:

Retorna o usuário criado.

#### Exemplo:

```json
{
  "name": "João Silva",
  "username": "joaosilva",
  "password": "senha123"
}
```

#### 2.2.2 Ler Usuário por ID

- GET /user/{user_id}

Busca um usuário pelo seu ID.

#### Parâmetros:

- **user_id (int)**: O ID do usuário a ser buscado.

#### Resposta:

- Se o usuário for encontrado, retorna o usuário com name, username e password.
- Se o usuário não for encontrado, retorna uma mensagem indicando "Usuário não encontrado".

#### Exemplo:

```json
{
  "name": "João Silva",
  "username": "joaosilva",
  "password": "senha123"
}
```

#### 2.2.3 Atualizar Usuário

- PUT /user/{user_id}

Atualiza um usuário pelo seu ID.

#### Parâmetros:

- **user_id (int)**: O ID do usuário a ser atualizado.

#### Corpo da Requisição:

- **name (string)**: O novo nome do usuário.
- **username (string)**: O novo nome de usuário do usuário.
- **password (string)**: A nova senha do usuário.

#### Resposta:

Retorna uma mensagem indicando "Usuário atualizado com sucesso".

#### Exemplo:

```json
{
  "name": "Maria Silva",
  "username": "mariasilva",
  "password": "novasenha123"
}
```

#### 2.2.4 Deletar Usuário

- DELETE /user/{user_id}

Deleta um usuário pelo seu ID.

#### Parâmetros:

- **user_id (int)**: O ID do usuário a ser deletado.

#### Resposta:

Retorna uma mensagem indicando "Usuário deletado com sucesso".

#### Exemplo:

```json
{
  "message": "Usuário deletado com sucesso"
}
```
