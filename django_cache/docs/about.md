# Django Cache Project

#### Training Exercies

- Site Developed to practice Celery Tasks and Django Cache options.

#### Tools used

- Redis server used as broker.
- Celery Beat used for scheduled tasks.
- Flower used to view tasks.
- DRF used for API

An endpoint was created that took a some number of Blog sites to be made, this was then based to a Celery Taks that would use faker to make x number of blogs.

Flower was used to view tasks being deployed.

After creating an endpoint that could take time to process x number of blogs, the need for cacheing was created. Cacheing would be needed to view the large number of blogs after hitting the create x number of blogs endpoint.
