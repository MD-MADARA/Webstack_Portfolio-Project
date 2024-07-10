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

document.addEventListener("DOMContentLoaded", function() {
  const categories = ["Sweater", "Jeans", "T-shirt", "Suit", "Dress", "Hoodie"]
  categories.forEach(category => {
    const types = ["Men", "Women"]
    types.forEach(type => {
      let url =`http://127.0.0.1:5001/api/products/${type}/${category}?order_desc=id&limit=10`
      fetch(url)
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
  });
});
