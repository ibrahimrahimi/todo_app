from django.contrib import admin

from .models import Task
from .models import Task_item
from .models import Repeate_type
from .models import(User)


admin.site.register(Task)
admin.site.register(Task_item)
admin.site.register(Repeate_type)
admin.site.register(User)

