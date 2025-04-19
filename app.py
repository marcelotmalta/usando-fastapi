from fastapi import FastAPI, HTTPException
from typing import List
from models.item import Item

app = FastAPI(
    title="Carrinho de Itens",
    version="1.0.0",
    description="API CRUD com FastAPI e Pydantic para gerenciar um carrinho de compras.",
)

# Simulando banco de dados com um dicionário
banco_itens = {}

@app.post("/itens/", response_model=Item, summary="Criar um novo item")
def criar_item(item: Item):
    """
    Cria um novo item no carrinho.

    - **id**: identificador único do item
    - **nome**: nome do item
    - **descricao**: descrição opcional do item
    - **preco**: preço do item (deve ser maior que 0)
    - **quantidade**: quantidade em estoque (deve ser >= 0)
    """
    if item.id in banco_itens:
        raise HTTPException(status_code=400, detail="Item com esse ID já existe")
    banco_itens[item.id] = item
    return item


@app.get("/itens/{item_id}", response_model=Item, summary="Obter um item por ID")
def ler_item(item_id: int):
    """
    Retorna os dados de um item a partir do seu ID.

    - **item_id**: ID inteiro do item
    """
    if item_id not in banco_itens:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return banco_itens[item_id]


@app.get("/itens/", response_model=List[Item], summary="Listar todos os itens")
def listar_itens():
    """
    Lista todos os itens presentes no carrinho.
    """
    return list(banco_itens.values())


@app.put("/itens/{item_id}", response_model=Item, summary="Atualizar item existente")
def atualizar_item(item_id: int, item: Item):
    """
    Atualiza os dados de um item existente no carrinho.

    - **item_id**: ID do item a ser atualizado
    - O corpo da requisição deve conter todos os dados atualizados do item
    """
    if item_id != item.id:
        raise HTTPException(status_code=400, detail="ID na URL e no corpo não coincidem")
    if item_id not in banco_itens:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    banco_itens[item_id] = item
    return item


@app.delete("/itens/{item_id}", summary="Deletar um item por ID")
def deletar_item(item_id: int):
    """
    Remove um item do carrinho com base no seu ID.

    - **item_id**: ID do item a ser removido
    """
    if item_id not in banco_itens:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del banco_itens[item_id]
    return {"message": f"Item {item_id} deletado com sucesso"}
