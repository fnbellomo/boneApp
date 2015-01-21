# Bone App

##HowTo install Bower and the JS libraries (in Debian)

1. First, we need install [Node.JS](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager). Like sudo, we do:

        # apt-get install curl
        # curl -sL https://deb.nodesource.com/setup | bash -
        # apt-get install -y nodejs

2. Now, install [Bower](http://bower.io/):

        $ sudo npm install -g bower

##Install Python dependence

	$ HACER EL requerimets.txt
    $ pip install requerimets.txt

##Enable the Drive API

Usar como guia para escribir este link: https://developers.google.com/drive/web/quickstart/quickstart-python

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Select a project, or create a new one.
3. In the sidebar on the left, expand **APIs & auth**. Next, click **APIs**. In the list of APIs, make sure the status is **ON** for the *Drive API* and *Drive SDK*.
4. In the sidebar on the left, select **Credentials**.
    1. In either case, you end up on the **Credentials** page and can create your project's credentials from here.
    2. If you haven't done so already, create your OAuth 2.0 credentials by clicking **Create new Client ID** under the **OAuth** heading. Next, look for your application's client ID and client secret in the relevant table. You may also create and edit redirect URIs from this page.

5. In **wsgi/route.py** remplace **YOUR_CLIENT_ID** with the **Client ID** and **YOUR_CLIENT_SECRET** with your **Client Secret**, both generated previously.

TENGO QUE ACLARAR LO DE REDIRECT_URI, QUE TUBE QUE AGREGAR A MI DNS PARA QUE FUNCIONE.
