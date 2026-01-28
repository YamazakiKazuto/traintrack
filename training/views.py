from django.contrib.auth.decorators import login_required
from .models import MenuItem, Record

from django.views.generic import TemplateView, ListView

from .forms import *
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')
class CreatemaeView(ListView):
    model = MenuItem
    template_name = 'create_mae.html'
    context_object_name = 'items'
    paginate_by = 7

    def get_queryset(self):
        # ログインユーザーのメニューだけを表示
        return MenuItem.objects.filter(user=self.request.user).order_by('parts','-posted_at')

    def post(self, request):
        item_id = request.POST.get("item_id")
        item = get_object_or_404(MenuItem, id=item_id, user=request.user)

        # ユーザーが入力した値を取得
        weight = request.POST.get("weight")
        rep = request.POST.get("rep")
        memo = request.POST.get("memo")

    # Record に保存（MenuItem は更新しない）
        Record.objects.create(
            user=request.user,
            menu_item=item,
            weight=weight,
            rep=rep,
            memo=memo
        )

        # 保存後の遷移先：urls.py にある post_done に飛ばす
        return redirect('training:post_done')

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
    '''筋トレ記録のビュー'''
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
    queryset = Record.objects.order_by('posted_at')
    paginate_by = 7


    def get_queryset(self):

      # self.kwargsでキーワードの辞書を取得し、
      # userキーの値(ユーザーテーブルのid)を取得
      user_id = self.kwargs['user']
      # filter(フィールド名=id)で絞り込む
      user_list = Record.objects.filter(
        user=user_id).order_by('posted_at')
      # クエリによって取得されたレコードを返す
      return user_list
        

class CreateatoView(CreateView):
            #筋トレ記録を作
    form_class = HistoryForm
    # レンダリングするテンプレート
    template_name = "create_ato.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('training:post_done')


class RecordListView(ListView):
    """部位別トレーニングメニューのビュー"""
    model = MenuItem
    template_name = 'menu_list.html'
    context_object_name = 'items'
    queryset = MenuItem.objects.order_by('-posted_at')
    paginate_by = 7
    


# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
    '''
    # index.htmlをレンダリングする
    template_name ='post_success.html'





