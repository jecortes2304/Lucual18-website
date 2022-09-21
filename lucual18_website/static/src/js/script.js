// odoo.define('lucual18_website.script', function (require) {
//     'use strict';

    const nav_offset_top = $('#my-custom-header').height() + 50;
    // function navbarFixed() {
        if ($('#my-custom-header').length) {
            $(window).scroll(function () {
                var scroll = $(window).scrollTop();
                if (scroll >= nav_offset_top) {
                    $('#my-custom-header').addClass('navbar_fixed');
                } else {
                    $('#my-custom-header').removeClass('navbar_fixed');
                }
            });
        // }
    }



    function changeActiveLink() {
        const items = document.querySelectorAll('.nav-item');

        items.forEach((link) => {
            link.addEventListener('click', (e) => {
                items.forEach((link) => {
                    link.classList.remove('active');
                });
                // e.preventDefault();
                link.classList.add('active');
            });
        });
    }

    changeActiveLink();


    var sections = $('section')
        , nav = $('nav')
        , nav_height = nav.outerHeight();

    $(window).on('scroll', function () {
        var cur_pos = $(this).scrollTop();

        sections.each(function () {
            var top = $(this).offset().top - nav_height,
                bottom = top + $(this).outerHeight();

            if (cur_pos >= top && cur_pos <= bottom) {
                nav.find('li').removeClass('active');
                sections.removeClass('active');

                $(this).addClass('active');
                nav.find('a[href="#' + $(this).attr('id') + '"]').parent("li").addClass('active');
            }
        });
    });

    nav.find('a').on('click', function () {
        var $el = $(this)
            , id = $el.attr('href');

        $('html, body').animate({
            scrollTop: $(id).offset().top - nav_height + 100
        }, 500);

        return false;
    });



//
// });
