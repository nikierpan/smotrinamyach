height()

document.addEventListener("DOMContentLoaded", function(event)
{
    window.onresize = function() {
        if (!navigator.userAgent.includes('Safari')) {
            height();
        }
    };
});

function height() {
    let windowHeight = window.innerHeight.toString();
    let windowWidth = window.innerWidth.toString();
    let el_0 = document.getElementsByClassName('page-header').item(0);
    el_0.style.height = windowHeight;
    el_0.style.width = windowWidth;
}


let img_white = new Image();
img_white.src = "/static/media/LOGO-WHITE.png";
img_white.width = 230
let img = document.getElementsByClassName('navbar-brand').item(0);
img.appendChild(img_white)
let img_dark = new Image();
img_dark.src = "/static/media/LOGO-DARK.png";
img_dark.width = 230

$(window).scroll(function() {
    if ($(this).scrollTop() > 0){
        $('header').addClass("sticky").removeClass("not-sticky");
        $('nav').addClass("navbar-light").removeClass("navbar-dark");
        try {
            img.removeChild(img_white);
        } finally {
            img.appendChild(img_dark);
        }

    }
    else{
        $('header').removeClass("sticky").addClass("not-sticky");
        $('nav').removeClass("navbar-light").addClass("navbar-dark");
        img.removeChild(img_dark);
        img.appendChild(img_white);
    }
});
