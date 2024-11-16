const genSwiper = new Swiper('.genSwiper', {
    slidesPerView: 'auto',
    spaceBetween: 30,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        320: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        480: {
            slidesPerView: 3,
            spaceBetween: 15,
        },
        640: {
            slidesPerView: 4,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 5,
            spaceBetween: 25,
        },
       1024: {
            slidesPerView: 6,
            spaceBetween: 30,
        },
    }
});

const livroSwiper = new Swiper('.livroSwiper', {
    slidesPerView: 2,
    spaceBetween: 20,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        320: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        480: {
            slidesPerView: 3,
            spaceBetween: 15,
        },
        640: {
            slidesPerView: 3,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 4,
            spaceBetween: 30,
        },
        1024: {
            slidesPerView: 5,
            spaceBetween: 30,
        },
    }
});

const resenhaSwiper = new Swiper('.resenhaSwiper', {
    slidesPerView: 1,
    spaceBetween: 20,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
       640: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    }
}); 

const clubeSwiper = new Swiper('.clubeSwiper', {
    slidesPerView: 1,
    spaceBetween: 20,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
       640: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    }
});

const notSwiper = new Swiper('.notSwiper', {
    slidesPerView: 1,
    spaceBetween: 20,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
       640: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    }
});




