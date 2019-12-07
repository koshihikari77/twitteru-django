
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

$(".tweet-card").click(function () {
    const this_ = $(this);
    const contentUrl = this_.attr("data-content-href");
    window.location.href = contentUrl;
});


$(".tweet-card").hover(function () {
    $(this).css('background', "#EEFFFF")
}, function () {
    $(this).css('background', "")
});


$(".reply-btn").click(function (e) {
    e.preventDefault();
    e.stopPropagation();
    const this_ = $(this);
    $("#reply-modal").modal("show");
})


$(".like-btn").click(function (e) {
    e.preventDefault()
    e.stopPropagation()
    const this_ = $(this);
    const like_cnt = this_.children("span");
    const post_id = this_.attr("data-post-id");
    const like_url = "api/twitteru/"+post_id+"/like"
    if (likeUrl) {
        $.ajax({
            url: like_url,
            method: "GET",
            success: function (data) {
                let change_like = like_cnt.text();
                console.log(change_like);
                if (data.liked) {　//　もしいいねされていたら
                    this_.removeClass("like-on");//　ボタンのデザインを初期状態に
                    like_cnt.text(String(data.liked_num));
                } else {　　//　もしいいねされていなかったら
                    this_.addClass("like-on");　//　ボタンをピンクに
                    like_cnt.text(String(data.liked_num));　//　いいねの数を１追加
                }
            }, error: function (error) {
                console.log("error")
            }
        })
    }
});


$(".follow-btn").submit(function (e) {
    e.preventDefault()
    const this_ = $(this);
    const followUrl = this_.attr("data-href-follow");
    const followed_user_id = this_.attr("data-followed-user-id");
    console.log(followUrl)
    if (followUrl) {
        $.ajax({
            url: followUrl,
            method: "GET",
            data: { "status": 1, "followed_user_id": followed_user_id }, //　いいねが押されましたと伝える
            success: function (data) {
                if (data.followed) {　//　もしいいねされていたら
                    this_.removeClass("follow-on");//　ボタンのデザインを初期状態に
                } else {　　//　もしいいねされていなかったら
                    this_.addClass("follow-on");　//　ボタンをピンクに
                }
            }, error: function (error) {
                console.log("error")
            }
        })
    }
});

