-- Creación de la tabla de integrantes
CREATE TABLE IF NOT EXISTS members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    legajo VARCHAR(20) NOT NULL,
    feature VARCHAR(50) NOT NULL,
    servicio VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL
);

-- Inserción de los datos del Grupo 
INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado) VALUES
('Pedro', 'Moyano Amaya', '31411', 'Feature 01', 'Infraestructura', 'Operativo'),
('Milagros Ailen', 'Reale Bortone', '32856', 'Feature 02', 'Frontend', 'Operativo'),
('Franco', 'Jimenez', '31848', 'Feature 03', 'Backend API', 'Operativo'),
('Franco Javier', 'Portillo Colinas', '31089', 'Feature 04', 'Base de Datos', 'Operativo'),
('Bautista', 'Calvo', '32156', 'Feature 05', 'Portainer', 'Operativo');