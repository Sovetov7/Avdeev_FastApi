from typing import List
import uuid
from fastapi import APIRouter, Depends
from App.dependencies import get_student_repo
from App.models.student import StudentIn, StudentOut
from App.repositories.student import BaseStudentRepository

router = APIRouter()


@router.get("/students", tags=["students"], response_model=List[StudentOut])
async def get_students(
        group: str = "",
        student_repo: BaseStudentRepository = Depends(get_student_repo),
        limit: int = 100,
        skip: int = 0
        ):

    return student_repo.get_all(group=group, limit=limit, skip=skip)


@router.get("/student", tags=["students"], response_model=StudentOut | str)
async def get_student(
        id: uuid.UUID,
        student_repo: BaseStudentRepository = Depends(get_student_repo),
        ):

    return student_repo.get_by_id(id)


@router.post("/student", tags=["students"], response_model=StudentOut)
async def create_student(
        student_in: StudentIn,
        student_repo: BaseStudentRepository = Depends(get_student_repo),
        ):

    return student_repo.create(student_in)


@router.put("/student", tags=["students"], response_model=StudentOut | str)
async def put_student(
        id: uuid.UUID,
        student_in: StudentIn,
        student_repo: BaseStudentRepository = Depends(get_student_repo),
        ):

    return student_repo.update_by_id(id, student_in)


@router.delete("/student", tags=["students"], response_model=str)
async def delete_student(
        id: uuid.UUID,
        student_repo: BaseStudentRepository = Depends(get_student_repo),
        ):

    return student_repo.delete_by_id(id)
