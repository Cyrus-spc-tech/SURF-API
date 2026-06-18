// API Base URL
const API_BASE = '';

// Navigation
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        
        // Update active link
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        
        // Show target section
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });
        document.getElementById(targetId).classList.add('active');
        
        // Load data if needed
        if (targetId === 'dashboard') {
            loadDashboard();
        } else if (targetId === 'patients') {
            loadPatients();
        }
    });
});

// Load Dashboard Statistics
async function loadDashboard() {
    try {
        const response = await fetch(`${API_BASE}/view`);
        const data = await response.json();
        
        const patients = Object.values(data);
        const totalPatients = patients.length;
        
        let totalBMI = 0;
        let normalCount = 0;
        let overweightCount = 0;
        
        patients.forEach(patient => {
            totalBMI += patient.bmi || 0;
            if (patient.verdict === 'Normal') normalCount++;
            if (patient.verdict === 'OverWeight') overweightCount++;
        });
        
        const avgBMI = totalPatients > 0 ? (totalBMI / totalPatients).toFixed(2) : 0;
        
        document.getElementById('total-patients').textContent = totalPatients;
        document.getElementById('avg-bmi').textContent = avgBMI;
        document.getElementById('normal-count').textContent = normalCount;
        document.getElementById('overweight-count').textContent = overweightCount;
    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}

// Load Patients Table
async function loadPatients() {
    try {
        const sortBy = document.getElementById('sort-select').value;
        const order = document.getElementById('order-select').value;
        const searchTerm = document.getElementById('search-input').value.toLowerCase();
        
        let url = `${API_BASE}/view`;
        
        if (sortBy && order) {
            url = `${API_BASE}/sort?sort_by=${sortBy}&order=${order}`;
        }
        
        const response = await fetch(url);
        const data = await response.json();
        
        let patients = Object.values(data);
        
        // Filter by search term
        if (searchTerm) {
            patients = patients.filter(patient => 
                patient.name.toLowerCase().includes(searchTerm) ||
                patient.id.toLowerCase().includes(searchTerm) ||
                patient.address.city.toLowerCase().includes(searchTerm)
            );
        }
        
        renderPatientTable(patients);
    } catch (error) {
        console.error('Error loading patients:', error);
        document.getElementById('patient-table-body').innerHTML = 
            '<tr><td colspan="9" class="loading">Error loading patients</td></tr>';
    }
}

// Render Patient Table
function renderPatientTable(patients) {
    const tbody = document.getElementById('patient-table-body');
    
    if (patients.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="9" class="empty-state">
                    <div class="empty-state-icon">📋</div>
                    <p>No patients found</p>
                </td>
            </tr>
        `;
        return;
    }
    
    tbody.innerHTML = patients.map(patient => {
        const statusClass = getStatusClass(patient.verdict);
        return `
            <tr>
                <td><strong>${patient.id || 'N/A'}</strong></td>
                <td>${patient.name || 'N/A'}</td>
                <td>${patient.age || 'N/A'}</td>
                <td>${patient.gender || 'N/A'}</td>
                <td>${patient.height || 'N/A'}</td>
                <td>${patient.weight || 'N/A'}</td>
                <td><strong>${patient.bmi || 'N/A'}</strong></td>
                <td><span class="status-badge ${statusClass}">${patient.verdict || 'N/A'}</span></td>
                <td>
                    <button onclick="editPatient('${patient.id}')" class="btn btn-edit">Edit</button>
                    <button onclick="deletePatient('${patient.id}')" class="btn btn-danger">Delete</button>
                </td>
            </tr>
        `;
    }).join('');
}

// Get Status Class
function getStatusClass(verdict) {
    switch (verdict) {
        case 'Normal':
            return 'status-normal';
        case 'OverWeight':
            return 'status-overweight';
        case 'UnderWeight':
            return 'status-underweight';
        default:
            return '';
    }
}

// Add Patient Form Submit
document.getElementById('patient-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const patientId = document.getElementById('patient-id').value || generatePatientId();
    
    const patientData = {
        id: patientId,
        name: document.getElementById('name').value,
        age: parseInt(document.getElementById('age').value),
        gender: document.getElementById('gender').value,
        height: parseFloat(document.getElementById('height').value),
        weight: parseFloat(document.getElementById('weight').value),
        address: {
            city: document.getElementById('city').value,
            state: document.getElementById('state').value,
            pin: document.getElementById('pin').value
        }
    };
    
    try {
        const response = await fetch(`${API_BASE}/create`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(patientData)
        });
        
        if (response.ok) {
            alert('Patient created successfully!');
            resetForm();
            loadDashboard();
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        console.error('Error creating patient:', error);
        alert('Error creating patient');
    }
});

// Generate Patient ID
function generatePatientId() {
    const timestamp = Date.now().toString(36).toUpperCase();
    return `P${timestamp}`;
}

// Reset Form
function resetForm() {
    document.getElementById('patient-form').reset();
    document.getElementById('patient-id').value = '';
}

// Edit Patient
async function editPatient(patientId) {
    try {
        const response = await fetch(`${API_BASE}/patient/${patientId}`);
        const patient = await response.json();
        
        // Populate edit form
        document.getElementById('edit-patient-id').value = patientId;
        document.getElementById('edit-name').value = patient.name;
        document.getElementById('edit-age').value = patient.age;
        document.getElementById('edit-gender').value = patient.gender;
        document.getElementById('edit-height').value = patient.height;
        document.getElementById('edit-weight').value = patient.weight;
        document.getElementById('edit-city').value = patient.address.city;
        document.getElementById('edit-state').value = patient.address.state;
        document.getElementById('edit-pin').value = patient.address.pin;
        
        // Show modal
        document.getElementById('edit-modal').style.display = 'block';
    } catch (error) {
        console.error('Error loading patient:', error);
        alert('Error loading patient data');
    }
}

// Edit Form Submit
document.getElementById('edit-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const patientId = document.getElementById('edit-patient-id').value;
    
    const patientData = {
        name: document.getElementById('edit-name').value,
        age: parseInt(document.getElementById('edit-age').value),
        gender: document.getElementById('edit-gender').value,
        height: parseFloat(document.getElementById('edit-height').value),
        weight: parseFloat(document.getElementById('edit-weight').value),
        address: {
            city: document.getElementById('edit-city').value,
            state: document.getElementById('edit-state').value,
            pin: document.getElementById('edit-pin').value
        }
    };
    
    try {
        const response = await fetch(`${API_BASE}/update/${patientId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(patientData)
        });
        
        if (response.ok) {
            alert('Patient updated successfully!');
            closeModal();
            loadPatients();
            loadDashboard();
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        console.error('Error updating patient:', error);
        alert('Error updating patient');
    }
});

// Close Modal
function closeModal() {
    document.getElementById('edit-modal').style.display = 'none';
}

// Delete Patient
async function deletePatient(patientId) {
    if (!confirm(`Are you sure you want to delete patient ${patientId}?`)) {
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/delete/${patientId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            alert('Patient deleted successfully!');
            loadPatients();
            loadDashboard();
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }
    } catch (error) {
        console.error('Error deleting patient:', error);
        alert('Error deleting patient');
    }
}

// Search and Sort Event Listeners
document.getElementById('search-input').addEventListener('input', loadPatients);
document.getElementById('sort-select').addEventListener('change', loadPatients);
document.getElementById('order-select').addEventListener('change', loadPatients);

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('edit-modal');
    if (event.target === modal) {
        closeModal();
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadDashboard();
});
