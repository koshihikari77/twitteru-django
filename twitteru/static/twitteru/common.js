
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

$(function () {
    const this_ = $(".like-btn");
    const likeUrl = this_.attr("data-href"); // ユーザーのステータス情報
    const post_id = this_.attr("data-post_id");//いいねされたtweetのid
    const like_btn_id = "#like_btn_" + String(post_id);
    $.ajax({
        url: likeUrl,
        method: "GET",
        data: { "status": 0, "post_id": post_id },　// ユーザーのステータス情報を変更しないように
        success: function (data) {
            if (data.liked) {　// もしユーザーが既にいいねをしていた場合
                $(like_btn_id).addClass("on");　// ボタンをピンクにする
            }
        }, error: function (error) {
            console.log("error")
        }
    })
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
                    this_.removeClass("on");//　ボタンのデザインを初期状態に
                    like_cnt.text(String(data.liked_num));
                } else {　　//　もしいいねされていなかったら
                    this_.addClass("on");　//　ボタンをピンクに
                    like_cnt.text(String(data.liked_num));　//　いいねの数を１追加
                }
            }, error: function (error) {
                console.log("error")
            }
        })
    }
});