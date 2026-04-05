const API = "http://127.0.0.1:5000";

// -------- ROUTES --------
async function addRoute() {
    const route_no = document.getElementById("route_no").value;
    const driver_name = document.getElementById("driver_name").value;
    const phone = document.getElementById("phone").value;

    console.log("Sending:", route_no, driver_name, phone); // DEBUG

    const res = await fetch(API + "/add_route", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({route_no, driver_name, phone})
    });

    const data = await res.json();
    console.log(data);

    alert("Route added ✅");
}

// -------- LOAD ROUTES --------
async function loadRoutes(dropdownId) {
    const res = await fetch(API + "/get_routes");
    const data = await res.json();

    const dropdown = document.getElementById(dropdownId);
    dropdown.innerHTML = "";

    data.forEach(r => {
        const opt = document.createElement("option");
        opt.value = r.route_no;
        opt.text = r.route_no;
        dropdown.appendChild(opt);
    });
}

// -------- STOPS --------
let stopCount = 0;

function addStopBox() {
    stopCount++;

    const div = document.createElement("div");
    div.className = "stop-box";

    div.innerHTML = `
        <h4>Stop ${stopCount}</h4>
        <input placeholder="Stop Name" id="name_${stopCount}">
        <input placeholder="Latitude" id="lat_${stopCount}">
        <input placeholder="Longitude" id="lon_${stopCount}">
    `;

    document.getElementById("stops").appendChild(div);
}

async function saveStops() {
    const route_no = document.getElementById("route_select").value;

    for (let i = 1; i <= stopCount; i++) {
        const stop_name = document.getElementById(`name_${i}`).value;
        const latitude = parseFloat(document.getElementById(`lat_${i}`).value);
        const longitude = parseFloat(document.getElementById(`lon_${i}`).value);

        await fetch(API + "/add_stop", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                route_no,
                stop_number: i,
                stop_name,
                latitude,
                longitude
            })
        });
    }

    alert("Stops saved");
}

// -------- DRIVER GPS --------
function startTracking() {
    const route_no = document.getElementById("driver_route").value;

    if (!navigator.geolocation) {
        alert("Geolocation not supported ❌");
        return;
    }

    navigator.geolocation.watchPosition(
        async pos => {
            const latitude = pos.coords.latitude;
            const longitude = pos.coords.longitude;

            console.log("Location:", latitude, longitude);

            await fetch(API + "/update_location", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({route_no, latitude, longitude})
            });
        },
        err => {
            console.error(err);
            alert("Location permission denied 🚫");
        }
    );
}

// -------- STUDENT TRACK --------
async function trackBus() {
    const route_no = document.getElementById("student_route").value;

    const res = await fetch(API + "/track/" + route_no);
    const data = await res.json();

    const container = document.getElementById("result");
    container.innerHTML = "";

    // 🔥 HANDLE ERROR FIRST
    if (data.error) {
        container.innerHTML = "No driver location yet 🚫";
        return;
    }

    data.forEach((s, index) => {
        const div = document.createElement("div");
        div.innerHTML = `
            0 -> ${s.stop} [${index+1}] ${s.status}
            <br>|
            <br>|
        `;
        container.appendChild(div);
    });
}