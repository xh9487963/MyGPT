document.addEventListener('DOMContentLoaded', fetchUser);


async function fetchUser() {
    const select =  document.getElementById('username')
    for(i = 1; i <= 30; i ++) {
        const option = document.createElement('option');  
        option.value = 'user' + i;  
        option.textContent = 'user' + i;;  
        select.appendChild(option); 
    }
    if (localStorage.getItem("USER_NAME") != null) {
        select.value = localStorage.getItem('USER_NAME');
    } else {
        localStorage.setItem("USER_NAME", 'user1'); 
        select.value = localStorage.getItem('USER_NAME');
        console.log(localStorage.getItem("USER_NAME")); 
    }
}

function changeUser(username) {  
    localStorage.setItem("USER_NAME", username);  
    console.log(localStorage.getItem("USER_NAME")); 
    location.reload();  
}