// ✅ LOAD TITLES & DIRECTORS FROM GET API AND FILL DATALISTS
fetch("http://127.0.0.1:5000/get_details")
    .then(response => response.json())
    .then(data => {

        let titlesList = document.getElementById("titles-list");
        let directorsList = document.getElementById("directors-list");

        // Fill titles datalist
        data.titles.forEach(title => {
            let option = document.createElement("option");
            option.value = title;
            titlesList.appendChild(option);
        });

        // Fill directors datalist
        data.directors.forEach(director => {
            let option = document.createElement("option");
            option.value = director;
            directorsList.appendChild(option);
        });
    });


// ✅ SEND DATA TO POST API & GET PREDICTION
function predict() {

    let payload = {
        "Title": document.getElementById("title").value,
        "Director": document.getElementById("director").value,
        "Runtime_Minutes": Number(document.getElementById("runtime").value),
        "Rating": Number(document.getElementById("rating").value),
        "Revenue_Millions": Number(document.getElementById("revenue").value),
        "Action": document.getElementById("action").checked ? 1 : 0,
        "Adventure": document.getElementById("adventure").checked ? 1 : 0,
        "Comedy": document.getElementById("comedy").checked ? 1 : 0,
        "Family": document.getElementById("family").checked ? 1 : 0,
        "Horror": document.getElementById("horror").checked ? 1 : 0,
        "Sport": document.getElementById("sport").checked ? 1 : 0
    };

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "🎯 Prediction Result: " + data.prediction;
    });
}
