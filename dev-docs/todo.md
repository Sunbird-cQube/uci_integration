# Authentication of UCI and user Workflow:

[[toc]]

## Tech Stack

- Django
- vitepress
- sqlite3

## TODO:

- Phase 1:

  - [x] Setup Django and make basic authentication
  - [x] Make schema
  - [x] Complete subscription model
  - [ ] Add google OAuth2 `(TBD)`
  - [x] Test workflow
  - [x] Create admin user-types
  - [x] Test user and admin flow
  - [ ] Write unit tests
  - [ ] Write integration test
  - [x] Document Dev Docs
  - [x] Final testing + UI improvements
  - [x] End user documentation

- Phase 2:
  - [ ] Integrate with cQube, UCI (TBD)

## Demo dB schema

::: details Replace with actual dB schema

**user: default with changes:**

- subscription
- org // might be removed
- type {choices=[('admin', 'Admin'), ('user', 'User')], default='user')}
- position // might be removed
- preferences

**subscription:**

- name of subscription
- name of org of subscription

**Alert:**

- subscription
- message
- date // of creation. change it to created_at
- users // many. send alert to them

:::

## Included here:

- FlowChart: application modules/ different sections
- AuthFlow: flow of authentication of user
- Demo dB schema: demo dB schema to use for initial development
- Admin workflow: Workflow of how admin panel will work

## FlowChart

![FlowChart](/assets/flowchart.png)

## AuthFlow

![User Auth Workflow](/assets/WorkFlow.png)

## Admin workflow

![Admin workflow](/assets/adminworkflow.png)
