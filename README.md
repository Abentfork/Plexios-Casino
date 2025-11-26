# 🎰 Plexios Casino: Demo de Casino Online

[![Estado del Proyecto](https://img.shields.io/badge/Estado-En%20Desarrollo-orange?style=for-the-badge)](https://github.com/Abentfork/proyecto-final)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Uso de Stripe](https://img.shields.io/badge/Pagos-Stripe%20(Test%20Mode)-informational?style=for-the-badge&logo=stripe&logoColor=white)](https://stripe.com)

## 💡 Resumen del Proyecto

Plexios Casino es una **demostración educativa** de un casino en línea diseñada para showcasing de arquitectura web completa. Este proyecto *no* utiliza dinero real; simula pagos y transacciones con **Stripe en modo de prueba**.

Incluye tres juegos principales, integrados mediante tecnología **Godot Web**:

| 🃏 Juegos Disponibles |
| :---: |
| **Slot** 🎰 |
| **Roulette** 🎡 |
| **Blackjack** ♠️ |

---

## 🚀 Pila Tecnológica / Stack

Una arquitectura **Full-Stack** robusta que combina rendimiento y modernidad.

### ⚙️ Backend & API

| Componente | Descripción | Detalles |
| :--- | :--- | :--- |
| **Lenguaje** | Python 3.11+ | [![Python](https://img.shields.io/badge/Python-3.11+-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) |
| **Framework** | FastAPI | [![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/) |
| **Base de Datos** | SQLite / PostgreSQL | [![Database](https://img.shields.io/badge/DB-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) |
| **Servidor ASGI** | Uvicorn / Gunicorn | Alto rendimiento para producción. |
| **Pagos** | Stripe API | Solo **modo de prueba** (`test mode`). |

> **Dependencias Clave:** `fastapi`, `uvicorn`, `sqlalchemy` / `tortoise-orm`, `python-dotenv`, `stripe`.

### 💻 Frontend & UI

| Componente | Descripción | Detalles |
| :--- | :--- | :--- |
| **Librería** | React | [![React](https://img.shields.io/badge/React-UI-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://react.dev/) |
| **Estilos** | TailwindCSS | [![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Styles-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/) |
| **Juegos** | Godot Engine 4 | [![Godot](https://img.shields.io/badge/Godot-Games-478CBF?style=for-the-badge&logo=godot-engine&logoColor=white)](https://godotengine.org/) |

### 🌐 Hosting / Despliegue

| Componente | Detalles |
| :--- | :--- |
| **Proveedor** | Oracle Cloud |
| **Reverse Proxy** | Nginx |
| **Seguridad (HTTPS)** | Let’s Encrypt |

---

## 💾 Diseño de Base de Datos

Utilizamos **SQLite** para desarrollo local y **PostgreSQL** para el entorno de servidor. El diseño se centra en la auditoría y la gestión de la economía virtual del casino.

### Entidad: `Users` (Usuarios) 👤

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | ID de usuario único |
| `username` | VARCHAR(50) | Nombre de usuario (Único) |
| `email` | VARCHAR(100) | Email (Único) |
| `password_hash` | VARCHAR(255) | Contraseña hasheada |
| `credits` | NUMERIC(10,2) | **Saldo virtual actual** |
| `created_at` | TIMESTAMP | Fecha de registro |
| `last_login` | TIMESTAMP | Último inicio de sesión |

### Entidad: `Games` (Juegos) 🕹️

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | ID de juego único |
| `name` | VARCHAR(50) | Nombre del juego |
| `type` | VARCHAR(20) | `slot` / `roulette` / `blackjack` |
| `created_at` | TIMESTAMP | Fecha de creación del registro del juego |

### Entidad: `Bets` (Apuestas) 💰

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | ID de apuesta única |
| `user_id` | INT / **FK** | Referencia al ID del usuario |
| `game_id` | INT / **FK** | Referencia al ID del juego |
| `bet_amount` | NUMERIC(10,2) | Cantidad apostada |
| `win_amount` | NUMERIC(10,2) | Cantidad ganada (0 si se pierde) |
| `outcome` | VARCHAR(20) | Resultado: `win` / `loss` / `draw` |
| `created_at` | TIMESTAMP | Marca de tiempo de la apuesta |

### Entidad: `Payments` (Pagos) 💳

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | SERIAL / **PK** | ID de pago único |
| `user_id` | INT / **FK** | Referencia al ID del usuario |
| `amount` | NUMERIC(10,2) | Créditos añadidos |
| `stripe_payment_id` | VARCHAR(100) | ID de pago de Stripe (Test Mode) |
| `status` | VARCHAR(20) | Estado: `succeeded` / `failed` |
| `created_at` | TIMESTAMP | Marca de tiempo del pago |

> 📌 **Nota:** Se puede añadir una tabla de registro de transacciones (*Transactions log*) para registrar **cualquier cambio en los créditos**, simulando una pista de auditoría profesional.

---

## ✨ Características Principales

* ✅ **Sistema Completo:** Registro de usuarios y gestión de inicio de sesión (`login`).
* 💰 **Economía Virtual:** Sistema de créditos virtuales.
* 🎮 **Juegos Integrados:** Juega a **Slot**, **Roulette** y **Blackjack**.
* 💳 **Simulación de Pagos:** Integración con **Stripe en modo de prueba** para recarga de créditos.
* 📊 **Registro Detallado:** Trazabilidad individual de cada apuesta y resultado.
* 🔧 **Diseño Escalable:** Fácilmente expandible para añadir nuevos juegos en el futuro.

---

## 🛠️ Configuración / Instalación

1. Clona el repositorio:

```bash
git clone [https://github.com/Abentfork/proyecto-final.git](https://github.com/Abentfork/proyecto-final.git)
cd proyecto-final
