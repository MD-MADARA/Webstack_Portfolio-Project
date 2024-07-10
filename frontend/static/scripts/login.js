document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector('form');
    form.addEventListener('submit', handleSubmit);

    function handleSubmit(event){
        event.preventDefault();
        let formData = new FormData(form);
        let data = Object.fromEntries(formData);
        console.log("data", data)
        let jsonData = JSON.stringify(data);

        fetch('http://127.0.0.1:5001/api/login',{
        method: 'POST',
        headers: {
            'Content-type' : 'application/json'
        },
        body: jsonData
        }).then(res => res.json())
        .then(result => {
            // alert(result.description);
            if (result.message == "login successful") {
                localStorage.setItem('id', result.user_id);
                localStorage.setItem('token', result.token);
                window.location.replace("/home");
            } else {
                alert(result.error)
            }
        })
        .catch(err => console.log(err))
    }
})
