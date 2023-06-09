from src.service.upkeep.feature import train_and_predict
from src.service.upkeep.incidents import predict
from src.service.upkeep.union import make_union
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from src.api import deps
from starlette import status
from src.schema.models import PredictionModels

router = APIRouter()


@router.get("/property")
async def predict_prop(session: AsyncSession = Depends(deps.get_db)):
    """
    Predict based on object properties
    """
    await train_and_predict(model=PredictionModels.feature, session=session)
    return status.HTTP_200_OK


@router.get("/incident")
async def predict_inc(session: AsyncSession = Depends(deps.get_db)):
    """
    Predict based on object incidents
    """
    await predict(model=PredictionModels.incident, session=session)
    return status.HTTP_200_OK


@router.get("/union")
async def predict_union(session: AsyncSession = Depends(deps.get_db)):
    """
    Make union of 2 model predictions 
    """
    await make_union(model=PredictionModels.union, session=session)
    return status.HTTP_200_OK
