
from django.contrib import admin
from .models import MenuItem, Record

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'parts', 'content', 'weight', 'rep', 'posted_at')
    search_fields = ('parts', 'content', 'memo')
    list_filter = ('parts', 'user')

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'menu_item', 'posted_at')
    list_select_related = ('menu_item',)  # 表示高速化（任意）
    list_filter = ('user', 'posted_at')