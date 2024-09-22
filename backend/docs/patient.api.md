# API пациента
## POST запросы
```mermaid
flowchart TD
POST   --> logout
CREATE --> patient-carts
CREATE --> patient-phones
CREATE --> patient-signatures
CREATE --> patient-invoices
POST   --> patient-invoices/purchase
```
## GET запросы
```mermaid
flowchart TD
OBJECT --> patient
LIST   --> patient-carts
OBJECT --> patient-carts/:id
LIST   --> patient-phones
LIST   --> patient-signatures
LIST   --> patient-agreements
OBJECT --> patient-agreements/:id
LIST   --> patient-talons
OBJECT --> patient-talons/:id
LIST   --> patient-transactions
OBJECT --> patient-transactions/:id
OBJECT --> patient-transactions/stats
LIST   --> patient-invoices
OBJECT --> patient-invoices/:id
OBJECT --> patient-balance
```
## PUT/PATCH запросы
```mermaid
flowchart TD
OBJECT --> patient
OBJECT --> patient-carts/:id   
OBJECT --> patient-phones/:id
OBJECT --> patient-signatures/:id
```
## DELETE запросы
```mermaid
flowchart TD
DELETE --> patient
DELETE --> patient-carts/:id
DELETE --> patient-phones/:id
DELETE --> patient-signatures/:id
DELETE --> patient-invoices/:id
```