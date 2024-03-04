let rbcbtn = document.getElementById('rbc')
let wbcbtn = document.getElementById('wbc')
let rbcCount = document.getElementById('rbcCount');
let wbcCount = document.getElementById('wbcCount');
let wbcContent = document.getElementById('wbcContent');
let rbcContent = document.getElementById('rbcContent');

rbcbtn.onclick = ()=>{
    wbcbtn.classList.remove('active');
    rbcbtn.classList.add('active');
    rbcCount.classList.remove('notActiveCell');
    wbcCount.classList.add('notActiveCell');
    rbcContent.classList.remove('notActiveCell');
    wbcContent.classList.add('notActiveCell');
}

wbcbtn.onclick = ()=>{
    rbcbtn.classList.remove('active');
    wbcbtn.classList.add('active');
    wbcCount.classList.remove('notActiveCell');
    rbcCount.classList.add('notActiveCell');
    wbcContent.classList.remove('notActiveCell');
    rbcContent.classList.add('notActiveCell');
}