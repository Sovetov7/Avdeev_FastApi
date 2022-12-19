from typing import List
import uuid
from fastapi import APIRouter, Depends
from App.dependencies import get_group_repo
from App.models.group import GroupIn, GroupStorage
from App.repositories.group import BaseGroupRepository

router = APIRouter()


@router.get("/groups", tags=["groups"], response_model=List[GroupStorage])
async def get_groups(
        group_repo: BaseGroupRepository = Depends(get_group_repo),
        limit: int = 100,
        skip: int = 0
        ):

    return group_repo.get_all(limit=limit, skip=skip)


@router.get("/group", tags=["groups"], response_model=GroupStorage | str)
async def get_group(
        id: uuid.UUID,
        group_repo: BaseGroupRepository = Depends(get_group_repo),
        ):

    return group_repo.get_by_id(id)


@router.post("/group", tags=["groups"], response_model=GroupStorage)
async def create_group(
        group_in: GroupIn,
        group_repo: BaseGroupRepository = Depends(get_group_repo),
        ):

    return group_repo.create(group_in)


@router.put("/group", tags=["groups"], response_model=GroupStorage | str)
async def put_group(
        id: uuid.UUID,
        group_in: GroupIn,
        group_repo: BaseGroupRepository = Depends(get_group_repo),
        ):

    return group_repo.update_by_id(id, group_in)


@router.delete("/group", tags=["groups"], response_model=str)
async def delete_group(
        id: uuid.UUID,
        group_repo: BaseGroupRepository = Depends(get_group_repo),
        ):

    return group_repo.delete_by_id(id)
