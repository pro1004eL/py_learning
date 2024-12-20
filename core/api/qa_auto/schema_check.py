"""
{
  "status": "ok",
  "data": {
    "userId": 165526,
    "photoFilename": "default-user.png",
    "distanceUnits": "km",
    "currency": "usd"
  }
}
"""

from marshmallow import Schema, fields, validate, ValidationError
from enum import Enum


def is_more_than_1(value):
    if value < 1:
        raise ValidationError('Should be more than 0')


validator = validate.And(validate.Range(min=1), is_more_than_1)  # validate.Range(min=1) теж саме, що is_more_than_1


class DistanceUnits(Enum):
    km = 'km'
    ml = 'ml'


class UserSchema(Schema):
    userId = fields.Int(required=True, validate=validator)
    distanceUnits = fields.Enum(enum=DistanceUnits, required=True)
    currency = fields.Str(required=True)
    photoFilename = fields.Str(required=True)


class CurrentSchema(Schema):
    status = fields.Str(required=True)
    data = fields.Nested(UserSchema, required=True)



if __name__=='__main__':

    user = {
      "status": "ok",
      "data": {
        "userId": 165526,
        "photoFilename": "default-user.png",
        "distanceUnits": "km",
        "currency": "usd"
      }
    }
    incorrect_user = {
      "status": "ok",
      "data": {
        "userId": 0,
        "photoFilename": "default-user.png",
        "distanceUnits": "km",
        "currency": "usd"
      }
    }

    # щоб описати список вказуємо many=True
    CurrentSchema().load([user, user, incorrect_user, user], many=True)



