document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector('form');
    form.addEventListener('submit', handleSubmit);

    function handleSubmit(event){
        event.preventDefault();
        let formData = new FormData(form);
        let data = Object.fromEntries(formData);
        console.log("data", data)
        let jsonData = JSON.stringify(data);

        fetch('http://127.0.0.1:5001/api/users',{
        method: 'POST',
        headers: {
            'Content-type' : 'application/json'
        },
        body: jsonData
        }).then(res => res.json())
        .then(result => {
            alert(result.description);
            if (result.description == "successfully registered") {
                window.location.replace("/login");
                fetch(`http://127.0.0.1:5001/api/users/${user_id}/orders/`,{
                    method: 'POST'})
                .then(res => res.json())
                .catch(err => console.log(err))
            }

        })
        .catch(err => console.log(err))
    };
});
