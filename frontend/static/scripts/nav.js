function checkoutPage() {
    window.open("/checkout", "_blank");
}
document.addEventListener("DOMContentLoaded", function() {
    const nav = document.querySelector('nav');
    nav.innerHTML =
    `<div class="nav_container">
        <div class="nav_left-sec">
            <img
                src="../static/images/icon-menu.svg"
                id="menu-btn"
                alt="menu"
                class="hidden-btn menu"
            />
            <a href="/"><img src="../static/images/logo-fashion.png" alt="logo" class="nav_logo" /></a>
            <div class="overlay"></div>
            <ul class="nav_links">
                <img
                src="../static/images/icon-close.svg"
                alt="close"
                class="close-btn hidden-btn"
                />
                <a href ="/home"><li class="nav_link">Home</li></a>
                <a href ="/men"><li class="nav_link">Men's</li></a>
                <a href ="/women"><li class="nav_link">Women's</li></a>
                <a href ="/about"><li class="nav_link">About</li></a>
                <a href ="#footer"><li class="nav_link">Contact</li></a>
            </ul>
        </div>
        <div class="nav_right-sec">
            <!-- Cart -->
            <div class="cart-container">
                <button class="cart-btn">
                <span class="indicator"></span>
                <img src="../static/images/icon-cart.svg" alt="cart" class="cart" />
                </button>
                <div class="cart-wrp invisible">
                    <div class="sticky-heading">
                        <p class="cart-heading">Cart</p>
                        <div class="divider"></div>
                    </div>
                    <div class="cart-content empty">
                        <p>Your cart is empty</p>
                    </div>
                </div>
            </div>
            <div class="profile-logo"></div>
            <span class="username"></span>
        </div>
    </div>`

    const menuBtn = document.getElementById("menu-btn");
    const closeBtn = document.querySelector(".close-btn");
    const menu = document.querySelector(".nav_links");
    const overlay = document.querySelector(".overlay");
    const cartBtn = document.querySelector(".cart-btn");
    const cart = document.querySelector(".cart-wrp");
    const indicator = document.querySelector(".indicator");
    window.addEventListener('scroll', function() {
        if (window.scrollY > 0) {
            nav.classList.add('sticky');
        } else {
            nav.classList.remove('sticky');
        }
    });

    indicator.style.display = "none";
    function openMenu() {
        menu.classList.add("active");
        overlay.classList.add("active");
    };
    function closeMenu() {
        menu.classList.remove("active");
        overlay.classList.remove("active");
    };
    function toggleCart() {
        cart.classList.toggle("invisible");
    };

    menuBtn.addEventListener("click", openMenu);
    closeBtn.addEventListener("click", closeMenu);
    cartBtn.addEventListener("click", toggleCart);
    const userid = localStorage.getItem('id');
    const profile = document.querySelector(".profile-logo");
    const username = document.querySelector(".username");
    if (userid) {
        profile.innerHTML = `
        <a href="/profile"><img src="../static/images/image-avatar.png" alt="avatar" class="avatar"/></a>`
        // cart
        fetch(`http://127.0.0.1:5001/api/users/${userid}/cart`)
        .then(response => {
            return response.json();
        })
        .then(data => {
            const wrp = document.querySelector(".cart-content");
            if (data.length > 0){
                wrp.classList.remove("empty");
                wrp.innerHTML = "";
                var checkout_btn = document.createElement('button');
                checkout_btn.className = 'checkout-btn';
                checkout_btn.innerHTML = "Checkout";
                const indicator = document.querySelector('.indicator');
                indicator.style.display = "block";
                indicator.innerText = data.length;
            }
            data.forEach(product => {
                new_price = product.price - product.price * (product.discount / 100)
                let amountValue = 1;
                let total = new_price * amountValue;
                var productDiv = document.createElement('div');
                productDiv.className = 'product';
                productDiv.innerHTML = 
                `<div>
                    <a href="/product/${product.id}"><img src="../static/images/${product.category_type}/${product.category_name}/product_ID_${product.id}/img1.WEBP" class="product-img" alt="product"></a>
                
                    <div class="product-info">
                        <p class="product-title">${product.title}</p>
                    <p><span>$${new_price.toFixed(2)}</span> × <span class="number">${amountValue}</span> <b>$${total.toFixed(2)}</b></p>
                    </div>
                    <button class="delete-btn" onclick="
                        fetch('http://127.0.0.1:5001/api/users/${userid}/cart/${product.id}', {method: 'DELETE'})
                        .then(response => {
                            return response.json();
                        })
                        .then(data => {
                            const indicator = document.querySelector('.indicator');
                            indicator.innerText = data.left;
                            if (data.left == 0) {
                                const wrp = document.querySelector('.cart-content');
                                indicator.style.display = 'none';
                                wrp.classList.add('empty');
                                wrp.innerHTML = '<p>Your cart is empty</p>';
                            };
                        })
                        .catch(error => {});
                        this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode);
                        "><img src="../static/images/icon-delete.svg" alt="delete"></button>
                </div>`
                wrp.appendChild(productDiv);
            });
            wrp.appendChild(checkout_btn);
            checkout_btn.addEventListener("click", checkoutPage);
        })
        .catch(error => {
            console.log(error)
        });
    } else {
        profile.innerHTML = `
        <a href="/login"><img src="../static/images/login-logo.png" alt="avatar" class="avatar"/></a>`
    }

});
