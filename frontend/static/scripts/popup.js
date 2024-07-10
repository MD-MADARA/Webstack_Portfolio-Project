function addToCartePopUp(product_id) {
  fetch('http://127.0.0.1:5001/api/products/' + product_id)
    .then(response => {
        if (!response.ok) { 
          throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const p_id = data.id;
        const p_title = data.title;
        const p_price = data.price;
        const p_disription = data.description;
        const p_discount = data.discount;
        const p_ctgType = data.category_type;
        const p_ctgName = data.category_name;
        let new_price = p_price - p_price * (p_discount / 100);
        const preveiwContainer = document.querySelector('.products-preview');
        const closePopup = document.querySelector('.products-preview .fa-times');
        preveiwContainer.classList.remove("hidden");
        document.querySelector(".products-preview .thumbnails").innerHTML =`
        <img
          src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP"
          alt="product"
          class="main-thumbnail"
        />

        <div>
          <div class="preview">
            <img
              class="selected"
              src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP"
              alt=""
            />
            <img src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img2.WEBP" alt="" />
            <img src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img3.WEBP" alt="" />
            <img src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img4.WEBP" alt="" />
          </div>
        </div>`
        document.querySelector(".products-preview .content").innerHTML = `
        <h1 class="title">${p_title}</h1>
        <div class="info">
          <h3>Description:</h3>
          ${p_disription}
        </div>
        <div class="price">
          <div class="new-price">
            <p class="now">$${new_price.toFixed(2)}</p>
            <span>${p_discount}% Off</span>
          </div>
          <p class="old-price">$${p_price.toFixed(2)}</p>
        </div>
        <form class="size-selector">
          <div class="size-option">
            <input type="radio" id="popup-size-xs" name="option" value="XS">
            <label for="popup-size-xs">XS</label>
          </div>
          <div class="size-option">
            <input type="radio" id="popup-size-s" name="option" value="S">
            <label for="popup-size-s">S</label>
          </div>
          <div class="size-option">
            <input type="radio" id="popup-size-m" name="option" value="M">
            <label for="popup-size-m">M</label>
          </div>
          <div class="size-option">
            <input type="radio" id="popup-size-l" name="option" value="L">
            <label for="popup-size-l">L</label>
          </div>
          <div class="size-option">
            <input type="radio" id="popup-size-xl" name="option" value="XL">
            <label for="popup-size-xl">XL</label>
          </div>
          <div class="size-option">
            <input type="radio" id="popup-size-xxl" name="option" value="XXL">
            <label for="popup-size-xxl">XXL</label>
          </div>
        </form>
        <div class="buttons">
        <!--<div class="amount-btn">
        <button id="minus">
          <img src="../static/images/icon-minus.svg" alt="minus" />
        </button>
        <p class="amount">0</p>
        <button id="plus">
          <img src="../static/images/icon-plus.svg" alt="plus" />
        </button>
        </div>-->
          <button class="add_btn">
            <img src="../static/images/icon-cart.svg" alt="cart" />
            Add to cart
          </button>
        </div>`
        setTimeout(function() {
          preveiwContainer.style.opacity = "1";
        }, 50);

        const mainThumbnail = document.querySelector(".products-preview .main-thumbnail");
        const images = document.querySelectorAll(".products-preview .preview img");
        // const plusBtn = document.querySelector(".products-preview #plus");
        // const minusBtn = document.querySelector(".products-preview #minus");
        // const amount = document.querySelector(".products-preview .amount");
        const addBtn = document.querySelector(".products-preview .add_btn");
        const indicator = document.querySelector(".indicator");
        const wrp = document.querySelector(".cart-content");
        const cart = document.querySelector(".cart-wrp");
        let amountValue = 1;


        indicator.style.display = "none";
    
        // function handlePlus() {
        // amountValue++;
        // amount.innerText = amountValue;
        // }

        // function handleMinus() {
        // if (amountValue > 0) {
        //     amountValue--;
        // }
        // amount.innerText = amountValue;
        // }
        // function addItem() {
        //     if (amountValue > 0) {
        //         let total = new_price * amountValue;
        //         wrp.classList.remove("empty");
        //         wrp.innerHTML = `
        //         <div class="product">
        //             <div>
        //             <img src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP" class="product-img" alt="product">
        //             <div class="product-info">
        //                 <p class="product-title">${p_title}</p>
        //             <p><span>$${new_price.toFixed(2)}</span> × <span class="number">${amountValue}</span> <b>$${total.toFixed(2)}</b></p>
        //             </div>
        //             <button class="delete-btn" onclick='
        //                 wrp = document.querySelector(".cart-content");
        //                 wrp.classList.add("empty");
        //                 wrp.innerHTML = "<p>Your cart is empty</p>";
        //             '><img src="../static/images/icon-delete.svg" alt="delete"></button>
        //             </div>
        //             <button class="checkout-btn">Checkout</button>
        //         </div>
        //         `;
        //         indicator.style.display = "block";
        //         indicator.innerText = amountValue;
        //         cart.classList.remove("invisible");
        //         setTimeout(() => {
        //           cart.classList.add("invisible");
        //         }, 2000);
        //     }
        // }
        function addItem() {
          if (amountValue > 0) {
            const user_id = localStorage.getItem('id');
            if (user_id) {
              const data = {"product_id": p_id};
              fetch(`http://127.0.0.1:5001/api/users/${user_id}/cart/`, {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
              })
              .then(response => {
                  return response.json();
              })
              .catch(error => {
                //
              });
            } else {
              let total = new_price * amountValue;
              wrp.classList.remove("empty");
              wrp.innerHTML = `
              <div class="product">  
                  <div>
                  <a href="/product/${p_id}"><img src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP" class="product-img" alt="product"></a>
                  <div class="product-info">
                      <p class="product-title">${p_title}</p>
                  <p><span>$${new_price.toFixed(2)}</span> × <span class="number">${amountValue}</span> <b>$${total.toFixed(2)}</b></p>
                  </div>
                  <button class="delete-btn" onclick='
                      wrp = document.querySelector(".cart-content");
                      wrp.classList.add("empty");
                      wrp.innerHTML = "<p>Your cart is empty</p>";
                  '><img src="../static/images/icon-delete.svg" alt="delete"></button>
                  </div>
                  <button class="checkout-btn">Checkout</button>
              </div>
              `;
              indicator.style.display = "block";
              indicator.innerText = amountValue;
            }
            cart.classList.remove("invisible");
            setTimeout(() => {
              cart.classList.add("invisible");
            }, 2000);
          }
      }

        images.forEach((image) => {
            image.addEventListener("click", () => {
                const lastImg = document.querySelectorAll(".selected");
                if (lastImg) {
                lastImg[0].classList.remove("selected");
                }
                image.classList.add("selected");
                const selectedImg = document.querySelector(".selected");
                
                switch (selectedImg.getAttribute("src")) {
                case `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP`:
                    mainThumbnail.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP`;
                    break;
                case `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img2.WEBP`:
                    mainThumbnail.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img2.WEBP`;
                    break;
                case `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img3.WEBP`:
                    mainThumbnail.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP`;
                    break;
                case `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img4.WEBP`:
                    mainThumbnail.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img4.WEBP`;
                    break;
                }
            });
        });
        function closeProductPreview() {
          preveiwContainer.style.opacity = "0";
          setTimeout(function() {
            preveiwContainer.classList.add("hidden");
          }, 300);
        };
        // plusBtn.addEventListener("click", handlePlus);
        // minusBtn.addEventListener("click", handleMinus);
        addBtn.addEventListener("click", addItem);
        closePopup.addEventListener("click", closeProductPreview);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
