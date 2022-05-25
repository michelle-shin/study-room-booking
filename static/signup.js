const form = document.getElementById('signup-form');
const nameInput = document.getElementById('name')
const studentIdInput = document.getElementById('studentID');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const password2Input = document.getElementById('password2');


form.addEventListener('submit', (event) => {
    validateForm();
    console.log(isFormValid())
    if (isFormValid()==true) {
        form.submit();
    }else {
        event.preventDefault();
    }
});

function isFormValid(){
    const inputContainers = form.querySelectorAll('.input-group');
    let result = true;
    inputContainers.forEach((container)=>{
        if(container.classList.contains('error')){
            result = false;
        }
    });
    return result;
}

function validateForm() {
    //name
    if (nameInput.value.trim() =='') {
        setError(nameInput, 'Name is required')
    }else {
        setSuccess(nameInput);
    }
    //student id
    if (studentIdInput.value.trim()=='') {
        setError(studentIdInput, 'Student ID is required')
    }else if(studentIdInput.value.trim().length < 9 || studentIdInput.value.trim().length > 9){
        setError(studentIdInput, 'Student ID must be 9 charecters');
    }else {
        setSuccess(studentIdInput);
    }
    //email
    if(emailInput.value.trim()=='') {
        setError(emailInput, 'Email is required')
    }else if(isEmailValid(emailInput.value)){
        setSuccess(emailInput);
    }else {
        setError(emailInput, 'Provide valid email address')
    }
    //password
    if(passwordInput.value.trim()=='') {
        setError(passwordInput, 'Password is required');
    }else if(passwordInput.value.trim().length <8 || passwordInput.value.trim().length >20){
        setError(passwordInput, 'Password must be at least 8 characters')
    }else {
        setSuccess(passwordInput)
    }
    //confirm pw
    if(password2Input.value.trim()=='') {
        setError(password2Input, 'Password is required')
    }else if(password2Input.value !== passwordInput.value) {
        setError(password2Input, 'Password does not match')
    }else {
        setSuccess(password2Input)
    }
}

function setError(element, errorMessage) {
    const parent = element.parentElement; 
    if(parent.classList.contains('success')) {
        parent.classList.remove('success');
    }
    parent.classList.add('error')
    const paragraph = parent.querySelector('p');
    paragraph.textContent = errorMessage;
}

function setSuccess(element) {
    const parent = element.parentElement;
    if(parent.classList.contains('error')) {
        parent.classList.remove('error')
    }
    parent.classList.add('success')
}

function isEmailValid(email){
    const reg =/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    return reg.test(email);
}