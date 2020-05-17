# Pycon Flask Example

AN example of deploying a simple flask/ginja2 web app using the serverless framework and aws lambda + api gateway


## Serverless Dependancies

```
npm install -g serverless

npm install --save serverless-wsgi

npm install serverless-domain-manager --save-dev
```

## Setup Local

```
npm run setup
```

(assumes virtualenvwrapper setup and osx path to python3)

```
mkvirtualenv --python=/usr/local/bin/python3 pycon-flask-example
```

## Run Local

```
workon pycon-flask-example (not required straight after mkvirtualenv)

pip install -r requirements.txt

pip install -r requirements_local.txt

export AWS_ACCESS_KEY_ID=#########
export AWS_SECRET_ACCESS_KEY=##########
export AWS_DEFAULT_REGiON=ap-southeast-2
export PYCON_EXAMPLE_URL=######

sls wsgi serve -p 8000
```

or to use aws profiless

```
export PYCON_EXAMPLE_URL=######
AWS_PROFILE=dcl sls wsgi serve -p 8000
```

can add stages as defined in the yaml

```
export PYCON_EXAMPLE_URL=######
AWS_PROFILE=dcl sls wsgi serve -p 8000 -s prod
```

## Deploy

```
export PYCON_EXAMPLE_URL=######
```
```
sls deploy
```
```
AWS_PROFILE=dcl sls deploy
```
```
AWS_PROFILE=dcl sls deploy -s prod
```

# Tear Down

```
sls remove
```
```
AWS_PROFILE=dcl sls remove
```
```
AWS_PROFILE=dcl sls deploy -s prod
```
```