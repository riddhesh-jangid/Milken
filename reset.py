from io import StringIO
from django.core.management import call_command
from django.db import connection


app_name = 'start'

# Get SQL commands from sqlsequencereset
output = StringIO.StringIO()
call_command('sqlsequencereset', app_name, stdout=output, no_color=True)
sql = output.getvalue()

with connection.cursor() as cursor:
    cursor.execute(sql)

output.close()