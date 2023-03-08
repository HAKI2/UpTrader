from django.contrib import admin
from menu.models import MenuNode, MenuNodeTree

admin.site.register(MenuNode)
admin.site.register(MenuNodeTree)