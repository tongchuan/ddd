如果你在 Mac OS X 或 Linux 下，下面两条命令可能会适用:.
sudo easy_install virtualenv
或更好的:
sudo pip install virtualenv
上述的命令会在你的系统中安装 virtualenv。它甚至可能会存在于包管理器中， 如果你用的是 Ubuntu，可以尝试:
sudo apt-get install python-virtualenv


mkdir myproject
cd myproject
virtualenv venv

现在，无论何时你想在某个项目上工作，只需要激活相应的环境。在 OS X 和 Linux 上，执行如下操作:
. venv/bin/activate
下面的操作适用 Windows:
venv\scripts\activate

pip install Flask
全局安装
sudo pip install Flask

如果你需要最新版本的 Flask，有两种方法：你可以使用 pip 拉取开发版本， 或让它操作一个 git checkout。无论哪种方式，依然推荐使用 virtualenv。

git clone http://github.com/mitsuhiko/flask.git
cd flask
virtualenv venv --distribute
. venv/bin/activate
python setup.py develop
没有 git 时，获取开发版本的替代操作:
mkdir flask
cd flask
virtualenv venv --distribute
. venv/bin/activate
pip install Flask==dev
