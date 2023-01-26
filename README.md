# CRUD_multiapp
Project created to develop skills in the field of django framework, docker, app building and DevOPS principles.

In short it should transform into Microservices app


## How to run in DEBUG mode.

### To download the project directly from Github:

---
1. Open ,,Code" tab

![obraz](https://user-images.githubusercontent.com/70173732/214968414-7b81b2e9-723e-4d86-84a2-25dbddfa3d2c.png)

2. Copy this part

![obraz](https://user-images.githubusercontent.com/70173732/214968592-b5b5d996-ae6c-468b-8507-c6d76c831f3d.png)

3. Paste it into terminal window after "git clone" 
#### Shhh. Remember that you need to press ctrl+l_shift+v to paste it into regular terminal. Or something like this
---

## Final command should look like:
```
git clone git@github.com:Kotmin/CRUD_multiapp.git
```

## We highly recoment do use for this purpose an virtual environment python
### Python has two main virtual env managers: venv and conda. We'll focus at first one.
## To create simple venv

Just run
```
python -m venv
```
## To log in into (pattern "source ENVName/bin/activate")
For us that should be
```
source venv/bin/activate

```
Sometimes the path should be slightly different like venv/Scripts/activate

Right now name of our env should appear
![obraz](https://user-images.githubusercontent.com/70173732/214974119-eb83b9fb-9bcb-44ec-b256-19d172491aeb.png)

Congratulation you're working now in semi-separated environment. Hmmmm you don't have any strong separation sooo be carefull. Just read the docs what that exactly is. And the most important part. Have Fun!

## To exit 
```
deactivate
```





## Project requirements
- Python3 at least 3.6
- Django version 3.2.16
