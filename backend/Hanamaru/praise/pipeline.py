def set_user_data(backend, strategy, details, response, user=None, *args, **kwargs):
    """
    SNS認証時にプロバイダから取得したデータをプロフィールに設定する
    """
    if backend.name == "line":
    # ユーザー名を取得。取得できなかった場合はuserIdをユーザー名とする。
        username = response.get("displayName", response["userId"])

    user.username = username
    #user.sns_icon_url = icon_url
    user.save()
