from django.db import models


# Create your models here.

class User(models.Model):
    """
    いるかどうかわからない。
    すでにあるモデルでまかなえるなら消すかも
    """

    passwordHash = models.CharField(max_length=50)
    email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)
    followUsers = models.ManyToManyField('self', through='Follow', symmetrical=False, related_name='related_follows+')


class UserProfile(models.Model):
    """
    プロフィールを表す
    """

    introduction = models.CharField(max_length=50, blank=True)
    photoPath = models.CharField(max_length=50, blank=True)
    targetWeight = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(blank=True)


class Information(models.Model):
    """
    その日の体重と測定した日を表す
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=3, decimal_places=3)
    measuredAt = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(blank=True)


class Comment(models.Model):
    """
    コメントはお互いにフォローしている人もしくは自分に対して行える
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    # 削除されたコメントを表す。投稿者本人か、そのチャットの持ち主のみ削除できる
    isHidden = models.BinaryField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(blank=True)


class Follow(models.Model):
    """
    ユーザからユーザへのフォロー
    フォローしておくことでその人の情報にアクセスできるし
    チャット（コメント）機能を使って盛り上がることもできる

    Parameters
    -----
    isRequesting : bool
        リクエスト中でまだ承認されてない

    """

    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_users')
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_users')
    isRequesting = models.BinaryField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
