const nav = document.getElementById("nav");
const occupation = document.getElementById("occupation");
const menu_chk = document.getElementById("chk");

const skill_canv = document.getElementById("skill-chart");

let fname = document.getElementById("fname");
let lname = document.getElementById("lname");
const send_email_btn = document.getElementById("send-email-btn");

const data = {
    labels: ["Django", "HTML", "CSS", "Javascript"],
    datasets: [{
        data: [50, 20, 20, 10],
        backgroundColor: ["rgb(66,0177,135)", "rgb(233,98,40)", "rgb(40,164,216)", "rgb(247,195,39)"],
        color: "#fff",
    }]
}

if (skill_canv) {
    const skill_chart = new Chart(
        skill_canv.getContext("2d"), {
            type: "doughnut",
            data: data,
            options: {
                plugins: {
                    datalabels: {
                        color: "#fff"
                    }
                }
            }
        }
    );
}

console.log("success")

if (nav) {
    window.addEventListener("scroll", function() {
        if (document.body.scrollTop >= 10 || document.documentElement.scrollTop >= 200) {
            nav.style.backgroundColor = "rgb(170, 26, 0)";
        } else {
            nav.style.backgroundColor = "transparent";
        }
    });
}


if (send_email_btn) {
    send_email_btn.addEventListener("click", function() {
        if (fname && lname) {
            console.log(fname);
            console.loog(lname);
            alert("Thanks " + fname + " " + lname + ", I will contact you shortly");
        }
    });
}