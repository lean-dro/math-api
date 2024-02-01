# math-api
Api simples de resolução de questões matemáticas, com enfoque na documentação da mesma.

## Tutorial de uso

- Crie o ambiente virtual

    ```bash
    python -m venv .venv/
    ```

- Ative o ambiente virtual

    ```bash
    .\.venv\Scripts\activate
    ```

- Instale as dependências

    ```bash
    py -m pip install -r .\requirements.txt
    ```

- Inicie o servidor

    ```bash
    uvicorn main:app --reload 
    ```
