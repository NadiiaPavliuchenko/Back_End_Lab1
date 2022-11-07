from marshmallow import Schema, fields


class User_schema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class Category_schema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(reguired=True)


class NoteQuery_schema(Schema):
    username = fields.Str(required=True)
    categoryname = fields.Str()


class Note_schema(Schema):
    id = fields.Int(dump_only=True)
    id_user = fields.Int(required=True)
    id_category = fields.Int(required=True)
    sum = fields.Float(required=True)


class Score_schema(Schema):
    id = fields.Int(dump_only=True)
    id_user = fields.Int(required=True)
    sum = fields.Float(required=True)


class ScoreQuery_schema(Schema):
    username = fields.Str(required=True)
    add_sum = fields.Float()


class ChangeScore_schema(Schema):
    username = fields.Str(required=True)
    add_sum = fields.Float(required=True)

