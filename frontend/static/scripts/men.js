function createProductDiv(product) {
    var productDiv = document.createElement('div');
      productDiv.classList.add('row');
      new_price = product.price - product.price * (product.discount / 100)
      productDiv.innerHTML = `
        <div class="card-img">
          <a href="/product/${product.id}">
            <img src="../static/images/${product.category_type}/${product.category_name}/product_ID_${product.id}/img1.WEBP" alt="">
          </a>
          <div class="product-text">
            <h5>hot</h5>
          </div>
          <button class="card-btn" onclick="addToCartePopUp('${product.id}');">add to cart</button>
        </div>
        <div class="heart-icon">
          <i class="bx bx-heart"></i>
        </div>
        <div class="price">
          <h4>${product.title}</h4>
          <p>$${new_price.toFixed(2)} &nbsp;&nbsp;&nbsp;<span class="line-through">$${product.price.toFixed(2)}</span></p>
        </div>
      `;
      document.querySelector('.products').appendChild(productDiv);
  }

const caregories = ["Suit", "Sweater", "Hoodie", "T-shirt", "Jeans"]
caregories.forEach(category => {
  fetch(`http://127.0.0.1:5001/api/products?category_type=Men&order_desc=id&category_name=${category}&limit=5`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    data.forEach(product => {
      createProductDiv(product);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
    document.getElementById('result').textContent = 'Error: ' + error;
  });
});

// Function to handle radio input click
function handleRadioClick(event) {
  const category_name = event.target.value;
  var products = document.querySelector('.products');
  while (products.firstChild) {
    products.removeChild(products.firstChild);
  }

  fetch(`http://127.0.0.1:5001/api/products?category_type=Men&order_desc=id&category_name=${category_name}`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    data.forEach(product => {
      createProductDiv(product);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
    document.getElementById('result').textContent = 'Error: ' + error;
  });
  }





document.addEventListener("DOMContentLoaded", function() {
  const radioInputs = document.querySelectorAll('input[type="radio"]');
  
  radioInputs.forEach(input => {
  input.addEventListener('click', handleRadioClick);
  });

});
