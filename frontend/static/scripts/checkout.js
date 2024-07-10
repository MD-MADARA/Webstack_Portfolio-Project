var totalVAlue = document.querySelector(".total-value");


function handlePlus(button, price) {
    var amountElement = button.parentNode.querySelector('.amount');
    var amount = parseInt(amountElement.innerText);
    if (amount < 10) {
        amount++;
        amountElement.innerText = amount;
        let subtotal = (amount * price).toFixed(2)
        var sub = button.parentNode.parentNode.parentNode.parentNode.querySelector(".sub");
        sub.innerHTML = `<b>$${subtotal}</b>`
        totalVAlue.innerText = (parseFloat(totalVAlue.innerText) + price).toFixed(2);
    }
}

function handleMinus(button, price) {
    var amountElement = button.parentNode.querySelector('.amount');
    var amount = parseInt(amountElement.innerText);
    if (amount > 1) {
        amount--;
        amountElement.innerText = amount;
        let subtotal = (amount * price).toFixed(2)
        var sub = button.parentNode.parentNode.parentNode.parentNode.querySelector(".sub");
        sub.innerHTML = `<b>$${subtotal}</b>`
        totalVAlue.innerText = (parseFloat(totalVAlue.innerText) - price).toFixed(2);
    }
}


function createProductRow(product) {
    
    new_price = product.price - product.price * (product.discount / 100);
    totalVAlue.innerText = (parseFloat(totalVAlue.innerText) + new_price).toFixed(2);
    var productRow = document.createElement('div');
    productRow.classList.add('checkout-row', 'Products');
    productRow.innerHTML = `
    <div class="checkout-column col1 prod-column">
        <div class="product-card">
        <a href="/product/${product.id}"><img src="../static/images/${product.category_type}/${product.category_name}/product_ID_${product.id}/img1.WEBP" class="product-img" alt="product"></a>
                
        <div class="product-info">
            <p class="product-title">${product.title}</p>
        <p><span><b>$${new_price.toFixed(2)}</b></span>
        </div>
        </div>
    </div>
    <div class="checkout-column col2">
        <div class="buttons" style="width: 100%">
            <div class="amount-btn">
            <button id="minus" onclick="handleMinus(this, ${new_price.toFixed(2)})">
                <img src="../static/images/icon-minus.svg" alt="minus" />
            </button>
            <p class="amount">1</p>
            <button id="plus" onclick="handlePlus(this, ${new_price.toFixed(2)})">
                <img src="../static/images/icon-plus.svg" alt="plus" />
            </button>
            </div>
        </div>
    </div>
    <div class="checkout-column col3">
        <p class="sub">
            <b>$${new_price.toFixed(2)}</b>
        </p>
    </div>`
    let checkoutContainer = document.querySelector(".checkout-container");
    checkoutContainer.appendChild(productRow);

}
document.addEventListener("DOMContentLoaded", function() {
    const userid = localStorage.getItem('id');
    fetch(`http://127.0.0.1:5001/api/users/${userid}/cart`)
    .then(response => {
      return response.json();
    })
    .then(data => {
        if (data.length == 0) {
            document.querySelector(".checkout-section").innerHTML = `
            <div class="emty_cart_img"></div>
            `
            document.querySelector(".checkout-section").classList.add("relative");
        } else {
            data.forEach(product => {
                createProductRow(product);
            });
        };
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
      document.getElementById('result').textContent = 'Error: ' + error;
    });
    const buyNow = document.querySelector(".buy-now");
    buyNow.addEventListener('click', () =>{
        window.location.replace('/payment');
    })

});
