from marshmallow import Schema, fields, ValidationError

# Схема для валидации данных сотрудника
class EmployeeSchema(Schema):
    name = fields.String(required=True, error_messages={"required": "Name is required."})
    department = fields.String(required=True, error_messages={"required": "Department is required."})
    position = fields.String(required=True, error_messages={"required": "Position is required."})
    birthday = fields.Date(
        required=True,
        format="%d.%m.%Y",  # Формат DD.MM.YYYY
        error_messages={"required": "Birthday is required.", "invalid": "Invalid date format. Use DD.MM.YYYY."}
    )
