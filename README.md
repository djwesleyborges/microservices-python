# Microservices with Python and React

[English](#english) | [Português](#português)

## English

This project is a microservices-based application that demonstrates the implementation of an inventory management system with order processing capabilities. It consists of three main components:

### 1. Inventory Service
A Python-based microservice built with FastAPI that manages product inventory. Features include:
- Product management (CRUD operations)
- Redis database integration for data persistence
- RESTful API endpoints for product operations
- CORS support for frontend integration

**Tech Stack:**
- FastAPI (Python web framework)
- Redis OM (Redis Object Mapping)
- Python 3.x

### 2. Payment Service
A Python-based microservice that handles order processing and payment operations. Features include:
- Order processing
- Payment status management
- Background task processing
- Integration with the inventory service
- Redis database for order storage

**Tech Stack:**
- FastAPI (Python web framework)
- Redis OM (Redis Object Mapping)
- Python 3.x
- Background Tasks for async processing

### 3. Inventory Frontend
A React-based web application that provides a user interface for the system. Features include:
- Product listing and management
- Order creation and tracking
- Responsive design
- Integration with both backend services

**Tech Stack:**
- React.js
- React Router for navigation
- Modern JavaScript (ES6+)
- REST API integration

## Setup and Installation

1. Clone the repository
2. Set up each service:

### Inventory Service:
```bash
cd inventory
cp env_sample .env  # Configure your environment variables
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Payment Service:
```bash
cd payment
cp env_sample .env  # Configure your environment variables
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

### Frontend:
```bash
cd inventory-frontend
npm install
npm start
```

---

## Português

Este projeto é uma aplicação baseada em microsserviços que demonstra a implementação de um sistema de gerenciamento de inventário com capacidades de processamento de pedidos. Consiste em três componentes principais:

### 1. Serviço de Inventário
Um microsserviço baseado em Python construído com FastAPI que gerencia o inventário de produtos. Recursos incluem:
- Gerenciamento de produtos (operações CRUD)
- Integração com banco de dados Redis para persistência de dados
- Endpoints API RESTful para operações de produtos
- Suporte a CORS para integração com frontend

**Stack Tecnológica:**
- FastAPI (Framework web Python)
- Redis OM (Mapeamento de Objetos Redis)
- Python 3.x

### 2. Serviço de Pagamento
Um microsserviço baseado em Python que gerencia o processamento de pedidos e operações de pagamento. Recursos incluem:
- Processamento de pedidos
- Gerenciamento de status de pagamento
- Processamento de tarefas em segundo plano
- Integração com o serviço de inventário
- Redis para armazenamento de pedidos

**Stack Tecnológica:**
- FastAPI (Framework web Python)
- Redis OM (Mapeamento de Objetos Redis)
- Python 3.x
- Tarefas em segundo plano para processamento assíncrono

### 3. Frontend do Inventário
Uma aplicação web baseada em React que fornece uma interface de usuário para o sistema. Recursos incluem:
- Listagem e gerenciamento de produtos
- Criação e acompanhamento de pedidos
- Design responsivo
- Integração com ambos os serviços backend

**Stack Tecnológica:**
- React.js
- React Router para navegação
- JavaScript moderno (ES6+)
- Integração com API REST

## Configuração e Instalação

1. Clone o repositório
2. Configure cada serviço:

### Serviço de Inventário:
```bash
cd inventory
cp env_sample .env  # Configure suas variáveis de ambiente
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Serviço de Pagamento:
```bash
cd payment
cp env_sample .env  # Configure suas variáveis de ambiente
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

### Frontend:
```bash
cd inventory-frontend
npm install
npm start
```