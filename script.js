
async function upload() {
    let file = document.getElementById("audio").files[0];
    let formData = new FormData();
    formData.append("file", file);

    let res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
    });

    let data = await res.json();
    document.getElementById("output").innerText = data.transcript;
}

async function ask() {
    let q = document.getElementById("question").value;

    let res = await fetch(`http://127.0.0.1:8000/ask?question=${q}`, {
        method: "POST"
    });

    let data = await res.json();
    document.getElementById("output").innerText = data.answer;
}
