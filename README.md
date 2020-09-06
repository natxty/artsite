# artsite  
Base structure for an artist's portfolio site, with simple extras (like blog/news, etc) and a tracker for provenance

## Running Locally

### quickstart
```bash
cd /path/to/johno-site
source ~/.venv/johno/bin/activate

python manage.py runserver
```

### Setting up your venv

```bash
# requires python 3 for our Django 3 apps
python3 -m venv ~/.venv/johno
. ~/.venv/johno/bin/activate

# confirm:
$ which python
/Users/natxty/.venv/johno/bin/python

```

### getting fixtures off heroku
```bash
# full dump:
heroku run python manage.py dumpdata # goes to stdout
 
# per app example:
heroku run python manage.py dumpdata gallery > artsite/fixtures/gallery.json
```

### loading fixtures
```bash
python manage.py loaddata # fixture dir?
```

## Deploying to Heroku

## Config

### Configure/confirm your heroku add-ons:

### Get the ENV config set:
```bash
# Your AWS security credentials:
$ heroku config:add AWS_ACCESS_KEY_ID=xxx
$ heroku config:add AWS_SECRET_ACCESS_KEY=xxx
$ heroku config:add AWS_STORAGE_BUCKET_NAME=xxx

# Replace 'woot' with the name of your project:
$ heroku config:add DJANGO_SETTINGS_MODULE=woot.settings.prod

# A random long (40 characters or so) string:
$ heroku config:add SECRET_KEY=xxx

# Email setup (these seem to be added immediately when adding mailgun)
$ heroku config:add EMAIL_HOST=xxx
$ heroku config:add EMAIL_HOST_PASSWORD=xxx
$ heroku config:add EMAIL_HOST_USER=xxx
$ heroku config:add EMAIL_PORT=xxx
```

```bash
# scale up a dyno (confirm):
heroku scale web=1

# check dynos // processes:
$ heroku ps
Free dyno hours quota remaining this month: 2950h 0m (100%)
Free dyno usage for this app: 0h 0m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

=== web (Free): gunicorn -c gunicorn.py.ini wsgi:application (1)
web.1: up 2020/09/01 11:40:20 -0700 (~ 4h ago)
```

Ensure we migrate on release:
```bash
# added as 1st line to Procfile:
release: python manage.py migrate
```


### collectstatic
This command copies the static files into whatever settings set for `STATIC_ROOT`.

```bash
# you can run with --dry-run to see what will be copied
python manage.py collectstatic --dry-run

# running locally will copy from artiste/media => artsite/static
# running with prod settings should copy from artiste/media => s3 bucket
# compress and then upload all your static assets to Amazon S3 (css, js, images, etc.).
$ heroku run python manage.py collectstatic --noinput
$ heroku run python manage.py compress

```


## Misc

### psql to heroku database
```bash
[base] natxty:~/heroku/johno-site (upgrade *+%)   heroku pg:psql
--> Connecting to giggling-stably-5086
psql (12.3, server 12.4 (Ubuntu 12.4-1.pgdg16.04+1))
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

johno-site::HEROKU_POSTGRESQL_CHARCOAL=> 
```


# Dev - Stage

* push to johno-dev
* run syncdb? run migrations?
* run collectstatic?
