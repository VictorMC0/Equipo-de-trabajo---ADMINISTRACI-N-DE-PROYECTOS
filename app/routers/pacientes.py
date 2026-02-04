from fastapi import APIRouter, Query
router = APIRouter(
    prefix="/pacientes",
    tags=["Pacientes"]
)

pacientes_db = [
    {"id": 1, "nombre": "Juan Pérez", "expediente": "OD-001", "motivo_consulta": "limpieza"},
    {"id": 2, "nombre": "María López", "expediente": "OD-002", "motivo_consulta": "caries"},
    {"id": 3, "nombre": "Carlos García", "expediente": "OD-003", "motivo_consulta": "ortodoncia"},
    {"id": 4, "nombre": "Ana Martínez", "expediente": "OD-004", "motivo_consulta": "extraccion"},
    {"id": 5, "nombre": "Pedro Sánchez", "expediente": "OD-005", "motivo_consulta": "caries"},
    {"id": 6, "nombre": "Carlos Marques", "expediente": "OD-006", "motivo_consulta": "limpieza"},
    {"id": 7, "nombre": "Luisa Martínez", "expediente": "OD-007", "motivo_consulta": "ortodoncia"},
    {"id": 8, "nombre": "Petronilo Sánchez", "expediente": "OD-008", "motivo_consulta": "extraccion"}
]

@router.get("/")
def listar_pacientes(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Cantidad de registros a retornar"),
    motivo_consulta: str = Query(None, description="Filtrar por motivo de consulta")
):
    """
    Lista todos los pacientes con paginación.
   
    - **skip**: Cuántos pacientes saltar (para paginación)
    - **limit**: Cuántos pacientes retornar (máximo 100)
    - **motivo_consulta**: Filtro de pacientes por motivo de consulta
    """
    pacientes = pacientes_db

    if motivo_consulta:
        pacientes = [p for p in pacientes if p["motivo_consulta"] == motivo_consulta]
    return {
        "total": len(pacientes_db),
        "skip": skip,
        "limit": limit,
        "Filtros": {"motivo_consulta": motivo_consulta} if motivo_consulta else None,
        "pacientes": pacientes_db[skip : skip + limit]
    }

@router.get("/{paciente_id}")
def obtener_paciente(paciente_id: int):
    """
    Obtiene un paciente por su ID.
    """
    for paciente in pacientes_db:
        if paciente["id"] == paciente_id:
            return paciente
    return {"error": "Paciente no encontrado"}
