## This is a test task for Develops-Today Company for position Python Junior Developer
## Task Decription
### Overview
This task involves building a CRUD application. The goal is to create a system that showcases your understanding in building RESTful APIs, interacting with SQL-like databases, and integrating third-party services. The test assessment is expected to be done within 2 hours.

### Requirements
Spy Cat Agency (SCA) asked you to create a management application, so that it simplifies their spying work processes. SCA needs a system to manage their cats, missions they undertake, and targets they are assigned to.

From cats perspective, a mission consists of spying on targets and collecting data. One cat can only have one mission at a time, and a mission assumes a range of targets (minimum: 1, maximum: 3). While spying, cats should be able to share the collected data into the system by writing notes on a specific target. Cats will be updating their notes from time to time and eventually mark the target as complete. If the target is complete, notes should be frozen, i.e. cats should not be able to update them in any way. After completing all of the targets, the mission is marked as completed.

From the agency perspective, they regularly hire new spy cats and so should be able to add them to and visualize in the system. SCA should be able to create new missions and later assign them to cats that are available. Targets are created in place along with a mission, meaning that there will be no page to see/create all/individual targets.

## Project Setup

Python version: 3.13.0

1. Create virtual environment with `python -m venv venv` command
2. Run command `pip install -r requirements.txt`
3. Run command `python manage.py migrate` to apply current database migrations
4. Run command `python manage.py runserver` to start development server

At this point everything should be working and you will have acces to the API.

## Localhost Endpoints

Postman Collection: https://api.postman.com/collections/15145004-82778dde-b849-416d-8188-208dedbbb928?access_key=PMAT-01JBHP9S6EJETGS0VVPANP2K0V

### Cats
- GET: http://127.0.0.1:8000/api/spy_cats/
- GET: http://127.0.0.1:8000/api/spy_cats/1/
- PATCH: http://127.0.0.1:8000/api/spy_cats/2/
- POST: http://127.0.0.1:8000/api/spy_cats/
- DELETE: http://127.0.0.1:8000/api/spy_cats/2/

### Missions
- GET: http://127.0.0.1:8000/api/missions/2/
- GET: http://127.0.0.1:8000/api/missions/
- DELETE: http://127.0.0.1:8000/api/missions/1/
- POST: http://127.0.0.1:8000/api/missions/
- PATCH: http://127.0.0.1:8000/api/missions/2/assign_cat/
- PATCH: http://127.0.0.1:8000/api/missions/2/complete_target/
- PATCH: http://127.0.0.1:8000/api/missions/1/update_target_notes/
- PATCH: http://127.0.0.1:8000/api/missions/1/remove_cat/
