## DJANGO AND Chart.js

## how to install
    open terminal or cmd
    mkdir django_chart
    git clone https://github.com/luggiestar/django_chart
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    on your browser url write 127.0.0.1:8000
    
Example of available model

``` python
class Club(models.Model):
    name = models.CharField(max_length=60, unique=True)
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name