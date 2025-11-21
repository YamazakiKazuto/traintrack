from django.contrib import admin
# CustomUserをインポート
from .models import MenuItem,Record

class CategoryAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'content')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'content')

class MenuPostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'content')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'content')

# Django管理サイトにCategory、CategoryAdminを登録する


# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(MenuItem, MenuPostAdmin)
admin.site.register(Record, MenuPostAdmin)
