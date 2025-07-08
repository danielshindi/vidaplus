# 🩺 Sistema de Gestão Hospitalar e de Serviços de Saúde (SGHSS) - VidaPlus

Este projeto é uma API desenvolvida com **Python**, **Django** e **Django REST Framework** para gerenciar pacientes, profissionais da saúde, agendamentos de consultas e prontuários médicos.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Django**
- **Django REST Framework**
- **MySQL**
- **JWT Authentication**

---


## ⚙️ Instalação do Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

## 2.Crie e ative o ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## 4. Configure o banco de dados

Crie um banco de dados MySQL e edite o arquivo settings.py com suas credenciais:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 5. Aplique as migrações

```bash
python manage.py migrate
```

## 6. Inicie o servidor
```bash
python manage.py runserver
```


