$('.loginBtn').onclick(function () {
    $('.login').show();
    $('.signUp').hide();
    /* border bottom on button click */
    $('.loginBtn').css({ 'border-bottom': '2px solid #ff4141' });
    /* remove border after click */
    $('.signUpBtn').css({ 'border-style': 'none' });
});