from marshmallow import Schema, fields


class User_schema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class Category_schema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(reguired=True)


class NoteQuery_schema(Schema):
    username = fields.Str(required=True)
    categoryname = fields.Str()


class Note_schema(Schema):
    id = fields.Str(dump_only=True)
    id_user = fields.Str(required=True)
    id_category = fields.Str(required=True)
    sum = fields.Float(required=True)
