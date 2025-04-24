from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.deps import get_session
from schemas import all_schemas
from models.office_model import OfficeModel  
from schemas.all_schemas import OfficeCharacterSchema

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=all_schemas.OfficeCharacterSchema)
async def post_office_character(character: all_schemas.OfficeCharacterSchema, db: AsyncSession = Depends(get_session)):
    new_character = OfficeModel(  
        name=character.name,
        position=character.position,
        age=character.age,
        relationship_status=character.relationship_status,
        office_hobbies=character.office_hobbies,
        quote=character.quote,
    )
    db.add(new_character)
    await db.commit()
    return new_character


@router.get("/", response_model=List[all_schemas.OfficeCharacterSchema], status_code=status.HTTP_200_OK)
async def get_office_characters(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OfficeModel)
        result = await session.execute(query)
        characters: List[OfficeModel] = result.scalars().all()
        return characters


@router.get("/{id}", response_model=all_schemas.OfficeCharacterSchema, status_code=status.HTTP_302_FOUND)
async def get_office_character(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OfficeModel).filter(OfficeModel.id == id)  
        result = await session.execute(query)
        character = result.scalar_one_or_none()
        if character:
            return character
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found!")


@router.put("/{id}", response_model=all_schemas.OfficeCharacterSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_office_character(id: int, character: all_schemas.OfficeCharacterSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OfficeModel).filter(OfficeModel.id == id) 
        result = await session.execute(query)
        character_up = result.scalar_one_or_none()
        if character_up:
            character_up.name = character.name
            character_up.position = character.position
            character_up.age = character.age
            character_up.relationship_status = character.relationship_status
            character_up.office_hobbies = character.office_hobbies
            character_up.quote = character.quote
            await session.commit()
            return character_up
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found!")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_office_character(id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OfficeModel).filter(OfficeModel.id == id)  # Usando o modelo correto
        result = await session.execute(query)
        character_del = result.scalar_one_or_none()
        if character_del:
            await session.delete(character_del)
            await session.commit()
            return Response(status.HTTP_204_NO_CONTENT)
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character not found!")
