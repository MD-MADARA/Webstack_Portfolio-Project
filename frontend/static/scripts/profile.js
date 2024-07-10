function logout() {
    localStorage.removeItem("id");
    localStorage.removeItem("token");
    window.location.replace("/home");
}
document.addEventListener("DOMContentLoaded", function() {
    const user_id = localStorage.getItem('id');
    fetch(`http://127.0.0.1:5001/api/users/${user_id}`)
    .then(res => res.json())
    .then(user => {
        document.querySelector(".user-details").innerHTML = 
        `<p><strong>First name:</strong> ${user.first_name}</p>
        <p><strong>Last name:</strong> ${user.last_name}</p>
        <p><strong>Email:</strong> ${user.email}</p>
        <p><strong>Address:</strong> ${user.address}</p>
        <p><strong>Phone:</strong> ${user.phone}</p>`
    })
    .catch(err => console.log(err))
});
