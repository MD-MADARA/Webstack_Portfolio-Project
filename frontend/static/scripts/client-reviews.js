const productContainers = [...document.querySelectorAll('.review-container')];
const preBtn = [...document.querySelectorAll('.slider-pre-btn')];
const nextBtn = [...document.querySelectorAll('.slider-nxt-btn')];

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nextBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    });

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    });
});
