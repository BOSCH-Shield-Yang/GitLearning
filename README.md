# GitLearning

Learn how to use basic git command :)

We will quickly develope a small program to test :
- manage a local repository : init, branch ...
- work with a remote repostory : clone, pull, push, fetch...

# Install Git
check your git version
```bash
git --version
```
# Start from a loacl repository
Before init a local repository, let others know who you are:
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
git config --list
```

## 1. Init a loacl repository
1. init local repository
```bash
mkdir GitLearning && cd GitLearning
git init
```
2. create a readme file
```bash
touch readme.md
```

## 2. Add and Commit
```bash
git add readme.md
git commit -m "[FILE UPLOAD] Upload readme"
```

## 3. Work on your own branch
1. List current work branch / remote branch / all branches
```bash
git branch
git branch -r
git branch -a
```
2. creat & swith branch
```bash
# Create a new branch
git branch <branch name>
# Switch to the new branch
git checkout <branch name>

# Create and switch to new branch
git checkout -b <branch name>
```
......

# Work on remote repository

## 1. Clone a remote repository
```bash
git clone <remote-repository-link>
git clone -b <branch-name> <remote-repo-url>
```
> Use ssh for authentication:
> [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
> [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
> Generate a ssh key
> ```bash
> ssh-keygen -t ed25519 -C "your_email@example.com"
> ```




# Resources
[1. Git Official Site](https://git-scm.com/)
[2. Learn how to manage branch](https://learngitbranching.js.org/?locale=zh_CN)
[3. Git教程 - 寥雪峰](https://www.liaoxuefeng.com/wiki/896043488029600)

# hello this is amiya