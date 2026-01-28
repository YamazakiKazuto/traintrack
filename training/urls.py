from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'training'

# URLパターンを登録する変数
urlpatterns = [

    path('', views.LoginTopView.as_view(), name='logintop'),
    
    
    path('mypage', views.IndexView.as_view(), name='index'),

    path('post_menu', views.CreateMenuView.as_view(), name='post_menu'),
    
     path('record_list/<int:user>/', views.RecordListView.as_view(), name='record_list'),

     path('record_history/<int:user>/',views.RecordHistoryView.as_view(), name='record_history'),


     path('record/create1/',views.CreatemaeView.as_view(), name='create_mae'),
     path('record/create2/<int:pk>/',views.CreateatoView.as_view(), name='create_ato'),

     #筋トレメニューで追加を押したときにメニューを出す
     
     #筋トレメニューで追加を押したときにメニューを出す


    # 筋トレ記録ページへのアクセスはviewsモジュールのCreateMenuViewを実行
    #path('post/',
     #    views.CreatetrainingView.as_view(),
      #   name='post'),    

    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    

    # 詳細ページ
    # photo-detail/<Photo postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される


]
