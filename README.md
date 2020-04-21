# Automating Project Initialization ![Author -Rehan Khan](https://img.shields.io/badge/Author-Rehan%20Khan-blue)

For MAC USERS:

## Tired of doing that same project initialization every single time while creating a project? Not anymore!!!

# Install:

## Note:-

- Install it in your home-directory eg: `/User/Your-homedirectory`
- !Important "After your installment of the respectives mentioned in requirements.txt, you will also need chrome driver" so install that too in your home-directory, for installation [Click here](https://chromedriver.chromium.org/)

```
git clone "https://github.com/khan-rehan/Automation_projectInitialization.git"
cd Automation_projectInitialization

pip install -r requirements.txt

source ~/.my_commands.sh

Then go to create.py and set the username and password to be your username and password also, in .my_custom_commands.sh  on line:8 put your github remote url, for detailed explanation on this take a look below👇🏻👇🏻👇🏻

Also make sure to change all directories to your directories so it should be '/Users/<your username>/path/to/your/project'
```

## Adding of github remote url in command script:

For https:- `git remote add origin https://github.com/USERNAME/$1.git`

For SSH:- `git remote add origin git@github.com:USERNAME/$1.git`

By default, its `https` for all if, still if you wanna check on about your github go to Github `SSH & GPG keys` in settings.

Refer, `Click on Reference 3` for further detailed explanation.

# Usage:

```
To run the script type in 'create <name of your folder/repo>' in your terminal
```

## To run this python script permanently for automating project initialization, read `Reference 1`.

Refereneces used to create this python script:

[Referenece 1](https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e) # creating a shell script

[Reference 2](https://askubuntu.com/questions/430196/how-to-pass-arguments-to-functions-while-executing-a-python-script-from-terminal) # pass arguments to functions while executing a python script from terminal

[Reference 3](https://help.github.com/en/github/using-git/changing-a-remotes-url) # Github remote url

[Reference 4](https://github.com/PyGithub/PyGithub) # For Github API script
