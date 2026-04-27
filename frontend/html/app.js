const tableBody = document.getElementById('team-table-body');
const statusLabel = document.getElementById('status-label');

async function getTeamData() {
    try {
        // Llamada al puerto 5000 del backend 
        const response = await fetch('http://localhost:5000/api/team');
        
        if (response.ok) {
            const data = await response.json();
            renderTable(data);
            statusLabel.innerText = "Conectado";
            statusLabel.style.color = "green";
        } else {
            throw new Error("Error en la respuesta del backend");
        }
    } catch (error) {
        console.error("Error al pedir datos:", error);
        statusLabel.innerText = "Desconectado";
        statusLabel.style.color = "red";
    }
}

function renderTable(members) {
    tableBody.innerHTML = ''; // Limpiar tabla
    members.forEach(member => {
        const row = `<tr>
            <td>${member.nombre} ${member.apellido}</td>
            <td>${member.legajo}</td>
            <td>${member.feature}</td>
            <td>${member.servicio}</td>
            <td>${member.estado}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });
}

// Ejecutar al cargar la página
getTeamData();