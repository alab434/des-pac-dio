# mynomar
O pacote `mynomar` é usado para:
	- Normalizar nomes de arquivos.
	- Modificar a caixa de textos.

## Instalação
Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) pip para instalar o `mynomar`

```bash
pip install mynomar
```

## Uso
```python
from mynomar.normalizar import nome

nome.pasta('./demo/Teste 0')

nome.pasta('./demo/Teste 1', caixa='baixa')

nome.pasta('./demo/Teste 2', caixa='alta')

nome.pasta('./demo/Teste 3', caixa='capital')
```

```shell
Renomeado: ./demo/Teste 0/estaçao espacial Construction Kit.glb -> ./demo/Teste 0/estaçao_espacial Construction_Kit.glb
Renomeado: ./demo/Teste 0/SaCos; PiLha.glb -> ./demo/Teste 0/SaCos_PiLha.glb

Renomeado: ./demo/Teste 1/Rebel Kids - Modern rebel font7.jpeg -> ./demo/Teste 1/rebel_kids_-_modern_rebel_font7.jpeg
Renomeado: ./demo/Teste 1/cara com capuz.glb -> ./demo/Teste 1/cara_com_capuz.glb

Renomeado: ./demo/Teste 2/estaçao espacial Construction Kit.glb -> ./demo/Teste 2/ESTAÇAO_ESPACIAL_CONSTRUCTION_KIT.GLB
Renomeado: ./demo/Teste 2/sacos; pilha.glb -> ./demo/Teste 2/SACOS_PILHA.GLB

Renomeado: ./demo/Teste 3/cara com capuz.glb -> ./demo/Teste 3/Cara_com_capuz.glb
Renomeado: ./demo/Teste 3/sacos; pilha.glb -> ./demo/Teste 3/Sacos_pilha.GLB
```

```python
from mynomar.modificar import texto

print( texto.caixa_alta('POO em Python') )

print( texto.caixa_baixa('README') )

print( texto.caixa_capital('POO em Python') )
```

```shell
POO EM PYTHON

readme.md

Poo em python
```


## Autor
Almyr P.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
