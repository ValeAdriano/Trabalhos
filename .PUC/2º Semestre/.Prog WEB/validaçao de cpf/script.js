function verifyCPF(cpf) {
    const rgx = /^\d{3}\.\d{3}\.\d{3}\-\d{2}$/
    return rgx.test(cpf)
}

function submitForm() {
    let name = document.getElementById("name").value
    let cpf = formatCPF(document.getElementById("cpf").value)

    console.log(cpf)

    if(name.trim() == "" || cpf == "") {
        alert("Digite um nome/cpf válido.")
        return
    }

    if(verifyCPF(cpf)) {
        alert("O CPF de " + name + " é válido")
    }
    else {
        alert("O CPF de " + name + " é inválido")
    }
}

function formatCEP(tel) {
    return tel.trim().replace(/(\d{5})(\d{3})/, "$1-$2")
}

function masktel(input){
    let tel = input.value
    
    if(isNaN(tel[tel.length - 1])){ // impede entrar outro caractere que não seja número
       input.value = tel.substring(0,tel.length-1)
       return
    }
    
    input.setAttribute("maxlength", "9")
    if (tel.length == 5) input.value += "-"
 }

 function maskName(input) {
    let name = input.value

    const allowedCaracters = /^[a-z]/
    if(!allowedCaracters.test(name[name.length - 1])) {
        input.value = name.substring(0, name.length - 1)
        return;
    }
 }

 function formatcep(tel) {
    return tel.trim().replace(/(\d{5})(\d{3})/, "$1-$2")
}

function formattel(tel) {
    return tel.trim().replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3")
}

function masktel(input){
    let tel = input.value
    
    if(isNaN(tel[tel.length - 1])){ // impede entrar outro caractere que não seja número
       input.value = tel.substring(0, tel.length-1)
       return
    }
    
    input.setAttribute("maxlength", "14")
    if (tel.length == 1) input.value = "("+tel
    if (tel.length == 3) input.value += ")"
    if (tel.length == 9) input.value += "-"
 }

 function maskName(input) {
    let name = input.value

    const allowedCaracters = /^[a-z]/
    if(!allowedCaracters.test(name[name.length - 1])) {
        input.value = name.substring(0, name.length - 1)
        return;
    }
 }

 function formattel(tel) {
    return tel.trim().replace(/(\d{2})(\d{5})(\d{4})/, "($1)$2-$3")
}