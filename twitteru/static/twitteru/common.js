
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



$(".like-btn").click(function (e) {
    e.preventDefault()
    const this_ = $(this);
    const like_cnt = this_.children("span");
    const likeUrl = this_.attr("data-href");
    const post_id = this_.attr("data-post_id");
    if (likeUrl) {
        $.ajax({
            url: likeUrl,
            method: "GET",
            data: { "status": 1, "post_id": post_id }, //　いいねが押されましたと伝える
            success: function (data) {
                let change_like = like_cnt.text();
                console.log(change_like);
                if (data.liked) {　//　もしいいねされていたら
                    this_.removeClass("like_on");//　ボタンのデザインを初期状態に
                    like_cnt.text(String(data.liked_num));
                } else {　　//　もしいいねされていなかったら
                    this_.addClass("like_on");　//　ボタンをピンクに
                    like_cnt.text(String(data.liked_num));　//　いいねの数を１追加
                }
            }, error: function (error) {
                console.log("error")
            }
        })
    }
});



$(".btn-search-bar").submit(function (e) {
    e.preventDefault()
    const this_ = $(this);
    const followUrl = this_.attr("data-href");
    const followed_user_id = this_.attr("data-followed_user_id");
    if (followUrl) {
        $.ajax({
            url: followUrl,
            method: "GET",
            data: { "status": 1, "followed_user_id": followed_user_id }, //　いいねが押されましたと伝える
            success: function (data) {
                if (data.followed) {　//　もしいいねされていたら
                    this_.removeClass("follow_on");//　ボタンのデザインを初期状態に
                } else {　　//　もしいいねされていなかったら
                    this_.addClass("follow_on");　//　ボタンをピンクに
                }
            }, error: function (error) {
                console.log("error")
            }
        })
    }
});