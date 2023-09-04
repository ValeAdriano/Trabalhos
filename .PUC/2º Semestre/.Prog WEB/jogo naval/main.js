const ships = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
    [0, 1, 0, 0, 0, 1, 0, 5, 31, 32, 33, 0,],
    [0, 1, 0, 0, 0, 21, 22, 0, 0, 0, 0, 0,],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
    [0, 1, 0, 0, 0, 1, 0, 21, 22, 0, 0, 0,],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 4, 5,]
];
let ammoCount = [0, 2, 1]
const jogo = document.getElementById("jogo")
const startGameBtn = document.getElementById("startGameBtn")
const selectAmmo = document.getElementById("selectAmmo")
jogo.style.display = "none"
selectAmmo.style.display = "none"
let life = 0;
let points = 0;
let endGame;
function resetGame() {

    life = 5;
    points = 0;
    endGame = false;
    shuffle();
}
 
function shuffle() {

    for (var i = 0; i < 1000; i++) {
        i1 = Math.floor(Math.random() * 8);
        j1 = Math.floor(Math.random() * 12);
        i2 = Math.floor(Math.random() * 8);
        j2 = Math.floor(Math.random() * 12);
        let temp = ships[i1][j1];
        ships[i1][j1] = ships[i2][j2];
        ships[i2][j2] = temp;
    }
}

function shipOnClick(indX, indY) {
    if (endGame) return;
    const ammoType = Number(selectAmmo.value);

    switch (ammoType) {
        case 0:
            ammoImpact(indX, indY, ammoType)
            break;
        case 1:
            if (ammoCount[ammoType] > 0) {
                ammoCount[ammoType]--;
                ammoImpact(indX, indY, ammoType)
                
            }
            break;
        case 2:
            if (ammoCount[ammoType] > 0) {
                ammoCount[ammoType]--;
                ammoImpact(indX, indY, ammoType)
                
            }
            break;
    }
}



function update_scoreboard(type) {
    points += type
    if (type == 0) {
        life--;
        update_scoreboard_view();
        if (life == 0) {
            alert('Você perdeu!');
            endGame = true;
            verificarVidas(false)
            selectAmmo.style.display = "none"
            startGameBtn.style.display = "inline"
            startGameBtn.innerText = "Reiniciar Jogo"
        }
    }
    else {
        update_scoreboard_view();
    }
}

function update_scoreboard_view() {
    const scoreboard = document.getElementById("divScoreboard");
    scoreboard.innerHTML = "Pontos: " + points + " - Vidas: " + life;
    document.getElementById("ammo1").innerText = `Bomba (${ammoCount[1]})`
    document.getElementById("ammo2").innerText = `Bomba Atômica (${ammoCount[2]})`
}

function startGame() {
    var vidas = document.getElementsByName("vidas");
    verificarVidas(true)
    startGameBtn.style.display = "none"
    jogo.style.display = "inline"
    selectAmmo.style.display = "inline"
    points = 0;
    endGame = false;
    ammoCount = [0, 2, 1]
    var tabela = document.getElementById("tabela")
    tabela.innerHTML = ``
    update_scoreboard_view()
    for (let x = 0; x < 8; x++) {
        var row = document.createElement("tr")
        for (let y = 0; y < 12; y++) {
            var cell = document.createElement("td")
            var cellimg = document.createElement("img")
            cellimg.id = `ship${x}${y}`
            cellimg.src = "images/fundo.jpg"
            cellimg.onclick = function () {
                shipOnClick(x, y)
            }
            cell.appendChild(cellimg)
            row.appendChild(cell)
        }
        tabela.appendChild(row)
    }
}

function verificarVidas(selecionar) {
    const vidas = document.getElementsByName("vidas");
    if (selecionar) {
        for (var i = 0; i < vidas.length; i++) {
            if (vidas[i].checked) {
                life = vidas[i].value;
            }
            vidas[i].disabled = true;
        }
    } else {
        for (var i = 0; i < vidas.length; i++) {
            vidas[i].disabled = false;
        }
    }
}

function ammoImpact(corX, corY, ammoType) {
    let totalType = 0;
    totalType += attackCell(corX, corY)
    if (ammoType == 1 || ammoType == 2) {
        totalType += attackCell(corX - 1, corY)
        totalType += attackCell(corX + 1, corY)
        totalType += attackCell(corX, corY - 1)
        totalType += attackCell(corX, corY + 1)
        if (ammoType == 2) {
            totalType += attackCell(corX - 1, corY - 1)
            totalType += attackCell(corX + 1, corY - 1)
            totalType += attackCell(corX - 1, corY + 1)
            totalType += attackCell(corX + 1, corY + 1)
        }
    }

    update_scoreboard(totalType);
}

function attackCell(corX, corY) {
    try {
        const ship = document.getElementById(`ship${corX}${corY}`);
        let type = ships[corX][corY];
        ship.src = getImage(type);
        let textType = type + ""
        type = Number(textType.charAt(0));
        switch (type) {
            case 4:
                ammoCount[1]++
                return 0
            case 5:
                ammoCount[2]++
                return 0

            default:
                return type
        }
    } catch (error) {

    }
}

function getImage(type) {
    switch (type) {
        case 0:
            return "images/agua.jpg";
            break;
        case 1:
            return "images/navio.jpg";
            break;
        case 21:
            return "images/subbunda.jpg";
            break;
        case 22:
            return "images/subnariz.jpg";
            break;
        case 31:
            return "images/naviobunda.jpg";
            break;
        case 32:
            return "images/naviomeiuca.jpg";
            break;
        case 33:
            return "images/navionariz.jpg";
            break;
        case 4:
            return "images/bomba.jpg";
            break;
        case 5:
            return "images/nuclear.jpg";
            break;
    }

    return "images/back.jpg";
}