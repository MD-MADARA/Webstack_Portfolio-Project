function Simular_products(p_ctgName, p_ctgType, from, p_id) {
  fetch(`http://127.0.0.1:5001/api/products/${p_ctgType}/${p_ctgName}?from=${from}&ignore=${p_id}&limit=15&order_desc=id`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const responseLength = data.length;
    if (responseLength > 0) {
      document.querySelector(".simular_heading").classList.remove("hidden");
      if (responseLength == 15) {
        document.querySelector(".show-more").classList.remove("hidden");
      } else {
        document.querySelector(".show-more").classList.add("hidden");
      }
    }
    data.forEach(product => {
        var productDiv = document.createElement('div');
        productDiv.classList.add('row');
        new_price = product.price - product.price * (product.discount / 100)
        productDiv.innerHTML = `
        <div class="card-img">
          <a href="/product/${product.id}">
              <img src="../static/images/${product.category_type}/${product.category_name}/product_ID_${product.id}/img1.WEBP" alt="">
          </a>
          <div class="product-discount">
              <h5>${product.discount}% Off</h5>
          </div>
          <button class="card-btn" onclick="addToCartePopUp('${product.id}')">add to cart</button>
        </div>
        <div class="heart-icon">
            <i class="bx bx-heart"></i>
        </div>
        <div class="price">
            <h4>${product.title}</h4>
            <p>$${new_price.toFixed(2)} &nbsp;&nbsp;&nbsp;<span class="line-through">$${product.price.toFixed(2)}</span></p>
        </div>
        `;
        document.querySelector('.also_viewed').appendChild(productDiv);

    });
  })
  .catch(error => {
  console.error('There was a problem with the fetch operation:', error);
  });
}

document.addEventListener("DOMContentLoaded", function() {
    let path = window.location.pathname;
    let product_id = path.split('product/').pop();
    
    
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
        let from = 0
        document.getElementById("dynamicTitle").innerText = p_title
        Simular_products(p_ctgName, p_ctgType, from, p_id)
        document.querySelector(".thumbnails").innerHTML =`
        <img
          src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP"
          alt="product"
          class="main-thumbnail invisible-mob"
        />
        <div class="mobile-thumb hidden">
          <img
            src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP"
            class="thumb-mob"
            alt="product"
          />
          <button id="next">
            <img src="../static/images/icon-next.svg" alt="next" />
          </button>
          <button id="previous">
            <img src="../static/images/icon-previous.svg" alt="previos" />
          </button>
        </div>
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
        document.querySelector(".content").innerHTML = `
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
            <input type="radio" id="size-xs" name="size" value="XS">
            <label for="size-xs">XS</label>
          </div>
          <div class="size-option">
            <input type="radio" id="size-s" name="size" value="S">
            <label for="size-s">S</label>
          </div>
          <div class="size-option">
            <input type="radio" id="size-m" name="size" value="M">
            <label for="size-m">M</label>
          </div>
          <div class="size-option">
            <input type="radio" id="size-l" name="size" value="L">
            <label for="size-l">L</label>
          </div>
          <div class="size-option">
            <input type="radio" id="size-xl" name="size" value="XL">
            <label for="size-xl">XL</label>
          </div>
          <div class="size-option">
            <input type="radio" id="size-xxl" name="size" value="XXL">
            <label for="size-xxl">XXL</label>
          </div>
        </form>
        <div class="buttons">
          <button class="add_btn">
            <img src="../static/images/icon-cart.svg" alt="cart" />
            Add to cart
          </button>
        </div>`

        const mainThumbnail = document.querySelector(".main-thumbnail");
        const images = document.querySelectorAll(".preview img");
        // const plusBtn = document.querySelector("#plus");
        // const minusBtn = document.querySelector("#minus");
        // const amount = document.querySelector(".amount");
        const nextBtn = document.getElementById("next");
        const prevBtn = document.getElementById("previous");
        const thumbMob = document.querySelector(".thumb-mob");
        const addBtn = document.querySelector(".add_btn");
        const indicator = document.querySelector(".indicator");
        const cart = document.querySelector(".cart-wrp");
        const wrp = document.querySelector(".cart-content");
        const more = document.querySelector(".show-more");
        let amountValue = 1;
        let currentImg = 1;

        // indicator.style.display = "none";
    
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

        function nextImage() {
            if (currentImg == 4) {
                currentImg = 1;
            } else {
                currentImg++;
            }
            thumbMob.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img${currentImg}.WEBP`;
        }

        function prevImage() {
            if (currentImg == 1) {
                currentImg = 4;
            } else {
                currentImg--;
            }
            thumbMob.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img${currentImg}.WEBP`;
        }

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
                  if (!response.ok) {
                    throw new Error('Network response was not ok');
                  }
                    return response.json();
                })
                .then(data => {
                  if (data.total == 1) {
                    wrp.classList.remove("empty");
                    wrp.innerHTML = "";
                  }
                  let total = new_price * amountValue;
                  if (data.total > 1) {
                    document.querySelector(".checkout-btn").style.display = "none"
                  }
                  var checkout_btn = document.createElement('button');
                  checkout_btn.className = 'checkout-btn';
                  checkout_btn.innerHTML = "Checkout";
                  var productDiv = document.createElement('div');
                  productDiv.className = 'product';
                  productDiv.innerHTML =
                  `<div>
                      <a href="/product/${p_id}"><img src="../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img1.WEBP" class="product-img" alt="product"></a>

                      <div class="product-info">
                          <p class="product-title">${p_title}</p>
                          <p><span>$${new_price.toFixed(2)}</span> × <span class="number">${amountValue}</span> <b>$${total.toFixed(2)}</b></p>
                      </div>
                      <button class="delete-btn" onclick="
                          fetch('http://127.0.0.1:5001/api/users/${user_id}/cart/${p_id}', {method: 'DELETE'})
                          .then(response => {
                              return response.json();
                          })
                          .then(data => {
                              const indicator = document.querySelector('.indicator');
                              indicator.innerText = data.left;
                              if (data.left == 0) {
                                  const wrp = document.querySelector('.cart-content');
                                  indicator.style.display = '';
                                  wrp.classList.add('empty');
                                  wrp.innerHTML = '<p>Your cart is empty</p>';
                              };
                          })
                          .catch(error => {});
                          this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode);
                          "><img src="../static/images/icon-delete.svg" alt="delete"></button>
                  </div>`
                  wrp.appendChild(productDiv);
                  wrp.appendChild(checkout_btn);
                  indicator.innerText = data.total;
                  addBtn.removeEventListener("click", addItem);
                  checkout_btn.addEventListener("click", checkoutPage);
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
                    mainThumbnail.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img3.WEBP`;
                    break;
                case `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img4.WEBP`:
                    mainThumbnail.src = `../static/images/${p_ctgType}/${p_ctgName}/product_ID_${p_id}/img4.WEBP`;
                    break;
                }
            });
        });
        // plusBtn.addEventListener("click", handlePlus);
        // minusBtn.addEventListener("click", handleMinus);
        nextBtn.addEventListener("click", nextImage);
        prevBtn.addEventListener("click", prevImage);
        addBtn.addEventListener("click", addItem);
        more.addEventListener("click", () => {
          from += 15;
          Simular_products(p_ctgName, p_ctgType, from, p_id);
        });
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
})
