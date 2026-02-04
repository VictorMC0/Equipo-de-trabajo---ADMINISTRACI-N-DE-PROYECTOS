from fastapi import FastAPI
from app.routers import pacientes

app = FastAPI(
    title="HealthyReminder",
    description="Sistema de gestión clínica odontológica",
    version="1.0.0"
)

app.include_router(pacientes.router)

@app.get("/")
def read_root():
    return {
        "mensaje": "HealthyReminder API en ejecución",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}