from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView, ListView
from .models import MenuItem#,MenuPost
from .forms import *
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models.functions import TruncDate
from django.db.models import Count
from .models import Record

# Create your views here.

#新しく部位別メニューを作成ができてない
#トレーニング記録がタイトルとコメントとかしかない


class LoginTopView(TemplateView):
    template_name ='login_top.html'

class IndexView(TemplateView):
    template_name = 'index.html'

#いまこのクラス使ってない
@method_decorator(login_required, name='dispatch')
class CreateMenuView(CreateView):
    '''メニュー投稿ページのビュー
    
    MenuPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
      form_class: モデルとフィールドが登録されたフォームクラス
      template_name: レンダリングするテンプレート
      success_url: データベスへの登録完了後のリダイレクト先
    '''
    # forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = MenuItemForm
    #def renda(self):    
        #menu_items = MenuItem.objects.select_related('post').all()

    # レンダリングするテンプレート
    template_name = "post_menu.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('training:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているPhotoPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CreatetrainingView(CreateView):
    #筋トレ記録を作るビュー
    
    form_class = HistoryForm
    # レンダリングするテンプレート
    template_name = "create_menu.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('training:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているPhotoPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


class RecordHistoryView(ListView):
    """行った記録表示のビュー"""
    model = Record
    template_name = 'record_list.html'
    context_object_name = 'items'
    queryset = Record.objects.order_by('-posted_at')
    paginate_by = 7


    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、
      get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # self.kwargsでキーワードの辞書を取得し、
      # userキーの値(ユーザーテーブルのid)を取得
      user_id = self.kwargs['user']
      # filter(フィールド名=id)で絞り込む
      user_list = Record.objects.filter(
        user=user_id).order_by('day')
      # クエリによって取得されたレコードを返す
      return user_list
    


class RecordListView(ListView):
    """部位別トレーニングメニューのビュー"""
    model = MenuItem
    template_name = 'menu_list.html'
    context_object_name = 'items'
    queryset = MenuItem.objects.order_by('-posted_at')
    paginate_by = 7
    
    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、
      get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # self.kwargsでキーワードの辞書を取得し、
      # userキーの値(ユーザーテーブルのid)を取得
      user_id = self.kwargs['user']
      # filter(フィールド名=id)で絞り込む
      user_list = MenuItem.objects.filter(
        user=user_id).order_by('parts')
      # クエリによって取得されたレコードを返す
      return user_list

# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
    '''
    # index.htmlをレンダリングする
    template_name ='post_success.html'





