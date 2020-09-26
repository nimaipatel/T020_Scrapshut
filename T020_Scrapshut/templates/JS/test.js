$(document).ready(function() {
    $(".menu-icon").on("click", function() {
          $("nav ul").toggleClass("showing");
    });
});

// Scrolling Effect

$(window).on("scroll", function() {
    if($(window).scrollTop()) {
          $('nav').addClass('black');
    }

    else {
          $('nav').removeClass('black');
    }
})
$(document).ready(function(){
    var dark= document.getElementById("dark-mode");
    dark.addEventListener("click",function(){
        document.getElementById("dark").style.color="white";
        document.getElementById("dark").style.backgroundColor="black";
    });
    var light= document.getElementById("light-mode");
    light.addEventListener("click",function(){
        document.getElementById("dark").style.color="black";
        document.getElementById("dark").style.backgroundColor="white";
    });
    var count = 1;
    var incr = document.getElementById("increment");
    incr.addEventListener("click", function() {
        var incr = document.getElementById("count");
        incr.innerText = count;
        if(count>0)
        count++;
        });
        var count = 1;
        var decr= document.getElementById("decrement");
        decr.addEventListener("click", function() {
        var decr = document.getElementById("count");
        decr.innerText = count;
        if(count>1)
        count--;
        else
        count=1;
        });
});