# delivery-ci

**ФИО:** Иванов Иван Иванович
**Группа:** XX-00

Учебный проект: функция `calculate_delivery(subtotal, express=False)` для расчёта
стоимости доставки заказа, автотесты на PyTest и их автоматический запуск в GitHub Actions.

## Установка зависимостей (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

## Запуск тестов локально

```powershell
python -m pytest -q
```
