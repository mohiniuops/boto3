import os
import boto3
import datetime
import time
import sys

db = boto3.resource('dynamodb')
table = db.Table("employees")

table.put_item(
Item = {
	'emp_id' : "2",
	'name' : "ShreeRam"
})
