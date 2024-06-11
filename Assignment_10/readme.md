<!-- برای فعال کردن گیت هاب در محیط vscode این مراحل را انجام دهید: -->
- [ ] In this work we run a machine learning task to predict weight based on the height of a person from scratch.

##for active push code in vs cod via terminal vs code follow these steps:

1. Check for existing keys-
```
a. ls -al ~/.ssh
```
2. Create a key if it does not exist.
Paste the text below and substitute it with your GitHub email address.
```
a. ssh-keygen -t ed25519 -C "your_email@example.com"
```
b. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
```
c. At the prompt, type a secure passphrase.
```
3. Adding your SSH key to the SSH agent.
Fire up the SSH agent and add the key.

```
a. eval `ssh-agent -s`
b. ssh-add ~/.ssh/id_ed25519
4. Adding key to GitHub account.
```
Pull up the key and add it to the GitHub account.

```
a. cat ~/.ssh/id_ed25519.pub
b. Navigate to the GitHub account and add the key.
```
- [X] Hooray! now you should be able to push files to your GitHub account.


<!-- اگر خطای نبودن ریپازیتوری را داد از این دستور استفاده کنید: -->
- [X] if get this error:(you have not repository)  so you type this command in terminal:
```
git remote set-url origin https://github.com/<user_name>/<repo_name>.git
```

First, in the action section for my repository, we run the Python package to create the first YAML file and then Python-publishes to create a second YAML file.
In the secret code section, we put the value of API-TOKEN-PYPI.

##In the lower part, you can see two images of the Python package before and after it was published in PYPI:

![1](https://github.com/mori-cyber/pythonpackge_morteza/assets/65276280/b0430046-78fb-4439-b9c2-1fab05e1338d)
