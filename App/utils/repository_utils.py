import datetime
import uuid
from App.models.student import StudentIn, StudentOut, StudentStorage
from App.models.group import GroupIn, GroupStorage


def convert_student_storage_to_out(student: StudentStorage) -> StudentOut:
    # Производит конвертацию StudentStorage --> StudentOut

    tmp_dict: dict = student.dict()
    tmp_dict.pop("password", None)
    return StudentOut(**tmp_dict)


def convert_student_in_to_storage(student: StudentIn) -> StudentStorage:
    # Производит конвертацию StudentIn --> StudentStorage

    tmp_dict: dict = student.dict()
    birth_date = str(tmp_dict.get('birth_date'))
    tmp_dict.update({'birth_date': birth_date})

    student_storage = StudentStorage(id=str(uuid.uuid4()),
                                     created_at=str(datetime.datetime.now()),
                                     **tmp_dict)
    return student_storage


def update_student_in_storage(id_old: uuid.UUID, student_new: StudentIn) -> StudentStorage:
    # Производит обновление данных студента

    tmp_dict: dict = student_new.dict()
    birth_date = str(tmp_dict.get('birth_date'))
    tmp_dict.update({'birth_date': birth_date})
    student_storage = StudentStorage(id=str(id_old),
                                     created_at=str(datetime.datetime.now()),
                                     **tmp_dict)

    return student_storage


def convert_student_dict_to_storage(student_dict: dict) -> StudentStorage:
    # Производит преобразование dict к типу StudentStorage

    student_storage = StudentStorage(**student_dict)
    return student_storage


def convert_group_in_to_storage(group: GroupIn) -> GroupStorage:
    # Производит конвертацию GroupIn --> GroupStorage

    tmp_dict: dict = group.dict()
    group_storage = GroupStorage(id=str(uuid.uuid4()),
                                 created_at=str(datetime.datetime.now()),
                                 **tmp_dict)
    return group_storage


def update_group_in_storage(id_old: uuid.UUID, group_new: GroupIn) -> GroupStorage:
    # Производит обновление данных группы

    tmp_dict: dict = group_new.dict()
    group_storage = GroupStorage(id=str(id_old),
                                 created_at=str(datetime.datetime.now()),
                                 **tmp_dict)

    return group_storage


def convert_group_dict_to_storage(group_dict: dict) -> GroupStorage:
    # Производит преобразование dict к типу GroupStorage

    group_storage = GroupStorage(**group_dict)
    return group_storage
