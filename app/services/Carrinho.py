import json


class Carrinho:
    _items = []

    def get_items(self):
        return self._items

    def clear_items(self):
        self._items = []

    def adiciona_produto(self, produto: str) -> None:
        produto = json.loads(produto.replace("'", '"'))
        for item in self._items:
            if item['id'] == produto['id']:
                item['quantity'] += 1
                return
        produto['quantity'] = 1
        self._items.append(produto)

    def remove_produto(self, produto) -> None:
        produto = json.loads(produto.replace("'", '"'))
        for item in self._items:
            if item['id'] == produto['id']:
                if item['quantity'] > 1:
                    item['quantity'] -= 1
                else:
                    self._items.remove(item)

    def get_total(self):
        valor_total = 0
        for item in self._items:
            valor_total += item['preco'] * item['quantity']
        return f'{valor_total:.2f}'
