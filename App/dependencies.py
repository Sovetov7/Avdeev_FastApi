from App.repositories.student import StudentJsonRepository
from App.repositories.group import GroupJsonRepository


TMP_STUDENT_REPOSITORY = StudentJsonRepository()
TMP_GROUP_REPOSITORY = GroupJsonRepository()


def get_student_repo() -> StudentJsonRepository:
    # Получение Student репозитория

    return TMP_STUDENT_REPOSITORY


def get_group_repo() -> GroupJsonRepository:
    # Получение Group репозитория

    return TMP_GROUP_REPOSITORY
