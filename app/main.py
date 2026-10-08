from fastapi import FastAPI

app = FastAPI(
    title="Plataforma SaaS para Associações",
    version="0.1.0",
    description="API RESTful para gestão, transparência e auditoria de ONGs.",
)


@app.get("/")
def home():
    return {
        "status": "online",
        "projeto": "Plataforma SaaS Associações",
        "mensagem": "API rodando com sucesso!",
    }
