# ArXiv Research Server (MCP Streamable HTTP)

Servidor MCP local para buscar papers en arXiv y consultar la informacion guardada.

## Requisitos

- Python 3.10+
- uv
- Node.js (para usar MCP Inspector)

## Instalacion

```powershell
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
```

## Ejecutar el servidor MCP

El servidor se expone por HTTP en:

- `http://localhost:8001/mcp`

Arranque recomendado:

```powershell
uv run main.py
```

Alternativa equivalente:

```powershell
uv run research_server.py
```

## Probar con MCP Inspector

Importante: inicia el Inspector con parametros explicitos para que no intente levantar un servidor de ejemplo (`mcp-server-everything`) y falle con `ENOENT`.

```powershell
npx @modelcontextprotocol/inspector --transport http --server-url http://localhost:8001/mcp
```

Luego abre la URL que imprime en consola (normalmente en `http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=...`).

En la UI del Inspector verifica:

- Transport Type: `Streamable HTTP`
- URL: `http://localhost:8001/mcp`
- Connection Type: `Direct`

Pulsa `Connect`.

## Configuracion en VS Code (MCP)

Este proyecto ya usa configuracion HTTP en `.vscode/mcp.json`:

```json
{
      "servers": {
            "research_server_streamable": {
                  "url": "http://localhost:8001/mcp",
                  "type": "http"
            }
      },
      "inputs": []
}
```

## Herramientas MCP disponibles

- `search_papers(topic, max_results=5)`: busca papers en arXiv y guarda metadata en `papers/<topic>/papers_info.json`.
- `extract_info(paper_id)`: recupera la informacion de un paper guardado.

## Troubleshooting rapido

### Error de puerto ocupado (WinError 10048)

Significa que ya hay otro proceso en el puerto 8001.

```powershell
Get-NetTCPConnection -LocalPort 8001 | Select-Object OwningProcess, State
Stop-Process -Id <PID> -Force
```

### El Inspector muestra Connection Error

- Confirma que el servidor esta corriendo en otra terminal.
- Confirma URL exacta: `http://localhost:8001/mcp`.
- Si hay instancias viejas del Inspector, cierra procesos Node y relanzalo con el comando con `--transport http --server-url ...`.