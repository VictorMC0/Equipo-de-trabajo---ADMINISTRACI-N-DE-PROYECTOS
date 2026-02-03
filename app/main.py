from fastapi import FastAPI
from app.routers import pacientes

app = FastAPI(
    title="HealthyReminder",
    description="Sistema de gestión clínica odontológica",
    version="1.0.0"
)

app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])

@app.get("/")
def root():
    return {"message": "HealthyReminder API en ejecución"}
