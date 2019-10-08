from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # 継承することで親クラスのfieldsやexcludesを変更できるようにする
        model = User
        fiels = ('username', 'email')  # モデルから入力フォームを生成する対象のフィールドを指定
