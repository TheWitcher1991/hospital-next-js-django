# API общедоступное
## POST запросы
```mermaid
---
title: Только для гостя
---
flowchart TD
    POST --> login
    POST --> signup/patient
    POST --> signup/employee
    POST --> yookassa-webhook
```
## GET запросы
```mermaid
flowchart TD
    LIST   -- cached --> service-types
    LIST   -- cached --> services
    LIST   -- cached --> patient-types
    LIST   --> employees
    OBJECT --> employees/:id
    LIST   -- cached --> cabinets
    LIST   -- cached --> positions
    LIST   --> work_schedules
```
