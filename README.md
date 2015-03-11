# [Bone App](bone.pewen.tk)

## Table of contents

- [Installation and configuration](#installation and configuration)
- [Hosting](#hosting)
- [Team](#team)
- [License](#license)

##Installation and configuration

###Python dependence

If you going to run in your PC, I recomend use a virtual enviroment. I use [conda](https://store.continuum.io/cshop/anaconda/) for this. If you never work with virtual envirionmet, read [this](http://conda.pydata.org/docs/faq.html#environments) can help you. In this example, the virtual enviroment is called `boneEnv`.
Else, go directly to step 2.

1. Create a virtual environment 

        $ conda create -n boneEnv python=2.7 pip
		# To activate this environment, use:
        $ source activate boneEnv

2. To install all python requeriments in this enviroment

        (boneEnv) $ pip install -r requerimets.txt
		# To deactivate this environment, use:
        (boneEnv) $ source deactivate

###HowTo enable the Drive API

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Select a project, or create a new one.
3. In the sidebar on the left, expand **APIs & auth**. Next, click **APIs**. In the list of APIs, make sure the status is **ON** for the *Drive API* and *Drive SDK*.
4. In the sidebar on the left, select **Credentials**.
5. Under OAuth, click Create New Client ID.
6. Select Web application and click Create Client ID.

    - In Redirect URIs put `http://a.b.com:8000/oauth2callback`
	- In Sources JavaScript put `http://a.b.com:8000`
	- Create Cliente ID

7. In **wsgi/route.py** remplace **YOUR_CLIENT_ID** with the **Client ID** and **YOUR_CLIENT_SECRET** with your **Client Secret**, both generated previously.

Now, in your pc do:

1. `$ sudo emcas /etc/hosts`
2. Change the firts line to: `127.0.0.1 localhost a.b.com`

The latter is done by Google's security policies.

###Run

- `cd boneApp`
- `python runServer.py` 
    * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
    * Restarting with stat

##Hosting

I recomend host the application in [OpenShift](https://www.openshift.com/), because we can, free, host own application in the public cloud. It also gives us the complet control over a VM with Redhats. The `/boneApp/wsgi/application` is for run automatically in OpenShift.

###Start Up

1. [Creater](https://www.openshift.com/app/account/new) a account.
2. Creater a new application and select **python2.7**
3. In `Source Code`put `https://github.com/fnbellomo/boneApp`
4. And it's ready!!


##Team

###Core Team
* [@fnbellomo](http://twitter.com/fnbellomo)
* [@dbellomo](http://twitter.com/dbellomo)
* [@ucaomo](http://twitter.com/ucaom)

###Thanks to:
* [@Lisax525](http://twitter.com/Lisax525) for helping in the colors of the application

##License

All the code is licensed under the MIT License, and this work is licensed under a Creative Commons Attribution 4.0 International License.
